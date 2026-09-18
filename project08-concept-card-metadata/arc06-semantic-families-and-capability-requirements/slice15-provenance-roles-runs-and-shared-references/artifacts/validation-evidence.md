# Slice15 validation evidence: literal native replay

Status: CC proposed-done; independent CRC verification is required. This is a
structural evidence route, not a semantic-acceptance verdict.

## Boundaries and modes

The route uses only Bash, Git, jq, shasum, awk, and the frozen native
inventory. Precommit mode reads the working-tree registry and checks the
staged/unstaged/named-new union. Committed mode requires both `CC_COMMIT` and
`REPLAY_COMMIT`, reads the registry from `CC_COMMIT`, extracts this literal
route from `REPLAY_COMMIT`, checks the opening-to-CC six-file contribution, and
requires clean source and planning checkouts. The route does not change source,
schema, extraction, graph/runtime, memory, coverage acceptance, reviewer
status, or UAT.

## Literal route

The committed wrapper is:

~~~text
CC_COMMIT=<cc-endpoint> REPLAY_COMMIT=<recipe-endpoint> bash -c '
set -euo pipefail
recipe=$(git show "$REPLAY_COMMIT:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references/artifacts/validation-evidence.md") || exit 2
code=$(printf "%s\n" "$recipe" | awk '/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p') || exit 2
[[ -n "$code" ]] || exit 2
printf "%s\n" "$code" | bash -s
'
~~~

The precommit wrapper is:

~~~text
CC_PRECOMMIT=1 bash -s < <(awk '/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p' project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references/artifacts/validation-evidence.md)
~~~

~~~bash
set -euo pipefail

fail() { printf '%s\n' "FAIL: $*" >&2; exit 1; }

root=$(git rev-parse --show-toplevel)
source=$(cd "$root/../.." && pwd)
slice_rel=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references
membership_rel=$slice_rel/artifacts/semantic-membership.json
validation_rel=$slice_rel/artifacts/validation-evidence.md
coverage_rel=project08-concept-card-metadata/artifacts/semantic-coverage-current.json
transition_rel=project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
inventory_rel=project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
opening_source=ce3f77103eff5e07b3533a03c65f158684fc1039
opening_planning=ea200f07c38c43b85991426804dea10a4e250743
mode=precommit

temp=$(mktemp -d)
trap 'rm -rf "$temp"' EXIT HUP INT TERM

if [[ -n "${CC_COMMIT:-}" ]]; then
  mode=committed
  [[ -n "${REPLAY_COMMIT:-}" ]] || fail "REPLAY_COMMIT is required with CC_COMMIT"
  git cat-file -e "$CC_COMMIT^{commit}" || fail "CC_COMMIT is not a commit"
  git cat-file -e "$REPLAY_COMMIT^{commit}" || fail "REPLAY_COMMIT is not a commit"
  git show "$CC_COMMIT:$membership_rel" > "$temp/semantic-membership.json" || fail "registry is absent from CC_COMMIT"
  registry=$temp/semantic-membership.json
else
  [[ "${CC_PRECOMMIT:-}" == "1" ]] || fail "set CC_PRECOMMIT=1 or provide CC_COMMIT"
  registry=$root/$membership_rel
  [[ -s "$registry" ]] || fail "working-tree registry is absent or empty"
fi

[[ "$root" == /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning ]] || fail "route must run from the canonical planning checkout"
source_current=$(git -C "$source" rev-parse HEAD)
[[ -z "$(git -C "$source" status --porcelain --untracked-files=all)" ]] || fail "source checkout is not clean"
git diff --check || fail "planning working tree has whitespace errors"
git diff --cached --check || fail "planning index has whitespace errors"
git -C "$source" diff --exit-code "$opening_source" "$source_current" -- knowledge/concept-cards knowledge/document-extraction || fail "registered relevant source tree differs from opening source"

