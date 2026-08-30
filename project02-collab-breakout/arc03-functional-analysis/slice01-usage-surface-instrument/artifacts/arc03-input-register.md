# Arc03 Input Register

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice01-usage-surface-instrument
status: proposed-done
architecture-decisions: none
input-status: analytical, non-final, not accepted architecture
```

## Evidence Basis

This register consumes Arc02 closed/composed evidence:

- `../../arc02-conceptual-analysis/closing-report.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-close-readiness.md`

Arc02 produced conceptual risks and an operator decision register for Arc04.
Arc03 turns them into functional question rows and usage evidence needs. This
register does not decide architecture; architecture deferred to Arc04 after
Arc03 closes and operator acceptance occurs.

Project01 and `project01-harmonise-paths` are carried forward as
source/package, package-local, zip, release surface, component contract,
package/release gate, and `make check-package-paths` test surfaces.

## Carried Functional Questions

| ID | Source | Functional question | Evidence to collect | Later owner |
|----|--------|---------------------|---------------------|-------------|
| AFQ-01 | Arc02 conceptual risk and operator decision D-01 | Does posture/methodology work better as standalone posture plus methodology dependency, or as a composed load? | Compare session-start and methodology-only load sets for context cost and missing prerequisites. | Slice03 and Arc04 |
| AFQ-02 | Operator decision D-02 | What does methodology own functionally versus route to? | Walk planning, audit, coverage, delegation, and contribution triggers from methodology. | Slice03 and Slice04 |
| AFQ-03 | Operator decision D-03 | Is PM granularity functionally one component family, separate PM guides, or a wayfinder plus selected standalone mechanics? | Evaluate PM wayfinder, scale model, layout, open set, close, and confirmation load paths. | Slice03 and Arc04 |
| AFQ-04 | Operator decision D-04 | Does ledger versus PM ownership stay clear in real close workflows? | Walk slice close and arc close with PM lifecycle docs and ledger evidence semantics. | Slice02 and Slice03 |
| AFQ-05 | Operator decision D-05 | What top-level composer contract gives enough floor without recreating monolithic context cost? | Compare session start, planning, audit, contribution, and mixed-component loads from top-level SKILL. | Slice03 and Arc04 |
| AFQ-06 | Operator decision D-06 | Where should agent-adapter role-language clarity live? | Test central adapter, local component note, and combined note scenarios for CC, CDC, Claude, Codex, and operator terms. | Slice03 and Arc04 |
| AFQ-07 | Operator decision D-07 and BNF-01 | Is coverage-hardening usable outside the Claude/Cargo-shaped source guide? | Apply coverage scenario to non-Rust or generic repo-tooling language and identify underfit. | Slice03 and Arc04 |
| AFQ-08 | Operator decision D-08 | Are audit and coverage sibling operational components or one quality-floor family? | Compare diagnosis-only audit workflow against test-editing coverage workflow. | Slice03 and Arc04 |
| AFQ-09 | Operator decision D-09 | Does contribution guidance need style and template together for minimum useful load? | Test style-only, template-only, and composed contribution load paths. | Slice03 and Arc04 |
| AFQ-10 | Operator decision D-10 and conceptual risk R-07 | What maintenance contract is functionally needed after breakout? | Identify source docs, package docs, support assets, templates, version history, and checks touched by component changes. | Slice04, Arc04, and Arc05 |
| AFQ-11 | Operator decision D-11 and Project01 gates | Which source/package and package/release gate behaviors are user-visible functional surfaces? | Inspect README, package-root expectations, package-local links, zip roots, CCDP separation, and `make check-package-paths`. | Slice02, Slice04, Arc04, and Arc05 |
| AFQ-12 | Operator decision D-12 and BNF-10 | Is ontology critique a repeatable workflow or only a Project02 analysis artifact? | Give a fresh session the boundary method and test whether it can resolve a new component-boundary question. | Slice03, Slice04, and Arc04 |

## Arc02 Conceptual Risks As Functional Questions

- mislabel: test whether candidate names route users to the correct workflow
  without false expectations.
- improper merge: test whether merged load sets impose unnecessary context cost
  or blur problem ownership.
- improper split: test whether separated components lose required dependencies
  or support assets.
- missing concept: test whether a repeated workflow has no usable entrypoint.
- overclaimed mechanism: test whether a guide claims behavior it cannot
  enforce.
- underfit: test whether current examples or source wording fail general use.
- overfit: test whether a narrow support asset is being treated as a component.
- overlap: test whether repeated rules have clear owner/citation relationships.
- duplication: test whether duplication is deliberate reinforcement or drift.
- maintenance: test whether future changes have a visible owner and gate.

## Project01 Functional Test Surfaces

- Source/package language: users must know whether a path is source-clone,
  generated skill zip, unzipped install, planning worktree, or CCDP package.
- Package-local links: package readers must not need source-only paths.
- Zip roots: generated skill zips need coherent roots and entrypoints.
- Release surface: README, SKILL, and package guidance must name the right
  audience and mode.
- CCDP contrast: CCDP remains a separate protocol package, not a collaboration
  framework skill component.
- Validation gates: `make check-package-paths` and related checks must remain
  visible as package/release gate evidence for Arc05.

## Questions Later Slices Must Answer Before Arc04

- Which current monolith usage surfaces work, and where are context cost,
  routing friction, unclear handoff, or missing functional goals observed?
- Which standalone component scenarios have a minimum useful load set and
  which depend on support assets or the top-level composer?
- Which composed component combinations are actually useful enough to route?
- Which role-language clarity pattern works outside the composer?
- Which Project01 path/package constraints belong in every component contract?
- Which operator decision rows can be answered from functional evidence, and
  which remain operator preference calls?

All rows remain analytical and non-final. This register carries inputs forward;
it does not select final breakout architecture.
