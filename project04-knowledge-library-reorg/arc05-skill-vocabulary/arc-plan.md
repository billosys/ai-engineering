# Arc 05: Skill Vocabulary, Atomicity, and Public Positioning

```yaml
project: project04-knowledge-library-reorg
arc: arc05-skill-vocabulary
status: active
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: per-slice
operating-mode: expedited
```

## Capability

Arc05 settles the public language for Project04's skill types, support
surfaces, and topology distinctions after the directory reorganization and
end-user docs work have landed.

The arc must keep two axes distinct:

- kind: what a surface is about, such as domain/tooling,
  framework/operational, method, protocol/package, support/template, or
  source/provenance;
- topology: how a surface composes, such as atomic, composite,
  bridge/integration layer, or application/task bundle.

Arc05 turns the prior research and inventory into accepted public wording only
where current source/package evidence supports it. It must not infer taxonomy
from folder placement alone.

## Inputs

- Project04 `project-plan.md` and project `ledger.md`.
- Project-level `artifacts/external-ontology-rubric-research.md`.
- Arc01 source inventory and skill topology classification artifacts.
- Arc02 accepted directory contract and migration/validation artifacts.
- Arc03 directory reorganization closure evidence.
- Arc04 README/docs guide set and Arc04 `closing-report.md`.
- Current source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`.

## Boundaries

In scope:

- Public language for skill kind and skill topology.
- Public positioning for domain/tooling skills, framework/operational skills,
  method skills, protocol packages, support templates, source/provenance
  material, atomic skills, composite skills, bridge/integration layers, and
  application/task bundles.
- Reconciliation of README/docs/SKILL wording with accepted vocabulary.
- Explicit treatment of anchor examples: Rust as an atomic domain/tooling
  candidate, `collaboration-framework` as the accepted composite
  framework/operational anchor, `concept-card-method` as planned/evidence-
  dependent method material, CCDP as a separate protocol package, and Biome as
  a multi-entrypoint knowledge root.

Out of scope:

- Reopening Arc02 directory contract or Arc03 source moves.
- Moving files between `docs/`, `knowledge/`, `templates/`, or `protocols/`.
- Implementing `concept-card-method`.
- Repackaging CCDP as an installable skill.
- Changing package roots, Makefile package lists, package-path exceptions, or
  generated zips unless a later opened source-edit slice explicitly authorizes
  a narrow vocabulary-related repair.

## Expedited Mode

Project04 remains in Expedited Mode.

- CC commits after changes, before CDC review, using explicit file lists.
- CDC commits CDC verification and planning updates after review.
- Closed slices automatically advance to the next slice.
- After the last Arc05 slice closes, CDC closes Arc05 and opens Arc06 with its
  first slice.

## Slice Breakdown

### Slice 01: Public Language Surface Inventory

Status: verified-closed.

Scope: produce a read-only inventory of current public wording in README,
docs, `SKILL.md`, package metadata, and planning inputs that Arc05 must accept,
rewrite, preserve, or explicitly defer.

### Slice 02: Accepted Vocabulary and Positioning Decision

Status: open.

Scope: decide the accepted public vocabulary, examples, avoid-list,
re-entry conditions, and source-edit impact plan.

### Slice 03: Public Wording Implementation

Status: not open.

Scope: apply accepted vocabulary to authorized public surfaces such as README,
focused docs, top-level `SKILL.md`, and package-facing descriptions if Slice02
authorizes those edits.

### Slice 04: Vocabulary Reconciliation and Arc Close Readiness

Status: not open.

Scope: reconcile public wording, package/path checks, README/docs/SKILL
consistency, and Arc05 close readiness after source edits.

## Dependencies

- Slice01 must close before vocabulary decisions because it establishes the
  current public-language surface and input evidence.
- Slice02 must close before source wording edits because it records accepted
  terms and avoid-list.
- Slice03 depends on Slice02 source-edit authorization.
- Slice04 closes the arc by validating consistency and package behavior after
  public wording changes.

## Version History

### v1.1 - 2026-09-03

Recorded Slice01 as verified-closed after CDC reproduced all six ledger rows,
checked the planning commit, confirmed no source commit was created, and
verified the public-language inventory and decision-question artifacts. Opened
Slice02, `slice02-accepted-vocabulary-positioning`, to decide accepted
vocabulary, examples, avoid-list, source-edit authorization, and re-entry
conditions before source wording implementation.

### v1.0 - 2026-09-03

Opened Arc05 after Arc04 closed. Planned four vocabulary-sized slices and
opened Slice01, `slice01-public-language-surface-inventory`, as a read-only
inventory and evidence synthesis before accepted vocabulary decisions or
source wording edits begin.
