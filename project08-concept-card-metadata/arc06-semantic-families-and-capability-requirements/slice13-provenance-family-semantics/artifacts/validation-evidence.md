# Slice13 validation and literal replay

Status: CC proposed-done; this file records reproducible structural and native
diagnostic evidence, not independent semantic acceptance. The repair addresses
CDC findings R1-R4 without changing the eight-pair scope, source, coverage,
schema, runtime or memory state.

## Fixed boundaries and evidence layers

- Source opening commit: `e763c661592ff1097a94bb470db9cf924524579d`, expected
  clean throughout and read-only.
- Original contribution: `609f2f558b100a06df42e6a8b85ebfe200a27b22` to
  `78be7fabae79039ef3f24daa639d8e314ebcee0f`, exactly six CC files.
- Repair contribution: `e42419482aebabcdac9be9e3032daa8f72da09d3` to the new
  repair CC endpoint, restricted to the authorized subset of those six files.
  Intervening CDC plans, review and prompt files are not part of this diff.
- Repair-opening plan and coverage authority are read from the explicit Git
  snapshot `e42419482aebabcdac9be9e3032daa8f72da09d3`; the current live
  coverage register is inspected separately for status and accounting only.
- `semantic-membership.json` is the registry authority. In committed mode it
  is loaded from `CC_COMMIT`, never from a later working-tree copy. In precommit
  mode the live candidate registry is explicitly allowed.
- Registered input count is derived from the validated registry. Each declared
  snapshot/live hash is recomputed, and the declared rich/teaching mappings are
  checked against both manifests and native bytes.

The route has one fail-closed invocation wrapper and one literal replay block.
The wrapper's `REPLAY_COMMIT` selects the recipe revision; `CC_COMMIT` selects
the contribution endpoint whose registry is inspected. A missing Git object or
empty extracted block is an error, not an empty successful shell.

## Fail-closed invocation wrapper

Run the following from any directory. For precommit mode, stage the six files
and set `CC_PRECOMMIT=1`. For committed mode, set both variables explicitly;
using the same SHA for recipe and contribution is valid but their roles remain
separate.

~~~bash
set -euo pipefail
source=/Users/oubiwann/lab/billosys/ai-engineering
plan=$source/.worktrees/planning
project=project08-concept-card-metadata
arc=arc06-semantic-families-and-capability-requirements
slice=$project/$arc/slice13-provenance-family-semantics
validation_rel=$slice/artifacts/validation-evidence.md
precommit=${CC_PRECOMMIT:-}
cc_commit=${CC_COMMIT:-}
recipe_commit=${REPLAY_COMMIT:-}

if [ -n "$precommit" ]; then
  test "$precommit" = 1
  test -z "$cc_commit"
  recipe=$(awk '/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p' "$plan/$validation_rel")
  test -n "$recipe"
  printf 'recipe_revision=live-precommit contribution_endpoint=working-tree-candidate\n'
  CC_PRECOMMIT=1 bash <<< "$recipe"
else
  test -n "$cc_commit"
  test -n "$recipe_commit"
  git -C "$plan" cat-file -e "$cc_commit^{commit}"
  git -C "$plan" cat-file -e "$recipe_commit^{commit}"
  recipe=$(git -C "$plan" show "$recipe_commit:$validation_rel" |
    awk '/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p')
  test -n "$recipe"
  printf 'recipe_revision=%s contribution_endpoint=%s\n' "$recipe_commit" "$cc_commit"
  CC_COMMIT="$cc_commit" bash <<< "$recipe"
fi
~~~

## Literal route

~~~bash
set -euo pipefail

source=/Users/oubiwann/lab/billosys/ai-engineering
plan=$source/.worktrees/planning
cd "$source"

