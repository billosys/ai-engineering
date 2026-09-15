# Slice02 validation evidence

This is the designated current replay for the Iteration 01 repair. It is
CC-attested until CDC reruns it independently.

Opening source HEAD: e763c661592ff1097a94bb470db9cf924524579d
Original CC endpoint: 753bacb051c041a75d0c4d36595cfbadd5a9b5eb
Repair opening planning HEAD: f15c896bfeec4c3618387413e63c95dfe9fc6771
Frozen slice-plan authority: a27c4d33a02d3e6047656b9ae0c17a145aa3f208
Frozen slice-ledger authority: 753bacb051c041a75d0c4d36595cfbadd5a9b5eb
Repair endpoint: pending until the scoped commit is created
Source cwd: /Users/oubiwann/lab/billosys/ai-engineering
Planning cwd: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
Model, settings, effort and compaction: unknown; no settings changed.
The route uses /bin/bash, jq, shasum, rg, awk, sed and git, with no new
parser/helper. The command prints tool versions. Set CC_COMMIT to the committed
repair endpoint for CDC. Set CC_PRECOMMIT=1 for the same checks against the
working-tree repair before commit; that mode checks the seven-file working-tree
scope rather than pretending the uncommitted files have a commit hash.

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
original_cc=753bacb051c041a75d0c4d36595cfbadd5a9b5eb
repair_opening=f15c896bfeec4c3618387413e63c95dfe9fc6771
slice_plan_authority=a27c4d33a02d3e6047656b9ae0c17a145aa3f208
slice_ledger_authority=$original_cc
slice_plan_path=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/slice-plan.md
slice_ledger_path=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/ledger.md
precommit=${CC_PRECOMMIT:-0}
cc_commit=$(git -C "$plan" rev-parse HEAD)
if [ -n "${CC_COMMIT:-}" ]; then cc_commit=$(printenv CC_COMMIT); fi
test "$(git -C "$source" rev-parse "$opening_source")" = "$opening_source"
test "$(git -C "$plan" rev-parse "$repair_opening")" = "$repair_opening"
git -C "$plan" merge-base --is-ancestor "$original_cc" "$repair_opening"
if [ "$precommit" = 1 ]; then
  endpoint="working-tree@$repair_opening"
else
  test -n "${CC_COMMIT:-}"
  test "$(git -C "$plan" rev-parse "$cc_commit")" = "$cc_commit"
  git -C "$plan" merge-base --is-ancestor "$repair_opening" "$cc_commit"
  endpoint="$cc_commit"
fi
printf 'source=%s repair_opening=%s endpoint=%s\n' "$(git -C "$source" rev-parse HEAD)" "$repair_opening" "$endpoint"
printf 'bash=%s jq=%s rg=%s\n' "$(bash --version|head -1)" "$(jq --version)" "$(rg --version|head -1)"

# Exact scope and current accounting. Read the plan table from its pinned
# authority bytes; live plan status may change during CDC. The table is
# pipe-delimited; \140 is the shell-safe backtick character to remove.
expected=$(git -C "$plan" show "$slice_plan_authority:$slice_plan_path"|sed -n 's/^| \([^|]*\) | \([^|]*\) |$/\1|\2/p'|tr -d '\140'|sed '/^Field path|/d;/^---|/d'|sort -u)
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

# Registry referential integrity, both evidence layers, pinned authority bytes,
# and every registered hash.
jq -e '. as $r|(.memberships|length)==30 and (.baseline_mappings|length)==2 and
  all(.memberships[];.meaning_id as $m|$r.meanings|has($m)) and
  all(([ $r.meanings[]?.evidence_ids[]?, $r.memberships[]?.evidence_ids[]?, $r.baseline_mappings[]?.evidence_ids[]? ][]); . as $id|$r.evidence|has($id))' "$m"
while IFS=$'\t' read -r id root path digest commit; do
  if [ -n "$commit" ]; then
    test "$root" = planning
    got=$(git -C "$plan" show "$commit:$path"|shasum -a 256|awk '{print $1}')
  else
    case "$root" in source) file="$source/$path";; planning) file="$plan/$path";; absolute) file="$path";; *) exit 1;; esac
    got=$(shasum -a 256 "$file"|awk '{print $1}')
  fi
  test "$got" = "$digest"
  printf 'hash-ok=%s\n' "$id"
