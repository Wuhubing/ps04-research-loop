from pathlib import Path
import json,re,difflib
from faster_whisper import WhisperModel
p=Path('data/media/technical-demo');scenes=json.loads((p/'scenes.json').read_text());model=WhisperModel('small.en',device='cpu',compute_type='int8')
results=[]
for i,scene in enumerate(scenes,1):
 f=p/f'scene-{i:02}_000.wav'
 if not f.exists():break
 segments,_=model.transcribe(str(f),language='en',beam_size=5)
 actual=' '.join(s.text for s in segments)
 clean=lambda t:re.findall(r'[a-z0-9]+',t.lower())
 score=difflib.SequenceMatcher(None,clean(scene[3]),clean(actual)).ratio()
 result=dict(scene=i,expected=scene[3],automatic_transcription=actual,token_similarity=score,human_listened=False)
 results.append(result);(p/f'scene-{i:02}-qa.json').write_text(json.dumps(result,indent=2));print(i,score,flush=True)
(p/'automatic_qa.json').write_text(json.dumps(results,indent=2))
