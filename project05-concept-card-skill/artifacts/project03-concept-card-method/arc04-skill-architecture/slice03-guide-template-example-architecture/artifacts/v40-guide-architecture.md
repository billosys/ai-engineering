# v4.0 Guide Architecture

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice03-guide-template-example-architecture
status: proposed-done
mode: guide architecture
```

## Purpose

This artifact defines the guide architecture for the first v4.0 concept-card
method skill. It decides guide surfaces by method concern while preserving the
Slice02 load contract, the thin `SKILL.md` entrypoint, and Arc03's conceptual
distinctions.

The future `SKILL.md` remains a thin entrypoint: it should state the reason to
load, preserve positive load and negative load triggers, define problem
ownership, and route the operator to focused guides. It should not embed the
full method.

## Guide Surface Decisions

| Guide surface | Owns | Does not own |
|---------------|------|--------------|
| Load and routing guide | The reason to load, positive load triggers, negative load triggers, problem ownership, dependency direction, adjacent guidance, and operator workflow entry boundary. | Final package behavior, README integration, source edit mechanics, and implementation planning. |
| Extraction guide | Source snapshot selection, source-faithful concept card extraction, claim identification, source support capture, extraction confidence, and extraction run provenance. | Runtime live extraction, graph database design, validator-code, or exact schema syntax. |
| Re-extraction and preservation guide | Re-extraction against old cards, preservation decision handling, superseded/rejected/unresolved prior-card value, and parallel-worker provenance. | A fixed worker count or a mandatory five-agent workflow. |
| Evidence lifecycle guide | The distinct lifecycle concerns: source span, source support, evidence grade, extraction confidence, verification state, validation result, reconciliation state, and memory admission. | Exact enum spelling, validation determinism, or deterministic validation script implementation. |
| Graph and CQ guide | Relationship vocabulary, graph-native edge identity when evidence or lifecycle state attaches, competency question and CQ coverage, answerability, retrieval-probe use, obsolete status, and deferred CQ handling. | Graph database design, graph indexes, or memory runtime behavior. |
| Reconciliation guide | Duplicate concepts, competing definitions, slug drift, taxonomy drift, relationship asymmetry, CQ coverage conflict, parallel-worker conflict, preservation conflict, and reconciliation result records. | Reconciliation algorithms or runtime services. |
| Validation and verification guide | Structural validation result versus semantic verification result/state, verifier role, evidence used, checked construct, and outcome recording. | Validator-code, final validation candidate selection, and implementation test gates. |
| Memory admission guide | Memory admission as a lifecycle gate distinct from validation and verification, with source support, evidence grade, verification state, validation result, reconciliation state, preservation disposition, and operator acceptance inputs. | Memory runtime design, GraphRAG runtime, or CCDP service design. |

## Cross-Guide Routing

- The load and routing guide routes work into the specific concern guides
  rather than expanding `SKILL.md`.
- The extraction and re-extraction guides route lifecycle evidence to the
  evidence lifecycle guide.
- The graph and CQ guide routes evidence-bearing relationships to the evidence
  lifecycle and reconciliation guides when source support, verification, or
  reconciliation attaches to an edge.
- The validation and verification guide routes durable-memory eligibility to
  the memory admission guide.
- All guides preserve the Slice02 decision that the five-agent workflow is a
  default recipe, not an invariant; every actual run needs extraction-run and
  parallel-worker provenance.

## Later Owner Routing

| Later owner | Routed question |
|-------------|-----------------|
| Slice04 | validation determinism, validation candidate selection, package behavior, package inclusion, README integration, discoverability, and maintenance ownership. |
| Slice05 | Architecture synthesis across the load contract, guide architecture, template architecture, example architecture, and validation/package decisions. |
| Arc05 | implementation planning for source edit work, exact source layout, schema syntax, enum spelling, Makefile changes, README changes, validator-code, generated zips, release mechanics, tests, and package updates. |

## Out of Scope

Out of scope for this slice: validation candidate selection, package
inclusion, README integration, Makefile changes, validator-code, deterministic
validation scripts, generated zips, released skill bundles, released skill
mechanics, source checkout edits, schema syntax, enum spelling, graph database
design, memory runtime design, CCDP service design, live extraction behavior,
runtime services, and source implementation.
