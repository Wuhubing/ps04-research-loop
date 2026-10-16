import calendar, datetime as dt, re, time
import feedparser, requests
from common import *
def fetch(kind):
 r=runarg()
 with Stage('collect_'+kind,r) as st:
  st.data['tools_or_models']=['requests','feedparser']
  for source in read(r/'config/sources.json'):
   if source['kind']!=kind:continue
   st.data['input_count']+=1
   try:
    response=requests.get(source['url'],headers={'User-Agent':'Mozilla/5.0 ResearchLoop/0.1'},timeout=45)
    if response.status_code==429:
     time.sleep(5)
     response=requests.get(source['url'],headers={'User-Agent':'Mozilla/5.0'},timeout=45)
    response.raise_for_status()
    raw=response.content
    write(r/'discovery'/f"{source['source_id']}.json",{'url':source['url'],'retrieved_at':now(),'body':response.text})
    feed=feedparser.parse(raw)
    if feed.bozo and not feed.entries:raise RuntimeError('Malformed feed')
    count=0
    for e in feed.entries:
     title=e.get('title',''); url=e.get('link','')
     if source.get('match') and not re.search(source['match'],title+' '+url,re.I):continue
     if count>=source.get('limit',20):break
     date=e.get('published_parsed')
     published=dt.datetime.fromtimestamp(calendar.timegm(date),dt.timezone.utc).isoformat().replace('+00:00','Z') if date else None
     media=next((x.get('href') for x in e.get('enclosures',[]) if x.get('type','').startswith('audio/')),None)
     if kind=='podcast' and not media:continue
     ident=e.get('id',url)
     if 'arxiv.org' in url:
      url=re.sub(r'v\d+$','',url.replace('http:','https:')); ident=url
     row=dict(item_id=source.get('identity_aliases',{}).get(ident,digest(ident)[:24]),source_id=source['source_id'],publisher_id=source.get('publisher_overrides',{}).get(url,source['publisher_id']),kind=kind,title=title,url=url,published_at=published,retrieved_at=now(),media_url=media)
     row['discovered_updated_at']=e.get('updated');row['discovery_method']='syndication'
     emit(row);count+=1;st.data['output_count']+=1
   except Exception as e:
    st.error(f"{source['source_id']}: {e}")
    # Optional original-page metadata recovery is supplemental web collection,
    # explicitly not counted as successful RSS discovery.
    for url in source.get('fallback_urls',[]):
     try:
      from lxml import html
      page=requests.get(url,timeout=45);page.raise_for_status();tree=html.fromstring(page.content)
      title=tree.xpath('//meta[@name="citation_title"]/@content')[0]
      history=tree.xpath('//div[contains(@class,"submission-history")]')
      history_text=history[0].text_content() if history else tree.text_content()
      stamp=re.search(r'\[v1\]\s*(\w{3},\s*\d{1,2} \w{3} \d{4} \d{2}:\d{2}:\d{2} UTC)',history_text)
      if not stamp:raise RuntimeError('Original submission timestamp unavailable')
      published=dt.datetime.strptime(stamp[1],'%a, %d %b %Y %H:%M:%S UTC').isoformat()+'Z'
      row=dict(item_id=digest(url)[:24],source_id=source['source_id'],publisher_id=source.get('publisher_overrides',{}).get(url,source['publisher_id']),kind='feed',title=title,url=url,published_at=published,retrieved_at=now(),media_url=None,discovery_method='direct_metadata_fallback')
      write(r/'discovery'/(row['item_id']+'-fallback.json'),{'url':url,'html':page.text,'reason':'Feed unavailable; original-page metadata recovery'})
      emit(row);st.data['output_count']+=1
     except Exception as fallback_error:st.error(str(fallback_error))
 st.finish()
