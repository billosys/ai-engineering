# Architecture Input Register

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice01-architecture-decision-instrument
status: proposed-done
input-status: closed-evidence-register
architecture-decisions: none
```

## Input Contract

This register records the closed Arc02 and Arc03 evidence Arc04 will use for
architecture work. It treats the Arc02 conceptual model, boundary and naming
findings, and operator decision register as candidate-boundary evidence, not
accepted architecture. It treats the Arc03 functional model, scenario
coverage, functional fit and risk synthesis, architecture inputs, and closing
report as functional evidence, not final component acceptance.

All rows preserve these constraints:

- Project01 and `project01-harmonise-paths` source/package rules remain
  cross-cutting component contract and package/release gate requirements.
- Package-local links, zip root assumptions, release surface guidance, README
  and `SKILL.md` routing, CCDP separation, and `make check-package-paths` must
  be carried into later component contracts.
- Operator acceptance is required before architecture is accepted.
- Source files remain read-only in Arc04 until a later implementation plan.

## Closed Arc02 Inputs

| Input | Role in Arc04 | Evidence strength | Constraints carried forward |
|-------|---------------|-------------------|-----------------------------|
| `../../arc02-conceptual-analysis/closing-report.md` | Closing report proving Arc02 delivered conceptual analysis and kept final architecture deferred. | reproduced at arc scale by CDC; `Composition verdict: delivered`. | Do not reopen conceptual analysis unless Arc04 finds a decision-instrument gap. |
| `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md` | Conceptual model of candidate components, component family members, support assets, adapters, dependency edges, constraints, templates, package/release gates, and non-component concepts. | verified child artifact, reproduced through Arc02 close. | Candidate labels are evidence handles, not accepted component names or package paths. |
| `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md` | Boundary and naming findings for mislabels, improper merges, improper splits, missing concepts, overclaimed mechanisms, underfit, overfit, overlap, duplication, and maintenance concerns. | verified child artifact, reproduced through Arc02 close. | Every finding routes to Arc03, Arc04, or Arc05 and remains analytical. |
| `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md` | D-01 through D-12 operator decision register for Arc04 architecture choices. | verified child artifact, reproduced through Arc02 close. | Decisions are open until Arc04 disposition and operator acceptance. |

## Closed Arc03 Inputs

| Input | Role in Arc04 | Evidence strength | Constraints carried forward |
|-------|---------------|-------------------|-----------------------------|
| `../../arc03-functional-analysis/closing-report.md` | Closing report proving Arc03 delivered functional analysis and made Arc04 eligible. | reproduced at arc scale by CDC; `Composition verdict: delivered`. | Arc04 must consume, not redo, direct-load and composition findings. |
| `../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc03-functional-model.md` | Functional model across direct source, source-clone, packaged skill, skill loading, human orientation, session start, planning, execution, review, audit, coverage, delegation, contribution, and combination workflow surfaces. | verified child artifact, reproduced through Arc03 close. | Direct-load classifications are functional inputs, not accepted architecture. |
| `../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/scenario-coverage-synthesis.md` | Scenario coverage for S-01 through S-14, comparing current monolith, standalone, composed, and top-level composer load shapes. | verified child artifact, reproduced through Arc03 close. | Arc04 should preserve scenario IDs as evaluation checks in later slices. |
| `../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/functional-fit-and-risk-synthesis.md` | Functional fit, context cost, routing friction, deficiency, source/package, role-language, package/release, and failure-mode risk synthesis. | verified child artifact, reproduced through Arc03 close. | LPF, FD, SPR, and RLF carry-forward rows must be dispositioned in component contracts or operator decisions. |
| `../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc04-architecture-inputs.md` | Arc04-ready architecture inputs: component-fit signals, dependency edges, support assets, adapters, constraints, package/release gates, component contract implications, operator questions, and go / adjust / defer posture. | verified child artifact, reproduced through Arc03 close. | This is the primary functional input for Slice02, but it is not accepted architecture. |
| `../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc03-close-readiness.md` | Close-readiness mapping to Arc03 ledger rows A-5 through A-9. | verified child artifact, reproduced through Arc03 close. | Historical readiness evidence; Arc03 is now closed by its arc closing report. |

## Source Grounding Inputs

Arc04 may inspect source files for factual grounding, but closed Project02
evidence has higher planning weight than any old soft layout sketch.

| Source surface | Role | Constraint |
|----------------|------|------------|
| `README.md` | Human orientation, source-clone guidance, build/install commands, CCDP distinction. | Architecture must preserve source/package reader paths and release surface language. |
| `SKILL.md` | Current top-level collaboration-framework skill entrypoint and routing surface. | Architecture must keep the top-level composition usable after breakout. |
| `docs/PROJECT-MANAGEMENT.md` and `docs/pm/*.md` | Current PM wayfinder, lifecycle, artifact-home, and close mechanics. | PM family and ledger dependency cannot drift. |
| `templates/LEDGER-DISCIPLINE.md` | Evidence-grade and row-closure protocol. | Ledger evidence semantics should have one owner. |
| `docs/CODE-AUDIT.md` | Diagnosis-only audit workflow and current output conventions. | Workbench output language needs adjustment against slice `artifacts/` convention. |
| `docs/CLAUDE-CODE-COVERAGE.md` | Coverage-hardening workflow and current tool-shaped examples. | Coverage naming/examples need generalization or adapter treatment. |
| `docs/SUBAGENT-DELEGATION-POLICY.md` | Delegation policy and Codex/Claude role-language surface. | Role-language adapter notes must survive standalone loading. |
| `docs/CONTRIBUTION-STYLE.md` and `templates/CONTRIBUTION-TICKET.md` | Contribution guide and template support asset. | Template travels with contribution guidance. |
| `Makefile` | Package lists, generated skill zip behavior, CCDP package behavior, and validation targets. | Component contracts must name package/release gates and validation commands. |

## Use Rules For Later Arc04 Slices

- Slice02 should evaluate candidate contracts against this input register,
  not against memory or the soft layout sketch alone.
- Slice03 should compose only candidates whose Slice02 contracts have a
  final go / adjust / defer disposition.
- Slice04 should present accepted architecture for operator acceptance and
  preserve any deferred rows for Arc05 or later projects.
- Any source/package or operator-acceptance constraint that cannot be met must
  be disclosed as a risk or deferral, not silently dropped.
