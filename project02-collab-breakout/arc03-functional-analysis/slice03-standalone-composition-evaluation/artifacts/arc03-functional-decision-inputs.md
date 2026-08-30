# Arc03 Functional Decision Inputs

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice03-standalone-composition-evaluation
status: proposed-done
architecture-decisions: none
input-status: analytical, non-final, not accepted architecture
```

## Non-Final Posture

This artifact is an analytical handoff. It does not decide final component
boundaries, names, source moves, package paths, or accepted architecture.
Architecture deferred to Arc04 after Slice04 synthesizes Arc03 and the
operator accepts a direction.

The inputs below consume verified Slice01, verified Slice02, and Arc02
candidate-boundary evidence. They preserve the input contract language:
scenario matrix, functional-analysis method, current-workflow evaluation,
load-path friction, functional-deficiency, source/package role-language,
Arc02 conceptual model, boundary and naming findings, and operator decision
register.

## Functional Fit Signals For Slice04

| Candidate or concept | Functional fit signal | Go / adjust / defer posture | Route |
|----------------------|-----------------------|-----------------------------|-------|
| collaborative posture | Real load path at substantial session start and when posture is itself in question. | go / adjust: likely standalone or named prerequisite; final package shape deferred. | Slice04, Arc04 D-01 |
| engineering methodology | Real load path for planning how work is done, SDLC, quality floor, and routing to operational guides. | adjust: own pillars and process; route specialized mechanics. | Slice04, Arc04 D-02 |
| ledger-verification protocol | Strong standalone load path for any ledgered unit and strong dependency edge into PM close. | go: standalone candidate with explicit PM dependency direction. | Slice04, Arc04 D-04 |
| project-management family | Strong load path for project/arc/slice planning and close, but family behavior is stronger than per-file component evidence. | adjust: PM component family; package granularity deferred. | Slice04, Arc04 D-03 |
| code-audit discipline | Real direct load moment for diagnosis-only repo audits. | adjust: standalone candidate with output-location and agent-adapter fixes. | Slice04, Arc04 D-08, Arc05 |
| coverage-hardening discipline | Real direct load moment for hard coverage thresholds. | adjust: surface-neutral naming and non-Rust command adaptation needed. | Slice04, Arc04 D-07 |
| delegation-policy | Clear narrow direct load moment for deciding what may be delegated. | go: low-risk standalone operational component with local role note. | Slice04, Arc04 D-06 |
| contribution guidance | Clear direct load moment for upstream tickets when style and template travel together. | go: component plus support asset. | Slice04, Arc04 D-09 |
| top-level composer | Still valuable for discovery and multi-discipline session start. | adjust: thin framework-entrypoint, not rich monolith. | Slice04, Arc04 D-05 |
| agent-adapter | Functional need across standalone and composed use. | adjust/defer: adapter pattern, not yet proven standalone component. | Slice04, Arc04 D-06 |

## Concepts Lacking Real Functional Load Paths

| Concept | Current evidence | Suggested classification | Route |
|---------|------------------|--------------------------|-------|
| verification-methodology | Shared vocabulary across methodology, ledger, PM, audit, and coverage, but no user trigger that loads it alone. | dependency edge / ontology glue | Slice04; Arc04 should avoid component promotion unless new evidence appears. |
| path-contract-constraints | Project01 package behavior is critical, but users need it through component contracts and release gates. | constraint / package/release gate | Slice04; Arc04 D-11; Arc05 validation plan. |
| planning-confirmation-protocol as standalone | Useful PM support guide, but no evidence of a top-level direct load outside PM planning. | PM support asset | Slice04; Arc04 D-03. |
| PM examples and provenance | Useful after PM rules are loaded; weak as primary entrypoints. | PM support assets | Slice04; Arc04 D-03. |
| ontology critique | Arc02 and Project03 evidence show a useful analysis method, but no accepted reusable framework load path yet. | unresolved: possible adapter/checklist, Project03 route, or future component | Slice04; Arc04 D-12; operator question. |
| component-maintenance discipline | Missing future need rather than a current standalone workflow. | contract field set / possible maintenance owner | Slice04; Arc04 D-10; Arc05. |

## Concepts To Keep As Edges, Assets, Adapters, Constraints, Or Gates

| Classification | Concepts | Reason |
|----------------|----------|--------|
| dependency edge | posture -> methodology; ledger-verification -> PM close; style -> ticket template; repository tooling -> coverage examples; domain skills -> audit findings | The value is ordering and ownership, not a separate user-facing package. |
| support asset | contribution-ticket-template, PM examples, PM provenance/version history, audit output examples | These are useful inside workflows but over-thin as independent components. |
| adapter | framework-entrypoint, agent-adapter, repository orientation/distribution, PM wayfinder | They mediate entry and translation rather than owning full discipline. |
| constraint | source/package mode, role-language clarity, component contract fields, no source/planning confusion | These must be honored by every relevant component. |
| package/release gate | package-local link behavior, zip root behavior, release surface behavior, `make check-package-paths`, CCDP separation | These are release obligations and verification gates, not optional docs. |

## Unresolved Operator Questions For Arc04

| Decision | Question | Evidence posture |
|----------|----------|------------------|
| D-01 | Should posture ship as a standalone component, mandatory methodology prerequisite, composer floor, or some combination? | go / adjust: functional dependency is strong; package shape open. |
| D-02 | What does methodology own versus route to after breakout? | go / adjust: own pillars/SDLC/process; route operational mechanics. |
| D-03 | Should project management be one component family, separately packaged family members, or wayfinder plus selected standalone mechanics? | adjust: family evidence strong; per-file package evidence weak. |
| D-04 | Should ledger own evidence semantics while PM owns lifecycle close? | go: evidence strongly supports this dependency direction. |
| D-05 | How thin should the top-level composer be? | adjust: route plus small floor; avoid monolith load cost. |
| D-06 | Should agent-adapter ownership be central, local, or both? | go / adjust: central adapter plus short local notes is best supported. |
| D-07 | How should coverage be named for non-Claude and non-Rust use? | adjust: direct load path exists; current surface is underfit. |
| D-08 | Should audit and coverage remain siblings or become a quality-floor family? | defer wrapper: sibling workflows differ enough on current evidence. |
| D-09 | Should contribution style and ticket template package together? | go: template is support asset under contribution guidance. |
| D-10 | Who owns component-maintenance contract fields? | go for contract fields; defer standalone maintenance component. |
| D-11 | How are Project01 source/package gates represented in every component contract? | go: central gate plus per-component package/release fields. |
| D-12 | Does ontology critique become a reusable abstraction-boundary component, Project03 route, or Arc04 checklist item? | defer: lacks real functional load path today. |

## Slice04, Arc04, And Arc05 Routing

- Slice04 should synthesize scenario coverage across S-01 through S-14,
  reconcile Slice02 current-monolith baselines with Slice03 standalone and
  composed results, and prepare Arc03 close-readiness.
- Slice04 should preserve current monolith strengths as requirements:
  single-entry discovery, role-language clarity in composed use,
  source/package visibility, PM close discipline, and reproduced composition.
- Arc04 should decide component contracts, package boundaries, dependency
  edges, support assets, adapter ownership, and package/release gates with
  operator acceptance.
- Arc05 should plan concrete source edits only after Arc04 architecture is
  accepted, including README, SKILL.md, Makefile/package lists, package-local
  paths, zip roots, and `make check-package-paths`.

All routes remain analytical and non-final.