allowed_paths="$membership_rel
$slice_rel/artifacts/semantic-evidence.md
$validation_rel
$slice_rel/artifacts/handoff.md
$slice_rel/ledger.md
$slice_rel/closing-report.md"
is_allowed() {
  case "$1" in
    "$membership_rel"|"$slice_rel/artifacts/semantic-evidence.md"|"$validation_rel"|"$slice_rel/artifacts/handoff.md"|"$slice_rel/ledger.md"|"$slice_rel/closing-report.md") return 0 ;;
    *) return 1 ;;
  esac
}
if [[ "$mode" == precommit ]]; then
  changed_paths=$( { git diff --cached --name-only; git diff --name-only; git ls-files --others --exclude-standard; } | sort -u )
  [[ -n "$changed_paths" ]] || fail "precommit union is empty"
  while IFS= read -r path; do [[ -z "$path" ]] && continue; is_allowed "$path" || fail "out-of-scope precommit path: $path"; done <<< "$changed_paths"
else
  [[ -z "$(git -C "$root" status --porcelain --untracked-files=all)" ]] || fail "planning checkout is not clean for committed replay"
  committed_paths=$(git diff --name-only "$opening_planning" "$CC_COMMIT" | sort -u)
  [[ -n "$committed_paths" ]] || fail "committed CC contribution is empty"
  while IFS= read -r path; do [[ -z "$path" ]] && continue; is_allowed "$path" || fail "out-of-scope opening-to-CC path: $path"; done <<< "$committed_paths"
fi

protected_paths="project08-concept-card-metadata/AGENTS.md
project08-concept-card-metadata/project-plan.md
project08-concept-card-metadata/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/arc-plan.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/ledger.md
$slice_rel/slice-plan.md
$slice_rel/cc-prompt.md
$slice_rel/cc-prompt-iteration01.md
$slice_rel/crc-verification.md
$coverage_rel
$transition_rel
$inventory_rel"
for path in $protected_paths; do git diff --exit-code "$opening_planning" -- "$path" >/dev/null || fail "protected planning path changed: $path"; done

jq empty "$registry" || fail "registry is not valid JSON"
assignment_json=$(git show "$opening_planning:$slice_rel/slice-plan.md" | awk '/^~~~json$/{n++; if (n == 1) {p=1; next}} p && /^~~~$/{exit} p')
[[ -n "$assignment_json" ]] || fail "opening assignment block is absent"
kinds_json=$(jq -c '[.[][1]] | unique' <<< "$assignment_json")
jq -e --argjson assignment "$assignment_json" '.scope.assignment == $assignment and (.scope.assignment | length == 8) and ((.scope.assignment | map(@json) | unique | length) == 8) and .scope.counts == {full:555, accepted:200, remaining:355, assigned:8, outside:347}' "$registry" >/dev/null || fail "registry scope or exact assignment failed"
jq -e --argjson assignment "$assignment_json" '.counts == {full:555, accepted:200, remaining:355, next_slice:8, not_yet_sliced:347} and ((.accepted_pairs|map(@json)|unique|length)==.counts.accepted) and ((.remaining_pairs|map(@json)|unique|length)==.counts.remaining) and ((.next_slice_pairs|map(@json)|unique|length)==.counts.next_slice) and ((.accepted_pairs|map(@json)|sort) as $a | (.remaining_pairs|map(@json)|sort) as $r | (($a-$r)|length)==($a|length)) and ((.next_slice_pairs|map(@json)|sort)==($assignment|map(@json)|sort)) and (((($assignment|map(@json)|sort)-(.remaining_pairs|map(@json)|sort))|length)==0) and (((($assignment|map(@json)|sort)-(.accepted_pairs|map(@json)|sort))|length)==8)' < <(git show "$opening_planning:$coverage_rel") >/dev/null || fail "opening coverage boundary failed"
jq -e '.counts == {full:555, accepted:115, remaining:440, next_slice:35, not_yet_sliced:405} and (.counts.accepted + .counts.remaining == .counts.full) and (.counts.next_slice + .counts.not_yet_sliced == .counts.remaining)' < <(git show "$opening_planning:$transition_rel") >/dev/null || fail "frozen transition counts failed"

inventory=$temp/inventory.json
git show "$opening_planning:$inventory_rel" > "$inventory" || fail "opening inventory is absent"

