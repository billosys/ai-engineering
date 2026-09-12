# Slice03 Plan: Feedback-Driven Skill Refinement

```yaml
project: project05-concept-card-skill
arc: arc07-real-corpus-uat-and-feedback
slice: slice03-feedback-driven-skill-refinement
status: cc-proposed-done
opened: 2026-09-11
depends-on:
  - slice02-pilot-markdown-preparation-and-card-extraction
```

## Goal

Disposition every Slice02 pilot finding as an accepted source refinement,
checked no-op, or follow-on boundary, then run the relevant gates. The purpose
is to convert real-use friction into skill quality without silently widening
Project05 into runtime retrieval, graph database, MCP server, or whole-corpus
implementation work.

## Artifact Home

Durable Slice03 artifacts live under:

```text
arc07-real-corpus-uat-and-feedback/slice03-feedback-driven-skill-refinement/artifacts/
```

Expected artifact groups:

- `finding-disposition.md`
- `source-change-summary.md`, if source files change
- `no-op-and-follow-on-decisions.md`
- `validation-evidence.md`

## In Scope

- Read Slice02 `friction-log.md`, candidate records, support records,
  preparation records, review packet, and CDC verification.
- Disposition all findings F-1 through F-7.
- Make narrow source updates when a finding exposes a real guidance gap in
  `document-extraction` or `concept-cards`.
- Update affected skill version metadata and sibling `version-history.md`
  when source skills change.
- Preserve explicit no-op decisions when current guidance already covers a
  finding.
- Preserve follow-on boundaries for runtime retrieval, graph/RAG/MCP, memory
  admission, or expanded evaluation work.
- Run relevant source/package/Markdown/version gates for every changed surface.
- Update planning ledger evidence and closing report.

## Out Of Scope

- Operator acceptance of any candidate card.
- Expanded corpus card generation.
- Whole-bibliography resolution.
- Production graph database, GraphRAG, MCP server, vector store, memory
  runtime, retrieval evaluation, or memory admission.
- Broad style rewrites of either skill.
- Treating Slice02 findings as accepted defects without checking the current
  skill text.

## Finding Disposition Requirements

Every finding must end in exactly one of:

- **refinement:** source change made, with file paths, rationale, version
  bump/history, and validation evidence;
- **no-op:** current guidance already covers the issue, with quoted or linked
  evidence from the current source;
- **follow-on:** outside Slice03 source-refinement scope, with owner,
  re-entry condition, and why it must not be done in this slice.

## Verification

- Inspect `finding-disposition.md` and confirm F-1 through F-7 are all present.
- Inspect any source diffs for narrowness, skill ownership, version-history
  compliance, and package-boundary preservation.
- Run `git diff --check`.
- Run `make check-skills` if any `SKILL.md` metadata or description changes.
- Run `make check-skill-versions` if any skill version or history changes.
- Run `make check-package-paths` if packaged links, support files, or package
  contents change.
- Run targeted Markdown link/path checks for changed Markdown when no broader
  package gate applies.
- Inspect source and planning `git status --short --untracked-files=all`.

## Exit Criteria

This slice exits when every Slice02 finding has a durable disposition, every
accepted source change has matching validation/version evidence, no-op and
follow-on decisions are explicit, and Arc07 is ready either for expanded corpus
card generation or for an operator-approved adjustment to that path.
