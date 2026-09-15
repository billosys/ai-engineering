# Slice01 Validation Evidence

From source cwd with Bash/jq:

```bash
set -euo pipefail
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
jq -e '(.memberships|length)==35 and ([.memberships[]|[.field_path,.record_kind]|join("\u0000")]|unique|length)==35' "$s/artifacts/semantic-membership.json"
jq -e '(.cases|length)==4 and all(.cases[];has("input") and has("path") and has("operation") and has("adapter") and has("expected") and has("observed") and has("limit"))' "$s/artifacts/query-cases.json"
jq empty "$s/artifacts/semantic-membership.json"; jq empty "$s/artifacts/query-cases.json"; git -C .worktrees/planning diff --check
```

The checks are structural only: 35 unique members, four diagnostic cases, valid
JSON and no whitespace errors. Scope is 115 accepted / 35 assigned / 405
outside; CDC decides acceptance.

The following replay adds plan-derived membership, frozen-transition inclusion,
registered-hash, and preservation checks. Run it from the source checkout; it
uses Bash, jq 1.6, shasum and Git 2.39.5.

```bash
set -euo pipefail
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
t=.worktrees/planning/project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
expected=$(awk -F'`' '/^\| `/{print $2 "|" $4}' "$s/slice-plan.md" | sort -u)
actual=$(jq -r '.memberships[] | .field_path + "|" + .record_kind' "$s/artifacts/semantic-membership.json" | sort -u)
test "$(printf '%s\n' "$expected" | sed '/^$/d' | wc -l | tr -d ' ')" = 35
test "$expected" = "$actual"
jq -e --argjson actual "$(jq '[.memberships[] | [.field_path,.record_kind]]' "$s/artifacts/semantic-membership.json")" '
  . as $transition |
  ($transition.accepted_pairs | length) == 115 and
  ($transition.remaining_pairs | length) == 440 and
  ([ $actual[] as $pair | select(any($transition.remaining_pairs[]; . == $pair)) ] | length) == ($actual | length) and
  ([ $actual[] as $pair | select(any($transition.accepted_pairs[]; . == $pair)) ] | length) == 0
' "$t"
test "$(jq '.remaining_pairs | length' "$t")" = 440
test $((440 - 35)) = 405
while IFS=$'\t' read -r path digest; do
  test "$(shasum -a 256 "$path" | awk '{print $1}')" = "$digest"
done < <(jq -r '.evidence[] | [.path,.sha256] | @tsv' "$s/artifacts/semantic-membership.json")
jq -e '(.cases|length)==4 and all(.cases[]; has("input") and has("path") and has("operation") and has("adapter") and has("expected") and has("observed") and has("limit"))' "$s/artifacts/query-cases.json"
git -C .worktrees/planning diff --exit-code 355d037f -- project08-concept-card-metadata/arc01-metadata-research-and-requirements
git -C .worktrees/planning diff --check
```

The census is the frozen frontmatter inventory registered in
`semantic-membership.json`: it separates the legacy untyped lists, the
relationship-edge template/example roots, and concept-card reference variants.
The template is deliberately null/unassessed; the sole populated edge is
synthetic; all target truth and unresolved-anchor claims remain bounded.

## Current Replay (Slice12-Repaired Route: R5/R6)

Executed from the source checkout for Slice12 after the Iteration 05 review.
Actual opening state: source `e763c661592ff1097a94bb470db9cf924524579d`,
planning `f3cadf33`; both worktrees were clean at inspection. Model/settings,
effort and compaction were not changed by this task and are unknown from
repository state. The route uses the frozen parsed inventory for structured
values, direct `shasum`/`cmp` for the teaching original/copy, and one
fail-closed lookup function for match/no-match/search-error states. It does
not extend `awk`/`grep` into a YAML parser or add a helper/parser.

The route below emits and checks every legacy census value and every card and
edge state, exact CDC-attributed projections and search controls before
replaying all four cases. Expected case objects remain
independently authored in `query-cases.json`; native objects are derived from
unchanged registered inputs before comparison.

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
t=.worktrees/planning/project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
music=/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician
teaching=workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-memory-forms.md
teaching_copy=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-memory-forms.md

expected=$(awk -F'`' '/^\| `/{print $2 "|" $4}' "$s/slice-plan.md" | sort -u)
actual=$(jq -r '.memberships[] | .field_path + "|" + .record_kind' "$s/artifacts/semantic-membership.json" | sort -u)
test "$(printf '%s\n' "$expected" | sed '/^$/d' | wc -l | tr -d ' ')" = 35
test "$expected" = "$actual"
jq -e --argjson actual "$(jq '[.memberships[] | [.field_path,.record_kind]]' "$s/artifacts/semantic-membership.json")" '
  . as $transition |
  ($transition.accepted_pairs | length) == 115 and
  ($transition.remaining_pairs | length) == 440 and
  ([ $actual[] as $pair | select(any($transition.remaining_pairs[]; . == $pair)) ] | length) == ($actual | length) and
  ([ $actual[] as $pair | select(any($transition.accepted_pairs[]; . == $pair)) ] | length) == 0
