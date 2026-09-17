# Slice14 validation evidence: literal native replay

Status: CC proposed-done; independent CRC verification is required. This
record is an evidence route and its observations, not a semantic-acceptance
verdict.

## Boundaries and modes

The route below uses only Bash, Git, jq, shasum and the repository's native
inventory. It has two explicit modes:

- precommit mode (CC_PRECOMMIT=1) reads the working-tree registry, covers the
  staged/unstaged/named-new union, and does not require the planning checkout
  to be clean;
- committed mode requires both CC_COMMIT and REPLAY_COMMIT, reads the
  registry from CC_COMMIT, executes the literal route extracted from the
  validation-evidence.md at REPLAY_COMMIT, checks the opening-to-CC six-file
  contribution, and requires clean source and planning checkouts.

CC_COMMIT is the contribution endpoint. REPLAY_COMMIT is the recipe endpoint.
They are intentionally separate. The route does not inspect or change
coverage acceptance, reviewer status, schema authority, operator acceptance,
source truth, memory admission or runtime behavior.

## Literal route

Run from the planning checkout. The committed invocation is:

~~~text
CC_COMMIT=<cc-endpoint> REPLAY_COMMIT=<recipe-endpoint> bash -c '
set -euo pipefail
recipe=$(git show "$REPLAY_COMMIT:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice14-provenance-context-and-reference-semantics/artifacts/validation-evidence.md") || exit 2
code=$(printf "%s\n" "$recipe" | awk '"'"'/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p'"'"') || exit 2
[[ -n "$code" ]] || exit 2
printf "%s\n" "$code" | bash -s
'
~~~

The precommit invocation is:

~~~text
CC_PRECOMMIT=1 bash -s < <(awk '/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p' project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice14-provenance-context-and-reference-semantics/artifacts/validation-evidence.md)
~~~

~~~bash
set -euo pipefail

fail() {
  printf '%s\n' "FAIL: $*" >&2
  exit 1
}

root=$(git rev-parse --show-toplevel)
source=$(cd "$root/../.." && pwd)
membership_rel=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice14-provenance-context-and-reference-semantics/artifacts/semantic-membership.json
validation_rel=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice14-provenance-context-and-reference-semantics/artifacts/validation-evidence.md
slice_rel=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice14-provenance-context-and-reference-semantics
coverage_rel=project08-concept-card-metadata/artifacts/semantic-coverage-current.json
transition_rel=project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
inventory_rel=project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
opening_source=020268248882358075b678bb855c0ac8d11b532a
opening_planning=8e6b67708eeeca391a139bb8d1b710633cfbbeb4
historical_source=e763c661592ff1097a94bb470db9cf924524579d
mode=precommit

temp=$(mktemp -d)
trap 'rm -rf "$temp"' EXIT HUP INT TERM

if [[ -n "${CC_COMMIT:-}" ]]; then
  mode=committed
  [[ -n "${REPLAY_COMMIT:-}" ]] || fail "REPLAY_COMMIT is required with CC_COMMIT"
  git cat-file -e "$CC_COMMIT^{commit}" || fail "CC_COMMIT is not a commit"
  git cat-file -e "$REPLAY_COMMIT^{commit}" || fail "REPLAY_COMMIT is not a commit"
  git show "$CC_COMMIT:$membership_rel" > "$temp/semantic-membership.json" ||
    fail "registry is absent from CC_COMMIT"
  registry=$temp/semantic-membership.json
else
  [[ "${CC_PRECOMMIT:-}" == "1" ]] || fail "set CC_PRECOMMIT=1 or provide CC_COMMIT"
  registry=$root/$membership_rel
  [[ -s "$registry" ]] || fail "working-tree registry is absent or empty"
fi

[[ "$root" == /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning ]] ||
  fail "route must run from the canonical planning checkout"
source_current=$(git -C "$source" rev-parse HEAD)
[[ -z "$(git -C "$source" status --porcelain --untracked-files=all)" ]] ||
  fail "source checkout is not clean"
