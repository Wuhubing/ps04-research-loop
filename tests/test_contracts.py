import datetime as dt,json,os,shutil,subprocess,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Contracts(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
  for folder in ['lib','data','processing','review','publishing','reporting','editorial']:
   shutil.copytree(ROOT/folder,self.root/folder,ignore=shutil.ignore_patterns('evidence','assets','media','__pycache__'))
  self.r=self.root/'runs/test';self.r.mkdir(parents=True)
  self.put('run.json',dict(run_id='test',as_of_date='2026-10-14',started_at='2026-10-14T00:00:00Z',mode='example',previous_run_id=None))
  self.env={**os.environ,'PYTHONPATH':str(self.root/'lib'),'RUN_DIR':str(self.r)}
 def tearDown(self):self.tmp.cleanup()
 def put(self,p,x):
  p=self.r/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x))
 def stream(self,p,x): (self.r/p).write_text(''.join(json.dumps(y)+'\n' for y in x))
 def runpy(self,file,args=(),rows=None):
  return subprocess.run([str(ROOT/'.venv/bin/python'),str(self.root/file),*map(str,args)],input=''.join(json.dumps(x)+'\n' for x in rows) if rows is not None else '',text=True,capture_output=True,env=self.env,cwd=self.root)
 def item(self,i=0):
  p=Path('data/assets')/str(i);(self.root/p).mkdir(parents=True,exist_ok=True);(self.root/p/'text.txt').write_text('Exact supporting passage.')
  media=i%3!=0
  if media:(self.root/p/'segments.json').write_text(json.dumps([dict(segment_id='s0',start_seconds=1.,end_seconds=3.,text='Exact supporting passage.')]))
  return dict(item_id=str(i),version_id='v1',source_id='s'+str(i),publisher_id='p'+str(i),kind=['feed','youtube','podcast'][i%3],title='Fixture '+str(i),url='https://example.org/'+str(i),published_at='2026-10-01T00:00:00Z',retrieved_at='2026-10-14T00:00:00Z',media_url=None,discovery_method='syndication',text_path=str(p/'text.txt'),segments_path=str(p/'segments.json') if media else None)
 def fixture(self):
  items=[self.item(i) for i in range(12)];self.stream('eligible.jsonl',items)
  self.stream('decisions.jsonl',[dict(item_id=x['item_id'],version_id='v1',decision='accept',reason='fixture',piece_ids=['01','02','03']) for x in items]);briefs=[]
  for pid in ['01','02','03']:
   claims=[dict(claim_id=pid+'-c'+str(i),statement='Supported statement',type='source_claim',evidence=[dict(item_id=str(i),version_id='v1',locator=dict(type='text',quote='Exact supporting passage.') if i%3==0 else dict(type='segment',segment_id='s0'))]) for i in range(3)]
   briefs.append(dict(piece_id=pid,title=pid,question=pid,argument=pid,synthesis='Connected reasoning',limitations='Fixture only',claims=claims))
  self.stream('briefs.jsonl',briefs)
  for name in ['articles','video_scripts']:
   manifests=[]
   for b in briefs:
    path=Path('runs/test')/name/(b['piece_id']+'.md');(self.root/path).parent.mkdir(exist_ok=True);(self.root/path).write_text('2026-10-14 https://example.org '+ ' '.join(c['claim_id'] for c in b['claims']))
    manifests.append(dict(piece_id=b['piece_id'],path=str(path),claim_ids=[c['claim_id'] for c in b['claims']]))
   self.stream(name+'.jsonl',manifests)
  return items
 def test_store_idempotence_and_versions(self):
  x=self.item();p=self.runpy('data/store.py',['upsert',self.r],[x,x]);self.assertEqual(p.returncode,0,p.stderr);self.assertEqual([json.loads(y)['change'] for y in p.stdout.splitlines()],['new','unchanged'])
  x['retrieved_at']='2026-10-15T00:00:00Z';p=self.runpy('data/store.py',['upsert',self.r],[x]);self.assertEqual(json.loads(p.stdout)['change'],'unchanged')
  x['version_id']='v2';self.runpy('data/store.py',['upsert',self.r],[x]);p=self.runpy('data/store.py',['get','0','v1']);self.assertEqual(json.loads(p.stdout)['version_id'],'v1')
 def test_filter_boundaries(self):
  dates=['2026-09-15T00:00:00Z','2026-09-14T23:59:59Z','2026-10-14T23:59:59Z','2026-10-15T00:00:00Z',None,'bad']
  rows=[{**self.item(i),'published_at':d} for i,d in enumerate(dates)];p=self.runpy('processing/filter_items.py',[self.r],rows);self.assertEqual(p.returncode,0,p.stderr);self.assertEqual(len(p.stdout.splitlines()),2)
  reasons=[json.loads(x)['reason'] for x in (self.r/'exclusions.jsonl').read_text().splitlines()];self.assertEqual(reasons,['outside_window','future_date','unknown_date','invalid_date'])
 def test_failed_feed_preserves_valid_results(self):
  import http.server,threading
  class Handler(http.server.BaseHTTPRequestHandler):
   def do_GET(self):
    if self.path!='/good':self.send_error(503);return
    body=b'<rss version="2.0"><channel><title>Fixture</title><item><title>Example research</title><link>https://example.org/paper</link><guid>fixture-one</guid><pubDate>Thu, 01 Oct 2026 00:00:00 GMT</pubDate></item></channel></rss>'
    self.send_response(200);self.end_headers();self.wfile.write(body)
   def log_message(self,*args):pass
  server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
  try:
   self.put('config/sources.json',[dict(source_id=k,publisher_id=k,kind='feed',url=f'http://127.0.0.1:{server.server_port}/'+k) for k in ['good','bad']])
   p=subprocess.run([str(ROOT/'.venv/bin/python'),'-c',"from feeds import fetch; fetch('feed')",str(self.r)],text=True,capture_output=True,env=self.env,cwd=self.root)
   self.assertEqual(p.returncode,1,p.stderr);self.assertEqual(len(p.stdout.splitlines()),1)
   receipt=json.loads(next((self.r/'logs').glob('collect_feed-*.json')).read_text());self.assertEqual(receipt['status'],'failed');self.assertEqual(receipt['output_count'],1)
  finally:server.shutdown();server.server_close()
 def test_invalid_input_exit_two(self):
  p=self.runpy('data/store.py',['upsert',self.r],[{}]);self.assertEqual(p.returncode,2)
 def test_synthesis_digest_rejects_invented_passage(self):
  item=self.item();note=dict(item_id=item['item_id'],version_id=item['version_id'],passages=[dict(locator=dict(type='text',quote='Exact supporting passage.'))])
  def check():
   return subprocess.run([str(ROOT/'.venv/bin/python'),'-c','import json,sys; from evidence_digest import validate; validate(*json.load(sys.stdin))'],input=json.dumps([item,note]),text=True,capture_output=True,cwd=self.root,env={**self.env,'PYTHONPATH':str(self.root/'lib')+os.pathsep+str(self.root/'editorial')})
  self.assertEqual(check().returncode,0)
  note['passages'][0]['locator']['quote']='Invented claim'
  self.assertNotEqual(check().returncode,0)
  item=self.item(1);note=dict(item_id=item['item_id'],version_id=item['version_id'],passages=[dict(locator=dict(type='segment',segment_id='missing'))])
  self.assertNotEqual(check().returncode,0)
 def test_incomplete_review(self):
  self.stream('eligible.jsonl',[]);self.stream('briefs.jsonl',[]);self.stream('decisions.jsonl',[])
  p=self.runpy('review/check_content.py',[self.r]);self.assertEqual(p.returncode,0,p.stderr);self.assertFalse(json.loads(p.stdout)['passed'])
 def test_wrong_window_rejected_despite_correct_asof(self):
  self.fixture();p=self.root/'runs/test/articles/01.md'
  with p.open('a') as f:f.write('\nPublication window: **2026-09-14–2026-10-13 UTC**\n')
  review=json.loads(self.runpy('review/check_content.py',[self.r]).stdout)
  self.assertFalse(review['passed']);self.assertTrue(any('window' in x['explanation'] for x in review['issues']))
 def test_quotes_and_fingerprint(self):
  self.fixture();p=self.runpy('review/check_content.py',[self.r]);original=json.loads(p.stdout);self.assertTrue(original['passed'],p.stdout)
  (self.root/'data/assets/0/text.txt').write_text('Changed source')
  p=self.runpy('review/check_content.py',[self.r]);new=json.loads(p.stdout);self.assertFalse(new['passed']);self.assertNotEqual(new['review_id'],original['review_id'])
 def test_fallback_does_not_satisfy_rss_quota(self):
  rows=self.fixture()
  for row in rows:row['discovery_method']='direct_metadata_fallback'
  self.stream('eligible.jsonl',rows)
  review=json.loads(self.runpy('review/check_content.py',[self.r]).stdout)
  self.assertFalse(review['passed']);self.assertTrue(any('RSS/Atom' in x['explanation'] for x in review['issues']))
 def test_shared_publisher_and_broken_media(self):
  rows=self.fixture()
  for row in rows:row['publisher_id']='same-origin'
  self.stream('eligible.jsonl',rows)
  (self.root/'data/assets/1/segments.json').write_text('[]')
  review=json.loads(self.runpy('review/check_content.py',[self.r]).stdout)
  self.assertFalse(review['passed']);self.assertTrue(any('media segment' in x['explanation'] for x in review['issues']));self.assertTrue(any('three independent' in x['explanation'] for x in review['issues']))
 def test_approval_staleness_and_links(self):
  self.fixture();review=json.loads(self.runpy('review/check_content.py',[self.r]).stdout)
  p=self.runpy('publishing/prepare_package.py',[self.r]);self.assertNotEqual(p.returncode,0)
  self.put('approval.json',dict(review_id=review['review_id'],decision='approve',reviewer='TEST FIXTURE ONLY',reviewed_at='2026-10-14T00:00:00Z',notes='Synthetic test, not student approval'))
  p=self.runpy('publishing/prepare_package.py',[self.r]);self.assertEqual(p.returncode,0,p.stderr)
  links=[dict(piece_id='01',substack_url='https://example.org/test',youtube_url=None)];self.put('package/publication_links.json',links)
  self.runpy('publishing/prepare_package.py',[self.r]);self.assertEqual(json.loads((self.r/'package/publication_links.json').read_text()),links)
  with open(self.r/'articles/01.md','a') as f:f.write('Change')
  p=self.runpy('publishing/prepare_package.py',[self.r]);self.assertNotEqual(p.returncode,0)
if __name__=='__main__':unittest.main()
