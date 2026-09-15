# Slice02 validation evidence

This is the designated current replay for the CC packet. It is CC-attested until
CDC reruns it independently.

Opening source HEAD: e763c661592ff1097a94bb470db9cf924524579d
Opening planning HEAD: a27c4d33a02d3e6047656b9ae0c17a145aa3f208
Source cwd: /Users/oubiwann/lab/billosys/ai-engineering
Planning cwd: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
Model, settings, effort and compaction: unknown; no settings changed.
The route uses /bin/bash, jq, shasum, rg, awk, sed and git, with no new
parser/helper. The command prints tool versions. Set CC_COMMIT for CDC;
otherwise the route uses the current planning HEAD.

~~~bash
set -euo pipefail
source=/Users/oubiwann/lab/billosys/ai-engineering
plan=$source/.worktrees/planning
cd "$source"
s=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
c=.worktrees/planning/project08-concept-card-metadata/artifacts/semantic-coverage-current.json
m=.worktrees/planning/$s/artifacts/semantic-membership.json
q=.worktrees/planning/$s/artifacts/query-cases.json
opening_source=e763c661592ff1097a94bb470db9cf924524579d
opening_planning=a27c4d33a02d3e6047656b9ae0c17a145aa3f208
cc_commit=$(git -C "$plan" rev-parse HEAD)
if printenv CC_COMMIT >/dev/null 2>&1; then cc_commit=$(printenv CC_COMMIT); fi
test "$(git -C "$source" rev-parse "$opening_source")" = "$opening_source"
test "$(git -C "$plan" rev-parse "$opening_planning")" = "$opening_planning"
printf 'source=%s planning_opening=%s planning_endpoint=%s\n' "$(git -C "$source" rev-parse HEAD)" "$opening_planning" "$cc_commit"
printf 'bash=%s jq=%s rg=%s\n' "$(bash --version|head -1)" "$(jq --version)" "$(rg --version|head -1)"

# Exact scope and current accounting. The plan table is pipe-delimited; \140
# is the shell-safe backtick character used to remove its YAML backticks.
expected=$(sed -n 's/^| \([^|]*\) | \([^|]*\) |$/\1|\2/p' "$plan/$s/slice-plan.md"|tr -d '\140'|sed '/^Field path|/d;/^---|/d'|sort -u)
actual=$(jq -r '.memberships[]|.field_path+"|"+.record_kind' "$plan/$s/artifacts/semantic-membership.json"|sort -u)
test "$(printf '%s\n' "$expected"|sed '/^$/d'|wc -l|tr -d ' ')" = 30
test "$expected" = "$actual"
pairs=$(jq '[.memberships[]|[.field_path,.record_kind]]' "$m")
jq -e --argjson a "$pairs" '. as $r|
  ($r.accepted_pairs|length)==150 and ($r.remaining_pairs|length)==405 and
  $r.counts.next_slice==30 and $r.counts.not_yet_sliced==375 and
  ([ $a[] as $p|select(any($r.remaining_pairs[];.==$p)) ]|length)==($a|length) and
  ([ $a[] as $p|select(any($r.accepted_pairs[];.==$p)) ]|length)==0' "$c"
test $((405-30)) = 375

# Registry referential integrity and every registered hash.
jq -e '. as $r|(.memberships|length)==30 and
  all(.memberships[];.meaning_id as $m|$r.meanings|has($m)) and
  all(.memberships[].evidence_ids[];. as $id|$r.evidence|has($id))' "$m"
while IFS=$'\t' read -r id root path digest; do
  case "$root" in source) file="$source/$path";; planning) file="$plan/$path";; absolute) file="$path";; *) exit 1;; esac
  test "$(shasum -a 256 "$file"|awk '{print $1}')" = "$digest"
  printf 'hash-ok=%s\n' "$id"
done < <(jq -r '.evidence|to_entries[]|[.key,.value.root,.value.path,.value.sha256]|@tsv' "$m")

# Full census: legacy, six card families, malformed rich exclusions, two CQs.
legacy=$(jq -c '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|.+{family:(if (.path|contains("complete-musician")) then "music" else "erlang" end)}]|group_by(.family)|map(. as $r|{family:$r[0].family,records:($r|length),present:([$r[]|select(.values|has("answers_questions"))]|length),items:([$r[]|.values.answers_questions[]]|length),distinct:([$r[]|.values.answers_questions[]]|unique|length)})' "$i")
printf 'legacy_census=%s\n' "$legacy"
test "$legacy" = '[{"family":"erlang","records":1664,"present":1664,"items":4059,"distinct":3265},{"family":"music","records":390,"present":390,"items":574,"distinct":379}]'
test "$(jq -c '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|.values.answers_questions[]]|{records:2054,items:length,distinct:(unique|length)}' "$i")" = '{"records":2054,"items":4633,"distinct":3644}'
card_count=$(jq '[.records[]|select(.record_kind=="concept-card")]|length' "$i")
cq_count=$(jq '[.records[]|select(.record_kind=="competency-question")]|length' "$i")
bad_rich=$(jq '[.records[]|select(.error!=null)|select(.path|test("compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-.*\\.md$"))]|length' "$i")
test "$card_count" = 31; test "$cq_count" = 2; test "$bad_rich" = 3
jq -e '. as $r|
  ([.records[]|select(.record_kind=="concept-card")|.path]|length)==31 and
  ([.records[]|select(.record_kind=="concept-card")|.values.cq_refs[]?]|length)==18 and
  ([.records[]|select(.record_kind=="concept-card")|select(.values|has("competency_question_refs"))]|length)==1 and
  ([.records[]|select(.record_kind=="competency-question")|.values]|any(.question=="Can a reviewer locate the source support for a claim?"))' "$i"