git diff --check || fail "planning working tree has whitespace errors"
git diff --cached --check || fail "planning index has whitespace errors"
git -C "$source" diff --exit-code "$historical_source" "$source_current" -- knowledge/concept-cards knowledge/document-extraction ||
  fail "registered relevant source tree differs from the historical source comparison"

fixture=$temp/unrelated-head-fixture
mkdir -p "$fixture/knowledge/concept-cards"
git init -q "$fixture"
printf '%s\n' "stable" > "$fixture/knowledge/concept-cards/stable.md"
git -C "$fixture" add -- knowledge/concept-cards/stable.md
git -C "$fixture" -c user.name="Slice14 validation" -c user.email="slice14@example.invalid" commit -qm base
printf '%s\n' "unrelated" > "$fixture/unrelated.txt"
git -C "$fixture" add -- unrelated.txt
git -C "$fixture" -c user.name="Slice14 validation" -c user.email="slice14@example.invalid" commit -qm unrelated
git -C "$fixture" diff --exit-code HEAD~1 HEAD -- knowledge/concept-cards ||
  fail "unrelated HEAD fixture changed a registered path"

allowed_paths="
$membership_rel
$slice_rel/artifacts/semantic-evidence.md
$validation_rel
$slice_rel/artifacts/handoff.md
$slice_rel/ledger.md
$slice_rel/closing-report.md
"
is_allowed() {
  case "$1" in
    "$membership_rel"|\
    "$slice_rel/artifacts/semantic-evidence.md"|\
    "$validation_rel"|\
    "$slice_rel/artifacts/handoff.md"|\
    "$slice_rel/ledger.md"|\
    "$slice_rel/closing-report.md") return 0 ;;
    *) return 1 ;;
  esac
}

if [[ "$mode" == precommit ]]; then
  changed_paths=$( {
    git diff --cached --name-only
    git diff --name-only
    git ls-files --others --exclude-standard
  } | sort -u )
  [[ -n "$changed_paths" ]] || fail "precommit union is empty"
  while IFS= read -r path; do
    [[ -z "$path" ]] && continue
    is_allowed "$path" || fail "out-of-scope staged/unstaged/named-new path: $path"
  done <<< "$changed_paths"
  for path in $allowed_paths; do
    grep -Fqx "$path" <<< "$changed_paths" ||
      fail "permitted path is missing from precommit union: $path"
  done
else
  [[ -z "$(git -C "$root" status --porcelain --untracked-files=all)" ]] ||
    fail "planning checkout is not clean for committed replay"
  committed_paths=$(git diff --name-only "$opening_planning" "$CC_COMMIT" | sort -u)
  while IFS= read -r path; do
    [[ -z "$path" ]] && continue
    is_allowed "$path" || fail "out-of-scope opening-to-CC path: $path"
  done <<< "$committed_paths"
  for path in $allowed_paths; do
    grep -Fqx "$path" <<< "$committed_paths" ||
      fail "permitted path is missing from opening-to-CC contribution: $path"
  done
fi

protected_paths="
project08-concept-card-metadata/project-plan.md
project08-concept-card-metadata/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/arc-plan.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/ledger.md
$slice_rel/slice-plan.md
$slice_rel/cc-prompt.md
$slice_rel/cc-prompt-iteration01.md
$slice_rel/cc-prompt-iteration02.md
project08-concept-card-metadata/artifacts/semantic-coverage-current.json
$transition_rel
$inventory_rel
"
for path in $protected_paths; do
  git diff --exit-code "$opening_planning" -- "$path" >/dev/null ||
    fail "protected planning path changed: $path"
done

jq empty "$registry" || fail "registry is not valid JSON"
assignment_json=$(git show "$opening_planning:$slice_rel/slice-plan.md" |
  awk '/^~~~json$/{n++; if (n == 1) {p=1; next}} p && /^~~~$/{exit} p')
[[ -n "$assignment_json" ]] || fail "opening assignment block is absent"
kinds_json=$(jq -c '[.[] | .[1]] | unique' <<< "$assignment_json")
jq -e --argjson assignment "$assignment_json" '
  .scope.assignment == $assignment
  and (.scope.assignment | length == 12)
  and ((.scope.assignment | map(@json) | unique | length) == 12)
