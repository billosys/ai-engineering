# Slice17 validation evidence: literal native replay

Status: CC proposed-done; this is structural evidence for CRC review, not
semantic acceptance, CDC composition or Operator acceptance.

## Intake and route contract

The route pins source `ce3f77103eff5e07b3533a03c65f158684fc1039`, issued
planning `c40e52fc1318e6213c60d5e0371fd01aa3208f1d`, preserved pre-opening
planning `c6d445b8cf693e0c03a70a79d5b45c07e3337dcb`, and Set A authority
`dee3052c88e0fd9361e74200fd1eea26ade76435`. The frozen inventory is read from
the issued planning commit and its SHA-256 is checked. The route reads every
registered evidence row through its declared authority, validates all 39
registered ranges, and rejects wrong roots, authorities, hashes, descriptors,
nulls, reversed spans and out-of-bounds spans.

The route has precommit mode for the working registry and committed mode for a
registry loaded from `CC_COMMIT`. A preserved outer wrapper below loads the
recipe bytes from a separately named `REPLAY_COMMIT`, extracts exactly the
literal route, syntax-checks it and executes it with the declared endpoints.
The Iteration01 route checks exactly the three permitted repair paths and protects the
prompt, plans, coverage, transition, directive, source authority, Slice16
records and other historical inputs. It preserves operation stdout, status
and stderr presence for the two successful no-matches and deliberate tool
error.

## Iteration01 intake and contract readback

This corrective assignment was loaded from planning `a0f51639` with source
`ce3f77103eff5e07b3533a03c65f158684fc1039`; the preserved semantic baseline
was read from registry endpoint `97a75091b6d124955762f12c72865f72d5aedd53`.
The complete required-full extents were loaded before editing: this iteration
prompt 200 lines, `crc-verification.md` 57, `slice-plan.md` 145, `ledger.md`
16, initial prompt 400, current validation evidence 376, closing report 70,
semantic membership 305, semantic evidence 241 and handoff 77. Required
sections were loaded from project plan, arc plan and directive02; source
guide07 named sections, testing-discipline sections and row-closure guidance
were read at source `ce3f7710`. A combined required-read output was truncated;
the omitted registry and plan material was recovered with bounded contiguous
reads. No context compaction occurred.

The contract readback is: R1 requires four additional candidates to pass
through the existing `check_matrix`/`check_registry`/native-input predicates,
with independent expected values unchanged: template null-to-absent,
accepted/outside membership addition, declared other-target path substitution,
and a missing inventory input or invalid authority. R2 requires the outer
wrapper, not the inner route, to load recipe bytes from `REPLAY_COMMIT`, reject
missing/multiple/malformed route blocks, run `bash -n`, and preserve the
actual execution status; opening and foreign endpoints must therefore be
tested at wrapper extraction. R3 is only the contradictory count wording.
Only this validation file, `ledger.md` and `closing-report.md` may change;
the six-file semantic baseline, exact 18/39 evidence, 220/335/18/317
accounting, no-pair-acceptance boundary and all future owners remain intact.

## Literal route

~~~bash
set -euo pipefail

fail() { printf '%s\n' "FAIL: $*" >&2; exit 1; }

root=$(git rev-parse --show-toplevel)
source=$(cd "$root/../.." && pwd)
slice_rel=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice17-run-preparation-method-and-reference-provenance
membership_rel=$slice_rel/artifacts/semantic-membership.json
coverage_rel=project08-concept-card-metadata/artifacts/semantic-coverage-current.json
transition_rel=project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
inventory_rel=project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
opening_source=ce3f77103eff5e07b3533a03c65f158684fc1039
opening_planning=c40e52fc1318e6213c60d5e0371fd01aa3208f1d
iteration_opening=a0f516398254a1357a86e67ab3378299120650c1
preopening_planning=c6d445b8cf693e0c03a70a79d5b45c07e3337dcb
set_authority=dee3052c88e0fd9361e74200fd1eea26ade76435
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
  [[ "${CC_PRECOMMIT:-}" == 1 ]] || fail "set CC_PRECOMMIT=1 or provide CC_COMMIT"
  registry=$root/$membership_rel
  [[ -s "$registry" ]] || fail "working-tree registry is absent or empty"
fi

[[ "$root" == /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning ]] || fail "route must run from canonical planning checkout"
[[ "$(git rev-parse "$opening_planning")" == "$opening_planning" ]] || fail "issued planning authority is unavailable"
[[ "$(git rev-parse "$iteration_opening")" == "$iteration_opening" ]] || fail "iteration contribution baseline is unavailable"
[[ "$(git -C "$source" rev-parse "$opening_source")" == "$opening_source" ]] || fail "source authority is unavailable"
source_current=$(git -C "$source" rev-parse HEAD)
[[ -z "$(git -C "$source" status --porcelain --untracked-files=all)" ]] || fail "source checkout is not clean"
git diff --check || fail "planning working tree has whitespace errors"
git diff --cached --check || fail "planning index has whitespace errors"
git -C "$source" diff --exit-code "$opening_source" "$source_current" -- knowledge/concept-cards knowledge/document-extraction || fail "relevant source tree differs from opening source"
jq empty "$registry" >/dev/null || fail "registry is not valid JSON"

