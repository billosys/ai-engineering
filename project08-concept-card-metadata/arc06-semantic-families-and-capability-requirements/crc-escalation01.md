# CRC Escalation 01: Size The Next Provenance Unit

Date: 2026-09-17. From: CRC. To: CDC through the Operator.
Owning project: `project08-concept-card-metadata`; owning arc:
`arc06-semantic-families-and-capability-requirements`. Originating slice:
`slice14-provenance-context-and-reference-semantics` (closed). This report
is the first arc-level design exchange; project-level `cdc-directive01.md`
remains the governing three-contributor assignment, not this report's
response. Current CC assignment: none. Do not send this packet to CC.

## State And Evidence

- Planning acceptance commit: `febbd7870442d19e96247a080c963306a725c673`.
  Slice14 CC contribution `b10bb1ec127568478bbd72f4ae929d4cb677c255`;
  separately committed replay recipe
  `a4a7047cb171e66d7ec1b17ce7c3c2707c48a50b`.
- Source HEAD at independent review:
  `76a69fd9c295e78f23faa651746c2e36646e0ebd`; no source edits were
  made by CRC. The planning worktree was clean after acceptance. The frozen
  transition inventory remains unchanged.
- Governing versions at this request: project plan 1.29, arc plan 1.15,
  closed Slice14 plan 1.4. Slice14 ledger S14-1 through S14-6 are done under
  its [independent CRC verdict](./slice14-provenance-context-and-reference-semantics/crc-verification.md).
  Arc ledger A6-1 through A6-10 and project P-1 through P-15 remain open.
- [Current coverage](../artifacts/semantic-coverage-current.json) independently
  reconciles to 555 full / 200 accepted / 355 remaining / zero assigned.
  Slice14 accepted twelve `actor`/`actor.id` pairs, not an actor ontology.
- [Slice14 handoff](./slice14-provenance-context-and-reference-semantics/artifacts/handoff.md)
  retains unresolved identity, authority and requiredness questions. It
  proposes the twenty remaining `actor.mode`/`actor.role` pairs as a candidate,
  subject to recount and split. Arc06 still owns all 355 remaining pairs.

## Design Question

The approved arc plans an unsized Slice15 with the remaining provenance
obligations: twenty `actor.mode`/`actor.role` pairs across ten record kinds,
plus run, preparation, method, shared-reference and remaining CQ provenance
interfaces. The coverage register assigns none of them. Opening all of these
as one CC task would silently turn a retained owner into an unbounded
execution packet. CRC may conduct routine acceptance and advancement, but
splitting this owner or changing the next slice's structural scope requires
CDC design direction. The uncertainty is size and grouping, not whether the
work remains required.

The twenty-pair set is directly enumerable from the current coverage
register: `actor.mode` and `actor.role` for claim, competency-question,
concept-card, extraction-run, memory-admission, preservation-decision,
relationship-edge, source-locator, source-support and validation-result.
It does not establish equal meanings, populated values, or sufficient
evidence in every kind. Fresh native recount and witness selection are
required before issuing a CC prompt.

## Options And Tradeoffs

1. **One twenty-pair Slice15.** Keeps related fields together and minimizes
   handoffs, but spans ten kinds and two different source populations. Slice14
   needed three executed CC runs for twelve pairs; that observation is a
   workload signal, not a model ranking or a proof that twenty will fail.
2. **Two kind-aligned units, eight then twelve.** First examine mode/role in
   claim, competency-question, concept-card and extraction-run (eight pairs),
   where Slice13 already established actor identity. Then examine the six
   supporting/result kinds from Slice14 (twelve pairs). This preserves
   identity-context continuity and gives each unit a bounded review loop,
   at the cost of an explicit later slice and cross-unit synthesis. Run,
   preparation, method, shared-reference and CQ interfaces remain owned for
   separately sized work; they are not discharged by these two units.
3. **Recount and choose another family boundary.** A native census may show
   mode/role evidence clusters differently. This could give better semantic
   cohesion, but requires CDC to specify a concrete owner/criterion split
   before CRC drafts any slice or prompt.

CRC recommends Option 2 as a starting hypothesis, conditional on a fresh
native-input recount and exact accepted/remaining set check. It matches the
two accepted actor.id kind groups and limits the next CC packet. It is not an
approved architecture or permission to create Slice15/Slice16.

## Decisions Requested Of CDC

1. Approve, reject or revise the next semantic-family boundary and exact
   Slice15 pair set; decide whether the other twelve mode/role pairs move to
   a separately numbered future slice, and name the owner of every retained
   provenance interface. Do not leave a catch-all implicit.
2. Specify whether a pre-opening native recount is part of CRC preparation
   or the first CC assignment, and the minimum evidence needed to approve
   the set. Preserve the 555-pair denominator and finer corpus/role context.
3. Confirm the permitted plan, ledger and coverage amendments, whether CRC
   may issue the next CC prompt using the new framework prompt-authoring guide,
   and which acceptance/reverification gates remain held. P-15's schema/spec
   discussion and Operator acceptance must not be inferred from this work.

No previously accepted membership, evidence packet or source skill needs
reopening solely because of the sizing decision. Any later contradiction
should be surfaced explicitly through the normal review path.

## Hold And Return

Paused: opening Slice15, assigning pairs, editing source/schema/runtime,
or sending a new CC prompt. CRC may inspect and prepare bounded census notes
under existing read-only authority, but may not treat them as an approved
new scope. CDC owns the next decision; the Operator should pass this exact
path to CDC:

`arc06-semantic-families-and-capability-requirements/crc-escalation01.md`

CDC returns a preserved arc-level `cdc-directive01.md` answering this report,
or records an explicit unresolved/Operator gate. CRC then reconciles the
directive with the current planning state, records its acknowledgment in the
arc Design Handoff History, and only then amends plans or issues a CC prompt.
Slice14's two executed corrective refinements and R1-R5 history remain
unchanged; this exchange does not reset an iteration count.