' "$registry" >/dev/null || fail "registry assignment is not the exact twelve-pair opening assignment"

jq -e '
  .counts as $c
  | .counts == {full:555, accepted:188, remaining:367, next_slice:12, not_yet_sliced:355}
  and ((.accepted_pairs | length) == $c.accepted)
  and ((.remaining_pairs | length) == $c.remaining)
  and ((.next_slice_pairs | length) == $c.next_slice)
  and ((.accepted_pairs | map(@json) | unique | length) == $c.accepted)
  and ((.remaining_pairs | map(@json) | unique | length) == $c.remaining)
  and ((.accepted_pairs | map(@json) | sort) as $accepted
       | (.remaining_pairs | map(@json) | sort) as $remaining
       | (($accepted - $remaining) | length) == ($accepted | length))
' < <(git show "$opening_planning:$coverage_rel") >/dev/null ||
  fail "opening current coverage counts or disjointness failed"
jq -e --argjson assignment "$assignment_json" '
  (.remaining_pairs | map(@json) | sort) as $remaining
  | (.accepted_pairs | map(@json) | sort) as $accepted
  | (.next_slice_pairs | map(@json) | sort) as $next
  | ($assignment | map(@json) | sort) as $a
  | ($next == $a)
    and ((($a - $remaining) | length) == 0)
    and ((($a - $accepted) | length) == ($a | length))
' < <(git show "$opening_planning:$coverage_rel") >/dev/null ||
  fail "opening coverage does not place the exact assignment in remaining"

jq -e '
  .counts == {full:555, accepted:115, remaining:440, next_slice:35, not_yet_sliced:405}
  and (.counts.accepted + .counts.remaining == .counts.full)
  and (.counts.next_slice + .counts.not_yet_sliced == .counts.remaining)
' < <(git show "$opening_planning:$transition_rel") >/dev/null ||
  fail "frozen transition counts failed"

inventory=$temp/inventory.json
git show "$opening_planning:$inventory_rel" > "$inventory" ||
  fail "frozen inventory is absent from opening planning snapshot"

