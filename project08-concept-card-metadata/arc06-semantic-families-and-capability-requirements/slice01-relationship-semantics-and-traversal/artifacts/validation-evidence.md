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
