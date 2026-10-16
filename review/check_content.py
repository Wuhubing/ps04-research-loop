import datetime as dt, re
from common import *
sys.path.insert(0,str(ROOT/'processing'))
from filter_items import exclusion
def assess(r):
 issues=[];finger={};seen=set();used={};manifests={}
 def issue(artifact,msg,severity='error'):issues.append(dict(artifact=artifact,severity=severity,explanation=msg))
 def load(name,islines=False):
  p=r/name
  if not p.exists():issue(name,'Missing artifact');return [] if islines else {}
  finger[name]=p.read_text();return lines(p) if islines else read(p)
 meta=load('run.json');eligible=load('eligible.jsonl',True);briefs=load('briefs.jsonl',True);decisions=load('decisions.jsonl',True)
 index={(x['item_id'],x['version_id']):x for x in eligible};accepted={(x['item_id'],x['version_id']) for x in decisions if x['decision']=='accept'}
 asof=dt.date.fromisoformat(meta['as_of_date'])
 distinct={x['item_id']:x for x in eligible}
 if len(distinct)<12:issue('eligible.jsonl','Need 12 distinct eligible items')
 if len({x['publisher_id'] for x in distinct.values()})<6:issue('eligible.jsonl','Need six independent source groups')
 if sum(x['kind']=='feed' and x.get('discovery_method')=='syndication' for x in distinct.values())<2:issue('eligible.jsonl','Need two substantive written items actually discovered from RSS/Atom, not metadata fallback')
 for kind in ['feed','youtube','podcast']:
  if sum(x['kind']==kind for x in distinct.values())<2:issue('eligible.jsonl','Need at least two '+kind+' items')
 if sorted(x['piece_id'] for x in briefs)!=['01','02','03']:issue('briefs.jsonl','Need exactly three unique briefs')
 if len({x['argument'] for x in briefs})!=3:issue('briefs.jsonl','Arguments must differ')
 for b in briefs:
  pubs=set();pid=b['piece_id']
  if not b['synthesis'] or not b['limitations']:issue(pid,'Missing synthesis or limitation')
  if not b['claims']:issue(pid,'No claims')
  for c in b['claims']:
   if c['claim_id'] in seen:issue(pid,'Duplicate claim ID')
   seen.add(c['claim_id'])
   if not c['evidence']:issue(pid,'Unsupported claim '+c['claim_id'])
   for ref in c['evidence']:
    key=(ref['item_id'],ref['version_id']);x=index.get(key)
    if x is None or key not in accepted:issue(pid,'Reference missing or not accepted');continue
    pubs.add(x['publisher_id']);used[key]=x
    if exclusion(x['published_at'],asof):issue(pid,'Reference outside date window')
    try:
     text=safe(x['text_path']).read_text();finger[x['text_path']]=text;loc=ref['locator']
     if loc['type']=='text':
      if not loc['quote'].strip() or loc['quote'] not in text:issue(pid,'Quote not found in saved text')
     else:
      segments=read(safe(x['segments_path']));finger[x['segments_path']]=segments
      seg=next((s for s in segments if s['segment_id']==loc['segment_id']),None)
      if not seg or seg['end_seconds']<=seg['start_seconds']:issue(pid,'Invalid media segment')
    except Exception as e:issue(pid,'Unreadable evidence: '+str(e))
  if len(pubs)<3:issue(pid,'Fewer than three independent sources')
 for kind in ['feed','youtube','podcast']:
  if not any(x['kind']==kind for x in used.values()):issue('series','No cited '+kind+' evidence')
 for name in ['articles','video_scripts']:
  rows=load(name+'.jsonl',True)
  if sorted(x['piece_id'] for x in rows)!=['01','02','03']:issue(name,'Need three manifests')
  for m in rows:
   try:
    p=safe(m['path']);text=p.read_text();finger[m['path']]=text
    expected={c['claim_id'] for b in briefs if b['piece_id']==m['piece_id'] for c in b['claims']}
    if set(m['claim_ids'])!=expected:issue(m['path'],'Manifest claim mismatch')
    if any(c not in text for c in expected):issue(m['path'],'Missing claim markers')
    if meta['as_of_date'] not in text:issue(m['path'],'Missing as-of date')
    expected_start=(asof-dt.timedelta(days=29)).isoformat()
    for start,end in re.findall(r'Publication window:[\s*`]*(\d{4}-\d{2}-\d{2})[–—](\d{4}-\d{2}-\d{2})',text):
     if (start,end)!=(expected_start,asof.isoformat()):issue(m['path'],'Publication window disagrees with actual UTC run date')
    for date in re.findall(r'window[^\n]{0,40}?ending ([A-Z][a-z]+ \d{1,2}, \d{4})',text):
     if dt.datetime.strptime(date,'%B %d, %Y').date()!=asof:issue(m['path'],'Narrative window ending date disagrees with run')
    if 'https://' not in text:issue(m['path'],'Missing audience-facing source links')
    body=re.sub(r'<!--.*?-->','',text.split('## References')[0],flags=re.S)
    body=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',body)
    if name=='video_scripts':
     narration=re.findall(r'\*\*Narration:?\*\*:?\s*(.*?)(?=\*\*Visual:?\*\*)',body,flags=re.S)
     if narration:body='\n'.join(narration)
    words=len(re.findall(r"\b[\w'-]+\b",body))
    low,high=(600,900) if name=='articles' else (390,750)
    if not low<=words<=high:issue(m['path'],f'Approximate length {words} words; target {low}–{high}','warning')
   except Exception as e:issue(name,str(e))
 issue('human_review','Verify interpretation, independence, article/script factual consistency, counterarguments, and quoted audio against the original.','warning')
 return dict(review_id=digest(finger),passed=not any(i['severity']=='error' for i in issues),issues=issues)
def main():
 r=runarg()
 with Stage('check_content',r) as st:
  result=assess(r);emit(result);st.data['output_count']=1
if __name__=='__main__':entry(main)