done < <(jq -r '.evidence|to_entries[]|[.key,.value.root,.value.path,.value.sha256,(.value.commit//"")]|@tsv' "$m")

slice_plan_live=$(shasum -a 256 "$plan/$slice_plan_path"|awk '{print $1}')
slice_ledger_live=$(shasum -a 256 "$plan/$slice_ledger_path"|awk '{print $1}')
printf 'pinned-authority-ok=slicePlan live-hash=%s\n' "$slice_plan_live"
printf 'pinned-authority-ok=sliceLedger live-hash=%s\n' "$slice_ledger_live"

source_manifest=$(jq -r '.evidence.baselineSourceManifest.path' "$m")
copy_manifest=$(jq -r '.evidence.baselineCopyManifest.path' "$m")
(cd "$source"; shasum -a 256 -c "$plan/$source_manifest" >/dev/null)
(cd "$source"; shasum -a 256 -c "$plan/$copy_manifest" >/dev/null)
printf '%s\n' 'baseline-manifests=source-and-copy-ok'
while IFS=$'\t' read -r original original_sha copy copy_sha; do
  test "$(shasum -a 256 "$source/$original"|awk '{print $1}')" = "$original_sha"
  test "$(shasum -a 256 "$source/$copy"|awk '{print $1}')" = "$copy_sha"
  cmp -s "$source/$original" "$source/$copy"
  printf 'baseline-mapping-ok=%s\n' "$original"
done < <(jq -r '.baseline_mappings[]|[.original_path,.original_sha256,.copy_path,.copy_sha256]|@tsv' "$m")

