# Candidate Architecture Worklist

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice01-architecture-decision-instrument
status: proposed-done
worklist-status: seeded-for-slice02
architecture-decisions: none
```

## Input Contract

This candidate architecture worklist seeds later Arc04 evaluation from the
closed Arc02 conceptual model and closed Arc03 functional model, scenario
coverage, functional fit synthesis, and architecture inputs. It preserves the
non-final status of all candidates.

Slice02 must evaluate these rows with the component-contract schema before
Slice03 composes a target architecture.

## Candidate Components And Families

| ID | Candidate | Initial category | Evidence signal | Go / adjust / defer | Slice02 work |
|----|-----------|------------------|-----------------|---------------------|--------------|
| CAW-01 | `collaborative-posture-and-ethics` | candidate component / dependency edge | Arc02 names posture as a strong candidate; Arc03 finds plausible direct-load value and prerequisite force for methodology. | go / adjust | Decide standalone component, composer summary, or both; fill dependency and operator acceptance fields. |
| CAW-02 | `engineering-methodology-and-process` | candidate component / router | Arc02 says methodology owns substrate/process but over-merges specialized operations; Arc03 says plausible direct load with routing responsibility. | adjust | Define what methodology owns versus routes to; prevent monolith recreation. |
| CAW-03 | `ledger-verification-protocol` | candidate component | Strong direct load, clear owned problem, low context cost, and dependency edge into PM close mechanics. | go | Fill contract and dependency fields; preserve evidence-grade ownership. |
| CAW-04 | `project-management` | component family | Arc02 and Arc03 both find PM has real load demand but current files are not each proven as standalone components. | adjust | Decide one PM component family, wayfinder strategy, and internal guide treatment. |
| CAW-05 | `code-audit-discipline` | candidate component | Strong direct load and diagnosis-only workflow; output-home and role-language updates required. | go / adjust | Contract audit as diagnosis-only; fix workbench versus slice `artifacts/` output convention. |
| CAW-06 | `coverage-hardening-discipline` | candidate component | Real coverage workflow but current title/examples are Claude/Cargo-shaped and underfit general framework use. | adjust | Decide surface-neutral name or adapter; preserve repository-specific command adaptation. |
| CAW-07 | `delegation-policy` | candidate component | Strong direct load, narrow trigger, low context cost, and clear rule set. | go | Fill contract with role-language and standing-instruction adapter notes. |
| CAW-08 | `contribution-style-and-voice` | candidate component with support asset | Strong direct load when paired with `CONTRIBUTION-TICKET.md`; weaker if split. | go | Contract guide plus template support asset and package-local link behavior. |

## Composer And Adapter Worklist

| ID | Candidate | Initial category | Evidence signal | Go / adjust / defer | Slice02 work |
|----|-----------|------------------|-----------------|---------------------|--------------|
| CAW-09 | top-level composer / `framework-entrypoint-and-routing` | top-level composer / adapter | Needed for discovery, human orientation, session start, skill loading, and combination workflow routing; current monolith is over-rich. | adjust | Define thin composer contract and compact posture/process floor. |
| CAW-10 | agent adapter / `agent-adapter-and-routing` | adapter | Required for standalone role-language clarity, but not proven as standalone component. | adjust / defer | Decide central adapter plus local notes, local-only, or central-only; guard drift. |
| CAW-11 | `repository-orientation-and-distribution` | adapter / constraint | Source-clone, generated skill zip, unzipped install, and human reader paths need explicit routing. | adjust | Define README/package reader behavior and package-local entrypoint implications. |
| CAW-12 | `project-management-wayfinder` | PM family wayfinder / adapter | Routes project, arc, slice, close, and ledger workflows inside PM. | adjust | Keep inside PM family unless direct-load evidence changes. |

## Support Assets

| ID | Asset | Owning candidate | Initial category | Slice02 work |
|----|-------|------------------|------------------|--------------|
| CAW-13 | `CONTRIBUTION-TICKET.md` | contribution guidance | support asset / template | Ensure template travels with contribution guidance and package-local links resolve. |
| CAW-14 | PM examples | project-management family | support asset | Keep as PM support unless direct-load evidence appears. |
| CAW-15 | PM provenance and version history notes | project-management family | support asset / maintenance evidence | Preserve rationale and version history responsibility. |
| CAW-16 | planning anti-patterns and repair guidance | project-management family | support asset | Keep corrective guidance discoverable through PM wayfinder. |
| CAW-17 | audit output examples | code-audit discipline | support asset | Update output-home convention if audit is accepted. |
| CAW-18 | protocol distribution guidance | repository orientation or release gate | support asset / constraint | Preserve CCDP separation from installable skill packages. |

## Constraints, Package/Release Gates, And Non-Components

| ID | Item | Initial category | Evidence signal | Go / adjust / defer | Slice02 work |
|----|------|------------------|-----------------|---------------------|--------------|
| CAW-19 | Project01 path-contract constraints | constraint / package/release gate | Project01 and Arc02/Arc03 all require source/package, package-local, zip root, release surface, and `make check-package-paths` behavior. | go as gate | Convert into component contract fields and validation gates. |
| CAW-20 | source/package reader modes | constraint / adapter | Source clone, generated skill zip, unzipped installed skill, and CCDP package are distinct. | go as contract requirement | Require each accepted component to state mode behavior. |
| CAW-21 | release surface synchronization | package/release gate | README, `SKILL.md`, Makefile lists, package exceptions, and generated zip behavior can drift. | go as gate | Require package/release gate checks in every accepted contract. |
| CAW-22 | CCDP separation | constraint / package/release gate | CCDP is a protocol distribution, not an installable skill component. | go as gate | Prevent framework skill breakout from merging protocol package semantics. |
| CAW-23 | verification-methodology | dependency edge / non-component | Shared ontology across methodology, ledger, PM close, audit, and coverage; no direct load proven. | defer component | Assign owner or citation edge rather than standalone package. |
| CAW-24 | ontology critique | deferred / non-component | Arc02 names it as missing concept; Arc03 does not prove a direct load moment. | defer | Decide Project02-only method, Project03 route, or future component. |
| CAW-25 | component-maintenance discipline | constraint / deferred component | Needed to prevent drift, but not proven as direct standalone workflow. | go as contract requirement, defer component | Add maintenance owner and version-history responsibility fields. |
| CAW-26 | evidence strength and memory admission vocabulary | non-component / dependency edge | Conceptual glue owned by ledger/methodology relationship. | defer component | Prevent duplicated standalone package; assign ownership. |

## Slice02 Evaluation Order

Recommended order for Slice02:

1. Evaluate package/release gates first: CAW-19 through CAW-22.
2. Evaluate composer and adapter rows: CAW-09 through CAW-12.
3. Evaluate core posture, methodology, ledger, and PM family: CAW-01 through
   CAW-04.
4. Evaluate operational components: CAW-05 through CAW-08.
5. Evaluate support assets and deferred/non-component concepts: CAW-13
   through CAW-18 and CAW-23 through CAW-26.

This ordering makes component contracts inherit source/package gates before
package paths or names are proposed.
