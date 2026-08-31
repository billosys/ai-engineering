# Operator Decision And Risk Register

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice01-architecture-decision-instrument
status: proposed-done
register-status: decision-instrument
architecture-decisions: none
```

## Input Contract

This register carries D-01 through D-12 from the Arc02 operator decision
register and OQ-01 through OQ-09 from Arc03 architecture inputs. No D/OQ rows
are merged in Slice01, because keeping both the conceptual decision source and
the functional operator question source visible improves Arc04 decision
quality. Later Arc04 slices may merge rows if the merge records the source
IDs and improves risk disposition.

Every row remains non-final. Operator acceptance is required before Arc04 can
close with an accepted architecture.

## Arc02 Decision Carry-Forward

| ID | Operator decision | Risk | Default posture | Arc04 acceptance check |
|----|-------------------|------|-----------------|------------------------|
| D-01 | Decide the posture/methodology boundary. | Merge preserves load cost; split can lose dependency order. | go / adjust / defer: go with dependency edge, adjust after functional evidence. | Operator accepts standalone posture, composer summary, or both. |
| D-02 | Decide what methodology owns versus routes to. | Too much ownership recreates the monolith; too little loses the craft substrate. | go / adjust / defer: go for ownership split, adjust wording. | Methodology contract names owned process and routed components. |
| D-03 | Decide PM component granularity. | Over-splitting PM creates drift; under-splitting preserves context load. | go / adjust / defer: adjust. | Operator accepts PM family/package strategy. |
| D-04 | Decide ledger versus PM close ownership. | Wrong ownership duplicates or weakens evidence semantics. | go / adjust / defer: go. | Ledger owns evidence; PM owns lifecycle. |
| D-05 | Decide the top-level composer contract. | Too thin loses safety floor; too rich fails breakout goal. | go / adjust / defer: adjust. | Operator accepts thin composer promise and required summaries. |
| D-06 | Decide agent-adapter ownership. | Central-only is unclear for standalone load; repeated local notes drift. | go / adjust / defer: go with drift controls. | Operator accepts central plus local notes or alternative. |
| D-07 | Decide coverage guide naming and generality. | Surface-specific naming hides a general discipline; renaming needs compatibility. | go / adjust / defer: adjust. | Coverage contract names compatibility and generality strategy. |
| D-08 | Decide audit and coverage relationship. | Broad quality family can blur diagnosis-only audit with test-editing coverage. | go / adjust / defer: defer wrapper, go with sibling distinction. | Operator accepts siblings or an explicit family wrapper. |
| D-09 | Decide contribution guide/template packaging. | Template alone overclaims; style alone is less actionable. | go / adjust / defer: go. | Template support asset travels with contribution guidance. |
| D-10 | Decide component-maintenance owner and contract fields. | No owner means README, SKILL, package, version history, and examples drift. | go / adjust / defer: go for fields; defer standalone component status. | Every accepted contract has maintenance owner and version history responsibility. |
| D-11 | Decide cross-component release gate strategy. | Extraction can break source/package, package-local, zip, and release surface promises. | go / adjust / defer: go. | Central release gate plus per-component package/release gate fields accepted. |
| D-12 | Decide whether ontology critique becomes reusable method. | New component may overfit; omitting it may under-mechanize abstraction failure. | go / adjust / defer: defer component, adjust checklist. | Operator accepts Project02-only, Project03-routed, or future-component treatment. |

## Arc03 Operator Question Carry-Forward

| ID | Operator question | Functional risk | Default posture | Arc04 acceptance check |
|----|-------------------|-----------------|-----------------|------------------------|
| OQ-01 | Is posture a standalone component, a required composer summary, or both? | Posture is needed, but package placement affects load cost and dependency order. | go / adjust / defer: go as dependency, adjust packaging. | Same disposition as D-01 with functional evidence cited. |
| OQ-02 | What does methodology own versus route to specialized components? | Over-owning recreates the monolith. | go / adjust / defer: adjust. | Same disposition as D-02 with routed component list. |
| OQ-03 | Does PM ship as one component family with internal guides or as multiple separately loadable packages? | PM direct load is real; individual guide package status is not proven. | go / adjust / defer: adjust. | Same disposition as D-03 with PM wayfinder treatment. |
| OQ-04 | Should audit and coverage remain sibling operational components? | Their workflows differ: diagnosis-only versus test/code hardening. | go / adjust / defer: go for siblings, defer broad wrapper. | Same disposition as D-08 with risk disposition. |
| OQ-05 | Should coverage be renamed or wrapped to avoid Claude/Cargo underfit? | Naming and examples can hide general framework value. | go / adjust / defer: adjust. | Same disposition as D-07 with compatibility rule. |
| OQ-06 | Is the agent adapter central-only, local-only, or central plus local notes? | Role-language clarity can fail in standalone load. | go / adjust / defer: go with central plus local notes. | Same disposition as D-06 with drift controls. |
| OQ-07 | Which component contract fields are mandatory for source/package and release gates? | Missing fields lead to broken package-local links and release surface drift. | go / adjust / defer: go. | Same disposition as D-11 and component-contract schema. |
| OQ-08 | Where does component-maintenance responsibility live? | No owner creates multi-component synchronization drift. | go / adjust / defer: go for contract fields, defer component status. | Same disposition as D-10. |
| OQ-09 | Does ontology critique become a reusable component or remain Project02/Project03 method evidence? | Component status is plausible but not proven as direct load. | go / adjust / defer: defer component. | Same disposition as D-12. |

## Consolidated Risk And Gate Register

| ID | Risk or gate | Source | Required Arc04 disposition |
|----|--------------|--------|----------------------------|
| ARG-01 | Over-rich top-level composer context cost. | Arc03 FR-01, S-01, S-13, D-05. | Decide thin composer contract and required safety floor. |
| ARG-02 | Over-thin direct-load component risk. | Arc03 FR-02 and direct-load tests. | Every contract names prerequisites, support assets, and adapters. |
| ARG-03 | PM/ledger unclear handoff. | Arc02 BNF-06, D-04; Arc03 FR-03. | Ledger owns evidence semantics; PM owns lifecycle. |
| ARG-04 | Audit output-home mismatch. | Arc03 FR-06, LPF-06, FD-05. | Contract audit output conventions against slice `artifacts/` default. |
| ARG-05 | Coverage underfit. | Arc02 BNF-01/BNF-13; Arc03 FR-07. | Rename or adapter-wrap coverage guide. |
| ARG-06 | Contribution support-asset separation. | D-09, FR-04, FD-06. | Template travels with contribution guidance. |
| ARG-07 | Source/package risk. | D-11, OQ-07, SPR rows, Project01. | Contract source path, package path, package-local links, zip root, and validation. |
| ARG-08 | Role-language risk. | D-06, OQ-06, RLF rows. | Central agent adapter plus short local notes unless operator chooses otherwise. |
| ARG-09 | Component-maintenance risk. | D-10, OQ-08, BNF-09. | Require maintenance owner and version-history responsibility. |
| ARG-10 | Ontology critique component overfit. | D-12, OQ-09, BNF-10. | Defer component status or route to Project03; do not silently package. |
| ARG-11 | CCDP package confusion. | Project01 gate, source grounding, SPR rows. | Preserve CCDP as protocol distribution, not installable skill component. |
| ARG-12 | Operator acceptance gap. | Arc04 arc plan. | Do not close Arc04 until accepted architecture is reviewed and recorded. |

## Acceptance Rules

Before Arc04 closes, every D row, OQ row, and ARG row must be accepted,
deferred with a re-entry condition, or ruled non-applicable with rationale.
The accepted architecture must include risk disposition, package/release gate
coverage, and operator acceptance evidence. This Slice01 register prepares
that work; it does not decide it.