# Full census: legacy, six card families, malformed rich exclusions, two CQs.
# Every advertised root/item state is derived from the frozen parsed inventory.
legacy=$(jq -c '
  def stats($rows;$k):
    {present:([$rows[]|select(.values|has($k))]|length),
     absent:([$rows[]|select(.values|has($k)|not)]|length),
     null:([$rows[]|select((.values|has($k)) and .values[$k]==null)]|length),
     empty:([$rows[]|select((.values|has($k)) and (.values[$k]|type)=="array" and (.values[$k]|length)==0)]|length),
     populated:([$rows[]|select((.values|has($k)) and (.values[$k]|type)=="array" and (.values[$k]|length)>0)]|length),
     items:([$rows[]|.values[$k][]?]|length),
     distinct:([$rows[]|.values[$k][]?]|unique|length),
     itemtypes:([$rows[]|.values[$k][]?|type]|unique)};
  [.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|.+{family:(if (.path|contains("complete-musician")) then "music" else "erlang" end)}]
  |group_by(.family)|map(. as $r|{family:$r[0].family,records:($r|length),answers_questions:stats($r;"answers_questions")})
' "$i")
printf 'legacy_census=%s\n' "$legacy"
test "$legacy" = '[{"family":"erlang","records":1664,"answers_questions":{"present":1664,"absent":0,"null":0,"empty":0,"populated":1664,"items":4059,"distinct":3265,"itemtypes":["string"]}},{"family":"music","records":390,"answers_questions":{"present":390,"absent":0,"null":0,"empty":0,"populated":390,"items":574,"distinct":379,"itemtypes":["string"]}}]'
test "$(jq -c '[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|.values.answers_questions[]]|{records:2054,items:length,distinct:(unique|length)}' "$i")" = '{"records":2054,"items":4633,"distinct":3644}'
card_count=$(jq '[.records[]|select(.record_kind=="concept-card")]|length' "$i")
cq_count=$(jq '[.records[]|select(.record_kind=="competency-question")]|length' "$i")
bad_rich=$(jq -c '[.records[]|select(.error!=null)|select(.path|test("compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-.*\\.md$"))|.path]' "$i")
test "$card_count" = 31; test "$cq_count" = 2
test "$bad_rich" = '["workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-memory-forms.md","workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-priming-forms.md","workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-recognition-dual-process.md"]'
card_roots=$(jq -c '
  def state($o;$k):
    if ($o|has($k)|not) then "absent"
    elif $o[$k]==null then "null"
    elif (($o[$k]|type)=="array" and ($o[$k]|length)==0) then "empty"
    elif (($o[$k]|type)=="array") then "populated"
    else ($o[$k]|type) end;
  [.records[]|select(.record_kind=="concept-card")|.path as $p|
   {family:(if $p=="knowledge/concept-cards/templates/concept-card.md" then "template"
            elif ($p|startswith("knowledge/concept-cards/examples/")) then "synthetic-examples"
            elif ($p|contains("slice02-pilot-markdown-preparation-and-card-extraction")) then "arc07-pilot"
            elif ($p|contains("slice04-expanded-corpus-card-generation")) then "arc07-expanded"
            elif ($p|contains("compcogneuro-rich-rerun")) then "rich-rerun"
            elif ($p|contains("compcogneuro-teaching-rerun")) then "teaching-rerun"
            else "other" end),
    competency_question_refs:state(.values;"competency_question_refs"),
    cq_refs:state(.values;"cq_refs")}]
  |group_by(.family)|map({family:.[0].family,cards:length,
    competency_question_refs:(group_by(.competency_question_refs)|map({state:.[0].competency_question_refs,n:length})),
    cq_refs:(group_by(.cq_refs)|map({state:.[0].cq_refs,n:length}))})
' "$i")
printf 'card_roots=%s\n' "$card_roots"
test "$card_roots" = '[{"family":"arc07-expanded","cards":6,"competency_question_refs":[{"state":"absent","n":6}],"cq_refs":[{"state":"absent","n":6}]},{"family":"arc07-pilot","cards":4,"competency_question_refs":[{"state":"absent","n":4}],"cq_refs":[{"state":"empty","n":4}]},{"family":"rich-rerun","cards":7,"competency_question_refs":[{"state":"absent","n":7}],"cq_refs":[{"state":"populated","n":7}]},{"family":"synthetic-examples","cards":3,"competency_question_refs":[{"state":"absent","n":2},{"state":"empty","n":1}],"cq_refs":[{"state":"absent","n":2},{"state":"populated","n":1}]},{"family":"teaching-rerun","cards":10,"competency_question_refs":[{"state":"absent","n":10}],"cq_refs":[{"state":"populated","n":10}]},{"family":"template","cards":1,"competency_question_refs":[{"state":"absent","n":1}],"cq_refs":[{"state":"empty","n":1}]}]'
test "$(jq -c '[.records[]|select(.record_kind=="concept-card")|.values.cq_refs[]?]|{items:length,item_types:([.[]|{id:(.id|type),path:(.path|type),revision:(.revision|type)}]|unique)}' "$i")" = '{"items":18,"item_types":[{"id":"string","path":"string","revision":"number"}]}'
test "$(jq -c '[.records[]|select(.record_kind=="concept-card")|.values.competency_question_refs[]?]|{items:length,item_types:([.[]|type]|unique)}' "$i")" = '{"items":0,"item_types":[]}'
standalone_roots=$(jq -c '
  def state($o;$k):
    if ($o|has($k)|not) then "absent"
    elif $o[$k]==null then "null"
    elif (($o[$k]|type)=="array" and ($o[$k]|length)==0) then "empty"
    elif (($o[$k]|type)=="array") then "populated"
    else ($o[$k]|type) end;
  [.records[]|select(.record_kind=="competency-question")|.path as $p|.values as $v|
   {path:$p,question:state($v;"question"),roles:state($v;"roles"),requirement_source_ref:state($v;"requirement_source_ref"),intended_use:state($v;"intended_use"),answer_criteria:state($v;"answer_criteria"),coverage_assertions:state($v;"coverage_assertions"),component_refs:state($v;"component_refs"),coverage_state:state($v;"coverage_state"),answerability_state:state($v;"answerability_state"),cq_status:state($v;"cq_status")}]
' "$i")
printf 'standalone_roots=%s\n' "$standalone_roots"
test "$standalone_roots" = '[{"path":"knowledge/concept-cards/examples/cq-coverage.md","question":"string","roles":"absent","requirement_source_ref":"absent","intended_use":"absent","answer_criteria":"absent","coverage_assertions":"absent","component_refs":"populated","coverage_state":"string","answerability_state":"string","cq_status":"absent"},{"path":"knowledge/concept-cards/templates/competency-question.md","question":"null","roles":"empty","requirement_source_ref":"null","intended_use":"null","answer_criteria":"null","coverage_assertions":"populated","component_refs":"absent","coverage_state":"absent","answerability_state":"string","cq_status":"string"}]'
jq -e '.records[]|select(.path=="knowledge/concept-cards/examples/cq-coverage.md")|.values|.component_refs|length==3 and all(.[]; (.id|type)=="string" and (.revision|type)=="number" and (.role|type)=="string")' "$i"
jq -e '.records[]|select(.path=="knowledge/concept-cards/templates/competency-question.md")|.values.coverage_assertions|length==1 and .[0].id==null and .[0].revision==null and .[0].component==null and .[0].assertion==null and .[0].covered_refs==[] and .[0].source_support_refs==[] and .[0].coverage_state=="unassessed"' "$i"

# Case 1: native legacy reverse lookup; the same parameterized selection is
# used for positives, the wrong-value no-match and the missing-input error.
legacy_lookup='[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|select((.values.answers_questions//[])|index($q))|{path,slug:.values.slug,concept:.values.concept}]'
music=$(jq -c --arg q 'What are the different types of accent in music?' "$legacy_lookup" "$i")
erlang=$(jq -c --arg q 'What is a behaviour in OTP?' "$legacy_lookup" "$i")
test "$music" = "$(jq -c '.cases[0].expected.music.matches' "$q")"; test "$music" = "$(jq -c '.cases[0].observed.music.matches' "$q")"
test "$erlang" = "$(jq -c '.cases[0].expected.erlang.matches' "$q")"; test "$erlang" = "$(jq -c '.cases[0].observed.erlang.matches' "$q")"
wrong_err=$(mktemp)
if wrong_output=$(jq -c --arg q 'What are the different types of accent in jazz?' "$legacy_lookup" "$i" 2>"$wrong_err"); then wrong_status=0; else wrong_status=$?; fi
wrong_stderr=false; test ! -s "$wrong_err" || wrong_stderr=true; rm -f "$wrong_err"
wrong_native=$(jq -c -n --arg stdout "$wrong_output" --argjson status "$wrong_status" --argjson stderr_nonempty "$wrong_stderr" '{stdout:$stdout,status:$status,stderr_nonempty:$stderr_nonempty,classification:"successful_no_match"}')
test "$wrong_native" = "$(jq -c '.cases[0].controls[0].expected' "$q")"; test "$wrong_native" = "$(jq -c '.cases[0].controls[0].observed' "$q")"
error_err=$(mktemp)
if error_output=$(jq -c --arg q 'What are the different types of accent in music?' "$legacy_lookup" /private/tmp/cc-slice02-no-such-inventory.json 2>"$error_err"); then error_status=0; else error_status=$?; fi
error_stderr=false; test ! -s "$error_err" || error_stderr=true; rm -f "$error_err"
error_native=$(jq -c -n --arg stdout "$error_output" --argjson status "$error_status" --argjson stderr_nonempty "$error_stderr" '{stdout:$stdout,status:$status,stderr_nonempty:$stderr_nonempty,classification:"tool_error"}')
test "$error_native" = "$(jq -c '.cases[0].controls[1].expected' "$q")"; test "$error_native" = "$(jq -c '.cases[0].controls[1].observed' "$q")"

# Case 2: rich external tuple; the native parent-path lookup records bounded
# absence separately from an rg tool error.
rich=$(jq -r '.cases[1].path' "$q")
rich_decl=$(jq -c --arg p "$rich" '.records[]|select(.path==$p)|.values.cq_refs[0]|{id,revision,path}' "$i")
rich_id=$(jq -r '.id' <<<"$rich_decl")
rich_path=$(jq -r '.path' <<<"$rich_decl")
rich_base=${rich%/*}
rich_target="$rich_base/$rich_path"
rich_parent=${rich_target%/*}
rich_declaration_present=true
if test ! -d "$rich_parent"; then
  rich_lookup_operation='test ! -d parent_path'; rich_lookup_status=0
  rich_lookup_classification=bounded_parent_absence; rich_target_available=unresolved
elif test -f "$rich_target"; then
  rich_lookup_operation='test -f resolved_path'; rich_lookup_status=0
  rich_lookup_classification=available; rich_target_available=available
else
  rich_lookup_operation='test -f resolved_path'; rich_lookup_status=1
  rich_lookup_classification=successful_no_match; rich_target_available=unavailable
fi
rich_native=$(jq -c -n --argjson declared "$rich_decl" --argjson declaration_present "$rich_declaration_present" --arg base "$rich_base" --arg target "$rich_path" --arg resolved "$rich_target" --arg parent "$rich_parent" --arg operation "$rich_lookup_operation" --argjson status "$rich_lookup_status" --arg classification "$rich_lookup_classification" --arg available "$rich_target_available" '{declared:$declared,declaration_present:$declaration_present,target_lookup:{selected_base:$base,declared_target:$target,resolved_path:$resolved,parent_path:$parent,operation:$operation,status:$status,classification:$classification,target_available:$available},identity_revision:"declared_only",answerability:"unassessed"}')
test "$rich_native" = "$(jq -c '.cases[1].expected' "$q")"; test "$rich_native" = "$(jq -c '.cases[1].observed' "$q")"
wrong_err=$(mktemp)
if wrong_output=$(rg -l -F "id: ${rich_id}-wrong" knowledge/concept-cards 2>"$wrong_err"); then wrong_status=0; else wrong_status=$?; fi
wrong_stderr=false; test ! -s "$wrong_err" || wrong_stderr=true; rm -f "$wrong_err"
wrong_native=$(jq -c -n --arg stdout "$wrong_output" --argjson status "$wrong_status" --argjson stderr_nonempty "$wrong_stderr" '{stdout:$stdout,status:$status,stderr_nonempty:$stderr_nonempty,classification:"successful_no_match"}')
test "$wrong_native" = "$(jq -c '.cases[1].controls[0].expected' "$q")"; test "$wrong_native" = "$(jq -c '.cases[1].controls[0].observed' "$q")"
error_err=$(mktemp)
if error_output=$(rg -l -F "id: $rich_id" knowledge/concept-cards/no-such-root 2>"$error_err"); then error_status=0; else error_status=$?; fi
error_stderr=false; test ! -s "$error_err" || error_stderr=true; rm -f "$error_err"
error_native=$(jq -c -n --arg stdout "$error_output" --argjson status "$error_status" --argjson stderr_nonempty "$error_stderr" '{stdout:$stdout,status:$status,stderr_nonempty:$stderr_nonempty,classification:"tool_error"}')
test "$error_native" = "$(jq -c '.cases[1].controls[1].expected' "$q")"; test "$error_native" = "$(jq -c '.cases[1].controls[1].observed' "$q")"
altered_expected=$(jq -c '.cases[1].expected|.declared.id="cq-inspect-support-for-card-statement-wrong"' "$q")
test "$rich_native" != "$altered_expected"
altered_native=$(jq -c -n '{comparison:"not_equal"}')
test "$altered_native" = "$(jq -c '.cases[1].controls[2].expected' "$q")"; test "$altered_native" = "$(jq -c '.cases[1].controls[2].observed' "$q")"

# Case 3: embedded generated CQ; native tuples, card revisions, literal
# headings and source text are separate, and rendered anchors are untested.
tick=$(printf '\x60')
rr=$(jq -r '.evidence.richRerun.path' "$m")
tr=$(jq -r '.evidence.teachingRerun.path' "$m")
rich_ref=$(jq -c --arg p "$rr" '.records[]|select(.path==$p)|.values.cq_refs[0]|{id,revision,path}' "$i")
teaching_ref=$(jq -c --arg p "$tr" '.records[]|select(.path==$p)|.values.cq_refs[0]|{id,revision,path}' "$i")
rich_cq_id=$(jq -r '.id' <<<"$rich_ref"); teaching_cq_id=$(jq -r '.id' <<<"$teaching_ref")
rich_card_revision=$(jq -r --arg p "$rr" '.records[]|select(.path==$p)|.values.revision' "$i")
teaching_card_revision=$(jq -r --arg p "$tr" '.records[]|select(.path==$p)|.values.revision' "$i")
rich_heading=$(awk -v id="$rich_cq_id" -v tick="$tick" '$0=="### CQ " tick id tick {print; exit}' "$source/$rr")
teaching_heading=$(awk -v id="$teaching_cq_id" -v tick="$tick" '$0=="### CQ " tick id tick {print; exit}' "$source/$tr")
rich_text=$(awk -v h="$rich_heading" '$0==h {phase="question"; next} phase=="question" {if ($0=="" && q=="") next; if ($0=="") {phase="answer"; next}; if (q!="") q=q " "; q=q $0; next} phase=="answer" {if ($0 ~ /^Expected answer/) {sub(/^Expected answer[^:]*: /,""); a=$0; next}; if (a!="" && $0=="") {print q "\t" a; exit}; if (a!="") a=a " " $0}' "$source/$rr")
teaching_text=$(awk -v h="$teaching_heading" '$0==h {phase="question"; next} phase=="question" {if ($0=="" && q=="") next; if ($0=="") {phase="answer"; next}; if (q!="") q=q " "; q=q $0; next} phase=="answer" {if ($0 ~ /^Expected answer/) {sub(/^Expected answer[^:]*: /,""); a=$0; next}; if (a!="" && $0=="") {print q "\t" a; exit}; if (a!="") a=a " " $0}' "$source/$tr")
rich_question=${rich_text%%$'\t'*}; rich_answer=${rich_text#*$'\t'}
teaching_question=${teaching_text%%$'\t'*}; teaching_answer=${teaching_text#*$'\t'}
embedded=$(jq -c -n --argjson rich_card_revision "$rich_card_revision" --arg rid "$rich_cq_id" --argjson rrevision "$(jq -r '.revision' <<<"$rich_ref")" --arg rfragment "$(jq -r '.path' <<<"$rich_ref")" --arg rh "$rich_heading" --arg rq "$rich_question" --arg ra "$rich_answer" --argjson teaching_card_revision "$teaching_card_revision" --arg tid "$teaching_cq_id" --argjson trevision "$(jq -r '.revision' <<<"$teaching_ref")" --arg tfragment "$(jq -r '.path' <<<"$teaching_ref")" --arg th "$teaching_heading" --arg tq "$teaching_question" --arg ta "$teaching_answer" '{rich:{card_revision:$rich_card_revision,id:$rid,revision:$rrevision,fragment:$rfragment,literal_heading:$rh,question:$rq,answer_text:$ra,heading_found:($rh!=""),rendered_anchor:"not_checked"},teaching:{card_revision:$teaching_card_revision,id:$tid,revision:$trevision,fragment:$tfragment,literal_heading:$th,question:$tq,answer_text:$ta,heading_found:($th!=""),rendered_anchor:"not_checked"}}')
test "$embedded" = "$(jq -c '.cases[2].expected' "$q")"; test "$embedded" = "$(jq -c '.cases[2].observed' "$q")"
wrong_err=$(mktemp)
if wrong_output=$(rg -n -F "$rich_heading" "$source/$tr" 2>"$wrong_err"); then wrong_status=0; else wrong_status=$?; fi
wrong_stderr=false; test ! -s "$wrong_err" || wrong_stderr=true; rm -f "$wrong_err"
wrong_native=$(jq -c -n --arg stdout "$wrong_output" --argjson status "$wrong_status" --argjson stderr_nonempty "$wrong_stderr" '{stdout:$stdout,status:$status,stderr_nonempty:$stderr_nonempty,classification:"successful_no_match"}')
test "$wrong_native" = "$(jq -c '.cases[2].controls[0].expected' "$q")"; test "$wrong_native" = "$(jq -c '.cases[2].controls[0].observed' "$q")"
error_err=$(mktemp)
if error_output=$(rg -n -F "$rich_heading" "$source/workbench/no-such-card.md" 2>"$error_err"); then error_status=0; else error_status=$?; fi
error_stderr=false; test ! -s "$error_err" || error_stderr=true; rm -f "$error_err"
error_native=$(jq -c -n --arg stdout "$error_output" --argjson status "$error_status" --argjson stderr_nonempty "$error_stderr" '{stdout:$stdout,status:$status,stderr_nonempty:$stderr_nonempty,classification:"tool_error"}')
test "$error_native" = "$(jq -c '.cases[2].controls[1].expected' "$q")"; test "$error_native" = "$(jq -c '.cases[2].controls[1].observed' "$q")"
altered_expected=$(jq -c '.cases[2].expected.rich|.revision=99' "$q")
test "$(jq -c '.rich' <<<"$embedded")" != "$altered_expected"
altered_native=$(jq -c -n '{comparison:"not_equal"}')
test "$altered_native" = "$(jq -c '.cases[2].controls[2].expected' "$q")"; test "$altered_native" = "$(jq -c '.cases[2].controls[2].observed' "$q")"

# Case 4: native synthetic components and template assertion slots.
synthetic_values=$(jq -c '.records[]|select(.path=="knowledge/concept-cards/examples/cq-coverage.md")|.values' "$i")
template_values=$(jq -c '.records[]|select(.path=="knowledge/concept-cards/templates/competency-question.md")|.values' "$i")
concept_err=$(mktemp)
if concept_output=$(rg -l -e '^id: cc-claim-support-is-assertion-specific$' knowledge/concept-cards/examples 2>"$concept_err"); then concept_status=0; else concept_status=$?; fi
concept_stderr=false; test ! -s "$concept_err" || concept_stderr=true; rm -f "$concept_err"
test "$concept_status" = 0; test -n "$concept_output"; test "$concept_stderr" = false
if [ "$concept_status" = 0 ]; then concept_declaration=found_in_example_root; else concept_declaration=unresolved; fi
claim_err=$(mktemp)
if claim_output=$(rg -l -e '^id: claim-support-is-assertion-specific$' knowledge/concept-cards 2>"$claim_err"); then claim_status=0; else claim_status=$?; fi
claim_stderr=false; test ! -s "$claim_err" || claim_stderr=true; rm -f "$claim_err"
test "$claim_status" = 1; test -z "$claim_output"; test "$claim_stderr" = false
if [ "$claim_status" = 1 ]; then claim_declaration=not_found_as_standalone_root; else claim_declaration=unresolved; fi
support_err=$(mktemp)
if support_output=$(rg -l -e '^id: support-synthetic-claim-001$' knowledge/concept-cards 2>"$support_err"); then support_status=0; else support_status=$?; fi
support_stderr=false; test ! -s "$support_err" || support_stderr=true; rm -f "$support_err"
test "$support_status" = 1; test -z "$support_output"; test "$support_stderr" = false
if [ "$support_status" = 1 ]; then support_declaration=not_found_as_standalone_root; else support_declaration=unresolved; fi
native=$(jq -c -n --argjson refs "$(jq '.component_refs' <<<"$synthetic_values")" --arg cov "$(jq -r '.coverage_state' <<<"$synthetic_values")" --arg ans "$(jq -r '.answerability_state' <<<"$synthetic_values")" --arg ret "$(jq -r '.retrieval_state' <<<"$synthetic_values")" --arg concept "$concept_declaration" --arg claim "$claim_declaration" --arg support "$support_declaration" '{component_refs:$refs,coverage_state:$cov,answerability_state:$ans,retrieval_state:$ret,named_id_root_declarations:{concept:$concept,claim:$claim,support:$support}}')
template=$(jq -c -n --argjson assertion "$(jq '.coverage_assertions' <<<"$template_values")" --arg ans "$(jq -r '.answerability_state' <<<"$template_values")" --arg stat "$(jq -r '.cq_status' <<<"$template_values")" '{coverage_assertions:[$assertion[]|{id,revision,component,assertion,covered_refs,source_support_refs,coverage_state}],answerability_state:$ans,cq_status:$stat}')
synthetic=$(jq -c -n --argjson native "$native" --argjson template "$template" '{synthetic:$native,template:$template}')
test "$synthetic" = "$(jq -c '.cases[3].expected' "$q")"; test "$synthetic" = "$(jq -c '.cases[3].observed' "$q")"
wrong_err=$(mktemp)
if wrong_output=$(rg -l -F 'id: support-synthetic-claim-999' knowledge/concept-cards 2>"$wrong_err"); then wrong_status=0; else wrong_status=$?; fi
wrong_stderr=false; test ! -s "$wrong_err" || wrong_stderr=true; rm -f "$wrong_err"
wrong_native=$(jq -c -n --arg stdout "$wrong_output" --argjson status "$wrong_status" --argjson stderr_nonempty "$wrong_stderr" '{stdout:$stdout,status:$status,stderr_nonempty:$stderr_nonempty,classification:"successful_no_match"}')
test "$wrong_native" = "$(jq -c '.cases[3].controls[0].expected' "$q")"; test "$wrong_native" = "$(jq -c '.cases[3].controls[0].observed' "$q")"
error_err=$(mktemp)
if error_output=$(rg -l -F 'id: support-synthetic-claim-001' knowledge/concept-cards/no-such-root 2>"$error_err"); then error_status=0; else error_status=$?; fi
error_stderr=false; test ! -s "$error_err" || error_stderr=true; rm -f "$error_err"
error_native=$(jq -c -n --arg stdout "$error_output" --argjson status "$error_status" --argjson stderr_nonempty "$error_stderr" '{stdout:$stdout,status:$status,stderr_nonempty:$stderr_nonempty,classification:"tool_error"}')
test "$error_native" = "$(jq -c '.cases[3].controls[1].expected' "$q")"; test "$error_native" = "$(jq -c '.cases[3].controls[1].observed' "$q")"

# JSON, preservation and exactly seven authorized planning files. Explicitly
# preserve Arc01, both coverage registers and the accepted Slice01/Slice12
# packets. CDC documentation is outside this CC diff.
jq empty "$m"; jq empty "$q"
git -C "$source" diff --exit-code "$opening_source" --
preserved=(
  project08-concept-card-metadata/arc01-metadata-research-and-requirements
  project08-concept-card-metadata/artifacts/semantic-coverage-current.json
  project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation
)
for path in "${preserved[@]}"; do
  if [ "$precommit" = 1 ]; then git -C "$plan" diff --exit-code -- "$path"; else git -C "$plan" diff --exit-code "$repair_opening" "$cc_commit" -- "$path"; fi
done
if [ "$precommit" = 1 ]; then
  git -C "$plan" diff --check
  actual_files=$(git -C "$plan" diff --name-only --|sort)
else
  git -C "$plan" diff --check "$repair_opening" "$cc_commit"
  actual_files=$(git -C "$plan" diff --name-only "$repair_opening" "$cc_commit" --|sort)
fi
expected_files=$(printf '%s\n' "$s/artifacts/semantic-membership.json" "$s/artifacts/semantic-evidence.md" "$s/artifacts/query-cases.json" "$s/artifacts/validation-evidence.md" "$s/artifacts/handoff.md" "$s/ledger.md" "$s/closing-report.md"|sort)
test "$expected_files" = "$actual_files"
test "$(git -C "$source" status --porcelain)" = ""
~~~

The intended result is exact 30-pair equality; inclusion/disjointness and
150/30/375 accounting; every registered hash plus both original/copy manifest
mappings; full legacy, six-family and standalone-CQ census with root/item types
and absence/null/empty distinctions; all four native comparisons; ten
controls without promoting a search error to no-match; altered expected
identity/revision rejection; valid JSON; preserved source and accepted paths;
no whitespace diagnostics; and exactly seven planning paths. The pre-commit
rehearsal is `CC_PRECOMMIT=1 bash <(awk '/^~~~bash$/{p=1;next} /^~~~$/{p=0} p' .worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/artifacts/validation-evidence.md)` from the source checkout; CDC runs the same block with
`CC_COMMIT=<repair-endpoint>`.

No package, install, source-skill, runtime, memory-admission or schema gate is
claimed. CDC must rerun the route with the committed endpoint and decide all
six ledger rows independently.
