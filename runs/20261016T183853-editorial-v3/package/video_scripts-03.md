# Build an experiment another person can check

Research Loop · Google Vids script draft  
**As of: 2026-10-15 (UTC)**  
Evidence window: 2026-09-16 through 2026-10-15, inclusive.  
Approximately 600 spoken words; approximately 4–5 minutes. Scene timings are proposed edit positions, not source timestamps. Use narration verbatim for subtitles. Simple diagrams and excerpt cards; no avatar.

### Scene 1 · What actually changes? · 0:00–0:40
<!-- 03-c1 -->
**Narration**

What should you delegate to a research agent, and how will someone check the result? Start by identifying what the agent can change. In AI Code King’s tutorial, the optimizer changes workflow instructions. The underlying model stays the same, and the grading rules stay fixed. So its “self-training” framing means instruction optimization here, not training model weights. That distinction defines the experiment: you are testing changes to instructions under unchanged grading rules.

**Visual**

Title and as-of date, followed by three boxes: “Model: unchanged,” “Instructions: editable,” and “Grading: fixed.” Badge: “Source procedure; no measured gain established.”

[AI Code King](https://www.youtube.com/watch?v=wMQB33rM28I) — **source recording timestamps:** 00:56.800–01:01.780 (s00011); 04:30.980–04:35.980 (s00056). Provisional transcript excerpt: “The grading rules stay fixed.”

### Scene 2 · Keep comparison tasks outside the search · 0:40–1:20
<!-- 03-c2 -->
**Narration**

The tutorial recommends comparing the original and optimized instructions on tasks excluded from the search. Then a person reviews the winning instruction changes. If that person edits the instructions, the edited version becomes a new candidate requiring evaluation. Human cleanup changes what was tested. This is procedural advice, not an observed improvement: the supplied tutorial evidence contains no inspectable measured gain. An ambiguous passage about rerunning is excluded pending audio review, and the automatic transcript remains provisional.

**Visual**

Diagram: “Instruction search → Frozen candidate → Held-out comparison → Human review.” An arrow from “Human edits” returns to “New candidate → Evaluation.”

[AI Code King](https://www.youtube.com/watch?v=wMQB33rM28I) — **source recording timestamps:** 10:49.900–10:53.820 (s00141); 13:29.460–13:34.140 (s00176); 13:34.140–13:38.780 (s00177). Provisional excerpt: “treat that edited version as a new candidate that needs checking.”

### Scene 3 · Budget for documentation · 1:20–2:00
<!-- 03-c3 -->
**Narration**

Campus Talks adds a researcher perspective: connect data to its provenance, share variable descriptions and executed analysis code, and allow extra planning time. Sharing should be appropriate and ethical. Our interpretation for agent experiments is to budget documentation alongside execution. Preserve enough context for another researcher to understand what happened. This podcast offers guidance, not a tested agent intervention. Its automatic transcript is provisional, and the guests’ report and journal roles carry professional interests. Their advice is not independent performance validation.

**Visual**

Diagram: “Data → Provenance → Variable descriptions → Executed code,” beside a planning calendar. Badge: “Researcher guidance → editorial application.”

[Campus Talks](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) — **source recording timestamps:** 16:14.680–16:17.600 (s00291), 16:17.600–16:20.000 (s00292); 39:07.310–39:10.510 (s00748); 41:08.670–41:11.870 (s00799); 41:13.710–41:16.430 (s00801); 54:36.070–54:40.270 (s01090). Provisional excerpt: “build extra time into your planning.”

### Scene 4 · Check individual claims · 2:00–2:40
<!-- 03-c4 -->
**Narration**

ResearchFlow-Eval’s authors report that fourteen of ninety end-to-end claims met their criteria. Only one empirical claim was met. These are findings within their evaluation, which uses one anchor task, not a universal success rate for research agents. A domain researcher spot-checked the AI judge’s ratings and rationales. Our practical inference is to retain human review of AI judgments, especially when a model judges its own output. That is a safeguard; it does not establish that judge bias occurred.

**Visual**

Show “14 / 90 claims met” and a separate annotation: “Only one empirical claim met.” Do not depict these as independent replications. Badge: “Authors’ reported result; one anchor task.”

[ResearchFlow-Eval](https://arxiv.org/abs/2610.18088) — **text locators:** Appendix G, opening paragraph before Table 15 and reference to Table 16; §3.3, “LLM judge”; §6, limitations. Excerpt: “A domain researcher spot-checked the judge’s ratings and rationales”.

### Scene 5 · Record how results were selected · 2:40–3:10
<!-- 03-c5 -->
**Narration**

ResearchFlow-Eval permits optimization using test sessions, but requires every test access to be logged with its purpose, configuration, and result. Results that informed optimization cannot be described as untouched or unbiased estimates. Our recommendation follows that distinction: record when evaluation data influenced selection. A reader needs both the result and its selection history. This study’s test-access policy also limits how its findings should be interpreted as held-out evidence.

**Visual**

A simple log: “Purpose | Configuration | Result | Influenced selection?” Arrow from “Used for optimization” to “Disclose in result.”

[ResearchFlow-Eval](https://arxiv.org/abs/2610.18088) — **text locator:** task-package passage headed “Data and test access.” Excerpt: “test results that informed optimization may not be described as untouched or unbiased estimates.”

### Scene 6 · Simple orchestration still needs accounting · 3:10–3:55
<!-- 03-c6 -->
**Narration**

Minimal orchestration does not establish low cost. Malena’s authors modeled its GLM 5.2 inference cost at twelve dollars and twelve cents, versus one dollar and ninety-five cents for AiScientist. Real cache-hit counts were unavailable. These are modeled inference costs, not complete measured expenditure. The supplied source also contains an unresolved inconsistency: its claim of matching or beating every tested pair conflicts with a table entry. We therefore draw no best-result conclusion. Measure your own resource use instead of adopting these figures as a complete budget.

**Visual**

Two cost cards, prominently labeled “Authors’ modeled inference cost”: “Malena: $12.12” and “AiScientist: $1.95.” Keep “Actual cache-hit counts unavailable” visible.

[Malena paper](https://arxiv.org/abs/2609.40303) — **text locators:** §5.1, paragraph discussing Figure 3’s inference costs; Appendix A.4, cache-read modeling paragraph. Excerpt: “none of the harnesses compared here report real cache-hit token counts directly”.

Uncertainty card: “Supplied results table, Kimi-K3 row: Malena 26.7%; AiScientist 27.1%. Adjacent headline text says Malena ‘matches or beats every harness on every tested pair.’ Unresolved.” Do not present this as proof of comparative superiority.

### Scene 7 · What to build, and what to watch · 3:55–4:35
<!-- 03-c7 -->
<!-- 03-c1 03-c2 03-c3 03-c4 03-c5 03-c6 -->
**Narration**

Our editorial recommendation is a small, auditable experiment: fixed grading, held-out comparisons, recorded provenance, human review, and complete resource accounting. This protocol is an inference, not a validated guarantee. Next, watch for evaluations on additional research tasks, claim judgments linked to evidence, and improvements that transfer to held-out work. Those would make future reports more useful than another unqualified success score. None alone guarantees replication. The goal is an experiment another researcher can reconstruct, including how its result was selected.

**Visual**

Checklist diagram of the five proposed practices. Badge: “Editorial interpretation; not a validated guarantee.” End card: “Can another researcher reconstruct the result—and its selection history?”

[ResearchFlow-Eval](https://arxiv.org/abs/2610.18088) — **text locators:** §3.3, “LLM judge,” evidence locations and rationale; §6, final future-work sentence about additional systems, models and anchor papers. Excerpt: “the locations of the supporting evidence and a short rationale”.

[AI Code King](https://www.youtube.com/watch?v=wMQB33rM28I) — **source recording timestamps:** 11:35.580–11:41.740 (s00152); 11:41.740–11:47.580 (s00153). Provisional excerpt: “we haven't demonstrated a transferable improvement.”

### YouTube description — draft

How can student researchers make agent experiments checkable? Research Loop examines instruction optimization, held-out comparisons, provenance, claim-level evaluation and resource accounting.

As of **2026-10-15 (UTC)**. Frozen evidence window: September 16–October 15, 2026. This is an editorial synthesis of supplied evidence, not a new live collection. Reported findings remain attributed to their authors; the proposed student protocol is interpretation, not a replication guarantee.

Companion article, currently unpublished: **[ARTICLE_URL_PENDING_PUBLICATION]**

Sources and locators:

- [AI Code King tutorial](https://www.youtube.com/watch?v=wMQB33rM28I): source recording timestamps 00:56.800–01:01.780; 04:30.980–04:35.980; 10:49.900–10:53.820; 11:35.580–11:47.580; 13:29.460–13:38.780.
- [Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/): source recording timestamps 16:14.680–16:20.000; 39:07.310–39:10.510; 41:08.670–41:11.870; 41:13.710–41:16.430; 54:36.070–54:40.270.
- [ResearchFlow-Eval](https://arxiv.org/abs/2610.18088): §3.3 “LLM judge”; §6; task-package “Data and test access”; Appendix G and Table 16.
- [Malena paper](https://arxiv.org/abs/2609.40303): §5.1, Figure 3 cost discussion and results-table inconsistency; Appendix A.4, modeled cache costs.

Limitations: automatic transcripts remain provisional. The tutorial does not establish measured improvement; podcast guidance is not a tested intervention. ResearchFlow-Eval uses one anchor task and permits logged test access during optimization. Malena’s costs are modeled, and its supplied comparative-results inconsistency remains unresolved. These sources do not independently validate the proposed combined protocol.

AI-assistance disclosure: AI assisted in drafting and organizing this script from supplied evidence. Final editorial approval remains with the student. This draft does not establish that full-source review, audio verification, video production or publication is complete.