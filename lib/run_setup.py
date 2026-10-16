import shutil
from common import *
def main():
 project=read('config/project.json');sources=read('config/sources.json')
 for k in ['publication_name','topic','audience','central_question']:
  if not isinstance(project.get(k),str) or not project[k].strip():raise ValueError('Invalid project '+k)
 for s in sources:
  for k in ['source_id','publisher_id','kind','url']:
   if not s.get(k):raise ValueError('Missing source '+k)
  if s['kind'] not in ['feed','youtube','podcast']:raise ValueError('Invalid kind')
 for name in ['select_items','create_briefs','write_articles','write_video_scripts']:
  if not Path('prompts/'+name+'.md').read_text().strip():raise ValueError('Empty prompt')
 stamp=now();rid=stamp.replace(':','').replace('-','').split('.')[0]+'-'+uuid.uuid4().hex[:6];r=Path('runs')/rid
 previous=sorted((p for p in Path('runs').glob('*/run.json') if read(p).get('mode')=='live'),key=lambda p:read(p)['started_at']) if Path('runs').exists() else []
 r.mkdir(parents=True);shutil.copytree('config',r/'config');shutil.copytree('prompts',r/'prompts');(r/'logs').mkdir();(r/'candidates').mkdir()
 write(r/'run.json',dict(run_id=rid,started_at=stamp,as_of_date=stamp[:10],mode='live',previous_run_id=read(previous[-1])['run_id'] if previous else None));print(r)
entry(main)
