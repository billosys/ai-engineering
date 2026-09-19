# Slice16 CRC Verification

Current verdict: **accepted after Iteration01**. This is independent CRC review
of the Slice16 packet, not CDC arc composition or Operator acceptance. Exactly
twelve bounded pairs enter accepted coverage once; live coverage becomes
220 accepted / 335 remaining / zero assigned. Slice17 remains held for CDC
sizing.

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

## Iteration01 Independent Review

Date: 2026-09-18. Assignment: `cc-prompt-iteration01.md`. CC registry endpoint
`9c8ea3a228bc5991126b2a8daf2b1e0a154175fe`; independently selected recipe
endpoint `713b88607b86c92fbedb50461829f52b20939efe`; source endpoint
`ce3f77103eff5e07b3533a03c65f158684fc1039`. Both worktrees were clean at
review intake. The Iteration01 diff from `ac618e0f` to `713b8860` contains
exactly the three authorized repair files and passes `git diff --check`.

CRC extracted and executed the committed literal route against the separate
registry and recipe endpoints. It returned status 0 and independently
reproduced the 12-record census, kind counts `2/1/2/1/5/1`, two absent actor
parents, six null template children, four populated pilot supports, three YAML
errors, 15 no-frontmatter records and the bounded 2,054-record legacy absence.
The four populated records retained the exact support-local actor object
`{id: codex-cc, mode: agent-direct, role: extractor}` without propagation to
their subjects.

R1 passes. Independent registry inspection found all 45 evidence rows in
snapshot mode: 21 planning rows declare opening planning commit `3b7790f8`,
and 24 source rows declare source commit `ce3f7710`. The production replay
resolved hashes and ranges through those declared authorities. Its wrong-
authority mutation returned status 1.

R2 passes. Independent classification found exactly 42 numeric line ranges,
two exact `JSON document` descriptors and one exact inventory descriptor.
Unknown, misplaced, out-of-bounds and reversed mutations each returned status
1. No evidence row escaped classification.

R3 passes. The native no-match actor query returned the literal JSON array
`[]` with status 0 and a separately measured count of zero. Missing input
returned status 2. Foreign source and pre-Slice16 recipe endpoints also failed
closed with status 2.

All other negative controls returned status 1 as required: wrong YAML set,
invalid membership, dangling evidence, wrong hash, absence-as-null, wrong mode,
wrong role, swapped mode/role and support-to-subject propagation. The registry
SHA-256 is
`bc561a720c09e375614dea1fc8cdde0a52fab6336fd6a556eab14323bce94e37`.
These checks establish bounded evidence integrity and the recorded contextual
meanings; they do not adopt a schema, closed vocabulary, authority model or
memory/runtime behavior.

## Final Row Verdict

S16-1 through S16-6 are independently done. The initial R1-R3 findings remain
preserved above and are satisfied by Iteration01. The six supporting artifacts
and all issued prompts are present at their canonical paths; CC's correction
touched only the three permitted close/replay records. No supporting artifact,
deferral or no-op is silently omitted.

## Final Bubble-Up To Arc06

Slice16 delivers the approved twelve-pair complement without importing
Slice15 meanings mechanically. It adds bounded per-kind actor mode/role
evidence, not a global role vocabulary. Nothing found changes the approved
Arc06 capability or the owners of Slices04-11. Exact closure accounting is
555 full / 220 accepted / 335 remaining / zero assigned.

The slice confirms rather than resolves the planned next design gate: Slice17
still combines run, preparation, method, time, shared-reference and remaining
CQ provenance interfaces and must be split by CDC before execution. CRC will
raise that sizing question in the next arc-level escalation. P-15, source,
schema, runtime, package, memory and UAT gates remain open.
