from common import *
name,run,started,code=sys.argv[1:]
write(Path(run)/'logs'/(name+'-'+uuid.uuid4().hex+'.json'),dict(stage=name,status='completed' if code=='0' else 'failed',input_count=None,output_count=None,started_at=started,finished_at=now(),tools_or_models=['bash'],cost_usd=None,cost_estimated=False,errors=[] if code=='0' else ['Exit '+code]))
