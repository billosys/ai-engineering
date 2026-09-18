# Slice15 closing report

Status: CC proposed-done; independent CRC verification and CDC composition
review required. This report is not an acceptance verdict.

## Assignment and result

Slice15 executed the initial `cc-prompt.md` for `actor.mode` and `actor.role`
across claim, competency-question, concept-card, and extraction-run records.
The exact eight pairs were preserved in the registry. The authorized source
baseline is clean at `ce3f77103eff5e07b3533a03c65f158684fc1039`; the
iteration opening canonical planning checkout is clean at
`ea200f07c38c43b85991426804dea10a4e250743`. The registry rebases only the two
source evidence rows affected by the latest prompt-authorship changes; the
ontology-support source files and native inventory remain unchanged.

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
- wrong registered-hash and wrong YAML-exclusion candidate rejection;
- dangling evidence and invalid membership rejection;
- real no-match with status 0 and `[]`; and
- missing input with nonzero status.

The final report records the actual precommit status, same-revision wrapper
preflight, missing/foreign recipe-path rejection, and separate committed
CC/recipe replay. The older/opening endpoint checks returned status 2 because
no valid prior Slice15 recipe path existed; they are not a stale-valid-recipe
semantic rejection. A status-0 replay is structural evidence only; it does
not accept semantic membership or close P-15.

Iteration01 repairs are: the same 39-row hash predicate rejects a candidate
with exactly one wrong `projectLedger` SHA-256; the same exact-set YAML
predicate rejects a three-path candidate with one plausible nonexistent path;
and the endpoint wording now reports missing/foreign recipe-path status 2
without inventing a valid stale predecessor. The route continues to derive
37 selected and 2,054 legacy records, 3 YAML errors, and 15 no-frontmatter
records; semantic acceptance remains unclaimed.

## Handoff and open gates

`artifacts/handoff.md` returns the eight observations to the Operator, gives
Slice16 an exact 12-pair comparison obligation, and retains run/preparation,
shared-reference, and remaining CQ questions for Slice17. P-15 and UAT remain
open. CRC must independently reproduce the route and review the evidence;
CDC must review composition and any bubble-up to Arc06. No successor slice,
coverage acceptance update, or schema decision is created by this report.