actual_census=$(jq -c --argjson kinds "$kinds_json" '
  def parent_state:
    if ((.values | has("actor")) | not) then "absent"
    elif .values.actor == null then "null"
    elif ((.values.actor | type) == "object" and (.values.actor | length) == 0) then "empty_object"
    elif (.values.actor | type) == "object" then "object"
    else "unexpected_type" end;
  def child_state($child):
    if parent_state == "absent" then "not_applicable_parent_absent"
    elif parent_state != "object" then "unexpected_type"
    elif ((.values.actor | has($child)) | not) then "missing_in_object"
    elif .values.actor[$child] == null then "null"
    elif ((.values.actor[$child] | type) == "string" and .values.actor[$child] == "") then "empty_string"
    elif (.values.actor[$child] | type) == "string" then "string"
    else "unexpected_type" end;
  def family_name:
    if (.path | startswith("knowledge/concept-cards/templates/")) then "template"
    elif (.path | startswith("knowledge/concept-cards/examples/")) then "synthetic"
    elif (.path | contains("slice02-pilot-markdown-preparation-and-card-extraction/")) then "pilot"
    elif (.path | contains("slice04-expanded-corpus-card-generation/")) then "expanded"
    elif (.path | contains("compcogneuro-rich-rerun-")) then "rich"
    elif (.path | contains("compcogneuro-teaching-rerun-")) then "teaching"
    else "unknown" end;
  def state_counts($rows;$child): reduce ["not_applicable_parent_absent","missing_in_object","null","empty_string","string","unexpected_type"][] as $s ({}; .[$s] = ($rows | map(select(child_state($child) == $s)) | length));
  . as $doc
  | [.records[] | select(.frontmatter == true and (.values? != null) and ((.values | type) == "object") and (.record_kind as $kind | ($kinds | index($kind)) != null))] as $r
  | {
      parsed_selected_mappings: ($r | length),
      record_kind_counts: ($r | group_by(.record_kind) | map({key: .[0].record_kind, value: length}) | from_entries),
      actor_parent_states: {absent:($r|map(select(parent_state=="absent"))|length),null:($r|map(select(parent_state=="null"))|length),empty_object:($r|map(select(parent_state=="empty_object"))|length),object:($r|map(select(parent_state=="object"))|length),unexpected_type:($r|map(select(parent_state=="unexpected_type"))|length)},
      actor_mode_states: state_counts($r;"mode"),
      actor_role_states: state_counts($r;"role"),
      family_breakdown: ($r | group_by(family_name) | map({key:(.[0]|family_name),value:{records:length,parent_absent:(map(select(parent_state=="absent"))|length),parent_object_null_children:(map(select(parent_state=="object" and .values.actor.mode==null and .values.actor.role==null))|length),parent_object_populated:(map(select(parent_state=="object" and (.values.actor.mode|type)=="string" and (.values.actor.role|type)=="string"))|length)}}) | from_entries),
      actor_label_breakdown: (($r|map(select(parent_state=="object" and (.values.actor.id|type)=="string" and .values.actor.id!=""))) as $p | {id_labels:($p|group_by(.values.actor.id)|map({key:.[0].values.actor.id,value:length})|from_entries),mode_labels:($p|group_by(.values.actor.mode)|map({key:.[0].values.actor.mode,value:length})|from_entries),role_labels:($p|group_by(.values.actor.role)|map({key:.[0].values.actor.role,value:length})|from_entries)}),
      by_kind: ($r | group_by(.record_kind) | map({key:.[0].record_kind,value:{records:length,parent_absent:(map(select(parent_state=="absent"))|length),parent_object_null_children:(map(select(parent_state=="object" and .values.actor.mode==null and .values.actor.role==null))|length),parent_object_populated:(map(select(parent_state=="object" and (.values.actor.mode|type)=="string" and (.values.actor.role|type)=="string"))|length)}}) | from_entries),
      mode_role_cells: ($r | map({kind:.record_kind,family:family_name,mode:(if child_state("mode")=="not_applicable_parent_absent" then "parent-absent" elif child_state("mode")=="null" then "child-null" elif child_state("mode")=="string" then ("value:" + (.values.actor.mode|tojson)) else child_state("mode") end),role:(if child_state("role")=="not_applicable_parent_absent" then "parent-absent" elif child_state("role")=="null" then "child-null" elif child_state("role")=="string" then ("value:" + (.values.actor.role|tojson)) else child_state("role") end)}) | group_by([.kind,.family,.mode,.role]) | map({kind:.[0].kind,family:.[0].family,mode:.[0].mode,role:.[0].role,n:length}) | sort_by([.kind,.family,.mode,.role])),
      legacy_untyped_census: ([$doc.records[] | select(.frontmatter==true and (.record_kind==null or .record_kind=="untyped") and (.values? != null) and ((.values|type)=="object"))] as $legacy | {parsed_mappings:($legacy|length),actor_parent_states:{absent:($legacy|map(select(parent_state=="absent"))|length),null:($legacy|map(select(parent_state=="null"))|length),empty_object:($legacy|map(select(parent_state=="empty_object"))|length),object:($legacy|map(select(parent_state=="object"))|length),unexpected_type:($legacy|map(select(parent_state=="unexpected_type"))|length)},actor_mode_states:(reduce ["not_applicable_parent_absent","missing_in_object","null","empty_string","string","unexpected_type"][] as $s ({}; .[$s]=($legacy|map(select(child_state("mode")==$s))|length))),actor_role_states:(reduce ["not_applicable_parent_absent","missing_in_object","null","empty_string","string","unexpected_type"][] as $s ({}; .[$s]=($legacy|map(select(child_state("role")==$s))|length))),literal_dotted_actor_id_keys:($legacy|map(select(.values|has("actor.id")))|length),meaning:"The frozen parsed legacy untyped inventory contains no actor parent or nested actor.mode/actor.role; this bounded absence is not a claim that legacy provenance never existed."})
    }
' "$inventory") || fail "native census derivation failed"

yaml_error_paths=$(jq -c '[.records[] | select((.error? // "") | contains("YAML::XS")) | .path] | sort' "$inventory")
no_frontmatter_count=$(jq '[.records[] | select(.error? == "no-opening-frontmatter")] | length' "$inventory")
[[ "$no_frontmatter_count" == 15 ]] || fail "no-frontmatter count changed"
[[ "$(jq 'length' <<< "$yaml_error_paths")" == 3 ]] || fail "YAML-error count changed"
jq -e --argjson actual "$actual_census" '.native_census | del(.inventory_evidence_id,.parse_exclusions) | .mode_role_cells |= sort_by([.kind,.family,.mode,.role]) | . == ($actual | .mode_role_cells |= sort_by([.kind,.family,.mode,.role]))' "$registry" >/dev/null || fail "authored native census differs from frozen inventory"
valid_registry=$(jq -c '.' "$registry") || fail "registry clone failed"
check_yaml_exclusions() {
  local candidate=$1
  jq -e --argjson errors "$yaml_error_paths" '.native_census.parse_exclusions.count == ($errors|length) and ((.native_census.parse_exclusions.records|sort) == $errors) and (.native_census.parse_exclusions.meaning|contains("not counted as absent actor"))' <<< "$candidate" >/dev/null
}
check_yaml_exclusions "$valid_registry" || fail "authored parse exclusions differ from native errors"
wrong_yaml=$(jq -c '.native_census.parse_exclusions.records[0] = "workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-definitely-not-a-yaml-error.md"' <<< "$valid_registry")
if check_yaml_exclusions "$wrong_yaml"; then fail "wrong YAML exclusion was accepted"; else wrong_yaml_status=$?; [[ "$wrong_yaml_status" == 1 ]] || fail "wrong-YAML control had unexpected status"; fi

check_registry() {
  jq -e --argjson assignment "$assignment_json" '(.evidence|map(.evidence_id)) as $ids | (.memberships|map([.field_path,.record_kind])) as $pairs | (.memberships|map(.meaning_id)) as $member_meanings | ($ids|unique|length)==($ids|length) and (.memberships|length)==8 and (($pairs|unique|sort)==($assignment|unique|sort)) and (($member_meanings|unique|sort)==(.meanings|keys|sort)) and ((([.memberships[].evidence_ids[]]|unique)-$ids)|length==0) and ((([.meanings[].evidence_ids[]]|unique)-$ids)|length==0)' "$1" >/dev/null
}
check_registry "$registry" || fail "registry references or membership boundary failed"
mutated_member=$(jq '.memberships[0].record_kind = "not-a-real-record-kind"' "$registry")
if printf '%s\n' "$mutated_member" | check_registry -; then fail "invalid membership mutation was accepted"; else mutated_member_status=$?; [[ "$mutated_member_status" == 1 ]] || fail "invalid membership mutation had unexpected status"; fi
mutated_evidence=$(jq '.meanings["actor.mode-claim"].evidence_ids[0] = "dangling-evidence-id"' "$registry")
if printf '%s\n' "$mutated_evidence" | check_registry -; then fail "dangling evidence mutation was accepted"; else dangling_status=$?; [[ "$dangling_status" == 1 ]] || fail "dangling evidence mutation had unexpected status"; fi

check_hashes() {
  local candidate=$1
  while IFS= read -r row; do
    [[ -z "$row" ]] && continue
    evidence_id=$(jq -r '.evidence_id' <<< "$row"); evidence_root=$(jq -r '.root' <<< "$row"); read_mode=$(jq -r '.read_mode' <<< "$row"); path=$(jq -r '.path' <<< "$row"); authority=$(jq -r '.authority_commit' <<< "$row")
    case "$evidence_root:$read_mode" in
      planning:snapshot) actual_hash=$(git -C "$root" show "$authority:$path" | shasum -a 256 | awk '{print $1}') ;;
      source:snapshot) actual_hash=$(git -C "$source" show "$authority:$path" | shasum -a 256 | awk '{print $1}') ;;
      planning:live) actual_hash=$(shasum -a 256 "$root/$path" | awk '{print $1}') ;;
      source:live) actual_hash=$(shasum -a 256 "$source/$path" | awk '{print $1}') ;;
      *) return 1 ;;
    esac
    expected_hash=$(jq -r --arg id "$evidence_id" '.evidence[]|select(.evidence_id==$id)|.sha256' <<< "$candidate")
    [[ "$actual_hash" == "$expected_hash" ]] || return 1
    if [[ "$evidence_root:$read_mode" == source:snapshot ]]; then current_hash=$(shasum -a 256 "$source/$path" | awk '{print $1}'); [[ "$current_hash" == "$expected_hash" ]] || return 1; fi
  done < <(jq -c '.evidence[]' <<< "$candidate")
}
check_hashes "$valid_registry" || fail "registered hash mismatch"
wrong_hash=$(jq -c '(.evidence[] | select(.evidence_id == "projectLedger") | .sha256) = "0000000000000000000000000000000000000000000000000000000000000000"' <<< "$valid_registry")
jq -n -e --argjson before "$valid_registry" --argjson after "$wrong_hash" '[range(0;($before.evidence|length)) as $i | select($before.evidence[$i].sha256 != $after.evidence[$i].sha256) | $i] | length == 1' >/dev/null || fail "wrong-hash candidate did not change exactly one hash"
if check_hashes "$wrong_hash"; then fail "wrong hash was accepted"; else wrong_hash_status=$?; [[ "$wrong_hash_status" == 1 ]] || fail "wrong-hash control had unexpected status"; fi

