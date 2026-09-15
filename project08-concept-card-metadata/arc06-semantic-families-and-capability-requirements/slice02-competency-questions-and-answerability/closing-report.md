# CC Proposed-Done: Arc06 Slice02 Iteration 01 Repair

Status: proposed-done for the Iteration 01 repair, pending independent CDC
verification. This report closes the CC repair pass only; it is not schema
acceptance, source-truth acceptance, extraction-quality acceptance, operator
quality approval, or memory admission. CDC owns independent closure of all six
rows.

## Pinned opening and scope

- Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`, opening
  `e763c661592ff1097a94bb470db9cf924524579d`, initially clean and preserved.
- Planning checkout: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`,
  opening `a27c4d33a02d3e6047656b9ae0c17a145aa3f208`, initially clean.
- Original CC endpoint retained: `753bacb051c041a75d0c4d36595cfbadd5a9b5eb`.
- Repair opening: `f15c896bfeec4c3618387413e63c95dfe9fc6771`; this is the
  reviewed planning state from which the seven-file repair began.
- Frozen authority inputs: slice plan bytes at
  `a27c4d33a02d3e6047656b9ae0c17a145aa3f208` and pre-review ledger bytes at
  `753bacb051c041a75d0c4d36595cfbadd5a9b5eb`. Live plan/ledger status is
  reported separately and is not used to refresh those historical hashes.
- Repair endpoint: the planning commit containing this exact report and the
  other six permitted files. The published replay resolves it from
  `CC_COMMIT`; CDC must set `CC_COMMIT` to that committed SHA and record its
  own verification separately.
- Current accounting preserved: 150 accepted, 405 remaining, 30 assigned to
  Slice02, and 375 outside. The immutable transition snapshot remains
  historical 115/440/35.
- No plans, other slices, source files, frozen inventory, current coverage
  register, transition snapshot, package/runtime surfaces, or CDC artifact was
  edited.

## Row closure

Rows S2-2, S2-3, S2-4 and S2-6 are `done (CC-attested/proposed-done)` and
remain pending independent CDC closure; S2-1 and S2-5 retain their recorded
independent CDC closure. The repaired rows are not marked independently done.

| Row | CC result | Evidence |
| --- | --- | --- |
| S2-1 | The plan-derived 30 pairs are exact and unique, remain included in the 405 remaining set, disjoint from the 150 accepted set, and leave 375 outside. | `artifacts/semantic-membership.json`; `artifacts/validation-evidence.md` |
| S2-2 | Repair R1 corrects the six-family root census to 8 absent / 5 empty / 18 populated `cq_refs`, identifies the three malformed rich cards (excluding the non-card INDEX), and registers both original/copy model-data-constraints witnesses and manifests. | `artifacts/semantic-evidence.md`; `artifacts/semantic-membership.json`; `artifacts/validation-evidence.md` |
| S2-3 | Repair R3 distinguishes required answer components, mapped construct references, coverage-assertion identity and assertion rationale; the template null component slot and synthetic `component_refs` list do not establish a populated assertion encoding or schema equivalence. | `artifacts/semantic-membership.json`; `artifacts/semantic-evidence.md`; `artifacts/validation-evidence.md` |
| S2-4 | Repair R2 derives all four native comparisons from registered inventory/card text, captures bounded lookup outputs/statuses, preserves the missing-parent and rg exit-2 distinctions, and rejects altered expected IDs/revisions. | `artifacts/query-cases.json`; `artifacts/validation-evidence.md` |
| S2-5 | The handoff preserves concrete research, shared-reference, lifecycle and P-15 questions, names outside owners, and supplies re-entry questions without choosing a schema or absorbing adjacent pairs. | `artifacts/handoff.md` |
| S2-6 | Repair R4 pins historical plan/ledger authority and the original CC endpoint, while the designated replay covers exact scope, accounting, 29 evidence hashes plus baseline manifests/mappings, full census, native cases and controls, JSON, preservation, whitespace and exactly seven planning paths. | `artifacts/validation-evidence.md`; this report; `ledger.md` |

