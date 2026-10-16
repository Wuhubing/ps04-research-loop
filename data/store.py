import sqlite3
from common import *
def main():
 if len(sys.argv)<2:raise ValueError('Expected init, upsert, list or get')
 cmd=sys.argv[1];run=Path(os.environ.get('RUN_DIR','runs/storage-operations'))
 if cmd=='upsert':
  if len(sys.argv)!=3:raise ValueError('upsert RUN_DIR')
  run=safe(sys.argv[2])
 with Stage('store_'+cmd,run) as st:
  folder=ROOT/'data/evidence';folder.mkdir(parents=True,exist_ok=True)
  db=sqlite3.connect(folder/'index.sqlite');db.execute('PRAGMA foreign_keys=ON')
  db.executescript('CREATE TABLE IF NOT EXISTS versions(item_id TEXT, version_id TEXT, record TEXT, PRIMARY KEY(item_id,version_id)); CREATE TABLE IF NOT EXISTS latest(item_id TEXT PRIMARY KEY, version_id TEXT); CREATE TABLE IF NOT EXISTS observations(run_id TEXT,item_id TEXT,version_id TEXT,observed_at TEXT);')
  if cmd=='init':pass
  elif cmd=='upsert':
   rows=stdin();st.data['input_count']=len(rows)
   for x in rows:
    for k in ['item_id','version_id','text_path','segments_path','publisher_id','kind','published_at']:x[k]
   for x in rows:
    old=db.execute('SELECT version_id FROM latest WHERE item_id=?',(x['item_id'],)).fetchone()
    change='new' if old is None else 'unchanged' if old[0]==x['version_id'] else 'changed'
    db.execute('INSERT OR IGNORE INTO versions VALUES(?,?,?)',(x['item_id'],x['version_id'],json.dumps(x)))
    db.execute('INSERT OR REPLACE INTO latest VALUES(?,?)',(x['item_id'],x['version_id']))
    db.execute('INSERT INTO observations VALUES(?,?,?,?)',(run.name,x['item_id'],x['version_id'],x['retrieved_at']))
    emit(dict(item_id=x['item_id'],version_id=x['version_id'],change=change));st.data['output_count']+=1
  elif cmd=='list':
   for row in db.execute('SELECT record FROM versions JOIN latest USING(item_id,version_id) ORDER BY item_id'):emit(json.loads(row[0]));st.data['output_count']+=1
  elif cmd=='get':
   if len(sys.argv) not in (3,4):raise ValueError('get ITEM_ID [VERSION_ID]')
   if len(sys.argv)==4:row=db.execute('SELECT record FROM versions WHERE item_id=? AND version_id=?',sys.argv[2:]).fetchone()
   else:row=db.execute('SELECT record FROM versions JOIN latest USING(item_id,version_id) WHERE item_id=?',(sys.argv[2],)).fetchone()
   if row is None:raise RuntimeError('Evidence item not found')
   emit(json.loads(row[0]));st.data['output_count']=1
  else:raise ValueError('Unknown store command')
  db.commit();db.close()
entry(main)
