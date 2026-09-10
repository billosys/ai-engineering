# Slice01 CDC design review — revision required; acceptance pending

Current disposition update (2026-09-10): the operator accepted recommendations
Q-01, Q-02, Q-04, Q-05 and Q-06. Q-03 was subsequently settled by the
[hierarchical progress correction](artifacts/progress-decision.md), which
requires revision of the draft-1 contract and cases; R-01 still requires
correction. See the updated [project plan](../../project-plan.md).
The dated draft-1 review below is preserved; its blanket pending-decision
statements describe the 2026-09-06 review, not the current approval set.

Date: 2026-09-06. Reviewer: coordinating contributor (Sofie), separate from
the CC context that authored the contract. This context created the original
planning brief, so this is independent reproduction of CC's packet and CDC
design review, not a fresh-context audit of the original project assumptions.

## Verdict

The author accurately reported a proposed design packet and limited author
checks. The document/example checks reproduce. The contract is **not yet an
accepted implementation input**: R-01 below requires correction, and Q-01–06
remain operator/design decisions. All seven ledger rows stay open. No source
implementation, schema validation, rendering, package validation or Lykn UAT
was performed. No next slice was opened and no commits were created.

Read [status-contract.md](artifacts/status-contract.md),
[contract-cases.md](artifacts/contract-cases.md), and the
[author closing report](closing-report.md) with this review. Do not infer
closure from the existence of this verification filename.

## R-01 — Make child exclusions checkable without interpreting prose

Significance: correctness-grade. Status: open; blocks accepting the contract
as written. Locations: status-contract sections 3 and 4 (draft-1 lines 145–187
and evidence fields), contract-cases C-03 and C-22.

The draft promises a consistency error when a parent is closed while a child
is open, unless the parent's criteria/decision evidence names that exclusion.
However, Criterion and Deferral do not carry a structured reference identifying
the child being excluded. The decision claim's subject is the parent; its claim
and rationale are free text. C-03 names the child in prose, and C-22 expects the
presence of that decision to switch validation from failure to success.

A validator can check that the parent has a decision claim, but cannot reliably
decide which child that claim excludes. Matching a child's name in English is
not an implementable reference contract and can confuse mention with exclusion.

