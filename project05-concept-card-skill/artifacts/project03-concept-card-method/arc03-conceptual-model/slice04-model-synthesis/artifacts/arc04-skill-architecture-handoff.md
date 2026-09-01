# Arc04 Skill Architecture Handoff

```yaml
project: project03-concept-card-method
from-arc: arc03-conceptual-model
from-slice: slice04-model-synthesis
to-arc: arc04-skill-architecture
status: proposed-done
not-final: true
mode: handoff packet
```

## Purpose

This handoff gives Arc04 the accepted Arc03 close input for planning the
v4.0 concept-card method skill architecture. It is not final skill
architecture and does not choose final file layout, package behavior, README
integration, exact schema syntax, enum spelling, validation script
implementation, generated zips, or source edits.

## Conceptual-Model Commitments Arc04 Must Preserve

- The concept card remains the visible atomic method unit: one concept per
  card, with source-faithful synthesis and required provenance.
- Claims are conceptually first-class when evidence, source support,
  verification, reconciliation, or memory admission needs finer granularity
  than the card.
- Source support and source span attachment points are distinct from general
  provenance.
- Extraction confidence, source support, evidence grade, verification state,
  reconciliation state, validation result, and memory admission are not one
  confidence field.
- Verification result, validation result, reconciliation result, and
  preservation decision records must remain auditable result records or
  explicit lifecycle attachments.
- v3.2 relationship vocabulary carries forward: `prerequisites`, `extends`,
  `related`, and `contrasts_with`.
- Graph-native edge identity is required when evidence, lifecycle state,
  provenance, reconciliation, or CQ coverage attaches to the relationship.
- Competency questions remain first-class constructs with requirement,
  answerability, coverage, verification, retrieval, obsolete, and deferred
  roles or statuses.
- Extraction runs are first-class trace records for source snapshot, method
  version or prompt version, agent scope, output set, old-card inputs,
  preservation decisions, validation result, reconciliation result, and
  parallel-worker provenance.
- Memory admission remains a lifecycle gate distinct from validation and
  verification.

## Candidate Skill-Architecture Inputs

Arc04 should decide how the loadable skill presents the method without
weakening the conceptual model:

- `SKILL.md` entrypoint scope: when to load the concept-card method skill and
  how it routes to focused guides.
- Guide split: extraction, re-extraction, evidence/lifecycle, graph/CQ
  semantics, reconciliation, memory admission, and verification/validation.
- Template set: concept card template, claim/source support template, CQ
  template, extraction-run trace template, reconciliation result template, and
  validation/verification result templates.
- Validation script candidates: checks for required sections, provenance,
  source support, relationship references, CQ coverage, graph closure,
  preservation decisions, and memory-admission gates.
- Example set: minimal card, claim-backed card, CQ coverage example,
  relationship/edge example, extraction-run trace example, reconciliation
  example, and memory-admission example.
- README integration: how the repo documents the skill, what package users can
  rely on, and what remains experimental.
- Package behavior: whether templates, guides, scripts, examples, and any
  generated artifacts belong in the packaged skill.

## Questions for Arc04

- How thin should `SKILL.md` be, and which guide should own each method
  concern?
- Which guides are required for first release, and which can remain examples
  or later additions?
- Which templates are user-authored surfaces versus internal trace/result
  records?
- Which validation script checks are deterministic enough for Arc05 to plan?
- How should Arc04 present provisional evidence-grade, verification-state,
  reconciliation-state, CQ-status, and memory-admission vocabularies without
  locking exact enum spelling too early?
- How should the v3.2 five-agent parallel workflow be represented: invariant,
  default recipe, or parameterized pattern?
- What README and package behavior should make the method discoverable without
  promising runtime GraphRAG, memory runtime, ontology database, or CCDP
  service behavior?

## Dependencies and Risks

- Arc04 depends on CDC verification of Slice04 and a formal Arc03 close report
  before treating this handoff as accepted Arc03 input.
- Over-collapsing concepts into one template risks losing the distinction
  between extraction confidence, source support, evidence grade, verification
  state, reconciliation state, and memory admission.
- Over-designing scripts in Arc04 risks trespassing into Arc05 implementation
  planning.
- Under-specifying result records risks returning to v3.2-style prose
  evidence where validation, verification, reconciliation, and preservation
  decisions are hard to audit.
- Treating CQ retrieval as runtime design would pull GraphRAG runtime, memory
  runtime, or indexes into scope too early.

## Arc03 Close Input

Arc03 can close once Slice04 is CDC-verified and the arc-scale composition
check reproduces that:

- Slice01 defined construct boundaries for concept card, claim, source span,
  evidence grade, relationship/edge, competency question, extraction run,
  verifier, reconciliation, and memory admission.
- Slice02 separated extraction confidence, source support, evidence grade,
  verification state/result, reconciliation state/result, validation result,
  and memory admission.
- Slice03 defined relationship/edge, CQ coverage, extraction-run traceability,
  reconciliation conflict classes, and result-record attachment points.
- Slice04 accepted the synthesized v4.0 conceptual model and recorded
  remaining accepted, provisional, deferred, out-of-scope, and open question
  decisions.

The Arc03 close should verify composition directly from the artifacts and
parent `ledger.md`, not merely inherit child closure.

## Explicit Non-Decisions

This handoff does not choose final skill architecture. It does not choose
final file layout, package behavior, README integration, exact schema syntax,
exact enum spelling, validator implementation, validation script code,
GraphRAG runtime, memory runtime, ontology database, CCDP service design,
generated zips, or source edits.
