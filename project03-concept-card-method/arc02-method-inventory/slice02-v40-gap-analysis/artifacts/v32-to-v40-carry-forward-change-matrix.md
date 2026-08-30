# v3.2 To v4.0 Carry-Forward And Change Matrix

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice02-v40-gap-analysis
status: proposed-done
baseline:
  - ../slice01-v32-source-inventory/artifacts/v32-source-inventory.md
  - ../slice01-v32-source-inventory/artifacts/v32-method-structure-map.md
  - ../slice01-v32-source-inventory/artifacts/v32-original-assessment.md
mode: source-backed matrix
v4-design-decisions: none
```

## Scope Fence

This matrix separates v3.2 baseline items into `carry forward`, `minor cleanup`,
`architectural change`, `operator decision`, and `defer`. It is an input for
Slice03 synthesis and Arc03 conceptual model planning. It does not design the
v4.0 conceptual model, does not choose the Arc04 final skill layout, and does
not define implementation files, scripts, or package lists.

## Matrix

| v3.2 baseline item | Disposition | Why | Source anchor | v4.0 routing |
|--------------------|-------------|-----|---------------|--------------|
| One concept per card | carry forward | This is the core atomicity rule and remains compatible with later claim/evidence modeling. | `v32-source-inventory.md`; 0009 lines 36-44 | Protect as a method invariant unless Arc03 finds a stronger term. |
| Source-faithful, not source-copied synthesis | carry forward | The baseline already separates faithful extraction from plagiarism and requires source anchoring. | `v32-source-inventory.md`; 0009 lines 45-50 | Preserve as baseline rule for all v4.0 states. |
| Provenance as required card content | carry forward | Source title, slug, chapter, page, section, source reference, and verification notes are already required. | `v32-source-inventory.md`; 0009 lines 81-89, 126-144, 438-470 | Carry forward while adding separate evidence/provenance grading if Arc03 accepts it. |
| Body sections for definitions, prerequisites, properties, procedures, examples, relationships, errors, confusions, source reference, and verification notes | carry forward | The body template is mature and useful for both humans and LLMs. | `v32-source-inventory.md`; 0009 lines 222-470; 0010 lines 396-509 | Preserve unless Arc03 splits some sections into new first-class constructs. |
| Competency question linkage | carry forward | CQs already connect cards to user questions and coverage checks. | `v32-source-inventory.md`; `v32-method-structure-map.md`; 0009 lines 209-219; 0010 lines 143-190, 715-720 | Preserve and consider explicit CQ status in Arc03. |
| Source-primary re-extraction | carry forward | v3.2 correctly makes converted Markdown source primary and old card secondary. | `v32-source-inventory.md`; 0009 lines 585-619; 0010 lines 534-551 | Preserve as anti-amnesia rule. |
| Old-card unique-value preservation | minor cleanup | The rule is strong, but v4.0 likely needs clearer evidence for preserved, rejected, and lost material. | `v32-source-inventory.md`; 0009 lines 621-629; 0010 lines 684-713, 895-902 | Keep the rule; improve evidence capture in later design/planning. |
| Path and slug hygiene | minor cleanup | The baseline already catches wrong paths and slug mismatches, but these are partly repo-specific constraints. | `v32-source-inventory.md`; 0009 lines 474-568; 0010 lines 798-806 | Route package/path specifics to Arc04/Arc05; keep method-level consistency rule. |
| Error versus confusion distinction | minor cleanup | The distinction is useful and already explicit; it may need tighter guidance but not a new architecture. | `v32-source-inventory.md`; 0009 lines 402-436, 712-718 | Carry forward with wording cleanup in later skill docs. |
| Confidence as `high` / `medium` / `low` | architectural change | The field mixes source explicitness, extractor certainty, verification status, evidence grade, and downstream usability. | `v32-source-inventory.md`; `v32-method-structure-map.md`; `v32-original-assessment.md`; 0009 lines 71-79; 0010 lines 860-866 | Arc03 should separate extraction confidence from evidence grade and verification/admission states. |
| Checklist/shell validation | architectural change | Existing checks are useful but do not specify schema validation, semantic QA evidence, verifier role, or reconciliation status. | `v32-source-inventory.md`; 0009 lines 632-672; 0010 lines 625-733 | Arc03 should define validation concepts; Arc05 later plans deterministic tooling. |
| Four relationship fields | architectural change | The fields are useful but not enough for graph-native relationships with edge evidence, status, inverse policy, or reconciliation. | `v32-method-structure-map.md`; 0009 lines 183-207, 370-399; 0010 lines 868-874 | Arc03 should define graph/edge concepts without discarding v3.2 fields prematurely. |
| Parallel five-agent workflow | operator decision | 0010 uses exactly five agents, but it is unclear whether this is invariant or an example operating default. | `v32-method-structure-map.md`; 0010 lines 311-339 | Operator decides whether v4.0 parameterizes parallelism. |
| Skill packaging | operator decision | v3.2 describes howtos and repo paths, not a final loadable skill boundary or package shape. | `v32-source-inventory.md`; 0009 lines 474-518; 0010 lines 35-91 | Arc04 owns final skill layout; Arc03 should avoid deciding package structure. |
| Memory admission | architectural change | v3.2 validates cards but does not define whether a card is admitted to durable memory. | `v32-method-structure-map.md`; `v32-original-assessment.md` Memory Fit | Arc03 should define memory admission as a possible lifecycle state. |
| CCDP-compatible evidence semantics | architectural change | CCDP is absent from 0009 and 0010, while the Project03 target requires claim/provenance/audit fit. | `v32-method-structure-map.md`; `v32-original-assessment.md` CCDP Fit | Arc03 should define method-side semantics; later arcs handle implementation/package work. |
| Extraction run traceability | architectural change | 0010 describes phases and prompts, but no first-class trace object records source snapshot, prompt, agent scope, output, and validation result. | `v32-source-inventory.md`; 0010 lines 95-339, 512-621 | Arc03 should decide whether extraction run is a concept in the model. |
| Live corpus validation | defer | This arc is source-backed planning, not a live extraction demonstration. | `slice-plan.md` Out of scope; `v32-source-inventory.md` Workflow | Defer to implementation planning or a later validation slice if the operator requests one. |
| Full GraphRAG or memory runtime | defer | Project03 boundaries exclude building a graph database or memory runtime during planning. | `project-plan.md` Boundaries; `v32-original-assessment.md` Memory Fit | Keep as external context; do not add runtime work to Arc02. |

## Disposition Counts

- `carry forward`: 6
- `minor cleanup`: 3
- `architectural change`: 7
- `operator decision`: 2
- `defer`: 2

## Slice03 Handoff

Slice03 should use this matrix to produce the Arc02 synthesis: what v3.2 keeps,
what v4.0 must change, what needs operator choice, and what remains deferred.
The highest-priority Arc03 inputs are confidence/evidence separation,
verification state, reconciliation, memory admission, graph-native
relationship semantics, extraction run traceability, and CCDP-compatible
evidence semantics.
