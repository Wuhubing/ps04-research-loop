import subprocess, datetime as dt
from common import *
def main():
 r=runarg()
 with Stage('collect_youtube',r) as st:
  st.data['tools_or_models']=['yt-dlp']
  for source in read(r/'config/sources.json'):
   if source['kind']!='youtube':continue
   st.data['input_count']+=1
   try:
    p=subprocess.run([str(ROOT/'.venv/bin/yt-dlp'),'--skip-download','--dump-single-json','--no-playlist',source['url']],capture_output=True,text=True,timeout=120)
    if p.returncode:raise RuntimeError(p.stderr[-1500:])
    v=json.loads(p.stdout);write(r/'discovery'/f"{source['source_id']}.json",v)
    date=dt.datetime.fromtimestamp(v['timestamp'],dt.timezone.utc).isoformat().replace('+00:00','Z') if v.get('timestamp') else dt.datetime.strptime(v['upload_date'],'%Y%m%d').isoformat()+'Z' if v.get('upload_date') else None
    emit(dict(item_id='youtube-'+v['id'],source_id=source['source_id'],publisher_id=source['publisher_id'],kind='youtube',title=v['title'],url=v['webpage_url'],published_at=date,retrieved_at=now(),media_url=None));st.data['output_count']+=1
   except Exception as e:st.error(f"{source['source_id']}: {e}")
 st.finish()
entry(main)