' "$t"
test "$(jq '.remaining_pairs | length' "$t")" = 440
test $((440 - 35)) = 405
jq -e '. as $r | all($r.memberships[]; .meaning_id as $m | $r.meanings | has($m)) and all(($r.meanings[].evidence_ids[], $r.memberships[].evidence_ids[], $r.baseline_mappings[].evidence_ids[]); . as $id | $r.evidence | has($id)) and (.baseline_mappings|length)==1' "$s/artifacts/semantic-membership.json"
test "$(jq '.evidence | length' "$s/artifacts/semantic-membership.json")" = 27
while IFS=$'\t' read -r path digest; do
  test "$(shasum -a 256 "$path" | awk '{print $1}')" = "$digest"
done < <(jq -r '.evidence[] | [.path,.sha256] | @tsv' "$s/artifacts/semantic-membership.json")
cmp -s "$teaching" "$teaching_copy"
test "$(shasum -a 256 "$teaching" | awk '{print $1}')" = 451a52574cce00df9a80bbc908e12ff7c0eb246b2c634cc93d7ad3cdae3d1ac9
test "$(shasum -a 256 "$teaching_copy" | awk '{print $1}')" = 451a52574cce00df9a80bbc908e12ff7c0eb246b2c634cc93d7ad3cdae3d1ac9
! rg -q '^relationship_refs:' "$teaching"
! rg -q '^relationship_edge_refs:' "$teaching"
rg -q '^## Relationships And Competency Questions$' "$teaching"
rg -q 'Contains or routes to: episodic memory, semantic memory, recognition, priming\.' "$teaching"
rg -q 'Related: complementary learning systems\.' "$teaching"
jq -e --arg p knowledge/erlang/concept-cards/erlang-otp-action/data-type-sizes.md '.records[]|select(.path==$p)|.values.prerequisites==null' "$i"
rg -q '^# Prerequisites$' knowledge/erlang/concept-cards/erlang-otp-action/data-type-sizes.md
rg -q "Erlang data types.*card quantifies the memory cost" knowledge/erlang/concept-cards/erlang-otp-action/data-type-sizes.md

