# Slice16 validation evidence: literal native replay

Status: CC proposed-done; independent CRC verification is required. This is a
structural evidence route, not a semantic-acceptance verdict.

## Intake and contract readback

The intake and source-cited contract readback are recorded in
`artifacts/semantic-evidence.md`. The route below derives all native values
from the frozen inventory at the opening planning commit, uses the current
coverage and immutable transition only for their declared structural checks,
and loads the authored registry from the CC commit in committed mode.

The conditional Slice15 route trigger applied: this packet reuses its Bash/jq/
Git/shasum mechanics for exact-set, hash, range, preservation, wrapper and
negative-control checks. It does not copy Slice15's assignment, census,
meanings or endpoints. The four raw inventory pilot paths are normalized from
the inventory's `.worktrees/planning/` acquisition prefix to the canonical
planning checkout path before hashing; the frozen inventory itself is not
modified.

Iteration01 intake records the CRC corrective requirements: every evidence row
must be read through its declared `.authority_commit`, the 45 registered
`source_range` values must classify as exactly 42 numeric `lines a-b`
descriptors plus the two `JSON document` descriptors and the inventory's exact
`JSON document; selected values and YAML-error records` descriptor, and a
real no-match actor projection must be the literal JSON array `[]` while the
separate count remains zero. The iteration opening planning commit is
`ac618e0fd3c428a68587b8195bc4c5817351a336`; the pinned evidence authorities
remain planning `3b7790f88cd30fa6c4988a6950b4989ae1933b7d` and source
`ce3f77103eff5e07b3533a03c65f158684fc1039`. The iteration prompt and CRC
verification are protected planning records; they are not CC outputs.

## Literal route

The committed wrapper is:

~~~text
CC_COMMIT=<cc-endpoint> REPLAY_COMMIT=<recipe-endpoint> bash -c '
set -euo pipefail
recipe=$(git show "$REPLAY_COMMIT:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/artifacts/validation-evidence.md") || exit 2
code=$(printf "%s\n" "$recipe" | awk '/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p') || exit 2
[[ -n "$code" ]] || exit 2
printf "%s\n" "$code" | bash -s
'
~~~

The precommit wrapper is:

~~~text
CC_PRECOMMIT=1 bash -s < <(awk '/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p' project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/artifacts/validation-evidence.md)
~~~

~~~bash
set -euo pipefail

fail() { printf '%s\n' "FAIL: $*" >&2; exit 1; }

root=$(git rev-parse --show-toplevel)
source=$(cd "$root/../.." && pwd)
slice_rel=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role
membership_rel=$slice_rel/artifacts/semantic-membership.json
coverage_rel=project08-concept-card-metadata/artifacts/semantic-coverage-current.json
transition_rel=project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
inventory_rel=project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
opening_source=ce3f77103eff5e07b3533a03c65f158684fc1039
opening_planning=3b7790f88cd30fa6c4988a6950b4989ae1933b7d
iteration_opening=ac618e0fd3c428a68587b8195bc4c5817351a336
mode=precommit
kinds_json='["memory-admission","preservation-decision","relationship-edge","source-locator","source-support","validation-result"]'

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

[[ "$root" == /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning ]] || fail "route must run from canonical planning checkout"
source_current=$(git -C "$source" rev-parse HEAD)
[[ -z "$(git -C "$source" status --porcelain --untracked-files=all)" ]] || fail "source checkout is not clean"
git diff --check || fail "planning working tree has whitespace errors"
git diff --cached --check || fail "planning index has whitespace errors"
git -C "$source" diff --exit-code "$opening_source" "$source_current" -- knowledge/concept-cards knowledge/document-extraction || fail "registered relevant source tree differs from opening source"

