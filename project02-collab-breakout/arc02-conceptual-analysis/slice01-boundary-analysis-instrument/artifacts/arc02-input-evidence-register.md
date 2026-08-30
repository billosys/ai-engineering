# Arc02 Input Evidence Register

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice01-boundary-analysis-instrument
status: proposed-done
architecture-decisions: none
```

## Purpose

This register names the inputs Arc02 may cite while evaluating conceptual
boundaries. It separates Project02 control evidence from Project03
operator-accepted input and v3.2 source provenance so later slices do not
confuse inputs with gates.

Project03 material is input-only for Project02. It is an operator-accepted
input, not a control gate, and does not gate Project02 after the operator's
acceptance recorded in the Project02 plan.

## Evidence Strength Vocabulary

- Project02 control evidence: Project02 planning or close artifacts that are
  part of this project's own gate structure.
- reproduced at arc scale: independently closed or composed Project02 evidence.
- operator-accepted input: material the operator accepted as useful for Arc02
  without making it Project02 control evidence or final architecture.
- read-only provenance: source material used to preserve concepts and wording,
  not a Project02 gate.
- input-only: may be cited as method input; cannot close Project02 ledger rows
  by itself.

## Register

| Input | Evidence class | Accepted use | Limits | Keywords for verification |
|-------|----------------|--------------|--------|---------------------------|
| `../../arc01-framework-inventory/closing-report.md` | Project02 control evidence; reproduced at arc scale | Establishes that Arc01 delivered the source inventory, problem map, candidate-component inputs, and Arc02 question register. | Does not decide final Arc02 architecture. | Arc01; Composition verdict; candidate labels; non-final |
| `../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md` | Project02 control evidence; reproduced through Arc01 close | States what Arc01 established, what remains undecided, and why Arc02 must evaluate rather than accept boundaries. | Does not complete conceptual analysis. | Arc01; non-final; Project01; package/release gate |
| `../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md` | Project02 control evidence; reproduced through Arc01 close | Primary seed source for the 26 candidate labels and initial classification vocabulary. | Seed classifications are not final. | candidate-component-inputs; candidate component; support asset; adapter; constraint |
| `../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md` | Project02 control evidence; reproduced through Arc01 close | Preserves operator and Arc02 questions that boundary evaluation must answer. | Questions are not decisions. | Arc02; Operator; Decision needed; Source evidence |
| `../../../project03-concept-card-method/arc01-method-positioning/slice01-project02-boundary-aid/artifacts/project02-conceptual-boundary-aid.md` | Project03 operator-accepted input; input-only | Supplies the boundary aid: reason to load, problem ownership, competency questions, relationship type, evidence grade, and memory admission. | Project03 is not a control gate and does not gate Project02; the aid does not decide Project02 architecture. | Project03; operator-accepted input; input-only; not a control gate; does not gate Project02; boundary aid |
| `../../../project03-concept-card-method/arc01-method-positioning/slice02-project02-acceptance-handoff/artifacts/project02-arc02-acceptance-handoff.md` | Project03 operator-accepted input; input-only | Records the acceptance handoff that allows Project02 Arc02 to consume Project03 outputs without waiting for the full v4.0 concept-card method. | The acceptance handoff does not close Project02 rows by itself and does not decide final component boundaries. | Project03; operator-accepted input; input-only; not a control gate; does not gate Project02; acceptance handoff |
| `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md` | read-only provenance; v3.2 source baseline | Preserves original concept-card ideas: one concept, source-faithful extraction, explicit relationship fields, confidence, provenance, and competency questions. | Workbench doc is not Project02 control evidence and should not override Project02 plans or ledgers. | v3.2 source baseline; 0009-howto; concept-card; one concept; provenance |
| `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md` | read-only provenance; v3.2 source baseline | Preserves re-extraction and preservation ideas: existing inventory audit, preservation checks, no dropped prior value, and validation after parallel work. | Workbench doc is not Project02 control evidence and should not authorize source edits or Project03 closure. | v3.2 source baseline; 0010-a-guide; concept-card; preservation; acceptance handoff |

## Control Boundary

Arc02 may cite Project03's boundary aid and acceptance handoff because the
operator accepted them as inputs. Project03 remains Project03. Project02 must
not close, verify, or update Project03 controls during this slice.

The v3.2 workbench docs are read-only provenance for the Project03 lens. They
preserve source method ideas, but they are not Project02 control gates, not
release gates, and not implementation authorization.

## Project01 Gate Carry-Forward

Project01 and `project01-harmonise-paths` enter this register through Arc01
close and the candidate-component inputs as cross-cutting constraints:

- source/package vocabulary must remain visible.
- package-local links must remain valid.
- generated zip roots and package entrypoints must remain coherent.
- release surface guidance must distinguish source clone, skill zip, unzipped
  install, and CCDP package workflows.
- `make check-package-paths` remains the package/release gate for future
  implementation.

These Project01 constraints are package/release gate inputs for future
component contracts. They do not make `path-contract-constraints` a user-facing
component by default.

## Non-Final Use

This register is analytical and non-final. It does not decide final
architecture, does not accept component boundaries, and does not replace
operator acceptance. It exists so Slice02 and Slice03 can make evidence use
explicit before Arc04 architecture work.
