# Component Contract Evaluation Matrix

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice02-component-contract-evaluation
status: proposed-done
matrix-status: evaluated-contract-candidates
architecture-decisions: none
```

## Input Contract

This matrix evaluates every `CAW-01` through `CAW-26` row from the verified
Slice01 architecture decision instrument:

- `../slice01-architecture-decision-instrument/cdc-verification.md`
- `../slice01-architecture-decision-instrument/artifacts/architecture-input-register.md`
- `../slice01-architecture-decision-instrument/artifacts/architecture-decision-method.md`
- `../slice01-architecture-decision-instrument/artifacts/component-contract-schema.md`
- `../slice01-architecture-decision-instrument/artifacts/candidate-architecture-worklist.md`
- `../slice01-architecture-decision-instrument/artifacts/operator-decision-and-risk-register.md`

The evidence basis is closed Arc02 conceptual evidence and closed Arc03
functional evidence, carried through the Slice01 input contract. The go /
adjust / defer posture below is a contract-evaluation result, not accepted
architecture. Slice03 owns target graph composition. Slice04 owns operator
acceptance.

## Evaluation Vocabulary

- `contract status`: how far the row can be expressed as a component contract
  before Slice03 composition.
- `risk disposition`: the current mitigation, deferral, or operator decision
  path for the row.
- `Project01 gate relevance`: whether source/package, package-local link,
  zip root, README, `SKILL.md`, Makefile, CCDP separation, release surface, or
  `make check-package-paths` constraints must bind the row.
- `go / adjust / defer`: Slice02 posture for Slice03 composition input.

## Matrix

| ID | Classification | Evidence basis | Contract status | Risk disposition | D/OQ/ARG links | Project01 gate relevance | Go / adjust / defer posture |
|----|----------------|----------------|-----------------|------------------|----------------|--------------------------|-----------------------------|
| CAW-01 | candidate component / dependency edge | Arc02 model names posture as a strong candidate and methodology prerequisite; Arc03 marks it plausible direct load in S-10; source grounding in `docs/AI-CONSTITUTION-SUPPLEMENT.md` and `SKILL.md`. | Evaluable as standalone candidate plus required composer summary; package placement remains non-final. | Avoid overclaiming automatic behavior; encode posture as prerequisite where methodology is loaded. | D-01, OQ-01, ARG-02, BNF-11. | If standalone, contract must state source/package modes, package-local links, zip root, README/SKILL wayfinding, and release gates. | go as dependency, adjust package/composer treatment. |
| CAW-02 | candidate component / router | Arc02 BNF-04 says methodology over-merges specialized operations; Arc03 model says methodology owns craft substrate and routes to specialized components. | Evaluable as core process component, but must route PM, ledger, audit, coverage, delegation, and contribution rather than duplicating them. | Prevent monolith recreation and methodology-only procedural drift by keeping posture dependency and route list explicit. | D-02, OQ-02, ARG-01, ARG-02. | Must carry package-local component links, source/package reader behavior, and release-surface routing fields. | adjust. |
| CAW-03 | candidate component | Arc02 and Arc03 both mark ledger-verification as strong direct load with low context cost and clear ownership of evidence semantics. | Ready for a full component contract. | Ledger owns evidence strength, row closure, deferral/no-op rules, and silent-drop prevention; PM owns lifecycle use. | D-04, ARG-03, FR-03, FR-11. | High: package-local links from PM close guides and release validation must preserve ledger ownership. | go. |
| CAW-04 | component family | Arc02 and Arc03 find real PM load demand but not independent top-level component status for every PM guide. | Evaluable as one PM family contract with internal guide surfaces and a PM wayfinder. | Avoid PM over-splitting; encode ledger dependency for close mechanics and artifact-home behavior. | D-03, OQ-03, ARG-03. | High: PM contains planning worktree, artifact-home, and package-local link constraints. | adjust. |
| CAW-05 | candidate component | Arc03 S-06 and FR-06 mark audit as strong direct load; Arc02 finds diagnosis-only workflow with output-home risk. | Evaluable as direct-load operational component after output-home and role-language adjustments. | Keep audit diagnosis-only; update old `workbench/` output convention to respect slice `artifacts/` default when audit outputs are durable planning artifacts. | D-08, OQ-04, ARG-04. | High: README/SKILL wayfinding, package-local examples, and `make check-package-paths` must survive packaging. | go / adjust. |
| CAW-06 | candidate component | Arc02 BNF-01/BNF-13 and Arc03 FR-07 find a real coverage workflow but underfit naming/examples. | Evaluable after surface-neutral naming or adapter treatment. | Preserve historical `CLAUDE-CODE-COVERAGE.md` provenance while making repository-specific command adaptation explicit. | D-07, OQ-05, ARG-05. | Medium/high: package name, package-local links, and README routing depend on final naming. | adjust. |
| CAW-07 | candidate component | Arc03 marks delegation-policy as strong direct load with narrow trigger and low context cost; source grounding in `docs/SUBAGENT-DELEGATION-POLICY.md`. | Ready for full component contract with short adapter notes. | Preserve thinking-vs-lookup rule and prevent subagent judgment leakage; keep role-language clear for Codex/Claude surfaces. | D-06, OQ-06, ARG-08. | Medium: package-local role adapter links and README routing required. | go. |
| CAW-08 | candidate component with support asset | Arc02 BNF-07 and Arc03 contribution rows show strong direct load only when paired with `CONTRIBUTION-TICKET.md`. | Ready for full component contract with template as support asset. | Prevent template-only overclaim and style-only under-action; keep ticket template packaged with the guide. | D-09, ARG-06. | High: template package-local link and support-asset travel are required. | go. |
| CAW-09 | top-level composer / adapter | Arc03 S-01 and S-13 require a broad session-start route, but current composer is over-rich for narrow work. | Partial composer contract only; Slice03 composes it with accepted component contracts. | Keep compact posture/process floor, discovery, and routing without retaining the monolith. | D-05, ARG-01. | High: README/SKILL release surface and package root behavior depend on composer contract. | adjust. |
| CAW-10 | adapter | Arc02 BNF-02 and Arc03 S-14 show role-language adapter need but no standalone user workflow. | Evaluable as central adapter plus local notes; not a component contract unless operator selects that shape. | Use central source of truth with drift-controlled local summaries where standalone loading needs them. | D-06, OQ-06, ARG-08. | Medium: package-local adapter links must resolve from every direct-load component. | adjust / defer component. |
| CAW-11 | adapter / constraint | Arc02 BNF-05 and Arc03 FR-08 show reader-mode and distribution routing risk. | Evaluable as repository-orientation adapter and contract requirement, not standalone discipline. | Separate human/source/package reader guidance from hard release gates. | D-11, OQ-07, ARG-07, ARG-10, ARG-11. | Primary gate row: source/package modes, package-local links, zip roots, README, SKILL.md, Makefile, and generated zip behavior. | adjust. |
| CAW-12 | PM family wayfinder / adapter | Arc02 PM model and Arc03 S-09 show PM direct-load demand through a family wayfinder. | Evaluable inside PM family contract. | Do not promote PM wayfinder to separate component unless Slice03 finds package need. | D-03, OQ-03, ARG-03. | High: PM wayfinder must maintain package-local links to internal PM guides and ledger dependency. | adjust. |
| CAW-13 | support asset / template | Arc02 BNF-07 and Arc03 contribution fit require the template to travel with contribution guidance. | Support-asset contract under contribution component. | Template alone is not a component; its owning guide controls voice and calibrated honesty. | D-09, ARG-06. | High: package-local template link is a release gate. | go as support asset; defer component. |
| CAW-14 | support asset | Arc02 BNF-15 and Arc03 PM family evidence place PM examples under PM. | Support-asset contract under PM family. | Keep examples discoverable but not load-bearing as independent PM components. | D-03, OQ-03. | Medium: package-local example links must travel with PM family if packaged. | adjust as support asset. |
| CAW-15 | support asset / maintenance evidence | Arc02 BNF-09 and Slice01 schema make version history responsibility mandatory. | Support and maintenance evidence under PM/top-level maintenance fields. | Preserve rationale and version-history ownership to prevent drift. | D-10, OQ-08, ARG-09. | High: versioned files and release-surface synchronization require explicit ownership. | go as contract requirement; defer component. |
| CAW-16 | support asset | Arc02 BNF-15 places planning anti-patterns under PM unless direct-load demand changes. | Support-asset contract under PM family. | Keep repair guidance reachable from PM wayfinder without fragmenting PM package shape. | D-03, OQ-03. | Medium: package-local links from PM wayfinder and support asset must resolve. | go as support asset; defer component. |
| CAW-17 | support asset | Arc03 FR-06 identifies audit output examples and old output conventions as adjustment need. | Support-asset contract under audit component after output-home adjustment. | Update output examples to respect slice `artifacts/` default when durable audit artifacts belong to a slice. | ARG-04, FD-05, LPF-06. | Medium/high: audit package must carry examples without reintroducing stale workbench-only language. | adjust as support asset. |
| CAW-18 | support asset / constraint | README and Makefile show CCDP as separate protocol package, not installable skill component. | Constraint/support asset under repository orientation or release gates. | Preserve CCDP separation; do not let framework breakout import protocol packaging semantics. | ARG-11, D-11, OQ-07. | Primary: CCDP package root and `make check-ccdp-package` stay separate from skill zip gates. | go as constraint; defer component. |
| CAW-19 | constraint / package/release gate | Project01 carry-forward, Arc02 BNF-14, Arc03 FR-08/FR-10, Slice01 schema. | Gate contract ready; every accepted component inherits fields. | Central gate plus per-component contract fields prevents path drift. | D-11, OQ-07, ARG-07, ARG-10. | Primary gate row: source paths, package paths, package-local links, zip root, release surface, README, SKILL.md, Makefile, and validation command fields. | go as gate. |
| CAW-20 | constraint / adapter | Arc03 functional model distinguishes source clone, generated skill zip, unzipped installed skill, and CCDP package modes. | Contract requirement ready for every component. | Reader modes must be local enough for standalone load and consistent enough not to drift. | D-11, OQ-07, ARG-07, FR-08. | Primary: source/package mode behavior and package-local links. | go as contract requirement. |
| CAW-21 | package/release gate | Arc03 FR-10 and source Makefile/README identify release surface synchronization risk. | Gate contract ready; Slice03 should place it in target architecture. | Require central gate plus per-component checklist fields. | D-10, D-11, OQ-07, OQ-08, ARG-09, ARG-10. | Primary: README, SKILL.md, Makefile package list, generated zip, and `make check-package-paths`. | go as gate. |
| CAW-22 | constraint / package/release gate | README and Makefile prove CCDP has separate `ccdp.zip` package flow. | Gate contract ready. | Keep protocol distribution out of installable skill component package shape. | ARG-11, D-11, OQ-07. | Primary: CCDP separation, package root, and `make check-ccdp-package` are distinct gates. | go as gate. |
| CAW-23 | dependency edge / non-component | Arc02 BNF-03 and Arc03 weak direct-load finding say verification-methodology is shared ontology, not standalone. | Non-component disposition; assign ownership edge to ledger/methodology relationship. | Prevent duplicated evidence vocabulary across methodology, ledger, PM close, audit, and coverage. | D-02, D-04, ARG-03, FR-11. | Medium: package-local links should cite owner instead of duplicating terminology. | defer component. |
| CAW-24 | deferred / non-component | Arc02 BNF-10 and Arc03 S-11/FR-05 find ontology critique important but not direct-load proven. | Deferred question; possible Project02 method, Project03 route, or future component. | Carry to Slice03/04 operator decision without accepting package status. | D-12, OQ-09, ARG-10. | Low/medium unless accepted later; would need full source/package fields if promoted. | defer. |
| CAW-25 | constraint / deferred component | Arc02 BNF-09 and Arc03 FR-05 require component-maintenance fields but do not prove direct standalone workflow. | Mandatory contract requirement; standalone component status deferred. | Every accepted contract must name maintenance owner and version history responsibility. | D-10, OQ-08, ARG-09. | Primary: release surface synchronization, README/SKILL updates, package lists, and version history. | go as contract requirement; defer component. |
| CAW-26 | non-component / dependency edge | Arc02 model says evidence strength and memory admission vocabulary are conceptual glue owned by ledger/methodology relationship. | Non-component disposition; cite owner instead of package duplication. | Prevent drift in evidence terms and memory admission language. | D-02, D-04, ARG-03, FR-11. | Medium: package-local references must resolve to owning component. | defer component. |

## Evaluation Summary

Rows ready for full or near-full contract work: `CAW-03`, `CAW-07`, `CAW-08`,
plus `CAW-05` after explicit output-home adjustment.

Rows requiring adjustment before architecture acceptance: `CAW-01`, `CAW-02`,
`CAW-04`, `CAW-06`, `CAW-09`, `CAW-10`, `CAW-11`, `CAW-12`, and `CAW-17`.

Rows that are support assets, constraints, gates, dependency edges,
non-components, or deferred concepts rather than standalone components:
`CAW-13` through `CAW-26`, except where `CAW-19` through `CAW-22` are go as
package/release gate rows and `CAW-25` is go as a component contract
requirement.

This matrix gives Slice03 evaluated inputs. It does not decide final target
composition, package paths, source moves, or operator acceptance.
