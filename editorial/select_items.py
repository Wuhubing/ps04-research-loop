from common import *
from model import *
def main():
 r=runarg()
 with Stage('select_items',r) as st:
  rows=stdin();st.data['input_count']=len(rows)
  schema=obj({'decisions':arr(obj({'item_id':S,'version_id':S,'decision':{'type':'string','enum':['accept','reject','defer']},'reason':S,'piece_ids':arr({'type':'string','enum':['01','02','03']})}))})
  result=[]
  for start in range(0,len(rows),4):
   result.extend(call(r,'select_items',evidence(rows[start:start+4]),schema)['decisions'])
  if sorted((x['item_id'],x['version_id']) for x in result)!=sorted((x['item_id'],x['version_id']) for x in rows):raise ValueError('Decisions must cover every candidate exactly once')
  for x in result:
   if x['decision']!='accept' and x['piece_ids']:raise ValueError('Rejected/deferred item assigned to article')
   emit(x);st.data['output_count']+=1
entry(main)