actual_census=$(jq -c --argjson kinds "$kinds_json" '
  def parent_state:
    if ((.values | has("actor")) | not) then "absent"
    elif .values.actor == null then "null"
    elif ((.values.actor | type) == "object" and (.values.actor | length) == 0) then "empty_object"
    elif (.values.actor | type) == "object" then "object"
    else "unexpected_type"
    end;
  def child_state:
    if parent_state == "absent" then "not_applicable_parent_absent"
    elif parent_state != "object" then "unexpected_type"
    elif ((.values.actor | has("id")) | not) then "missing_in_object"
    elif .values.actor.id == null then "null"
    elif ((.values.actor.id | type) == "string" and .values.actor.id == "") then "empty_string"
    elif (.values.actor.id | type) == "string" then "string"
    else "unexpected_type"
    end;
  def family_name:
    if (.path | startswith("knowledge/concept-cards/templates/")) then "template"
    elif (.path | startswith("knowledge/concept-cards/examples/")) then "synthetic"
    elif (.path | startswith(".worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/")) then "arc07-pilot"
    else "other"
    end;
  def count_child($state):
    map(select(child_state == $state)) | length;
  . as $doc
  | .records
  | map(select(
      .frontmatter == true
      and (.values? != null)
      and ((.values | type) == "object")
      and (.record_kind as $kind | ($kinds | index($kind)) != null)
    )) as $r
  | {
      parsed_selected_mappings: ($r | length),
      record_kind_counts: ($r | group_by(.record_kind) | map({key: .[0].record_kind, value: length}) | from_entries),
      actor_parent_states: {
        absent: ($r | map(select(parent_state == "absent")) | length),
        null: ($r | map(select(parent_state == "null")) | length),
        empty_object: ($r | map(select(parent_state == "empty_object")) | length),
        object: ($r | map(select(parent_state == "object")) | length),
        unexpected_type: ($r | map(select(parent_state == "unexpected_type")) | length)
      },
      actor_id_states: {
        not_applicable_parent_absent: ($r | count_child("not_applicable_parent_absent")),
        missing_in_object: ($r | count_child("missing_in_object")),
        null: ($r | count_child("null")),
        empty_string: ($r | count_child("empty_string")),
        string: ($r | count_child("string")),
        unexpected_type: ($r | count_child("unexpected_type"))
      },
      family_breakdown: (
        $r
        | group_by(family_name)
        | map({
            key: .[0] | family_name,
            value: {
              records: length,
              parent_absent: (map(select(parent_state == "absent")) | length),
              parent_object_null_id: (map(select(parent_state == "object" and .values.actor.id == null)) | length),
              parent_object_string_id: (map(select(parent_state == "object" and (.values.actor.id | type) == "string" and .values.actor.id != "")) | length)
            }
          })
        | from_entries
      ),
      actor_label_breakdown: (
        ($r | map(select(parent_state == "object" and (.values.actor.id | type) == "string" and .values.actor.id != ""))) as $pop
        | {
            id_labels: ($pop | group_by(.values.actor.id) | map({key: .[0].values.actor.id, value: length}) | from_entries),
            mode_labels: ($pop | group_by(.values.actor.mode) | map({key: .[0].values.actor.mode, value: length}) | from_entries),
            role_labels: ($pop | group_by(.values.actor.role) | map({key: .[0].values.actor.role, value: length}) | from_entries)
          }
      ),
      by_kind: (
        $r
        | group_by(.record_kind)
        | map({
            key: .[0].record_kind,
            value: {
              records: length,
              parent_absent: (map(select(parent_state == "absent")) | length),
              parent_object_null_id: (map(select(parent_state == "object" and .values.actor.id == null)) | length),
              parent_object_string_id: (map(select(parent_state == "object" and (.values.actor.id | type) == "string" and .values.actor.id != "")) | length),
              witnesses: (map(.path) | sort)
            }
          })
        | from_entries
      ),
      legacy_untyped_census: (
        [ $doc.records[] | select(
            .frontmatter == true
            and (.record_kind == null or .record_kind == "untyped")
            and (.values? != null)
            and ((.values | type) == "object")
          ) ] as $legacy
        | {
            parsed_mappings: ($legacy | length),
            actor_parent_states: {
              absent: ($legacy | map(select(parent_state == "absent")) | length),
              null: ($legacy | map(select(parent_state == "null")) | length),
              empty_object: ($legacy | map(select(parent_state == "empty_object")) | length),
              object: ($legacy | map(select(parent_state == "object")) | length),
              unexpected_type: ($legacy | map(select(parent_state == "unexpected_type")) | length)
            },
            actor_id_states: {
              not_applicable_parent_absent: ($legacy | count_child("not_applicable_parent_absent")),
              missing_in_object: ($legacy | count_child("missing_in_object")),
              null: ($legacy | count_child("null")),
              empty_string: ($legacy | count_child("empty_string")),
              string: ($legacy | count_child("string")),
              unexpected_type: ($legacy | count_child("unexpected_type"))
            },
            literal_dotted_actor_id_keys: ($legacy | map(select(.values | has("actor.id"))) | length),
            meaning: "The frozen parsed legacy untyped inventory contains no actor parent or nested actor.id; this bounded absence is not a claim that legacy provenance never existed."
          }
      )
    }
' "$inventory")
yaml_error_paths=$(jq -c '
  [.records[]
   | select((.error? // "") | contains("YAML::XS"))
   | .path]
  | sort
' "$inventory")
no_frontmatter_count=$(jq '[.records[] | select(.error? == "no-opening-frontmatter")] | length' "$inventory")
[[ "$no_frontmatter_count" == "15" ]] ||
  fail "native no-frontmatter distinction changed"
[[ "$(jq 'length' <<< "$yaml_error_paths")" == "3" ]] ||
  fail "native YAML-error cell count changed"
jq -e --argjson yaml_errors "$yaml_error_paths" '
  .native_census.parse_exclusions.count == ($yaml_errors | length)
  and ((.native_census.parse_exclusions.records | sort) == $yaml_errors)
  and (.native_census.parse_exclusions.meaning | contains("not actor absence"))
' "$registry" >/dev/null || fail "authored parse exclusions differ from native YAML-error paths"
wrong_exclusions=$(jq '
  .native_census.parse_exclusions.records[0] = "not-a-real-yaml-error-path"
' "$registry")
if printf '%s\n' "$wrong_exclusions" | jq -e --argjson yaml_errors "$yaml_error_paths" '
  .native_census.parse_exclusions.count == ($yaml_errors | length)
  and ((.native_census.parse_exclusions.records | sort) == $yaml_errors)
' >/dev/null; then
  fail "wrong YAML exclusion mutation was accepted"
else
  wrong_exclusion_status=$?
  [[ "$wrong_exclusion_status" == "1" ]] ||
    fail "wrong YAML exclusion mutation failed with unexpected jq status"
fi
jq -e --argjson actual "$actual_census" '
  (.native_census
   | del(.inventory_evidence_id, .parse_exclusions)
   | .by_kind |= with_entries(
       .value |= ((.witnesses // [.witness]) as $w
         | del(.witness, .witnesses)
         | .witnesses = ($w | sort))
     )
  ) == $actual
' "$registry" >/dev/null || fail "authored native or legacy census differs from native inventory"

check_registry() {
  jq -e --argjson assignment "$assignment_json" '
    .evidence as $e
    | ($e | map(.evidence_id)) as $ids
    | (.memberships) as $m
    | ($m | map([.field_path, .record_kind])) as $pairs
    | ($m | map(.meaning_id)) as $member_meanings
    | ($ids | unique | length) == ($ids | length)
    and ($m | length) == 12
    and (($pairs | unique | sort) == ($assignment | unique | sort))
    and (($member_meanings | unique | sort) == (.meanings | keys | sort))
    and ((([$m[].evidence_ids[]] | unique) - $ids) | length == 0)
    and ((([.meanings[] | .evidence_ids[]] | unique) - $ids) | length == 0)
  ' "$1" >/dev/null
}

check_registry "$registry" || fail "membership and evidence reference predicate failed"
mutated_member=$(jq '.memberships[0].record_kind = "not-a-real-record-kind"' "$registry")
if printf '%s\n' "$mutated_member" | check_registry -; then
  fail "invalid membership mutation was accepted"
fi
mutated_evidence=$(jq '.meanings["actor-memory-admission"].evidence_ids[0] = "dangling-evidence-id"' "$registry")
if printf '%s\n' "$mutated_evidence" | check_registry -; then
  fail "dangling evidence mutation was accepted"
fi

hash_evidence() {
  while IFS= read -r row; do
    [[ -z "$row" ]] && continue
    evidence_id=$(jq -r '.evidence_id' <<< "$row")
    evidence_root=$(jq -r '.root' <<< "$row")
    read_mode=$(jq -r '.read_mode' <<< "$row")
    path=$(jq -r '.path' <<< "$row")
    authority=$(jq -r '.authority_commit' <<< "$row")
    case "$evidence_root:$read_mode" in
      planning:snapshot)
        actual_hash=$(git -C "$root" show "$authority:$path" | shasum -a 256 | awk '{print $1}')
        ;;
      source:snapshot)
        actual_hash=$(git -C "$source" show "$authority:$path" | shasum -a 256 | awk '{print $1}')
        ;;
      planning:live)
        actual_hash=$(shasum -a 256 "$root/$path" | awk '{print $1}')
        ;;
      source:live)
        actual_hash=$(shasum -a 256 "$source/$path" | awk '{print $1}')
        ;;
      *)
        fail "unsupported evidence root/read mode: $evidence_root:$read_mode"
        ;;
    esac
    expected_hash=$(jq -r --arg id "$evidence_id" '.evidence[] | select(.evidence_id == $id) | .sha256' "$registry")
    [[ "$actual_hash" == "$expected_hash" ]] ||
      fail "evidence hash mismatch: $evidence_id"
    if [[ "$evidence_root:$read_mode" == "source:snapshot" ]]; then
      current_hash=$(shasum -a 256 "$source/$path" | awk '{print $1}')
      [[ "$current_hash" == "$expected_hash" ]] ||
        fail "registered source bytes changed: $evidence_id"
    fi
  done < <(jq -c '.evidence[]' "$registry")
}
hash_evidence

support_path=.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/support-emergent-explanation.md
support_actor=$(jq -c --arg path "$support_path" '
  .records[] | select(.path == $path) | .values.actor
' "$inventory")
expected_support_actor='{"id":"codex-cc","mode":"agent-direct","role":"extractor"}'
[[ "$support_actor" == "$expected_support_actor" ]] ||
  fail "populated support actor differs from independently authored expectation"
support_context=$(jq -c --arg path "$support_path" '
  .records[] | select(.path == $path)
  | {subject_ref: .values.subject_ref, source_ref: .values.source_spans[0].source_ref}
' "$inventory")
jq -e '
  (.subject_ref.record_type == "claim")
  and (.subject_ref.id != .source_ref.id)
  and (.source_ref.id == "ccn-book")
' <<< "$support_context" >/dev/null ||
  fail "support subject/source context did not remain distinct"
if jq -e --arg path "$support_path" '
  .records[] | select(.path == $path) | .values.actor.id == "codex-deliberately-wrong"
' "$inventory" >/dev/null; then
  fail "wrong support actor expectation was accepted"
else
  support_wrong_status=$?
  [[ "$support_wrong_status" == "1" ]] || fail "wrong support expectation failed with unexpected jq status"
fi

template_path=knowledge/concept-cards/templates/memory-admission.md
synthetic_path=knowledge/concept-cards/examples/memory-admission.md
template_actor=$(jq -c --arg path "$template_path" '
  .records[] | select(.path == $path) | .values.actor
' "$inventory")
[[ "$template_actor" == '{"id":null,"mode":null,"role":null}' ]] ||
  fail "template actor was not object/null"
synthetic_state=$(jq -r --arg path "$synthetic_path" '
  .records[] | select(.path == $path)
  | if (.values | has("actor")) then
      if .values.actor == null then "null"
      elif (.values.actor | type) == "object" then "object"
      else "unexpected_type"
      end
    else "absent"
    end
' "$inventory")
[[ "$synthetic_state" == absent ]] || fail "synthetic actor parent was not absent"
if jq -e --arg path "$synthetic_path" '
  .records[] | select(.path == $path) | (.values | has("actor") and .actor == null)
' "$inventory" >/dev/null; then
  fail "absence-to-null mutation was accepted"
else
  absence_to_null_status=$?
  [[ "$absence_to_null_status" == "1" ]] ||
    fail "absence-to-null negative control failed with unexpected jq status"
fi

no_match_err=$temp/no-match.err
no_match_output=$(jq -c --arg path .worktrees/planning/no-such-real-inventory-path '
  [.records[] | select(.path == $path)]
' "$inventory" 2>"$no_match_err")
no_match_status=$?
[[ "$no_match_status" == "0" ]] || fail "real inventory no-match did not succeed"
[[ "$no_match_output" == "[]" ]] || fail "real inventory no-match was not an empty result"
[[ ! -s "$no_match_err" ]] || fail "real inventory no-match wrote an error"
missing_inventory=$temp/missing-inventory.json
if jq -c '.records' "$missing_inventory" >/dev/null 2>"$temp/missing.err"; then
  fail "missing inventory unexpectedly succeeded"
else
  missing_status=$?
  [[ "$missing_status" == "2" ]] || fail "missing inventory returned unexpected status"
fi

printf '%s\n' "mode=$mode"
printf '%s\n' "registry=$registry"
printf '%s\n' "source_opening=$opening_source"
printf '%s\n' "source_current=$source_current"
printf '%s\n' "planning_head=$(git -C "$root" rev-parse HEAD)"
printf '%s\n' "native_census=12 selected, legacy_untyped=2054"
printf '%s\n' "yaml_error_count=$(jq 'length' <<< "$yaml_error_paths") no_frontmatter_count=$no_frontmatter_count"
printf '%s\n' "wrong_yaml_exclusion_status=$wrong_exclusion_status"
printf '%s\n' "unrelated_head_fixture=pass"
printf '%s\n' "support_actor_positive=0"
printf '%s\n' "support_actor_wrong_expectation_status=$support_wrong_status"
printf '%s\n' "absence_to_null_negative_control_status=$absence_to_null_status"
printf '%s\n' "no_match_status=$no_match_status output=$no_match_output stderr_bytes=$(wc -c < "$no_match_err" | tr -d ' ')"
printf '%s\n' "missing_input_status=$missing_status stderr_bytes=$(wc -c < "$temp/missing.err" | tr -d ' ')"
printf '%s\n' "mutated_member=reject"
printf '%s\n' "mutated_evidence=reject"
printf '%s\n' "semantic_acceptance=not_claimed"
~~~

The route's pinned values and checks are deliberate:

- source opening/current commits are both reported; the relevant source tree is
  compared against the historical source reference and each registered source
  snapshot is compared by bytes, so unrelated source HEAD advance is tolerated
  while material registered-path drift fails;
- opening planning authority is fixed at the clean post-acknowledgement commit;
  protected plans, ledgers, coverage, inventory, prior Slice13 records and both
  issued prompts must remain byte-stable;
- current coverage is checked for the 555/188/367/12/355 accounting and the
  frozen transition for 555/115/440/35/405;
- the exact assignment is extracted from the opening slice plan, rather than
  copied from an expected object;
- the selected 12-record census and the 2,054-record legacy comparison are
  derived from the pinned native inventory;
- all 42 registered evidence hashes are recomputed according to their declared
  root and read mode;
- expected support and template/absent cases are authored in the route,
  while wrong expectations, invalid memberships, dangling evidence, wrong
  YAML exclusions, a real no-match and a missing input exercise failure
  behavior. The committed wrapper separately rejects a missing recipe file and
  a stale valid recipe endpoint.

## Recorded observations

Precommit and committed replay results are recorded here after execution. The
route must report status 0, reject all mutations and wrong expectations, return
status 0 with [] for the real no-match, and return status 2 for the missing
inventory input. No status-0 route run is a semantic-acceptance decision.

- precommit iteration02: status 0 at planning HEAD
  8e6b67708eeeca391a139bb8d1b710633cfbbeb4; selected census 12 and legacy
  comparison 2054; derived YAML-error count 3 and no-frontmatter count 15;
  unrelated-HEAD fixture passed; positive support actor status 0; wrong
  support expectation status 1; wrong YAML exclusion status 1;
  absence-to-null negative control status 1; real no-match status 0 with []
  and 0 stderr bytes; missing-input status 2 with 145 stderr bytes; invalid
  membership and dangling evidence mutations rejected; semantic acceptance not
  claimed
- committed same-revision preflight: status 0 with CC_COMMIT=15da9e33 and
  REPLAY_COMMIT=15da9e33; registry was loaded from CC_COMMIT and the wrapper
  extracted the literal route from that revision; all structural outcomes
  matched the precommit run. This was a wrapper preflight, not the required
  separate-revision result.
- stale valid recipe rejection: status 1 with CC_COMMIT=15da9e33 and
  REPLAY_COMMIT=8e6b67708eeeca391a139bb8d1b710633cfbbeb4; the older recipe was
  rejected on its opening-to-CC scope predicate.
- missing recipe-file rejection: status 2 with CC_COMMIT=15da9e33 and
  REPLAY_COMMIT=2fa4c2a5273485d5bdf5bfba9a59677df79d14cf; the valid commit
  lacked the recipe path, so the committed wrapper stopped before execution.
- committed separate-revision: pending the follow-up recipe commit; it must
  use CC_COMMIT=15da9e33 and the later metadata-only recipe endpoint, return
  status 0 with the same structural outcomes, and be rerun after that endpoint
  is recorded.
