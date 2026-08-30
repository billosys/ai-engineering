# Arc04 Operator Decision Register

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice03-ontology-decision-synthesis
status: proposed-done
architecture-decisions: none
```

## Evidence Basis

This register consumes the Slice01 input contract and CDC verification plus the
verified Slice02 `candidate-boundary evaluation`,
`component relationship map`, and `conceptual risk register`. It turns Arc02
analysis into explicit operator decisions for Arc04 architecture.

Each row is an operator decision candidate, not an accepted architecture
choice. Project01 and `project01-harmonise-paths` remain cross-cutting
component contract constraints for source/package language, package-local
links, zip roots, release surface guidance, CCDP package separation, and
`make check-package-paths`.

## Decisions

| ID | Operator decision | Decision owner | Options | Evidence basis | Risk | Default recommendation | Go / adjust / defer posture | Why this belongs before Arc04 |
|----|-------------------|----------------|---------|----------------|------|------------------------|-----------------------------|-------------------------------|
| D-01 | Decide the posture/methodology boundary. | Operator with Arc04. | A: posture standalone plus methodology prerequisite. B: posture merged into methodology. C: posture only in top-level composer. | Slice02 rows for posture and methodology; risk R-03; Arc02 Q-01. | Merge preserves load cost; split can make methodology procedural if dependency is lost. | Treat posture as standalone candidate and mandatory methodology prerequisite. | go / adjust / defer: go with dependency edge, adjust after Arc03 usage evidence. | Arc04 cannot design component contracts without knowing whether posture is a component, dependency, or summary. |
| D-02 | Decide what methodology owns versus routes to. | Arc04 with operator review. | A: methodology owns pillars, SDLC, anti-degradation, and routing. B: methodology owns all operational guides. C: methodology becomes a thin index only. | Slice02 methodology row; relationship map routes-to edges; risk R-03. | Too much ownership recreates the monolith; too little loses the craft substrate. | Keep methodology as core component that routes to PM, ledger, audit, coverage, delegation, and contribution. | go / adjust / defer: go for ownership split, adjust wording after Arc03. | This decides several downstream component scopes at once. |
| D-03 | Decide PM component granularity. | Operator and Arc04. | A: one PM component with internal guides. B: separately loadable PM family members. C: PM wayfinder plus selected standalone guides. | Slice02 PM grouping; risks R-13, R-14, R-20; Arc02 Q-04. | Over-splitting PM creates drift; under-splitting preserves context load. | Model PM as one component family with internal guides; leave package granularity open until Arc03. | go / adjust / defer: adjust; concept model is strong, package split deferred. | Arc04 must choose package boundaries and SKILL entrypoints for PM before implementation planning. |
| D-04 | Decide ledger versus PM close ownership. | Operator and Arc04. | A: ledger owns evidence semantics; PM owns lifecycle close. B: PM owns all close semantics. C: ledger owns all close mechanics. | Slice02 relationship map; risk R-05; Arc02 Q-03. | Wrong ownership duplicates or weakens evidence semantics. | Ledger owns evidence strength and row closure; PM close guides use ledger and own bubble-up lifecycle. | go / adjust / defer: go. | Arc04 needs this dependency direction before packaging ledger and PM components. |
| D-05 | Decide the top-level composer contract. | Operator. | A: thin composer/router. B: default bundle with posture and methodology summaries. C: rich monolith retained. | Slice02 row for `framework-entrypoint-and-routing`; adapter overlap R-16; Arc02 Q-06. | Too thin may lose safety floor; too rich fails breakout goal. | Thin composer with minimal posture/process floor and explicit routes to components. | go / adjust / defer: adjust after Arc03 load tests. | Arc04 architecture begins from the entrypoint promise. |
| D-06 | Decide agent-adapter ownership. | Operator and Arc04. | A: one central adapter guide. B: repeated local notes in each component. C: central adapter plus short local notes. | Slice02 row for `agent-adapter-and-routing`; risk R-02; Arc02 Q-11. | Central-only adapter can make standalone components unclear; repeated notes can drift. | Central adapter plus minimal local notes where role language appears. | go / adjust / defer: go with drift controls. | Every standalone component needs correct CDC/CC/Codex/Claude interpretation. |
| D-07 | Decide coverage guide naming and generality. | Operator and Arc04. | A: rename to surface-neutral coverage-hardening component. B: keep historical Claude Code title. C: keep title but add prominent adapter. | Slice02 coverage row; risks R-01 and R-11; Arc02 Q-10. | Surface-specific naming may hide a general discipline; renaming may require careful compatibility guidance. | Rename or wrap with surface-neutral component language while preserving provenance. | go / adjust / defer: adjust; final name should wait for Arc04 naming pass. | Naming affects component discoverability and package entrypoints. |
| D-08 | Decide audit and coverage relationship. | Arc04 with operator review. | A: sibling operational components. B: broader quality-floor family. C: coverage as methodology appendix. | Slice02 rows for audit, modernization, and coverage; unresolved relationship question. | A broad family can blur diagnosis-only audit with test-editing coverage work. | Treat them as sibling components for now; defer any quality-family wrapper until Arc03. | go / adjust / defer: defer wrapper, go with sibling distinction. | Arc04 needs separate contracts if workflows differ. |
| D-09 | Decide contribution guide/template packaging. | Arc04. | A: one contribution-guidance component with template asset. B: two components. C: template only. | Slice02 contribution rows; risks R-06 and R-18; Arc02 Q-13. | Template alone invites formulaic, overclaimed tickets; style alone is less actionable. | One contribution-guidance component with `CONTRIBUTION-TICKET.md` as support template. | go / adjust / defer: go. | Arc04 must specify template placement and package-local links. |
| D-10 | Decide component-maintenance owner and contract fields. | Operator and Arc04. | A: top-level composer owns maintenance. B: each component owns local maintenance plus shared gate. C: separate maintenance contract. | Slice02 risk R-07; `framework-maintenance-discipline`; Arc02 Q-14. | No owner means README, SKILL, package, version history, and examples drift after breakout. | Add component contract fields: owner, source paths, package behavior, dependency links, verification gates, support assets, and version-history rule. | go / adjust / defer: go for contract fields; defer standalone component status. | Architecture acceptance needs maintenance semantics before source edits start. |
| D-11 | Decide cross-component release gate strategy. | Operator and Arc04. | A: central gates only. B: per-component gates only. C: central gates plus per-component package contract fields. | Project01 path contract; Slice02 path row; Arc02 Q-07/Q-15. | Component extraction can break source/package, package-local, zip, and release surface promises. | Central release gate plus repeated per-component package/release gate fields. | go / adjust / defer: go. | Arc04/Arc05 must preserve Project01 constraints by design, not late repair. |
| D-12 | Decide whether ontology critique becomes reusable method. | Operator and Arc04. | A: add reusable abstraction-boundary component. B: keep as Project02-only method. C: route to Project03 concept-card method. | Slice02 missing concept R-08; Arc02 Q-05. | A new component may overfit this project; omitting it may leave abstraction failure under-mechanized. | Defer final component status; require Arc04 to name where boundary-review discipline lives. | go / adjust / defer: defer component, adjust architecture checklist. | Arc04 is the first point where concept-boundary decisions become architecture. |

## Decision Ordering

Recommended Arc04 order:

1. D-11 release gate strategy, because every component contract inherits it.
2. D-05 top-level composer contract.
3. D-01, D-02, and D-04 for core posture/methodology/ledger ownership.
4. D-03 PM granularity.
5. D-06 adapter ownership.
6. D-07, D-08, and D-09 specialized guide packaging.
7. D-10 and D-12 maintenance and ontology-review placement.

This register is analytical and does not decide final architecture. Operator
acceptance in Arc04 remains required.
