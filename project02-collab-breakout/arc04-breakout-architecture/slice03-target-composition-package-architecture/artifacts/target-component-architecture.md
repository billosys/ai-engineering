# Target Component Architecture

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice03-target-composition-package-architecture
status: proposed-done
artifact-status: proposed-architecture-input
source-files-edited: false
operator-acceptance: pending
```

## Input Contract

This artifact consumes the verified Slice01 architecture decision method,
component-contract schema, and operator decision register, plus the verified
Slice02 component contract evaluation, support/adapter/constraint
dispositions, package/release gate dispositions, and slice03 composition
inputs.

The proposal below is not accepted architecture. Slice04 must still record
operator acceptance, rejected alternatives, risk disposition, and any deferred
question treatment before Arc04 can close.

## Component Graph

The proposed component graph is gate-first and composer-routed:

1. Package/release gate rows bind every accepted component before package
   paths are chosen: `CAW-19`, `CAW-20`, `CAW-21`, `CAW-22`, and `CAW-25`.
2. The top-level composer remains `collaboration-framework` /
   `framework-entrypoint-and-routing` (`CAW-09`): thin but not link-only,
   with a compact posture/process floor and route table.
3. The core dependency chain is
   `collaborative-posture-and-ethics` (`CAW-01`) ->
   `engineering-methodology-and-process` (`CAW-02`) ->
   operational route choices.
4. `ledger-verification-protocol` (`CAW-03`) owns evidence semantics. The
   `project-management` component family (`CAW-04`) uses ledger for closure
   but owns lifecycle, layout, and PM wayfinding.
5. The operational direct-load siblings are `code-audit-discipline`
   (`CAW-05`), `coverage-hardening-discipline` (`CAW-06`),
   `delegation-policy` (`CAW-07`), and
   `contribution-style-and-voice` (`CAW-08`).
6. Adapter rows provide shared reader and role-language behavior without
   silently becoming standalone components: `agent-adapter-and-routing`
   (`CAW-10`), `repository-orientation-and-distribution` (`CAW-11`), and the
   PM wayfinder (`CAW-12`).
7. Support asset rows travel with their owners. Dependency edge,
   non-component, and deferred rows keep owner and re-entry conditions.

## Proposed Graph Edges

| From | To | Edge Type | Reason |
|------|----|-----------|--------|
| `collaboration-framework` composer (`CAW-09`) | all accepted components, adapters, and gates | top-level route | The composer is the broad session-start surface and selects the next component. |
| `CAW-19`/`CAW-20`/`CAW-21`/`CAW-22`/`CAW-25` | every component, component family, support asset, and adapter | package/release gate / constraint | Package roots, package-local links, release surfaces, CCDP separation, and maintenance fields bind all accepted contracts. |
| `collaborative-posture-and-ethics` (`CAW-01`) | `engineering-methodology-and-process` (`CAW-02`) | dependency edge | Methodology needs the posture floor but should not own it wholesale. |
| `engineering-methodology-and-process` (`CAW-02`) | PM, ledger, audit, coverage, delegation, contribution, domain skills | router edge | Methodology owns the craft substrate and routes to specialized operations. |
| `ledger-verification-protocol` (`CAW-03`) | `project-management` close guides (`CAW-04`) | dependency edge | PM owns lifecycle; ledger owns evidence strength, row closure, and silent-drop prevention. |
| `code-audit-discipline` (`CAW-05`) | `coverage-hardening-discipline` (`CAW-06`) | sibling handoff | Audit diagnoses; coverage edits tests/code to reach a coverage gate. No shared wrapper is proposed. |
| `code-audit-discipline` (`CAW-05`) | domain skills | dependency edge | Audit loads language/domain correctness guidance as needed. |
| `coverage-hardening-discipline` (`CAW-06`) | domain skills and target-project tooling | dependency edge | Coverage work is repository-specific and language-specific. |
| `contribution-style-and-voice` (`CAW-08`) | `CONTRIBUTION-TICKET.md` (`CAW-13`) | support asset edge | The template travels with the contribution component. |
| `project-management` (`CAW-04`) | PM examples, provenance/version notes, anti-patterns (`CAW-14`..`CAW-16`) | component family support | The PM family owns examples, repair guidance, and version-history support. |
| `code-audit-discipline` (`CAW-05`) | audit output examples (`CAW-17`) | support asset edge | Audit examples travel only after output-home language uses slice `artifacts/` when durable. |
| repository orientation / release gates (`CAW-11`, `CAW-19`..`CAW-22`) | protocol distribution guidance (`CAW-18`) | support asset / constraint edge | CCDP stays adjacent protocol distribution material, not a skill component. |
| `agent-adapter-and-routing` (`CAW-10`) | every role-bearing component | adapter edge | Central role mapping plus local notes keep standalone loads readable. |

## CAW Placement Table

Every `CAW-01` through `CAW-26` row is placed below as a component,
component family, support asset, adapter, constraint, package/release gate,
dependency edge, non-component, or deferred question. The go / adjust / defer
posture is preserved from Slice02 and adjusted placement is called out.

| ID | Proposed Placement | Go / Adjust / Defer | Owner | Source IDs | Rationale |
|----|--------------------|---------------------|-------|------------|-----------|
| CAW-01 | Component plus dependency edge: `collaborative-posture-and-ethics`; compact composer summary required. | Go as dependency; adjust package/composer treatment. | Posture component owner; composer owns only the summary. | D-01, OQ-01, ARG-02, BNF-11. | The posture is a real load surface and methodology prerequisite. The adjusted placement allows both standalone use and a small composer floor without copying the full text into the composer. |
| CAW-02 | Component / router: `engineering-methodology-and-process`. | Adjust. | Methodology component owner. | D-02, OQ-02, ARG-01, ARG-02, BNF-04. | Methodology owns craft substrate and process rigor, but routes PM, ledger, audit, coverage, delegation, contribution, and domain skills instead of recreating the monolith. |
| CAW-03 | Component: `ledger-verification-protocol`. | Go. | Ledger component owner. | D-04, ARG-03, FR-03, FR-11. | Ledger has strong direct-load evidence and owns evidence strength, row closure, deferral/no-op rules, and silent-drop prevention. |
| CAW-04 | Component family: `project-management`. | Adjust. | PM family owner. | D-03, OQ-03, ARG-03, BNF-08. | PM has real direct-load demand, but its internal guides should travel as one family with a PM wayfinder rather than separate unproven packages. |
| CAW-05 | Component: `code-audit-discipline`, with audit examples as support. | Go / adjust. | Audit component owner. | D-08, OQ-04, ARG-04, FR-06. | Audit is a strong direct-load workflow. Acceptance requires preserving diagnosis-only scope and replacing old durable-output assumptions with slice `artifacts/` where planning outputs are durable. |
| CAW-06 | Component: `coverage-hardening-discipline`, with compatibility alias or adapter note. | Adjust. | Coverage component owner. | D-07, OQ-05, ARG-05, BNF-01, BNF-13. | Coverage is a real operational discipline but needs naming/generalization work so the component is not overfit to historical Claude or Cargo examples. |
| CAW-07 | Component: `delegation-policy`. | Go. | Delegation component owner. | D-06, OQ-06, ARG-08. | Delegation has a narrow direct-load trigger and must preserve the thinking-vs-lookup boundary with role-language adapter support. |
| CAW-08 | Component with support asset: `contribution-style-and-voice`. | Go. | Contribution component owner. | D-09, ARG-06. | The guide is useful as a direct load when the `CONTRIBUTION-TICKET.md` template travels with it. |
| CAW-09 | Top-level composer / adapter: `framework-entrypoint-and-routing` in the `collaboration-framework` package. | Adjust. | Composer owner. | D-05, ARG-01. | The composer remains the broad load surface, but should become thin, not link-only: compact safety floor, route table, and package/source orientation only. |
| CAW-10 | Adapter: `agent-adapter-and-routing`; central plus local notes; standalone component deferred. | Adjust / defer component. | Central adapter owner plus component owners for local notes. | D-06, OQ-06, ARG-08. | Role-language mapping is necessary everywhere but current evidence does not justify a standalone workflow. |
| CAW-11 | Adapter / constraint: `repository-orientation-and-distribution`. | Adjust. | Repository orientation adapter and release gate owner. | D-11, OQ-07, ARG-07, ARG-10, ARG-11. | This row explains source/package reader modes while hard package/release gates remain enforceable contract checks. |
| CAW-12 | Adapter inside component family: `project-management-wayfinder`. | Adjust. | PM family owner. | D-03, OQ-03, ARG-03. | The PM wayfinder belongs inside the PM family unless Slice04 accepts a separate package need. |
| CAW-13 | Support asset / template: `CONTRIBUTION-TICKET.md`. | Go as support asset; defer component. | `contribution-style-and-voice`. | D-09, ARG-06. | The template is required for actionable contribution work but is not a standalone component. |
| CAW-14 | Support asset: PM examples. | Adjust as support asset. | `project-management`. | D-03, OQ-03, BNF-15. | Examples are discoverability and learning support for PM, not independent direct-load packages. |
| CAW-15 | Support asset / maintenance evidence: PM provenance and version history notes. | Go as contract requirement; defer component. | `project-management` plus component-maintenance fields. | D-10, OQ-08, ARG-09. | Version-history rationale supports maintenance but does not form a component by itself. |
| CAW-16 | Support asset: planning anti-patterns and repair guidance. | Go as support asset; defer component. | `project-management`. | D-03, OQ-03. | Anti-patterns remain reachable through the PM wayfinder and do not get promoted without direct-load evidence. |
| CAW-17 | Support asset: audit output examples. | Adjust as support asset. | `code-audit-discipline`. | ARG-04, FD-05, LPF-06. | Audit examples travel with audit only after they stop implying old workbench-only durable output homes. |
| CAW-18 | Support asset / constraint: protocol distribution guidance. | Go as constraint; defer component. | Repository orientation and release gate owner. | ARG-11, D-11, OQ-07. | CCDP package guidance supports separation. It is not a collaboration-framework component. |
| CAW-19 | Constraint and package/release gate: Project01 path-contract constraints. | Go as gate. | Release gate owner. | D-11, OQ-07, ARG-07, ARG-10. | Every accepted component inherits source path, package path, package-local link, zip root, release surface, README, `SKILL.md`, Makefile, and validation command fields. |
| CAW-20 | Constraint / adapter: source/package reader modes. | Go as contract requirement. | Repository orientation adapter and component owners. | D-11, OQ-07, ARG-07, FR-08. | Components must state behavior for source clone, generated zip, installed skill, and CCDP-adjacent reader modes. |
| CAW-21 | Package/release gate: release surface synchronization. | Go as gate. | Release gate owner. | D-10, D-11, OQ-07, OQ-08, ARG-09, ARG-10. | README, `SKILL.md`, component entrypoints, source docs, package list entries, generated zip behavior, and checks must change together. |
| CAW-22 | Constraint and package/release gate: CCDP separation. | Go as gate. | CCDP separation / release gate owner. | ARG-11, D-11, OQ-07. | CCDP remains a protocol distribution with `ccdp.zip`, not an installable skill component or package dependency. |
| CAW-23 | Dependency edge / non-component: verification-methodology. | Defer component. | Ledger/methodology relationship. | D-02, D-04, ARG-03, FR-11. | The concept is not discarded, but ledger owns evidence semantics and methodology cites the process relation; no standalone load is proven. |
| CAW-24 | Deferred question / non-component: ontology critique. | Defer. | Project02 architecture method; possible Project03 or future owner. | D-12, OQ-09, ARG-10. | Ontology critique stays visible as architecture method evidence until operator or Project03 evidence justifies a reusable component. |
| CAW-25 | Constraint / contract requirement; standalone component deferred: component-maintenance discipline. | Go as contract requirement; defer component. | Release gate owner plus every component owner. | D-10, OQ-08, ARG-09. | Maintenance ownership and version history are mandatory fields for all accepted contracts, but no direct-load maintenance workflow is proven. |
| CAW-26 | Non-component / dependency edge: evidence strength and memory admission vocabulary. | Defer component. | Ledger/methodology relationship; future memory/evidence ontology if accepted. | D-02, D-04, ARG-03, FR-11. | Evidence strength belongs to ledger and methodology references. Memory admission language remains a citation edge unless a future memory project creates direct-load demand. |

## Adjusted Placement Notes

- `CAW-01` is not reduced to composer prose. It becomes a component candidate
  and dependency edge with a compact top-level summary.
- `CAW-02` is not a container for PM, ledger, audit, coverage, delegation, or
  contribution. It becomes a router with explicit dependency order.
- `CAW-04` is a component family, not a set of separate packages for each PM
  guide.
- `CAW-05` accepts the audit component but gates old output-home examples until
  durable outputs use slice `artifacts/` or an explicitly chosen output home.
- `CAW-06` remains a component candidate but must carry naming and
  compatibility treatment.
- `CAW-09` stays the top-level composer and remains useful on its own; it does
  not own full component bodies.
- `CAW-10` and `CAW-11` are adapters, not default standalone components.
- `CAW-23`, `CAW-24`, `CAW-25` standalone status, and `CAW-26` are not
  discarded. They remain owner-linked non-component or deferred rows with
  re-entry conditions for Slice04.
