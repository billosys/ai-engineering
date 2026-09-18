# Slice15 handoff: provenance roles, runs, and shared references

Status: CC proposed-done. Return to the Operator for CRC routine review and
CDC composition review; no semantic membership is accepted by this handoff.

## Returned observations

Slice15 covered exactly eight `actor.mode`/`actor.role` pairs across claim,
competency-question, concept-card, and extraction-run records. The native
selected census is 37 parsed object mappings: 12 absent actor parents, four
template objects with null mode/role children, and 21 populated card actors.
The populated values are `agent-direct`/`extractor`; the parent IDs are literal
`codex-cc` on four pilot cards and `codex` on 17 rich/teaching cards. The
legacy untyped comparison is 2,054 records with actor parent absent. YAML
errors and no-frontmatter records remain separate availability states.

The durable registry, semantic report, and literal replay route are the six
files listed in the closing report. The route distinguishes precommit working
tree evidence from committed CC and recipe endpoints, and it leaves source,
schema, extraction, memory, coverage acceptance, and UAT untouched.

## Per-kind questions for review

- Claim: is a reserved actor mode/role slot intentionally claim-local, and
  which authority (if any) may populate it?
- Competency question: how should the actor slot relate to CQ roles,
  coverage, answerability, and later query execution without conflation?
- Concept card: are the populated values revision/extraction provenance only,
  and should family and run references be required before any normalization?
- Extraction run: should run actor mode/role remain optional and distinct from
  worker-scope mode/role and output-card actors?

## Slice16 comparison obligation

Slice16 should compare the eight returned pairs with the next exact 12-pair
assignment, preserving pair identity and state distinctions. It should
explicitly compare:

1. card `agent-direct`/`extractor` observations against any new generated
   families or revision stages;
2. template child-null against absent parents on synthetic CQ/run examples;
3. worker-scope roles/modes against run actor roles/modes;
4. CQ role arrays against `actor.role`;
5. literal IDs and family labels without normalizing them into authority;
6. legacy absent actor parents against newly parsed typed records;
7. YAML-error and no-frontmatter denominators against any refreshed inventory;
8. negative controls for wrong mode `human-assisted`, wrong role `validator`,
   swapped mode/role, and absent-as-null;
9. source/planning hash and range drift at the new opening commits;
10. coverage placement as a remaining-set subset, not equality with the full
    unassigned space;
11. the source/registry/route six-file scope fence; and
12. the distinction between proposed-done evidence and independent review.

Slice16 must not treat this handoff as a schema or vocabulary decision.

## Slice17 retention and ownership

Slice17 should retain the unresolved extraction-run actor semantics, run
preparation/method references, shared-reference identity, and remaining CQ
role/context questions. The concept-card generated-card evidence remains
useful as an observed provenance witness, not as a universal actor contract.
The Operator/CDC retains acceptance authority, the CRC owns independent review
of this slice, and the CC remains the implementation/evidence contributor.

P-15 and UAT remain open. No successor slice is created here, no schema or
parser work is authorized, and no coverage acceptance is updated by this
handoff. Any follow-up must be issued through the canonical planning worktree
and preserved as a new prompt or recorded review directive.