allowed_paths="$slice_rel/artifacts/validation-evidence.md
$slice_rel/ledger.md
$slice_rel/closing-report.md"
is_allowed() { grep -Fqx "$1" <<< "$allowed_paths"; }
if [[ "$mode" == precommit ]]; then
  changed_paths=$( { git diff --name-only; git diff --cached --name-only; git ls-files --others --exclude-standard; } | sort -u )
  [[ -n "$changed_paths" ]] || fail "precommit union is empty"
  while IFS= read -r path; do [[ -z "$path" ]] && continue; is_allowed "$path" || fail "out-of-scope precommit path: $path"; done <<< "$changed_paths"
else
  [[ -z "$(git status --porcelain --untracked-files=all)" ]] || fail "planning checkout is not clean for committed replay"
  committed_paths=$(git diff --name-only "$iteration_opening" "$CC_COMMIT" | sort -u)
  expected_paths=$(printf '%s\n' "$allowed_paths" | sort)
  [[ "$committed_paths" == "$expected_paths" ]] || fail "committed contribution is not exactly the three permitted paths"
  git diff --check "$iteration_opening" "$CC_COMMIT" || fail "committed contribution has whitespace errors"
fi

protected_paths="project08-concept-card-metadata/AGENTS.md
project08-concept-card-metadata/project-plan.md
project08-concept-card-metadata/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/arc-plan.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/cdc-directive02.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/crc-escalation02.md
$slice_rel/cc-prompt.md
$slice_rel/slice-plan.md
$coverage_rel
$transition_rel
$inventory_rel
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/cc-prompt.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/cc-prompt-iteration01.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/crc-verification.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/artifacts/semantic-membership.json
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/artifacts/semantic-evidence.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/artifacts/validation-evidence.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/artifacts/handoff.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/closing-report.md"
if [[ "$mode" == committed ]]; then
  while IFS= read -r path; do [[ -z "$path" ]] && continue; git diff --exit-code "$iteration_opening" -- "$path" >/dev/null || fail "protected planning path changed: $path"; done <<< "$protected_paths"
fi

assignment_json=$(git show "$opening_planning:$slice_rel/slice-plan.md" | awk '/^~~~json$/{n++;if(n==1){p=1;next}} p&&/^~~~$/{exit} p')
set_a_json=$(git show "$set_authority:project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/crc-escalation02.md" | awk '/^~~~json$/{p=1;next} p&&/^~~~$/{p=0;next} p' | jq -s '.[0]')
coverage=$(git show "$opening_planning:$coverage_rel") || fail "current coverage is unavailable"
transition=$(git show "$opening_planning:$transition_rel") || fail "transition coverage is unavailable"
inventory=$temp/inventory.json
git show "$opening_planning:$inventory_rel" > "$inventory" || fail "inventory is unavailable"
jq -n -e --argjson a "$set_a_json" --argjson c "$coverage" '
  ($a|length)==18 and ($a|unique|length)==18 and
  ($a-$c.remaining_pairs|length)==0 and ($a-$c.accepted_pairs|length)==18 and
  $c.counts=={full:555,accepted:220,remaining:335,next_slice:18,not_yet_sliced:317} and
  $c.next_slice=="arc06-semantic-families-and-capability-requirements/slice17-run-preparation-method-and-reference-provenance" and
  ($c.next_slice_pairs|sort)==($a|sort)' >/dev/null || fail "exact Set A or current coverage failed"
jq -e '.counts=={full:555,accepted:115,remaining:440,next_slice:35,not_yet_sliced:405} and (.accepted_pairs|length)==115 and (.remaining_pairs|length)==440' <<< "$transition" >/dev/null || fail "frozen transition failed"

