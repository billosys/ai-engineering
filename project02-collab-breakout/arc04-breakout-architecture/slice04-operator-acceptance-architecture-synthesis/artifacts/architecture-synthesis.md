# Architecture Synthesis

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice04-operator-acceptance-architecture-synthesis
architecture-status: accepted-architecture
operator-acceptance: accepted
accepted-architecture: accepted-with-adjustments
explicit-operator-evidence: recorded
source-files-edited: false
```

## Status

This architecture synthesis originally recorded the proposed architecture from
verified Slice01, Slice02, and Slice03 inputs before operator acceptance was
available.

Operator acceptance has now been recorded in
`operator-accepted-architecture.md`. The component table below preserves the
pre-acceptance synthesis; the accepted names, contracts, package/source
assumptions, and adjusted component boundaries are authoritative in
`operator-accepted-architecture.md`.

## Component Contracts

| Component name | Contract | Dependency | Package/source assumption | Acceptance status |
|----------------|----------|------------|---------------------------|-------------------|
| `collaboration-framework` | Top-level composer and framework-entrypoint-and-routing surface; thin but not link-only, with compact safety floor and route table. | Routes to all accepted components, adapters, support assets, and package/release gates. | Current source starts at top-level `SKILL.md`, README, `docs/`, and `templates/`; future package root proposed as `collaboration-framework/`. | pending |
| `collaborative-posture-and-ethics` | Direct-load posture component plus compact composer summary. | Prerequisite to methodology; route to contribution where public voice matters. | Source assumption: `docs/AI-CONSTITUTION-SUPPLEMENT.md`; package/source links remain non-final. | pending |
| `engineering-methodology-and-process` | Process component/router; owns craft substrate and routes specialized operations. | Depends on posture; routes PM, ledger, audit, coverage, delegation, contribution, and domain skills. | Source assumption: `docs/AI-ENGINEERING-METHODOLOGY.md`; package root pending. | pending |
| `ledger-verification-protocol` | Direct-load evidence component; owns evidence strength, row closure, deferral/no-op handling, and silent-drop prevention. | PM close depends on ledger; methodology, audit, and coverage may cite ledger evidence semantics. | Source assumption: `templates/LEDGER-DISCIPLINE.md` and PM close docs; package root pending. | pending |
| `project-management` | Component family with PM wayfinder; owns project/arc/slice lifecycle, planning layout, open/close mechanics, examples, and anti-pattern guidance. | Depends on ledger for evidence closure; includes PM wayfinder and support assets. | Source assumption: `docs/PROJECT-MANAGEMENT.md` plus `docs/pm/*.md`; package root pending. | pending |
| `code-audit-discipline` | Diagnosis-only audit component with findings, evidence, synthesis, and domain-skill routing. | Sibling handoff to coverage only when implementation hardening is requested; uses domain skills as needed. | Source assumption: `docs/CODE-AUDIT.md`; audit output examples must use slice `artifacts/` or explicit output home. | pending |
| `coverage-hardening-discipline` | Coverage improvement component with compatibility treatment for old Claude/Cargo naming. | Uses domain skills and target-project test tooling. | Source assumption: `docs/CLAUDE-CODE-COVERAGE.md`; package root and compatibility alias pending. | pending |
| `delegation-policy` | Direct-load delegation component for subagent and lookup boundaries. | Uses agent adapter role terms; routes to methodology or audit for broader process. | Source assumption: `docs/SUBAGENT-DELEGATION-POLICY.md`; package root pending. | pending |
| `contribution-style-and-voice` | Direct-load contribution component plus package-local `CONTRIBUTION-TICKET.md` support asset. | Uses posture for voice and audit findings as possible inputs. | Source assumption: `docs/CONTRIBUTION-STYLE.md` and `templates/CONTRIBUTION-TICKET.md`; package root pending. | pending |

## Adapters, Support Assets, And Gates

| Item | Placement | Owner | Citation edge | Re-entry condition |
|------|-----------|-------|---------------|--------------------|
| `agent-adapter-and-routing` | adapter; central plus local notes; standalone component deferred. | Central adapter owner plus component owners for local notes. | D-06, OQ-06, ARG-08, CAW-10. | Reopen if direct-load role mapping becomes a workflow independent of another component. |
| `repository-orientation-and-distribution` | adapter and constraint for source/package reader modes. | Repository orientation and release gate owner. | D-11, OQ-07, ARG-07, ARG-10, ARG-11, CAW-11. | Reopen if package/source assumptions change during Arc05. |
| `project-management-wayfinder` | PM wayfinder inside PM component family. | `project-management`. | D-03, OQ-03, ARG-03, CAW-12. | Reopen if a standalone PM wayfinder package is explicitly requested. |
| `CONTRIBUTION-TICKET.md` | support asset. | `contribution-style-and-voice`. | D-09, ARG-06, CAW-13. | Reopen if the template must be consumed without contribution guidance. |
| PM examples | support asset. | `project-management`. | D-03, OQ-03, CAW-14. | Reopen if direct-load evidence supports separate example package. |
| PM provenance/version notes | support asset and component-maintenance evidence. | `project-management` plus maintenance fields. | D-10, OQ-08, ARG-09, CAW-15. | Reopen if maintenance becomes a standalone workflow. |
| Planning anti-pattern guidance | support asset. | `project-management`. | D-03, OQ-03, CAW-16. | Reopen if it becomes a separate repair component. |
| Audit output examples | support asset with output-home adjustment. | `code-audit-discipline`. | ARG-04, CAW-17. | Reopen if examples cannot be package-local or preserve slice `artifacts/` default. |
| Protocol distribution guidance | support asset / constraint. | Repository orientation and release gate owner. | D-11, OQ-07, ARG-11, CAW-18, CAW-22. | Reopen if CCDP packaging changes. |
| Project01 path-contract gates | package/release gate and source/package constraint. | Release gate owner plus every component owner. | D-11, OQ-07, ARG-07, CAW-19, CAW-20, CAW-21, CAW-22, CAW-25. | Reopen if Arc05 cannot satisfy package-local links, zip root behavior, or validation command coverage. |

## Deferred Decisions

| Deferred decision | Current placement | Owner | Citation edge | Re-entry condition |
|-------------------|------------------|-------|---------------|--------------------|
| verification-methodology component status | dependency edge / non-component. | Ledger/methodology relationship. | D-02, D-04, ARG-03, CAW-23. | Reopen only if operator or later use evidence shows direct-load need beyond ledger and methodology ownership. |
| ontology critique component status | deferred decision / non-component. | Project02 architecture method; possible Project03 or future owner. | D-12, OQ-09, ARG-10, ARG-12, CAW-24. | Reopen if operator requests reusable abstraction-boundary method or Project03 supplies component-ready evidence. |
| component-maintenance standalone status | contract requirement and package/release gate; standalone component deferred. | Release gate owner plus every component owner. | D-10, OQ-08, ARG-09, CAW-25. | Reopen if maintenance becomes an independent recurring workflow. |
| evidence strength and memory admission vocabulary package status | non-component / dependency edge. | Ledger/methodology relationship; possible future memory/evidence owner. | D-02, D-04, ARG-03, CAW-26. | Reopen only in a future memory protocol or evidence ontology effort with direct-load evidence. |

## Arc05 Implications

Arc05 may use `operator-accepted-architecture.md` as accepted architecture
input. Its implementation-plan should preserve source/package assumptions,
specify exact source edits, README changes, `SKILL.md` entrypoints,
Makefile/package list updates, generated zip behavior, validation gates,
migration notes, and review concerns.

The source checkout remains untouched by this slice.
