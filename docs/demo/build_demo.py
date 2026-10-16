"""Render an explicitly AI-narrated walkthrough of saved, real project artifacts.
Run from repository root with the private local voice environment.
No source collection, drafting, publication, or approval is performed here.
"""
from pathlib import Path
import json, subprocess, os, textwrap
from PIL import Image, ImageDraw, ImageFont
ROOT=Path.cwd(); OUT=ROOT/'data/media/technical-demo'; OUT.mkdir(parents=True,exist_ok=True)
RUN=ROOT/'runs/20261016T183853-editorial-v3'
def read(p):return json.loads(p.read_text())
def rows(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
scenes=[
('Architecture and entry points', 'run.sh + ARCHITECTURE.md',
'''bash run.sh\n  collectors -> extraction -> store -> freshness\n  selection -> briefs -> articles + scripts -> review\n\nbash run.sh --package runs/RUN_ID\n  review fingerprint -> student approval -> package\n\nOnly data/store.sh accesses SQLite.\nAll component calls retain receipts and partial results.''',
'''This is an AI-narrated walkthrough of Research Loop, a repeatable intelligence pipeline for student researchers. The series asks which experimental tasks agents can automate, and what makes the results trustworthy. The display presents excerpts from retained project artifacts, rather than pretending to be a live collection. The main Bash entry point coordinates independent components for feeds, YouTube, podcasts, extraction, storage, editorial decisions, and drafting. Python implements each component. Only the storage interface accesses the SQLite evidence index. Articles and video scripts share an evidence-linked brief. A separate packaging command checks the reviewed fingerprint and a matching student decision. It does not fetch new sources or silently rewrite approved drafts.'''),
('Trace one published claim', 'briefs.jsonl -> exact source version -> article 01',
'',
'''Here is a concrete claim from the first article. Li and Lu report contact precision increasing from twenty-eight point two percent to thirty-six point six percent at the same forty-eight point four billion token budget. The source passage also says a human decided which recipes to scale. The brief retains the exact item identifier, source version, and quotation. The article therefore attributes the numbers to the authors and preserves the human role. It does not describe an independently replicated result or a fully autonomous discovery. This chain matters because a fluent summary can otherwise erase the condition that makes a reported result interpretable. The saved article and its free published version can be compared directly.'''),
('Two real collection dates', 'October 14 and October 15 summaries; current storage replay',
'',
'''The first real run occurred on October fourteenth, UTC. It retained seventeen items, of which fifteen met the thirty-day window. The second real run occurred on October fifteenth. Twenty-six observations represented twenty-five distinct retained items, and twenty-three were eligible. Eight distinct items were newly collected, seventeen were unchanged, and none had a changed content version. These eight items were already published before the first run. They reflect restored feed access and an explicitly added podcast, not eight overnight publications. The storage-only replay shown here was run separately: all twenty-six imported observations were unchanged. It demonstrates deduplication, but is explicitly not a replacement for either live run.'''),
('Failures remain visible', 'First-run collector receipt and second-run recovery',
'',
'''The first collection encountered an actual rate limit on the arXiv feed. The collector retained the error and the useful records from other sources. Original-page recovery was labeled supplemental evidence, so it could not silently satisfy the RSS quota. On the second date, the native feeds succeeded and expanded the corpus. That distinction lets a reader separate a lack of coverage from a lack of new research. Publication dates are also separate from collection times. Old, unknown, and future dates are handled explicitly. Isolated contract tests exercise date boundaries, partial failure, source versions, and approval invalidation. Those tests use synthetic fixtures and are not counted as research evidence or live collection runs.'''),
('A real human editorial correction', 'Student six-case review -> policy v3 -> preserved draft differences',
'',
'''The student compared three accepted and three rejected cases with the saved AI decisions. One accepted tutorial was restricted to procedural guidance: it cannot prove that a model is stronger. The student also requested human review of AI evaluations to reduce the risk of a model judging its own output. Another accepted paper must remain an author-reported result with its human role visible. Conflicting numbers must be disclosed rather than turned into a speed or cost superiority claim. News digests supply leads, not independent confirmation. These recorded judgments informed policy version three. The editorial rerun reused the frozen October fifteenth evidence, so it is not a third collection. The human-review safeguard appears in article three and its matching narration.'''),
('Delivery, checks, and tradeoffs', 'Published series + review.json + remaining human verification',
'',
'''All three articles are published free, and their three companion videos are unlisted on YouTube, with reciprocal links. Mechanical content checks pass. The student approved the finished videos after listening and explicitly authorized publication of the articles. This does not establish that every original audio quotation has been heard and checked. Those source excerpts remain on the final listening checklist. The main architectural tradeoff is additional artifacts and storage in exchange for inspectable evidence and reproducible decisions. Retaining source versions also makes stale approval detectable after a draft changes. Local transcription and speech generation avoid a per-call hosted audio fee, but consume machine resources. Codex subscription usage cannot be reliably converted into dollars here, so its cost remains unknown, not free.''')]
brief=rows(RUN/'briefs.jsonl')[0];c=next(x for x in brief['claims'] if x['claim_id']=='01-c1');ref=c['evidence'][0]
scenes[1]=(scenes[1][0],scenes[1][1],f"Claim: {c['claim_id']}\nItem: {ref['item_id']}\nVersion: {ref['version_id'][:24]}...\n\n"+ref['locator']['quote']+'\n\nPublished interpretation: author-reported; human-guided.',scenes[1][3])
a=read(ROOT/'runs/20261014T032814-a43e45/summary.json');b=read(ROOT/'runs/20261015T003111-ebae97/summary.json')
replay=ROOT/'runs/replay-c48d0475956e'; result=next(replay.glob('*result*'),None)
scenes[2]=(scenes[2][0],scenes[2][1],f"LIVE 2026-10-14: {a['counts']['extracted']} extracted; {a['counts']['eligible']} eligible\nLIVE 2026-10-15: {b['counts']['extracted']} observations; {b['counts']['eligible']} eligible\n\nDistinct retained comparison: 8 new / 17 unchanged / 0 changed\nAll newly collected items predate the first run.\n\nActual storage replay: replay-c48d0475956e\n26 unchanged / 0 new / 0 changed\nREPLAY ONLY: not a new live collection",scenes[2][3])
fail=a['failed_or_incomplete_stages'][0]
scenes[3]=(scenes[3][0],scenes[3][1],'Actual failed stage: '+fail['stage']+'\n'+ '\n'.join(fail['errors'])[:600]+'\n\nSecond live run: native feeds succeeded.\nSupplemental page recovery is not RSS collection.\nTests: synthetic fixtures, never counted as evidence.',scenes[3][3])
scenes[4]=(scenes[4][0],scenes[4][1],'Recorded student judgment (English translation):\n\nUse the tutorial as a reference for designing tests,\nbut not to prove which model is stronger.\nAdd human review to avoid AI evaluation bias.\n\nPolicy v3: procedural claims + human review\n23 unchanged evidence versions; 19 accepts / 3 rejects / 1 defer\nSee student_review_record.json and policy_revision.md',scenes[4][3])
scenes[5]=(scenes[5][0],scenes[5][1],'3 free Substack articles + 3 unlisted companion videos\nMechanical review: PASS\nPublication authorization: recorded actual student statements\nOriginal-source listening: still pending\n\nTradeoff: more artifacts, more inspectable claims\nCodex subscription cost: UNKNOWN, not $0\nLocal media and private voice sample excluded from Git',scenes[5][3])
(OUT/'scenes.json').write_text(json.dumps(scenes,indent=2));(ROOT/'docs/demo/narration.md').write_text('\n\n'.join('## '+s[0]+'\n\n'+s[3] for s in scenes))
font='/System/Library/Fonts/Supplemental/Arial.ttf';bold='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
for i,(title,source,body,narration) in enumerate(scenes,1):
 name=f'scene-{i:02}'; im=Image.new('RGB',(1920,1080),'#11161e');d=ImageDraw.Draw(im)
 d.text((90,65),f'RESEARCH LOOP | TECHNICAL DEMONSTRATION | {i:02}/06',font=ImageFont.truetype(bold,28),fill='#ffdf68')
 d.text((90,135),title,font=ImageFont.truetype(bold,55),fill='white'); y=245
 for raw in body.splitlines():
  for line in textwrap.wrap(raw,85) or ['']:
   d.text((90,y),line,font=ImageFont.truetype(font,33),fill='#e0e6ee');y+=45
 d.text((90,960),source,font=ImageFont.truetype(font,25),fill='#ffdf68')
 d.text((90,1010),'Saved artifact excerpts | AI narration using authorized voice | Not a live collection',font=ImageFont.truetype(font,23),fill='#aebccc')
 im.save(OUT/f'{name}.png');wav=OUT/f'{name}_000.wav'
 if not wav.exists():
  args=[str(ROOT/'data/media/voice-local/.venv/bin/python'),'-m','mlx_audio.tts.generate','--model','mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16','--text',narration,'--ref_audio',str(ROOT/'data/media/voice-local/reference-short.wav'),'--ref_text',"Welcome to Research Loop. Today, we'll explore how AI agents can help run experiments.",'--lang_code','English','--temperature','0.5','--output_path',str(OUT),'--file_prefix',name,'--audio_format','wav']
  with (OUT/f'{name}.log').open('w') as f:subprocess.run(args,check=True,stdout=f,stderr=subprocess.STDOUT,env={**os.environ,'HF_HUB_OFFLINE':'1','HF_HUB_DISABLE_TELEMETRY':'1'})
 duration=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(wav)]))+1.4
 subprocess.run(['ffmpeg','-y','-v','error','-loop','1','-i',str(OUT/f'{name}.png'),'-i',str(wav),'-af','volume=12dB,alimiter=limit=0.891:level=false,adelay=700,apad','-t',str(duration),'-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k',str(OUT/f'{name}.mp4')],check=True)
 print(name,duration,flush=True)
(OUT/'concat.txt').write_text('\n'.join(f"file '{OUT}/scene-{i:02}.mp4'" for i in range(1,7)))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(OUT/'concat.txt'),'-c','copy','-movflags','+faststart',str(OUT/'Research-Loop-Technical-Demo.mp4')],check=True)
print('DONE',flush=True)
