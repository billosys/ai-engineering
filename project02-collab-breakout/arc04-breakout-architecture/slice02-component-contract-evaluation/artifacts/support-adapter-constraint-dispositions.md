# Support, Adapter, Constraint, And Deferred Dispositions

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice02-component-contract-evaluation
status: proposed-done
architecture-decisions: none
```

## Input Contract

This artifact dispositions support asset, adapter, constraint, dependency
edge, package/release gate, non-component, and deferred rows from `CAW-09`
through `CAW-26`. It consumes the verified Slice01 architecture decision
instrument and preserves merged source IDs where rows overlap D/OQ/ARG risks.

These dispositions are evaluated contract inputs. They are not accepted
architecture and do not decide final package paths.

## Composer And Adapter Rows

| ID | Row | Disposition | Owner Candidate | Dependency Edge | Risk / Decision Links |
|----|-----|-------------|-----------------|-----------------|-----------------------|
| CAW-09 | top-level composer / `framework-entrypoint-and-routing` | Adapter/composer, adjust. Keep `/collaboration-framework` as a thin broad-load route with compact posture/process floor and explicit component routing. | Top-level composer. | Routes to posture, methodology, PM, ledger, audit, coverage, delegation, contribution, repository orientation, and agent adapter. | D-05, ARG-01. |
| CAW-10 | agent adapter / `agent-adapter-and-routing` | Adapter, adjust / defer standalone component. Use central adapter plus short local notes unless operator chooses another pattern. | Agent adapter owner plus each component owner for local notes. | Every role-bearing component depends on adapter semantics. | D-06, OQ-06, ARG-08. |
| CAW-11 | `repository-orientation-and-distribution` | Adapter / constraint, adjust. Separate reader orientation from hard package/release gates. | Repository orientation adapter and release gate owner. | Every component depends on source/package reader-mode language. | D-11, OQ-07, ARG-07, ARG-10, ARG-11. |
| CAW-12 | `project-management-wayfinder` | PM family wayfinder / adapter, adjust. Keep inside PM family by default. | Project-management family. | Routes PM users to project/arc/slice/open/close/ledger guide surfaces. | D-03, OQ-03, ARG-03. |

## Support Asset Rows

| ID | Support Asset | Disposition | Owning Component | Package/Release Handling | Risk / Decision Links |
|----|---------------|-------------|------------------|--------------------------|-----------------------|
| CAW-13 | `CONTRIBUTION-TICKET.md` | support asset / template. Do not promote to standalone component. | `contribution-style-and-voice`. | Must travel with contribution package; package-local links from guide to template must resolve. | D-09, ARG-06. |
| CAW-14 | PM examples | support asset. Keep under PM family unless later direct-load evidence appears. | `project-management`. | Package with PM family if PM package includes examples; otherwise keep source route explicit. | D-03, OQ-03, BNF-15. |
| CAW-15 | PM provenance and version history notes | support asset / maintenance evidence. Preserve as rationale, not component. | `project-management` plus component-maintenance contract fields. | Version-history responsibility must remain visible in source and package modes. | D-10, OQ-08, ARG-09. |
| CAW-16 | planning anti-patterns and repair guidance | support asset. Keep discoverable through PM wayfinder. | `project-management`. | Package-local links from PM wayfinder to anti-pattern guidance must resolve. | D-03, OQ-03. |
| CAW-17 | audit output examples | support asset, adjust. Keep under audit after output-home convention is corrected. | `code-audit-discipline`. | Examples must not force old workbench-only paths when durable slice artifacts belong in slice `artifacts/`. | ARG-04, FD-05, LPF-06. |
| CAW-18 | protocol distribution guidance | support asset / constraint. Keep CCDP guidance separate from installable skill components. | Repository orientation / release gate owner. | README and Makefile show CCDP package root and `make check-ccdp-package`; do not include it in skill zips. | ARG-11, D-11, OQ-07. |

## Constraint And Package/Release Gate Rows

| ID | Constraint / Gate | Disposition | Required Contract Effect | Validation / Evidence |
|----|-------------------|-------------|--------------------------|-----------------------|
| CAW-19 | Project01 path-contract constraints | constraint / package/release gate, go. | Every accepted component contract must state source paths, package paths, package-local links, zip root assumptions, release surface behavior, README and `SKILL.md` routing, Makefile package list impact, and validation commands. | `make check-package-paths`; Project01 carry-forward in project, Arc02, Arc03, and Slice01 artifacts. |
| CAW-20 | source/package reader modes | constraint / adapter, go as contract requirement. | Every component must say how it reads in source clone, generated skill zip, unzipped installed skill, and adjacent CCDP package contexts where relevant. | Arc03 FR-08, SPR rows, source README and Makefile. |
| CAW-21 | release surface synchronization | package/release gate, go. | Any new or renamed component must update README, top-level `SKILL.md` routes, relevant component entrypoint, package lists, package-path exceptions, and generated zip expectations in the same implementation slice. | `make check-skills`, `make check-package-paths`, package list review. |
| CAW-22 | CCDP separation | constraint / package/release gate, go. | CCDP remains a protocol distribution with `ccdp.zip`; collaboration-framework component breakout must not treat CCDP as an installable skill component. | README CCDP section, Makefile `ccdp-package` and `check-ccdp-package`. |

## Dependency Edge And Non-Component Rows

| ID | Concept | Disposition | Owner / Citation Edge | Re-entry Condition |
|----|---------|-------------|-----------------------|--------------------|
| CAW-23 | verification-methodology | dependency edge / non-component; defer component. | Ledger owns evidence-grade vocabulary and row closure. Methodology cites the concept when explaining process rigour. PM close uses ledger; audit and coverage cite evidence semantics. | Reopen only if Slice04/operator or later use evidence shows a natural direct-load workflow not covered by ledger/methodology. |
| CAW-24 | ontology critique | deferred / non-component. | Project02 architecture method and Project03 concept-card method remain current homes; Slice03 may include it as an architecture checklist item. | Reopen if operator asks for reusable abstraction-boundary method or Project03 delivers a component-ready guide. |
| CAW-25 | component-maintenance discipline | constraint / deferred component; go as contract requirement. | Every accepted component contract must name maintenance owner, source path, package path, support assets, version history responsibility, and release gates. | Reopen standalone component status only if maintenance becomes an independent recurring workflow rather than a contract field set. |
| CAW-26 | evidence strength and memory admission vocabulary | non-component / dependency edge; defer component. | Ledger owns evidence strength; methodology owns broader process relation; memory-admission vocabulary remains a citation edge, not a package. | Reopen only if a later project creates a memory protocol or evidence ontology component with direct-load evidence. |

## Explicit Non-Promotion Rules

- A support asset stays with its owner unless Slice03 records a concrete
  reason-to-load stronger than its owning component.
- An adapter may be central, local, or both, but does not become a component
  merely because every component needs it.
- A constraint or package/release gate becomes contract language and validation
  work, not a user-facing guide by default.
- A dependency edge must name direction of ownership so evidence semantics,
  role language, source/package behavior, and support assets do not drift.
- A non-component is still real ontology; it is denied standalone package
  status on current evidence, not discarded.

## Slice03 Hand-Off

Slice03 should compose from these classifications:

- composer/adapter inputs: `CAW-09`, `CAW-10`, `CAW-11`, `CAW-12`;
- support asset inputs: `CAW-13` through `CAW-18`;
- gate/constraint inputs: `CAW-19` through `CAW-22`, plus `CAW-25`;
- non-component/deferred inputs: `CAW-23`, `CAW-24`, `CAW-26`, and standalone
  component status for `CAW-25`.

The target graph still belongs to Slice03. This artifact only states
dispositions and dependency edges.
