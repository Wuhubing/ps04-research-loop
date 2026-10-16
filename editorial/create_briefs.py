from common import *
from model import *
def main():
 r=runarg()
 with Stage('create_briefs',r) as st:
  decisions=stdin();st.data['input_count']=len(decisions)
  corpus={x['item_id']:x for x in lines(r/'eligible.jsonl')}
  if len(corpus)<12 or len({x['publisher_id'] for x in corpus.values()})<6 or any(sum(x['kind']==k for x in corpus.values())<2 for k in ['feed','youtube','podcast']):raise RuntimeError('Coverage incomplete: need 12 items, six independent sources and two per input kind before generating briefs')
  accepted={(x['item_id'],x['version_id']) for x in decisions if x['decision']=='accept'}
  rows=[x for x in lines(r/'eligible.jsonl') if (x['item_id'],x['version_id']) in accepted]
  if len(rows)<3 or len({x['publisher_id'] for x in rows})<3:raise RuntimeError('Insufficient accepted independent evidence')
  loc={'anyOf':[obj({'type':{'type':'string','enum':['text']},'quote':S}),obj({'type':{'type':'string','enum':['segment']},'segment_id':S})]}
  ref=obj({'item_id':S,'version_id':S,'locator':loc})
  claim=obj({'claim_id':S,'statement':S,'type':{'type':'string','enum':['reported_fact','source_claim','inference']},'evidence':arr(ref)})
  brief=obj({**{k:S for k in ['piece_id','title','question','argument','synthesis','limitations']},'claims':arr(claim)})
  material=evidence(rows)
  if len(json.dumps(material,ensure_ascii=False))>800000:
   from evidence_digest import compact
   material=compact(r,rows,decisions,loc)
   write(r/'synthesis_context.json',{'mode':'validated_excerpts','reason':'Full accepted evidence exceeds safe single-call input size','full_sources_retained':True,'source_count':len(rows),'evidence':material})
  result=call(r,'create_briefs',{'decisions':decisions,'evidence':material},obj({'briefs':arr(brief)}))['briefs']
  if sorted(x['piece_id'] for x in result)!=['01','02','03']:raise ValueError('Need three unique briefs')
  index={(x['item_id'],x['version_id']):x for x in rows}
  for b in result:
   publishers=set()
   for claim in b['claims']:
    if not claim['evidence']:raise RuntimeError('Unsupported claim in generated brief')
    for ref in claim['evidence']:
     item=index.get((ref['item_id'],ref['version_id']))
     if not item:raise RuntimeError('Brief cites evidence not accepted for this run')
     publishers.add(item['publisher_id']);loc=ref['locator']
     if loc['type']=='text':
      if not loc['quote'].strip() or loc['quote'] not in safe(item['text_path']).read_text():raise RuntimeError('Brief quote cannot be traced to saved evidence')
     elif not item['segments_path'] or loc['segment_id'] not in {s['segment_id'] for s in read(safe(item['segments_path']))}:raise RuntimeError('Brief segment cannot be traced to saved evidence')
   if len(publishers)<3:raise RuntimeError('Brief needs three independent source groups')
  for x in result:emit(x);st.data['output_count']+=1
entry(main)
