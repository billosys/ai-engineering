# Code Auditing Version History

## Version 1.1.0 - 2026-09-05

Split the former CODE-AUDIT guide into five focused guides:
`01-audit-scope-and-map.md`, `02-findings-and-severity.md`,
`03-scale-aware-auditing.md`, `04-modernization-synthesis.md`, and
`05-audit-to-hardening-handoff.md`. The old CODE-AUDIT path was renamed with
Git history to `01-audit-scope-and-map.md` and is no longer a live route or
package entry.

## Version 1.0.1 - 2026-09-04

Normalized the component history into this sibling file for Arc08 Slice05.
The audit guide remains unsplit in this slice; its former embedded history is
preserved below as component lineage. Future changes to `SKILL.md`, `guides/`,
`templates/`, or `examples/` for this component should be recorded here.

## Code Audit Lineage

### Version 1.1 - 2026-08-27

Added the multi-scale audit model: audit mapping, explicit scale coverage from
line/function through workspace/monorepo, stable finding IDs, scale labels on
findings, architecture/coherence and modernization categories, coherence
observations, and the evidence-backed modernization synthesis.

### Version 1.0 - 2026-04-23

Initial version. Added the whole-repo, per-language code audit prompt with
language detection, skill-backed review, severity-graded file:line findings,
top-level index, and diagnosis-only stance.
