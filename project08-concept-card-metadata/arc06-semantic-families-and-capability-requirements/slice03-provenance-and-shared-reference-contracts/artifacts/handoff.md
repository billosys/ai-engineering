# Slice03 handoff

Status: CC proposed-done; independent CDC review is required. This slice adds
no semantic membership pairs. Current accepted inventory remains 180 pairs,
with 375 remaining and zero assigned to Slice03.

## Reuse contract

The next semantic-family packet can reuse `evidence-replay-contract.md` and
the literal route in `worked-replay.md` for four mechanical separations:

1. Register each input with root, exact path, byte hash, role, and applicability.
   Pin historical planning authority to an explicit Git commit; read live
   status separately and never refresh a mutable ledger hash in a
   self-referential loop.
2. Keep original/copy lineage, source/planning roots, construct revision and
   Git snapshot revision distinct. Byte equality supports preservation of
   bytes, not semantic authority.
3. Author expected results independently from native observations. Compare
   parsed JSON structurally, preserve key-order invariance, and retain stdout,
   stderr presence, exit status and classification.
4. Exercise match, successful no-match, wrong expected identity/revision and
   actual tool-error controls using the same bounded operation. Preserve
   missing, null and empty states rather than normalizing them away.

The recipe is intentionally a planning convention. It is not a generic
validator, parser, schema, extraction framework, runtime, graph service or
memory admission mechanism.

## Semantic work retained for Slice13

The former combined Slice03 provenance/shared-reference responsibilities remain
intact and move to planned Slice13 for exact sizing. They include actor,
actor.id, actor.mode, actor.role, run, preparation, method and shared
reference semantics across the applicable record kinds, including provenance
interfaces for CQ records. No field is accepted here merely because the
replay contract can name or hash it.

The future semantic review still has to decide, from actual contexts and
documented rules:

- whether an actor identifies a human, model, tool, process or other role, and
  how mode and role differ;
- which run, preparation and method references identify the operation versus
  the source or resulting construct;
- when a shared reference is a reusable evidence identity, a locator, a
  provenance link or only an editorial navigation aid;
- which revision, snapshot and source boundaries govern reference
  applicability; and
- which CQ provenance interfaces are required for origin, intended use,
  answerability review and later lifecycle results without collapsing their
  scopes.

These remain evidence-backed design questions, not a requiredness policy or
future profile decision.

## Bounded Slice13 sizing recommendation

Do not open the former combined workload as one semantic packet. A manageable
candidate first unit is **Slice13A: actor identity across four record kinds**:
`actor` and `actor.id` for claim, competency-question, concept-card and
extraction-run (8 remaining pairs), with the applicable source/template/
generated contexts selected before execution. A later bounded unit can cover
`actor.mode` and `actor.role` after Slice13A exposes whether those meanings
actually differ. Run/provenance/preparation/reference families should be split
again if their census or evidence layers exceed one context with review
headroom.

This is a sizing recommendation, not an assignment or acceptance. Before
opening Slice13, derive the exact pairs from the current remaining register,
record the authoritative inputs and four-way role boundaries, and amend the
arc plan if the observed workload changes sequencing or ownership.

## Cross-owner interfaces and gates

| Interface | Re-entry / owner |
| --- | --- |
| Slice02 CQ/reference distinctions | Slice13 must attach provenance without treating a CQ tuple, literal heading or parent-card revision as proof of source support or answerability. |
| Slice04 evidence grade/confidence | Keep assessment subject, rubric, rationale and extraction confidence separate from actor/run provenance. |
| Slice05 validation/verification | A replay status and a validation result are different records; independence and applicability remain later work. |
| Slice06-08 lifecycle | Reconciliation, preservation, admission and authority must not be inferred from a provenance reference or successful lookup. |
| P-15 schema/specification gate | Operator discussion is required before any future field structure, requiredness, schema language or specification is adopted. |

The next semantic packet should report unresolved references, inaccessible
sources and unknown actor/run roles explicitly, with re-entry conditions. The
replay route proves operational reproducibility only; it does not settle those
semantic judgments.

## Preserved boundaries

Arc01, both coverage registers, and accepted Slice01/Slice02/Slice12 packets
remain read-only. Source, package, install, runtime, extraction, RAG/MCP,
graph and memory-admission work remains out of scope. Slice03 does not open
Slice13 or any later slice.
