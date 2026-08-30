# Arc04 Architecture Inputs

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice04-functional-synthesis
status: proposed-done
input-status: analytical, non-final, not accepted architecture
architecture-decisions: none
```

## Input Contract

These Arc04-ready architecture inputs consume verified Slice01, Slice02, and
Slice03 Arc03 evidence, including CDC verification, scenario matrix,
current-workflow baseline, load-path friction, functional-deficiency,
source/package role-language notes, minimum-load findings, and
dependency-adapter findings. They also consume the closed Arc02 conceptual
model, boundary and naming findings, Arc04 operator decision register, and
closing report.

This artifact produces component-fit signals and operator question inputs. It
does not decide final architecture, accepted component names, source moves,
package paths, or operator acceptance.

## Component-Fit Signals

The direct-load vocabulary for Arc04 is: strong direct load, plausible direct
load, and weak direct load. These are functional classifications, not accepted
package boundaries.

| Candidate or concept | Classification | Component-fit signal | Go / adjust / defer |
|----------------------|----------------|----------------------|---------------------|
| Top-level collaboration-framework composer | Adapter / composer | Needed for discovery, human orientation, session start, skill loading, and combination workflow routing. Current shape is too rich. | adjust |
| Collaborative posture and ethics | Plausible direct load / dependency | Strong posture value and likely prerequisite to methodology; final package placement is still an operator decision. | go / adjust |
| Engineering methodology and process | Plausible direct load / router | Owns craft substrate, SDLC posture, anti-degradation, and routes to specialized components. Must not absorb all details. | adjust |
| Ledger-verification protocol | Strong direct load | Clear standalone trigger, low context cost, and necessary ownership of evidence semantics. | go |
| Project-management family | Plausible to strong family load | Real planning and close workflow, but current PM guide boundaries are not proven as separate top-level components. | adjust |
| Code-audit discipline | Strong direct load | Clear diagnosis-only workflow; needs updated output-location and role-language adapter treatment. | go / adjust |
| Coverage-hardening discipline | Plausible direct load | Real workflow; current naming and examples are underfit for general use. | adjust |
| Delegation policy | Strong direct load | Narrow trigger and coherent rule set. | go |
| Contribution guidance | Strong direct load plus support asset | Strong with `CONTRIBUTION-TICKET.md` as support asset. Weak if separated from the template or style discipline. | go |
| Agent adapter | Adapter | Required for standalone components, but not proven as a standalone user workflow. | adjust / defer |
| Verification-methodology | Dependency edge / shared ontology | Useful concept; no direct load moment proven. | defer component |
| Path-contract constraints | Constraint / package/release gate | Project01 source/package behavior is mandatory but not a user-facing component. | go as gate |
| Ontology critique | Unresolved method question | Functional demand is plausible but not proven by current Arc03 scenarios. | defer |
| Component-maintenance discipline | Constraint / contract field set | Necessary to prevent drift after breakout; not proven as standalone component. | go as contract requirement, defer component |

## Dependency Edges

Arc04 should model these dependency edge relationships explicitly:

- Posture precedes methodology.
- Methodology routes to PM, ledger, audit, coverage, delegation, and
  contribution.
- PM close mechanics use ledger-verification protocol; ledger owns evidence
  semantics, while PM owns lifecycle, artifact inventory, bubble-up, and
  remediation-not-iteration guidance.
- Code audit uses domain skills and ledger-grade evidence language but remains
  diagnosis-only.
- Coverage hardening uses repository tooling and domain test idioms.
- Contribution guidance owns and ships the contribution ticket template as a
  support asset.
- All accepted components depend on source/package, package-local link, zip
  root, release surface, CCDP separation, and `make check-package-paths`
  package/release gate constraints.

## Support Assets

Support assets should travel with their owning component rather than becoming
separate top-level components by default:

- `CONTRIBUTION-TICKET.md` belongs with contribution guidance.
- PM examples, PM provenance, planning anti-patterns, and planning
  confirmation protocol belong under the PM family unless Arc04 finds direct
  load demand.
- Audit output examples belong with code-audit discipline once output-home
  rules are corrected.
- Package/release gate references should be contract fields plus central
  release checks, not hidden prose.

## Adapter Requirements

Arc04 should include these adapters in the architecture design:

- Framework entrypoint and routing adapter: thin composer with compact
  posture/process floor and routes.
- Repository orientation and distribution adapter: source-clone, packaged
  skill, generated zip, unzipped install, and human reader guidance.
- Agent adapter: central role-language guide plus short local notes wherever
  CDC, CC, Codex, Claude, or human/operator language affects direct use.
- PM wayfinder: routes project, arc, slice, close, and ledger workflows inside
  the PM family.

## Constraints And Package/Release Gates

Every accepted component contract should include:

- source path and package path;
- source/package mode behavior;
- package-local links and support assets;
- generated zip root expectations;
- README and `SKILL.md` release surface updates;
- component dependency edges and adapter notes;
- version-history responsibility for versioned documents;
- CCDP separation where protocol distribution is nearby but not the same
  package;
- required validation such as `make check-package-paths` and any component
  package/release gate.

## Operator Questions

Arc04 should ask or decide the following before implementation planning:

| ID | Operator question | Default posture |
|----|-------------------|-----------------|
| OQ-01 | Is posture a standalone component, a required composer summary, or both? | go / adjust / defer: go as dependency, adjust packaging. |
| OQ-02 | What does methodology own versus route to specialized components? | go / adjust / defer: adjust. |
| OQ-03 | Does PM ship as one component family with internal guides or as multiple separately loadable packages? | go / adjust / defer: adjust. |
| OQ-04 | Should audit and coverage remain sibling operational components? | go / adjust / defer: go for siblings, defer broad wrapper. |
| OQ-05 | Should coverage be renamed or wrapped to avoid Claude/Cargo underfit? | go / adjust / defer: adjust. |
| OQ-06 | Is the agent adapter central-only, local-only, or central plus local notes? | go / adjust / defer: go with central plus local notes. |
| OQ-07 | Which component contract fields are mandatory for source/package and release gates? | go / adjust / defer: go. |
| OQ-08 | Where does component-maintenance responsibility live? | go / adjust / defer: go for contract fields, defer component status. |
| OQ-09 | Does ontology critique become a reusable component or remain Project02/Project03 method evidence? | go / adjust / defer: defer component. |

## Architecture Handoff Verdict

Arc04 can proceed after Slice04 CDC verification and formal Arc03 close. The
recommended posture is go for architecture work, adjust for composer,
methodology, PM, audit, coverage, and adapter details, and defer standalone
component status for weak direct-load concepts.

This is an Arc04-ready input set, not accepted architecture.