expected_population='[
  {"record":"parallel","frontmatter":true,"error":null,"keys":["extraction_confidence","id","input_source_ref","memory_admission_refs","prepared_source_ref","preservation_decision_refs","reconciliation_result_refs","record_type","revision","surface_class","synthetic","validation_result_refs","verification_result_refs","worker_scope"]},
  {"record":"template","frontmatter":true,"error":null,"keys":["actor","actual_coverage","agent_scope","extraction_confidence","finished_at","id","intended_outputs","intended_scope","memory_admission_refs","method_ref","old_card_inputs","operation","output_refs","parallel_worker_count","prepared_source_refs","preservation_refs","prior_run_refs","prompt_ref","reconciliation_refs","record_type","revision","settings","source_snapshot_refs","started_at","validation_refs","verification_refs","worker_outputs"]},
  {"record":"trace","frontmatter":true,"error":null,"keys":["extraction_confidence","id","input_source_ref","memory_admission_refs","output_refs","prepared_source_ref","preservation_decision_refs","reconciliation_result_refs","record_type","revision","surface_class","synthetic","validation_result_refs","verification_result_refs","worker_scope"]}
]'
actual_population=$(jq -c '
  def record_name:
    if (.path|endswith("knowledge/concept-cards/templates/extraction-run.md")) then "template"
    elif (.path|contains("extraction-run-trace.md")) then "trace" else "parallel" end;
  [.records[]|select(.record_kind=="extraction-run")|{record:record_name,frontmatter,error,keys:(.values|keys)}]|sort_by(.record)' "$inventory")
jq -n -e --argjson actual "$actual_population" --argjson expected "$expected_population" '$actual==$expected' >/dev/null || fail "native extraction-run population differs"

expected_matrix=$(cat <<'JSON'
[
  {"record":"parallel","fields":{"finished_at":{"state":"absent","value":null},"input_source_ref":{"state":"populated-mapping","value":{"id":"de-synthetic-method-note-003","revision":1}},"input_source_ref.id":{"state":"populated-string","value":"de-synthetic-method-note-003"},"input_source_ref.path":{"state":"child-absent","value":null},"input_source_ref.revision":{"state":"populated-number","value":1},"method_ref":{"state":"absent","value":null},"old_card_inputs":{"state":"absent","value":null},"operation":{"state":"absent","value":null},"prepared_source_ref":{"state":"populated-mapping","value":{"id":"de-prepared-synthetic-method-note-003","revision":1}},"prepared_source_ref.id":{"state":"populated-string","value":"de-prepared-synthetic-method-note-003"},"prepared_source_ref.path":{"state":"child-absent","value":null},"prepared_source_ref.revision":{"state":"populated-number","value":1},"prepared_source_refs":{"state":"absent","value":null},"prior_run_refs":{"state":"absent","value":null},"prompt_ref":{"state":"absent","value":null},"settings":{"state":"absent","value":null},"source_snapshot_refs":{"state":"absent","value":null},"started_at":{"state":"absent","value":null}}},
  {"record":"template","fields":{"finished_at":{"state":"null","value":null},"input_source_ref":{"state":"absent","value":null},"input_source_ref.id":{"state":"parent-absent","value":null},"input_source_ref.path":{"state":"parent-absent","value":null},"input_source_ref.revision":{"state":"parent-absent","value":null},"method_ref":{"state":"null","value":null},"old_card_inputs":{"state":"empty-list","value":[]},"operation":{"state":"null","value":null},"prepared_source_ref":{"state":"absent","value":null},"prepared_source_ref.id":{"state":"parent-absent","value":null},"prepared_source_ref.path":{"state":"parent-absent","value":null},"prepared_source_ref.revision":{"state":"parent-absent","value":null},"prepared_source_refs":{"state":"empty-list","value":[]},"prior_run_refs":{"state":"empty-list","value":[]},"prompt_ref":{"state":"null","value":null},"settings":{"state":"empty-mapping","value":{}},"source_snapshot_refs":{"state":"empty-list","value":[]},"started_at":{"state":"null","value":null}}},
  {"record":"trace","fields":{"finished_at":{"state":"absent","value":null},"input_source_ref":{"state":"populated-mapping","value":{"id":"de-synthetic-method-note-002","path":"document-extraction/raw/synthetic-method-note-002.txt","revision":1}},"input_source_ref.id":{"state":"populated-string","value":"de-synthetic-method-note-002"},"input_source_ref.path":{"state":"populated-string","value":"document-extraction/raw/synthetic-method-note-002.txt"},"input_source_ref.revision":{"state":"populated-number","value":1},"method_ref":{"state":"absent","value":null},"old_card_inputs":{"state":"absent","value":null},"operation":{"state":"absent","value":null},"prepared_source_ref":{"state":"populated-mapping","value":{"id":"de-prepared-synthetic-method-note-002","path":"document-extraction/prepared/synthetic-method-note-002.md","revision":1}},"prepared_source_ref.id":{"state":"populated-string","value":"de-prepared-synthetic-method-note-002"},"prepared_source_ref.path":{"state":"populated-string","value":"document-extraction/prepared/synthetic-method-note-002.md"},"prepared_source_ref.revision":{"state":"populated-number","value":1},"prepared_source_refs":{"state":"absent","value":null},"prior_run_refs":{"state":"absent","value":null},"prompt_ref":{"state":"absent","value":null},"settings":{"state":"absent","value":null},"source_snapshot_refs":{"state":"absent","value":null},"started_at":{"state":"absent","value":null}}}
]
JSON
)
actual_matrix=$(jq -c --argjson paths "$assignment_json" '
  def leaf_state($x):
    if $x==null then {state:"null",value:null}
    elif ($x|type)=="array" and ($x|length)==0 then {state:"empty-list",value:$x}
    elif ($x|type)=="object" and ($x|length)==0 then {state:"empty-mapping",value:$x}
    elif ($x|type)=="array" then {state:"populated-list",value:$x}
    elif ($x|type)=="object" then {state:"populated-mapping",value:$x}
    else {state:("populated-"+($x|type)),value:$x} end;
  def field_state($v;$path):
    ($path|split(".")) as $p |
    if ($p|length)==1 then
      if ($v|has($p[0])|not) then {state:"absent",value:null} else leaf_state($v[$p[0]]) end
    elif ($v|has($p[0])|not) then {state:"parent-absent",value:null}
    elif ($v[$p[0]]|type)!="object" then {state:("parent-unexpected-"+($v[$p[0]]|type)),value:$v[$p[0]]}
    elif ($v[$p[0]]|has($p[1])|not) then {state:"child-absent",value:null}
    else leaf_state($v[$p[0]][$p[1]]) end;
  def record_name:
    if (.path|endswith("knowledge/concept-cards/templates/extraction-run.md")) then "template"
    elif (.path|contains("extraction-run-trace.md")) then "trace" else "parallel" end;
  [.records[]|select(.record_kind=="extraction-run")|. as $r|{record:($r|record_name),fields:(reduce ($paths[]) as $pair ({}; .[$pair[0]]=field_state($r.values;$pair[0])))}]|sort_by(.record)' "$inventory")
check_matrix() { jq -n -e --argjson actual "$1" --argjson expected "$expected_matrix" '$actual==$expected' >/dev/null; }
check_matrix "$actual_matrix" || fail "native state/value matrix differs"

yaml_errors=$(jq -c '[.records[]|select((.error? // "")|contains("YAML::XS"))|.path]|sort' "$inventory")
no_frontmatter=$(jq -c '[.records[]|select(.error?=="no-opening-frontmatter")|.path]|sort' "$inventory")
expected_yaml='["workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-memory-forms.md","workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-priming-forms.md","workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-recognition-dual-process.md"]'
expected_no_frontmatter='[".worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/README.md",".worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards/README.md","knowledge/concept-cards/references/README.md","knowledge/concept-cards/references/operator-review-gates.md","knowledge/concept-cards/references/record-field-groups.md","knowledge/concept-cards/references/semantic-audit-boundaries.md","knowledge/concept-cards/references/structural-validation-candidates.md","knowledge/concept-cards/references/vocabulary.md","workbench/compcogneuro-rich-rerun-2026-09-12/README.md","workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/INDEX.md","workbench/compcogneuro-rich-rerun-2026-09-12/comparison/evaluation-rubric.md","workbench/compcogneuro-rich-rerun-2026-09-12/comparison/subset-comparison.md","workbench/compcogneuro-teaching-rerun-2026-09-12/README.md","workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/INDEX.md","workbench/compcogneuro-teaching-rerun-2026-09-12/comparison/teaching-profile-comparison.md"]'
[[ "$yaml_errors" == "$expected_yaml" ]] || fail "YAML exclusion set differs"
[[ "$no_frontmatter" == "$expected_no_frontmatter" ]] || fail "no-frontmatter set differs"

historical=$(jq -c --argjson roots '["finished_at","input_source_ref","method_ref","old_card_inputs","operation","prepared_source_ref","prepared_source_refs","prior_run_refs","prompt_ref","settings","source_snapshot_refs","started_at"]' '
  [.records[]|select(.frontmatter==true and (.values?|type)=="object")|select((.path|contains("complete-musician") or contains("knowledge/erlang/")))] as $r |
  {parsed_records:($r|length),root_presence:(reduce $roots[] as $k ({}; .[$k]=([$r[]|select(.values|has($k))]|length)))}' "$inventory")
expected_historical='{"parsed_records":2054,"root_presence":{"finished_at":0,"input_source_ref":0,"method_ref":0,"old_card_inputs":0,"operation":0,"prepared_source_ref":0,"prepared_source_refs":0,"prior_run_refs":0,"prompt_ref":0,"settings":0,"source_snapshot_refs":0,"started_at":0}}'
jq -n -e --argjson actual "$historical" --argjson expected "$expected_historical" '$actual==$expected' >/dev/null || fail "historical absence comparison differs"

check_registry() {
  jq -e --argjson assignment "$assignment_json" '
    (.scope.assignment==$assignment) and
    (.scope.counts=={full:555,accepted:220,remaining:335,assigned:18,outside:317}) and
    (.memberships|length)==18 and
    ((.memberships|map([.field_path,.record_kind])|sort)==($assignment|sort)) and
    ((.memberships|map(.meaning_id)|unique|length)==18) and
    ([(.memberships[])|select((has("field_path") and has("record_kind") and has("meaning_id") and has("effective_meaning") and has("applicability") and has("observed_states") and has("evidence_ids") and has("exceptions") and (.consequences|type)=="object" and ((.consequences|keys|sort)==["extractor","migration","query","reader"]) and has("unresolved_questions") and has("disposition"))|not)]|length)==0 and
    ((([.memberships[].evidence_ids[]]|unique)-(.evidence_registry|map(.evidence_id)))|length)==0
  ' <<< "$1" >/dev/null
}
valid_registry=$(jq -c . "$registry") || fail "registry clone failed"
check_registry "$valid_registry" || fail "registry boundary or required fields failed"

resolve_snapshot() {
  local row=$1 root path authority read_mode
  root=$(jq -r '.root' <<< "$row"); path=$(jq -r '.path' <<< "$row"); authority=$(jq -r '.authority_commit' <<< "$row"); read_mode=$(jq -r '.read_mode' <<< "$row")
  [[ "$read_mode" == snapshot ]] || return 1
  case "$root" in
    planning)
      [[ "$authority" == "$opening_planning" || "$authority" == "$preopening_planning" || "$authority" == "$set_authority" ]] || return 1
      git show "$authority:$path" ;;
    source)
      [[ "$authority" == "$opening_source" ]] || return 1
      git -C "$source" show "$authority:$path" ;;
    *) return 1 ;;
  esac
}

