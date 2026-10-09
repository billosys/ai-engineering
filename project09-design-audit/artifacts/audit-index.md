# Design audit index

Date: 2026-10-08, America/Chicago.

Repository: `/Users/oubiwann/lab/billosys/ai-engineering`.

Source baseline: `dffa504e851b03b8e4746f1941068e4cc850b612` (`main`).

This is a user-requested qualitative audit of `knowledge/design`, applying the audit method to design guidance and illustrative CSS. It is not a repository-wide language audit. Other language/tooling domains are outside scope, rather than silently unreviewed portions of the design findings.

- [Findings and evidence](audit-results-design.md): 16 findings, comprising 7 High, 8 Medium, 1 Low, no Blockers.
- [Current reference systems and release proposals](audit-modernization-synthesis.md): 1.5 foundation repair and 2.0 unified design practice; Project10/Project11 release scope, with shared audit ownership in Project09.

## Audit map

| Boundary | Contents | Review |
| --- | --- | --- |
| Live skill | Entrypoint, six guides, one history; 4,114 lines | Complete reading and cross-guide review. |
| Generated package | Eight files, 166,519 uncompressed bytes | Fresh `make design`, exit 0; inspected package content and unchanged entrypoint. |
| Sources | 156 Practical Typography Markdown pages; four articles; one conversion report | Complete inventory; targeted source reading. |
| Cards | 112 Arnheim; 46 posts; 37 Practical Typography; 19 Munsell; 19 Tschichold | Complete inventory/search; targeted substantive checks, not full semantic certification. |
| Integration | Makefile, staging helper, README/skill-library route, exception registry | Focused inspection for package contents and guide routes. |
| External practice | Material, Carbon, Polaris, Spectrum, Fluent, GOV.UK, USWDS; W3C/DTCG and selected original sources | Targeted primary-source research, checked on audit date. |

The skill's architecture is stated in its entrypoint and manifesto. The audit traverses claims/expressions, guides, connected visual subsystems, the whole skill, and its package/repository boundaries. No executable application exists in this scope. Actual product usability, browser accessibility and all-card semantic verification remain unassessed.

The dominant cross-cutting findings are brand contamination (DES-001), unsupported universality (DES-002), an inadequate accessibility floor (DES-005/006), evidence and package disconnects (DES-010/013), and a workflow that omits problem framing and validation (DES-014).

The original audit changed no skill source, historical source/card material, canonical planning artifact or unrelated work. At the Operator's subsequent request, these reports moved from the Git-ignored `workbench/` into this project's shared `artifacts/` home, with undated filenames. [The relocation record](artifact-relocation.md) identifies the original hashes and administrative changes. [Project09](../project-plan.md) owns the audit; [Project10](../../project10-design-foundations/project-plan.md) owns the 1.5 repair, and [Project11](../../project11-unified-design-practice/project-plan.md) owns the 2.0 expansion. The skill source remains unchanged; no release has been published.