project=project08-concept-card-metadata
arc=arc06-semantic-families-and-capability-requirements
slice=$project/$arc/slice13-provenance-family-semantics
membership_rel=$slice/artifacts/semantic-membership.json
coverage_rel=$project/artifacts/semantic-coverage-current.json
transition_rel=$project/artifacts/semantic-transition-coverage.json
inventory_rel=$project/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
slice_plan_rel=$slice/slice-plan.md
opening_source=e763c661592ff1097a94bb470db9cf924524579d
original_opening=609f2f558b100a06df42e6a8b85ebfe200a27b22
original_endpoint=78be7fabae79039ef3f24daa639d8e314ebcee0f
repair_opening=e42419482aebabcdac9be9e3032daa8f72da09d3
opening_inventory_sha=afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b
cc_commit=${CC_COMMIT:-}
precommit=${CC_PRECOMMIT:-}
tmp=$(mktemp -d /private/tmp/cc-slice13-repair.XXXXXX)
trap 'rm -rf "$tmp"' EXIT

test "$(git -C "$source" rev-parse HEAD)" = "$opening_source"
test -z "$(git -C "$source" status --porcelain)"
test "$(git -C "$plan" rev-parse "$repair_opening^{commit}")" = "$repair_opening"
printf 'source=%s repair_opening=%s\n' "$opening_source" "$repair_opening"
printf 'bash=%s jq=%s rg=%s\n' "$(bash --version|head -1)" "$(jq --version)" "$(rg --version|head -1)"

expected_files=$(printf '%s\n' \
  "$slice/artifacts/semantic-membership.json" \
  "$slice/artifacts/semantic-evidence.md" \
  "$slice/artifacts/validation-evidence.md" \
  "$slice/artifacts/handoff.md" \
  "$slice/ledger.md" \
  "$slice/closing-report.md" | sort)

# Preserve the original contribution boundary separately from this repair.
original_files=$(git -C "$plan" diff --name-only "$original_opening" "$original_endpoint" -- | sort)
test "$original_files" = "$expected_files"
git -C "$plan" diff --check "$original_opening" "$original_endpoint"
printf 'original-boundary=%s..%s exact-six-files\n' "$original_opening" "$original_endpoint"

if [ -n "$precommit" ]; then
  test "$precommit" = 1
  test -z "$cc_commit"
  actual_files=$( { \
    git -C "$plan" diff --name-only "$repair_opening" --; \
    git -C "$plan" diff --cached --name-only "$repair_opening" --; \
    git -C "$plan" ls-files --others --exclude-standard; \
  } | sort -u )
  test "$actual_files" = "$expected_files"
  git -C "$plan" diff --check "$repair_opening" --
  git -C "$plan" diff --cached --check
  membership=$plan/$membership_rel
  printf 'repair-boundary=precommit opening=%s authorized-six-file-union\n' "$repair_opening"
else
  test -n "$cc_commit"
  git -C "$plan" cat-file -e "$cc_commit^{commit}"
  actual_files=$(git -C "$plan" diff --name-only "$repair_opening" "$cc_commit" -- | sort)
  test "$actual_files" = "$expected_files"
  git -C "$plan" diff --check "$repair_opening" "$cc_commit"
  membership=$tmp/semantic-membership.json
  git -C "$plan" show "$cc_commit:$membership_rel" > "$membership"
  test -s "$membership"
  printf 'repair-boundary=committed opening=%s endpoint=%s authorized-six-file-diff\n' "$repair_opening" "$cc_commit"
fi

# These are the intervening CDC/planning files. They are protected from the
# repair diff; the original contribution is checked above, not recomputed as
# if it were the repair's history.
if [ -z "$precommit" ]; then
  protected=(
    "$project/project-plan.md"
    "$project/ledger.md"
    "$project/$arc/arc-plan.md"
    "$project/$arc/ledger.md"
    "$project/$arc/slice13-provenance-family-semantics/slice-plan.md"
    "$project/$arc/slice13-provenance-family-semantics/cc-prompt.md"
    "$project/$arc/slice13-provenance-family-semantics/artifacts/iteration-01-cc-prompt.md"
    "$project/$arc/slice13-provenance-family-semantics/cdc-verification.md"
    "$coverage_rel"
    "$transition_rel"
    "$project/$arc/slice01-relationship-semantics-and-traversal/cdc-verification.md"
    "$project/$arc/slice02-competency-questions-and-answerability/cdc-verification.md"
    "$project/$arc/slice03-provenance-and-shared-reference-contracts/cdc-verification.md"
  )
  for p in "${protected[@]}"; do
    git -C "$plan" diff --exit-code "$repair_opening" "$cc_commit" -- "$p"
  done
