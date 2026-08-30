# Component Dependency And Adapter Findings

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice03-standalone-composition-evaluation
status: proposed-done
architecture-decisions: none
findings-status: analytical, non-final, not accepted architecture
```

## Input Contract

These findings consume the Slice01 functional-analysis method and scenario
matrix, the Slice02 current-workflow evaluation, load-path friction,
functional-deficiency, and source/package role-language baseline, and the Arc02
conceptual model, boundary and naming findings, and operator decision register.
They preserve Project01 and `project01-harmonise-paths` as source/package,
package-local, zip root, release surface, `make check-package-paths`, and
package/release gate constraints for future component contracts.

## Findings

| ID | Finding area | Finding | Evidence basis | Downstream implication |
|----|--------------|---------|----------------|------------------------|
| CDA-01 | dependency direction | Ledger-verification should own evidence strength, row closure, deferral/no-op semantics, and silent-drop prevention. Project-management should depend on ledger for close evidence rather than duplicate those semantics. | Arc02 BNF-06 and D-04; Slice02 LPF-04 and FD-07; S-12. | Arc04 should encode ledger -> PM close dependency direction; Arc05 should verify package-local links from PM close docs to the ledger component. |
| CDA-02 | project-management component-family / PM family behavior | PM has a real direct load moment, but current evidence supports one project-management component family with a wayfinder and internal focused guides, not every split file as a top-level package. | Arc02 BNF-08 and BNF-15; Slice02 LPF-03 and FD-09; S-12. | Arc04 should choose PM package granularity explicitly. Slice04 should carry "family, not file boundary" as a functional result. |
| CDA-03 | support-asset travel | Support assets must travel with the component that owns the workflow they support. PM examples/provenance travel with PM; audit output examples travel with audit; contribution-ticket-template travels with contribution guidance. | Arc02 support asset model; Slice02 LPF-05, LPF-06, FD-06. | Arc04 component contracts need a support assets field. Arc05 package lists must stage support assets with their owning component. |
| CDA-04 | contribution-ticket-template ownership | `templates/CONTRIBUTION-TICKET.md` is not a standalone component on current evidence. It is a support asset owned by `contribution-style-and-voice` / contribution-guidance. | S-10; Arc02 BNF-07 and D-09; Slice02 LPF-05 and FD-06; source template says to read `docs/CONTRIBUTION-STYLE.md` first. | Package the template with contribution guidance and verify package-local template links. |
| CDA-05 | role-language clarity | Role-language clarity is acceptable in composed mode, but standalone components need local adapter notes when they mention CDC, CC, Claude, Codex, verifier, reviewer, or operator. | Slice02 LPF-09, FD-11, RLF-01 through RLF-08; S-14. | Arc04 should choose central adapter plus short local notes unless operator chooses a different drift-control pattern. |
| CDA-06 | agent-adapter behavior | Agent-adapter behavior is required, but it behaves like adapter infrastructure more than an independently loaded user workflow. It should mediate standalone use without becoming another hidden prerequisite. | Arc02 BNF-02 and D-06; Slice02 RLF-08; S-14. | Arc04 should decide adapter ownership and minimum local note content; Arc05 should check old Claude-era references during packaging. |
| CDA-07 | source/package constraints | Project01 source/package vocabulary is a cross-cutting constraint, not a user-facing component. Every component contract should distinguish source clone, generated skill zip, unzipped install, planning worktree, and CCDP package where relevant. | Slice02 SPR-01, SPR-05, SPR-07; Arc02 BNF-05, BNF-14, D-11. | Arc04 should require source/package fields in every accepted component contract. Arc05 should update README and package docs without creating a second composer. |
| CDA-08 | package-local link behavior | Package-local links currently work because `CF_FILES` stages an explicit set of framework files. Breakout will multiply this maintenance point. | Slice02 SPR-02 and SPR-06; source Makefile `CF_FILES`; Project01 package-path gates. | Arc04 should make package-local link behavior part of component contracts. Arc05 should run `make check-package-paths` after package list or Markdown link changes. |
| CDA-09 | zip root behavior | Zip root behavior is clear for the current `collaboration-framework.zip` and separate `ccdp.zip`; future components need named roots and entrypoints. | Slice02 SPR-03 and SPR-05; README build/package guidance; Project01 gate language. | Arc04 should specify zip root behavior for each component. Arc05 should verify generated zips and unzipped package readers. |
| CDA-10 | release surface behavior | README, SKILL routing, Make targets, package docs, and package-path exceptions currently compose into one release surface. Breakout can drift unless each component has a release-surface contract. | Slice02 SPR-04, SPR-06, FD-10; Arc02 D-10 and D-11. | Arc05 implementation planning should include README, SKILL.md, Makefile, package exceptions, package docs, and validation gates in one slice or explicitly sequenced slices. |
| CDA-11 | make check-package-paths | `make check-package-paths` remains the current hard package/release gate for Markdown links inside generated skill zips. It should remain central, with per-component expected inputs. | Slice02 SPR-06; Project01 carried constraints; prompt-required source/package checks. | Arc04 should name the gate in contract form; Arc05 should run it after every packaged Markdown link, bundle, or exception change. |
| CDA-12 | package/release gate implications | Package/release gates are constraints that compose with every accepted component. They are not cleanup tasks to defer after source moves. | Arc02 package/release gates; Slice02 FD-10; S-13. | Slice04 should carry this as a serious functional input. Arc04 should decide the contract shape before Arc05 plans implementation. |

## Adapter And Dependency Conclusions

- The clearest dependency direction is posture -> methodology -> routed
  operational components; ledger-verification -> PM close evidence; style ->
  contribution-ticket-template; repository tooling -> coverage command
  adaptation; domain skills -> code-audit language findings.
- The strongest adapter pattern is a thin framework-entrypoint plus an
  agent-adapter, with short local component notes where standalone loading
  otherwise loses role-language clarity.
- Source/package and Project01 rules should stay constraints and
  package/release gates. Promoting them into a standalone component would hide
  their cross-cutting role.
- Support-asset travel is a contract requirement: every accepted component
  needs an owned support assets list and package-local link expectations.

These findings do not accept final architecture. They are Arc03 functional
decision inputs for Slice04 and Arc04.
