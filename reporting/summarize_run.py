from collections import Counter
from common import *
def main():
 r=runarg()
 with Stage('summarize_run',r) as st:
  meta=read(r/'run.json')
  def records(name):return lines(r/(name+'.jsonl')) if (r/(name+'.jsonl')).exists() else None
  counts={}
  for field,name in [('discovered','candidates'),('extracted','items'),('eligible','eligible'),('excluded','exclusions'),('articles','articles'),('video_scripts','video_scripts')]:
   rows=records(name);counts[field]=len(rows) if rows is not None else None
  for name,field,labels in [('changes','change',['new','changed','unchanged']),('decisions','decision',['accept','reject','defer'])]:
   rows=records(name)
   for label in labels:counts[{'accept':'accepted','reject':'rejected','defer':'deferred'}.get(label,label)]=sum(x[field]==label for x in rows) if rows is not None else None
  logs=[read(p) for p in sorted((r/'logs').glob('*.json'))];latest={}
  for x in sorted(logs,key=lambda x:x['started_at']):latest[x['stage']]=x
  lookup_misses=[x for x in logs if x['stage']=='store_get' and x['errors']==['Evidence item not found']]
  failed=[x for x in latest.values() if x['status']=='failed' and not (x['stage']=='store_get' and x['errors']==['Evidence item not found'])]
  review=read(r/'review.json') if (r/'review.json').exists() else {}
  ready=False
  if (r/'package/manifest.json').exists():
   sys.path.insert(0,str(ROOT/'review'));from check_content import assess
   current=assess(r);a=read(r/'approval.json') if (r/'approval.json').exists() else {}
   ready=current['passed'] and a.get('decision')=='approve' and a.get('review_id')==current['review_id']==read(r/'package/manifest.json')['review_id']
  status='ready_for_production' if ready else 'awaiting_review' if review.get('passed') else 'failed'
  rows=records('eligible') or [];distinct={x['item_id']:x for x in rows}
  result=dict(run_id=meta['run_id'],status=status,store_lookup_misses=len(lookup_misses),counts=counts,coverage_by_kind=dict(Counter(x['kind'] for x in distinct.values())),independent_publishers=sorted({x['publisher_id'] for x in rows}),failed_or_incomplete_stages=failed,duplicate_observations=max(0,len(records('candidates') or [])-len({x['item_id'] for x in records('candidates') or []})),elapsed_seconds=(__import__('datetime').datetime.fromisoformat(now().replace('Z','+00:00'))-__import__('datetime').datetime.fromisoformat(meta['started_at'].replace('Z','+00:00'))).total_seconds(),tools_or_models=sorted({t for x in logs for t in x['tools_or_models']}),known_cost_usd=sum(x['cost_usd'] for x in logs if x['cost_usd'] is not None) if any(x['cost_usd'] is not None for x in logs) else None, total_cost_usd=None if any(x['cost_usd'] is None for x in logs) else sum(x['cost_usd'] for x in logs),unknown_cost_receipts=sum(x['cost_usd'] is None for x in logs),remaining_manual_actions=['Student six-case editorial review; document policy revision outcome','Student final approval','Second live run on a different UTC date','Google Vids production','Substack and YouTube publication','Technical demonstration'],publication_links=read(r/'package/publication_links.json') if (r/'package/publication_links.json').exists() else None)
  if meta.get('collection_run_id'):
   origin=Path('runs')/meta['collection_run_id']/'summary.json'
   result['evidence_collection_run_id']=meta['collection_run_id']
   result['inherited_collection_failures']=[x for x in read(origin).get('failed_or_incomplete_stages',[]) if x['stage'].startswith(('collect','extract'))] if origin.exists() else ['Collection summary unavailable']
  comparison=r/'comparison_collection.json'
  if comparison.exists():
   compared=read(comparison)
   if compared.get('after')==meta['run_id'] and compared.get('different_date_live_runs') and review.get('passed'):
    result['remaining_manual_actions'].remove('Second live run on a different UTC date')
    result['different_date_live_comparison']=str(comparison.relative_to(ROOT))
  student_record=r/'student_review_record.json'
  if student_record.exists():
   student=read(student_record)
   if student.get('status')=='six_case_judgments_completed' and student.get('accepted_cases_reviewed',0)>=3 and student.get('rejected_or_deferred_cases_reviewed',0)>=3 and (r/student.get('record','')).is_file():
    result['student_case_review']=student
    result['remaining_manual_actions'].remove('Student six-case editorial review; document policy revision outcome')
  if meta.get('collection_run_id'):
   prior=Path('runs')/meta['collection_run_id']/'comparison_collection.json'
   if prior.exists():
    compared=read(prior)
    if compared.get('after')==meta['collection_run_id'] and compared.get('different_date_live_runs'):
     action='Second live run on a different UTC date'
     if action in result['remaining_manual_actions']:result['remaining_manual_actions'].remove(action)
     result['different_date_live_comparison']=str(prior)
  if ready:
   result['remaining_manual_actions']=[x for x in result['remaining_manual_actions'] if x not in ['Student final approval','Google Vids production','Substack and YouTube publication','Technical demonstration']]
   result['remaining_manual_actions'].extend(read(r/'package/manifest.json').get('remaining_manual_actions',[]))
  emit(result);st.data['output_count']=1
entry(main)
