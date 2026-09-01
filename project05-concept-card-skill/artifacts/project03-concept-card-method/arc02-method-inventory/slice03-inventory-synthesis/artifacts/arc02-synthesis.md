# Arc02 Inventory Synthesis

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice03-inventory-synthesis
status: proposed-done
inputs:
  - ../slice01-v32-source-inventory/cdc-verification.md
  - ../slice01-v32-source-inventory/artifacts/v32-source-inventory.md
  - ../slice01-v32-source-inventory/artifacts/v32-method-structure-map.md
  - ../slice01-v32-source-inventory/artifacts/v32-original-assessment.md
  - ../slice02-v40-gap-analysis/cdc-verification.md
  - ../slice02-v40-gap-analysis/artifacts/v40-gap-register.md
  - ../slice02-v40-gap-analysis/artifacts/v32-to-v40-carry-forward-change-matrix.md
mode: Arc02 close input
v4-design-decisions: none
```

## Scope Fence

This synthesis composes verified Slice01 and Slice02 artifacts into Arc02 close
input. It is source-backed by `v32-source-inventory.md`,
`v32-method-structure-map.md`, `v32-original-assessment.md`,
`v40-gap-register.md`, and
`v32-to-v40-carry-forward-change-matrix.md`. It does not design the Arc03
conceptual model, choose the Arc04 skill layout, plan Arc05 implementation
mechanics, or authorize source edits.

## Composition Summary

Arc02 has enough evidence to close once this slice is independently verified:
Slice01 preserves and inventories the v3.2 baseline; Slice02 identifies the
source-backed v4.0 gaps; Slice03 composes them into the handoff below.

The v3.2 method is not being replaced wholesale. Its strong substrate rules
remain useful. The v4.0 move is justified where v3.2 collapses distinct
operational concerns into prose, checklist judgment, or a single field.

## v3.2 keeps

The following should carry forward as protected baseline material:

- One concept per card as the atomicity rule.
- Source-faithful synthesis instead of copied prose or unsupported inference.
- Required provenance through source metadata, source references, and
  verification notes.
- The body template for definitions, prerequisites, properties, procedures,
  examples, relationships, common errors, common confusions, source reference,
  and verification notes.
- Typed relationship fields as a compact baseline: `prerequisites`, `extends`,
  `related`, and `contrasts_with`.
- Competency questions as requirements, coverage hooks, and usability checks.
- Source-primary re-extraction with old-card content treated as secondary
  preservation input.
- Old-card unique-value preservation, card-count checks, and preservation
  notes.
- Validation as an explicit close gate, even where v4.0 later strengthens its
  mechanics.

Source basis: `v32-source-inventory.md` Purpose, Schema, Workflow,
Provenance, Relationship Model, Competency Question Handling, Re-Extraction
Mechanics, and Preservation Checks; `v32-method-structure-map.md` Cross-
Document Shape and Baseline Constructs.

## v4.0 must change

The following are architectural change inputs, not final design decisions:

- Separate extraction confidence from source evidence, verification status,
  and memory-admission status.
- Treat source span, claim, evidence grade, and provenance reference as
  potentially distinct concepts.
- Model verifier role, verification result, and reproduced evidence explicitly.
- Add reconciliation for duplicate concepts, competing definitions, slug drift,
  taxonomy drift, relationship asymmetry, and parallel-run conflict.
- Make memory admission explicit instead of assuming validated cards are ready
  for durable future cognition.
- Upgrade relationship semantics from graph-ready fields to graph-native edge
  concepts with evidence, status, and possible inverse or closure policy.
- Define CCDP-compatible evidence semantics on the method side: cognitive
  outputs are claims with provenance, audit history, and admission decisions.
- Distinguish deterministic schema validation from semantic QA and operator
  judgment.
- Add extraction run traceability for source snapshot, prompt version, agent
  scope, produced card set, validation result, and merge/reconciliation result.

Source basis: `v40-gap-register.md` G-01 through G-10 and
`v32-to-v40-carry-forward-change-matrix.md` architectural change rows.

## operator choice

Two decisions should remain explicit operator choices rather than hidden design
defaults:

- Whether the exactly-five-agent parallel re-extraction workflow from 0010 is
  a method invariant, a default operating recipe, or a parameterized pattern.
- Where the eventual loadable skill boundary belongs: thin `SKILL.md`, guide
  split, templates, scripts, examples, package behavior, and README
  integration are Arc04 decisions, not Slice03 decisions.

Source basis: `v40-gap-register.md` G-07 and G-14;
`v32-to-v40-carry-forward-change-matrix.md` operator decision rows.

## deferred or out of scope

Deferred:

- Live corpus validation. Arc02 is a source-backed inventory and gap analysis,
  not a live extraction demonstration.
- Full GraphRAG, memory runtime, ontology database, or CCDP service
  implementation.

Out of scope:

- Designing the final Arc03 conceptual model.
- Choosing the final Arc04 skill layout.
- Planning Arc05 implementation mechanics, source file locations, Makefile
  behavior, package updates, examples, scripts, or README changes.
- Editing source files in `/Users/oubiwann/lab/billosys/ai-engineering`.
- Reopening verified Slice01 or Slice02 artifacts absent a concrete defect.

## Arc02 close and composition input

This artifact supports the Arc02 ledger rows as follows:

- A-4: Slice01 preserves the v3.2 baseline source snapshots and inventories
  schema, workflow, validation, provenance, relationships, competency
  questions, confidence, re-extraction, and preservation. This synthesis
  identifies those as v3.2 keeps and as protected carry forward material.
- A-5: Slice02 distinguishes carry forward, minor cleanup, architectural
  change, operator decision, and defer routes. This synthesis preserves those
  distinctions and names the v4.0 must change areas without introducing new
  design commitments.
- A-6: Slice03 leaves explicit Arc03 conceptual model inputs by routing the
  candidate constructs and open questions to
  `artifacts/arc03-conceptual-model-inputs.md`.

Composition verdict for Arc02 close: delivered, pending independent CDC
verification of Slice03 and an arc-scale composition check. The slices compose
into the promised capability because the v3.2 baseline is preserved and
inventoried, the v4.0 gaps are source-backed, and the Arc03 handoff has a
bounded list of conceptual-model inputs.

## Bubble-up

No defect was found in the verified Slice01 or Slice02 artifacts. The only
bubble-up is status/composition: Arc02 can close after CDC verifies Slice03 and
reproduces A-4, A-5, and A-6 at arc scale.