def_stats='def stats($rows;$field): {present:([$rows[]|select(.values|has($field))]|length),absent:([$rows[]|select(.values|has($field)|not)]|length),null:([$rows[]|select(.values|has($field))|select(.values[$field]==null)]|length),empty:([$rows[]|select(.values[$field]|type=="array" and length==0)]|length),populated:([$rows[]|select(.values[$field]|type=="array" and length>0)]|length),items:([$rows[]|.values[$field][]?]|length),distinct:([$rows[]|.values[$field][]?]|unique|length),itemtypes:([$rows[]|.values[$field][]?|type]|unique)};'
legacy_census=$(jq -c "$def_stats
  [.records[]|select(.values|type==\"object\")|select((.record_kind//\"untyped\")==\"untyped\")|.+{family:(if (.path|contains(\"complete-musician\")) then \"music\" else \"erlang\" end)}]
  |group_by(.family)|map(. as \$rows | {family:\$rows[0].family,records:(\$rows|length),fields:([\"prerequisites\",\"extends\",\"related\",\"contrasts_with\"]|map({field:.,stats:stats(\$rows;.)}))})" "$i")
printf '%s\n' "$legacy_census"
jq -e "$def_stats
  [.records[]|select(.values|type==\"object\")|select((.record_kind//\"untyped\")==\"untyped\")|.+{family:(if (.path|contains(\"complete-musician\")) then \"music\" else \"erlang\" end)}]
  |group_by(.family)|map(. as \$rows | {family:\$rows[0].family,records:(\$rows|length),fields:([\"prerequisites\",\"extends\",\"related\",\"contrasts_with\"]|map({field:.,stats:stats(\$rows;.)}))})
  == [{family:\"erlang\",records:1664,fields:[{field:\"prerequisites\",stats:{present:1664,absent:0,null:1,empty:306,populated:1357,items:2282,distinct:586,itemtypes:[\"string\"]}},{field:\"extends\",stats:{present:1598,absent:66,null:0,empty:1289,populated:309,items:314,distinct:162,itemtypes:[\"string\"]}},{field:\"related\",stats:{present:1664,absent:0,null:1,empty:21,populated:1642,items:4065,distinct:1239,itemtypes:[\"string\"]}},{field:\"contrasts_with\",stats:{present:1664,absent:0,null:3,empty:1133,populated:528,items:643,distinct:385,itemtypes:[\"string\"]}}]},{family:\"music\",records:390,fields:[{field:\"prerequisites\",stats:{present:390,absent:0,null:0,empty:5,populated:385,items:620,distinct:183,itemtypes:[\"string\"]}},{field:\"extends\",stats:{present:390,absent:0,null:0,empty:180,populated:210,items:210,distinct:88,itemtypes:[\"string\"]}},{field:\"related\",stats:{present:390,absent:0,null:0,empty:16,populated:374,items:752,distinct:331,itemtypes:[\"string\"]}},{field:\"contrasts_with\",stats:{present:390,absent:0,null:0,empty:262,populated:128,items:148,distinct:107,itemtypes:[\"string\"]}}]}]" "$i"
```

The first block checks the teaching original/copy mapping and body reading,
the null-field contrast, exact membership/accounting and all 27 registered
hashes. Its census emits and checks every legacy field's presence, absence,
null, empty, populated, item-total, distinct-value and item-type value.

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json

card_census=$(jq -c '
  [.records[]|select(.record_kind=="concept-card")|.path as $p
   |{family:(if $p=="knowledge/concept-cards/templates/concept-card.md" then "template"
             elif ($p|startswith("knowledge/concept-cards/examples/")) then "synthetic-examples"
             elif ($p|contains("slice02-pilot-markdown-preparation-and-card-extraction")) then "arc07-pilot"
             elif ($p|contains("slice04-expanded-corpus-card-generation")) then "arc07-expanded"
             elif ($p|contains("compcogneuro-rich-rerun")) then "rich-rerun"
             elif ($p|contains("compcogneuro-teaching-rerun")) then "teaching-rerun"
             else "other" end),
     edge_refs:(if (.values|has("relationship_edge_refs")) then (if .values.relationship_edge_refs==[] then "empty" else (.values.relationship_edge_refs|type) end) else "absent" end),
     relationship_refs:(if (.values|has("relationship_refs")) then (if .values.relationship_refs==[] then "empty" elif (.values.relationship_refs|length)>0 then "populated" else (.values.relationship_refs|type) end) else "absent" end)}]
  |group_by(.family)|map({family:.[0].family,parsed_cards:length,edge_refs:(group_by(.edge_refs)|map({state:.[0].edge_refs,count:length})),relationship_refs:(group_by(.relationship_refs)|map({state:.[0].relationship_refs,count:length}))})
' "$i")
printf '%s\n' "$card_census"
test "$card_census" = '[{"family":"arc07-expanded","parsed_cards":6,"edge_refs":[{"state":"absent","count":6}],"relationship_refs":[{"state":"absent","count":6}]},{"family":"arc07-pilot","parsed_cards":4,"edge_refs":[{"state":"absent","count":4}],"relationship_refs":[{"state":"empty","count":4}]},{"family":"rich-rerun","parsed_cards":7,"edge_refs":[{"state":"absent","count":7}],"relationship_refs":[{"state":"absent","count":6},{"state":"empty","count":1}]},{"family":"synthetic-examples","parsed_cards":3,"edge_refs":[{"state":"absent","count":2},{"state":"empty","count":1}],"relationship_refs":[{"state":"absent","count":2},{"state":"populated","count":1}]},{"family":"teaching-rerun","parsed_cards":10,"edge_refs":[{"state":"absent","count":10}],"relationship_refs":[{"state":"absent","count":10}]},{"family":"template","parsed_cards":1,"edge_refs":[{"state":"absent","count":1}],"relationship_refs":[{"state":"empty","count":1}]}]'
jq -e '[.records[]|select(.error != null)|select(.path|test("compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-.*\\.md$"))]|length==3' "$i"
```

The card census checks the six selected context families, the 31 parsed-card
denominator, all root state combinations and the three malformed-rich card
exclusions. README/INDEX/comparison files without card frontmatter are not
counted as malformed cards.

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
jq -e '
  def state($object;$key):
    if ($object|has($key)|not) then "absent"
    elif $object[$key] == null then "null"
    elif (($object[$key]|type)=="array" and ($object[$key]|length)==0) then "empty"
    elif (($object[$key]|type)=="object") then "mapping"
    else ($object[$key]|type) end;
  (.records[]|select(.path=="knowledge/concept-cards/templates/relationship-edge.md")|.values) as $t
  |(.records[]|select(.path=="knowledge/concept-cards/examples/relationship-edge.md")|.values) as $e
  |{template:{directed:state($t;"directed"),direction:state($t;"direction"),endpoint_roles:state($t;"endpoint_roles"),endpoint_roles_from_role:state($t.endpoint_roles;"from_role"),endpoint_roles_to_role:state($t.endpoint_roles;"to_role"),from_ref:state($t;"from_ref"),to_ref:state($t;"to_ref"),relationship_type:state($t;"relationship_type"),relation_type:state($t;"relation_type"),meaning:state($t;"meaning"),inverse_reading:state($t;"inverse_reading"),symmetry:state($t;"symmetry"),graph_closure_state:state($t;"graph_closure_state"),source_support_refs:state($t;"source_support_refs"),source_support_items:($t.source_support_refs|length)},example:{directed:state($e;"directed"),direction:state($e;"direction"),endpoint_roles:state($e;"endpoint_roles"),from_ref:state($e;"from_ref"),from_ref_id:state($e.from_ref;"id"),from_ref_revision:state($e.from_ref;"revision"),to_ref:state($e;"to_ref"),to_ref_id:state($e.to_ref;"id"),to_ref_revision:state($e.to_ref;"revision"),relationship_type:state($e;"relationship_type"),relation_type:state($e;"relation_type"),meaning:state($e;"meaning"),inverse_reading:state($e;"inverse_reading"),symmetry:state($e;"symmetry"),graph_closure_state:state($e;"graph_closure_state"),source_support_refs:state($e;"source_support_refs"),source_support_items:($e.source_support_refs|length),source_support_id:state($e.source_support_refs[0];"id"),source_support_revision:state($e.source_support_refs[0];"revision")}}
  |.template=={directed:"absent",direction:"null",endpoint_roles:"mapping",endpoint_roles_from_role:"null",endpoint_roles_to_role:"null",from_ref:"null",to_ref:"null",relationship_type:"null",relation_type:"absent",meaning:"null",inverse_reading:"null",symmetry:"null",graph_closure_state:"string",source_support_refs:"empty",source_support_items:0}
   and .example=={directed:"boolean",direction:"absent",endpoint_roles:"absent",from_ref:"mapping",from_ref_id:"string",from_ref_revision:"number",to_ref:"mapping",to_ref_id:"string",to_ref_revision:"number",relationship_type:"absent",relation_type:"string",meaning:"absent",inverse_reading:"absent",symmetry:"absent",graph_closure_state:"absent",source_support_refs:"array",source_support_items:1,source_support_id:"string",source_support_revision:"number"}
' "$i"
```

This edge-state check covers every selected root/nested component in the
template/example table, including empty versus populated support collections
and the actual item types for endpoint and support references.

### Current Route: CDC-Supplementary Exact Projections

The following two projections are retained from the Iteration 05 independent
review as CDC-authored supplementary checks. They verify exact frozen
reference/edge values; they are attributed review evidence, not newly
discovered CC semantics.

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
jq -e '
[.records[]|select(.record_kind=="concept-card")|.values.relationship_refs[]?]
== [{id:"edge-evidence-map-related-to-claim",path:"records/edge-evidence-map-related-to-claim.md",revision:1}]
' "$i"
jq -e '
["directed","direction","endpoint_roles","from_ref","to_ref","relationship_type","relation_type","meaning","inverse_reading","symmetry","graph_closure_state","source_support_refs"] as $keys
|[.records[]|select(.record_kind=="relationship-edge")
 |{path,values:(.values|with_entries(select(.key as $k|$keys|index($k)!=null)))}]
|sort_by(.path)
|.==[
 {path:"knowledge/concept-cards/examples/relationship-edge.md",
  values:{directed:true,from_ref:{id:"cc-prepared-source-provenance",revision:1},to_ref:{id:"cc-claim-support-is-assertion-specific",revision:1},relation_type:"precedes",source_support_refs:[{id:"support-synthetic-edge-001",revision:1}]}},
 {path:"knowledge/concept-cards/templates/relationship-edge.md",
  values:{direction:null,endpoint_roles:{from_role:null,to_role:null},from_ref:null,to_ref:null,relationship_type:null,meaning:null,inverse_reading:null,symmetry:null,graph_closure_state:"unassessed",source_support_refs:[]}}
]
' "$i"
test ! -e records/edge-evidence-map-related-to-claim.md
```

## Current Route: Native Cases And Preservation

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
music=/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician

prereq=$(jq -r --arg path "$music/accent-types.md" '.records[]|select(.path==$path)|.values.prerequisites[0]' "$i")
prereq_found=false
if test -f "$music/$prereq.md"; then prereq_found=true; fi
prereq_native=$(jq -n --arg from "$prereq" --argjson found "$prereq_found" '{from:$from,to:"accent-types",target_found:$found}')

ext=$(jq -r --arg path "$music/accented-incomplete-neighbor.md" '.records[]|select(.path==$path)|.values.extends[0]' "$i")
ext_found=false
if test -f "$music/$ext.md"; then ext_found=true; fi
extension_native=$(jq -n --arg from accented-incomplete-neighbor --arg to "$ext" --arg inverse "$ext is extended by accented-incomplete-neighbor" --argjson found "$ext_found" '{from:$from,to:$to,inverse:$inverse,target_found:$found}')

a=accented-incomplete-neighbor
b=appoggiatura
a_lists_b=$(jq -r --arg path "$music/$a.md" --arg target "$b" '.records[]|select(.path==$path)|(.values.related|index($target) != null)' "$i")
b_lists_a=$(jq -r --arg path "$music/$b.md" --arg target "$a" '.records[]|select(.path==$path)|(.values.related|index($target) != null)' "$i")
symmetry_native=$(jq -n --arg a "$a" --arg b "$b" --argjson ab "$a_lists_b" --argjson ba "$b_lists_a" '{a:$a,b:$b,a_lists_b:$ab,b_lists_a:$ba,reciprocal:($ab and $ba),lookup:"symmetric"}')

edge_path=knowledge/concept-cards/examples/relationship-edge.md
from_target=knowledge/concept-cards/examples/minimal-card.md
to_target=knowledge/concept-cards/examples/claim-backed-card.md
from_id=$(jq -r --arg path "$edge_path" '.records[]|select(.path==$path)|.values.from_ref.id' "$i")
from_revision=$(jq -r --arg path "$edge_path" '.records[]|select(.path==$path)|.values.from_ref.revision' "$i")
to_id=$(jq -r --arg path "$edge_path" '.records[]|select(.path==$path)|.values.to_ref.id' "$i")
to_revision=$(jq -r --arg path "$edge_path" '.records[]|select(.path==$path)|.values.to_ref.revision' "$i")
support_id=$(jq -r --arg path "$edge_path" '.records[]|select(.path==$path)|.values.source_support_refs[0].id' "$i")
support_revision=$(jq -r --arg path "$edge_path" '.records[]|select(.path==$path)|.values.source_support_refs[0].revision' "$i")
from_declared_id=$(jq -r --arg path "$from_target" '.records[]|select(.path==$path)|.values.id' "$i")
from_declared_revision=$(jq -r --arg path "$from_target" '.records[]|select(.path==$path)|.values.revision' "$i")
to_declared_id=$(jq -r --arg path "$to_target" '.records[]|select(.path==$path)|.values.id' "$i")
to_declared_revision=$(jq -r --arg path "$to_target" '.records[]|select(.path==$path)|.values.revision' "$i")
lookup_fixture=$(mktemp -d)
lookup_error_log="$lookup_fixture/error.log"
trap 'rm -rf "$lookup_fixture"' EXIT
printf '%s\n' 'id: support-match' > "$lookup_fixture/match.md"

lookup_support() {
  local search_root=$1
  local search_id=$2
  local matches
  local search_status
  if matches=$(rg -l -e "^id: ${search_id}$" -e "path: .*${search_id}" -- "$search_root"); then
    if test -n "$matches"; then
      printf '%s\n' match
      return 0
    fi
    printf '%s\n' no-match
    return 1
  else
    search_status=$?
    if test "$search_status" = 1; then
      printf '%s\n' no-match
      return 1
    fi
    printf 'search-error:%s\n' "$search_status" >&2
    return "$search_status"
  fi
}

resolve_support() {
  local lookup_result
  local lookup_status
  if lookup_result=$(lookup_support "$1" "$2"); then
    printf '%s\n' "$lookup_result"
    return 0
  else
    lookup_status=$?
    if test "$lookup_status" = 1; then
      printf '%s\n' "$lookup_result"
      return 0
    fi
    printf 'support-search-error:%s\n' "$lookup_status" >&2
    return "$lookup_status"
  fi
}

if match_result=$(resolve_support "$lookup_fixture" support-match); then match_status=0; else match_status=$?; fi
if no_match_result=$(resolve_support "$lookup_fixture" support-missing); then no_match_status=0; else no_match_status=$?; fi
rg() { printf '%s\n' 'CDC injected search failure' >&2; return 2; }
if error_result=$(resolve_support "$lookup_fixture" support-match 2>"$lookup_error_log"); then error_status=0; else error_status=$?; fi
unset -f rg
printf 'lookup-control match status=%s result=%s\n' "$match_status" "$match_result"
printf 'lookup-control no-match status=%s result=%s\n' "$no_match_status" "$no_match_result"
printf 'lookup-control error status=%s result=%s\n' "$error_status" "${error_result:-<empty>}"
test "$match_status" = 0
test "$match_result" = match
test "$no_match_status" = 0
test "$no_match_result" = no-match
test "$error_status" = 2
rg -q '^CDC injected search failure$' "$lookup_error_log"

if native_support_result=$(resolve_support knowledge/concept-cards/examples "$support_id"); then
  test "$native_support_result" = no-match
  support_found=false
  support_path=unavailable
else
  native_search_status=$?
  printf 'native support search failed with status %s\n' "$native_search_status" >&2
  exit "$native_search_status"
fi
endpoint_native=$(jq -n --arg fi "$from_id" --argjson fr "$from_revision" --arg fdi "$from_declared_id" --argjson fdr "$from_declared_revision" --arg ti "$to_id" --argjson tr "$to_revision" --arg tdi "$to_declared_id" --argjson tdr "$to_declared_revision" --arg si "$support_id" --argjson sr "$support_revision" --arg sp "$support_path" --argjson sf "$support_found" '{from:{requested:{id:$fi,revision:$fr},declared:{id:$fdi,revision:$fdr},identity_match:($fi==$fdi),revision_match:($fr==$fdr)},to:{requested:{id:$ti,revision:$tr},declared:{id:$tdi,revision:$tdr},identity_match:($ti==$tdi),revision_match:($tr==$tdr)},support:{requested:{id:$si,revision:$sr},declared_path:$sp,declared_id_found:$sf}}')

jq -e --argjson native "$prereq_native" '.cases[]|select(.id=="prerequisite")|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"
jq -e --argjson native "$extension_native" '.cases[]|select(.id=="extension")|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"
jq -e --argjson native "$symmetry_native" '.cases[]|select(.id=="symmetry")|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"
jq -e --argjson native "$endpoint_native" '.cases[]|select(.id=="edge-endpoints")|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"
! jq -e --argjson native "$symmetry_native" '.cases[]|select(.id=="symmetry")|.expected.a="CDC-deliberately-wrong-endpoint"|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"
! jq -e --argjson native "$endpoint_native" '.cases[]|select(.id=="edge-endpoints")|.expected.to.revision_match=false|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"

jq empty "$s/artifacts/semantic-membership.json"
jq empty "$s/artifacts/query-cases.json"
git -C .worktrees/planning diff --check
git -C .worktrees/planning diff --exit-code 3cf075ff 91c7f5f3 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements project08-concept-card-metadata/artifacts
git -C .worktrees/planning diff --exit-code 91db42fa a24758b4 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements project08-concept-card-metadata/artifacts
opening_planning_head=f3cadf33
committed_review_head=${COMMITTED_REVIEW_HEAD:?set to the committed Slice12 planning commit}
git -C .worktrees/planning diff --exit-code "$opening_planning_head" "$committed_review_head" -- project08-concept-card-metadata/arc01-metadata-research-and-requirements project08-concept-card-metadata/artifacts
diff -u \
  <(printf '%s\n' \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-membership.json \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-evidence.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/handoff.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/validation-evidence.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/artifacts/historical-policy-comparison.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/artifacts/validation-evidence.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/ledger.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/closing-report.md | sort) \
  <(git -C .worktrees/planning diff --name-only "$opening_planning_head" "$committed_review_head" | sort)
```

After the scoped commit, invoke this route with
`COMMITTED_REVIEW_HEAD=<Slice12-commit>`. The explicit before/after scope is
`f3cadf33 -> <Slice12-commit>`; CDC edits after the opening planning head are
outside this CC scope and must not be counted as CC evidence.

## Iteration 01 Replay

Executed pre-commit from the source checkout with Bash, jq 1.6, shasum and Git
2.39.5. Opening planning head: `46f60e46`; packet preservation is fixed to
`355d037f -> 400b847a`. Model/effort is unavailable from repository state.

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
jq -e '([.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")]|length)==2054 and ([.records[]|select(.values|type=="object")|select(.record_kind=="concept-card")]|length)==31 and ([.records[]|select(.values|type=="object")|select(.record_kind=="relationship-edge")]|length)==2' "$i"
 jq -e 'all(.cases[]; has("input") and has("path") and has("operation") and has("expected") and has("observed"))' "$s/artifacts/query-cases.json"
 jq -e '.cases[0].expected==.cases[0].observed and .cases[1].expected==.cases[1].observed and .cases[2].expected==.cases[2].observed and .cases[3].expected==.cases[3].observed' "$s/artifacts/query-cases.json"
test -f /Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/meter.md
test ! -e records/edge-evidence-map-related-to-claim.md
test ! -e records/support-synthetic-edge-001.md
git -C .worktrees/planning diff --exit-code 355d037f 400b847a -- project08-concept-card-metadata/arc01-metadata-research-and-requirements project08-concept-card-metadata/artifacts
git -C .worktrees/planning diff --check
```

All assertions passed pre-commit. Detailed field type/shape/value counts and
named reads are in `semantic-evidence.md`; they are not the 35 membership count.

## Iteration 03 Native Replay (Historical)

Executed from the source checkout after the Iteration 03 edits. Opening heads:
source `e763c661`, planning `91db42fa`; the final preservation endpoint is the
uncommitted current planning worktree and is labeled as such. Bash uses only
`awk`, `grep`, `jq`, `rg`, `shasum`, and Git; it computes each observed case
from native inputs before comparing it with the independently authored expected
object. The negative control remains in the shell only and changes no input.

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
music=/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician

# Scope, two evidence layers, and every registered input hash.
expected=$(awk -F'`' '/^\| `/{print $2 "|" $4}' "$s/slice-plan.md" | sort -u)
actual=$(jq -r '.memberships[] | .field_path + "|" + .record_kind' "$s/artifacts/semantic-membership.json" | sort -u)
test "$(printf '%s\n' "$expected" | sed '/^$/d' | wc -l | tr -d ' ')" = 35
test "$expected" = "$actual"
jq -e '. as $r | all($r.memberships[]; .meaning_id as $m | $r.meanings | has($m)) and all(($r.meanings[].evidence_ids[], $r.memberships[].evidence_ids[]); . as $id | $r.evidence | has($id))' "$s/artifacts/semantic-membership.json"
while IFS=$'\t' read -r path digest; do test "$(shasum -a 256 "$path" | awk '{print $1}')" = "$digest"; done < <(jq -r '.evidence[] | [.path,.sha256] | @tsv' "$s/artifacts/semantic-membership.json")

# Native prerequisite and extension values, then bounded filename resolution.
prereq=$(awk '/^prerequisites:/{p=1;next} /^extends:/{p=0} p && /^  - /{sub(/^  - /, ""); print; exit}' "$music/accent-types.md")
ext=$(awk '/^extends:/{p=1;next} /^related:/{p=0} p && /^  - /{sub(/^  - /, ""); print; exit}' "$music/accented-incomplete-neighbor.md")
test "$prereq" = meter; test -f "$music/$prereq.md"
test "$ext" = incomplete-neighbor; test -f "$music/$ext.md"
jq -e --arg from "$prereq" --arg to accent-types --argjson found true '.cases[] | select(.id=="prerequisite") | .expected == {from:$from,to:$to,target_found:$found} and .observed == {from:$from,to:$to,target_found:$found}' "$s/artifacts/query-cases.json"
jq -e --arg from accented-incomplete-neighbor --arg to "$ext" --arg inverse "$ext is extended by accented-incomplete-neighbor" --argjson found true '.cases[] | select(.id=="extension") | .expected == {from:$from,to:$to,inverse:$inverse,target_found:$found} and .observed == {from:$from,to:$to,inverse:$inverse,target_found:$found}' "$s/artifacts/query-cases.json"
! test "$ext" = CDC-deliberately-wrong-target

# Native reciprocal related lookup; no reciprocal stored edge is created.
grep -A4 '^related:' "$music/accented-incomplete-neighbor.md" | grep -qx '  - appoggiatura'
grep -A4 '^related:' "$music/appoggiatura.md" | grep -qx '  - accented-incomplete-neighbor'
jq -e '.cases[] | select(.id=="symmetry") | .expected == .observed and .observed.reciprocal == true' "$s/artifacts/query-cases.json"

# Native populated-edge declarations and a declared-path negative lookup.
grep -A4 '^from_ref:' knowledge/concept-cards/examples/relationship-edge.md | grep -qx '  id: cc-prepared-source-provenance'
grep -A4 '^to_ref:' knowledge/concept-cards/examples/relationship-edge.md | grep -qx '  id: cc-claim-support-is-assertion-specific'
grep -A4 '^from_ref:' knowledge/concept-cards/examples/relationship-edge.md | grep -qx '  revision: 1'
grep -A4 '^to_ref:' knowledge/concept-cards/examples/relationship-edge.md | grep -qx '  revision: 1'
grep -q '^id: cc-prepared-source-provenance$' knowledge/concept-cards/examples/minimal-card.md
grep -q '^id: cc-claim-support-is-assertion-specific$' knowledge/concept-cards/examples/claim-backed-card.md
! rg -n '^id: support-synthetic-edge-001$|path: .*support-synthetic-edge-001' knowledge/concept-cards/examples
jq -e '.cases[] | select(.id=="edge-endpoints") | .expected == .observed and .observed.support_path == "unavailable"' "$s/artifacts/query-cases.json"

# Census facts, JSON, whitespace, and constrained preservation.
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
jq -e '([.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")]|length)==2054 and ([.records[]|select(.values|type=="object")|select(.record_kind=="concept-card")]|length)==31 and ([.records[]|select(.values|type=="object")|select(.record_kind=="relationship-edge")]|length)==2' "$i"
jq empty "$s/artifacts/semantic-membership.json"; jq empty "$s/artifacts/query-cases.json"
git -C .worktrees/planning diff --check
diff -u \
  <(printf '%s\n' \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/handoff.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/query-cases.json \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-evidence.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-membership.json \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/validation-evidence.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/closing-report.md \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/ledger.md | sort) \
  <(git -C .worktrees/planning diff --name-only | sort)
```

The replay demonstrates the four selected operations only. It does not prove
global slug resolution, target identity/revision, source support for an edge,
or final-profile/extraction quality.

## Iteration 04 Replay

Executed from the source checkout after the Iteration 04 edits. Actual opening
state: source `e763c661`, planning `3cf075ff`; the planning tree was clean
before this packet. The current pre-commit route deliberately checks the
uncommitted seven-file packet. The bounded `awk` reads below extract only named
frontmatter regions, not a general YAML grammar. The native symmetry and
endpoint objects are derived from unchanged inputs; both authored objects are
compared independently to each native object.

```bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
t=.worktrees/planning/project08-concept-card-metadata/artifacts/semantic-transition-coverage.json
music=/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician

expected=$(awk -F'`' '/^\| `/{print $2 "|" $4}' "$s/slice-plan.md" | sort -u)
actual=$(jq -r '.memberships[] | .field_path + "|" + .record_kind' "$s/artifacts/semantic-membership.json" | sort -u)
test "$(printf '%s\n' "$expected" | sed '/^$/d' | wc -l | tr -d ' ')" = 35
test "$expected" = "$actual"
jq -e '(.accepted_pairs|length)==115 and (.remaining_pairs|length)==440' "$t"
test $((440 - 35)) = 405
jq -e '. as $r | all($r.memberships[]; .meaning_id as $m | $r.meanings | has($m)) and all(($r.meanings[].evidence_ids[], $r.memberships[].evidence_ids[]); . as $id | $r.evidence | has($id))' "$s/artifacts/semantic-membership.json"
while IFS=$'\t' read -r path digest; do test "$(shasum -a 256 "$path" | awk '{print $1}')" = "$digest"; done < <(jq -r '.evidence[] | [.path,.sha256] | @tsv' "$s/artifacts/semantic-membership.json")

# Census anchors for the literal 35-pair tables: populations, legacy states,
# card roots/components, and template/example edge shapes.
jq -e '
  ([.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")]|length)==2054 and
  ([.records[]|select(.record_kind=="concept-card")]|length)==31 and
  ([.records[]|select(.record_kind=="relationship-edge")]|length)==2 and
  ([.records[]|select(.path|test("complete-musician"))|select(.values.prerequisites|type=="array" and length==0)]|length)==5 and
  ([.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")|select(.values|has("extends")|not)]|length)==66 and
  ([.records[]|select(.values|has("prerequisites"))|select(.values.prerequisites==null)]|length)==1 and
  ([.records[]|select(.values|has("related"))|select(.values.related==null)]|length)==1 and
  ([.records[]|select(.values|has("contrasts_with"))|select(.values.contrasts_with==null)]|length)==3 and
  ([.records[]|select(.record_kind=="concept-card")|select(.values|has("relationship_edge_refs"))]|length)==1 and
  ([.records[]|select(.record_kind=="concept-card")|select(.values.relationship_refs|type=="array" and length==0)]|length)==6 and
  ([.records[]|select(.record_kind=="concept-card")|.values.relationship_refs?[]?|select(.id=="edge-evidence-map-related-to-claim" and .path=="records/edge-evidence-map-related-to-claim.md" and .revision==1)]|length)==1 and
  ([.records[]|select(.path=="knowledge/concept-cards/templates/relationship-edge.md")|select(.values.direction==null and .values.endpoint_roles.from_role==null and .values.source_support_refs==[])]|length)==1 and
  ([.records[]|select(.path=="knowledge/concept-cards/examples/relationship-edge.md")|select(.values.directed==true and .values.relation_type=="precedes" and .values.source_support_refs[0]=={id:"support-synthetic-edge-001",revision:1})]|length)==1
' "$i"

# Unchanged native prerequisite/extension comparators.
prereq=$(awk '/^prerequisites:/{p=1;next} /^extends:/{p=0} p && /^  - /{sub(/^  - /,""); print; exit}' "$music/accent-types.md")
ext=$(awk '/^extends:/{p=1;next} /^related:/{p=0} p && /^  - /{sub(/^  - /,""); print; exit}' "$music/accented-incomplete-neighbor.md")
test "$prereq" = meter; test -f "$music/$prereq.md"
test "$ext" = incomplete-neighbor; test -f "$music/$ext.md"

# Symmetry: every reported field derives from the two native related arrays.
a=accented-incomplete-neighbor; b=appoggiatura
a_lists_b=false; b_lists_a=false
grep -A4 '^related:' "$music/$a.md" | grep -qx "  - $b" && a_lists_b=true
grep -A4 '^related:' "$music/$b.md" | grep -qx "  - $a" && b_lists_a=true
symmetry_native=$(jq -n --arg a "$a" --arg b "$b" --argjson ab "$a_lists_b" --argjson ba "$b_lists_a" '{a:$a,b:$b,a_lists_b:$ab,b_lists_a:$ba,reciprocal:($ab and $ba),lookup:"symmetric"}')
jq -e --argjson native "$symmetry_native" '.cases[]|select(.id=="symmetry")|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"
! jq -e --argjson native "$symmetry_native" '.cases[]|select(.id=="symmetry")|.expected.a="CDC-deliberately-wrong-endpoint"|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"

# Endpoints: requested identity and revision are separately compared to each
# target declaration; support is a bounded, independent lookup.
edge=knowledge/concept-cards/examples/relationship-edge.md
from_id=$(awk '/^from_ref:/{p=1;next} /^to_ref:/{p=0} p&&/^  id:/{sub(/^  id: /,"");print;exit}' "$edge"); from_revision=$(awk '/^from_ref:/{p=1;next} /^to_ref:/{p=0} p&&/^  revision:/{sub(/^  revision: /,"");print;exit}' "$edge")
to_id=$(awk '/^to_ref:/{p=1;next} /^source_support_refs:/{p=0} p&&/^  id:/{sub(/^  id: /,"");print;exit}' "$edge"); to_revision=$(awk '/^to_ref:/{p=1;next} /^source_support_refs:/{p=0} p&&/^  revision:/{sub(/^  revision: /,"");print;exit}' "$edge")
support_id=$(awk '/^source_support_refs:/{p=1;next} p&&/^  - id:/{sub(/^  - id: /,"");print;exit}' "$edge"); support_revision=$(awk '/^source_support_refs:/{p=1;next} p&&/^    revision:/{sub(/^    revision: /,"");print;exit}' "$edge")
from_target=knowledge/concept-cards/examples/minimal-card.md; to_target=knowledge/concept-cards/examples/claim-backed-card.md
from_target_id=$(awk '/^id:/{sub(/^id: /,"");print;exit}' "$from_target"); from_target_revision=$(awk '/^revision:/{sub(/^revision: /,"");print;exit}' "$from_target")
to_target_id=$(awk '/^id:/{sub(/^id: /,"");print;exit}' "$to_target"); to_target_revision=$(awk '/^revision:/{sub(/^revision: /,"");print;exit}' "$to_target")
support_found=false; support_path=unavailable
if rg -q "^id: $support_id$|path: .*${support_id}" knowledge/concept-cards/examples; then support_found=true; support_path=found; fi
endpoint_native=$(jq -n --arg fi "$from_id" --argjson fr "$from_revision" --arg fdi "$from_target_id" --argjson fdr "$from_target_revision" --arg ti "$to_id" --argjson tr "$to_revision" --arg tdi "$to_target_id" --argjson tdr "$to_target_revision" --arg si "$support_id" --argjson sr "$support_revision" --arg sp "$support_path" --argjson sf "$support_found" '{from:{requested:{id:$fi,revision:$fr},declared:{id:$fdi,revision:$fdr},identity_match:($fi==$fdi),revision_match:($fr==$fdr)},to:{requested:{id:$ti,revision:$tr},declared:{id:$tdi,revision:$tdr},identity_match:($ti==$tdi),revision_match:($tr==$tdr)},support:{requested:{id:$si,revision:$sr},declared_path:$sp,declared_id_found:$sf}}')
jq -e --argjson native "$endpoint_native" '.cases[]|select(.id=="edge-endpoints")|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"
! jq -e --argjson native "$endpoint_native" '.cases[]|select(.id=="edge-endpoints")|.expected.to.revision_match=false|.expected==$native and .observed==$native' "$s/artifacts/query-cases.json"

jq empty "$s/artifacts/semantic-membership.json"; jq empty "$s/artifacts/query-cases.json"
git -C .worktrees/planning diff --check
git -C .worktrees/planning diff --exit-code 91db42fa a24758b4 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements project08-concept-card-metadata/artifacts
git -C .worktrees/planning diff --name-only 3cf075ff -- | sort
```

Every command in this Iteration 04 block passed before the commit. The two
`! jq -e` controls pass only because the same native-result comparator rejects
the deliberately wrong symmetry endpoint and target revision expectation.
After the scoped commit, review this packet with
`git -C .worktrees/planning diff --name-only 3cf075ff HEAD`; the prior packet
remains reproducible with the fixed `91db42fa -> a24758b4` route above.
