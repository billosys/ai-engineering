# Slice18 validation evidence: literal native replay

Status: CC proposed-done. This route is structural and evidence reproduction
for CRC. It does not accept semantic meanings, adopt a schema, authorize
source repair, establish a real extraction, close P-15, or replace
CRC/CDC/Operator gates.

## Intake and route contract

The route pins source `ce3f77103eff5e07b3533a03c65f158684fc1039`, issued
planning `961c748f7915c71ba59ef37a2dd65253800be268`, preserved predecessor
planning `eb7b606baac634f0a3beb3db5d7dcfea26c986e3`, Set B authority
`dee3052c88e0fd9361e74200fd1eea26ade76435`, and frozen inventory SHA
`afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.
Precommit mode reads the working registry; committed mode reads the registry
from `CC_COMMIT`. The wrapper loads the route from a separately named
`REPLAY_COMMIT`, extracts exactly one route between the two headings, runs
`bash -n`, and executes it with explicit endpoints.

## Literal route

~~~bash
set -euo pipefail
source=/Users/oubiwann/lab/billosys/ai-engineering
plan=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
slice_rel=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice18-run-scope-workers-and-outputs
coverage_rel=project08-concept-card-metadata/artifacts/semantic-coverage-current.json
transition_rel=project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
inventory_rel=project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
membership_rel=$slice_rel/artifacts/semantic-membership.json
opening_source=ce3f77103eff5e07b3533a03c65f158684fc1039
opening_planning=961c748f7915c71ba59ef37a2dd65253800be268
predecessor_planning=eb7b606baac634f0a3beb3db5d7dcfea26c986e3
set_authority=dee3052c88e0fd9361e74200fd1eea26ade76435
inventory_sha=afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b
cc_commit=$(printenv CC_COMMIT 2>/dev/null || true)
replay_commit=$(printenv REPLAY_COMMIT 2>/dev/null || true)
precommit=$(printenv CC_PRECOMMIT 2>/dev/null || true)
tmp=$(mktemp -d /private/tmp/cc-slice18-replay.XXXXXX)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
fail() { printf 'FAIL: %s\n' "$*" >&2; exit 1; }
cd "$plan"

expected_files=$(printf '%s\n' \
  "$slice_rel/artifacts/semantic-membership.json" \
  "$slice_rel/artifacts/semantic-evidence.md" \
  "$slice_rel/artifacts/validation-evidence.md" \
  "$slice_rel/artifacts/handoff.md" \
  "$slice_rel/ledger.md" \
  "$slice_rel/closing-report.md" | sort)
if [ "$precommit" = 1 ]; then
  [ -z "$cc_commit" ] || fail "precommit must not receive CC_COMMIT"
  actual_files=$( { git diff --name-only "$opening_planning" --; git diff --cached --name-only "$opening_planning" --; git ls-files --others --exclude-standard; } | sort -u )
  [ "$actual_files" = "$expected_files" ] || fail "precommit six-file union differs"
  git diff --check "$opening_planning" --
  git diff --cached --check
  registry=$plan/$membership_rel
  evidence_doc=$plan/$slice_rel/artifacts/semantic-evidence.md
  mode=precommit
else
  [ -n "$cc_commit" ] || fail "committed mode requires CC_COMMIT"
  [ -n "$replay_commit" ] || fail "committed mode requires REPLAY_COMMIT"
  git cat-file -e "$cc_commit^{commit}" || fail "CC_COMMIT is not a commit"
  git cat-file -e "$replay_commit^{commit}" || fail "REPLAY_COMMIT is not a commit"
  git diff --name-only "$opening_planning" "$cc_commit" | sort > "$tmp/committed-files"
  [ "$(cat "$tmp/committed-files")" = "$expected_files" ] || fail "committed six-file scope differs"
  git diff --check "$opening_planning" "$cc_commit"
  dirty=$(git status --porcelain --untracked-files=all)
  [ -z "$dirty" ] || fail "planning checkout is dirty"
  git show "$cc_commit:$membership_rel" > "$tmp/semantic-membership.json"
  git show "$cc_commit:$slice_rel/artifacts/semantic-evidence.md" > "$tmp/semantic-evidence.md"
  registry=$tmp/semantic-membership.json
  evidence_doc=$tmp/semantic-evidence.md
  mode=committed
fi

[ "$(git rev-parse "$opening_planning")" = "$opening_planning" ] || fail "opening planning authority unavailable"
[ "$(git -C "$source" rev-parse "$opening_source")" = "$opening_source" ] || fail "source authority unavailable"
dirty_source=$(git -C "$source" status --porcelain --untracked-files=all)
[ -z "$dirty_source" ] || fail "source checkout is dirty"
source_current=$(git -C "$source" rev-parse HEAD)
git -C "$source" diff --exit-code "$opening_source" "$source_current" -- knowledge/concept-cards knowledge/agent-coordination
jq empty "$registry" >/dev/null || fail "membership registry is invalid JSON"
inventory=$tmp/inventory.json
git show "$opening_planning:$inventory_rel" > "$inventory"
[ "$(shasum -a 256 "$inventory" | awk '{print $1}')" = "$inventory_sha" ] || fail "frozen inventory hash differs"

set_b=$(git show "$set_authority:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/crc-escalation02.md" | awk '/^~~~json$/{p=1;next} p && /^~~~$/{p=0;next} p' | jq -s -c '.[1]')
coverage=$(git show "$opening_planning:$coverage_rel")
transition=$(git show "$opening_planning:$transition_rel")
assignment=$set_b
jq -n -e --argjson b "$set_b" --argjson c "$coverage" '
  ($b|length)==22 and ($b|unique|length)==22 and
  ($b-$c.remaining_pairs|length)==0 and ($b-$c.accepted_pairs|length)==22 and
  $c.counts=={full:555,accepted:238,remaining:317,next_slice:22,not_yet_sliced:295} and
  $c.next_slice=="arc06-semantic-families-and-capability-requirements/slice18-run-scope-workers-and-outputs" and
  ($c.next_slice_pairs|sort)==($b|sort)' >/dev/null || fail "Set B or opening coverage failed"
jq -n -e --argjson c "$transition" '$c.counts=={full:555,accepted:115,remaining:440,next_slice:35,not_yet_sliced:405}' >/dev/null || fail "frozen transition failed"

check_registry() {
  candidate=$1
  jq -e --argjson assignment "$assignment" '
    (.scope.assignment==$assignment) and
    (.scope.counts=={full:555,accepted:238,remaining:317,assigned:22,outside:295}) and
    (.scope.assignment_is_acceptance==false) and (.scope.outside_complement==248) and
    (.memberships|length)==22 and
    ((.memberships|map([.field_path,.record_kind])|sort)==($assignment|sort)) and
    ((.memberships|map(.meaning_id)|unique|length)==22) and
    (([.memberships[]|select((has("field_path") and has("record_kind") and has("meaning_id") and has("effective_meaning") and has("applicability") and has("observed_states") and has("evidence_ids") and has("exceptions") and (.consequences|type)=="object" and ((.consequences|keys|sort)==["extractor","migration","query","reader"]) and has("unresolved_questions") and has("disposition"))|not)]|length)==0) and
    ((([.memberships[].evidence_ids[]]|unique)-(.evidence_registry|map(.evidence_id)))|length)==0 and
    ((.evidence_registry|map(.evidence_id)|unique|length)==(.evidence_registry|length))
  ' "$candidate" >/dev/null
}
check_registry "$registry" || fail "registry boundary or required fields failed"
for field in $(printf '%s' "$assignment" | jq -r '.[] | .[0]'); do grep -Fq "$field" "$evidence_doc" || fail "semantic evidence omits $field"; done

resolve_snapshot() {
  row=$1
  root=$(jq -r '.root' <<< "$row")
  path=$(jq -r '.path' <<< "$row")
  authority=$(jq -r '.authority_commit' <<< "$row")
  [ "$(jq -r '.read_mode' <<< "$row")" = snapshot ] || return 1
  case "$root" in
    planning)
      case "$authority" in "$opening_planning"|"$predecessor_planning"|"$set_authority") git show "$authority:$path" ;; *) return 1;; esac ;;
    source)
      [ "$authority" = "$opening_source" ] || return 1
      git -C "$source" show "$authority:$path" ;;
    *) return 1 ;;
  esac
}

check_evidence() {
  candidate=$1
  n=0
  while IFS= read -r row; do
    evidence_id=$(jq -r '.evidence_id' <<< "$row")
    sha=$(jq -r '.sha256' <<< "$row")
    source_range=$(jq -r '.source_range' <<< "$row")
    [ "$evidence_id" != null ] && printf '%s' "$sha" | grep -Eq '^[0-9a-f]{64}$' || return 1
    jq -e 'has("evidence_id") and has("root") and has("path") and has("read_mode") and has("authority_commit") and has("sha256") and has("role") and has("member_scope") and has("source_range") and has("interpretation") and has("limit")' <<< "$row" >/dev/null || return 1
    snapshot=$tmp/evidence-$n
    resolve_snapshot "$row" > "$snapshot" || return 1
    [ "$(shasum -a 256 "$snapshot" | awk '{print $1}')" = "$sha" ] || return 1
    if [ "$source_range" = "JSON document" ]; then
      jq empty "$snapshot" >/dev/null || return 1
    else
      case "$source_range" in lines*) spans=$(printf '%s' "$source_range" | sed 's/^lines //');; *) return 1;; esac
      line_count=$(wc -l < "$snapshot" | tr -d ' ')
      for span in $(printf '%s' "$spans" | tr ',' ' '); do
        start=$(printf '%s' "$span" | cut -d- -f1)
        end=$(printf '%s' "$span" | cut -d- -f2)
        printf '%s' "$start" | grep -Eq '^[0-9]+$' || return 1
        printf '%s' "$end" | grep -Eq '^[0-9]+$' || return 1
        [ "$start" -ge 1 ] && [ "$start" -le "$end" ] && [ "$end" -le "$line_count" ] || return 1
        [ "$(awk -v s="$start" -v e="$end" 'NR>=s && NR<=e{n++} END{print n+0}' "$snapshot")" -eq "$((end-start+1))" ] || return 1
      done
    fi
    n=$((n+1))
  done < <(jq -c '.evidence_registry[]' "$candidate")
}
check_evidence "$registry" || fail "authority/hash/range registry failed"

expected_population='[
  {"record":"parallel","frontmatter":true,"error":null,"keys":["extraction_confidence","id","input_source_ref","memory_admission_refs","prepared_source_ref","preservation_decision_refs","reconciliation_result_refs","record_type","revision","surface_class","synthetic","validation_result_refs","verification_result_refs","worker_scope"]},
  {"record":"template","frontmatter":true,"error":null,"keys":["actor","actual_coverage","agent_scope","extraction_confidence","finished_at","id","intended_outputs","intended_scope","memory_admission_refs","method_ref","old_card_inputs","operation","output_refs","parallel_worker_count","prepared_source_refs","preservation_refs","prior_run_refs","prompt_ref","reconciliation_refs","record_type","revision","settings","source_snapshot_refs","started_at","validation_refs","verification_refs","worker_outputs"]},
  {"record":"trace","frontmatter":true,"error":null,"keys":["extraction_confidence","id","input_source_ref","memory_admission_refs","output_refs","prepared_source_ref","preservation_decision_refs","reconciliation_result_refs","record_type","revision","surface_class","synthetic","validation_result_refs","verification_result_refs","worker_scope"]}
]'
actual_population=$(jq -c 'def rn: if (.path|endswith("knowledge/concept-cards/templates/extraction-run.md")) then "template" elif (.path|contains("extraction-run-trace.md")) then "trace" else "parallel" end; [.records[]|select(.record_kind=="extraction-run")|{record:rn,frontmatter,error:(.error//null),keys:(.values|keys)}]|sort_by(.record)' "$inventory")
jq -n -e --argjson a "$actual_population" --argjson e "$expected_population" '$a==$e' >/dev/null || fail "native extraction-run population differs"

matrix_filter='
  def leaf($x): $x | if .==null then {state:"null",value:null} elif (type=="array" and length==0) then {state:"empty-list",value:.} elif (type=="object" and length==0) then {state:"empty-mapping",value:.} elif type=="array" then {state:"populated-sequence",value:.} elif type=="object" then {state:"populated-mapping",value:.} else {state:("populated-"+type),value:.} end;
  def kind: if type=="array" then "sequence" elif type=="object" then "mapping" else type end;
  def lookup($v;$parts): reduce $parts[] as $k ({present:true,value:$v}; if .present and (.value|type)=="object" and (.value|has($k)) then {present:true,value:.value[$k]} else {present:false,value:null} end);
  def state_at($v;$path):
    if ($path|contains("[]")) then ($path|split("[]")) as $parts | (lookup($v;($parts[0]|split(".")))) as $parent |
      if $parent.present|not then {state:"parent-absent",value:null} elif ($parent.value|type)!="array" then {state:("parent-unexpected-"+($parent.value|kind)),value:$parent.value} elif ($parts[1]=="" and $path=="output_refs[]") then leaf($parent.value)
      else ($parts[1][1:]|split(".")) as $child | if ($parent.value|length)==0 then {state:"empty-sequence",value:[]} else {state:(if $path=="worker_scope.roles[]" then "sequence-elements" else "sequence-element-children" end),value:([$parent.value|to_entries[]|. as $e|if ($e.value|type)!="object" then ({index:$e.key} + (leaf($e.value))) else (lookup($e.value;$child)) as $c|if $c.present then ({index:$e.key} + (leaf($c.value))) else {index:$e.key,state:"element-child-absent",value:null} end end])} end end
    elif ($path|contains(".")) then ($path|split(".")) as $parts | (lookup($v;[$parts[0]])) as $parent | if $parent.present|not then {state:"parent-absent",value:null} elif ($parent.value|type)!="object" then {state:("parent-unexpected-"+($parent.value|kind)),value:$parent.value} elif ($parent.value|has($parts[1])|not) then {state:"child-absent",value:null} else leaf($parent.value[$parts[1]]) end
    else if ($v|has($path)|not) then {state:"absent",value:null} else leaf($v[$path]) end end;
  def rn: if (.path|endswith("knowledge/concept-cards/templates/extraction-run.md")) then "template" elif (.path|contains("extraction-run-trace.md")) then "trace" else "parallel" end;
  [.records[]|select(.record_kind=="extraction-run")|. as $r|{key:($r|rn),value:(reduce ($paths[]) as $p ({}; .[$p[0]]=state_at($r.values;$p[0])))}]|sort_by(.key)|from_entries
'
actual_matrix=$(jq -c --argjson paths "$assignment" "$matrix_filter" "$inventory")
matrix_blocks=$(awk '/^~~~json$/{n++;if(n==1){p=1;next}} p && /^~~~$/{p=0} p' "$evidence_doc")
[ "$(printf '%s\n' "$matrix_blocks" | jq -s 'length')" = 1 ] || fail "expected matrix block count differs"
expected_matrix=$(printf '%s\n' "$matrix_blocks" | jq -c .)
jq -n -e --argjson a "$actual_matrix" --argjson e "$expected_matrix" '$a==$e' >/dev/null || fail "native 3x22 state/value matrix differs"

yaml_errors=$(jq -c '[.records[]|select((.error? // "")|contains("YAML::XS"))|.path]|sort' "$inventory")
no_frontmatter=$(jq -c '[.records[]|select(.error?=="no-opening-frontmatter")|.path]|sort' "$inventory")
expected_yaml='["workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-memory-forms.md","workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-priming-forms.md","workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-recognition-dual-process.md"]'
expected_no_frontmatter='[".worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/README.md",".worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards/README.md","knowledge/concept-cards/references/README.md","knowledge/concept-cards/references/operator-review-gates.md","knowledge/concept-cards/references/record-field-groups.md","knowledge/concept-cards/references/semantic-audit-boundaries.md","knowledge/concept-cards/references/structural-validation-candidates.md","knowledge/concept-cards/references/vocabulary.md","workbench/compcogneuro-rich-rerun-2026-09-12/README.md","workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/INDEX.md","workbench/compcogneuro-rich-rerun-2026-09-12/comparison/evaluation-rubric.md","workbench/compcogneuro-rich-rerun-2026-09-12/comparison/subset-comparison.md","workbench/compcogneuro-teaching-rerun-2026-09-12/README.md","workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/INDEX.md","workbench/compcogneuro-teaching-rerun-2026-09-12/comparison/teaching-profile-comparison.md"]'
[ "$yaml_errors" = "$expected_yaml" ] || fail "YAML exclusions differ"
[ "$no_frontmatter" = "$expected_no_frontmatter" ] || fail "no-frontmatter exclusions differ"

historical=$(jq -c '[.records[]|select(has("values") and (.values|type)=="object")|select((.path|startswith("/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/")) or (.path|startswith("knowledge/erlang/concept-cards/")))] as $r | {parsed_records:($r|length),root_presence:([ "actual_coverage","agent_scope","intended_outputs","intended_scope","output_refs","parallel_worker_count","worker_outputs","worker_scope" ] as $keys | reduce $keys[] as $k ({}; .[$k]=([$r[]|select(.values|has($k))]|length)))}' "$inventory")
expected_historical='{"parsed_records":2054,"root_presence":{"actual_coverage":0,"agent_scope":0,"intended_outputs":0,"intended_scope":0,"output_refs":0,"parallel_worker_count":0,"worker_outputs":0,"worker_scope":0}}'
jq -n -e --argjson a "$historical" --argjson e "$expected_historical" '$a==$e' >/dev/null || fail "historical comparison differs"

trace_refs=$(jq -c '.records[]|select(.path=="knowledge/concept-cards/examples/extraction-run-trace.md")|.values.output_refs' "$inventory")
target_results=$(jq -c --argjson refs "$trace_refs" '[.records[]|select(has("values"))] as $records | [$refs[] as $ref | {ref:$ref,matches:[$records[]|select(.values.id?==$ref.id and .record_kind==$ref.record_type and .values.revision?==$ref.revision)|{path,record_kind,id:.values.id,revision:.values.revision}],match_count:([$records[]|select(.values.id?==$ref.id and .record_kind==$ref.record_type and .values.revision?==$ref.revision)]|length)}]' "$inventory")
expected_targets='[{"ref":{"id":"cc-claim-support-is-assertion-specific","revision":1,"record_type":"concept-card"},"matches":[{"path":"knowledge/concept-cards/examples/claim-backed-card.md","record_kind":"concept-card","id":"cc-claim-support-is-assertion-specific","revision":1}],"match_count":1},{"ref":{"id":"claim-support-is-assertion-specific","revision":1,"record_type":"claim"},"matches":[],"match_count":0}]'
jq -n -e --argjson a "$target_results" --argjson e "$expected_targets" '$a==$e' >/dev/null || fail "target lookup differs"

compare_failure() {
  name=$1; actual=$2; expected=$3
  if jq -n -e --argjson a "$actual" --argjson e "$expected" '$a==$e' >/dev/null; then fail "$name unexpectedly matched"; else status=$?; [ "$status" = 1 ] || fail "$name returned status $status"; fi
}
matrix_mutation_reject() {
  name=$1; filter=$2; mutated=$tmp/matrix-$name.json
  jq "$filter" "$inventory" > "$mutated"
  changed=$(jq -c --argjson paths "$assignment" "$matrix_filter" "$mutated")
  compare_failure "$name" "$changed" "$expected_matrix"
  printf 'control.%s.status=1 classification=comparison_failure\n' "$name"
}
matrix_mutation_reject "mapping_to_sequence" '.records |= map(if .path=="knowledge/concept-cards/templates/extraction-run.md" then .values.output_refs=[] else . end)'
matrix_mutation_reject "sequence_to_mapping" '.records |= map(if .path=="knowledge/concept-cards/examples/extraction-run-trace.md" then .values.output_refs={"cards":[]} else . end)'
matrix_mutation_reject "remove_mapping_child" '.records |= map(if .path=="knowledge/concept-cards/templates/extraction-run.md" then del(.values.output_refs.cards) else . end)'
matrix_mutation_reject "scalar_mapping_child" '.records |= map(if .path=="knowledge/concept-cards/templates/extraction-run.md" then .values.output_refs.cards="wrong" else . end)'
matrix_mutation_reject "mapping_child_on_sequence" '.records |= map(if .path=="knowledge/concept-cards/examples/extraction-run-trace.md" then .values.output_refs += [{"cards":[]}] else . end)'
matrix_mutation_reject "remove_element_child" '.records |= map(if .path=="knowledge/concept-cards/examples/extraction-run-trace.md" then del(.values.output_refs[0].record_type) else . end)'
matrix_mutation_reject "change_element_revision" '.records |= map(if .path=="knowledge/concept-cards/examples/extraction-run-trace.md" then .values.output_refs[0].revision=99 else . end)'
matrix_mutation_reject "scalar_element" '.records |= map(if .path=="knowledge/concept-cards/examples/extraction-run-trace.md" then .values.output_refs[0]=1 else . end)'
matrix_mutation_reject "null_count_to_zero" '.records |= map(if .path=="knowledge/concept-cards/templates/extraction-run.md" then .values.parallel_worker_count=0 else . end)'
matrix_mutation_reject "copy_count_surface" '.records |= map(if .path=="knowledge/concept-cards/templates/extraction-run.md" then .values.parallel_worker_count=1 else . end)'
matrix_mutation_reject "worker_count_string" '.records |= map(if .path=="knowledge/concept-cards/examples/parallel-worker-default-recipe.md" then .values.worker_scope.worker_count="2" else . end)'
matrix_mutation_reject "remove_worker_scope" '.records |= map(if .path=="knowledge/concept-cards/examples/extraction-run-trace.md" then del(.values.worker_scope) else . end)'
matrix_mutation_reject "roles_scalar" '.records |= map(if .path=="knowledge/concept-cards/examples/extraction-run-trace.md" then .values.worker_scope.roles="extractor" else . end)'
matrix_mutation_reject "mode_role_swap" '.records |= map(if .path=="knowledge/concept-cards/examples/extraction-run-trace.md" then .values.worker_scope.mode=.values.worker_scope.roles[0] else . end)'
matrix_mutation_reject "backfill_worker_outputs" '.records |= map(if .path=="knowledge/concept-cards/examples/parallel-worker-default-recipe.md" then .values.worker_outputs=[] else . end)'
matrix_mutation_reject "empty_to_absent" '.records |= map(if .path=="knowledge/concept-cards/templates/extraction-run.md" then del(.values.worker_outputs) else . end)'
matrix_mutation_reject "null_scope_to_absent" '.records |= map(if .path=="knowledge/concept-cards/templates/extraction-run.md" then del(.values.intended_scope) else . end)'

expect_evidence_failure() {
  name=$1; filter=$2; mutated=$tmp/evidence-$name.json
  jq "$filter" "$registry" > "$mutated"
  if check_evidence "$mutated"; then fail "$name unexpectedly passed"; else status=$?; [ "$status" != 0 ] || fail "$name had no failure"; fi
  printf 'control.%s.status=%s classification=authority_or_range_failure\n' "$name" "$status"
}
expect_evidence_failure "wrong_authority" '.evidence_registry[0].authority_commit="0000000000000000000000000000000000000000000000000000000000000000"'
expect_evidence_failure "wrong_digest" '.evidence_registry[0].sha256="0000000000000000000000000000000000000000000000000000000000000000"'
expect_evidence_failure "out_of_bounds_range" '.evidence_registry[0].source_range="lines 999-1000"'
expect_evidence_failure "unknown_range" '.evidence_registry[0].source_range="unknown"'

mutated_registry=$tmp/accepted-addition.json
jq '.memberships += [{"field_path":"outside-added","record_kind":"extraction-run","meaning_id":"outside-added","effective_meaning":"wrong","applicability":"wrong","observed_states":{},"evidence_ids":[],"exceptions":[],"consequences":{"reader":"x","extractor":"x","query":"x","migration":"x"},"unresolved_questions":[],"disposition":"wrong"}]' "$registry" > "$mutated_registry"
if check_registry "$mutated_registry"; then fail "outside addition unexpectedly passed"; else status=$?; [ "$status" != 0 ] || fail "outside addition had no failure"; fi
printf 'control.accepted-outside-addition.status=%s classification=scope_failure\n' "$status"

set +e
jq -c '.records[]' "$tmp/no-such-inventory.json" > "$tmp/missing.stdout" 2> "$tmp/missing.stderr"
missing_status=$?
git -C "$plan" show 0000000000000000000000000000000000000000:no-such-path > "$tmp/git.stdout" 2> "$tmp/git.stderr"
invalid_git_status=$?
set -e
[ "$missing_status" = 2 ] && [ ! -s "$tmp/missing.stdout" ] && [ -s "$tmp/missing.stderr" ] || fail "missing inventory control failed"
[ "$invalid_git_status" = 128 ] && [ ! -s "$tmp/git.stdout" ] && [ -s "$tmp/git.stderr" ] || fail "invalid Git authority control failed"
printf 'control.missing-inventory.status=%s classification=tool_error stderr_nonempty=true\n' "$missing_status"
printf 'control.invalid-git-authority.status=%s classification=tool_error stderr_nonempty=true\n' "$invalid_git_status"
printf 'mode=%s source=%s planning_opening=%s\n' "$mode" "$source_current" "$opening_planning"
printf 'population=3-extraction-runs yaml-errors=3 no-frontmatter=15 historical=2054-zero-set-b-roots\n'
printf 'coverage=555/238/317/22/295 matrix=3x22 target=one-match-one-successful-no-match\n'
printf 'json=valid registry=valid evidence=authority-hash-range-valid source=clean scope=six-files\n'
~~~

## Committed endpoint wrapper

~~~bash
set -euo pipefail
source=/Users/oubiwann/lab/billosys/ai-engineering
plan=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
route_doc=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice18-run-scope-workers-and-outputs/artifacts/validation-evidence.md
cc_commit=$(printenv CC_COMMIT 2>/dev/null || true)
replay_commit=$(printenv REPLAY_COMMIT 2>/dev/null || true)
[ -n "$cc_commit" ] || { printf 'CC_COMMIT is required\n' >&2; exit 2; }
[ -n "$replay_commit" ] || { printf 'REPLAY_COMMIT is required\n' >&2; exit 2; }
git -C "$plan" cat-file -e "$cc_commit^{commit}" || exit 2
git -C "$plan" cat-file -e "$replay_commit^{commit}" || exit 2
route=$(git -C "$plan" show "$replay_commit:$route_doc" | awk '/^## Literal route$/{p=1;next} /^## Committed endpoint wrapper$/{exit} p && /^~~~bash$/{n++;if(n==1){q=1;next}} q && /^~~~$/{q=0;next} q && p{print}')
[ -n "$route" ] || { printf 'missing route\n' >&2; exit 2; }
count=$(printf '%s\n' "$route" | wc -l | tr -d ' ')
[ "$count" -gt 0 ] || exit 2
bash -n <<< "$route" || exit 2
CC_COMMIT="$cc_commit" REPLAY_COMMIT="$replay_commit" bash <<< "$route"
~~~

## Recorded precommit and replay results

Precommit is run from the canonical planning checkout root with
`CC_PRECOMMIT=1` after the six authorized paths exist. The committed route
is then run through the wrapper with distinct `CC_COMMIT` and
`REPLAY_COMMIT` endpoints; valid same-endpoint and distinct-recipe endpoints
must both return 0. Opening-planning, foreign-source and absent recipe
endpoints are wrapper extraction failures and remain nonzero with no route
execution. All mutation controls must fail through the same predicates;
successful no-match remains status 0 and tool errors retain nonempty stderr.

### Precommit run

The literal route was extracted from this file, passed `bash -n`, and run
with `CC_PRECOMMIT=1` from the planning checkout. Final status was `0`.
Positive output recorded:

~~~text
control.mapping_to_sequence.status=1 classification=comparison_failure
control.sequence_to_mapping.status=1 classification=comparison_failure
control.remove_mapping_child.status=1 classification=comparison_failure
control.scalar_mapping_child.status=1 classification=comparison_failure
control.mapping_child_on_sequence.status=1 classification=comparison_failure
control.remove_element_child.status=1 classification=comparison_failure
control.change_element_revision.status=1 classification=comparison_failure
control.scalar_element.status=1 classification=comparison_failure
control.null_count_to_zero.status=1 classification=comparison_failure
control.copy_count_surface.status=1 classification=comparison_failure
control.worker_count_string.status=1 classification=comparison_failure
control.remove_worker_scope.status=1 classification=comparison_failure
control.roles_scalar.status=1 classification=comparison_failure
control.mode_role_swap.status=1 classification=comparison_failure
control.backfill_worker_outputs.status=1 classification=comparison_failure
control.empty_to_absent.status=1 classification=comparison_failure
control.null_scope_to_absent.status=1 classification=comparison_failure
control.wrong_authority.status=1 classification=authority_or_range_failure
control.wrong_digest.status=1 classification=authority_or_range_failure
control.out_of_bounds_range.status=1 classification=authority_or_range_failure
control.unknown_range.status=1 classification=authority_or_range_failure
control.accepted-outside-addition.status=1 classification=scope_failure
control.missing-inventory.status=2 classification=tool_error stderr_nonempty=true
control.invalid-git-authority.status=128 classification=tool_error stderr_nonempty=true
mode=precommit source=ce3f77103eff5e07b3533a03c65f158684fc1039 planning_opening=961c748f7915c71ba59ef37a2dd65253800be268
population=3-extraction-runs yaml-errors=3 no-frontmatter=15 historical=2054-zero-set-b-roots
coverage=555/238/317/22/295 matrix=3x22 target=one-match-one-successful-no-match
json=valid registry=valid evidence=authority-hash-range-valid source=clean scope=six-files
route_status=0
~~~

Exploratory failures were retained during route construction: an invalid jq
array projection (`.[].0`), a predecessor-review digest/range copied from the
working planning tree rather than its pinned commit, a zero-argument jq leaf
function called with an argument, matrix shape/state-label mismatches, a jq
optional-field spacing parse error, and one unmatched historical jq delimiter.
Each failed attempt stopped before any commit, and the route was corrected and
re-run to the passing result above. The committed replay and endpoint-control
results are recorded below.

### First committed endpoint

`CC_COMMIT=13d219abd00d6b879f87da199837beb6c9a31090` and the same value for
`REPLAY_COMMIT` were passed through the committed wrapper extracted from the
committed validation artifact. `bash -n` passed and the wrapper returned `0`.
Its output was identical to the precommit control and summary block except
for `mode=committed`; the route reported `source=ce3f77103eff5e07b3533a03c65f158684fc1039`,
`planning_opening=961c748f7915c71ba59ef37a2dd65253800be268`,
`population=3-extraction-runs`, `matrix=3x22`, `target=one-match-one-successful-no-match`,
and `json=valid registry=valid evidence=authority-hash-range-valid source=clean scope=six-files`.
All 17 matrix mutations, four authority/range mutations, the outside-addition
scope control, and the two tool-error controls retained their recorded
nonzero classifications.

### Distinct recipe endpoint and endpoint controls

The distinct recipe endpoint is
`2ab6679718326fc76ecf2e10d3678f385f086eb0`. The wrapper extracted from that
commit was syntax-checked and run with
`CC_COMMIT=13d219abd00d6b879f87da199837beb6c9a31090` and
`REPLAY_COMMIT=2ab6679718326fc76ecf2e10d3678f385f086eb0`. It returned `0` and
reported the same positive population, coverage, matrix, target and control
results as the first committed endpoint.

The wrapper fail-closed endpoint controls were run with the same CC commit:

~~~text
endpoint.opening.status=128 stdout_empty=true stderr_nonempty=true
endpoint.foreign-source.status=128 stdout_empty=true stderr_nonempty=true
endpoint.absent-recipe.status=2 stdout_empty=true stderr_nonempty=true
~~~

The opening endpoint failed because the route file did not exist at the
opening planning commit; the foreign-source endpoint failed because the
source commit did not contain the planning route; and the all-zero endpoint
failed Git object validation. None executed the route.

## Failed or unrun checks

No source package, install, runtime, graph, memory, real-extraction, UAT or
coverage gate is authorized or run. CRC independent replay, CDC composition and
Operator acceptance are pending. Any exploratory failure, command status,
stderr-presence result and correction must be appended here without replacing
the original attempt.