fi

# Registry validity is checked from the actual endpoint. These predicates bind
# scope, membership pairs, meaning IDs, and both member/shared evidence layers.
assignment=$(git -C "$plan" show "$repair_opening:$slice_plan_rel" |
  awk '/^~~~json$/{p=1;next} /^~~~$/{if(p){exit}} p' | jq -c .)
test -n "$assignment"
jq -e 'type=="array" and length==8 and (unique|length)==8' <<< "$assignment" >/dev/null

registry_predicate='
  . as $doc |
  ($doc.memberships | map([.field_path,.record_kind])) as $pairs |
  ($doc.evidence | map(.evidence_id)) as $evidence_ids |
  ($doc.meanings | keys) as $meaning_ids |
  ($doc.memberships | map(.meaning_id)) as $member_meaning_ids |
  ($pairs|length)==8 and ($pairs|unique|length)==8 and
  ($pairs==$plan_assignment) and
  ($doc.scope.assignment==$plan_assignment) and
  (($member_meaning_ids|unique|sort)==($meaning_ids|sort)) and
  (($evidence_ids|unique|length)==($evidence_ids|length)) and
  all($doc.memberships[]; . as $member |
    ($doc.meanings|has($member.meaning_id)) and
    all($member.evidence_ids[]; . as $id | any($doc.evidence[]; .evidence_id==$id))) and
  all(($doc.meanings|to_entries[]); .value as $meaning |
    all($meaning.evidence_ids[]; . as $id | any($doc.evidence[]; .evidence_id==$id)))
'
jq -e --argjson plan_assignment "$assignment" "$registry_predicate" "$membership" >/dev/null
printf 'registry=actual-memberships-scope-meanings-and-both-evidence-layers-valid\n'

# The same registry predicates must reject isolated mutation variants.
jq '.memberships[0].field_path="deliberately-invalid-field"' \
  "$membership" > "$tmp/invalid-member.json"
jq '.memberships[0].evidence_ids += ["missing-member-evidence"] |
   .meanings["actor-claim"].evidence_ids += ["missing-shared-evidence"]' \
  "$membership" > "$tmp/dangling-reference.json"
set +e
jq -e --argjson plan_assignment "$assignment" "$registry_predicate" "$tmp/invalid-member.json" >/dev/null
invalid_member_status=$?
jq -e --argjson plan_assignment "$assignment" "$registry_predicate" "$tmp/dangling-reference.json" >/dev/null
dangling_reference_status=$?
set -e
test "$invalid_member_status" -ne 0
test "$dangling_reference_status" -ne 0
printf 'control.invalid-member.status=%s classification=assignment-membership-rejection\n' "$invalid_member_status"
printf 'control.dangling-reference.status=%s classification=meaning-or-member-evidence-rejection\n' "$dangling_reference_status"

# Every registered evidence hash is recomputed from its declared root/mode.
evidence_count=$(jq -r '.evidence|length' "$membership")
test "$evidence_count" -gt 0
while IFS=$'\t' read -r root path expected mode authority; do
  case "$root:$mode" in
    source:snapshot) actual=$(git -C "$source" show "$authority:$path" | shasum -a 256 | awk '{print $1}') ;;
    planning:snapshot) actual=$(git -C "$plan" show "$authority:$path" | shasum -a 256 | awk '{print $1}') ;;
    source:live) actual_path=$source/$path; test -f "$actual_path"; actual=$(shasum -a 256 "$actual_path" | awk '{print $1}') ;;
    planning:live) actual_path=$plan/$path; test -f "$actual_path"; actual=$(shasum -a 256 "$actual_path" | awk '{print $1}') ;;
    absolute:live) actual_path=$path; test -f "$actual_path"; actual=$(shasum -a 256 "$actual_path" | awk '{print $1}') ;;
    *) printf 'unsupported evidence root/mode: %s\n' "$root:$mode" >&2; exit 1 ;;
  esac
  test "$actual" = "$expected"
done < <(jq -r '.evidence[] | [.root,.path,.sha256,.read_mode,(.authority_commit//"")] | @tsv' "$membership")
printf 'registered-input-hashes=%s/%s matched\n' "$evidence_count" "$evidence_count"

