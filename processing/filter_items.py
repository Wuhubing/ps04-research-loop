import datetime as dt
from common import *
def exclusion(value,asof):
 if value is None:return 'unknown_date'
 try:
  timestamp=dt.datetime.fromisoformat(value.replace('Z','+00:00'))
  if timestamp.tzinfo is None:return 'invalid_date'
  d=timestamp.astimezone(dt.timezone.utc).date()
 except (ValueError,TypeError):return 'invalid_date'
 if d>asof:return 'future_date'
 if d<asof-dt.timedelta(days=29):return 'outside_window'
 return None
def main():
 r=runarg()
 with Stage('filter_items',r) as st:
  rows=stdin();st.data['input_count']=len(rows);out=[]
  for x in rows:
   reason=exclusion(x['published_at'],dt.date.fromisoformat(read(r/'run.json')['as_of_date']))
   if reason:out.append(dict(item_id=x['item_id'],version_id=x['version_id'],reason=reason,detail=x.get('publication_date_evidence',str(x['published_at']))))
   else:emit(x);st.data['output_count']+=1
  jsonl(r/'exclusions.jsonl',out)
if __name__=='__main__':entry(main)
