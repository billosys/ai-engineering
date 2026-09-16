# Worked replay: committed authority and native query

Status: CC proposed-done pending independent CDC verification. Run the fenced
block from the source checkout. In committed mode CDC must extract the block
from the claimed endpoint with `git show`, rather than executing a later
working-tree copy:

```bash
CC_COMMIT=<slice03-commit>
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning show "$CC_COMMIT:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice03-provenance-and-shared-reference-contracts/artifacts/worked-replay.md" |
  awk '/^~~~bash$/{p=1;next} /^~~~$/{if(p){exit}} p' |
  CC_COMMIT="$CC_COMMIT" bash
```

The route also supports `CC_PRECOMMIT=1` after the five files are staged. That
mode checks the union of unstaged tracked changes, staged tracked changes and
the explicitly named new outputs. It does not pretend an uncommitted endpoint
is a commit.

## Pinned inputs and prerequisites

- Source cwd: `/Users/oubiwann/lab/billosys/ai-engineering`; opening HEAD
  `e763c661592ff1097a94bb470db9cf924524579d`, initially clean.
- Planning cwd: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`;
  opening HEAD `ba2dbfd0a30ca4b0fad406d796efc7f54c76e5b6`, initially clean.
- Historical authority: Slice02 CC commit
  `753bacb051c041a75d0c4d36595cfbadd5a9b5eb`.
- Frozen inventory: `project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json`,
  SHA-256 `afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.
- Tools: Bash, jq, rg, shasum, cmp, awk, sed and Git; no new helper/parser,
  Ruby, Python, extraction, package, source-skill or runtime work.

## Case 1: committed authority versus live status

The route reads Slice02's plan, ledger and current-coverage register from the
explicit historical commit with `git show`. Their recorded snapshot digests
are, respectively:

```text
slice-plan.md       89ea7c74b6c806471ce4b1bd2243ebb9d502814e9068c34c8c25f2cadd48a151
ledger.md           31ad0696d41dae69d5e3c9394b91fd9b3799e9e7f2f8dc57ff9c507b7eee9660
semantic-coverage   770b0ea12ff8b260ce10b9cb5fea9a5c63e119993195111176bd6d4889568a03
```

The route checks those exact bytes against the explicit commit. It then reads
the current planning files live, computes their current digests, checks the
current coverage artifact's own purpose and values (`180` accepted, `375`
remaining, `0` assigned), and confirms the three current files differ from the
historical bytes. This demonstrates review/coverage advancement without using
a stale digest as the meaning of current status.

Controls:

- A deliberately wrong digest is passed to `cmp`; its status is `1`, a
  comparison failure.
- An invalid Git commit/path is requested with `git show`; its status is `128`
  and stderr is non-empty, a Git/input error.

Neither control is classified as semantic absence. Hashes establish byte
identity only; the live coverage purpose check is a bounded status observation.

## Case 2: native query versus authored expectation

The exact legacy question lookup reuses the accepted frozen inventory values:

```text
What are the different types of accent in music?
What is a behaviour in OTP?
```

The independently authored expected result is:

```json
{
  "music": {"question": "What are the different types of accent in music?", "matches": [{"path": "/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/accent-types.md", "slug": "accent-types", "concept": "Accent Types"}]},
  "erlang": {"question": "What is a behaviour in OTP?", "matches": [{"path": "knowledge/erlang/concept-cards/otp-design-principles/behaviour.md", "slug": "behaviour", "concept": "Behaviour"}]}
}
```

The observed object is computed by running the same parameterized `jq`
selection over the frozen inventory. The route compares parsed JSON with
`jq -S`, then reverses object key order and confirms the structurally equal
object still passes. It never uses the authored expected object as observed.

The same native inventory read derives the current CQ tuple from the rich
profile card:

```json
{"id":"cq-inspect-support-for-card-statement","path":"records/cq-inspect-support-for-card-statement.md","revision":1}
```

Its selected parent-state observation retains the distinctions
`answer_criteria: missing`, `memory_admission_ref: null`, and
`preservation_refs: empty`. The route compares that native object with an
independently authored tuple/state expectation structurally.

Controls:

- The same legacy lookup with the wrong question returns `[]`, status `0`,
  and is a successful no-match.
