"""Build an unanswered review worksheet; this never impersonates the student."""
import argparse
from common import *
def main():
 r=runarg()
 with Stage('prepare_student_review',r) as st:
  decisions=lines(r/'decisions.jsonl');items={(x['item_id'],x['version_id']):x for x in lines(r/'eligible.jsonl')}
  selected=[x for x in decisions if x['decision']=='accept'][:3]+[x for x in decisions if x['decision'] in ['reject','defer']][:3]
  text=['# Student editorial review — unanswered','This is a worksheet, not approval. Fill in your own judgments after inspecting the evidence.']
  for d in selected:
   item=items[(d['item_id'],d['version_id'])]
   text.extend(['## '+item['title'],f"Source: {item['url']}\n\nEvidence: {item['text_path']}\n\nAI decision: {d['decision']}\n\nAI reason: {d['reason']}",'Student judgment: **PENDING**\n\nAgree/disagree and why: **PENDING**\n\nCorrection and exact supporting evidence: **PENDING**'])
  accepted=sum(x['decision']=='accept' for x in selected);other=len(selected)-accepted
  text.append(f'Sample coverage: {accepted}/3 accepted and {other}/3 rejected or deferred. Collect more candidates if incomplete; do not invent decisions.')
  text.extend(['## Policy revision','Original policy and outputs: **PENDING student review**\n\nChange and reason: **PENDING**\n\nRerun comparison and outcome: **PENDING**','## Final approval','Only the student supplies approval.json after reviewing the actual current drafts and review_id.'])
  (r/'student_review.md').write_text('\n\n'.join(text));st.data['output_count']=len(selected)
entry(main)
