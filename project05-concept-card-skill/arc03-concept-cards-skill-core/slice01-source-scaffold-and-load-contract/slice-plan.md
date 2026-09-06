# Slice01 Plan: Source Scaffold And Load Contract

```yaml
project: project05-concept-card-skill
arc: arc03-concept-cards-skill-core
slice: slice01-source-scaffold-and-load-contract
status: open
opened: 2026-09-06
depends-on:
  - arc02-document-extraction-skill
```

## Goal

Create the initial `knowledge/concept-cards/` source root with a thin
entrypoint, sibling version history, load contract, and operator workflow. The
scaffold must translate Project03's v4.0 concept-card method evidence into the
current Project05 skill name and layout without claiming later guide,
template, example, package, or install work has landed.

## Scope

In scope:

- add `knowledge/concept-cards/SKILL.md`;
- add `knowledge/concept-cards/version-history.md`;
- add `knowledge/concept-cards/guides/01-load-contract.md`;
- add `knowledge/concept-cards/guides/02-operator-workflow.md`;
- route raw PDF/EPUB/HTML or converted-source cleanup to the closed
  `document-extraction` skill;
- name the core v4.0 constructs and lifecycle distinctions that later Arc03
  slices must preserve;
- identify later guides, templates, examples, validation/reference surfaces,
  package targets, generated zips, docs, and install integration as future
  work.

Out of scope:

- adding extraction, re-extraction, evidence lifecycle, graph/CQ,
  reconciliation, validation/verification, memory-admission, or maintenance
  guides beyond the load/workflow foundation;
- adding templates, examples, validation/reference support directories, or
  schema files;
- adding package, Makefile, README, docs, generated zip, or install wiring;
- implementing executable validators, runtime services, graph databases,
  ontology databases, GraphRAG, CCDP services, or memory runtime automation;
- recreating `knowledge/concept-card-method/`.

## Required Design Pressure

The scaffold must make `concept-cards` load for concept-card method work, not
for generic source reading or document extraction. It should treat
`document-extraction` outputs as upstream provenance when document preparation
is needed.

The initial guides must name and preserve the Project03 v4.0 distinctions:
concept card, claim, source support, source span/source locator, relationship
edge, competency question, extraction run, validation result, verification
result, reconciliation result, preservation decision, and memory admission.
They must not collapse evidence grade, extraction confidence, validation
result, verification state/result, reconciliation state/result, and memory
admission into one confidence field.

## Exit Criteria

Slice01 is complete when:

- the four source files exist under `knowledge/concept-cards/`;
- `SKILL.md` uses `name: concept-cards`, current `metadata.version`, positive
  and negative load boundaries, ownership boundaries, `document-extraction`
  routing, a guide map, and a version-history pointer;
- `version-history.md` records the initial scaffold and explains the
  Project03/Project05 name translation;
- guides 01 and 02 cover the load contract, operator/assistant workflow,
  human-assisted and agent-direct use, future-route boundaries, and v4.0
  construct distinctions;
- no templates/examples/package/docs/install work is added or claimed;
- `knowledge/concept-card-method/` is absent;
- focused validators pass.

## Expected Artifacts

No separate durable planning artifacts are expected. Implementation output is
the source files listed above. Durable close evidence belongs in this slice's
`closing-report.md`, `ledger.md`, and later `cdc-verification.md`.
