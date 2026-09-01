# CC Prompt: Arc05 Slice05 Implementation Plan Synthesis and Project Close Input

You are CC implementing Project03 Arc05 Slice05 in the planning worktree.

Work only under:

`project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/`

Do not edit the source checkout at
`/Users/oubiwann/lab/billosys/ai-engineering`. Do not create or edit
`cdc-verification.md`; CDC owns that file after your close.

## Context

Read these files before writing:

- `project03-concept-card-method/project-plan.md`
- `project03-concept-card-method/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/arc-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/slice-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/slice01-source-surface-inventory/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-source-layout-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-schema-surface-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-validation-review-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/artifacts/v40-package-update-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/artifacts/v40-release-gate-plan.md`

Preserve verified Slice01 through Slice04 outputs and accepted Arc03/Arc04
decisions. This is the final Arc05 planning slice: it prepares Arc05 close and
Project03 close input, but it does not close either scale.

## Task

Create the required Slice05 artifacts:

- `artifacts/v40-implementation-plan.md`
- `artifacts/v40-source-edit-sequence.md`
- `artifacts/v40-verification-gate-matrix.md`
- `artifacts/v40-implementation-slice-recommendations.md`
- `artifacts/v40-deferral-register.md`
- `artifacts/project03-close-input.md`

Update:

- `ledger.md`
- `closing-report.md`

The implementation plan should synthesize verified Slice01 source-surface
inventory, Slice02 source layout/content sequence, Slice03 schema/enum/
validation plan, and Slice04 package/discoverability/release-gate plan. It
must preserve accepted Arc03 and Arc04 decisions.

The source edit sequence should cover `knowledge/concept-card-method/SKILL.md`,
`guides/`, templates, examples, validation documentation, support documents,
README, Makefile, package lists, package-path behavior, generated zip
verification, and source version-history obligations.

The verification gate matrix should cover source checkout cleanliness,
planning checkout hygiene, `make check-skills`, `make concept-card-method`,
generated zip listing, `make check-package-paths`, installability,
documentation-only validator scope, README/library discoverability, and
version-history checks.

The implementation-slice recommendations should split future source edit work
into bounded slices with inputs, outputs, source paths, checks, and commit
boundaries.

The deferral register should record deferred work with owner, rationale, and
re-entry condition, especially executable validator-code, runtime services,
GraphRAG, graph database, ontology database, memory runtime, CCDP service,
live extraction, package release, and generated release artifacts.

The Project03 close input should evaluate Definition of Done coverage, Arc05
close readiness, Project03 close readiness, remaining deferrals, and closure
evidence. It should support Arc05 close without claiming that planning has
implemented or released the skill.

## Scope Fences

Do not:

- edit source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, validator-code, generated-zip, or release files;
- implement the concept-card method skill, Makefile targets, package list
  edits, package-path exception rows, README/library prose, tests, generated
  zips, package release, executable validator-code, release gates, CI changes,
  or source version-history text;
- create runtime services, GraphRAG, graph database, ontology database, memory
  runtime, CCDP service, or live extraction behavior;
- close Arc05 or Project03.

## Verification

Run the Slice05 ledger checks from this directory:

`project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/`

Also run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`
- strict ASCII and trailing-whitespace checks over Slice05 Markdown.

The closing report must include:

- row-by-row disposition for F-1 through F-13;
- `Rows: 13. Done: 13. Deferred: 0. No-op: 0.` unless a row is explicitly
  deferred or no-op with rationale;
- artifact inventory;
- Bubble-Up section stating whether Slice05 requires Arc05 re-sequencing, a
  remediation slice, an arc-scope correction, or Project03 roadmap correction;
- explicit statement of whether Arc05 is ready for formal arc close after CDC
  verification.

## Expedited Commit Requirement

After verification passes, commit your changes. Stage only these explicit files:

```sh
git add \
  project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-implementation-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-source-edit-sequence.md \
  project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-verification-gate-matrix.md \
  project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-implementation-slice-recommendations.md \
  project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-deferral-register.md \
  project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/project03-close-input.md \
  project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/ledger.md \
  project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/closing-report.md
```

Then commit:

```sh
git commit -m "Close Arc05 implementation plan synthesis" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>"
```

If any other file changes, report it and do not commit until the operator
approves the exact file list.
