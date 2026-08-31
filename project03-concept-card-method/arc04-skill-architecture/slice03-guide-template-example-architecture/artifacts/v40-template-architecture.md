# v4.0 Template Architecture

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice03-guide-template-example-architecture
status: proposed-done
mode: template architecture
```

## Purpose

This artifact defines the template architecture for the first v4.0
concept-card method skill. It distinguishes user-authored surfaces from trace
record and result record surfaces while preserving Arc03's no-flattening rule.

The template architecture preserves positive load and negative load boundaries
from Slice02: templates are for concept-card method output, not for every
research, project-management, source-reading, implementation planning, or
memory interaction.

## Surface Classes

| Surface class | Purpose | Operator posture |
|---------------|---------|------------------|
| user-authored | Human- or model-authored method artifacts that users directly curate. | Keep concise and reviewable. |
| trace record | Provenance-bearing records of extraction, re-extraction, source snapshot, prompt/method version, agent scope, and parallel-worker provenance. | Preserve what happened without turning it into narrative summary. |
| result record | Auditable validation result, verification result, reconciliation result, preservation decision, and memory admission outcomes. | State checked construct, evidence used, decision, rationale, lifecycle effect, and downstream implication. |

## Template Surface Decisions

| Template surface | Surface class | Required method coverage |
|------------------|---------------|--------------------------|
| Concept card template | user-authored | concept card boundary, one concept per card, summary prose, provenance, relationships, competency question references, and memory admission state when card-level admission is used. |
| Claim/source support template | user-authored and result record attachment | claim text, source span locator, source support attachment, evidence grade, extraction confidence, verification state, validation result, reconciliation state, and memory admission where claim-level granularity matters. |
| Competency question/CQ template | user-authored | competency question text, CQ role, answerability, coverage target, covered cards/claims/edges, verification target, retrieval probe, obsolete status, and deferred status. |
| Relationship/edge template | user-authored and result record attachment | relationship vocabulary, edge endpoints, direction or symmetry expectation, source support, evidence grade, extraction run, verification state, reconciliation state, graph closure state, and memory admission implication. |
| Extraction run template | trace record | source snapshot, method or prompt version, agent scope, generated or updated concept cards, claims, edges, CQs, old-card inputs, preservation decisions, validation result, reconciliation result, verification result, and parallel-worker provenance. |
| Validation result template | result record | structural checks for required fields, body sections, provenance, source support, relationship references, CQ coverage, path/slug hygiene, and consistency. |
| Verification result template | result record | verifier role, checked construct, evidence used, verification state, outcome, uncertainty, and source support reviewed. |
| Reconciliation result template | result record | conflict class, affected cards/claims/edges/CQs/runs, source support, decision, rationale, lifecycle effect, reconciler or verifier role, and memory admission implication. |
| Preservation decision template | result record | prior-card value, preserved/superseded/rejected/unresolved disposition, rationale, source support, reconciliation state, and downstream effect. |
| Memory admission template | result record | admission state, admitted construct, source support, evidence grade, verification state, validation result, reconciliation state, preservation disposition, and operator acceptance when required. |

## Distinction Rules

- A concept card remains the visible user-authored unit, but a claim carries
  finer-grained source support, evidence grade, extraction confidence,
  verification state, reconciliation state, validation result, and memory
  admission when needed.
- Source support is distinct from general provenance and should be represented
  as a relationship between a claim, edge, or CQ coverage assertion and a
  source span.
- Extraction confidence is not evidence grade, not verification state, not
  validation result, not reconciliation state, and not memory admission.
- Verification result, validation result, reconciliation result, preservation
  decision, and memory admission are result record surfaces, not prose notes
  buried in the card body.
- The five-agent workflow remains a default recipe, not an invariant. The
  extraction run template records actual agent scope and parallel-worker
  provenance regardless of worker count.

## Later Owner Routing

| Later owner | Routed question |
|-------------|-----------------|
| Slice04 | validation determinism, validation candidate selection, package behavior, package inclusion, README integration, discoverability, and maintenance ownership for templates. |
| Slice05 | Architecture synthesis and the final cross-surface decision register. |
| Arc05 | implementation planning for source edit work, exact file layout, schema syntax, enum spelling, Makefile changes, README changes, validator-code, generated zips, release mechanics, tests, and package updates. |

## Out of Scope

Out of scope for this slice: validation candidate selection, package
inclusion, README integration, Makefile changes, validator-code, deterministic
validation scripts, generated zips, released skill bundles, released skill
mechanics, source checkout edits, schema syntax, enum spelling, graph database
design, memory runtime design, CCDP service design, live extraction behavior,
runtime services, exact field spelling, and source implementation.