# Case 1: native legacy reverse lookup; wrong value is no-match, missing input is error.
music=$(jq -c --arg q 'What are the different types of accent in music?' '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|select(.values.answers_questions?|index($q))|{path,slug:.values.slug,concept:.values.concept}]' "$i")
erlang=$(jq -c --arg q 'What is a behaviour in OTP?' '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|select(.values.answers_questions?|index($q))|{path,slug:.values.slug,concept:.values.concept}]' "$i")
test "$music" = "$(jq -c '.cases[0].expected.music.matches' "$q")"; test "$music" = "$(jq -c '.cases[0].observed.music.matches' "$q")"
test "$erlang" = "$(jq -c '.cases[0].expected.erlang.matches' "$q")"; test "$erlang" = "$(jq -c '.cases[0].observed.erlang.matches' "$q")"
if jq --arg q 'What are the different types of accent in jazz?' '.records[]' "$i" >/dev/null; then wrong=0; else wrong=$?; fi
test "$wrong" = 0
if jq -e '.records[]' /private/tmp/cc-slice02-no-such-inventory.json >/dev/null 2>&1; then error=0; else error=$?; fi
test "$error" = 2

# Case 2: rich external tuple; the native parent-path lookup is a path error.
rich=knowledge/concept-cards/examples/rich-profile-card.md
rg -q -F 'id: cq-inspect-support-for-card-statement' "$rich"
rg -q -F 'path: records/cq-inspect-support-for-card-statement.md' "$rich"
test ! -d knowledge/concept-cards/examples/records
rich_native=$(jq -c -n '{declared:{id:"cq-inspect-support-for-card-statement",revision:1,path:"records/cq-inspect-support-for-card-statement.md"},declaration_present:true,target_lookup:{status:1,classification:"path_error_missing_parent",target_available:"unresolved"},identity_revision:"declared_only",answerability:"unassessed"}')
test "$rich_native" = "$(jq -c '.cases[1].expected' "$q")"; test "$rich_native" = "$(jq -c '.cases[1].observed' "$q")"
if rg -l -F 'cq-inspect-support-for-card-statement-wrong' knowledge/concept-cards >/dev/null 2>&1; then wrong=0; else wrong=$?; fi
test "$wrong" = 1
if rg -l -F 'cq-inspect-support-for-card-statement' knowledge/concept-cards/no-such-root >/dev/null 2>&1; then error=0; else error=$?; fi
test "$error" = 2

# Case 3: embedded generated CQ; fragment, literal heading and text are separate.
tick=$(printf '\x60')
rr=workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
tr=workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
rich_heading=$(printf '### CQ %scq-model-constraint-trust%s' "$tick" "$tick")
teaching_heading=$(printf '### CQ %scq-model-data-constraint%s' "$tick" "$tick")
rg -q -F 'cq_refs: [{id: cq-model-constraint-trust, revision: 1, path: "#cq-model-constraint-trust"}]' "$rr"
rg -q -F "$rich_heading" "$rr"
rg -q -F 'cq_refs: [{id: cq-model-data-constraint, revision: 1, path: "#cq-model-data-constraint"}]' "$tr"
rg -q -F "$teaching_heading" "$tr"
rq=$(sed -n '124,125p' "$rr"|paste -sd ' ' -); ra=$(sed -n '127,128p' "$rr"|sed 's/^Expected answer scope: //'|paste -sd ' ' -|sed 's/\.$//')
tq=$(sed -n '98p' "$tr"); ta=$(sed -n '100,101p' "$tr"|sed 's/^Expected answer: //'|paste -sd ' ' -|sed 's/\.$//')
embedded=$(jq -c -n --arg rh "$rich_heading" --arg th "$teaching_heading" --arg rq "$rq" --arg ra "$ra" --arg tq "$tq" --arg ta "$ta" '{rich:{card_revision:2,id:"cq-model-constraint-trust",revision:1,fragment:"#cq-model-constraint-trust",literal_heading:$rh,question:$rq,answer_text:$ra,heading_found:true,rendered_anchor:"not_checked"},teaching:{card_revision:3,id:"cq-model-data-constraint",revision:1,fragment:"#cq-model-data-constraint",literal_heading:$th,question:$tq,answer_text:$ta,heading_found:true,rendered_anchor:"not_checked"}}')
test "$embedded" = "$(jq -c '.cases[2].expected' "$q")"; test "$embedded" = "$(jq -c '.cases[2].observed' "$q")"
if rg -n -F "$rich_heading" "$tr" >/dev/null 2>&1; then wrong=0; else wrong=$?; fi
test "$wrong" = 1
if rg -n -F "$rich_heading" "$source/workbench/no-such-card.md" >/dev/null 2>&1; then error=0; else error=$?; fi
test "$error" = 2

