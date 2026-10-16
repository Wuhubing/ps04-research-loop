"""Bound synthesis context with source-validated excerpts, retaining full evidence."""
from concurrent.futures import ThreadPoolExecutor
from common import *
from model import *

def validate(item,note):
 if (note['item_id'],note['version_id'])!=(item['item_id'],item['version_id']):raise RuntimeError('Digest changed evidence identity')
 if not note['passages']:raise RuntimeError('Digest has no evidence passages')
 text=safe(item['text_path']).read_text()
 segments={s['segment_id']:s for s in read(safe(item['segments_path']))} if item['segments_path'] else {}
 for passage in note['passages']:
  loc=passage['locator']
  if item['segments_path'] and loc['type']!='segment':raise RuntimeError('Media digest requires timestamped segments')
  if loc['type']=='text':
   if not loc['quote'].strip() or loc['quote'] not in text:raise RuntimeError('Digest quote does not match preserved source')
  elif loc['segment_id'] not in segments:raise RuntimeError('Digest segment does not exist')

def compact(run,rows,decisions,locator_schema):
 schema=obj({'item_id':S,'version_id':S,'synopsis':S,'limitations_and_counterevidence':S,'passages':arr(obj({'purpose':S,'locator':locator_schema}))})
 selected={(d['item_id'],d['version_id']):d for d in decisions}
 def one(item):
  cache=run/'evidence_digest'/(item['item_id']+'-'+item['version_id']+'.json')
  if cache.exists():note=read(cache)
  else:
   note=call(run,'distill_evidence',{'decision':selected[(item['item_id'],item['version_id'])],'evidence':evidence([item])},schema)
  try:validate(item,note)
  except RuntimeError as error:
   write(run/'evidence_digest'/(item['item_id']+'-rejected-'+uuid.uuid4().hex+'.json'),{'validation_error':str(error),'rejected_response':note})
   note=call(run,'distill_evidence',{'decision':selected[(item['item_id'],item['version_id'])],'evidence':evidence([item]),'invalid_previous_response':note,'repair_instruction':'Correct the validation error using exact preserved evidence; do not paraphrase inside quote locators. '+str(error)},schema)
   validate(item,note)
  write(cache,note)
  view={**item,'excerpted_for_synthesis':True,'synopsis':note['synopsis'],'limitations_and_counterevidence':note['limitations_and_counterevidence'],'passages':note['passages']}
  if item['segments_path']:
   chosen={p['locator'].get('segment_id') for p in note['passages']}
   view.update(text=None,segments=[s for s in read(safe(item['segments_path'])) if s['segment_id'] in chosen])
  else:view.update(text='\n\n[Separate verified excerpt]\n\n'.join(p['locator']['quote'] for p in note['passages']),segments=None)
  return view
 with ThreadPoolExecutor(max_workers=2) as pool:return list(pool.map(one,rows))