# Derive assignment authority from the repair-opening plan and coverage
# snapshot. The live register is checked only for current structural status.
git -C "$plan" show "$repair_opening:$coverage_rel" > "$tmp/opening-coverage.json"
opening_coverage_sha=$(shasum -a 256 "$tmp/opening-coverage.json" | awk '{print $1}')
live_coverage_sha=$(shasum -a 256 "$plan/$coverage_rel" | awk '{print $1}')
jq -e --argjson assignment "$assignment" '
  .artifact_kind=="current-semantic-coverage" and
  .counts.full==555 and .counts.accepted==180 and .counts.remaining==375 and
  .counts.next_slice==8 and .counts.not_yet_sliced==367 and
  .next_slice_pairs==$assignment and
  (.accepted_pairs|length)==180 and (.remaining_pairs|length)==375 and
  ((.accepted_pairs+.remaining_pairs)|unique|length)==555 and
  (.accepted_pairs as $a | .remaining_pairs as $r |
    all($assignment[]; . as $p | any($r[]; .==$p) and all($a[]; .!=$p)))
' "$tmp/opening-coverage.json" >/dev/null
jq -e --argjson assignment "$assignment" --argjson opening "$(jq -c . "$tmp/opening-coverage.json")" '
  .scope.assignment==$assignment and
  .scope.counts.full==$opening.counts.full and
  .scope.counts.accepted==$opening.counts.accepted and
  .scope.counts.remaining==$opening.counts.remaining and
  .scope.counts.assigned==$opening.counts.next_slice and
  .scope.counts.outside==$opening.counts.not_yet_sliced
' "$membership" >/dev/null
jq -e '
  .artifact_kind=="current-semantic-coverage" and
  .counts.full==((.accepted_pairs|length)+(.remaining_pairs|length)) and
  .counts.accepted==(.accepted_pairs|length) and
  .counts.remaining==(.remaining_pairs|length) and
  .counts.next_slice==(.next_slice_pairs|length) and
  .counts.full==(.counts.accepted+.counts.remaining) and
  .counts.remaining==(.counts.next_slice+.counts.not_yet_sliced) and
  ((.accepted_pairs+.remaining_pairs)|unique|length)==.counts.full and
  ((.next_slice_pairs-.remaining_pairs)|length)==0
' "$plan/$coverage_rel" >/dev/null
printf 'coverage.opening.sha256=%s live.sha256=%s\n' "$opening_coverage_sha" "$live_coverage_sha"
printf 'coverage.opening=%s live=%s\n' "$(jq -c .counts "$tmp/opening-coverage.json")" "$(jq -c .counts "$plan/$coverage_rel")"

git -C "$plan" show "$repair_opening:$transition_rel" > "$tmp/transition-coverage.json"
jq -e '
  .artifact_kind=="project08-semantic-transition-coverage" and
  .counts.full==555 and .counts.accepted==115 and .counts.remaining==440 and
  .counts.next_slice==35 and .counts.not_yet_sliced==405 and
  (.accepted_pairs|length)==115 and (.remaining_pairs|length)==440 and
  ((.accepted_pairs+.remaining_pairs)|unique|length)==555
' "$tmp/transition-coverage.json" >/dev/null
printf 'transition=115/440 preserved from repair-opening snapshot\n'

