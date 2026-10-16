"""Compare retained artifacts without collecting, generating or modifying evidence."""
import argparse
from common import *

def compare(before, after):
 def records(r, name):
  return lines(r/name) if (r/name).exists() else []
 a=read(before/'run.json');b=read(after/'run.json')
 old={x['item_id']:x for x in records(before,'eligible.jsonl')}
 new={x['item_id']:x for x in records(after,'eligible.jsonl')}
 od={x['item_id']:x for x in records(before,'decisions.jsonl')}
 nd={x['item_id']:x for x in records(after,'decisions.jsonl')}
 def label(x):return {'item_id':x['item_id'],'title':x['title'],'version_id':x['version_id']}
 return {
  'before':a['run_id'],'after':b['run_id'],
  'different_date_live_runs':a.get('mode')=='live' and b.get('mode')=='live' and a['as_of_date']!=b['as_of_date'],
  'dates':[a['as_of_date'],b['as_of_date']],
  'newly_eligible':[label(new[k]) for k in sorted(new.keys()-old.keys())],
  'no_longer_eligible':[label(old[k]) for k in sorted(old.keys()-new.keys())],
  'changed_versions':[{'item_id':k,'before':old[k]['version_id'],'after':new[k]['version_id']} for k in sorted(old.keys()&new.keys()) if old[k]['version_id']!=new[k]['version_id']],
  'unchanged_versions':sum(old[k]['version_id']==new[k]['version_id'] for k in old.keys()&new.keys()),
  'decision_changes':[{'item_id':k,'before':od[k],'after':nd[k]} for k in sorted(od.keys()&nd.keys()) if od[k]['decision']!=nd[k]['decision'] or od[k]['reason']!=nd[k]['reason']],
  'policy_changed':(before/'config/editorial_policy.md').read_text()!=(after/'config/editorial_policy.md').read_text(),
  'note':'Comparison only. Inspect collection failures before interpreting missing items as expiry. Changed wording alone is not proof of a changed editorial judgment. Completion and publication require their own artifacts.'}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('before');parser.add_argument('after');args=parser.parse_args()
 emit(compare(safe(args.before),safe(args.after)))

if __name__=='__main__':entry(main)
