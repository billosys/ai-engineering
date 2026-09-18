# Slice14 CRC Verification

Current verdict: **accepted** after independent iteration03 review below. The
earlier changes-required findings remain as chronological review history.

Date: 2026-09-17. Reviewer: independent CRC context. CC endpoint:
`6003975321334a0ad554d92663836317b71bd6ce`; committed replay/attestation
follow-up: `ef61a57d636a04deabb9918be80c89ac04b49f14`. Source HEAD:
`020268248882358075b678bb855c0ac8d11b532a`. Governing slice plan at
review: 1.1. This is a CRC verdict, not CDC design approval or Operator
acceptance. No semantic pair is accepted and coverage remains 188/367/12/355.

## Independent Checks

- Inspected the six-file CC contribution and follow-up against the current
  project/arc/slice plans and ledgers. Source and planning checkouts were clean.
- Ran the literal Bash route extracted from the committed `60039753` recipe
  with `CC_COMMIT=60039753` and `REPLAY_COMMIT=60039753`. It exited 0, reported
  12 selected native mappings and 2,054 legacy mappings, rejected both wrong
  expectations and both registry mutations, distinguished no-match (`[]`,
  status 0) from missing input (status 2), and verified registered hashes.
- Independently read the source-support census and registry text, the frozen
  inventory error cells, the literal invocation and source-drift guards.
  Mechanical replay success is not semantic or contract acceptance.

## Findings

| ID | Row | Finding and evidence | Required correction |
| --- | --- | --- | --- |
| R1 | S14-3 | `semantic-membership.json` membership `actor.id`/`source-support` says "four template/null records" in `effective_meaning`. Its own `native_census.by_kind.source-support` is five records: four populated pilot supports and one template/null. The shared meaning and semantic report also say one. | Correct the member-specific statement and check all twelve effective meanings against the derived census and raw witnesses. Preserve the four populated values and single template null. |
| R2 | S14-5 | `validation-evidence.md` documents a separately pinned `REPLAY_COMMIT`, but its published command extracts executable code from the live working-tree Markdown. Inside that code it reads the `REPLAY_COMMIT` file into `recipe` and only checks presence; it never executes or compares the extracted committed recipe. Thus the advertised recipe endpoint is not the executed endpoint. | Make the documented committed invocation execute code extracted from `REPLAY_COMMIT`, or fail closed on an exact comparison before executing live code. Demonstrate a wrong/missing recipe endpoint rejection and a valid separate-revision replay. |
| R3 | S14-5 | The route requires current source HEAD to equal the opening source commit (`validation-evidence.md`, lines 84-85, 484), contrary to slice-plan lines 185-193 and the issued prompt, which explicitly allow an unrelated global HEAD advance when registered inputs and relevant paths are unchanged. | Remove the global HEAD equality gate; retain source cleanliness, relevant-path/registered-byte comparisons, and explicit old/current commit and hash reporting. Exercise a bounded unrelated-HEAD case without changing source files or weakening material-drift rejection. |
| R4 | S14-2, S14-5 | The route checks only authored parse-exclusion count, list length and prose. It does not derive the three excluded YAML-error paths from the frozen inventory and compare them to the authored list. An arbitrary three-path substitution would pass this check. The frozen inventory has exactly the three named rich-rerun YAML errors, distinct from no-frontmatter entries. | Derive the scoped YAML-error path set from pinned inventory error records; compare exact paths and count to the authored exclusions. Include a wrong-exclusion negative control, and retain error versus absence distinctions. |

## Iteration01 Row Disposition And Handoff

S14-1, S14-4 and S14-6 have no finding in this review, but the slice is not
partially accepted. S14-2, S14-3 and S14-5 need correction and fresh replay.
The CC report remains proposed-done historical attestation, not an accepted
close. No coverage register, source skill, schema, runtime, prior packet or
Slice15 was changed. The same acceptance contract suffices for these repairs;
no CDC escalation is needed. Assignment:
`cc-prompt-iteration02.md` in this slice root. After CC returns, CRC must
independently replay the corrected packet and issue a new verdict before
acceptance or advancement.

## Iteration02 Independent Review: Changes Required

Date: 2026-09-17. CC contribution `ee80f9149a8badaa998ef65e5b8e17239164cb5f`;
separate recipe `3372da88c5ed2d9d070a89974473532ff0f29e4a`; reviewed planning
HEAD `eab5e69c02afc1cce0cb983d8ba26f893a0902c0`; source HEAD
`76a69fd9c295e78f23faa651746c2e36646e0ebd`. Both checkouts were clean.
The CC contribution changed exactly the six allowed files.

I independently executed the literal recipe from `3372da88` against registry
`ee80f914`; it exited 0. It reproduced twelve selected mappings, 2,054
legacy mappings, 42 evidence hashes, three YAML-error exclusions and 15
no-frontmatter records. Wrong actor, absence/null, wrong-exclusion,
invalid-member and dangling-reference controls rejected; no-match returned
status 0 with `[]`, while missing inventory returned status 2. Current source
HEAD differs from opening HEAD but registered relevant source bytes still
matched. Native member and shared meanings now correctly say four populated
pilot supports and one template/null. R1-R4 from iteration01 are resolved
within their stated scope, not promoted to schema or operator acceptance.

