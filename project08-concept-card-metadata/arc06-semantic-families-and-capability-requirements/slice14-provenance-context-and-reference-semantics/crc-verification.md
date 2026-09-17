# Slice14 CRC Verification: Changes Required

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

## Row Disposition And Handoff

S14-1, S14-4 and S14-6 have no finding in this review, but the slice is not
partially accepted. S14-2, S14-3 and S14-5 need correction and fresh replay.
The CC report remains proposed-done historical attestation, not an accepted
close. No coverage register, source skill, schema, runtime, prior packet or
Slice15 was changed. The same acceptance contract suffices for these repairs;
no CDC escalation is needed. Assignment:
`cc-prompt-iteration02.md` in this slice root. After CC returns, CRC must
independently replay the corrected packet and issue a new verdict before
acceptance or advancement.
