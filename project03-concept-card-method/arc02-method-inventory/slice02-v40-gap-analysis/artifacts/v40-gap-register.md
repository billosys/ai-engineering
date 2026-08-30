# v4.0 Gap Register

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice02-v40-gap-analysis
status: proposed-done
baseline:
  - ../slice01-v32-source-inventory/cdc-verification.md
  - ../slice01-v32-source-inventory/artifacts/v32-source-inventory.md
  - ../slice01-v32-source-inventory/artifacts/v32-method-structure-map.md
  - ../slice01-v32-source-inventory/artifacts/v32-original-assessment.md
mode: source-backed gap analysis
v4-design-decisions: none
```

## Scope Fence

This register is source-backed by the verified Slice01 baseline artifacts:
`v32-source-inventory.md`, `v32-method-structure-map.md`, and
`v32-original-assessment.md`. It records gaps and routing for Slice03 and
Arc03; it does not design the v4.0 conceptual model, does not decide the Arc04
final skill layout, and does not edit source files. The analysis uses source
anchor references to the Slice01 inventory and, through it, to source docs
0009 and 0010.

## Summary

The v3.2 baseline should carry forward its core knowledge-substrate discipline:
one concept per card, source-faithful extraction, source provenance, typed
relationships, competency questions, re-extraction from source, old-card
preservation checks, and explicit quality checks. The v4.0 change is justified
where v3.2 treats operationally distinct ideas as prose conventions or one flat
field: evidence/provenance grading, independent verification, reconciliation,
memory admission, graph-native relationships, CCDP-compatible evidence
semantics, skill packaging, schema validation, semantic QA, and extraction run
traceability.

## Gap Rows

| ID | Concern area | v3.2 baseline | Gap | Classification | Source anchor | Downstream routing |
|----|--------------|---------------|-----|----------------|---------------|--------------------|
| G-01 | evidence/provenance grading | Provenance is required through source metadata, source reference, and verification notes. | Source citation, extraction confidence, and evidence grade are not separated. | architectural change | `v32-source-inventory.md` Provenance and Confidence Semantics; `v32-method-structure-map.md` Provenance and Confidence rows; 0009 lines 71-89, 126-152, 438-470; `v32-original-assessment.md` What Needs Updating. | Arc03 should define the conceptual distinction between source span, claim, extraction confidence, and evidence grade. |
| G-02 | independent verification | v3.2 validates by checklist, grep, CQ coverage, and sampling after extraction. | The method does not model verifier role, verification status, reproduced evidence, or reconciliation status. | architectural change | `v32-source-inventory.md` Validation; `v32-method-structure-map.md` Validation row; 0009 lines 632-672; 0010 lines 625-733. | Arc03 should decide which verification concepts are part of the method; Arc05 can later plan scripts after the model exists. |
| G-03 | reconciliation | Parallel extraction balances exactly five agents and validates output after the run. | There is no explicit reconciliation authority for duplicate concepts, competing definitions, slug drift, taxonomy drift, or relationship asymmetry. | architectural change | `v32-source-inventory.md` Workflow and Notable Limitations; `v32-method-structure-map.md` Parallel workflow; 0010 lines 311-339 and 625-733; `v32-original-assessment.md` What Needs Updating. | Arc03 should define reconciliation as concept/process if accepted; Slice03 should carry this as a high-priority Arc03 input. |
| G-04 | memory admission | Validated cards become effective durable substrate. | The baseline has no explicit memory admission state for whether a card is safe for future cognition to rely on. | architectural change | `v32-source-inventory.md` Notable Limitations; `v32-method-structure-map.md` Memory admission row; `v32-original-assessment.md` Memory Fit. | Arc03 should define memory-admission status and its relationship to evidence and verification; implementation deferred beyond Arc03. |
| G-05 | graph-native relationships | v3.2 has four typed relationship fields and body explanations. | Relationships are graph-ready but not graph-native: no edge evidence, edge status, reconciliation, inverse-edge policy, or graph closure contract. | architectural change | `v32-source-inventory.md` Relationship Model; `v32-method-structure-map.md` Relationship row; 0009 lines 183-207, 370-399, 661-665; 0010 lines 666-681. | Arc03 should define relationship/edge concepts; Slice03 should preserve the exact v3.2 relationship fields as carry-forward inputs. |
| G-06 | CCDP-compatible evidence semantics | CCDP is absent from 0009 and 0010. | v3.2 does not encode cognitive outputs as claims with provenance grade, audit trail, dispatchable capability, or admission decision. | architectural change | `v32-method-structure-map.md` CCDP row; `v32-source-inventory.md` Notable Limitations; `v32-original-assessment.md` CCDP Fit. | Arc03 should define only the method-side concepts; Arc04/Arc05 should decide packaging and source edits later. |
| G-07 | skill packaging | v3.2 is documented as workbench/howto material and references repo paths. | The baseline does not define a loadable skill boundary, reason to load, guide split, templates, scripts, examples, or package behavior. | operator decision | `v32-source-inventory.md` File Organization; `v32-method-structure-map.md` Source And Repository Placement; 0009 lines 474-518; 0010 lines 35-91. | Arc04 owns final skill layout; Slice03 should ask what packaging decisions Arc03 must avoid. |
| G-08 | schema validation | v3.2 names required fields and uses shell checks. | Required shape is not captured as a formal schema with enum validation, required/nullable semantics, or relationship-field type rules. | architectural change | `v32-source-inventory.md` Schema and Validation; `v32-method-structure-map.md` Schema and Validation rows; 0010 lines 627-649 and 877-889. | Arc03 should decide the conceptual schema; Arc05 can later decide script/schema implementation. |
| G-09 | semantic QA | v3.2 samples definitions, confidence rationales, prerequisites, examples, variants, relationships, and section names. | Sampling is procedural but lacks explicit QA evidence records, reviewer identity, pass/fail status, and source-span fidelity criteria. | architectural change | `v32-source-inventory.md` Validation; `v32-method-structure-map.md` Validation And Quality Control; 0010 lines 722-733. | Arc03 should define semantic QA concepts and status; Slice03 should distinguish deterministic validation from human/LLM review. |
| G-10 | extraction run traceability | 0010 gives coordinator phases, agent assignments, prompts, and run workflow. | The baseline does not make extraction run, agent scope, source snapshot, prompt version, generated card set, or validation result first-class trace records. | architectural change | `v32-source-inventory.md` Workflow; `v32-method-structure-map.md` Extraction Workflow and Parallel Coordination; 0010 lines 95-339 and 512-621. | Arc03 should define extraction-run trace concepts; Arc04 can later decide files/templates. |
| G-11 | source-faithful extraction | v3.2 strongly states source-primary extraction, one concept per card, and provenance. | No major conceptual gap; preserve this as the baseline method core. | carry forward | `v32-source-inventory.md` Purpose, Workflow, Provenance; 0009 lines 36-89 and 585-619. | Slice03 should list this as a protected carry-forward item. |
| G-12 | old-card preservation | v3.2 requires old-card review, unique-value preservation, card-count comparison, and preservation notes. | The preservation rule is strong, but evidence capture is lighter than v4.0 likely needs. | minor cleanup | `v32-source-inventory.md` Re-Extraction Mechanics and Preservation Checks; 0009 lines 621-629; 0010 lines 684-713 and 895-902. | Slice03 should mark preservation discipline as carry-forward with cleanup around evidence detail. |
| G-13 | competency questions | v3.2 links cards to CQs and uses CQs for requirements, mapping, and coverage checks. | The CQ role is sound; the gap is making CQ coverage status and test results explicit enough for v4.0. | minor cleanup | `v32-source-inventory.md` Competency Question Handling; `v32-method-structure-map.md` Competency question row; 0009 lines 209-219; 0010 lines 143-190, 289-309, 715-720. | Slice03 should carry forward CQs and route explicit CQ status to Arc03. |
| G-14 | parallelism degree | 0010 requires exactly five agents for the described parallel re-extraction workflow. | It is unclear whether "five agents" is a method invariant, a default operating recipe, or historical tooling assumption. | operator decision | `v32-method-structure-map.md` Parallel Coordination; 0010 lines 311-339. | Operator should decide whether v4.0 generalizes this to parameterized parallelism. |
| G-15 | live corpus extraction | This slice did not run extraction against a live corpus and v3.2 docs describe the process abstractly. | Live-use validation is useful but not required for Arc02 inventory/gap analysis. | defer | `slice-plan.md` Out of scope; `v32-source-inventory.md` Workflow. | Defer until implementation planning or a later validation project, unless operator adds a demo slice. |

## Routing Summary

- Carry forward: atomic cards, source-faithful synthesis, provenance discipline,
  typed relationships, CQs, re-extraction from source, old-card preservation,
  and validation as an explicit close gate.
- Minor cleanup: preservation evidence wording, CQ coverage status, path/name
  clarity, and distinction between procedural errors and conceptual confusions.
- Architectural change: evidence/provenance grading, independent verification,
  reconciliation, memory admission, graph-native relationships,
  CCDP-compatible evidence semantics, schema validation, semantic QA, and
  extraction run traceability.
- Operator decision: skill packaging boundaries and whether exactly-five-agent
  parallelism remains a rule or becomes a parameter.
- Defer: live corpus validation and final implementation mechanics.

## Inputs For Slice03 And Arc03

Slice03 can synthesize this register with the Slice01 inventory into an Arc02
close input. Arc03 can later define the conceptual model using these open
questions: concept card versus claim, source span, evidence grade,
relationship/edge, competency question status, extraction run, verifier role,
reconciliation result, and memory admission. This register intentionally stops
at routing and gap naming.
