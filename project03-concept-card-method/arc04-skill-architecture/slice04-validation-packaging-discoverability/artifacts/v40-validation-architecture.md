# v4.0 Validation Architecture

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice04-validation-packaging-discoverability
status: proposed-done
mode: validation architecture
```

## Purpose

This artifact defines the v4.0 concept-card method validation architecture.
It classifies each validation candidate by the strongest suitable verification
mode without collapsing Arc03's evidence lifecycle constructs.

Validation result is distinct from verification result, verification state,
evidence grade, extraction confidence, reconciliation result, reconciliation
state, preservation decision, and memory admission. A validation result records
whether a construct satisfies structural method expectations. It is not
semantic verification, not operator acceptance, and not one confidence field.

## Validation Classes

| Class | Owns | Does not own |
|-------|------|--------------|
| deterministic structural | Machine-checkable presence, reference, and shape checks over artifacts. | Judging whether source support actually warrants a claim. |
| semantic audit | Human or reviewer assessment of meaning, warrant, and interpretive adequacy. | Pretending subjective warrant can be proven by string shape alone. |
| human/operator review | Explicit operator review for memory admission, conflict decisions, and method exceptions. | Automated approval of durable-memory admission. |
| deferred runtime | Checks that require a future graph, retrieval, memory, CCDP, or live extraction runtime. | First-release planning-document closure. |

## Deterministic Structural Candidates

The following validation candidate set is deterministic enough for Arc05 to
plan as future validator-code or deterministic validation scripts, without
choosing exact schema syntax or CLI/API behavior here:

- Required fields and required sections are present for concept cards, claims,
  CQs, edges, extraction runs, and result records.
- Provenance is present for concept cards and extraction runs.
- Source support is present when a claim, relationship edge, or CQ coverage
  assertion requires a source span attachment.
- Relationship reference checks ensure edge endpoints resolve to existing
  concept cards or claims.
- CQ coverage checks ensure each covered card, claim, edge, or source support
  target has an explicit reference.
- Graph closure checks verify that local edge references are internally
  complete inside the artifact set available to the validator.
- Preservation decision records contain a prior-card disposition and rationale
  reference.
- Memory admission records contain admission state and the required lifecycle
  inputs: source support, evidence grade, verification state, validation
  result, reconciliation state, preservation disposition, and operator review
  when required.

These checks are structural. Passing them does not prove truth, source warrant,
or durable-memory suitability.

## Semantic Audit Candidates

Semantic audit remains required for questions where shape is insufficient:

- Whether source support actually supports the claim, edge, or CQ coverage
  assertion.
- Whether evidence grade is appropriate for the source and claim.
- Whether extraction confidence is well calibrated to the extractor's limits.
- Whether relationship vocabulary, direction, and symmetry are meaningful.
- Whether CQ coverage is sufficient to answer the competency question.
- Whether reconciliation result and reconciliation state reflect the real
  conflict and lifecycle effect.
- Whether a preservation decision keeps useful prior-card value without
  preserving stale material.

Semantic audit produces reviewer evidence; it does not replace deterministic
structural validation.

## Human/Operator Review Candidates

Human/operator review is required when the method needs accountable judgment:

- Operator review of memory admission when the construct becomes durable
  working memory.
- Operator acceptance of unresolved preservation decisions.
- Operator approval for exceptions to the thin SKILL.md load contract, the
  guide architecture, or the release-critical example set.
- Operator confirmation where semantic audit leaves material uncertainty.

The validation architecture treats these as explicit workflow gates rather
than hidden prose notes.

## Deferred Runtime Checks

Deferred runtime checks are out of scope for Slice04 and Arc04 first-release
planning unless a later owner explicitly adds a runtime project:

- Full graph closure over a graph database or ontology database.
- GraphRAG retrieval probes against live indexes.
- Memory runtime enforcement of memory admission.
- CCDP service orchestration.
- Live extraction over changing source corpora.

## Preservation of Prior Decisions

This artifact preserves the Slice02 load contract and thin SKILL.md routing
posture. It also preserves Slice03 guide architecture, template architecture,
and example architecture outputs: user-authored surfaces remain separate from
trace record and result record surfaces; release-critical examples remain a
first-release target; the five-agent workflow remains a default recipe, not an
invariant; and every actual extraction run records parallel-worker provenance.

## Later Owner Routing

| Later owner | Routed question |
|-------------|-----------------|
| Slice05 | architecture synthesis, final cross-artifact validation policy, unresolved-decision register, and Arc05 handoff wording. |
| Arc05 | source edit planning, exact file layout, exact schema syntax, exact enum spelling, validator-code design, Makefile changes, README edits, generated zips, tests, release mechanics, and package updates. |

## Out of Scope

Out of scope for this artifact: source SKILL.md edits, source checkout edits,
source edit mechanics, validator-code implementation, deterministic validation
scripts, exact CLI/API behavior, graph database design, GraphRAG runtime,
memory runtime, CCDP service behavior, live extraction, package release, and
generated zips.