check_evidence() {
  local candidate=$1 row evidence_id root path authority source_range snapshot total range_text start end count=0 actual_hash expected_hash
  while IFS= read -r row; do
    evidence_id=$(jq -r '.evidence_id' <<< "$row"); root=$(jq -r '.root' <<< "$row"); path=$(jq -r '.path' <<< "$row"); authority=$(jq -r '.authority_commit' <<< "$row"); source_range=$(jq -r '.source_range' <<< "$row")
    [[ -n "$evidence_id" && "$root" != null && -n "$path" && "$authority" != null && "$source_range" != null ]] || return 1
    [[ "$evidence_id" != "null" ]] || return 1
    jq -e 'has("evidence_id") and has("root") and has("path") and has("read_mode") and has("authority_commit") and has("sha256") and has("role") and has("member_scope") and has("source_range") and has("interpretation") and has("limit") and (.sha256|test("^[0-9a-f]{64}$"))' <<< "$row" >/dev/null || return 1
    snapshot="$temp/evidence-$count"
    resolve_snapshot "$row" > "$snapshot" || return 1
    actual_hash=$(shasum -a 256 "$snapshot" | awk '{print $1}')
    expected_hash=$(jq -r --arg id "$evidence_id" '.evidence_registry[]|select(.evidence_id==$id)|.sha256' <<< "$candidate")
    [[ "$actual_hash" == "$expected_hash" ]] || return 1
    case "$evidence_id" in
      current-coverage)
        [[ "$source_range" == "JSON document" ]] || return 1; jq -e '.counts.full==555 and .counts.accepted==220 and .counts.remaining==335' "$snapshot" >/dev/null || return 1 ;;
      transition)
        [[ "$source_range" == "JSON document" ]] || return 1; jq -e '.counts.full==555 and .counts.accepted==115 and .counts.remaining==440' "$snapshot" >/dev/null || return 1 ;;
      inventory)
        [[ "$source_range" == "JSON document; selected values and YAML-error records" ]] || return 1; jq -e '.records|length==2124' "$snapshot" >/dev/null || return 1 ;;
      *)
        [[ "$source_range" =~ ^lines[[:space:]][0-9]+-[0-9]+$ ]] || return 1
        range_text=${source_range#lines }; start=${range_text%-*}; end=${range_text##*-}
        [[ "$start" -ge 1 && "$start" -le "$end" ]] || return 1
        total=$(wc -l < "$snapshot" | awk '{print $1}')
        [[ "$end" -le "$total" ]] || return 1 ;;
    esac
    count=$((count+1))
  done < <(jq -c '.evidence_registry[]' <<< "$candidate")
  [[ "$count" == 39 ]]
}
check_evidence "$valid_registry" || fail "registered evidence hashes or ranges failed"

