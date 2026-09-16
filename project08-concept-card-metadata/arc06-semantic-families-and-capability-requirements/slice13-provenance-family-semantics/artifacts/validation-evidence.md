# Slice13 validation and literal replay

Status: CC proposed-done; this file records reproducible structural and native
diagnostic evidence, not independent semantic acceptance. The route below is
the complete validation route. It uses Bash, jq, rg, Git, shasum, cmp, awk and
standard shell tools only; it introduces no helper, parser, extraction,
runtime, schema, package, source or memory work.

## Pinned state and evidence layers

- Source opening commit: `e763c661592ff1097a94bb470db9cf924524579d`, expected
  clean throughout.
- Planning opening commit: `609f2f558b100a06df42e6a8b85ebfe200a27b22`, clean
  before the six-file contribution.
- Frozen inventory SHA-256:
  `afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.
- Current coverage opening/live SHA-256:
  `5d4413abe585274750544784627f65b6f83668596815d55c6a1e9dbcd9339070`.
- Current coverage is checked as a live status input and separately against
  its opening Git snapshot. It is not refreshed in a self-referential loop.
- `semantic-membership.json` contains 40 registered inputs. The literal route
  recomputes every registered hash and checks the declared original/copy
  mappings for the rich and teaching witnesses.
- Expected actor observations are authored before each native read in the
  route. Native JSON is compared with parsed jq value equality, not text or
  object-key order. A wrong expected actor is a comparison failure, not a
  semantic no-match.

## Literal route

Run this block from the source checkout before commit with
`CC_PRECOMMIT=1`, after staging the six files. Run it again against the actual
committed endpoint with `CC_COMMIT=<six-file-commit>`.

~~~bash
set -euo pipefail

source=/Users/oubiwann/lab/billosys/ai-engineering
plan=$source/.worktrees/planning
cd "$source"

project=project08-concept-card-metadata
arc=arc06-semantic-families-and-capability-requirements
slice=$project/$arc/slice13-provenance-family-semantics
membership=$plan/$slice/artifacts/semantic-membership.json
coverage_rel=$project/artifacts/semantic-coverage-current.json
transition_rel=$project/artifacts/semantic-transition-coverage.json
inventory_rel=$project/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
opening_source=e763c661592ff1097a94bb470db9cf924524579d
opening_planning=609f2f558b100a06df42e6a8b85ebfe200a27b22
opening_inventory_sha=afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b
expected_opening_coverage_sha=5d4413abe585274750544784627f65b6f83668596815d55c6a1e9dbcd9339070
cc_commit=${CC_COMMIT:-}
precommit=${CC_PRECOMMIT:-}
tmp=$(mktemp -d /private/tmp/cc-slice13-replay.XXXXXX)
trap 'rm -rf "$tmp"' EXIT

test "$(git -C "$source" rev-parse HEAD)" = "$opening_source"
test -z "$(git -C "$source" status --porcelain)"
test "$(git -C "$plan" rev-parse "$opening_planning^{commit}")" = "$opening_planning"
printf 'source=%s planning_opening=%s\n' "$opening_source" "$opening_planning"
printf 'bash=%s jq=%s rg=%s\n' "$(bash --version|head -1)" "$(jq --version)" "$(rg --version|head -1)"

expected_files=$(printf '%s\n' \
  "$slice/artifacts/semantic-membership.json" \
  "$slice/artifacts/semantic-evidence.md" \
  "$slice/artifacts/validation-evidence.md" \
  "$slice/artifacts/handoff.md" \
  "$slice/ledger.md" \
  "$slice/closing-report.md" | sort)

if [ -n "$precommit" ]; then
  test -z "$cc_commit"
  actual_files=$( { \
    git -C "$plan" diff --name-only "$opening_planning" --; \
    git -C "$plan" diff --cached --name-only "$opening_planning" --; \
    git -C "$plan" ls-files --others --exclude-standard; \
  } | sort -u )
  test "$actual_files" = "$expected_files"
  git -C "$plan" diff --check "$opening_planning" --
  git -C "$plan" diff --cached --check
  printf 'scope=precommit staged-unstaged-new-output-union exact-six-files\n'
else
  cc_commit=${cc_commit:-$(git -C "$plan" rev-parse HEAD)}
  git -C "$plan" cat-file -e "$cc_commit^{commit}"
  actual_files=$(git -C "$plan" diff --name-only "$opening_planning" "$cc_commit" -- | sort)
  test "$actual_files" = "$expected_files"
  git -C "$plan" diff --check "$opening_planning" "$cc_commit"
  printf 'scope=committed endpoint=%s exact-six-files\n' "$cc_commit"
fi

# Every registered input is hashed at its declared root. The membership file
# is the manifest authority for this loop, not a generated success summary.
jq -e '.evidence|length==40' "$membership" >/dev/null
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
printf 'registered-input-hashes=40/40 matched\n'

# Fixed authority versus live status. The current register is read live but
# its opening bytes and opening counts are checked from the pinned snapshot.
opening_coverage_sha=$(git -C "$plan" show "$opening_planning:$coverage_rel" | shasum -a 256 | awk '{print $1}')
live_coverage_sha=$(shasum -a 256 "$plan/$coverage_rel" | awk '{print $1}')
test "$opening_coverage_sha" = "$expected_opening_coverage_sha"
test "$live_coverage_sha" = "$expected_opening_coverage_sha"
printf 'coverage.opening.sha256=%s live.sha256=%s\n' "$opening_coverage_sha" "$live_coverage_sha"

assignment='[["actor","claim"],["actor","competency-question"],["actor","concept-card"],["actor","extraction-run"],["actor.id","claim"],["actor.id","competency-question"],["actor.id","concept-card"],["actor.id","extraction-run"]]'
jq -e --argjson a "$assignment" '
  .counts.full==555 and .counts.accepted==180 and .counts.remaining==375 and
  .counts.next_slice==8 and .counts.not_yet_sliced==367 and
  .next_slice_pairs==$a and
  (.remaining_pairs|length)==375 and (.accepted_pairs|length)==180 and
  ((.accepted_pairs + .remaining_pairs)|unique|length)==555 and
  (.remaining_pairs as $r | .accepted_pairs as $q |
    all($a[]; . as $p | any($r[]; .==$p) and all($q[]; .!=$p)))
' "$plan/$coverage_rel" >/dev/null
jq -e '
  .counts.full==555 and .counts.accepted==115 and .counts.remaining==440 and
  .counts.next_slice==35 and .counts.not_yet_sliced==405 and
  (.accepted_pairs|length)==115 and (.remaining_pairs|length)==440 and
  ((.accepted_pairs + .remaining_pairs)|unique|length)==555
' "$plan/$transition_rel" >/dev/null
printf 'coverage=180 accepted / 375 remaining / 8 assigned / 367 outside; transition=115/440 preserved\n'

# Frozen native census: selected kinds, parent state, child state and no
# unexpected values. The three malformed rich records are inherited
# exclusions, not silently counted as absent actor mappings.
inventory=$plan/$inventory_rel
test "$(shasum -a 256 "$inventory" | awk '{print $1}')" = "$opening_inventory_sha"
jq -e '
  [.records[] | select(.record_kind=="claim" or .record_kind=="competency-question" or .record_kind=="concept-card" or .record_kind=="extraction-run")] as $r |
  ($r|length)==37 and
  ([$r[]|select(.record_kind=="claim")]|length)==1 and
  ([$r[]|select(.record_kind=="competency-question")]|length)==2 and
  ([$r[]|select(.record_kind=="concept-card")]|length)==31 and
  ([$r[]|select(.record_kind=="extraction-run")]|length)==3 and
  ([$r[]|select((.values|has("actor"))|not)]|length)==12 and
  ([$r[]|select((.values.actor|type)=="object" and .values.actor.id==null)]|length)==4 and
  ([$r[]|select((.values.actor|type)=="object" and (.values.actor.id|type)=="string")]|length)==21 and
  ([$r[]|select((.values|has("actor")) and .values.actor==null)]|length)==0 and
  ([$r[]|select((.values.actor|type)=="object" and ((.values.actor|length)==0))]|length)==0 and
  ([$r[]|select((.values.actor|type)=="object" and ((.values.actor|has("id"))|not))]|length)==0 and
  ([$r[]|select((.values.actor|type)!="object" and ((.values|has("actor"))))]|length)==0
' "$inventory" >/dev/null
printf 'native-census=37 parsed mappings; parent absent=12 object-null=4 object-string=21; malformed-rich-exclusions=3 inherited\n'

# Original/copy mappings are checked with both the registered manifests and
# direct byte comparison. Copy equality is preservation evidence only.
rich_original=$source/workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
rich_copy=$plan/$project/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
teaching_original=$source/workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
teaching_copy=$plan/$project/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
cmp "$rich_original" "$rich_copy"
cmp "$teaching_original" "$teaching_copy"
printf 'original-copy=rich and teaching byte-equal; copy not treated as independent read\n'

# Diagnostic 1: native generated actor versus an independently authored
# expected object, then a deliberately wrong expected identity.
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

# Diagnostic 2: template object/null versus an actual absent parent. These
# are distinct native states; the child is null in one and not applicable in
# the other. A missing inventory is a real jq input error.
template_path=knowledge/concept-cards/templates/concept-card.md
expanded_path=.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards/cc-complementary-learning-systems.md
template_actor=$(jq -c --arg p "$template_path" '.records[]|select(.path==$p)|.values.actor' "$inventory")
expected_template_actor='{"id":null,"mode":null,"role":null}'
jq -n -e --argjson expected "$expected_template_actor" --argjson observed "$template_actor" '$expected==$observed' >/dev/null
jq -e --arg p "$expanded_path" '.records[]|select(.path==$p)|(.values|has("actor")|not)' "$inventory" >/dev/null
test -z "$(rg -n '^actor:' "$source/$expanded_path" || true)"
printf 'diagnostic2.template=object/null; diagnostic2.expanded=parent_absent/child_not_applicable\n'

wrong_path=$(jq -c --arg p 'no-such-actor-record.md' '[.records[]|select(.path==$p)]' "$inventory")
test "$wrong_path" = '[]'
printf 'lookup.successful_no_match.status=0\n'
set +e
jq -c --arg p 'no-such-actor-record.md' '[.records[]|select(.path==$p)]' "$tmp/no-such-inventory.json" > "$tmp/missing.stdout" 2> "$tmp/missing.stderr"
missing_status=$?
set -e
test "$missing_status" = 2
test ! -s "$tmp/missing.stdout"
test -s "$tmp/missing.stderr"
printf 'lookup.missing-input.status=%s classification=tool_error stderr_nonempty=true\n' "$missing_status"

# Fixed history versus current-state preservation. No source or protected
# planning file may move between opening and the CC endpoint.
if [ -z "$precommit" ]; then
  protected=(
    "$project/project-plan.md"
    "$project/ledger.md"
    "$arc/arc-plan.md"
    "$arc/ledger.md"
    "$coverage_rel"
    "$transition_rel"
    "$project/$arc/slice01-relationship-semantics-and-traversal/cdc-verification.md"
    "$project/$arc/slice02-competency-questions-and-answerability/cdc-verification.md"
    "$project/$arc/slice03-provenance-and-shared-reference-contracts/cdc-verification.md"
  )
  for p in "${protected[@]}"; do git -C "$plan" diff --exit-code "$opening_planning" "$cc_commit" -- "$p"; done
  test -z "$(git -C "$plan" status --porcelain)"
  printf 'history=opening-to-CC six-file diff only; protected planning history unchanged; planning endpoint clean\n'
else
  printf 'history=precommit scope checked; committed endpoint remains to be checked with CC_COMMIT\n'
fi
test -z "$(git -C "$source" status --porcelain)"
printf 'source-status=clean; json=structural-comparisons-pass; semantic-acceptance=not-claimed\n'
~~~

## Expected and actual result classes

The positive generated-card diagnostic is an exact structural match for the
independently authored actor object `{id: codex, mode: agent-direct, role:
extractor}`. The wrong `id` is expected to exit 1 as a comparison failure.
The template null diagnostic and the expanded-card absent-parent diagnostic
are intentionally different states. A wrong record path is a successful
bounded no-match with status 0; a missing inventory input is a jq tool error
with status 2 and non-empty stderr. No result is relabelled as semantic
absence, authority, verification, answerability or admission.

The precommit invocation proves the fixed six-file contribution against the
opening state. The committed invocation must be run against the actual CC
commit and proves the same endpoint, hashes, native census, controls,
original/copy mappings and protected-history preservation. It does not close
the ledger: CDC must independently rerun this route and inspect the artifacts.
