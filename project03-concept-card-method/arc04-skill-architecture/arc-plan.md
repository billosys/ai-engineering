# Arc 04: Skill Architecture

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
status: active
depends-on:
  - ../arc03-conceptual-model/closing-report.md
blocks:
  - ../arc05-implementation-plan
related:
  - ../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md
  - ../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-model-decision-register.md
  - ../arc03-conceptual-model/slice04-model-synthesis/artifacts/arc04-skill-architecture-handoff.md
```

## Capability

Arc04 defines the v4.0 concept-card method skill architecture. It turns the
accepted Arc03 conceptual model into a loadable knowledge-skill design:
entrypoint contract, reason-to-load boundary, guide split, template set,
example set, deterministic validation candidates, package behavior, README
integration, and maintenance ownership.

The arc plans architecture only. It does not edit source `SKILL.md` files,
guides, templates, README, Makefile/package lists, generated zips, validator
code, schema files, or released skill bundles. Those remain Arc05
implementation-planning and later implementation responsibilities.

## Slice Breakdown

### Slice 01: Architecture Input Inventory

Directory: `slice01-architecture-input-inventory`

Status: verified-closed on 2026-08-30.

Scope: inventory the accepted Arc03 conceptual-model commitments, architecture
handoff inputs, candidate skill surfaces, and open decision questions that
Arc04 must carry into later architecture slices. This slice maps inputs; it
does not choose final file layout or package behavior.

Blocks: Slice02, Slice03, Slice04, and Slice05.

Durable architecture inputs belong under the slice-local `artifacts/`
directory.

### Slice 02: Load Contract and Ownership Model

Directory: `slice02-load-contract-ownership`

Status: verified-closed on 2026-08-31.

Scope: define when the v4.0 concept-card method skill should load, what
problem it owns, what adjacent skills or framework capabilities it depends on,
what it leaves out, and how `SKILL.md` routes an operator to focused guides.

Blocks: Slice03, Slice04, and Slice05.

Durable architecture outputs belong under the slice-local `artifacts/`
directory.

### Slice 03: Guide, Template, and Example Architecture

Directory: `slice03-guide-template-example-architecture`

Status: open.

Scope: decide the guide set, template set, example set, and user-authored
surfaces needed for the first v4.0 skill, while preserving the Arc03
construct distinctions between cards, claims, source support, evidence grades,
result records, reconciliation, CQs, extraction runs, and memory admission.
Slice03 should consume Slice02's decision that the v3.2 five-agent workflow is
a default recipe rather than an invariant, preserving extraction-run and
parallel-worker provenance without hard-coding a worker count.

Blocks: Slice04 and Slice05.

Durable architecture outputs belong under the slice-local `artifacts/`
directory.

### Slice 04: Validation, Packaging, and Discoverability

Directory: `slice04-validation-packaging-discoverability`

Status: planned.

Scope: decide which validation checks are deterministic enough to plan for
Arc05, which are semantic/audit checks, how templates/guides/examples/scripts
should be packaged, and how README/library discoverability should represent
the method without promising runtime services.

Blocks: Slice05.

Durable architecture outputs belong under the slice-local `artifacts/`
directory.

### Slice 05: Architecture Synthesis and Arc05 Handoff

Directory: `slice05-architecture-synthesis`

Status: planned.

Scope: compose the verified Arc04 slices into an accepted v4.0 skill
architecture, record architecture decisions, and produce the bounded
implementation-planning handoff for Arc05.

Blocks: Arc04 close and Arc05.

Durable architecture outputs belong under the slice-local `artifacts/`
directory.

## Dependencies

Consumes:

- Closed Arc03 conceptual model and arc close report.
- Accepted v4.0 conceptual model, model decision register, and Arc04 handoff
  packet.
- Project03's v4.0 target framing and planning-only source-edit boundary.

Leaves for later arcs:

- An accepted skill architecture that preserves the v4.0 conceptual model.
- A clear split between loadable `SKILL.md`, focused guides, templates,
  examples, validation candidates, package behavior, and README integration.
- A bounded Arc05 input for source-edit planning, Makefile/package changes,
  validation gates, and generated skill artifacts.

## Version History

### v1.0 - 2026-08-30

Arc04 opened after Arc03 formal close. Slice01 begins with architecture-input
inventory so later slices can decide load contract, guide/template/example
architecture, validation/package behavior, and final synthesis from a stable
input map.

### v1.1 - 2026-08-30

Slice01 marked verified-closed after CDC reproduced all eight slice ledger
rows. Slice02 can now be planned against the architecture input inventory and
decision-question map; no new Arc04 slice, re-sequencing, or scope change was
required.

### v1.2 - 2026-08-30

Slice02 opened for load contract and ownership modeling. The slice is scoped
to positive and negative load triggers, problem ownership, dependency
direction, adjacent-guidance routing, and operator workflow boundaries while
leaving guide/template/example architecture, validation/package decisions, and
source edits to later slices or Arc05.

### v1.3 - 2026-08-31

Slice02 marked verified-closed after CDC reproduced all ten slice ledger rows.
The slice decided that the v3.2 five-agent workflow carries forward as a
default recipe, not an invariant; Slice03 should preserve extraction-run and
parallel-worker provenance without hard-coding worker count. No new Arc04
slice or re-sequencing was required.

### v1.4 - 2026-08-31

Slice03 opened for guide, template, and example architecture. The slice is
scoped to user-facing skill surfaces and first-release examples while leaving
validation determinism, package behavior, README integration, maintenance
ownership, source edits, and implementation planning to later slices or Arc05.