- The same CQ comparison with an altered expected ID returns comparison
  status `1`.
- The same CQ comparison with revision `99` returns comparison status `1`.
- The same legacy lookup against a missing inventory path returns jq status
  `2` with stderr, an execution/input error.

These controls preserve the distinction among match, successful no-match,
wrong expected value and tool error. They do not establish answer adequacy,
source support, semantic verification, reconciliation, preservation, memory
admission or schema conformance.

## Literal route

~~~bash
set -euo pipefail

source=/Users/oubiwann/lab/billosys/ai-engineering
plan=$source/.worktrees/planning
cd "$source"
s=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice03-provenance-and-shared-reference-contracts
slice02=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
opening_source=e763c661592ff1097a94bb470db9cf924524579d
opening_planning=ba2dbfd0a30ca4b0fad406d796efc7f54c76e5b6
historical=753bacb051c041a75d0c4d36595cfbadd5a9b5eb
historical_plan=89ea7c74b6c806471ce4b1bd2243ebb9d502814e9068c34c8c25f2cadd48a151
historical_ledger=31ad0696d41dae69d5e3c9394b91fd9b3799e9e7f2f8dc57ff9c507b7eee9660
historical_coverage=770b0ea12ff8b260ce10b9cb5fea9a5c63e119993195111176bd6d4889568a03
inventory_sha=afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b
cc_commit=${CC_COMMIT:-}
precommit=${CC_PRECOMMIT:-}
tmp=$(mktemp -d /private/tmp/cc-slice03-replay.XXXXXX)
trap 'rm -rf "$tmp"' EXIT

test "$(git -C "$source" rev-parse "$opening_source")" = "$opening_source"
test "$(git -C "$plan" rev-parse "$opening_planning")" = "$opening_planning"
test "$(shasum -a 256 "$source/$i"|awk '{print $1}')" = "$inventory_sha"
printf 'source=%s planning_opening=%s\n' "$(git -C "$source" rev-parse HEAD)" "$opening_planning"
printf 'bash=%s jq=%s rg=%s\n' "$(bash --version|head -1)" "$(jq --version)" "$(rg --version|head -1)"

expected_files=$(printf '%s\n' \
  "$s/artifacts/evidence-replay-contract.md" \
  "$s/artifacts/worked-replay.md" \
  "$s/artifacts/handoff.md" \
  "$s/ledger.md" \
  "$s/closing-report.md" | sort)
if [ -n "$precommit" ]; then
  test -z "$cc_commit"
  actual_files=$( { git -C "$plan" diff --name-only "$opening_planning" --; git -C "$plan" diff --cached --name-only "$opening_planning" --; git -C "$plan" ls-files --others --exclude-standard; } | sort -u )
  test "$expected_files" = "$actual_files"
  git -C "$plan" diff --check "$opening_planning" --
  git -C "$plan" diff --cached --check
  printf 'scope=precommit staged-unstaged-new-output-union\n'
else
  cc_commit=${cc_commit:-$(git -C "$plan" rev-parse HEAD)}
  git -C "$plan" cat-file -e "$cc_commit^{commit}"
  actual_files=$(git -C "$plan" diff --name-only "$opening_planning" "$cc_commit" -- | sort)
  test "$expected_files" = "$actual_files"
  git -C "$plan" diff --check "$opening_planning" "$cc_commit"
  printf 'scope=committed endpoint=%s\n' "$cc_commit"
fi
test "$(git -C "$source" status --porcelain)" = ""

# Case 1: read historical planning authority from explicit Git bytes.
hist_dir=$tmp/historical
mkdir "$hist_dir"
hist_plan=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/slice-plan.md
hist_ledger=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/ledger.md
hist_coverage=project08-concept-card-metadata/artifacts/semantic-coverage-current.json
git -C "$plan" show "$historical:$hist_plan" > "$hist_dir/plan"
git -C "$plan" show "$historical:$hist_ledger" > "$hist_dir/ledger"
git -C "$plan" show "$historical:$hist_coverage" > "$hist_dir/coverage"
test "$(shasum -a 256 "$hist_dir/plan"|awk '{print $1}')" = "$historical_plan"
test "$(shasum -a 256 "$hist_dir/ledger"|awk '{print $1}')" = "$historical_ledger"
test "$(shasum -a 256 "$hist_dir/coverage"|awk '{print $1}')" = "$historical_coverage"
printf 'historical.plan.sha256=%s\n' "$historical_plan"
printf 'historical.ledger.sha256=%s\n' "$historical_ledger"
printf 'historical.coverage.sha256=%s\n' "$historical_coverage"

