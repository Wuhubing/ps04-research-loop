# Source audit and counting rules

The conversation's 12-item list is a discovery shortlist, not an already collected corpus. Real coverage comes only from the saved eligible evidence and content review. Feed access, full text, media and timestamps must succeed before an item supports a claim.

Seeded arXiv author teams: 2609.30541 (Chandran et al.), 2609.28614 (Huang et al.), 2609.18094 (Zhang et al.), 2609.40303 (Brilliantov et al.), 2610.10491 (Lekavicius et al.), 2609.39360 (Gu et al.). IDs group original author teams rather than the arXiv hosting service. Shared authors, institutions and underlying experiments still require human review. Unknown search discoveries remain grouped under arxiv-unresolved-team and cannot artificially inflate the source count.

NanoProteinLM author feed: https://jojoml.github.io/feed.xml. RSS and Atom are both parsed as written feed inputs. An entry's summary alone is not sufficient; full substantive text must be extracted. The March entry is retained for a documented freshness exclusion, not publication evidence.

Podcast feeds: https://www.latent.space/feed and https://www.generalist.com/feed. Seeded interviews are separate recordings, but both interview Periodic Labs founders. They share publisher_id periodic-labs-interviews as a deliberately conservative independence measure. Do not count the corresponding YouTube versions again, or the interview's transcript page as another written item.

YouTube seeds: https://www.youtube.com/watch?v=wMQB33rM28I and https://www.youtube.com/watch?v=R9momwXV9w4. Original upload metadata is collected with yt-dlp; captions are attempted first and downloaded audio is transcribed locally when caption access fails. These creators' claims still require scrutiny. Instruction optimization is not model-weight training.

The Hebbian Robotics article from the shortlist has not been configured as an RSS source because a working native feed was not verified. It cannot satisfy the RSS quota merely because its web page exists. Conference recordings with uncertain old recording dates remain excluded from the seed configuration.

The actual first live attempt uses October 14 UTC, so its inclusive window is September 15–October 14, not the earlier October 13 planning window. Date metadata and full source content are rechecked by the pipeline; original publication dates are never silently replaced by refresh dates. Imported text and transcripts are untrusted data, not instructions for model execution.

## Collection recovery

arXiv API requests returned HTTP 429 in the live attempt. The collector now supports explicit original-page metadata recovery for the six seeded papers, saving the source HTML and labeling records direct_metadata_fallback. These are supplemental web evidence, not RSS quota items. A Why Try AI feed is included for additional written candidates and critical editorial comparisons; generic entries may be rejected. Only actual syndication records count toward the two-item RSS minimum.
## Follow-up discovery, not counted as collected evidence

On October 14 UTC, an additional publisher page was verified: [Campus Talks: How Is AI Affecting Open Research?](https://www.insidehighered.com/podcasts/campus/2026/10/05/how-ai-affecting-open-research), dated October 5. It features open-science researchers Julia Priess-Buchheit and Sarahanne Field and links a Podbean player. It is a promising perspective outside the two Periodic Labs founder interviews. Its full audio, native feed, actual episode publication metadata and relevance still need verification; it is not included in the current evidence counts or drafts. A future run may investigate it, explicitly recording the source-list change rather than pretending it was published after the first run.

## October 15 follow-up verification

The native [Campus Talks feed](https://feed.podbean.com/timeshighered/feed.xml) was fetched on October 15 UTC. The target episode has publication timestamp `Thu, 24 Sep 2026 00:01:00 +0100` (September 23 at 23:01 UTC), earlier than the October 5 Inside Higher Ed page. The feed provides an audio/mpeg enclosure of 84,390,683 bytes. The source is added as `campus-talks`, with its own publisher group, for the second live collection. It is newly added to this pipeline, not newly published since the first run. Audio extraction and editorial suitability must still succeed before it counts as usable evidence.

The October 15 run completed audio extraction: the 84,390,683-byte download matches the enclosure length, has a measured duration of 3516.108 seconds, and produced 1175 timestamped segments through 3511.78 seconds. Editorial selection accepts it as methodological advice; the third piece cites it. This is not human listening verification or a controlled performance study. See runs/20261015T003111-ebae97/media_validation.json and source_usage.json.