**R5, S14-5: registered reading ranges exceed pinned inputs.** The registry's
`source_range` values are evidence-location claims required by slice-plan
lines 120-127. I resolved each row at its declared root, read mode and
authority commit and compared the largest cited line to the file length:

| Evidence ID | Registered range | Pinned file lines |
| --- | --- | ---: |
| `projectLedger` | `lines 1-45` | 43 |
| `slicePlan` | `lines 17-225` | 223 |
| `assignmentPrompt` | `lines 1-236` | 72 |
| `slice03ReplayContract` | `lines 1-100` | 93 |

The other numeric ranges are in bounds. The literal route never reads
`source_range`, so a whole-file hash pass cannot catch these false reading
locations. Correct the four registrations against the pinned bytes and add a
fail-closed line-range check over all 42 evidence rows with an out-of-bounds
negative control. Preserve non-line `JSON document` range descriptions.

S14-1 through S14-4 and S14-6 have no remaining finding in this review, but
the slice is not partially accepted. S14-5 remains changes-required, and no
semantic pair or coverage row is accepted. This is a bounded correction within
the existing evidence-integrity criterion, not a new scope or schema rule.
The next preserved CC assignment is `cc-prompt-iteration03.md`; CRC will
independently replay the corrected endpoint before closure. Slice15 remains
unopened pending Slice14 closure and CDC-governed sizing.

## Iteration03 Independent Review: Accepted

Date: 2026-09-17. CC contribution `b10bb1ec`; separately committed recipe
`a4a7047c`; planning HEAD at review `d38fc3edc8e3f004b3c7d573f6a555c3e4d5b4fb`;
source HEAD `76a69fd9c295e78f23faa651746c2e36646e0ebd`.
Both worktrees were clean before CRC's planning updates. The contribution
changed exactly the six authorized files; whitespace checks passed.

I extracted and executed the literal recipe from the committed recipe
revision with `CC_COMMIT=b10bb1ec`. It exited 0 and independently reproduced
the twelve selected mappings, 2,054 legacy mappings, 42 registered hashes,
42 resolved reading ranges, three frozen YAML-error exclusions and 15
no-frontmatter records. I also resolved each numeric `source_range` against
its registered root, read mode and authority commit. The four previously
invalid ranges now end within the pinned files: `projectLedger` lines 1-43,
`slicePlan` lines 1-249, `assignmentPrompt` lines 1-247, and
`slice03ReplayContract` lines 1-93. Non-line JSON and multi-span descriptors
retain their explicit interpretation. R5 is resolved.

Native positive cases and wrong-actor, absence/null, invalid-member,
dangling-reference, YAML-exclusion, out-of-bounds and reversed-range controls
produced the expected distinct outcomes. No-match returned `[]` with status
0; missing input returned status 2. The older recipe revision `8e6b6770`
was rejected with status 1, and a missing recipe at `2fa4c2a5` with status
2. Source HEAD had advanced from the opening commit, but registered relevant
source bytes matched; no global-HEAD-equality assertion was used. The
membership meanings remain bounded to observed contexts and retain identity,
subject, source and authority distinctions. Mechanical checks are evidence
for this bounded semantic disposition, not schema or runtime validation.

| Row | CRC disposition |
| --- | --- |
| S14-1 | Done: exact twelve-pair set, accepted-set disjointness, frozen inclusion and 355 outside pairs reproduced. |
| S14-2 | Done: selected native census and frozen parse-error/no-frontmatter, parent-absent/child-null distinctions reproduced. |
| S14-3 | Done: member and shared meanings were inspected against the bounded populated/template witnesses; no cross-kind principal equivalence is asserted. |
| S14-4 | Done: native diagnostics, negative controls, successful no-match and real error remain distinct. |
| S14-5 | Done: committed replay, 42 hashes/ranges, mutation and endpoint controls, preservation, exact file scope and whitespace passed. |
| S14-6 | Done: handoff preserves broader provenance, unresolved identity/authority questions, all 355 outside pairs and P-15 without opening or deciding Slice15. |

The CC closing report lacks a separately titled bubble-up section, but its
row walk and handoff preserve the substantive unresolved questions. This is
a non-blocking report-format gap, not a missing semantic or ownership gate.
CRC accepts all six rows and transfers exactly twelve pairs to accepted
coverage: 200 accepted / 355 remaining / zero assigned. This is independent
slice verification, not CDC arc composition, schema adoption, memory admission
or Operator acceptance.

### Bubble-up To Arc06

Slice15 remains unsized. Its 20 actor.mode/actor.role pairs, remaining
run/preparation/method/shared-reference responsibilities and CQ provenance
interfaces still have Arc06 ownership. The next structural sizing decision
belongs to CDC through a preserved CRC escalation; no successor slice or
implementation prompt is opened by this verdict.