allowed_paths="$slice_rel/artifacts/semantic-membership.json
$slice_rel/artifacts/semantic-evidence.md
$slice_rel/artifacts/validation-evidence.md
$slice_rel/artifacts/handoff.md
$slice_rel/ledger.md
$slice_rel/closing-report.md"
is_allowed() { grep -Fqx "$1" <<< "$allowed_paths"; }
if [[ "$mode" == precommit ]]; then
  changed_paths=$( { git diff --cached --name-only; git diff --name-only; git ls-files --others --exclude-standard; } | sort -u )
  [[ -n "$changed_paths" ]] || fail "precommit union is empty"
  while IFS= read -r path; do [[ -z "$path" ]] && continue; is_allowed "$path" || fail "out-of-scope precommit path: $path"; done <<< "$changed_paths"
else
  [[ -z "$(git status --porcelain --untracked-files=all)" ]] || fail "planning checkout is not clean for committed replay"
  committed_paths=$(git diff --name-only "$iteration_opening" "$CC_COMMIT" | sort -u)
  [[ -n "$committed_paths" ]] || fail "committed CC contribution is empty"
  while IFS= read -r path; do [[ -z "$path" ]] && continue; is_allowed "$path" || fail "out-of-scope opening-to-CC path: $path"; done <<< "$committed_paths"
fi

protected_paths="project08-concept-card-metadata/AGENTS.md
project08-concept-card-metadata/project-plan.md
project08-concept-card-metadata/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/arc-plan.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/cdc-directive01.md
$slice_rel/cc-prompt.md
$slice_rel/cc-prompt-iteration01.md
$slice_rel/crc-verification.md
$slice_rel/slice-plan.md
$coverage_rel
$transition_rel
$inventory_rel
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references/artifacts/semantic-membership.json
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references/artifacts/semantic-evidence.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references/artifacts/handoff.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references/crc-verification.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references/artifacts/validation-evidence.md"
while IFS= read -r path; do [[ -z "$path" ]] && continue; git diff --exit-code "$iteration_opening" -- "$path" >/dev/null || fail "protected planning path changed: $path"; done <<< "$protected_paths"

assignment_json=$(git show "$iteration_opening:$slice_rel/slice-plan.md" | awk '/^~~~json$/{n++; if(n==1){p=1;next}} p && /^~~~$/{exit} p')
[[ -n "$assignment_json" ]] || fail "assignment block is absent"
jq -e --argjson assignment "$assignment_json" '.counts == {full:555,accepted:208,remaining:347,next_slice:12,not_yet_sliced:335} and (.accepted_pairs|length==208) and (.remaining_pairs|length==347) and ((.accepted_pairs+.remaining_pairs)|unique|length==555) and ((.next_slice_pairs|sort)==($assignment|sort)) and (((.remaining_pairs-$assignment)|length)==335)' < <(git show "$opening_planning:$coverage_rel") >/dev/null || fail "current coverage boundary failed"
jq -e '.counts == {full:555,accepted:115,remaining:440,next_slice:35,not_yet_sliced:405} and (.counts.accepted + .counts.remaining == .counts.full) and (.counts.next_slice + .counts.not_yet_sliced == .counts.remaining)' < <(git show "$opening_planning:$transition_rel") >/dev/null || fail "frozen transition counts failed"

inventory=$temp/inventory.json
git show "$opening_planning:$inventory_rel" > "$inventory" || fail "opening inventory is absent"