# Case 4: native synthetic components and template assertion slots.
native=$(jq -c '.records[]|select(.path=="knowledge/concept-cards/examples/cq-coverage.md")|{component_refs:.values.component_refs,coverage_state:.values.coverage_state,answerability_state:.values.answerability_state,retrieval_state:.values.retrieval_state}' "$i")
template=$(jq -c '.records[]|select(.path=="knowledge/concept-cards/templates/competency-question.md")|{coverage_assertions:.values.coverage_assertions,answerability_state:.values.answerability_state,cq_status:.values.cq_status}' "$i")
rg -q '^id: cc-claim-support-is-assertion-specific$' knowledge/concept-cards/examples/claim-backed-card.md
if rg -n '^id: claim-support-is-assertion-specific$' knowledge/concept-cards >/dev/null 2>&1; then claim=0; else claim=$?; fi
test "$claim" = 1
if rg -n '^id: support-synthetic-claim-001$' knowledge/concept-cards >/dev/null 2>&1; then support=0; else support=$?; fi
test "$support" = 1
synthetic=$(jq -c -n --argjson refs "$(jq '.records[]|select(.path=="knowledge/concept-cards/examples/cq-coverage.md")|.values.component_refs' "$i")" --arg cov "$(jq -r '.records[]|select(.path=="knowledge/concept-cards/examples/cq-coverage.md")|.values.coverage_state' "$i")" --arg ans "$(jq -r '.records[]|select(.path=="knowledge/concept-cards/examples/cq-coverage.md")|.values.answerability_state' "$i")" --arg ret "$(jq -r '.records[]|select(.path=="knowledge/concept-cards/examples/cq-coverage.md")|.values.retrieval_state' "$i")" --argjson assertion "$(jq '.records[]|select(.path=="knowledge/concept-cards/templates/competency-question.md")|.values.coverage_assertions' "$i")" --arg tans "$(jq -r '.records[]|select(.path=="knowledge/concept-cards/templates/competency-question.md")|.values.answerability_state' "$i")" --arg stat "$(jq -r '.records[]|select(.path=="knowledge/concept-cards/templates/competency-question.md")|.values.cq_status' "$i")" '{synthetic:{component_refs:$refs,coverage_state:$cov,answerability_state:$ans,retrieval_state:$ret,named_id_root_declarations:{concept:"found_in_example_root",claim:"not_found_as_standalone_root",support:"not_found_as_standalone_root"}},template:{coverage_assertions:[$assertion[]|{id,revision,component,assertion,covered_refs,source_support_refs,coverage_state}],answerability_state:$tans,cq_status:$stat}}')
test "$synthetic" = "$(jq -c '.cases[3].expected' "$q")"; test "$synthetic" = "$(jq -c '.cases[3].observed' "$q")"
if rg -n -F 'id: support-synthetic-claim-999' knowledge/concept-cards >/dev/null 2>&1; then wrong=0; else wrong=$?; fi
test "$wrong" = 1
if rg -n -F 'id: support-synthetic-claim-001' knowledge/concept-cards/no-such-root >/dev/null 2>&1; then error=0; else error=$?; fi
test "$error" = 2

# JSON, preservation and exactly seven authorized planning files.
jq empty "$m"; jq empty "$q"
git -C "$source" diff --exit-code "$opening_source" --
git -C "$plan" diff --exit-code "$opening_planning" "$cc_commit" -- project08-concept-card-metadata/arc01-metadata-research-and-requirements project08-concept-card-metadata/artifacts/semantic-coverage-current.json project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
git -C "$plan" diff --check "$opening_planning" "$cc_commit"
expected_files=$(printf '%s\n' "$s/artifacts/semantic-membership.json" "$s/artifacts/semantic-evidence.md" "$s/artifacts/query-cases.json" "$s/artifacts/validation-evidence.md" "$s/artifacts/handoff.md" "$s/ledger.md" "$s/closing-report.md"|sort)
actual_files=$(git -C "$plan" diff --name-only "$opening_planning" "$cc_commit" --|sort)
test "$expected_files" = "$actual_files"
test "$(git -C "$source" status --porcelain)" = ""
~~~

The intended result is exact 30-pair equality; inclusion/disjointness and
150/30/375 accounting; every registered hash; full legacy, six-family and
standalone-CQ census; all four native comparisons; eight controls without
promoting a search error to no-match; valid JSON; preserved source and
accepted paths; no whitespace diagnostics; and exactly seven planning paths.

No package, install, source-skill, runtime, memory-admission or schema gate is
claimed. CDC must rerun the route with the committed endpoint and decide all
six ledger rows independently.