Recommended correction: introduce a typed exclusion association (for example,
a closure criterion's affected child EntityKey list), with exact permitted
relationships, disposition and supporting decision evidence. Alternatively,
explicitly make this a human review check and remove the promised automatic
error. The structured association is preferred because it preserves the
intended check while keeping acceptance judgments with the author/operator.
Exact field spelling is CC's proposed revision for design review.

Acceptance for the correction:

- A closed parent with an open child and no applicable exclusion fails.
- An exclusion naming a different child does not discharge this child.
- A dangling or unrelated child key fails reference/relationship validation.
- A valid association with correctly scoped decision evidence passes the
  structural check, without asserting the decision itself is true or accepted
  by the reviewer merely because it validates.
- Prose that happens to mention the child cannot alter the result.
- Define which state predicate counts as an open child; do not leave it to
  conflicting interpretations of lifecycle, delivery, closure and acceptance.

Update C-03/C-22 and add the necessary variants. Keep the original case IDs and
record the contract revision; the initial 38-case count is historical, not a cap.

## Recommendations on Q-01–06

These are CDC recommendations for operator review, not recorded operator
acceptance. They do not silently amend the draft or parent scope.

| Decision | Recommendation | Reason / qualification |
| --- | --- | --- |
| Q-01 ownership | Accept detail references or inline records with one owner | Eliminates copied summary contradictions. Referenced child JSON is needed to build the parent, but the generated parent HTML can still stand alone. |
| Q-02 state | Accept separate lifecycle, delivery, closure and acceptance axes, subject to R-01 | Avoid inherited verification. Historical source labels must remain visible beside normalized unknown/archive states; adoption must not silently reclassify historical claims. Test the authoring burden in Lykn UAT. |
| Q-03 progress | Accept slice delivery as the built-in ratio, with explicit coverage | Label it “slices reported delivered”; no-op/deferred is not delivered, and unknown/zero populations produce no misleading percentage. Project and arc status counts can still be separate labeled counts. |
| Q-04 compatibility | Accept strict core fields, locally resolved schemas and one supported format per tree | Fits pinned consumer copies. A schema-format version is distinct from the owning skill version. Upgrades are deliberate and cover data plus toolkit; extension warnings must make unsupported content visible. |
| Q-05 adjacent capabilities | Recommend typed links for core; leave full lessons/port modules outside the initial toolkit unless requested | The existing project scope requires explicit disposition, not automatic extraction of these domain capabilities. This is a recommendation requiring operator disposition, not an accepted deferral. |
| Q-06 Frontier | Accept eligibility from declared dependencies, shown separately from authored next actions | Labels must describe the actual computation. Slice02 should specify evaluation of unknown/unsatisfied inputs and whether ancestor constraints apply, or clearly label eligibility as local to the record. No implied world-state reconciliation or unimplemented topological sort. |

Additional UAT consideration: a two-leaf example already needs a substantial
amount of metadata. Preserve rigor, but test how much ordinary maintenance
requires duplicating planning evidence into JSON. Guidance and later tooling
should make the minimal honest record straightforward. This is a design/UAT
concern, not a newly invented acceptance blocker or instruction to weaken
evidence requirements.

## Reproduced checks

The reviewer wrote and executed an independent temporary Python check through
standard input rather than running the author's temporary checker. It:

1. Parsed all fenced JSON with duplicate-object-key rejection: **8 blocks**.
   Only the first three blocks are whole documents; the other five are fragments.
2. Indexed the three complete documents and walked detail/inline ownership:
   **5 distinct qualified entities**. Checked immediate parent keys, entry IDs
   and kinds, local source/evidence references, claim subjects, and delivery
   claims for the completed leaf.
3. Traversed leaf slices exactly once: collection **1/2**, project **1/2**, arc
   **1/1**. These are example delivery counts, not computed parent closure.
4. Resolved **28 relative Markdown links**, including local heading fragments,
   across the five author-authored/updated documents. Checked trailing
   whitespace and final newlines; no errors.
5. Enumerated S-01–07 once in each ledger/close row walk, C-01–38 once as primary
   cases, and Q-01–06 once in the decision table. This verifies inventory, not
   semantic correctness of every proposed negative case.
6. Recomputed the three private Rootstock project summary/arc-sum comparisons:
   all three disagree. No private payload copied; neither count is adjudicated.
7. Refreshed Lykn top-level project/arc/direct-slice directory shapes: arc
   counts **18, 19, 0, 1, 7, 3**; direct-slice counts **0, 0, 3, 0, 0, 0**.
   The six-project case mapping agrees with the inspected structural census.

All commands exited 0. Source worktree remained clean on `feature/project-status`
at `31d96b151781c63004370569d14db556ce21a604`. Planning HEAD observed during
review was `2796082486248d76dc2be9d83e2b69d71c88dd4e`; Project06 is untracked.
Other planning work is progressing, so HEAD alone does not identify this packet.

Reviewed input SHA-256 hashes, before this review's ledger annotation:

```text
6170f8ca8fbebbfe1b522e0cb86b0bf6bf070dd929d8512b9493769f63feb141  artifacts/status-contract.md
3ef85a6ddd9a6a9815cfe102e273f044dd02b043cbe7ad75e3e3ae9fed82467c  artifacts/contract-cases.md
02692244fa8fe8a61f11a0d57fb19634e54272f026c367acb9667064c684e4ce  artifacts/verification-record.md
b590da921455cb00b6bb34791a06422f84d3fa486352d1120938d88ebf11942f  ledger.md
8ed4e26b37b6fcc7e37c56cf9b559d75b3fc8d59f645d3c844feb33cdb97f622  closing-report.md
```

## Ledger review and bubble-up

| Row | Review result | Remaining boundary |
| --- | --- | --- |
| S-01 | Field tables and worked identities/references inspected; C-01 checks reproduce | Q-01/Q-04 and R-01 contract revision |
| S-02 | Distinct state/evidence semantics and cases present | Q-02 and machine-checkable exclusion rule R-01 |
| S-03 | Leaf ownership/arithmetic and sparse/unknown rules inspected | Q-03 design acceptance; no executable validator exists yet |
| S-04 | All six live structural shapes are represented | Design acceptance; actual open-arc census and historical judgments remain later UAT |
| S-05 | Extraction/view map covers original capabilities and named defects | Q-05 explicit adjacent-module disposition |
| S-06 | Snapshot/evolution policy respects the operator's ownership decision | Q-04 acceptance and already-planned Slice02 mechanics |
| S-07 | Document checks reproduce; artifact placement and row inventory correct | R-01 revision/review plus outstanding design decisions |

The author delivered the assigned proposed packet and disclosed its limits.
No evidence of a silently dropped slice deliverable was found. R-01 is a
contract correction within this slice, not a new arc. Q-05 may change scope
if full optional modules are chosen; amend the roadmap before planning against
that choice. Otherwise the existing arc/slice sequence still fits. No arc
scope/sequencing amendment or next-slice opening is justified yet.

What worked: the fictional mixed hierarchy exposes direct-slice counting;
single-owner records remove duplicate summary sources; source observations,
author checks and future toolkit/UAT tests are explicitly distinguished.

Next: obtain the operator's design dispositions, return the bounded R-01
correction to CC, re-review the revised contract/cases, then determine whether
the slice can close and Slice02 can be opened. Preserve this review as the
draft-1 result when recording a later pass.