actual_census=$(jq -c --argjson kinds "$kinds_json" '
  def family:
    if (.path|startswith("knowledge/concept-cards/templates/")) then "template"
    elif (.path|startswith("knowledge/concept-cards/examples/")) then "synthetic"
    elif (.path|contains("slice02-pilot")) then "pilot"
    elif (.path|contains("slice04-expanded")) then "expanded"
    elif (.path|contains("teaching")) then "teaching"
    elif (.path|contains("rich")) then "rich"
    else "other" end;
  def parent_state:
    if ((.values|has("actor"))|not) then "absent"
    elif .values.actor == null then "null"
    elif ((.values.actor|type)=="object" and (.values.actor|length)==0) then "empty_object"
    elif (.values.actor|type)=="object" then "object"
    else "unexpected_type" end;
  def child_state($child):
    if parent_state == "absent" then "not_applicable_parent_absent"
    elif parent_state != "object" then "unexpected_type"
    elif ((.values.actor|has($child))|not) then "missing_in_object"
    elif .values.actor[$child] == null then "null"
    elif ((.values.actor[$child]|type)=="string" and .values.actor[$child]=="") then "empty_string"
    elif (.values.actor[$child]|type)=="string" then "string"
    else "unexpected_type" end;
  def display($child):
    if parent_state == "absent" then "parent-absent"
    elif child_state($child) == "null" then "child-null"
    elif child_state($child) == "string" then ("value:" + (.values.actor[$child]|tojson))
    else child_state($child) end;
  . as $doc
  | [.records[] | select(.frontmatter==true and (.values?|type)=="object" and (.record_kind as $k | ($kinds|index($k)) != null))] as $r
  | {
      parsed_selected_mappings:($r|length),
      record_kind_counts:($r|group_by(.record_kind)|map({key:.[0].record_kind,value:length})|from_entries),
      actor_parent_states:{absent:($r|map(select(parent_state=="absent"))|length),null:($r|map(select(parent_state=="null"))|length),empty_object:($r|map(select(parent_state=="empty_object"))|length),object:($r|map(select(parent_state=="object"))|length),unexpected_type:($r|map(select(parent_state=="unexpected_type"))|length)},
      actor_mode_states:(reduce ["not_applicable_parent_absent","missing_in_object","null","empty_string","string","unexpected_type"][] as $s ({}; .[$s]=($r|map(select(child_state("mode")==$s))|length))),
      actor_role_states:(reduce ["not_applicable_parent_absent","missing_in_object","null","empty_string","string","unexpected_type"][] as $s ({}; .[$s]=($r|map(select(child_state("role")==$s))|length))),
      family_breakdown:($r|group_by(family)|map({key:(.[0]|family),value:{records:length,parent_absent:(map(select(parent_state=="absent"))|length),parent_object_null_children:(map(select(parent_state=="object" and .values.actor.mode==null and .values.actor.role==null))|length),parent_object_populated:(map(select(parent_state=="object" and (.values.actor.mode|type)=="string" and (.values.actor.role|type)=="string"))|length)}})|from_entries),
      by_kind:($r|group_by(.record_kind)|map({key:.[0].record_kind,value:{records:length,parent_absent:(map(select(parent_state=="absent"))|length),parent_object_null_children:(map(select(parent_state=="object" and .values.actor.mode==null and .values.actor.role==null))|length),parent_object_populated:(map(select(parent_state=="object" and (.values.actor.mode|type)=="string" and (.values.actor.role|type)=="string"))|length)}})|from_entries),
      mode_role_cells:($r|map({kind:.record_kind,family:family,mode:display("mode"),role:display("role")})|group_by([.kind,.family,.mode,.role])|map({kind:.[0].kind,family:.[0].family,mode:.[0].mode,role:.[0].role,n:length})|sort_by([.kind,.family,.mode,.role])),
      support_witnesses:($r|map(select(.record_kind=="source-support" and parent_state=="object" and child_state("mode")=="string" and child_state("role")=="string")|{path:(.path|sub("^\\.worktrees/planning/";"")),subject_ref:(.values.subject_ref.id // .values.subject_ref),actor:.values.actor})|sort_by(.path))
    }
' "$inventory") || fail "native selected census failed"

legacy_census=$(jq -c '
  def parent_state:
    if ((.values|has("actor"))|not) then "absent"
    elif .values.actor == null then "null"
    elif ((.values.actor|type)=="object" and (.values.actor|length)==0) then "empty_object"
    elif (.values.actor|type)=="object" then "object"
    else "unexpected_type" end;
  def child_state($child):
    if parent_state == "absent" then "not_applicable_parent_absent"
    elif parent_state != "object" then "unexpected_type"
    elif ((.values.actor|has($child))|not) then "missing_in_object"
    elif .values.actor[$child] == null then "null"
    elif ((.values.actor[$child]|type)=="string" and .values.actor[$child]=="") then "empty_string"
    elif (.values.actor[$child]|type)=="string" then "string"
    else "unexpected_type" end;
  [.records[]|select(.frontmatter==true and (.record_kind==null or .record_kind=="untyped") and (.values?|type)=="object")] as $r
  | {parsed_mappings:($r|length),actor_parent_states:{absent:($r|map(select(parent_state=="absent"))|length),null:($r|map(select(parent_state=="null"))|length),empty_object:($r|map(select(parent_state=="empty_object"))|length),object:($r|map(select(parent_state=="object"))|length),unexpected_type:($r|map(select(parent_state=="unexpected_type"))|length)},actor_mode_states:(reduce ["not_applicable_parent_absent","missing_in_object","null","empty_string","string","unexpected_type"][] as $s ({}; .[$s]=($r|map(select(child_state("mode")==$s))|length))),actor_role_states:(reduce ["not_applicable_parent_absent","missing_in_object","null","empty_string","string","unexpected_type"][] as $s ({}; .[$s]=($r|map(select(child_state("role")==$s))|length))),literal_dotted_actor_id_keys:($r|map(select(.values|has("actor.id")))|length),meaning:"The frozen parsed legacy untyped inventory contains no actor parent or nested actor.mode/actor.role; this bounded absence is not a claim that legacy provenance never existed."}
' "$inventory") || fail "legacy census failed"

yaml_error_paths=$(jq -c '[.records[]|select((.error? // "")|contains("YAML::XS"))|.path] | sort' "$inventory")
no_frontmatter_count=$(jq '[.records[]|select(.error?=="no-opening-frontmatter")]|length' "$inventory")
[[ "$no_frontmatter_count" == 15 ]] || fail "no-frontmatter count changed"
[[ "$(jq 'length' <<< "$yaml_error_paths")" == 3 ]] || fail "YAML-error count changed"
jq -e --argjson actual "$actual_census" '(.native_census|{parsed_selected_mappings,record_kind_counts,actor_parent_states,actor_mode_states,actor_role_states,family_breakdown,by_kind,mode_role_cells,support_witnesses}) == ($actual|{parsed_selected_mappings,record_kind_counts,actor_parent_states,actor_mode_states,actor_role_states,family_breakdown,by_kind,mode_role_cells,support_witnesses})' "$registry" >/dev/null || fail "authored native census differs from frozen inventory"
jq -e --argjson legacy "$legacy_census" '.native_census.legacy_untyped_census == $legacy' "$registry" >/dev/null || fail "legacy census differs from frozen inventory"

valid_registry=$(jq -c '.' "$registry") || fail "registry clone failed"
check_yaml_exclusions() { local candidate=$1; jq -e --argjson errors "$yaml_error_paths" '.native_census.parse_exclusions.count == ($errors|length) and ((.native_census.parse_exclusions.records|sort)==$errors) and (.native_census.parse_exclusions.meaning|contains("not counted as absent actor"))' <<< "$candidate" >/dev/null; }
check_yaml_exclusions "$valid_registry" || fail "authored YAML exclusions differ from native errors"
wrong_yaml=$(jq -c '.native_census.parse_exclusions.records[0]="workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-definitely-not-a-yaml-error.md"' <<< "$valid_registry")
if check_yaml_exclusions "$wrong_yaml"; then fail "wrong YAML exclusion was accepted"; else wrong_yaml_status=$?; [[ "$wrong_yaml_status" == 1 ]] || fail "wrong YAML control had unexpected status"; fi

check_scope() { jq -e --argjson assignment "$assignment_json" '(.scope.assignment == $assignment) and (.scope.counts == {full:555,accepted:208,remaining:347,assigned:12,outside:335}) and ((.scope.assignment|unique|length)==12)' "$1" >/dev/null; }
check_registry() { jq -e --argjson assignment "$assignment_json" '(.evidence|map(.evidence_id)) as $ids | (.memberships|map([.field_path,.record_kind])) as $pairs | (.memberships|map(.meaning_id)) as $member_meanings | (.meanings|to_entries|map(.value.evidence_ids[])|unique) as $meaning_evidence | (.memberships|map(.evidence_ids[])|unique) as $membership_evidence | (.scope.assignment == $assignment) and ((.memberships|length)==12) and (($pairs|unique|sort)==($assignment|unique|sort)) and (($member_meanings|unique|sort)==(.meanings|keys|sort)) and ((([.memberships[].evidence_ids[]]|unique)-$ids)|length==0) and (($meaning_evidence-$ids)|length==0) and (($membership_evidence-$ids)|length==0)' "$1" >/dev/null; }
check_scope "$registry" || fail "scope boundary failed"
check_registry "$registry" || fail "registry references or membership boundary failed"
check_absence_boundary() { jq -e '[.native_census.mode_role_cells[]|select(.mode=="parent-absent" and .role=="parent-absent")]|length==2' <<< "$1" >/dev/null; }
check_absence_boundary "$valid_registry" || fail "authored parent-absence boundary failed"
absence_as_null=$(jq -c '.native_census.mode_role_cells[0].mode="child-null"' <<< "$valid_registry")
if check_absence_boundary "$absence_as_null"; then fail "absence-as-null mutation was accepted"; else absence_status=$?; [[ "$absence_status" == 1 ]] || fail "absence-as-null control had unexpected status"; fi
wrong_member=$(jq -c '.memberships[0].record_kind="claim"' <<< "$valid_registry")
if printf '%s\n' "$wrong_member" | check_registry -; then fail "Slice15 or invalid member mutation was accepted"; else wrong_member_status=$?; [[ "$wrong_member_status" == 1 ]] || fail "invalid membership control had unexpected status"; fi
mutated_evidence=$(jq -c '.meanings["actor.mode-source-support"].evidence_ids[0]="dangling-evidence-id"' <<< "$valid_registry")
if printf '%s\n' "$mutated_evidence" | check_registry -; then fail "dangling evidence mutation was accepted"; else dangling_status=$?; [[ "$dangling_status" == 1 ]] || fail "dangling evidence control had unexpected status"; fi

resolve_snapshot() {
  local row=$1 root path authority_commit read_mode
  root=$(jq -r '.root' <<< "$row")
  path=$(jq -r '.path' <<< "$row")
  authority_commit=$(jq -r '.authority_commit' <<< "$row")
  read_mode=$(jq -r '.read_mode' <<< "$row")
  [[ "$read_mode" == snapshot ]] || return 1
  case "$root" in
    planning)
      [[ "$authority_commit" == "$opening_planning" ]] || return 1
      git show "$authority_commit:$path"
      ;;
    source)
      [[ "$authority_commit" == "$opening_source" ]] || return 1
      git -C "$source" show "$authority_commit:$path"
      ;;
    *) return 1 ;;
  esac
}

check_hashes() {
  local candidate=$1 row evidence_id read_mode root actual_hash expected_hash current_hash snapshot_file count=0
  while IFS= read -r row; do
    evidence_id=$(jq -r '.evidence_id' <<< "$row")
    read_mode=$(jq -r '.read_mode' <<< "$row")
    root=$(jq -r '.root' <<< "$row")
    actual_hash=$(jq -r --arg id "$evidence_id" '.evidence[]|select(.evidence_id==$id)|.sha256' <<< "$candidate")
    expected_hash=$(jq -r --arg id "$evidence_id" '.evidence[]|select(.evidence_id==$id)|.sha256' <<< "$valid_registry")
    [[ -n "$actual_hash" && "$actual_hash" == "$expected_hash" ]] || return 1
    case "$root:$read_mode" in
      planning:snapshot|source:snapshot)
        snapshot_file="$temp/hash-$count"
        resolve_snapshot "$row" > "$snapshot_file" || return 1
        current_hash=$(shasum -a 256 "$snapshot_file" | awk '{print $1}') || return 1
        [[ "$current_hash" == "$actual_hash" ]] || return 1
        ;;
      *) return 1 ;;
    esac
    count=$((count + 1))
  done < <(jq -c '.evidence[]' <<< "$candidate")
  [[ "$count" == 45 ]]
}
check_hashes "$valid_registry" || fail "registered hashes do not reproduce"
wrong_hash=$(jq -c '.evidence[0].sha256="0000000000000000000000000000000000000000000000000000000000000000"' <<< "$valid_registry")
if check_hashes "$wrong_hash"; then fail "wrong hash was accepted"; else wrong_hash_status=$?; [[ "$wrong_hash_status" == 1 ]] || fail "wrong hash control had unexpected status"; fi
wrong_authority=$(jq -c '.evidence[0].authority_commit="ce3f77103eff5e07b3533a03c65f158684fc1039"' <<< "$valid_registry")
if check_hashes "$wrong_authority"; then fail "wrong declared authority was accepted"; else wrong_authority_status=$?; [[ "$wrong_authority_status" == 1 ]] || fail "wrong authority control had unexpected status"; fi

check_ranges() {
  local candidate=$1 entry evidence_id source_range range_text start end total expected snapshot_file count=0 numeric=0 json=0
  while IFS= read -r entry; do
    evidence_id=$(jq -r '.evidence_id' <<< "$entry")
    source_range=$(jq -r '.source_range' <<< "$entry")
    snapshot_file="$temp/range-$count"
    resolve_snapshot "$entry" > "$snapshot_file" || return 1
    expected=""
    case "$evidence_id" in
      currentCoverage|transitionCoverage) expected="JSON document" ;;
      inventory) expected="JSON document; selected values and YAML-error records" ;;
    esac
    if [[ -n "$expected" ]]; then
      [[ "$source_range" == "$expected" ]] || return 1
      json=$((json + 1))
      count=$((count + 1))
      continue
    fi
    [[ "$source_range" =~ ^lines[[:space:]][0-9]+-[0-9]+$ ]] || return 1
    range_text=${source_range#lines }
    start=${range_text%-*}
    end=${range_text##*-}
    [[ "$start" =~ ^[0-9]+$ && "$end" =~ ^[0-9]+$ && "$start" -ge 1 && "$start" -le "$end" ]] || return 1
    total=$(wc -l < "$snapshot_file" | awk '{print $1}') || return 1
    [[ "$end" -le "$total" ]] || return 1
    numeric=$((numeric + 1))
    count=$((count + 1))
  done < <(jq -c '.evidence[]|select((.source_range|type)=="string")' <<< "$candidate")
  [[ "$count" == 45 && "$numeric" == 42 && "$json" == 3 ]]
}
check_ranges "$valid_registry" || fail "registered source ranges do not reproduce"
range_unknown=$(jq -c '.evidence[0].source_range="not-a-range"' <<< "$valid_registry")
if check_ranges "$range_unknown"; then fail "unknown range descriptor was accepted"; else range_unknown_status=$?; [[ "$range_unknown_status" == 1 ]] || fail "unknown range control had unexpected status"; fi
range_misplaced=$(jq -c '(.evidence[] | select(.evidence_id=="currentCoverage") | .source_range) = "lines 1-1"' <<< "$valid_registry")
if check_ranges "$range_misplaced"; then fail "misplaced range descriptor was accepted"; else range_misplaced_status=$?; [[ "$range_misplaced_status" == 1 ]] || fail "misplaced range control had unexpected status"; fi
range_oob=$(jq -c '.evidence[0].source_range="lines 1-999999"' <<< "$valid_registry")
if check_ranges "$range_oob"; then fail "out-of-bounds range was accepted"; else range_oob_status=$?; [[ "$range_oob_status" == 1 ]] || fail "out-of-bounds range control had unexpected status"; fi
range_reversed=$(jq -c '.evidence[0].source_range="lines 2-1"' <<< "$valid_registry")
if check_ranges "$range_reversed"; then fail "reversed range was accepted"; else range_reversed_status=$?; [[ "$range_reversed_status" == 1 ]] || fail "reversed range control had unexpected status"; fi

support_path=$(jq -r '.native_census.support_witnesses[0].path' <<< "$valid_registry")
support_actual=$(jq -c --arg p "$support_path" '.records[] | select(.path==(".worktrees/planning/"+$p) or .path==$p) | .values.actor' "$inventory" | head -n 1)
expected_support='{"id":"codex-cc","mode":"agent-direct","role":"extractor"}'
[[ "$support_actual" == "$expected_support" ]] || fail "native support witness did not reproduce"
support_subject=$(jq -r --arg p "$support_path" '.records[] | select(.path==(".worktrees/planning/"+$p) or .path==$p) | .values.subject_ref.id' "$inventory" | head -n 1)
[[ -n "$support_subject" ]] || fail "support subject reference is absent"
support_scope=$(jq -c --arg p "$support_path" '.records[] | select(.path==(".worktrees/planning/"+$p) or .path==$p) | {actor:.values.actor,subject_ref:.values.subject_ref}' "$inventory" | head -n 1)
jq -e '(.actor == {id:"codex-cc",mode:"agent-direct",role:"extractor"}) and (.subject_ref|has("actor")|not)' <<< "$support_scope" >/dev/null || fail "support actor scope did not reproduce"
wrong_mode=$(jq -c '.native_census.support_witnesses[0].actor.mode="worker-scope"' <<< "$valid_registry")
if jq -e --arg actual "$support_actual" '.native_census.support_witnesses[0].actor|tojson == $actual' <<< "$wrong_mode" >/dev/null; then fail "wrong actor mode was accepted"; else wrong_mode_status=$?; [[ "$wrong_mode_status" == 1 ]] || fail "wrong mode control had unexpected status"; fi
wrong_role=$(jq -c '.native_census.support_witnesses[0].actor.role="validator"' <<< "$valid_registry")
if jq -e --arg actual "$support_actual" '.native_census.support_witnesses[0].actor|tojson == $actual' <<< "$wrong_role" >/dev/null; then fail "wrong actor role was accepted"; else wrong_role_status=$?; [[ "$wrong_role_status" == 1 ]] || fail "wrong role control had unexpected status"; fi
swapped_actor=$(jq -c '.native_census.support_witnesses[0].actor={id:"codex-cc",mode:"extractor",role:"agent-direct"}' <<< "$valid_registry")
if jq -e --arg actual "$support_actual" '.native_census.support_witnesses[0].actor|tojson == $actual' <<< "$swapped_actor" >/dev/null; then fail "swapped mode and role were accepted"; else swapped_status=$?; [[ "$swapped_status" == 1 ]] || fail "swapped control had unexpected status"; fi
check_no_propagation() { jq -e '[.native_census.support_witnesses[]|select(has("subject_ref_actor"))]|length==0' <<< "$1" >/dev/null; }
check_no_propagation "$valid_registry" || fail "authored support actor scope is propagated"
propagated_actor=$(jq -c --arg id "$support_subject" '.native_census.support_witnesses[0].subject_ref_actor={id:"codex-cc",mode:"agent-direct",role:"extractor"}' <<< "$valid_registry")
if check_no_propagation "$propagated_actor"; then fail "support actor propagation was accepted"; else propagation_status=$?; [[ "$propagation_status" == 1 ]] || fail "propagation control had unexpected status"; fi

no_match_path="project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/artifacts/no-such-record.md"
no_match_count=$(jq -r --arg p "$no_match_path" '[.records[]|select(.path==$p)]|length' "$inventory")
[[ "$no_match_count" == 0 ]] || fail "no-match path unexpectedly matched"
no_match_actors_status=0
no_match_actors=$(jq -c --arg p "$no_match_path" '[.records[]|select(.path==$p)|.values.actor]' "$inventory") || no_match_actors_status=$?
[[ "$no_match_actors_status" == 0 && "$no_match_actors" == "[]" ]] || fail "no-match actor projection was not literal []"
if jq -e '.records' "$temp/no-such-inventory.json" >/dev/null 2>&1; then fail "missing input was accepted"; else missing_status=$?; [[ "$missing_status" == 2 || "$missing_status" == 1 ]] || fail "missing input control had unexpected status"; fi

fixture=$temp/support-propagation-fixture.json
jq -n --arg id "$support_subject" --argjson actor "$expected_support" '{subject:{id:$id,actor:null},support:{subject_ref:$id,actor:$actor}}' > "$fixture"
jq -e --arg id "$support_subject" '(.support.subject_ref==$id) and (.support.actor=={id:"codex-cc",mode:"agent-direct",role:"extractor"}) and (.subject.actor==null)' "$fixture" >/dev/null || fail "support propagation fixture failed"

printf '%s\n' "native_census=$actual_census" "legacy_census=$legacy_census" "wrong_yaml_status=$wrong_yaml_status" "wrong_member_status=$wrong_member_status" "dangling_status=$dangling_status" "wrong_hash_status=$wrong_hash_status" "wrong_authority_status=$wrong_authority_status" "range_unknown_status=$range_unknown_status" "range_misplaced_status=$range_misplaced_status" "range_oob_status=$range_oob_status" "range_reversed_status=$range_reversed_status" "absence_status=$absence_status" "wrong_mode_status=$wrong_mode_status" "wrong_role_status=$wrong_role_status" "swapped_status=$swapped_status" "propagation_status=$propagation_status" "missing_status=$missing_status" "no_match_count=$no_match_count" "no_match_actors_status=$no_match_actors_status" "no_match_actors=$no_match_actors"
~~~

## Recorded observations

The precommit route was designed to fail closed on wrong hashes, wrong YAML
exclusions, invalid membership, dangling evidence references, out-of-bounds or
reversed ranges, wrong actor mode, wrong actor role, swapped mode/role, support
actor propagation, no-match drift, and missing input. The native positive
controls are the four inventory support witnesses and the exact literal actor
object `{ "id": "codex-cc", "mode": "agent-direct", "role": "extractor" }`.

The route records its execution output here after the six-file CC endpoint is
committed. A successful route is structural evidence only; it does not accept
the ontology, authorize vocabulary, or close CDC/CRC/UAT gates.

## Working-tree precommit observation

The route passed with status 0 before the CC endpoint commit. Native output was
12 selected records with kind counts `2/1/2/1/5/1`, actor parents `2 absent,
10 object`, child states `6 null, 4 string` among object parents, four exact
populated support witnesses, three YAML exclusions, fifteen no-frontmatter
records and 2,054 legacy parent-absent records. The negative controls returned
status 1 for wrong YAML, invalid membership, dangling evidence, wrong hash,
wrong declared authority, unknown and misplaced range descriptors,
out-of-bounds range, reversed range, absence-as-null, wrong mode, wrong role,
swapped mode/role and support propagation; missing input returned status 2.
The route validated all 45 rows: 42 numeric line descriptors and the three
exact JSON-document descriptors. The real no-match actor projection returned
the literal `[]` with status 0, while its separate count was 0.

## Committed endpoint observations

The committed wrapper loaded the registry and recipe from the same CC endpoint
`9c8ea3a2` and passed with status 0. The true missing-recipe endpoint, opening
planning commit `3b7790f88cd30fa6c4988a6950b4989ae1933b7d`, failed closed with
status 2, and the foreign source endpoint `ce3f77103eff5e07b3533a03c65f158684fc1039`
also failed closed with status 2. An exploratory replay against intermediate
planning endpoint `ac618e0fd3c428a68587b8195bc4c5817351a336` returned status 1
because that older recipe still used the predecessor scope baseline and saw
the protected iteration records as out of scope; it is not the missing-recipe
observation. The first literal-wrapper shell invocation also failed before
route execution because of nested-quote parsing; the equivalent quote-safe
wrapper was then rerun and passed. The wrapper must load the registry from the
CC endpoint and recipe bytes from the separately supplied replay endpoint; it
must not fall back to the working tree. A successful route remains structural
evidence only.

The separate committed replay loaded the registry from CC endpoint `9c8ea3a2`
and recipe bytes from replay endpoint `3079b62b`; it passed with status 0. The
separate endpoint pair confirms that the recipe is independently selected from
the registry endpoint rather than inferred from the same commit.
