# Project05 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P-1 | Project05 has a current plan-of-record that supersedes stale Project03/early Project05 layout assumptions. | Read `project-plan.md` and confirm it names Project04 as closed/current authority and marks old artifacts as evidence. | serious | operator reorientation | open | | |
| P-2 | `document-extraction` is implemented as a live installable skill. | Confirm `knowledge/document-extraction/SKILL.md`, sibling guides/support files, package target, generated zip, and install surface exist. | serious | operator reorientation | open | | Nondeferrable. |
| P-3 | `concept-cards` is implemented as a live installable skill. | Confirm `knowledge/concept-cards/SKILL.md`, sibling guides/support files, package target, generated zip, and install surface exist. | serious | operator reorientation | open | | Nondeferrable. |
| P-4 | The skills use the current post-Project04 sibling-directory layout rather than burying templates/examples/reference material under `guides/` by default. | Inspect source tree and generated zips for `guides/`, `templates/`, `examples/`, and `version-history.md` placement. | correctness-grade | operator correction | open | | |
| P-5 | `concept-cards` routes document cleanup/extraction work to `document-extraction` and consumes its outputs as upstream provenance. | Grep `knowledge/concept-cards` for routing language and verify examples/templates use document-extraction output contracts where relevant. | serious | operator reorientation | open | | |
| P-6 | Historical v3.2, Project03, old PDF/EPUB prompts, and Project05 architecture artifacts remain preserved as provenance and are not mistaken for current instructions. | Inspect Project05 artifacts README, reorientation artifact, and concept/document skill version histories. | correctness-grade | project continuity | open | | |
| P-7 | Packaging, docs, and validation surfaces include both new skills. | Run or inspect `make check-skills`, skill package targets, `make check-package-paths`, generated zip contents, install smoke, and docs/skill-library updates. | serious | repository gate | open | | |
| P-8 | Project05 closes without deferring key objectives P-2 or P-3. | Read final project closing report and verify any deferrals exclude the nondeferrable objectives unless explicitly operator-approved. | serious | operator reorientation | open | | |

Rows: 8. Open: 8. Done: 0. Deferred: 0. No-op: 0.
