"""Run each independent piece against its own evidence-linked brief."""
from concurrent.futures import ThreadPoolExecutor
from common import *
from model import *
def brief_evidence(brief,rows):
 """Draft from cited passages plus context; full artifacts remain preserved and selection/briefing use full content."""
 views=[]
 for x in rows:
  refs=[e['locator'] for c in brief['claims'] for e in c['evidence'] if (e['item_id'],e['version_id'])==(x['item_id'],x['version_id'])]
  if not refs:continue
  view={**x,'excerpted_for_drafting':True,'full_evidence_location':x['text_path']}
  if x['segments_path']:
   segments=read(safe(x['segments_path']));selected={i for i,s in enumerate(segments) if any(loc.get('segment_id')==s['segment_id'] for loc in refs)}
   context={j for i in selected for j in range(max(0,i-1),min(len(segments),i+2))}
   view.update(text=None,segments=[s for i,s in enumerate(segments) if i in context])
  else:
   text=safe(x['text_path']).read_text();spans=[]
   for loc in refs:
    q=loc.get('quote','');i=text.find(q)
    if not q or i<0:raise RuntimeError('Brief quote missing from preserved evidence')
    spans.append((max(0,i-1500),min(len(text),i+len(q)+1500)))
   merged=[]
   for start,end in sorted(spans):
    if merged and start<=merged[-1][1]:merged[-1]=(merged[-1][0],max(end,merged[-1][1]))
    else:merged.append((start,end))
   view.update(text='\n\n[Non-cited intervening material omitted from drafting context]\n\n'.join(text[a:b] for a,b in merged),segments=None)
  views.append(view)
 return views
def generate(stage,foldername):
 r=runarg()
 with Stage(stage,r) as st:
  briefs=stdin();st.data['input_count']=len(briefs)
  rows=lines(r/'eligible.jsonl')
  def one(b):
   if b['piece_id'] not in ['01','02','03']:raise ValueError('Invalid piece ID')
   ids={(e['item_id'],e['version_id']) for c in b['claims'] for e in c['evidence']}
   result=call(r,stage,{'brief':b,'as_of_date':read(r/'run.json')['as_of_date'],'evidence':brief_evidence(b,[x for x in rows if (x['item_id'],x['version_id']) in ids])},obj({'markdown':S}))
   path=r/foldername/(b['piece_id']+'.md');path.parent.mkdir(exist_ok=True);path.write_text(result['markdown'])
   return dict(piece_id=b['piece_id'],path=str(path.relative_to(ROOT)),claim_ids=[c['claim_id'] for c in b['claims']])
  with ThreadPoolExecutor(max_workers=2) as pool:
   for result in pool.map(one,briefs):emit(result);st.data['output_count']+=1
