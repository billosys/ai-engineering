# Slice15 closing report

Status: CC proposed-done; independent CRC verification and CDC composition
review required. This report is not an acceptance verdict.

## Assignment and result

Slice15 executed the initial `cc-prompt.md` for `actor.mode` and `actor.role`
across claim, competency-question, concept-card, and extraction-run records.
The exact eight pairs were preserved in the registry. The opening source was
clean at `76a69fd9c295e78f23faa651746c2e36646e0ebd`; the opening canonical
planning checkout was clean at `4db8d8829185ac8fa0a9d9c74783466cfd45682a`.

The six authorized output paths are the only intended planning changes:

1. `artifacts/semantic-membership.json`
2. `artifacts/semantic-evidence.md`
3. `artifacts/validation-evidence.md`
4. `artifacts/handoff.md`
5. `ledger.md`
6. `closing-report.md`

## Evidence summary

The frozen native inventory produced 37 selected parsed mappings: claim 1,
CQs 2, cards 31, and runs 3. Actor-parent states are 12 absent, four object
parents with null mode/role children, and 21 populated card actors. Populated
values are `agent-direct` and `extractor`; generated card IDs are four
`codex-cc` pilot records and 17 `codex` rich/teaching records. The legacy
untyped comparison is 2,054 records with absent actor parents. Three YAML
errors and 15 no-frontmatter records remain outside the selected parsed
denominator.

The semantic conclusion is deliberately narrow: preserve exact actor values,
record kind, family, and absent/null/populated state; keep CQ role arrays,
worker scopes, run actors, and card actors distinct; and defer global
vocabularies, inheritance, authority, and backfill rules. No schema, parser,
graph/runtime, extraction, memory, or UAT change was made.

## Validation and route status

`artifacts/validation-evidence.md` contains the literal Bash/jq/Git/shasum
route. It derives the census from the native inventory, validates all
registry hashes and source ranges, checks the opening coverage subset and
frozen transition counts, preserves the six-file fence, and exercises:

- populated card positive evidence;
- template object/null and synthetic absent-parent witnesses;
- wrong mode `human-assisted` and wrong role `validator` rejection;
- swapped mode/role rejection;
- absent-as-null rejection;
- wrong YAML-exclusion, dangling evidence, and invalid membership rejection;
- real no-match with status 0 and `[]`; and
- missing input with nonzero status.

The final report must record the actual precommit status, same-revision
wrapper preflight, stale valid-recipe rejection, missing-recipe rejection,
and separate committed CC/recipe replay. A status-0 replay is structural
evidence only; it does not accept semantic membership or close P-15.

Recorded route outcomes are: precommit status 0 at opening planning
`4db8d882`; same-revision wrapper status 0 at `CC_COMMIT=678a8c76`,
`REPLAY_COMMIT=678a8c76`; stale/foreign and missing recipe-path controls status
2; and separate committed replay status 0 at
`CC_COMMIT=678a8c76`, `REPLAY_COMMIT=89568110`. The separate endpoints are
distinct. The route derived 37 selected and 2,054 legacy records, 3 YAML
errors, and 15 no-frontmatter records; all requested negative controls
rejected and semantic acceptance remained unclaimed.

## Handoff and open gates

`artifacts/handoff.md` returns the eight observations to the Operator, gives
Slice16 an exact 12-pair comparison obligation, and retains run/preparation,
shared-reference, and remaining CQ questions for Slice17. P-15 and UAT remain
open. CRC must independently reproduce the route and review the evidence;
CDC must review composition and any bubble-up to Arc06. No successor slice,
coverage acceptance update, or schema decision is created by this report.
