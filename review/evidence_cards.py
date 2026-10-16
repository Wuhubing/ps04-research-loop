"""Prepare a readable audit trail; this report does not grant approval."""
from common import *

def main():
 r=runarg();items={(x['item_id'],x['version_id']):x for x in lines(r/'eligible.jsonl')}
 with Stage('evidence_cards',r) as st:
  out=['# Evidence review cards','Draft audit aid. Every media passage still requires listening against the original recording. Check interpretation and independence, not just string matches. No student approval is recorded here.']
  for b in lines(r/'briefs.jsonl'):
   out+=['## '+b['piece_id']+' — '+b['title'],b['argument']]
   for c in b['claims']:
    out+=['### '+c['claim_id'],c['type']+': '+c['statement']]
    for ref in c['evidence']:
     x=items[(ref['item_id'],ref['version_id'])];loc=ref['locator'];url=x['url'];passage=loc.get('quote','');timing='Written passage'
     if loc['type']=='segment':
      segment=next(s for s in read(safe(x['segments_path'])) if s['segment_id']==loc['segment_id'])
      timing=f"{segment['start_seconds']:.2f}–{segment['end_seconds']:.2f} seconds ({segment['segment_id']})";passage=segment['text']
      if x['kind']=='youtube':url+='&t='+str(int(segment['start_seconds']))+'s'
     out.append(f"[{x['title']}]({url}) · {timing}\n\nOrigin: `{x['publisher_id']}` · Version: `{x['version_id']}`\n\nSaved evidence: `{x['text_path']}`\n\n> "+passage.replace('\n','\n> '))
     st.data['output_count']+=1
  (r/'evidence_review.md').write_text('\n\n'.join(out)+'\n')
  usage=[];briefs=lines(r/'briefs.jsonl')
  for decision in lines(r/'decisions.jsonl'):
   key=(decision['item_id'],decision['version_id']);item=items[key]
   claims=[{'piece_id':b['piece_id'],'claim_id':c['claim_id']} for b in briefs for c in b['claims'] if any((ref['item_id'],ref['version_id'])==key for ref in c['evidence'])]
   usage.append({'item_id':key[0],'version_id':key[1],'title':item['title'],'decision':decision['decision'],'suggested_piece_ids':decision['piece_ids'],'actual_piece_ids':sorted({c['piece_id'] for c in claims}),'claims':claims,'usage_state':'cited' if claims else 'accepted_not_cited' if decision['decision']=='accept' else 'not_selected'})
  write(r/'source_usage.json',usage)

if __name__=='__main__':entry(main)