## Checks, failures and limits

The Iteration 01 pre-commit rehearsal is the required final check for this
report. While making the route literal and reproducible, it exposed and
corrected shell/fixture issues rather than weakening criteria: the plan-table
extractor initially retained header rows; compact JSON was required for
string-level comparisons; native generated answer text included terminal
periods absent from the independently authored expected object; and the
synthetic coverage assertion needed explicit field ordering. The final route
records the corrected commands and its result below after execution.

The designated route records the following bounded observations:

- Legacy census: Complete Musician 390 records/574 items/379 distinct strings;
  Erlang 1,664/4,059/3,265; total 2,054/4,633/3,644.
- Card census: 31 parsed cards across Arc07 expanded (6), Arc07 pilot (4),
  rich rerun (7), synthetic examples (3), teaching rerun (10), and template
  (1); two standalone CQ records; three malformed rich exclusions (memory
  forms, priming forms and recognition-dual-process).
- The 18 populated `cq_refs[]` items all request revision 1. The selected
  `competency_question_refs` root has no populated item, so no equivalence or
  requiredness is inferred.
- The rich-profile external target has a declared path whose parent directory
  is absent. The native bounded result is successful parent absence with an
  unresolved target; the separate rg missing-root control is the actual tool
  error. Neither is a semantic no-match.
- The three malformed rich inputs remain exclusions: missing opening
  frontmatter or frozen YAML parse failure. They are not negative CQ evidence.
- No rendered anchor, resolver, answer warrant, source-support edge, schema
  conformance, lifecycle result, or operator acceptance is claimed. The
  repair also does not claim that required answer components are populated
  merely because mapped constructs or a null template slot were observed.

## Artifact inventory and exact edit scope

The commit contains exactly these seven planning-root-relative paths:

1. `.../slice02-competency-questions-and-answerability/artifacts/semantic-membership.json`
2. `.../slice02-competency-questions-and-answerability/artifacts/semantic-evidence.md`
3. `.../slice02-competency-questions-and-answerability/artifacts/query-cases.json`
4. `.../slice02-competency-questions-and-answerability/artifacts/validation-evidence.md`
5. `.../slice02-competency-questions-and-answerability/artifacts/handoff.md`
6. `.../slice02-competency-questions-and-answerability/ledger.md`
7. `.../slice02-competency-questions-and-answerability/closing-report.md`

`cdc-verification.md` was intentionally not created. The packet uses existing
Bash, jq, rg, sed, awk, shasum and git routes; no new parser/helper or
Ruby/Python script was created.

## Bubble-up to Arc06

This packet delivers the assigned CQ capability analysis without changing the
Arc06 plan or current coverage. It bubbles up four concrete findings for later
research and P-15 discussion:

1. Legacy question text supports exact discovery, but equal text cannot by
   itself establish CQ identity, revision, origin, intended use or answer
   criteria.
2. `cq_refs` and `competency_question_refs` are observed as distinct surfaces;
   the frozen population does not establish migration equivalence.
3. External paths, embedded fragments, literal headings and rendered anchors
   need separate resolution policy; a missing parent path is not a semantic
   no-match.
4. Component roles, assertion-level coverage, answerability, retrieval,
   verification and admission carry different evidence burdens.

Outside owners retain actor/result/retrieval/admission/replacement and related
lifecycle pairs. P-15 must review any future canonical reference shape,
identity/deduplication rule, target-anchor policy, answer-criteria placement,
state vocabulary, schema language and specification before normative adoption.
No next-slice execution is authorized by this CC packet.

## CDC handoff

CDC should run the literal fenced block in `artifacts/validation-evidence.md`
from the declared source checkout with `CC_COMMIT` set to the actual repair
commit SHA, inspect the exact seven-file diff from the repair opening, confirm
the pinned authorities, source preservation and all registered hashes, and
write the separate CDC artifact only if the independent review accepts the
rows. Until then, the ledger remains CC-attested/proposed-done.