check_line_range() {
  local row=$1 range evidence_root read_mode authority path line_count span start end
  range=$(jq -r '.source_range // empty' <<< "$row") || return 1
  case "$range" in "JSON document"|"JSON document; selected values and YAML-error records") return 0 ;; lines\ *) ;; *) return 1 ;; esac
  evidence_root=$(jq -r '.root' <<< "$row"); read_mode=$(jq -r '.read_mode' <<< "$row"); authority=$(jq -r '.authority_commit' <<< "$row"); path=$(jq -r '.path' <<< "$row")
  case "$evidence_root:$read_mode" in
    planning:snapshot) line_count=$(git -C "$root" show "$authority:$path" | awk 'END {print NR}') ;;
    source:snapshot) line_count=$(git -C "$source" show "$authority:$path" | awk 'END {print NR}') ;;
    planning:live) line_count=$(awk 'END {print NR}' "$root/$path") ;;
    source:live) line_count=$(awk 'END {print NR}' "$source/$path") ;;
    *) return 1 ;;
  esac
  range=${range#lines }; IFS=',' read -ra spans <<< "$range"; [[ "${#spans[@]}" -gt 0 ]] || return 1
  for span in "${spans[@]}"; do span=${span# }; [[ "$span" =~ ^([1-9][0-9]*)-([1-9][0-9]*)$ ]] || return 1; start=${BASH_REMATCH[1]}; end=${BASH_REMATCH[2]}; ((start<=end && end<=line_count)) || return 1; done
}
check_registered_ranges() {
  local candidate=$1 row id
  [[ "$(jq '.evidence|length' <<< "$candidate")" == 39 ]] || return 1
  while IFS= read -r row; do [[ -z "$row" ]] && continue; id=$(jq -r '.evidence_id' <<< "$row"); check_line_range "$row" || { printf '%s\n' "invalid source_range: $id" >&2; return 1; }; done < <(jq -c '.evidence[]' <<< "$candidate")
}
registry_json=$(jq -c '.' "$registry") || fail "registry clone failed"
check_registered_ranges "$registry_json" || fail "registered ranges failed"
valid_multi_span=$(jq -c '.evidence[]|select(.evidence_id=="recordFieldGroups")' <<< "$registry_json"); check_line_range "$valid_multi_span" || fail "valid multi-span range rejected"
valid_json_descriptor=$(jq -c '.evidence[]|select(.evidence_id=="currentCoverage")' <<< "$registry_json"); check_line_range "$valid_json_descriptor" || fail "valid JSON descriptor rejected"
mutated_range=$(jq -c '.evidence |= map(if .evidence_id=="projectLedger" then .source_range="lines 1-999999" else . end)' <<< "$registry_json")
if check_registered_ranges "$mutated_range"; then fail "out-of-bounds range accepted"; else range_oob_status=$?; [[ "$range_oob_status" == 1 ]] || fail "out-of-bounds range had unexpected status"; fi
mutated_range=$(jq -c '.evidence |= map(if .evidence_id=="projectLedger" then .source_range="lines 15-10" else . end)' <<< "$registry_json")
if check_registered_ranges "$mutated_range"; then fail "reversed range accepted"; else range_reversed_status=$?; [[ "$range_reversed_status" == 1 ]] || fail "reversed range had unexpected status"; fi

pilot_path=$(jq -r '.evidence[]|select(.evidence_id=="pilotCard")|.path' "$registry")
pilot_actor=$(jq -c --arg path "$pilot_path" '.records[]|select(.path==(".worktrees/planning/"+$path))|.values.actor' "$inventory")
expected_actor='{"id":"codex-cc","mode":"agent-direct","role":"extractor"}'
jq -n -e --argjson actual "$pilot_actor" --argjson expected "$expected_actor" '$actual==$expected' >/dev/null || fail "positive populated card actor differs"
wrong_mode=$(jq -c '.mode="human-assisted"' <<< "$pilot_actor")
if jq -n -e --argjson actual "$wrong_mode" --argjson expected "$expected_actor" '$actual==$expected' >/dev/null; then fail "wrong mode human-assisted was accepted"; else wrong_mode_status=$?; [[ "$wrong_mode_status" == 1 ]] || fail "wrong mode control had unexpected status"; fi
wrong_role=$(jq -c '.role="validator"' <<< "$pilot_actor")
if jq -n -e --argjson actual "$wrong_role" --argjson expected "$expected_actor" '$actual==$expected' >/dev/null; then fail "wrong role validator was accepted"; else wrong_role_status=$?; [[ "$wrong_role_status" == 1 ]] || fail "wrong role control had unexpected status"; fi
swapped=$(jq -c '{id,mode:.role,role:.mode}' <<< "$pilot_actor")
if jq -n -e --argjson actual "$swapped" --argjson expected "$expected_actor" '$actual==$expected' >/dev/null; then fail "swapped mode/role was accepted"; else swapped_status=$?; [[ "$swapped_status" == 1 ]] || fail "swapped control had unexpected status"; fi

assert_absent() {
  local file=$1 path=$2
  jq -e --arg path "$path" '.records[]|select(.path==$path)|((.values|has("actor"))|not)' "$file" >/dev/null
}
synthetic_path=$(jq -r '.evidence[]|select(.evidence_id=="cqCoverage")|.path' "$registry")
assert_absent "$inventory" "$synthetic_path" || fail "synthetic CQ actor parent was not absent"
mutated_inventory=$temp/mutated-inventory.json
jq --arg path "$synthetic_path" '(.records[]|select(.path==$path)|.values.actor)=null' "$inventory" > "$mutated_inventory"
if assert_absent "$mutated_inventory" "$synthetic_path"; then fail "absence-as-null mutation was accepted"; else absence_null_status=$?; [[ "$absence_null_status" == 1 ]] || fail "absence-as-null control had unexpected status"; fi

no_match_err=$temp/no-match.err
no_match_output=$(jq -c --arg path .worktrees/planning/no-such-real-inventory-path '[.records[]|select(.path==$path)]' "$inventory" 2>"$no_match_err")
no_match_status=$?
[[ "$no_match_status" == 0 && "$no_match_output" == "[]" && ! -s "$no_match_err" ]] || fail "real no-match behavior changed"
missing_inventory=$temp/missing-inventory.json
if jq -c '.records' "$missing_inventory" >/dev/null 2>"$temp/missing.err"; then fail "missing input unexpectedly succeeded"; else missing_status=$?; [[ "$missing_status" != 0 ]] || fail "missing input returned zero"; fi

fixture=$temp/unrelated-head-fixture
mkdir -p "$fixture/knowledge/concept-cards"
git init -q "$fixture"
printf '%s\n' stable > "$fixture/knowledge/concept-cards/stable.md"
git -C "$fixture" add -- knowledge/concept-cards/stable.md
git -C "$fixture" -c user.name="Slice15 validation" -c user.email="slice15@example.invalid" commit -qm base
printf '%s\n' unrelated > "$fixture/unrelated.txt"
git -C "$fixture" add -- unrelated.txt
git -C "$fixture" -c user.name="Slice15 validation" -c user.email="slice15@example.invalid" commit -qm unrelated
git -C "$fixture" diff --exit-code HEAD~1 HEAD -- knowledge/concept-cards || fail "unrelated HEAD fixture changed registered path"

printf '%s\n' "mode=$mode"
printf '%s\n' "source_opening=$opening_source"
printf '%s\n' "source_current=$source_current"
printf '%s\n' "planning_opening=$opening_planning"
printf '%s\n' "planning_head=$(git rev-parse HEAD)"
printf '%s\n' "native_selected=$(jq -r '.parsed_selected_mappings' <<< "$actual_census") legacy_untyped=$(jq -r '.legacy_untyped_census.parsed_mappings' <<< "$actual_census")"
printf '%s\n' "yaml_error_count=$(jq 'length' <<< "$yaml_error_paths") no_frontmatter_count=$no_frontmatter_count"
printf '%s\n' "wrong_hash_status=$wrong_hash_status wrong_yaml_status=$wrong_yaml_status"
printf '%s\n' "wrong_mode_status=$wrong_mode_status wrong_role_status=$wrong_role_status swapped_status=$swapped_status"
printf '%s\n' "absence_as_null_status=$absence_null_status no_match_status=$no_match_status no_match_output=$no_match_output missing_input_status=$missing_status"
printf '%s\n' "invalid_membership_status=$mutated_member_status dangling_evidence_status=$dangling_status"
printf '%s\n' "range_oob_status=$range_oob_status range_reversed_status=$range_reversed_status unrelated_head_fixture=pass"
printf '%s\n' "semantic_acceptance=not_claimed"
~~~

## Intake and contract readback

The iteration preflight loaded the source and planning standing instructions,
the current project/arc/slice plans and ledgers, this prompt, the initial
Slice15 prompt, `crc-verification.md`, the Arc06 CDC directive, the prior
Slice13/Slice14 evidence and handoff, the complete initial literal route, the
registry and closing report. Required extents were: iteration prompt 1-134;
slice plan 1-148; ledger 1-14; CRC record 1-50; initial prompt 1-222;
validation record 1-328 before repair; registry 1-266; and closing report
1-77. Named project sections were loaded at project-plan lines 39-171 and
214-268; named Arc sections at arc-plan lines 22-91, 154-230 and 275-402;
the CDC directive was loaded 1-233. Source full records and guides were read
at the authorized latest source baseline `ce3f7710`, including the updated
prompt-authoring corrective-iteration guidance and testing behavioral-oracle/
failure-triage sections. The source and planning checkouts were clean at
`ce3f7710` and iteration opening `ea200f07`, respectively. The two registered
source entries affected by the baseline move (`sourceCollab` and
`implementationPrompt`) now pin their `ce3f7710` bytes; the other registered
source evidence remains byte-identical.

The planning advance from the initial CC close `178f1e6e` to `ea200f07` is
the expected CRC return packet: the iteration prompt, CRC verification,
factual slice plan and ledger state only. It does not change the initial
registry's evidence authorities at `4db8d882`, the source bytes, assignment,
coverage, inventory or prior packets. The iteration route therefore uses
`ea200f07` for its opening-to-CC scope/protected-path check while retaining
the initial registry's `4db8d882` snapshot authorities.

The exact eight-pair assignment, 200/355/8/347 current coverage, frozen
555/115/440/35/405 transition, native 37/2,054 census, three YAML exclusions
and 15 no-frontmatter records remain route inputs. Slice14's literal route was
read as a bounded predecessor for wrapper, hash, range, preservation and
negative-control mechanics only; its obsolete counts/endpoints were not
reused. Observed values remain separate from expected or accepted values, and
CRC/CDC authority remains with the Operator.

## Recorded observations

The following entries are filled after running the route. A status-0 run is
structural replay evidence only.

- Exploratory exact-set predicate: failed because it incorrectly required the
  eight assigned pairs to equal all 20 remaining mode/role pairs. Corrected
  predicate: exact eight, subset of remaining, disjoint from accepted.
- Iteration01 preflight before repair: status 0 for the inherited valid route,
  but CRC findings R1/R2 were reproduced as unrun controls; R3 was a wording
  defect because the older endpoint checks returned status 2 for an absent
  recipe path, not a valid stale-recipe rejection.
- Iteration01 baseline reconciliation: the Operator authorized the clean
  `ce3f7710` source checkout as the new baseline; only the two affected source
  evidence rows were rebased, with ontology-support source files unchanged.
- Iteration01 precommit replay: status 0 at planning HEAD `ea200f07` and
  source baseline `ce3f7710`; native selected 37, legacy untyped 2054, YAML
  errors 3, and no-frontmatter 15. Wrong hash and wrong YAML candidate
  controls both returned status 1, as did wrong mode, wrong role, swapped
  mode/role, absence-as-null, invalid membership, dangling evidence,
  out-of-bounds range, and reversed range; real no-match returned status 0
  with `[]`; missing input returned status 2; unrelated-head fixture passed;
  semantic acceptance not claimed.
- The initial packet's historical endpoint observations remain bounded
  context: same-revision and separate committed replays were status 0, while
  the older/opening recipe-path checks returned status 2 because the Slice15
  recipe was absent. Those observations are not reused as current
  Iteration01 endpoints.
- Iteration01 committed same-revision, missing/foreign recipe-path, and
  separate CC/recipe outcomes are recorded after their commits below; no pair
  moves to accepted coverage.
