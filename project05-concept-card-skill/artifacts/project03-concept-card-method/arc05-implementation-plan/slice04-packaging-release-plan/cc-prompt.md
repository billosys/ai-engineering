# CC Prompt: Arc05 Slice04 Packaging, Discoverability, and Release Gates

You are CC implementing Project03 Arc05 Slice04 in the planning worktree.

Work only under:

`project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/`

Do not edit the source checkout at
`/Users/oubiwann/lab/billosys/ai-engineering`. Do not create or edit
`cdc-verification.md`; CDC owns that file after your close.

## Context

Read these files before writing:

- `project03-concept-card-method/project-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/arc-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/slice-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/slice01-source-surface-inventory/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-source-layout-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-schema-surface-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-validator-scope-test-plan.md`

Preserve the verified Slice02 package-compatible `guides/` layout and the
verified Slice03 documentation-only validator-code scope. This slice plans
packaging and release mechanics; it must not perform source implementation,
build generated zips, or claim release readiness.

## Task

Create the required Slice04 artifacts:

- `artifacts/v40-package-update-plan.md`
- `artifacts/v40-discoverability-plan.md`
- `artifacts/v40-release-gate-plan.md`
- `artifacts/v40-version-history-plan.md`

Update:

- `ledger.md`
- `closing-report.md`

The package update plan should decide future Makefile/package-list
requirements for the concept-card method skill: package target names, package
list edits, install behavior, clean behavior, generated archive behavior,
package-path checks, package-path exceptions, generated zip policy, and
package update boundaries.

The discoverability plan should decide README and skill-library requirements:
skill description, tags/metadata, reason to load, promise boundary,
adjacent-skill routing, and operator-facing package expectations.

The release gate plan should decide evidence required before future
implementation can claim release readiness: skill checks, package-path checks,
generated zip checks, source checkout cleanliness, planning checkout hygiene,
package installability, documentation-only validator scope, and release gate
sequencing.

The version history plan should decide which source files need version-history
or enclosing-history updates when the skill is implemented: `SKILL.md`, guides,
templates, examples, validation documentation, support documents, README,
Makefile, and package-path exception surfaces.

Route implementation-plan synthesis, implementation-slice recommendations,
deferral register, and Project03 close input to Slice05.

## Scope Fences

Do not:

- edit source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, validator-code, generated-zip, or release files;
- implement Makefile targets, package list edits, package-path exception rows,
  README/library prose, tests, generated zips, package release, executable
  validator-code, release gates, CI changes, or source version-history text;
- create runtime services, GraphRAG, graph database, ontology database, memory
  runtime, CCDP service, or live extraction behavior;
- reopen Slice02 layout or Slice03 schema/validation decisions unless a
  packaging fact forces a documented Arc05 plan update;
- close Arc05 or Project03.

## Verification

Run the Slice04 ledger checks from this directory:

`project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/`

Also run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`
- strict ASCII and trailing-whitespace checks over Slice04 Markdown.

The closing report must include:

- row-by-row disposition for F-1 through F-12;
- `Rows: 12. Done: 12. Deferred: 0. No-op: 0.` unless a row is explicitly
  deferred or no-op with rationale;
- artifact inventory;
- Bubble-Up section stating whether Slice04 requires Arc05 re-sequencing, a new
  slice, or a scope correction.

## Expedited Commit Requirement

After verification passes, commit your changes. Stage only these explicit files:

```sh
git add \
  project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/artifacts/v40-package-update-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/artifacts/v40-discoverability-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/artifacts/v40-release-gate-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/artifacts/v40-version-history-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/ledger.md \
  project03-concept-card-method/arc05-implementation-plan/slice04-packaging-release-plan/closing-report.md
```

Then commit:

```sh
git commit -m "Close Arc05 packaging release plan" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>"
```

If any other file changes, report it and do not commit until the operator
approves the exact file list.