live_plan=$plan/$hist_plan
live_ledger=$plan/$hist_ledger
live_coverage=$plan/$hist_coverage
live_plan_sha=$(shasum -a 256 "$live_plan"|awk '{print $1}')
live_ledger_sha=$(shasum -a 256 "$live_ledger"|awk '{print $1}')
live_coverage_sha=$(shasum -a 256 "$live_coverage"|awk '{print $1}')
test "$live_plan_sha" != "$historical_plan"
test "$live_ledger_sha" != "$historical_ledger"
test "$live_coverage_sha" != "$historical_coverage"
jq -e '(.artifact_kind=="current-semantic-coverage") and (.meaning|contains("Current accepted inventory interpretation"))' "$live_coverage" >/dev/null
jq -e '.counts.accepted==180 and .counts.remaining==375 and .counts.next_slice==0 and .counts.not_yet_sliced==375' "$live_coverage" >/dev/null
printf 'live.plan.sha256=%s\n' "$live_plan_sha"
printf 'live.ledger.sha256=%s\n' "$live_ledger_sha"
printf 'live.coverage.sha256=%s accepted=180 remaining=375 next_slice=0\n' "$live_coverage_sha"

set +e
printf '%s\n' wrong-digest | cmp -s "$hist_dir/plan" -
wrong_digest_status=$?
git -C "$plan" show "$historical:project08-concept-card-metadata/no-such-slice.md" > "$tmp/invalid.stdout" 2> "$tmp/invalid.stderr"
invalid_path_status=$?
set -e
test "$wrong_digest_status" = 1
test "$invalid_path_status" = 128
test ! -s "$tmp/invalid.stdout"
test -s "$tmp/invalid.stderr"
printf 'control.wrong-digest.status=%s classification=comparison_failure\n' "$wrong_digest_status"
printf 'control.invalid-git-path.status=%s classification=tool_error stderr_nonempty=true\n' "$invalid_path_status"

# Case 2: derive native legacy matches and one current CQ tuple.
music_q='What are the different types of accent in music?'
erlang_q='What is a behaviour in OTP?'
music_native=$(jq -c --arg q "$music_q" '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|select(.values.answers_questions?|index($q))|{path,slug:.values.slug,concept:.values.concept}]' "$source/$i")
erlang_native=$(jq -c --arg q "$erlang_q" '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|select(.values.answers_questions?|index($q))|{path,slug:.values.slug,concept:.values.concept}]' "$source/$i")
expected_legacy=$(jq -c -n --arg mq "$music_q" --arg eq "$erlang_q" '{music:{question:$mq,matches:[{path:"/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/accent-types.md",slug:"accent-types",concept:"Accent Types"}]},erlang:{question:$eq,matches:[{path:"knowledge/erlang/concept-cards/otp-design-principles/behaviour.md",slug:"behaviour",concept:"Behaviour"}]}}')
observed_legacy=$(jq -c -n --arg mq "$music_q" --arg eq "$erlang_q" --argjson mm "$music_native" --argjson em "$erlang_native" '{music:{question:$mq,matches:$mm},erlang:{question:$eq,matches:$em}}')
jq -n -e --argjson e "$expected_legacy" --argjson o "$observed_legacy" '$e==$o' >/dev/null
reordered_legacy=$(printf '%s' "$observed_legacy"|jq -c 'to_entries|reverse|from_entries')
jq -n -e --argjson a "$observed_legacy" --argjson b "$reordered_legacy" '$a==$b' >/dev/null
printf 'case2.legacy.expected=%s\n' "$expected_legacy"
printf 'case2.legacy.observed=%s\n' "$observed_legacy"
printf 'case2.legacy.reordered_keys=structurally_equal\n'

