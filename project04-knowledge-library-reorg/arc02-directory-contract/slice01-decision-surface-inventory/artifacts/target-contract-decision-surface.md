# Target Contract Decision Surface

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice01-decision-surface-inventory
artifact: target-contract-decision-surface
artifact-status: decision-surface inventory
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This artifact groups the Arc01 decision rows into Arc02 decision areas. It
consumes Arc01 close evidence and the Slice04 synthesis artifacts:
`arc02-readiness-packet.md`, `directory-contract-requirements.md`, and
`arc01-synthesis-decision-register.md`.

Arc01 recorded `Composition verdict: delivered`, but this artifact is not
source-edit authorization. Arc02 may select a target contract in a later slice;
this slice only inventories the decision surface.

## Authority Labels

- accepted fact: already accepted by Project04, Project02, Project03, or Arc01
  closure evidence.
- working hypothesis: useful prior implementation or layout idea that Arc02
  must test before accepting.
- operator decision required: a choice with more than one viable contract.
- planner recommendation: a non-binding recommendation from Arc01 evidence.
- planned surface: accepted or planned work not yet present in the source
  checkout.
- live source: current material observed in
  `/Users/oubiwann/lab/billosys/ai-engineering`.
- source-edit risk: a risk for later source-edit slices, not permission to edit
  source now.
- re-entry condition: a condition that reopens a prior assumption, architecture
  boundary, or package policy.

## Decision Surface Summary

| Decision area | Source decision rows | Authority level | Operator decision required | Planner recommendation | Re-entry condition |
|---------------|----------------------|-----------------|----------------------------|------------------------|--------------------|
| `docs/` versus `knowledge/` contract | D-1 | accepted fact: Project04 wants `docs/` as explanation and `knowledge/` as substrate where accepted; working hypothesis: wrappers for moved source. | Yes. Arc02 must decide move/remain/wrapper treatment for current source-like `docs/`. | Keep `docs/` focused on reader-facing explanation and move substrate-like material only where the accepted contract preserves provenance. | Re-enter if package validation or source provenance requires a specific source-like exception under `docs/`. |
| Project02 framework/operational component roots | D-2 | accepted fact: component names and roles; working hypothesis: top-level component roots. | Yes. Arc02 must choose between `knowledge/<component>`, top-level roots, `knowledge/framework/<component>`, or wrappers. | Prefer a contract that keeps component source in the knowledge-library substrate unless compatibility evidence forces a separate family. | Re-enter Project02 only if no coherent contract preserves accepted roles and composer behavior. |
| `collaboration-framework` composer | D-3 | accepted fact: daily-driver composite composer; live source: top-level `SKILL.md`. | Yes for transitional top-level `SKILL.md` shim or removal policy. | Preserve the composer as the default broad sustained-work route while allowing specialist components to become independently loadable. | Re-enter if moving the entrypoint breaks source checkout readers, generated package roots, or installed route wording. |
| Planned `concept-card-method` method skill | D-4 | accepted fact: Project03 planned method skill; planned surface, not live source. | Yes before public docs claim implementation or package availability. | Treat it as planned method-skill input; do not place it under CCDP or call it live source. | Re-enter Project03 if the accepted directory contract cannot preserve thin `SKILL.md`, focused `guides/`, and planned status. |
| Skill kind and topology language | D-5 | accepted Arc01 fact: skill kind and topology are independent axes. | Yes if Arc02 wants public-facing terminology before Arc05. | Keep contract language internal and route final public wording to Arc05. | Re-enter classifications if source roots, package roots, entrypoint shape, or package behavior changes load reason. |
| Source root versus package root relationship | D-6 | live source fact: roots and packages already differ in selected-file and frontmatter-based cases. | Yes for any intentional divergence rule. | State source-root and package-root rules separately; avoid one-root-one-package assumptions. | Re-enter if Biome-style or composer selected-file packaging cannot satisfy the accepted rule. |
| Biome multi-entrypoint root | D-7 | live source fact: `knowledge/biome/` has multiple `SKILL*.md` entrypoints and package roots. | Yes if Arc02 splits or preserves the source root by policy. | Treat Biome as a first-class edge case in the contract. | Re-enter if package validation or user wayfinding becomes clearer with split roots. |
| Template ownership | D-8 | live source fact: top-level `templates/`; working hypothesis: owner-local templates. | Yes for cross-cutting templates left at top level. | Assign owner-local templates where ownership is clear; keep top-level only for true cross-cutting support. | Re-enter if package payloads lose required template files. |
| CCDP protocol/package surface | D-9 | accepted fact: CCDP remains separate protocol/package; live source under `protocols/ccdp`. | Yes only to reopen protocol package policy. | Keep `protocols/ccdp` separate and add docs or method links as wrappers, not package absorption. | Re-enter only with explicit protocol package decision evidence. |
| README, `docs/`, and `SKILL.md` wayfinding | D-10 | accepted Project04 direction plus Project02 reader-mode hypothesis. | Yes for final public wording later in Arc05. | Use README for concise orientation, `docs/` for explanation, and `SKILL.md` files for load behavior. | Re-enter if package-root or installed-route evidence changes reader modes. |
| Migration sequencing and compatibility gates | D-11 | working hypothesis: Project02 implementation roadmap; accepted boundary: no source edits yet. | Yes before source implementation begins. | Sequence mechanical moves before prose rewrites; update Makefile and packages after payloads exist. | Re-enter if accepted directory contract invalidates the prior implementation order. |
| Package-path exception policy | D-12 | working hypothesis and compatibility obligation from Project02; live validator evidence from Arc01. | Yes for accepted warnings that remain after migration. | Repair package-local links first; use narrow expiring exceptions only for intentional cases. | Re-enter if package-local links cannot be repaired without broad exceptions. |

## Required Arc02 Decision Areas

Arc02 must decide all of the following before Arc03 source implementation can
open without a narrower operator override:

- `docs/` move/remain/wrapper treatment for current framework, method,
  extraction, design/dev, and end-user material;
- `knowledge/` source-root scope for live domain/tooling skills and planned
  framework/operational or method skills;
- Project02 component source-root and package-root placement;
- Project03 `concept-card-method` planned source-root handling;
- CCDP protocol/package placement and wrapper-link policy;
- template ownership and top-level exception policy;
- README, `docs/`, and `SKILL.md` wayfinding responsibility;
- source-root and package-root relationship;
- Biome multi-entrypoint root handling;
- validation commands and compatibility gates for each later source-edit
  slice;
- package-path exception policy and accepted-warning policy.

## Explicit Non-Decisions

- This artifact does not choose the final directory contract.
- This artifact does not authorize source edits.
- This artifact does not make Project02 implementation hypotheses into
  accepted Project04 layout.
- This artifact does not make planned `concept-card-method` live source.
- This artifact does not make the external ontology rubric accepted taxonomy.
- This artifact does not move CCDP into installable skill packages.

## Bubble-Up Candidates For Slice02

- Slice02 should turn these grouped areas into an accepted contract and an
  operator decision register.
- Slice02 should mark every selected path rule as accepted fact, adjusted
  hypothesis, rejected hypothesis, or operator decision.
- Slice02 should keep source root and package root decisions separate.
- Slice02 should keep skill kind and topology independent: domain/tooling,
  framework/operational, method, protocol/package, support/template, and
  source/provenance are kind labels; atomic, composite, bridge/integration, and
  application/task bundle are topology labels.
