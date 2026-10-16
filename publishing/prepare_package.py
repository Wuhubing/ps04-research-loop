import shutil,re
from common import *
sys.path.insert(0,str(ROOT/'review'))
from check_content import assess
def main():
 r=runarg()
 with Stage('prepare_package',r) as st:
  current=assess(r);approval=read(r/'approval.json')
  if not current['passed'] or approval.get('review_id')!=current['review_id'] or approval.get('decision')!='approve':raise RuntimeError('Current passing review and matching student approval required')
  for k in ['reviewer','reviewed_at','notes']:
   if not approval.get(k):raise ValueError('Missing approval '+k)
  dest=r/'package';dest.mkdir(exist_ok=True);assets=[]
  for kind in ['articles','video_scripts']:
   for m in lines(r/(kind+'.jsonl')):
    target=dest/(kind+'-'+m['piece_id']+'.md');shutil.copyfile(safe(m['path']),target);assets.append(dict(piece_id=m['piece_id'],path=str(target.relative_to(ROOT))))
    if kind=='video_scripts':
     chunks=re.findall(r'\*\*Narration:?\*\*:?\s*(.*?)(?=\*\*Visual:?\*\*)',target.read_text(),flags=re.S)
     if chunks:
      narration='\n\n'.join(re.sub(r'<!--.*?-->','',s,flags=re.S).strip() for s in chunks)
      captions=dest/('subtitle-text-'+m['piece_id']+'.txt');captions.write_text(narration+'\n');assets.append(dict(piece_id=m['piece_id'],path=str(captions.relative_to(ROOT)),note='Approved narration text; align caption timings to the actual rendered video.'))
  index={(x['item_id'],x['version_id']):x for x in lines(r/'eligible.jsonl')}
  for b in lines(r/'briefs.jsonl'):
   notes=[]
   for c in b['claims']:
    notes.append('## '+c['claim_id']+'\n'+c['statement'])
    for ref in c['evidence']:
     x=index[(ref['item_id'],ref['version_id'])];loc=ref['locator']; detail=loc.get('quote','')
     if loc['type']=='segment':
      segment=next(s for s in read(safe(x['segments_path'])) if s['segment_id']==loc['segment_id'])
      detail=f"{segment['start_seconds']:.1f}–{segment['end_seconds']:.1f} seconds: {segment['text']}"
     notes.append(x['title']+' — '+x['url']+'\n'+detail)
   path=dest/('sources-'+b['piece_id']+'.md');path.write_text('\n\n'.join(notes));assets.append(dict(piece_id=b['piece_id'],path=str(path.relative_to(ROOT))))
  pending=['Produce three videos in Google Vids','Publish free Substack articles','Upload YouTube videos as unlisted','Add reciprocal links and citations','Record separate narrated technical demonstration']
  published=read(r/'publication_links.json') if (r/'publication_links.json').exists() else {}
  if isinstance(published,dict):
   if all(published.get('substack',{}).get(p) for p in ['01','02','03']):pending.remove('Publish free Substack articles')
   if all(published.get('youtube',{}).get(p) for p in ['01','02','03']):pending.remove('Upload YouTube videos as unlisted')
   if published.get('reciprocal_links_verified'):pending.remove('Add reciprocal links and citations')
   production=[read(r/f'video_{p}_production.json') if (r/f'video_{p}_production.json').exists() else {} for p in ['01','02','03']]
   if all(x.get('cloud_production_url') for x in production):
    pending.remove('Produce three videos in Google Vids')
    pending.append('Confirm course acceptance of locally rendered videos 02/03 imported into Google Vids; preserve exact production provenance')
   if not published.get('signed_out_access_verified'):pending.append('Verify published links signed out')
   if not all(x.get('human_source_listening') for x in production):pending.append('Student verifies original source audio excerpts')
  manifest=dict(review_id=current['review_id'],assets=assets,remaining_manual_actions=pending)
  write(dest/'manifest.json',manifest)
  if not (dest/'publication_links.json').exists():write(dest/'publication_links.json',[dict(piece_id=p,substack_url=None,youtube_url=None) for p in ['01','02','03']])
  emit(manifest);st.data['output_count']=len(assets)
entry(main)
