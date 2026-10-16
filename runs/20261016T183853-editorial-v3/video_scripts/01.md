# What changed: agents can run bounded research loops

**Research Loop · Google Vids script draft**  
**As of: 2026-10-15 (UTC)**  
**Evidence window: 2026-09-16–2026-10-15, inclusive; frozen collection**  
**Estimated runtime:** 4 minutes at approximately 130 words per minute. Narration only is intended to be spoken and used for subtitles. Visual directions and citations are not spoken. No avatar required.

### Scene 1 — Who controls the experiment?
<!-- 01-c6 -->

**Narration**

Which research tasks can you delegate to an agent while keeping responsibility for the experiment? Our interpretation of these reports is a practical division of work. Agents can execute bounded changes and record attempts. Humans define the scientific objective and decide which candidates deserve larger validation runs. That is bounded delegation, not evidence of fully autonomous discovery. We will look at a protein model recipe, a shared experiment history, and a physical laboratory account. They offer different perspectives, rather than independent replications of one result.

**Visual**

Show title and exact as-of date. Draw: “Human: objective” → “Agent: bounded iterations + records” → “Human: validation decision.” Label **Interpretation**. Cite [NanoProteinLM](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/), “Building hill-climbable environments for research tasks,” table rows “Research objective” and “Validation”; and [Agora](https://arxiv.org/abs/2609.18094), “Negative results,” excerpt beginning “The graph also records what did not work.”

### Scene 2 — A result with a human gate
<!-- 01-c1 -->

**Narration**

First, the protein model example. Li and Lu report that long-range contact precision increased from 28.2 percent to 36.6 percent at the same 48.4-billion-token budget. A human chose which recipes to scale up. That gate matters: this was a human-guided result. Contact precision is a proxy for downstream protein folding, so the reported improvement should retain that qualification. It is an author-reported result at a matched token budget, not evidence that agents generally deliver faster, cheaper, or independently validated scientific discoveries.

**Visual**

Use two bars on a common zero-based scale: “28.2%” and “36.6%.” Underneath: “Same 48.4B-token budget · Author-reported proxy result.” Add a human decision diamond before scaling.

Source: [NanoProteinLM](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/), “A better PLM recipe by hill-climbing NanoProteinLM,” paragraph beginning “Starting from the ESMC recipe.” Display excerpt: “with a human deciding which recipes to scale up.” Proxy qualification: “Failure mode: Perfect on reward, failure on science.”

### Scene 3 — An inspectable research history
<!-- 01-c2 -->

**Narration**

Agora describes a different part of the research process: shared experiment memory. Agents pick a parent, check out its exact code commit, make a change, evaluate it, and record the result with material needed for reproduction. This gives later work a traceable starting point. Keep the chronology straight, though. The reported run took place from April 26 to May 8. Its September publication falls within our evidence window; the experiment itself does not. A recent report can document older work without making that execution a new event.

**Visual**

Animate a simple loop: “Exact parent commit → Change → Evaluate → Commit and record.” Label **Authors’ workflow description**.

Source: [Agora](https://arxiv.org/abs/2609.18094), §4.3 “Research loop.” Display excerpt: “fetch and check out that exact commit.” Separate calendar cards: “Execution: April 26–May 8” and “Publication: September 16, 2026.” These are dates, not recording timestamps.

### Scene 4 — Records do not settle validation
<!-- 01-c3 -->

**Narration**

An experiment history is not the same as independent validation. Agora’s authors describe human interventions during the run, including server changes and a worker prompt change. Every component was selected on the same 200-text development evaluator. The authors also say they did not rerun the winning method. Their primary result is archived evaluator output, supported by agents’ cross-hardware reproductions. Our inference is limited: the history documents the process, but does not establish independent validation. Keep the record of what happened separate from the question of whether the result generalizes.

**Visual**

Show three evidence cards: “Human interventions,” “One development evaluator,” and “No fresh author rerun.” Label the conclusion **Interpretation: independent validation not established**.

Source: [Agora](https://arxiv.org/abs/2609.18094), §4.7 “Human intervention”; “Primary result,” excerpt “Every component was selected on the same 200-text development evaluator”; §4.8 “How we verified the record,” excerpt “We did not rerun the winning method.”

### Scene 5 — Physical labs: an interested perspective
<!-- 01-c4 -->
<!-- 01-c5 -->

**Narration**

For a physical laboratory contrast, Periodic Labs’ founders say characterization shifted substantially toward AI assistance, while campaign guidance became a mixture of human and AI work. They explicitly call full autonomy a non-goal. They also describe taking their tools to industry partners, so this is a commercially interested operational perspective. It describes their workflow, not a measured productivity gain. The supplied transcript is provisional, and the evidence contains no controlled measurements or inspectable execution logs for that account. Treat it as testimony about how they organize work, with those uncertainties attached.

**Visual**

Draw two boxes: “Characterization: shift toward AI assistance” and “Campaign guidance: human + AI.” Label **Founders’ account · Provisional transcript**. Display transcript excerpt: “full autonomy is a non-goal.”

Source: [Periodic Labs interview](https://www.latent.space/p/periodic) · [Recording](https://api.substack.com/feed/podcast/219146438/4de3baad7036438bcc048cc532556c6a.mp3).

Exact recording timestamp labels from supplied segments:

- **01:04:24–01:05:04** — s00305: characterization and campaign guidance.
- **00:50:46–00:51:39** — s00230: autonomy as a non-goal.
- **01:15:06–01:16:53** — s00341: commercial deployment to industry partners.

### Scene 6 — A boundary students can use
<!-- 01-c6 -->

**Narration**

For your next small computational experiment, our practical recommendation is to fix the scientific objective before search. Let the agent make bounded changes and preserve failed attempts alongside successful ones. Then retain the decision about which candidates deserve larger validation runs against the baseline. This recommendation combines the protein account’s human gate with Agora’s reusable history. It does not promise portable speed, cost, or discovery gains. The useful question is concrete: what will the agent execute, what evidence will it preserve, and what will you require before trusting the result?

**Visual**

Return to the opening diagram. Add a branch for “Failed attempts retained” and a final gate marked “Larger validation against baseline.” Label **Practical interpretation**.

Sources: [NanoProteinLM](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/), “Building hill-climbable environments for research tasks,” “Research objective” and “Validation” rows; [Agora](https://arxiv.org/abs/2609.18094), “Negative results.” Display excerpt: “The graph also records what did not work.”

### YouTube description — draft

Which research tasks can students delegate to agents while retaining responsibility for the experiment? Research Loop examines author-reported protein model results, Agora’s shared experiment history, and Periodic Labs’ account of AI-assisted laboratory work.

The evidence supports bounded delegation, with human objectives and validation decisions. It does not establish fully autonomous discovery or portable speed and cost gains. The protein result is a proxy improvement; Agora’s history does not establish independent validation; Periodic’s commercially interested testimony uses a provisional transcript.

**As of:** 2026-10-15 UTC. **Frozen evidence window:** September 16–October 15, 2026. Agora’s reported execution occurred April 26–May 8, before this publication window.

**Article:** [UNPUBLISHED_ARTICLE_URL]

**Sources and locators:**

- [Li and Lu: NanoProteinLM](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) — “A better PLM recipe by hill-climbing NanoProteinLM”; “Building hill-climbable environments for research tasks”; “Failure mode: Perfect on reward, failure on science.”
- [Agora](https://arxiv.org/abs/2609.18094) — §4.3, “Negative results,” “Primary result,” §4.7 and §4.8.
- [Periodic Labs interview](https://www.latent.space/p/periodic) — recording 00:50:46–00:51:39, 01:04:24–01:05:04 and 01:15:06–01:16:53. Transcript provisional.

**AI-assistance disclosure:** AI assisted in drafting this script and description from supplied excerpts and an editorial brief. This disclosure does not indicate completed human review, audio verification, video production, or publication. Editorial approval remains with the student.