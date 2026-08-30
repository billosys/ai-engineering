# Conceptual Analysis Method

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice01-boundary-analysis-instrument
status: proposed-done
architecture-decisions: none
method-status: analytical, non-final
```

## Purpose

This method defines how Arc02 evaluates Project02 collaboration-framework
boundary candidates before any final architecture is selected. It merges the
Arc01 evidence base with the Project03 concept-card boundary lens and the v3.2
source baseline from:

- `../../arc01-framework-inventory/closing-report.md`
- `../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md`
- `../../../project03-concept-card-method/arc01-method-positioning/slice01-project02-boundary-aid/artifacts/project02-conceptual-boundary-aid.md`
- `../../../project03-concept-card-method/arc01-method-positioning/slice02-project02-acceptance-handoff/artifacts/project02-arc02-acceptance-handoff.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`

The method does not decide final architecture. It creates a disciplined way for
Slice02 to evaluate each seeded label and for Slice03 to synthesize the
ontology and operator decision set. Final component architecture belongs later,
after Arc03 functional analysis and Arc04 operator acceptance.

## Input Contract

Arc01 supplies the Project02 evidence and candidate labels. Project03 supplies
an operator-accepted input lens, not a Project02 control gate. The v3.2 source
baseline supplies the original concept-card method ideas behind the Project03
lens.

Use these inputs this way:

- Arc01 close report: proof that the evidence base is closed/composed and that
  candidate labels are non-final.
- Arc01 `candidate-component-inputs.md`: seed classification and source/problem
  evidence for every candidate label.
- Arc01 question register: operator and Arc02 questions that must stay visible
  while boundaries are evaluated.
- Project03 boundary aid: concept-card-inspired boundary heuristics, including
  reason to load, problem ownership, competency questions, relationship type,
  evidence grade, and memory admission.
- Project03 acceptance handoff: accepted-use limits for Project03 material;
  it is input-only and does not gate Project02.
- `0009-howto` v3.2 source baseline: one concept per card, source-faithful
  extraction, explicit relationship fields, confidence, provenance, and
  competency-question coverage.
- `0010-a-guide` v3.2 source baseline: preservation during re-extraction,
  no dropped prior value, parallel work verification, and post-extraction
  checks.

## Classification Vocabulary

Arc02 must classify each label using this classification vocabulary. A label
may have a primary classification and secondary relationships, but the final
classification remains analytical and non-final until later operator
acceptance.

- concept: an atomic idea worth understanding and naming.
- candidate component: a plausible standalone or composed package/load unit
  with its own contract, reason to load, problem ownership, competency
  questions, dependency edges, and package behavior.
- component family member: a subpart of a larger component whose standalone
  usefulness is plausible but not yet proved.
- support asset: an example, version history, template, provenance note, or
  explanatory artifact that should travel with the owner of the rule it
  supports.
- adapter: an entrypoint or surface translator, such as README orientation,
  runtime `SKILL.md` routing, Claude/Codex terminology, or source/package
  guidance.
- dependency edge: a required relation between concepts or components.
- constraint: a rule that governs accepted boundaries but is not itself a
  user-facing load target.
- template: a reusable output shape that may be an asset of a component rather
  than a component by itself.
- package/release gate: a validation rule or release-surface check, such as
  Project01 source/package constraints and `make check-package-paths`.
- non-component concept: a concept that should be represented in the ontology
  but should not be packaged or loaded as a standalone component.

## Required Boundary Axes

Every Slice02 evaluation row must answer the Project03 axes explicitly:

1. reason to load: when would a user or LLM load this without the rest of the
   monolith?
2. problem ownership: which historical or functional failure mode does it own?
3. competency question set: what can a fresh session answer or do after loading
   it?
4. relationship type: how does it relate to other labels?
5. evidence grade: how strong is the evidence for this boundary?
6. memory admission: is it ready to enter durable framework memory as a
   component, or is it still an analysis claim?

### Reason To Load

A candidate component needs a distinct reason to load. A label that is useful
only because another component needs it is probably a support asset, dependency
edge, constraint, or component family member.

Questions:

- What task begins by loading this label?
- What context cost is avoided by loading it separately?
- What would be missing if a user loaded only this and not the top-level
  collaboration framework?
- Does the load moment belong to a human source reader, a model runtime skill,
  a package reader, or a maintainer?

### Problem Ownership

A candidate component should own a problem, not merely a file. Problem
ownership must point back to Arc01 problem-solution evidence.

Questions:

- Which Arc01 problem class does this label primarily address?
- Does another label already own the same problem more cleanly?
- Is the overlap deliberate reinforcement or duplication likely to drift?
- Is the label solving a real user/LLM problem, or naming a current source
  location?

### Competency Question Set

The competency question lens comes from the v3.2 concept-card method and the
Project03 boundary aid. A component should answer a cluster of questions; one
isolated question usually indicates a guide section or support asset.

Minimum row requirements:

- List 2-5 competency questions when the label is plausibly a component.
- List 1-2 competency questions when the label is likely a support asset,
  adapter, constraint, template, or non-component concept.
- Mark unanswered or weak questions as evaluation gaps rather than inventing
  strength.
- Use competency questions as coverage checks: if no row can answer a needed
  question, record a missing concept or underfit area.

### Relationship Type

Use explicit relationship type values rather than burying relationships in
prose:

- prerequisite: this must be understood or loaded first.
- extends: this specializes a more general concept or component.
- uses: this calls on another component during a workflow.
- supports: this supplies examples, template, provenance, or explanation.
- constrains: this imposes a release, path, evidence, or package rule.
- contrasts-with: this prevents improper merge or confusion.
- composes-into: this is a family member or asset within a larger component.
- routes-to: this is an adapter or wayfinder to another component.

These relationship types extend the v3.2 typed relationship idea from concept
cards into Project02 component-boundary analysis.

### Evidence Grade

Use evidence grade as information, not decoration:

- asserted: label exists as a claim but lacks cited source/problem evidence.
- attested: CC has supplied evidence in an artifact or close report.
- reproduced: CDC or an independent pass has reproduced the evidence at the
  relevant scale.
- reconciled: the claim has also been checked against broader project state.
- operator-accepted input: the operator accepted an input artifact for this
  analysis, without making it a final architecture decision.

For this slice, Arc01 close evidence is reproduced at arc scale, Project03
boundary aid and acceptance handoff are operator-accepted input, and v3.2
workbench docs are read-only provenance. The seeded component-boundary ledger
starts evaluation rows as `seeded-from-Arc01`, not as accepted component
evidence.

### Memory Admission

Memory admission asks whether a classification is ready to become durable
framework memory. This is stricter than producing a label:

- denied: no source-backed, problem-backed reason to keep it.
- analysis-only: useful as an Arc02 working handle, but not accepted substrate.
- candidate-for-memory: may enter durable memory after Slice02/03 evaluation
  and operator acceptance.
- admitted-by-operator: accepted for future Project02 architecture work.
- deferred: potentially useful but waiting on Arc03 functional analysis,
  Arc04 architecture, or Project03 v4.0 method work.

No row in this slice should be `admitted-by-operator`; this slice seeds the
instrument only.

## v3.2 Method Concepts Preserved

The v3.2 source baseline contributes method constraints that Arc02 must keep:

- one concept: keep one concept per evaluation object; split labels that hide
  multiple concepts, and merge only when evidence shows the same concept across
  contexts.
- source-faithful: classify from source evidence and Arc01 artifacts rather
  than tidy labels or current file boundaries.
- explicit relationship: record typed relationships so merges, splits, and
  dependencies are auditable.
- confidence: report uncertainty and evidence grade instead of flattening every
  row into the same strength.
- provenance: cite the artifact or source basis for each evaluation row.
- competency question: use questions as both requirements and coverage checks.
- preservation: when Arc02 revises a seed classification, preserve unique
  prior value from Arc01 and Project03 rather than silently overwriting it.

## Evaluation Workflow For Slice02

Slice02 should evaluate each row in `component-boundary-ledger.md` in a
consistent order:

1. Read the Arc01 seed evidence for the label.
2. Identify the atomic concept or concepts represented by the label.
3. Write or refine the candidate competency question set.
4. State the primary problem ownership claim.
5. Classify the label using the classification vocabulary.
6. Record relationship type edges to other labels.
7. Apply Project01 source/package and package/release gate constraints.
8. Assign evidence grade and memory admission status.
9. Record risks: mislabel, improper merge, improper split, underfit, overfit,
   overlap, duplication, or missing concept.
10. Write a provisional disposition for Slice03 synthesis.

If a label contains multiple concepts, Slice02 should mark it as an improper
merge candidate and preserve the original seed label while naming the split
proposal as analytical. If several labels name one concept through different
surfaces, Slice02 should mark them as improper split candidates and preserve
the individual evidence before proposing a merge.

## Project01 Cross-Cutting Gates

Project01 and `project01-harmonise-paths` remain cross-cutting constraints for
every boundary evaluation:

- source/package vocabulary must stay explicit.
- package-local links must remain valid after any component split.
- generated skill zip roots and entrypoints must be coherent.
- CCDP remains a separate protocol package, not an installable skill package.
- release surface guidance must distinguish source clone, skill zip, unzipped
  install, and CCDP package workflows.
- `make check-package-paths` remains a package/release gate for future source
  implementation.

These are package/release gate and cross-cutting constraint rows, not
standalone user-facing components unless Arc02 later proves a direct user load
moment.

## Non-Final Decision Posture

All classifications produced under this method are non-final. Slice02 may
propose provisional dispositions, and Slice03 may synthesize an Arc02 model,
but Arc02 does not decide final breakout architecture. Final architecture
belongs to Arc04 after Arc03 functional analysis and operator acceptance.

This method should make bad boundaries harder to accept accidentally; it should
not make accepted boundaries appear before the evidence supports them.
