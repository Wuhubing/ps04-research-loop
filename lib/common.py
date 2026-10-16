"""Shared I/O and receipts only; stage logic belongs to its component."""
import datetime as dt, hashlib, json, os, sys, uuid
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
def now(): return dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')
def digest(x): return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def read(p): return json.loads(Path(p).read_text())
def write(p,x):
 p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def lines(p):
 with open(p) as f: return [json.loads(s) for s in f if s.strip()]
def stdin(): return [json.loads(s) for s in sys.stdin if s.strip()]
def emit(x): print(json.dumps(x,ensure_ascii=False),flush=True)
def jsonl(p,rows):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
def safe(p):
 q=(ROOT/p).resolve()
 if not q.is_relative_to(ROOT): raise ValueError('Path outside repository')
 return q
class Stage:
 def __init__(self,name,run):
  self.run=Path(run); self.data=dict(stage=name,status='running',input_count=0,output_count=0,started_at=now(),tools_or_models=[],cost_usd=None,cost_estimated=False,errors=[])
 def __enter__(self): return self
 def error(self,e): self.data['errors'].append(str(e));print(str(e),file=sys.stderr)
 def __exit__(self,typ,exc,tb):
  if exc:self.error(exc)
  self.data.update(finished_at=now(),status='failed' if self.data['errors'] else 'completed')
  write(self.run/'logs'/f"{self.data['stage'].replace('/','_')}-{uuid.uuid4().hex}.json",self.data)
 def finish(self):
  if self.data['errors']: raise SystemExit(1)
def entry(fn):
 try:fn()
 except (ValueError,KeyError,IndexError,json.JSONDecodeError) as e:print(str(e),file=sys.stderr);sys.exit(2)
 except Exception as e:print(str(e),file=sys.stderr);sys.exit(1)
def runarg():
 if len(sys.argv)!=2:raise ValueError('Expected RUN_DIR')
 r=safe(sys.argv[1]);read(r/'run.json');return r
