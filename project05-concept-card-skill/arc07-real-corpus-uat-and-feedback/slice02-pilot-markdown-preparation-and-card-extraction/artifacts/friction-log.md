# Pilot Friction Log

| ID | Area | Observation | Severity | Suggested Slice03 disposition |
| --- | --- | --- | --- | --- |
| F-1 | Markdown preparation | Existing authored Markdown made preparation light, but stable line locators still need a pinned file hash and heading context to survive future edits. | moderate | Evaluate whether the Markdown guide should show the combined hash/heading/line locator convention; otherwise record explicit no-op. |
| F-2 | Citation handling | The chapter frontmatter names `ccnlab.bib` while the repository inventory identifies `references.bib`; citation-key resolution could not be assumed. | serious | Add or clarify a Markdown-source dependency checklist only if the current guidance is insufficient; do not invent a bibliography mapping. |
| F-3 | Figure handling | Figure references are easy to mistake for claim support. Directly viewing two assets was feasible but does not scale to all figures. | serious | Assess whether the support template/example needs a clearer figure-inspection versus caveat example. |
| F-4 | One-concept boundary | Pattern separation, sparseness, overlap, and interference are tightly coupled, making a single-card boundary debatable. | moderate | Review whether an existing example should demonstrate split-versus-retain reasoning; preserve as a no-op if current guidance already suffices. |
| F-5 | Qualification retention | The consolidation passage combines an on-balance conclusion with explicit uncertainty, creating a high risk of overstated summary. | serious | Evaluate whether extraction guidance needs a qualified-claim example; do not change source guidance before review. |
| F-6 | Review burden | A small four-card set is reviewable, but meaningful review still requires access to the exact checkout and dependency notes. | moderate | Carry the pinned-source and review-packet requirement into any expanded run; no runtime solution is implied. |
| F-7 | RAG handoff | Provenance and lifecycle fields are sufficient to describe a later projection, but do not establish retrieval quality or runtime readiness. | serious | Preserve current runtime boundary; route any retrieval evaluation to a separate project/slice. |

All findings are observations for Slice03 disposition, not accepted defects in
either source skill. No source-skill change is proposed or made in this slice.
