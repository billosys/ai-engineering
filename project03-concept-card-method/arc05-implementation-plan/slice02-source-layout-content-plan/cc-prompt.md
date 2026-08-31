# CC Prompt: Arc05 Slice02 Skill Source Layout and Content Sequence

You are CC implementing Project03 Arc05 Slice02 in the planning worktree.

Work only under:

`project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/`

Do not edit the source checkout at
`/Users/oubiwann/lab/billosys/ai-engineering`. Do not create or edit
`cdc-verification.md`; CDC owns that file after your close.

## Context

Read these files before writing:

- `project03-concept-card-method/project-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/arc-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/slice-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/slice01-source-surface-inventory/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice01-source-surface-inventory/artifacts/source-surface-inventory.md`
- `project03-concept-card-method/arc05-implementation-plan/slice01-source-surface-inventory/artifacts/implementation-input-question-map.md`
- `project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`
- `project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/arc05-implementation-planning-handoff.md`

Preserve the accepted Arc04 architecture. Treat Slice01's source-surface
inventory as factual input. In particular, preserve this package-behavior
constraint: the current generic skill package path copies the selected
`SKILL.md` plus sibling `guides/`; if templates, examples, schema guidance, or
validation guidance need to ship outside `guides/`, route that deliberately to
Slice04.

## Task

Create the required Slice02 artifacts:

- `artifacts/v40-source-layout-plan.md`
- `artifacts/v40-content-sequence-plan.md`
- `artifacts/v40-surface-routing-decision-register.md`

Update:

- `ledger.md`
- `closing-report.md`

The source layout plan should decide the planned source home and exact planned
paths for the v4.0 concept-card method skill surfaces: `SKILL.md`, guides,
templates, examples, validation documentation, and support documents. It should
state whether the layout fits the current `SKILL.md` plus sibling `guides/`
package contract or whether a package behavior change is deliberately routed
to Slice04.

The content sequence plan should decide how the thin `SKILL.md` and supporting
guides route the operator through reason to load, positive and negative load
triggers, problem ownership, dependency direction, operator workflow, guide
routing, and source edit sequencing. Name guide files, template files, example
files, cross-links, and first implementation edit order.

The decision register should record accepted, deferred, and no-op decisions
with an owner or later-slice routing. It must route schema syntax, enum
spelling, validator-code scope, deterministic validation, tests, package
targets, package lists, package-path exceptions, generated zip policy, release
gates, and source version-history obligations to later Arc05 slices.

## Scope Fences

Do not:

- edit source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, schema, validator-code, generated-zip, or release
  files;
- choose exact schema syntax, enum spelling, validator-code language,
  failure-message format, deterministic validation implementation, tests,
  package target names, package list edits, package-path exception rows,
  generated zip policy, release gates, or source version-history text;
- create generated zips, released bundles, validator implementations, runtime
  services, GraphRAG, graph database, ontology database, memory runtime, CCDP
  service, or live extraction behavior;
- close Arc05 or Project03.

## Verification

Run the Slice02 ledger checks from this directory:

`project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/`

Also run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`
- strict ASCII and trailing-whitespace checks over Slice02 Markdown.

The closing report must include:

- row-by-row disposition for F-1 through F-11;
- `Rows: 11. Done: 11. Deferred: 0. No-op: 0.` unless a row is explicitly
  deferred or no-op with rationale;
- artifact inventory;
- Bubble-Up section stating whether Slice02 requires Arc05 re-sequencing, a new
  slice, or a scope correction.

## Expedited Commit Requirement

After verification passes, commit your changes. Stage only these explicit files:

```sh
git add \
  project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-source-layout-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-content-sequence-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-surface-routing-decision-register.md \
  project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/ledger.md \
  project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/closing-report.md
```

Then commit:

```sh
git commit -m "Close Arc05 source layout content plan" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>"
```

If any other file changes, report it and do not commit until the operator
approves the exact file list.
