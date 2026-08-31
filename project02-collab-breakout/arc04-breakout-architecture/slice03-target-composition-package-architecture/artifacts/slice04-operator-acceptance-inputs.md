# Slice04 Operator Acceptance Inputs

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice03-target-composition-package-architecture
status: proposed-done
artifact-status: slice04-acceptance-input
operator-acceptance: pending
source-files-remain-untouched: true
```

## Input Contract

This artifact packages Slice04 acceptance inputs from the verified Slice01
architecture decision method and operator decision register, the verified
Slice02 component contract evaluation and slice03 composition inputs, and the
Slice03 proposed architecture artifacts:

- `artifacts/target-component-architecture.md`;
- `artifacts/dependency-and-composition-order.md`;
- `artifacts/package-and-release-architecture.md`;
- `artifacts/wayfinding-adapter-and-support-plan.md`.

The architecture is proposed, not accepted. Operator acceptance is pending.
Source files remain untouched; no source edits were made in Slice03.

## Proposed Decisions For Slice04

| Decision | Source IDs | Proposed Decision | Risk Disposition | Rejected Alternatives |
|----------|------------|-------------------|------------------|-----------------------|
| Posture placement | D-01, OQ-01, ARG-02, BNF-11, CAW-01 | Accept `collaborative-posture-and-ethics` as a component plus dependency edge, with compact composer summary. | Mitigates over-thin direct-load risk by retaining methodology dependency. | Composer-only posture; methodology-owned posture; standalone posture with no composer summary. |
| Methodology boundary | D-02, OQ-02, ARG-01, ARG-02, BNF-04, CAW-02 | Accept `engineering-methodology-and-process` as a process component/router. | Mitigates monolith recreation by routing PM, ledger, audit, coverage, delegation, contribution, and domain skills. | Methodology monolith; methodology reduced to links only; separate component for every SDLC subtopic. |
| PM granularity | D-03, OQ-03, ARG-03, CAW-04, CAW-12, CAW-14, CAW-16 | Accept `project-management` as a component family with PM wayfinder and support assets. | Avoids PM guide over-splitting while preserving direct PM load surface. | Separate packages for every PM guide; bury PM inside methodology. |
| Ledger ownership | D-04, ARG-03, FR-03, FR-11, CAW-03, CAW-23, CAW-26 | Accept `ledger-verification-protocol` as direct-load component and evidence owner. | Keeps evidence strength and row closure out of PM lifecycle prose duplication. | Ledger as PM-only appendix; ledger spread across methodology, audit, and coverage. |
| Top-level composer | D-05, ARG-01, CAW-09 | Accept a thin but not link-only `collaboration-framework` composer with compact safety floor and route table. | Controls top-level context cost while preserving broad session-start usability. | Existing monolith; link-only index; no top-level composer. |
| Agent adapter | D-06, OQ-06, ARG-08, CAW-10 | Accept central plus local notes for `agent-adapter-and-routing`; defer standalone package. | Central source limits drift; local notes preserve standalone readability. | Central-only adapter; local-only repeated notes; standalone adapter component now. |
| Coverage naming and generality | D-07, OQ-05, ARG-05, CAW-06 | Accept `coverage-hardening-discipline` with compatibility alias or adapter from historical `CLAUDE-CODE-COVERAGE.md`. | Preserves history while making non-Claude/non-Cargo usage explicit. | Hard rename without compatibility; keep surface-specific name without adapter; merge coverage into audit. |
| Audit/coverage relationship | D-08, OQ-04, ARG-04, CAW-05, CAW-06, CAW-17 | Accept audit and coverage as sibling operational components. | Preserves diagnosis-only audit and implementation-oriented coverage hardening. | Broad quality wrapper; audit owns coverage; coverage owns audit findings. |
| Contribution guide/template | D-09, ARG-06, CAW-08, CAW-13 | Accept `contribution-style-and-voice` as direct-load component with `CONTRIBUTION-TICKET.md` support asset. | Keeps voice and template coupled without promoting template alone. | Template-only package; contribution prose without template. |
| Maintenance ownership | D-10, OQ-08, ARG-09, CAW-15, CAW-21, CAW-25 | Accept maintenance owner and version-history responsibility as mandatory component fields; defer standalone component. | Prevents README, SKILL, package, examples, and version-history drift. | No explicit owner; standalone maintenance package now. |
| Release gate strategy | D-11, OQ-07, ARG-07, ARG-10, ARG-11, CAW-11, CAW-18, CAW-19, CAW-20, CAW-21, CAW-22 | Accept central package/release gates plus per-component source/package fields. | Preserves package-local links, zip root behavior, release surface synchronization, and CCDP separation. | Package paths first; prose-only gate; bundle CCDP with skills. |
| Ontology critique | D-12, OQ-09, ARG-10, ARG-12, CAW-24 | Defer standalone ontology critique component; keep as Project02/Project03 method evidence and acceptance checklist item. | Avoids overfitting a component before direct-load evidence exists. | Package ontology critique now; silently drop the concept. |

## Open Risks For Slice04

| Risk | Source IDs | Slice04 Acceptance Check |
|------|------------|--------------------------|
| Top-level composer may become too thin or too rich. | ARG-01, D-05, CAW-09 | Operator accepts exact composer promise: compact safety floor, route table, and no full component bodies. |
| Direct-load components may lose prerequisites. | ARG-02, D-01, D-02, CAW-01, CAW-02 | Operator confirms dependency edges and local adapter notes. |
| PM/ledger handoff may drift. | ARG-03, D-03, D-04, OQ-03, CAW-03, CAW-04 | Operator accepts ledger as evidence owner and PM as lifecycle owner. |
| Audit output homes can regress to old workbench-only language. | ARG-04, OQ-04, CAW-05, CAW-17 | Operator accepts slice `artifacts/` as the durable planning default, with explicit override allowed. |
| Coverage remains underfit to a specific agent/toolchain. | ARG-05, D-07, OQ-05, CAW-06 | Operator accepts final name or compatibility adapter. |
| Contribution template can separate from contribution style. | ARG-06, D-09, CAW-08, CAW-13 | Operator accepts template support asset travel. |
| Source/package breakage can occur during implementation. | ARG-07, D-11, OQ-07, CAW-19, CAW-20, CAW-21 | Operator accepts mandatory source/package fields and `make check-package-paths`. |
| Role-language can be unclear in standalone packages. | ARG-08, D-06, OQ-06, CAW-10 | Operator accepts central plus local notes or records an alternative. |
| Maintenance responsibility can be underspecified. | ARG-09, D-10, OQ-08, CAW-15, CAW-25 | Operator accepts maintenance owner and version-history fields for every component. |
| Ontology critique can be overfit or silently dropped. | ARG-10, D-12, OQ-09, CAW-24 | Operator accepts deferred placement and re-entry condition. |
| CCDP package confusion can reappear. | ARG-11, D-11, OQ-07, CAW-18, CAW-22 | Operator accepts CCDP separation as a package/release gate. |
| Operator acceptance gap can be skipped. | ARG-12, D-12, OQ-09 | Operator acceptance required before Arc04 close or Arc05 implementation planning. |

## Deferred Questions And Re-Entry Conditions

| Deferred Question | Source IDs | Current Placement | Re-entry Condition |
|-------------------|------------|-------------------|--------------------|
| Should `agent-adapter-and-routing` become standalone? | D-06, OQ-06, ARG-08, CAW-10 | Adapter, central plus local notes. | Reopen only if users need direct-load role mapping independent of another component. |
| Should PM guides become separate packages? | D-03, OQ-03, ARG-03, CAW-04, CAW-12, CAW-14, CAW-16 | PM component family. | Reopen if direct-load evidence shows one PM guide has a distinct workflow and low-context standalone load. |
| Should audit/coverage receive a broad quality wrapper? | D-08, OQ-04, ARG-04, ARG-05, CAW-05, CAW-06 | Sibling operational components. | Reopen if repeated workflows require a combined quality orchestration package. |
| Should component-maintenance become standalone? | D-10, OQ-08, ARG-09, CAW-25 | Contract requirement and package/release gate. | Reopen if maintenance itself becomes a recurring direct-load workflow. |
| Should verification-methodology become a component? | D-02, D-04, ARG-03, CAW-23 | Dependency edge / non-component. | Reopen if evidence shows direct-load use beyond ledger and methodology ownership. |
| Should ontology critique become reusable method? | D-12, OQ-09, ARG-10, ARG-12, CAW-24 | Deferred non-component; Project02/Project03 method evidence. | Reopen if operator asks for reusable abstraction-boundary method or Project03 supplies component-ready evidence. |
| Should evidence strength and memory admission vocabulary become a package? | D-02, D-04, ARG-03, FR-11, CAW-26 | Non-component / dependency edge. | Reopen only in a future memory protocol or evidence ontology effort with direct-load evidence. |

## Rejected Alternatives

Slice03 recommends rejecting these alternatives unless Slice04 records a new
operator decision:

- Keep the current collaboration-framework monolith unchanged.
- Replace the top-level composer with a link-only index.
- Make every PM guide its own component package now.
- Merge audit and coverage into a broad quality wrapper.
- Promote `CONTRIBUTION-TICKET.md`, PM examples, audit examples, or protocol
  distribution guidance to standalone components.
- Choose package paths before Project01 source/package and package/release
  gates are accepted.
- Bundle CCDP into collaboration-framework skill packages.
- Treat deferred/non-component rows as discarded.

## Arc05 Implementation-Plan Fields

If Slice04 accepts the proposed architecture, Arc05 should create an
implementation-plan with these fields for every accepted component, component
family, support asset, adapter, constraint, and package/release gate:

| Field | Required Content |
|-------|------------------|
| Source edits | Exact source files to edit, move, split, or stage. |
| README updates | Source-clone route, component route, composed collaboration-framework route, package route, and CCDP separation text. |
| SKILL.md entrypoints | Top-level composer changes and every component `SKILL.md` entrypoint. |
| Packaging changes | Makefile target/list changes, package roots, support asset travel, generated zip behavior, and package-local link rules. |
| Validation gates | `make check-skills`, `make check-package-paths`, package build targets, and CCDP validation only if CCDP source is touched. |
| Migration notes | Compatibility aliases, renamed surfaces, current `collaboration-framework.zip` migration, and old workbench output-home language updates. |
| Review concerns | Over-thin direct loads, monolith recreation, PM/ledger drift, role-language drift, package-local link drift, and unsupported component promotion. |

Arc05 must preserve operator acceptance evidence from Slice04 and must not
upgrade proposed package paths into final package paths without that evidence.

## Source Boundary

Source files remain untouched in Slice03. There were no source edits, no
README updates, no `SKILL.md` entrypoints changed, no Makefile/package list
updates, no packaging changes, no generated zip changes, and no CCDP package
changes.

Slice04 owns operator acceptance. Arc05 owns implementation planning only
after operator acceptance required fields are recorded.
