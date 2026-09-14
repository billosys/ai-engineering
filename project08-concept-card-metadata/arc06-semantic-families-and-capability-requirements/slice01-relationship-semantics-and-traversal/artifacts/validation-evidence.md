# Slice01 Validation Evidence

From source cwd with Bash/jq:

```bash
set -euo pipefail
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
jq -e '(.memberships|length)==35 and ([.memberships[]|[.field_path,.record_kind]|join("\u0000")]|unique|length)==35' "$s/artifacts/semantic-membership.json"
jq -e '(.cases|length)==4 and all(.cases[];has("input") and has("path") and has("operation") and has("adapter") and has("expected") and has("observed") and has("limit"))' "$s/artifacts/query-cases.json"
jq empty "$s/artifacts/semantic-membership.json"; jq empty "$s/artifacts/query-cases.json"; git -C .worktrees/planning diff --check
```

The checks pass: 35 unique members, four diagnostic cases, valid JSON and no whitespace errors. Scope is 115 accepted / 35 assigned / 405 outside; CDC decides acceptance.

The following replay adds plan-derived membership, frozen-transition inclusion,
registered-hash, and preservation checks. Run it from the source checkout; it
uses Bash, jq 1.6, shasum and Git 2.39.5.

```bash
set -euo pipefail
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
t=.worktrees/planning/project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
expected=$(awk -F'`' '/^\| `/{print $2 "|" $4}' "$s/slice-plan.md" | sort -u)
actual=$(jq -r '.memberships[] | .field_path + "|" + .record_kind' "$s/artifacts/semantic-membership.json" | sort -u)
test "$(printf '%s\n' "$expected" | sed '/^$/d' | wc -l | tr -d ' ')" = 35
test "$expected" = "$actual"
jq -e --argjson actual "$(jq '[.memberships[] | [.field_path,.record_kind]]' "$s/artifacts/semantic-membership.json")" '
  . as $transition |
  ($transition.accepted_pairs | length) == 115 and
  ($transition.remaining_pairs | length) == 440 and
  ([ $actual[] as $pair | select(any($transition.remaining_pairs[]; . == $pair)) ] | length) == ($actual | length) and
  ([ $actual[] as $pair | select(any($transition.accepted_pairs[]; . == $pair)) ] | length) == 0
' "$t"
test "$(jq '.remaining_pairs | length' "$t")" = 440
test $((440 - 35)) = 405
while IFS=$'\t' read -r path digest; do
  test "$(shasum -a 256 "$path" | awk '{print $1}')" = "$digest"
done < <(jq -r '.evidence[] | [.path,.sha256] | @tsv' "$s/artifacts/semantic-membership.json")
jq -e '(.cases|length)==4 and all(.cases[]; has("input") and has("path") and has("operation") and has("adapter") and has("expected") and has("observed") and has("limit"))' "$s/artifacts/query-cases.json"
git -C .worktrees/planning diff --exit-code 355d037f -- project08-concept-card-metadata/arc01-metadata-research-and-requirements
git -C .worktrees/planning diff --check
```

The census is the frozen frontmatter inventory registered in
`semantic-membership.json`: it separates the legacy untyped lists, the
relationship-edge template/example roots, and concept-card reference variants.
The template is deliberately null/unassessed; the sole populated edge is
synthetic; all target truth and unresolved-anchor claims remain bounded.

## Iteration 01 Replay

Executed pre-commit from the source checkout with Bash, jq 1.6, shasum and Git
2.39.5. Opening planning head: `46f60e46`; packet preservation is fixed to
`355d037f -> 400b847a`. Model/effort is unavailable from repository state.

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
jq -e '([.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")]|length)==2054 and ([.records[]|select(.values|type=="object")|select(.record_kind=="concept-card")]|length)==31 and ([.records[]|select(.values|type=="object")|select(.record_kind=="relationship-edge")]|length)==2' "$i"
 jq -e 'all(.cases[]; has("input") and has("path") and has("operation") and has("expected") and has("observed"))' "$s/artifacts/query-cases.json"
 jq -e '.cases[0].expected==.cases[0].observed and .cases[1].expected==.cases[1].observed and .cases[2].expected==.cases[2].observed and .cases[3].expected==.cases[3].observed' "$s/artifacts/query-cases.json"
test -f /Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/meter.md
test ! -e records/edge-evidence-map-related-to-claim.md
test ! -e records/support-synthetic-edge-001.md
git -C .worktrees/planning diff --exit-code 355d037f 400b847a -- project08-concept-card-metadata/arc01-metadata-research-and-requirements project08-concept-card-metadata/artifacts
git -C .worktrees/planning diff --check
```

All assertions passed pre-commit. Detailed field type/shape/value counts and
named reads are in `semantic-evidence.md`; they are not the 35 membership count.