wrong_authority=$(jq -c '.evidence_registry[0].authority_commit="ce3f77103eff5e07b3533a03c65f158684fc1039"' <<< "$valid_registry")
if check_evidence "$wrong_authority"; then fail "wrong authority was accepted"; else wrong_authority_status=$?; [[ "$wrong_authority_status" == 1 ]] || fail "wrong authority status unexpected"; fi
wrong_hash=$(jq -c '.evidence_registry[0].sha256="0000000000000000000000000000000000000000000000000000000000000000"' <<< "$valid_registry")
if check_evidence "$wrong_hash"; then fail "wrong hash was accepted"; else wrong_hash_status=$?; [[ "$wrong_hash_status" == 1 ]] || fail "wrong hash status unexpected"; fi
unknown_range=$(jq -c '.evidence_registry[0].source_range="not-a-range"' <<< "$valid_registry")
if check_evidence "$unknown_range"; then fail "unknown range was accepted"; else unknown_range_status=$?; [[ "$unknown_range_status" == 1 ]] || fail "unknown range status unexpected"; fi
null_range=$(jq -c '.evidence_registry[0].source_range=null' <<< "$valid_registry")
if check_evidence "$null_range"; then fail "null range was accepted"; else null_range_status=$?; [[ "$null_range_status" == 1 ]] || fail "null range status unexpected"; fi
misplaced_range=$(jq -c '(.evidence_registry[]|select(.evidence_id=="current-coverage")|.source_range)="lines 1-1"' <<< "$valid_registry")
if check_evidence "$misplaced_range"; then fail "misplaced range was accepted"; else misplaced_range_status=$?; [[ "$misplaced_range_status" == 1 ]] || fail "misplaced range status unexpected"; fi
reversed_range=$(jq -c '.evidence_registry[0].source_range="lines 2-1"' <<< "$valid_registry")
if check_evidence "$reversed_range"; then fail "reversed range was accepted"; else reversed_range_status=$?; [[ "$reversed_range_status" == 1 ]] || fail "reversed range status unexpected"; fi