# Frozen native inventory: all selected census cells, family/state/label
# breakdown, and named YAML parse exclusions are compared to authored values.
git -C "$plan" show "$repair_opening:$inventory_rel" > "$tmp/inventory.json"
inventory=$tmp/inventory.json
test "$(shasum -a 256 "$inventory" | awk '{print $1}')" = "$opening_inventory_sha"
actual_selected=$(jq -c '
  def selected: [.records[] | select((.record_kind=="claim" or .record_kind=="competency-question" or .record_kind=="concept-card" or .record_kind=="extraction-run") and (.values|type=="object"))];
  def parent_state:
    if ((.values|has("actor"))|not) then "absent"
    elif (.values.actor|type)=="null" then "null"
    elif (.values.actor|type)=="object" and (.values.actor|length)==0 then "empty_object"
    elif (.values.actor|type)=="object" then "object"
    else "unexpected_type" end;
  def id_state:
    if parent_state=="absent" then "not_applicable_parent_absent"
    elif (.values.actor|type)!="object" then "unexpected_type"
    elif ((.values.actor|has("id"))|not) then "missing_in_object"
    elif .values.actor.id==null then "null"
    elif (.values.actor.id|type)=="string" and .values.actor.id=="" then "empty_string"
    elif (.values.actor.id|type)=="string" then "string"
    else "unexpected_type" end;
  def family:
    if (.path|startswith("knowledge/concept-cards/templates/")) then "template"
    elif (.path|startswith("knowledge/concept-cards/examples/")) then "synthetic"
    elif (.path|startswith(".worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02")) then "arc07-pilot"
    elif (.path|startswith(".worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04")) then "arc07-expanded"
    elif (.path|startswith("workbench/compcogneuro-rich-rerun-2026-09-12/")) then "rich-rerun"
    elif (.path|startswith("workbench/compcogneuro-teaching-rerun-2026-09-12/")) then "teaching-rerun"
    else "unexpected" end;
  def fill($keys): reduce $keys[] as $key (.; .[$key]=(.[$key]//0));
  (selected) as $r |
  {
    parsed_selected_mappings:($r|length),
    record_kind_counts:($r|group_by(.record_kind)|map({key:.[0].record_kind,value:length})|from_entries),
    actor_parent_states:($r|map({state:parent_state})|group_by(.state)|map({key:.[0].state,value:length})|from_entries|fill(["absent","null","empty_object","object","unexpected_type"])),
    actor_id_states:($r|map({state:id_state})|group_by(.state)|map({key:.[0].state,value:length})|from_entries|fill(["not_applicable_parent_absent","missing_in_object","null","empty_string","string","unexpected_type"])),
    by_kind:($r|map({kind:.record_kind,parent:parent_state,id:id_state})|group_by(.kind)|map({key:.[0].kind,value:{records:length,parent_absent:map(select(.parent=="absent"))|length,parent_object_null_id:map(select(.parent=="object" and .id=="null"))|length,parent_object_string_id:map(select(.parent=="object" and .id=="string"))|length}})|from_entries),
    family_breakdown:($r|map({family:family,parent:parent_state,id:id_state})|group_by(.family)|map({key:.[0].family,value:{records:length,parent_absent:map(select(.parent=="absent"))|length,parent_object_null_id:map(select(.parent=="object" and .id=="null"))|length,parent_object_string_id:map(select(.parent=="object" and .id=="string"))|length}})|from_entries),
    actor_label_breakdown:{id_labels:($r|map(select(id_state=="string")|.values.actor.id)|group_by(.)|map({key:.[0],value:length})|from_entries),mode_labels:($r|map(select(id_state=="string")|.values.actor.mode)|group_by(.)|map({key:.[0],value:length})|from_entries),role_labels:($r|map(select(id_state=="string")|.values.actor.role)|group_by(.)|map({key:.[0],value:length})|from_entries)}
  }
' "$inventory")
authored_selected=$(jq -c '.native_census | {parsed_selected_mappings,record_kind_counts,actor_parent_states,actor_id_states,by_kind:(.by_kind|with_entries(.value|=del(.witness,.witnesses))),family_breakdown,actor_label_breakdown}' "$membership")
jq -n -e --argjson authored "$authored_selected" --argjson observed "$actual_selected" '$authored==$observed' >/dev/null
actual_legacy=$(jq -c '
  ([.records[]|select((.record_kind//"untyped")=="untyped")|select(.values|type=="object")]) as $l |
  {parsed_mappings:($l|length),
   actor_parent_states:{absent:($l|map(select((.values|has("actor"))|not))|length),null:($l|map(select((.values|has("actor")) and (.values.actor==null)))|length),empty_object:($l|map(select((.values.actor|type)=="object" and (.values.actor|length)==0))|length),object:($l|map(select((.values.actor|type)=="object" and (.values.actor|length)>0))|length),unexpected_type:($l|map(select((.values|has("actor")) and (.values.actor!=null) and ((.values.actor|type)!="object")))|length)},
   actor_id_states:{not_applicable_parent_absent:($l|map(select((.values|has("actor"))|not))|length),missing_in_object:($l|map(select((.values.actor|type)=="object" and ((.values.actor|has("id"))|not)))|length),null:($l|map(select((.values.actor|type)=="object" and .values.actor.id==null))|length),empty_string:($l|map(select((.values.actor.id|type)=="string" and .values.actor.id==""))|length),string:($l|map(select((.values.actor.id|type)=="string" and .values.actor.id!=""))|length),unexpected_type:($l|map(select((.values|has("actor")) and (.values.actor|type)=="object" and (.values.actor|has("id")) and (.values.actor.id!=null) and (.values.actor.id|type)!="string"))|length)},
   literal_dotted_actor_id_keys:($l|map(select(.values|has("actor.id")))|length)}
' "$inventory")
authored_legacy=$(jq -c '.native_census.legacy_untyped_census|del(.meaning)' "$membership")
jq -n -e --argjson authored "$authored_legacy" --argjson observed "$actual_legacy" '$authored==$observed' >/dev/null
actual_exclusions=$(jq -c '[.records[]|select((.error? // "")|startswith("YAML::XS"))|.path]|sort|{count:length,records:.}' "$inventory")
authored_exclusions=$(jq -c '.native_census.parse_exclusions|{count,records:(.records|sort)}' "$membership")
jq -n -e --argjson authored "$authored_exclusions" --argjson observed "$actual_exclusions" '$authored==$observed' >/dev/null
printf 'native-census=authored 37-record family/state/label cells and 3 named YAML exclusions reconcile\n'
printf 'legacy-untyped=authored 2054 parsed mappings; actor-parent-absent=2054; nested-actor.id=not-applicable; dotted-key=0\n'

# Declared original/copy mappings must resolve through their registered
# manifests and the native bytes; no hard-coded cmp-only assertion is used.
source_manifest=$(jq -r '.evidence[]|select(.evidence_id=="sourceBaselineManifest")|.path' "$membership")
copy_manifest=$(jq -r '.evidence[]|select(.evidence_id=="copyBaselineManifest")|.path' "$membership")
test -n "$source_manifest"; test -n "$copy_manifest"
while IFS=$'\t' read -r mapping_id original_root original_path original_sha copy_root copy_path copy_sha manifest_ids; do
  test "$original_root" = source; test "$copy_root" = planning
  test -f "$source/$original_path"; test -f "$plan/$copy_path"
  test "$(shasum -a 256 "$source/$original_path"|awk '{print $1}')" = "$original_sha"
  test "$(shasum -a 256 "$plan/$copy_path"|awk '{print $1}')" = "$copy_sha"
  rg -F -x -- "$original_sha  $original_path" "$plan/$source_manifest" >/dev/null
  rg -F -x -- "$copy_sha  .worktrees/planning/$copy_path" "$plan/$copy_manifest" >/dev/null
  cmp "$source/$original_path" "$plan/$copy_path"
  witness_id=$(jq -r --arg p "$original_path" --arg h "$original_sha" '[.evidence[]|select(.root=="source" and .path==$p and .sha256==$h)|.evidence_id]|if length==1 then .[0] else empty end' "$membership")
  test -n "$witness_id"
  case "$manifest_ids" in *sourceBaselineManifest*) ;; *) exit 1;; esac
  case "$manifest_ids" in *copyBaselineManifest*) ;; *) exit 1;; esac
  case "$manifest_ids" in *"$witness_id"*) ;; *) exit 1;; esac
  printf 'baseline-mapping=%s manifest-entries-and-native-bytes-match witness=%s\n' "$mapping_id" "$witness_id"
done < <(jq -r '.baseline_mappings[]|[.mapping_id,.original_root,.original_path,.original_sha256,.copy_root,.copy_path,.copy_sha256,(.manifest_evidence_ids|join(","))]|@tsv' "$membership")

# Native diagnostics: expected values are authored independently of observed
# inventory values. Raw actor rg search is deliberately removed; it was
# redundant with this hash-bound field-state proof and had swallowed errors.
rich_path=workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
native_actor=$(jq -c --arg p "$rich_path" '.records[]|select(.path==$p)|.values.actor' "$inventory")
expected_actor='{"id":"codex","mode":"agent-direct","role":"extractor"}'
jq -n -e --argjson expected "$expected_actor" --argjson observed "$native_actor" '$expected==$observed' >/dev/null
wrong_actor='{"id":"codex-deliberately-wrong","mode":"agent-direct","role":"extractor"}'
set +e
jq -n -e --argjson expected "$wrong_actor" --argjson observed "$native_actor" '$expected==$observed' >/dev/null
wrong_actor_status=$?
set -e
test "$wrong_actor_status" = 1
printf 'diagnostic1.match=codex/agent-direct/extractor; wrong-expected.status=%s classification=comparison_failure\n' "$wrong_actor_status"

template_path=knowledge/concept-cards/templates/concept-card.md
expanded_path=.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards/cc-complementary-learning-systems.md
template_actor=$(jq -c --arg p "$template_path" '.records[]|select(.path==$p)|.values.actor' "$inventory")
expected_template_actor='{"id":null,"mode":null,"role":null}'
jq -n -e --argjson expected "$expected_template_actor" --argjson observed "$template_actor" '$expected==$observed' >/dev/null
jq -e --arg p "$expanded_path" '.records[]|select(.path==$p)|(.values|has("actor")|not)' "$inventory" >/dev/null
printf 'diagnostic2.template=object/null; diagnostic2.expanded=parent_absent/child_not_applicable\n'

wrong_path=$(jq -c --arg p 'no-such-actor-record.md' '[.records[]|select(.path==$p)]' "$inventory")
test "$wrong_path" = '[]'
set +e
jq -c --arg p 'no-such-actor-record.md' '[.records[]|select(.path==$p)]' "$tmp/no-such-inventory.json" > "$tmp/missing.stdout" 2> "$tmp/missing.stderr"
missing_status=$?
set -e
test "$missing_status" = 2
test ! -s "$tmp/missing.stdout"
test -s "$tmp/missing.stderr"
printf 'lookup.successful_no_match.status=0; lookup.missing-input.status=%s classification=tool_error stderr_nonempty=true\n' "$missing_status"

if [ -z "$precommit" ]; then
  test -z "$(git -C "$plan" status --porcelain)"
fi
test -z "$(git -C "$source" status --porcelain)"
printf 'history=original-and-repair-boundaries-separated; protected-history=unchanged; source-status=clean\n'
printf 'json=structural-comparisons-pass; semantic-acceptance=not-claimed\n'
~~~

## Claimed control classes and limits

The valid registry passes actual scope, unique membership, plan-derived
assignment, meaning IDs and both member/shared evidence-ID layers. The same
predicates reject an invalid member path and dangling member/shared references.
The evidence count is read from the registry rather than a stale constant.

The repair-opening plan and coverage snapshot establish 180 accepted / 375
remaining / eight assigned / 367 outside; the live register is printed and
checked only for current accounting invariants. The immutable 115/440
transition remains pinned. The original six-file history and repair
opening-to-endpoint history are checked separately, with project-prefixed
protected paths.

The native route compares every authored selected census cell, including the
37-record family/state/label breakdown, three named YAML exclusions and the
2,054 parsed legacy untyped mappings. It retains parent absence as the reason
that nested `actor.id` is not applicable. The declared rich/teaching mappings
must match registered source/copy manifest entries, native hashes and bytes.

The positive generated-card diagnostic matches `codex/agent-direct/extractor`;
the wrong identity rejects with comparison status 1. The template object/null
and expanded parent-absent states remain distinct. A successful no-match is
status 0, while missing inventory input is jq status 2 with stderr. The raw
actor search that previously converted errors into absence is explicitly not
used; hash-bound native field-state proof and the real jq missing-input control
remain.

These checks establish structural binding and bounded observations only. They
do not establish actor authority, identity uniqueness, semantic verification,
requiredness, schema conformance, operator acceptance or memory admission.
CDC must independently run the committed wrapper against the actual repair
endpoint. Rows S13-1 and S13-6 retain their prior CDC-verified status; this
repair can only make S13-2 through S13-5 CC-attested proposed-done.
