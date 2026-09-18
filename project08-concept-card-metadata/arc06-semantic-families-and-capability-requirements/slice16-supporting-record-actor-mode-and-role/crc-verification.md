# Slice16 CRC Verification

Current verdict: **changes required**. This is independent CRC review of the
initial `cc-prompt.md` packet, not CDC arc composition or Operator acceptance.
No Slice16 pair is accepted; live coverage remains 208/347/12/335. Slice17
remains held for CDC sizing.

Date: 2026-09-18. CC registry endpoint `2953953d`, final reported recipe
endpoint `974dd26a`, planning HEAD `974dd26a`, source HEAD `ce3f7710`.
Both worktrees were clean at review intake. `git diff --name-only
3b7790f8..974dd26a` contains exactly the six authorized Slice16 files;
`git diff --check` passed.

## Independent Checks

- Read the active project/arc/slice plans, ledger, directive, initial prompt,
  six-file packet, registry memberships, native witnesses and handoff. The
  twelve member meanings remain kind-specific and do not promote support
  actors to claim/card actors, admission authority, edge endpoint roles or
  validator identity.
- Executed the literal route extracted from committed `REPLAY_COMMIT=974dd26a`
  against registry `CC_COMMIT=2953953d`. Exit status 0. It reproduced twelve
  selected mappings by kind, 2 absent parents, 6 null template children,
  4 populated pilot supports, 2,054 legacy mappings, three YAML errors and
  15 no-frontmatter records. Reported mutation statuses were 1; missing
  inventory returned 2. These are structural checks, not semantic acceptance.
- Inspected the route's hash/range dispatch against all 45 registered evidence
  rows. All current snapshot rows name one of the two opening commits. The
  positive replay passes, but the checks below do not enforce the declared
  `authority_commit` or all declared `source_range` values.

## Findings

| ID | Row | Finding and evidence | Required correction |
| --- | --- | --- | --- |
| R1 | S16-5 | `semantic-membership.json` gives every evidence row an `authority_commit`, but `validation-evidence.md` `check_hashes` (lines 214-245) reads snapshots from the hard-coded `opening_planning`/`opening_source` without reading that field. `check_line_range` (lines 250-267) does likewise. A candidate row can declare a nonexistent or wrong authority while the route continues checking the original bytes. The positive 45-hash/range result therefore does not validate the registered authority layer. | For every snapshot row, read its declared commit, validate its intended root/authority against this slice's pinned opening commit, and resolve both hash and range from that declared revision. Use the same production predicates for valid and mutated candidates. Mutate one `authority_commit` to a wrong/nonexistent revision and show rejection; retain the 45 positive hashes/ranges and unrelated-global-HEAD tolerance. |
| R2 | S16-5 | `check_line_range` selects only strings starting `lines ` (line 266). The registry has three legitimate JSON-document descriptors. Replacing a numeric range with `not-a-range` removes the row from the checked projection; the route would skip it. Independent jq projection showed 41 selected numeric rows after this mutation, down from 42, with no all-45 coverage assertion. | Validate every one of 45 range registrations. Allow the exact current JSON descriptors only on their intended JSON evidence IDs, validate numeric spans at the declared authority, and reject null/unknown/misplaced descriptors. Add a mutation such as `source_range="not-a-range"` and show status 1, alongside existing out-of-bounds/reversed controls. |
| R3 | S16-4 | The issued prompt and ledger require real no-match `[]`/status 0 versus a missing-input error. The route instead wraps the empty query in `{count:0,actors:[]}` (lines 294-297), and the close report records that object. This establishes emptiness, but not the specified raw result. | Run the real inventory lookup so the returned value itself is `[]` with status 0, and record that exit/output separately from missing-input status 2. An additional count is fine, but it cannot replace the required result. Correct the validation and closeout wording. |

S16-1, S16-2, S16-3 and S16-6 have no finding in this review, but the slice is
not partially accepted. S16-4 and S16-5 remain open. The current twelve
meanings and census are preserved as CC-attested evidence, not a schema or
accepted semantic vocabulary. This is a bounded evidence-route correction
inside the approved assignment; no CDC escalation is needed.

## Bubble-up To Arc06

The twelve-pair boundary, 335 outside pairs and existing Slice17/later-family
owners remain unchanged. R1-R3 are replay-contract repairs, not a new arc
capability or authority decision. P-15, CDC composition and UAT stay open.
The current correction assignment is `cc-prompt-iteration01.md` in this slice
root; CRC will independently replay the returned endpoint before any coverage
transfer or successor opening.