check_target() { jq -n -e --argjson actual "$1" --argjson expected "$2" '$actual==$expected' >/dev/null; }
lookup_target() {
  local path=$1 out=$temp/target-out err=$temp/target-err status
  set +e; git -C "$source" ls-tree -r --name-only "$opening_source" -- "$path" > "$out" 2> "$err"; status=$?; set -e
  jq -n -c --arg path "$path" --rawfile stdout "$out" --rawfile stderr "$err" --argjson status "$status" '{path:$path,stdout:($stdout|rtrimstr("\n")),status:$status,stderr_nonempty:(($stderr|length)>0),classification:(if $status==0 and ($stdout|length)==0 then "successful_no_match" else "tool_error" end)}'
}
lookup_missing_target() {
  local path=$1 out=$temp/missing-target-out err=$temp/missing-target-err status
  set +e; git -C "$source" show "$opening_source:$path" > "$out" 2> "$err"; status=$?; set -e
  jq -n -c --arg path "$path" --rawfile stdout "$out" --rawfile stderr "$err" --argjson status "$status" '{path:$path,stdout:($stdout|rtrimstr("\n")),status:$status,stderr_nonempty:(($stderr|length)>0),classification:(if $status==0 then "match" else "tool_error" end)}'
}
target1=$(lookup_target document-extraction/raw/synthetic-method-note-002.txt)
target2=$(lookup_target document-extraction/prepared/synthetic-method-note-002.md)
missing_target=$(lookup_missing_target document-extraction/no-such-input.md)
expected_target1=$(jq -n --arg p document-extraction/raw/synthetic-method-note-002.txt '{path:$p,stdout:"",status:0,stderr_nonempty:false,classification:"successful_no_match"}')
expected_target2=$(jq -n --arg p document-extraction/prepared/synthetic-method-note-002.md '{path:$p,stdout:"",status:0,stderr_nonempty:false,classification:"successful_no_match"}')
check_target "$target1" "$expected_target1" || fail "first declared target result differs"
check_target "$target2" "$expected_target2" || fail "second declared target result differs"
[[ "$(jq -r '.status' <<< "$missing_target")" != 0 && "$(jq -r '.stderr_nonempty' <<< "$missing_target")" == true ]] || fail "missing target did not fail as a tool error"

wrong_field=$(jq -c '(.memberships[]|select(.field_path=="prepared_source_ref")|.field_path)="prepared_source_refs"' <<< "$valid_registry")
if check_registry "$wrong_field"; then fail "singular/plural field mutation was accepted"; else wrong_field_status=$?; [[ "$wrong_field_status" == 1 ]] || fail "wrong field status unexpected"; fi
prepared_list_absent=$(jq -c 'map(if .record=="template" then .fields.prepared_source_refs={state:"absent",value:null} else . end)' <<< "$actual_matrix")
if check_matrix "$prepared_list_absent"; then fail "empty-list to absent mutation was accepted"; else empty_absent_status=$?; [[ "$empty_absent_status" == 1 ]] || fail "empty/absent status unexpected"; fi
path_added=$(jq -c 'map(if .record=="parallel" then .fields.input_source_ref.path={state:"populated-string",value:"document-extraction/raw/synthetic-method-note-003.txt"} else . end)' <<< "$actual_matrix")
if check_matrix "$path_added"; then fail "path-added mutation was accepted"; else path_added_status=$?; [[ "$path_added_status" == 1 ]] || fail "path-added status unexpected"; fi
wrong_id=$(jq -c 'map(if .record=="trace" then .fields.input_source_ref.id.value="wrong-id" else . end)' <<< "$actual_matrix")
if check_matrix "$wrong_id"; then fail "wrong id mutation was accepted"; else wrong_id_status=$?; [[ "$wrong_id_status" == 1 ]] || fail "wrong id status unexpected"; fi
wrong_revision=$(jq -c 'map(if .record=="trace" then .fields.input_source_ref.revision.value=99 else . end)' <<< "$actual_matrix")
if check_matrix "$wrong_revision"; then fail "wrong revision mutation was accepted"; else wrong_revision_status=$?; [[ "$wrong_revision_status" == 1 ]] || fail "wrong revision status unexpected"; fi
wrong_path=$(jq -c 'map(if .record=="trace" then .fields.input_source_ref.path.value="document-extraction/raw/other.txt" else . end)' <<< "$actual_matrix")
if check_matrix "$wrong_path"; then fail "wrong path mutation was accepted"; else wrong_path_status=$?; [[ "$wrong_path_status" == 1 ]] || fail "wrong path status unexpected"; fi
wrong_target_expected=$(jq -n '{path:"document-extraction/raw/synthetic-method-note-002.txt",stdout:"wrong",status:0,stderr_nonempty:false,classification:"successful_no_match"}')
if check_target "$target1" "$wrong_target_expected"; then fail "wrong target expectation was accepted"; else wrong_target_status=$?; [[ "$wrong_target_status" == 1 ]] || fail "wrong target status unexpected"; fi

