import io, re, subprocess
import requests, trafilatura
from pypdf import PdfReader
from common import *
def download(url,path):
 partial=path.with_suffix(path.suffix+'.part')
 with requests.get(url,stream=True,timeout=90) as response:
  response.raise_for_status()
  with open(partial,'wb') as f:
   for block in response.iter_content(1024*1024):f.write(block)
 partial.replace(path)
def main():
 r=runarg()
 with Stage('extract_content',r) as st:
  rows=stdin();st.data['input_count']=len(rows);st.data['tools_or_models']=['requests','trafilatura','yt-dlp','faster-whisper/small.en']
  for x in rows:
   try:
    folder=ROOT/'data/media'/x['item_id'];folder.mkdir(parents=True,exist_ok=True)
    previous=subprocess.run(['bash','data/store.sh','get',x['item_id']],capture_output=True,text=True)
    old=json.loads(previous.stdout) if previous.returncode==0 else None
    # Reuse stored media by identity/URL. This is a cache assumption, not proof that remote bytes never change.
    if old and x['kind']!='feed' and old.get('media_url')==x.get('media_url'):
     text=safe(old['text_path']).read_text();segments=read(safe(old['segments_path']))
    elif x['kind']=='feed':
     url=x['url'];segments=None
     if 'arxiv.org/abs/' in url:
      url=url.replace('/abs/','/html/')
     response=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=60)
     if response.status_code!=200 and 'arxiv.org' in x['url']:
      response=requests.get(x['url'].replace('/abs/','/pdf/'),timeout=90);response.raise_for_status()
      text='\n'.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(response.content)).pages)
     else:
      response.raise_for_status();text=trafilatura.extract(response.text,include_tables=True,include_links=True) or ''
     rawhash=digest(response.content.hex());(folder/(rawhash+'.source')).write_bytes(response.content)
     if len(text)<1000:raise RuntimeError('Substantive full text unavailable (not accepting an abstract)')
     original=re.search(r'I first published this [^.\n]{0,80}? on ([A-Z][a-z]+ \d{1,2}, \d{4})',text)
     if original:
      x['known_original_date']=dt.datetime.strptime(original[1],'%B %d, %Y').date().isoformat()
      x['publication_date_evidence']=original[0]
      x['published_at']=None # The original calendar date is known, but its timestamp/timezone is not.
    else:
     segments=[]
     if x['kind']=='youtube':
      target=str(folder/'source.%(ext)s')
      p=subprocess.run([str(ROOT/'.venv/bin/yt-dlp'),'--no-playlist','-f','bestaudio/best','--write-subs','--write-auto-subs','--sub-langs','en','--sub-format','json3','-o',target,x['url']],capture_output=True,text=True,timeout=600)
      if p.returncode:
       print('Subtitles unavailable; retrying audio-only for local transcription',file=sys.stderr)
       p=subprocess.run([str(ROOT/'.venv/bin/yt-dlp'),'--js-runtimes','node','--no-playlist','-f','bestaudio/best','-o',target,x['url']],capture_output=True,text=True,timeout=600)
       if p.returncode:raise RuntimeError(p.stderr[-1200:])
      subs=list(folder.glob('*.en.json3'))
      if subs:
       for e in read(subs[0]).get('events',[]):
        t=''.join(z.get('utf8','') for z in e.get('segs',[])).strip()
        if t:segments.append(dict(segment_id=f's{len(segments):05}',start_seconds=e['tStartMs']/1000,end_seconds=(e['tStartMs']+e.get('dDurationMs',1000))/1000,text=t))
      audio=next((p for p in folder.glob('source.*') if p.suffix in ['.webm','.m4a','.mp4','.opus','.mp3']),None)
     else:
      audio=folder/'source.mp3'
      if not audio.exists():download(x['media_url'],audio)
     if not segments and x['kind']=='podcast':
      try:
       page=requests.get(x['url'],timeout=45);page.raise_for_status()
       transcript=trafilatura.extract(page.text) or ''
      except requests.RequestException as e:
       print('Publisher transcript unavailable; using downloaded audio: '+str(e),file=sys.stderr)
       transcript=''
      matches=list(re.finditer(r'(?m)^([^\n]{1,80}) \[(\d{2}):(\d{2}):(\d{2})\]:',transcript))
      if len(matches)>20:
       for current,nxt in zip(matches,matches[1:]):
        start=int(current[2])*3600+int(current[3])*60+int(current[4]);end=int(nxt[2])*3600+int(nxt[3])*60+int(nxt[4])
        if end>start:
         segments.append(dict(segment_id=f's{len(segments):05}',start_seconds=start,end_seconds=end,text=transcript[current.end():nxt.start()].strip()))
       (folder/'publisher-transcript.html').write_text(page.text)
     if not segments:
      if not audio:raise RuntimeError('No downloaded audio')
      from faster_whisper import WhisperModel
      model=WhisperModel('small.en',device='cpu',compute_type='int8')
      transcribed,_=model.transcribe(str(audio),beam_size=3,vad_filter=True)
      for s in transcribed:segments.append(dict(segment_id=f's{len(segments):05}',start_seconds=float(s.start),end_seconds=float(s.end),text=s.text.strip()))
     if not segments:raise RuntimeError('Empty transcript')
     text='\n'.join(s['text'] for s in segments)
    version=digest({'title':x['title'],'url':x['url'],'published_at':x['published_at'],'publisher_id':x['publisher_id'],'kind':x['kind'],'text':text,'segments':segments})
    asset=Path('data/assets')/x['item_id']/version;asset.mkdir(parents=True,exist_ok=True)
    (asset/'text.txt').write_text(text)
    if segments is not None:write(asset/'segments.json',segments)
    x.update(version_id=version,text_path=str(asset/'text.txt'),segments_path=str(asset/'segments.json') if segments is not None else None)
    emit(x);st.data['output_count']+=1
   except Exception as e:st.error(f"{x['item_id']} {x['title']}: {e}")
 st.finish()
entry(main)