cq_path=knowledge/concept-cards/examples/rich-profile-card.md
cq_native=$(jq -c --arg p "$cq_path" '.records[]|select(.path==$p)|.values.cq_refs[0]' "$source/$i")
cq_parent_native=$(jq -c --arg p "$cq_path" '.records[]|select(.path==$p)|.values|{answer_criteria:(if has("answer_criteria") then {state:"present",value:.answer_criteria} else {state:"missing"} end),memory_admission_ref:(if has("memory_admission_ref") then (if .memory_admission_ref==null then {state:"null",value:null} else {state:"present",value:.memory_admission_ref} end) else {state:"missing"} end),preservation_refs:(if has("preservation_refs") then (if (.preservation_refs|type)=="array" and (.preservation_refs|length)==0 then {state:"empty",value:[]} else {state:"present",value:.preservation_refs} end) else {state:"missing"} end)}' "$source/$i")
expected_cq=$(jq -c -n '{tuple:{id:"cq-inspect-support-for-card-statement",path:"records/cq-inspect-support-for-card-statement.md",revision:1},parent_state:{answer_criteria:{state:"missing"},memory_admission_ref:{state:"null",value:null},preservation_refs:{state:"empty",value:[]}}}')
observed_cq=$(jq -c -n --argjson tuple "$cq_native" --argjson state "$cq_parent_native" '{tuple:$tuple,parent_state:$state}')
jq -n -e --argjson e "$expected_cq" --argjson o "$observed_cq" '$e==$o' >/dev/null
printf 'case2.cq.expected=%s\n' "$expected_cq"
printf 'case2.cq.observed=%s\n' "$observed_cq"

wrong_question=$(jq -c --arg q 'What are the different types of accent in jazz?' '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|select(.values.answers_questions?|index($q))|{path,slug:.values.slug,concept:.values.concept}]' "$source/$i")
jq -n -e --argjson actual "$wrong_question" '$actual==[]' >/dev/null
wrong_id_expected=$(jq -c -n '{id:"cq-inspect-support-for-card-statement-wrong",path:"records/cq-inspect-support-for-card-statement.md",revision:1}')
wrong_revision_expected=$(jq -c -n '{id:"cq-inspect-support-for-card-statement",path:"records/cq-inspect-support-for-card-statement.md",revision:99}')
if jq -n -e --argjson e "$wrong_id_expected" --argjson o "$cq_native" '$e==$o' >/dev/null; then wrong_id_status=0; else wrong_id_status=$?; fi
if jq -n -e --argjson e "$wrong_revision_expected" --argjson o "$cq_native" '$e==$o' >/dev/null; then wrong_revision_status=0; else wrong_revision_status=$?; fi
test "$wrong_id_status" = 1
test "$wrong_revision_status" = 1
set +e
jq -c --arg q "$music_q" '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|select(.values.answers_questions?|index($q))|{path,slug:.values.slug,concept:.values.concept}]' "$tmp/no-such-inventory.json" > "$tmp/missing.stdout" 2> "$tmp/missing.stderr"
missing_status=$?
set -e
test "$missing_status" = 2
test ! -s "$tmp/missing.stdout"
test -s "$tmp/missing.stderr"
printf 'control.wrong-question.stdout=[] status=0 classification=successful_no_match\n'
printf 'control.wrong-cq-id.status=%s classification=comparison_failure\n' "$wrong_id_status"
printf 'control.wrong-cq-revision.status=%s classification=comparison_failure\n' "$wrong_revision_status"
printf 'control.missing-inventory.status=%s classification=tool_error stderr_nonempty=true\n' "$missing_status"

# Protected history and no silent source/planning edits outside the five paths.
protected=(
  project08-concept-card-metadata/artifacts/semantic-coverage-current.json
  project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/cdc-verification.md
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/cdc-verification.md
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/cdc-verification.md
)
if [ -z "$precommit" ]; then
  for p in "${protected[@]}"; do git -C "$plan" diff --exit-code "$opening_planning" "$cc_commit" -- "$p"; done
fi
printf 'json=structural-comparisons-pass\nprotected-history=unchanged\nsource-status=clean\n'
~~~

The final committed replay prints the actual endpoint and tool versions,
historical/live digests, both expected/observed JSON objects, every control
status, protected-history result and the exact five-file scope. CDC must rerun
that committed block independently; this CC route does not create
`cdc-verification.md` or accept any semantic pairs.
