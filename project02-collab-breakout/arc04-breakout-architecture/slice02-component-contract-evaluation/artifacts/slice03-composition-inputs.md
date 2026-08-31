# Slice03 Composition Inputs

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice02-component-contract-evaluation
status: proposed-done
handoff-status: ready-for-slice03
architecture-decisions: none
```

## Input Contract

This handoff summarizes the evaluated row set from Slice02. It consumes:

- verified Slice01 architecture decision instrument inputs;
- `artifacts/component-contract-evaluation-matrix.md`;
- `artifacts/candidate-component-contracts.md`;
- `artifacts/support-adapter-constraint-dispositions.md`;
- `artifacts/package-release-gate-dispositions.md`;
- closed Arc02 conceptual evidence and closed Arc03 functional evidence.

Slice03 owns target graph composition and package architecture. Slice02 does
not accept final architecture, final package paths, source moves, operator
acceptance, or Arc05 implementation slices.

## Ready For Composition

These rows are ready for Slice03 composition as component or gate candidates,
subject to operator acceptance later in Slice04:

| Row | Composition Role | Required Edge / Gate |
|-----|------------------|----------------------|
| CAW-03 `ledger-verification-protocol` | direct-load component candidate | PM close uses ledger; ledger owns evidence semantics. |
| CAW-07 `delegation-policy` | direct-load operational component candidate | Methodology and composer route to it; role adapter note required. |
| CAW-08 `contribution-style-and-voice` | direct-load operational component candidate with support asset | Owns `CAW-13` `CONTRIBUTION-TICKET.md`. |
| CAW-19 Project01 path-contract constraints | package/release gate | Every accepted component inherits source/package fields. |
| CAW-20 source/package reader modes | contract requirement / adapter | Each component states source clone, generated zip, installed skill, and CCDP adjacency behavior. |
| CAW-21 release surface synchronization | package/release gate | README, `SKILL.md`, Makefile, package lists, generated zip, and validation stay synchronized. |
| CAW-22 CCDP separation | package/release gate | CCDP remains separate protocol distribution. |
| CAW-25 component-maintenance discipline | contract requirement | Every accepted component names maintenance owner and version history responsibility. |

## Requires Adjustment Before Acceptance

These rows can be composed by Slice03 only with explicit adjustment notes:

| Row | Adjustment Needed | Source IDs |
|-----|-------------------|------------|
| CAW-01 `collaborative-posture-and-ethics` | Decide standalone package, composer summary, or both; preserve methodology prerequisite. | D-01, OQ-01, ARG-02, BNF-11. |
| CAW-02 `engineering-methodology-and-process` | Define owned process versus routed components; prevent monolith recreation. | D-02, OQ-02, ARG-01, ARG-02, BNF-04. |
| CAW-04 `project-management` | Compose as PM family by default; decide package granularity and internal guide treatment. | D-03, OQ-03, ARG-03, BNF-08. |
| CAW-05 `code-audit-discipline` | Preserve diagnosis-only scope and update output-home convention from old workbench language to slice `artifacts/` where applicable. | D-08, OQ-04, ARG-04, FR-06. |
| CAW-06 `coverage-hardening-discipline` | Pick surface-neutral name or adapter; preserve historical compatibility. | D-07, OQ-05, ARG-05, BNF-01, BNF-13. |
| CAW-09 top-level composer | Make composer thin but not link-only; include compact posture/process floor and route table. | D-05, ARG-01. |
| CAW-10 agent adapter | Choose central plus local notes by default; decide whether standalone package is deferred. | D-06, OQ-06, ARG-08. |
| CAW-11 repository orientation | Separate adapter guidance from hard gates; make reader modes package-local. | D-11, OQ-07, ARG-07, ARG-10, ARG-11. |
| CAW-12 PM wayfinder | Keep inside PM family unless Slice03 chooses a package architecture that requires a separate entrypoint. | D-03, OQ-03, ARG-03. |
| CAW-17 audit output examples | Package with audit only after output-home examples match the slice `artifacts/` convention. | ARG-04, FD-05, LPF-06. |

## Support Asset Inputs

| Row | Owner | Slice03 Use |
|-----|-------|-------------|
| CAW-13 `CONTRIBUTION-TICKET.md` | `contribution-style-and-voice` | Compose as required support asset and package-local template link. |
| CAW-14 PM examples | `project-management` | Compose as optional PM support asset, not direct-load component. |
| CAW-15 PM provenance/version history notes | `project-management` / maintenance fields | Preserve as rationale and version-history support. |
| CAW-16 planning anti-patterns and repair guidance | `project-management` | Compose under PM wayfinder. |
| CAW-17 audit output examples | `code-audit-discipline` | Compose under audit after adjustment. |
| CAW-18 protocol distribution guidance | repository orientation / release gates | Keep as CCDP separation support and constraint. |

## Deferred Or Non-Component Inputs

| Row | Disposition | Re-entry Condition |
|-----|-------------|--------------------|
| CAW-23 verification-methodology | deferred component; dependency edge / non-component | Reopen only if later evidence proves a direct-load workflow beyond ledger/methodology ownership. |
| CAW-24 ontology critique | deferred / non-component | Reopen if operator requests reusable boundary-review component or Project03 produces component-ready method. |
| CAW-25 component-maintenance discipline | go as contract requirement; deferred as standalone component | Reopen standalone status only if maintenance becomes a recurring direct-load workflow. |
| CAW-26 evidence strength and memory admission vocabulary | deferred component; non-component / dependency edge | Reopen only in a future memory/evidence ontology effort with direct-load evidence. |

## Operator Decisions Preserved

No D/OQ/ARG rows were silently merged. Slice03 should carry the following
operator acceptance groups forward:

- posture and methodology boundary: D-01, D-02, OQ-01, OQ-02;
- PM and ledger ownership: D-03, D-04, OQ-03, ARG-03;
- composer and agent adapter: D-05, D-06, OQ-06, ARG-01, ARG-08;
- audit, coverage, and contribution: D-07, D-08, D-09, OQ-04, OQ-05,
  ARG-04, ARG-05, ARG-06;
- maintenance and release gates: D-10, D-11, OQ-07, OQ-08, ARG-07, ARG-09,
  ARG-10, ARG-11;
- ontology critique and acceptance gap: D-12, OQ-09, ARG-10, ARG-12.

## Slice03 Worklist

1. Compose package/release gates first, using `CAW-19` through `CAW-22` and
   `CAW-25` as mandatory contract language.
2. Compose the top-level composer and adapter layer: `CAW-09`, `CAW-10`,
   `CAW-11`, and `CAW-12`.
3. Compose core components and families: `CAW-01` through `CAW-04`, with
   ledger and PM dependency direction explicit.
4. Compose operational components: `CAW-05` through `CAW-08`, preserving
   audit/coverage sibling distinction and contribution/template travel.
5. Place support assets under owners and leave non-components/deferred concepts
   as explicit edges or re-entry conditions.

## Non-Final Boundary

These inputs are ready for Slice03 target composition, but they are not
accepted architecture. Slice03 may propose the target graph, dependency order,
package architecture, top-level composer contract, support-asset travel,
adapter placement, source/package assumptions, README/SKILL wayfinding
implications, and release-gate strategy. Slice04 must still produce the
operator acceptance packet before Arc04 can close.