null_to_absent=$(jq -c 'map(if .record=="template" then .fields.finished_at={state:"absent",value:null} else . end)' <<< "$actual_matrix")
if check_matrix "$null_to_absent"; then fail "null-to-absent mutation was accepted"; else null_to_absent_status=$?; [[ "$null_to_absent_status" == 1 ]] || fail "null-to-absent status unexpected"; fi
accepted_outside_add=$(jq -c '.memberships += [(.memberships[0] | .field_path="actor" | .record_kind="claim" | .meaning_id="slice17-invalid-accepted-outside")]' <<< "$valid_registry")
if check_registry "$accepted_outside_add"; then fail "accepted/outside membership addition was accepted"; else accepted_outside_status=$?; [[ "$accepted_outside_status" == 1 ]] || fail "accepted/outside status unexpected"; fi
other_target_path=$(jq -c 'map(if .record=="trace" then .fields.input_source_ref.path.value="document-extraction/prepared/synthetic-method-note-002.md" else . end)' <<< "$actual_matrix")
if check_matrix "$other_target_path"; then fail "other-target path mutation was accepted"; else other_target_path_status=$?; [[ "$other_target_path_status" == 1 ]] || fail "other-target path status unexpected"; fi

lookup_missing_inventory() {
  local out=$temp/missing-inventory-out err=$temp/missing-inventory-err status
  set +e; git show "$opening_planning:${inventory_rel}.missing" > "$out" 2> "$err"; status=$?; set -e
  jq -n -c --arg path "${inventory_rel}.missing" --rawfile stdout "$out" --rawfile stderr "$err" --argjson status "$status" '{path:$path,stdout_bytes:($stdout|length),status:$status,stderr_nonempty:(($stderr|length)>0),classification:(if $status==0 then "match" else "tool_error" end)}'
}
missing_inventory=$(lookup_missing_inventory)
missing_inventory_status=$(jq -r '.status' <<< "$missing_inventory")
[[ "$missing_inventory_status" != 0 && "$(jq -r '.stderr_nonempty' <<< "$missing_inventory")" == true ]] || fail "missing inventory input did not fail as a tool error"

printf '%s\n' "mode=$mode" "native_population=$actual_population" "matrix=$actual_matrix" "yaml_error_count=$(jq length <<< "$yaml_errors")" "no_frontmatter_count=$(jq length <<< "$no_frontmatter")" "historical=$historical" "target1=$target1" "target2=$target2" "missing_target=$missing_target" "missing_inventory=$missing_inventory" "wrong_authority_status=$wrong_authority_status" "wrong_hash_status=$wrong_hash_status" "unknown_range_status=$unknown_range_status" "null_range_status=$null_range_status" "misplaced_range_status=$misplaced_range_status" "reversed_range_status=$reversed_range_status" "wrong_field_status=$wrong_field_status" "empty_absent_status=$empty_absent_status" "path_added_status=$path_added_status" "wrong_id_status=$wrong_id_status" "wrong_revision_status=$wrong_revision_status" "wrong_path_status=$wrong_path_status" "wrong_target_status=$wrong_target_status" "null_to_absent_status=$null_to_absent_status" "accepted_outside_status=$accepted_outside_status" "other_target_path_status=$other_target_path_status" "missing_inventory_status=$missing_inventory_status"
~~~

## Committed endpoint wrapper

The following wrapper is the exact shell used for committed replay. Its route
extraction is bounded to the `## Literal route` section, so this wrapper does
not count itself as another literal route. Extraction failures return status 2;
an extracted route's own status is returned unchanged.

~~~bash
set -euo pipefail

validation_rel=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice17-run-preparation-method-and-reference-provenance/artifacts/validation-evidence.md

run_endpoint() {
  local cc=$1 recipe=$2 doc script section starts closes
  doc=$(mktemp)
  script=$(mktemp)
  trap 'rm -f "$doc" "$script"' RETURN
  git cat-file -e "$cc^{commit}" || return 2
  git cat-file -e "$recipe^{commit}" || return 2
  git show "$recipe:$validation_rel" > "$doc" 2>/dev/null || return 2
  section=$(awk '/^## Literal route$/{p=1;next} p&&/^## Committed endpoint wrapper$/{exit} p' "$doc") || return 2
  starts=$(printf '%s\n' "$section" | grep -c '^~~~bash$' || true)
  closes=$(printf '%s\n' "$section" | grep -c '^~~~$' || true)
  [[ "$starts" == 1 && "$closes" == 1 ]] || return 2
  printf '%s\n' "$section" | awk '/^~~~bash$/{p=1;next} p&&/^~~~$/{found=1;exit} p{print} END{if (!found) exit 2}' > "$script" || return 2
  [[ -s "$script" ]] || return 2
  bash -n "$script" || return 2
  CC_COMMIT="$cc" REPLAY_COMMIT="$recipe" bash "$script"
}

[[ -n "${CC_COMMIT:-}" && -n "${REPLAY_COMMIT:-}" ]] || exit 2
run_endpoint "$CC_COMMIT" "$REPLAY_COMMIT"
~~~

## Required control and endpoint observations

The route must be run with `CC_PRECOMMIT=1` after the six output files are
present and with a committed wrapper that extracts this block from a separate
`REPLAY_COMMIT`. The recorded result below is filled after the scoped commit.
The required mutation statuses are status 1 for wrong field, empty-list to
absent, added path, wrong id/revision/path, wrong authority/hash/range, wrong
target expectation, null-to-absent, accepted/outside membership addition and
other-target path. The two declared paths must be status 0 with empty stdout
and stderr; the deliberate missing target and missing inventory input must be
nonzero with stderr.

The route's structural comparisons do not establish source support, semantic
verification, a resolved synthetic target, schema conformance, memory
admission, extraction completion or Operator acceptance.

~~~

## Recorded observations

The route records exact population, state matrix, availability exclusions,
historical comparison, target lookup stdout/status/stderr, evidence authority
checks, native diagnostic mutations and endpoint replay results below after the
six-file contribution is committed.

### Precommit result

The literal route was extracted from this file and run from the canonical
planning checkout root with `CC_PRECOMMIT=1`; it exited 0. It printed three
parsed records (trace, parallel recipe and template), the full eighteen-field
matrix for each, `yaml_error_count=3`, `no_frontmatter_count=15`, and the
2,054-record historical census with zero root presence for all twelve
comparison paths. The two declared target lookups both returned status 0,
empty stdout and `stderr_nonempty=false`, classified as
`successful_no_match`. The deliberate missing input returned status 128 with
`stderr_nonempty=true`, classified as `tool_error`.

The negative controls all exited with the expected status 1:
wrong-authority, wrong-hash, unknown-range, null-range, misplaced-range,
reversed-range, singular/plural field mutation, empty-list-to-absent,
path-added, wrong-id, wrong-revision, wrong-path, wrong-target expectation,
null-to-absent, accepted/outside membership addition and other-target path.
The missing inventory input returned a nonzero Git error with stderr and is
recorded separately from the missing synthetic target.

The native availability census is exact: the three YAML-error paths are the
three compcogneuro candidate-card files for memory/priming/recognition and the
fifteen no-opening-frontmatter paths are listed in `semantic-evidence.md`.
The native record projections are the trace's populated singular input and
prepared mappings, the parallel recipe's populated ID/revision-only mappings,
and the template's null/empty/absent distinctions; no projection is treated
as global requiredness or a completed run.

### Endpoint and failure record

The Iteration01 CC endpoint is
`e123b60dd846f2dfaf655642c0198f6895d8d675`; its wrapper loaded the registry
from that commit, extracted one route from the same recipe endpoint, ran
`bash -n`, and exited 0 after the route printed the positive and control
results above. The distinct recipe endpoint is recorded after the final
documentation-only commit. The wrapper probes against opening planning
`c40e52fc1318e6213c60d5e0371fd01aa3208f1d`, foreign source
`ce3f77103eff5e07b3533a03c65f158684fc1039`, and the absent all-zero commit ID
each failed during recipe extraction with status 2.

### Exploratory and unrun checks

Two initial historical `jq` query attempts failed with syntax errors (exit 2)
before the corrected query passed. The first combined required-read output was
truncated; the required files were reread through contiguous bounded ranges.
The first route attempt used `.error?//""` and failed with a jq syntax error
(exit 2); spacing it as `.error? // ""` corrected the route. Evidence-range
validation then exposed a registered replay-contract range of `1-118` against
the actual 93-line snapshot; the registry was corrected to `lines 1-93`.
The first route invocation from the slice subdirectory failed its intended
root-relative scope check; rerunning from the canonical planning root passed.
The first wrapper extraction counted both literal Bash blocks and failed closed
with status 2; a committed replay attempted while the planning checkout was
dirty also failed closed before route execution. The route was then corrected
to stop extraction at the committed-wrapper section, and the contribution
baseline was corrected from the prior six-file endpoint to the current CRC
review commit `a0f516398254a1357a86e67ab3378299120650c1`.

No CRC or CDC verification, Operator acceptance, source/schema/runtime/parser
change, package/install check, extraction execution, memory admission, UAT,
coverage acceptance, or model/effort measurement was run or authorized by
this slice. These are explicit open gates, not failed semantic checks.

### Iteration01 correction observations

The corrected precommit route exited 0. Positive structural results remain
unchanged: exact Set A and 220/335/18/317 accounting, 3 x 18 native matrix,
3 YAML-error records, 15 no-frontmatter records, 2,054 historical records
with zero selected roots, two status-0 successful no-matches, and the status-128
missing synthetic-target tool error. Existing authority/hash/range,
singular/plural, empty/absent, path, identity, revision and target controls
continued to return status 1.

The four new production-predicate controls returned status 1:
`null_to_absent_status=1`, `accepted_outside_status=1`,
`other_target_path_status=1` and `missing_inventory_status=128`. The missing
inventory probe used `git show "$opening_planning:${inventory_rel}.missing"`,
captured zero stdout, nonempty stderr and status 128, and remained distinct
from the declared-target no-match and missing synthetic-target probes.
The corrected availability wording now says three YAML-error files and keeps
the exact three paths separate from the fifteen no-frontmatter records.

The inner literal route and the preserved outer wrapper passed `bash -n` before
staging. An initial committed-wrapper attempt failed closed with status 2
because its extraction boundary counted both literal Bash blocks; the wrapper
was corrected to stop at its own section header. Committed wrapper
extraction/execution statuses, including the valid separate recipe, opening
planning, foreign source and absent commit endpoints, are recorded after the
scoped correction commit below.
