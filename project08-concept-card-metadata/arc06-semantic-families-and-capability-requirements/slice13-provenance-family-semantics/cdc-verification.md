# CDC Review: Arc06 Slice13

## Current Verdict: Closed (2026-09-17)

Workflow: Two-Contributor, separate CDC review of CC implementation.
Reviewed assignment: preserved legacy artifacts/iteration-01-cc-prompt.md.
Reviewed endpoint: d94ab1c6ffe69674cfc2a334f87607257e4ad5a1.
Repair opening: e42419482aebabcdac9be9e3032daa8f72da09d3.
Original opening/endpoint: 609f2f55 / 78be7fab, separately checked.
Source at review: 020268248882358075b678bb855c0ac8d11b532a, clean;
historical source authority remains e763c661592ff1097a94bb470db9cf924524579d.

All six ledger rows are independently done. R1-R4 below are resolved, not
deleted. Accept exactly eight inventory-interpretation pairs; this does not
accept actor identity equivalence, requiredness, a schema, source truth,
extraction quality, memory admission or any runtime operation.

### Reproduction And Source Drift

The unmodified committed wrapper at d94ab1c6 exits 1 at the exact source-HEAD
guard: main advanced to 02026824 after CC's run. This failure is retained;
the submitted recipe is not claimed to pass unchanged on today's checkout.
Independent comparison finds no changes in knowledge/concept-cards or
knowledge/document-extraction between its historical source and current HEAD.
The recipe already hashes each registered source input at its declared commit.
CDC therefore runs the exact endpoint recipe with only its global HEAD equality
guard replaced by historical commit existence, after the scoped source diff.
No tracked CC supporting artifact or implementation was changed. This is an explicitly
bounded equivalent verification against unchanged relevant source, not a
repair to be independently accepted by its author.

The source= line in that replay names the historical authority e763c661;
it is not a claim that current main still has that HEAD.

Literal equivalent route (Bash; existing Git/awk/sed/grep/jq/rg/hash tools):

~~~bash
set -euo pipefail
source=/Users/oubiwann/lab/billosys/ai-engineering
plan=$source/.worktrees/planning
s=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics
endpoint=d94ab1c6ffe69674cfc2a334f87607257e4ad5a1
git -C "$source" diff --exit-code e763c661 HEAD -- knowledge/concept-cards knowledge/document-extraction
recipe=$(git -C "$plan" show "$endpoint:$s/artifacts/validation-evidence.md" |
 awk '/^## Literal route$/{seen=1;next} seen && /^~~~bash$/{p=1;next} p && /^~~~$/{exit} p')
test -n "$recipe"
test "$(printf '%s\n' "$recipe" | grep -Fc 'test "$(git -C "$source" rev-parse HEAD)" = "$opening_source"')" = 1
recipe=$(printf '%s\n' "$recipe" | sed 's@test "$(git -C "$source" rev-parse HEAD)" = "$opening_source"@git -C "$source" cat-file -e "$opening_source^{commit}"@')
CC_COMMIT="$endpoint" bash <<< "$recipe"
~~~

Independent results, before reviewer edits:

- Status 0; exact original and repair six-file contributions and protected
  historical paths pass independently.
- 8 actual unique memberships match the pinned plan, registry scope and
  opening coverage; shared meanings and both evidence-reference layers resolve.
- Invalid-member and dangling-reference controls return 1. Native wrong-actor
  expectation returns 1; successful no-match returns 0; missing-input jq
  returns 2 with stderr. The redundant suppressed-error raw search is removed.
- All 51 registered hashes match. Both declared rich/teaching original-copy
  mappings resolve through their registered manifests and compare byte-equal.
- All authored 37-record family/state/label census cells and three named YAML
  exclusions reconcile to the frozen native inventory. Legacy comparison:
  2,054 parsed mappings, 2,054 absent actor parents, zero literal dotted keys.
- Original opening coverage remains 180/375/8/367; live status is separately
  inspected. Frozen 115/440 transition and earlier packets remain unchanged.
- The submitted wrapper independently rejects a nonexistent recipe object
  and a valid recipe commit lacking the file; both return 128, never success.
- Source/planning clean before editing; whitespace checks pass.

The wrapper controls used its first Bash block from d94ab1c6, with
CC_COMMIT=d94ab1c6 and REPLAY_COMMIT respectively
0000000000000000000000000000000000000000 and 609f2f55. No fixture was substituted
into a tracked file. Earlier exploratory inspection queries with the wrong
JSON key/shape were corrected; only actual evidence_id entries and records
are used in the checks and decisions here.

### Finding Dispositions And Row Walk

| Finding / row | Independent evidence and decision |
| --- | --- |
| R1 / S13-2, S13-3, S13-5 | The committed registry, actual membership projection, shared/member reference layers, authored native census and declared baseline mappings are checked. Controls reject invalid membership/references. Closed. |
| R2 / S13-5 | Recipe and contribution endpoints are explicit; registry and authority use Git snapshots. Original and repair histories are separate; project-prefixed protected paths checked. Live coverage is status, not fixed historical bytes. Closed, with source-HEAD drift limitation above. |
| R3 / S13-4 | Redundant raw rg search removed as explicitly permitted. Hash-bound native absence query, genuine wrong expectation and missing-input error reproduce without suppressed error paths. Closed. |
| R4 / S13-2, S13-3 | Legacy census reproduced; field-group table explicitly names actor only for run/preservation while four templates establish selected placements. Correct project AGENTS is separately registered from planning-root AGENTS, at the declared snapshot. Closed. |
| S13-1 | Exact eight-pair set, frozen inclusion and accepted disjointness at opening reproduced; accept the eight once in live coverage. Done. |
| S13-2 | 37 records: 12 absent parents, four template object/null identities, 21 object/string identities. Family distinctions and three malformed exclusions retained; legacy result bounded to frozen inventory. Done. |
| S13-3 | Full per-kind meanings/dispositions and contextual witnesses reviewed. Actor labels remain separate from root record identity, source author, run, reviewer and embedded-record actors. Field-specific limits are supported; no global principal authority is inferred. Done. |
| S13-4 | Native actor observation, wrong expectation, template null versus actual parent absence, successful no-match and tool-error separation reproduced. Done. |
| S13-5 | 51/51 hashes, manifest/native-copy mapping, mutation checks, exact original/repair boundaries and preservation pass with disclosed equivalent execution. Done. |
| S13-6 | All nonassigned provenance and later lifecycle work retain owners; P-15 stays open. Successor is sized below, not silently reduced. Done. |

Interpretation limit: not_applicable_parent_absent is a child-lookup result
because there is no parent object to inspect. It is NOT evidence that actor
provenance is semantically inapplicable to a record. The evidence explicitly
rejects that inference. Matching codex/codex-cc labels cannot establish a
particular human, model/version or globally unique principal. Template-only
claim/run cases do not establish populated semantics or requiredness.

### Bubble-Up And Successor

The six-row contract and four supporting artifacts are complete; the legacy
iteration prompt remains an issued assignment, not a fifth produced artifact.
No source, package, helper, parser, runtime or extraction work was performed.
No new semantic defect remains against this bounded contract. The historical
literal source-HEAD constraint is a reproducibility limitation, not hidden.

Update live coverage to 188 accepted / 367 remaining. Size Slice14 to the
12 actor/actor.id pairs in the other six kinds. CDC's frozen-input sizing query
selects those kinds from inventory.records and counts object-valued mappings:
memory-admission 2, preservation-decision 1, relationship-edge 2,
source-locator 1, source-support 5, validation-result 1. Those 12 records are
six template object/null, two synthetic absent parents and four populated
pilot supports. They are not 12 established actor meanings.

Planned Slice15 explicitly retains all 20 actor.mode/actor.role pairs and the
other former provenance/run/preparation/method/shared-reference/CQ interface
obligations, with sizing required before execution. Other semantic families
keep their owners. The live register assigns 12, leaving 355 outside Slice14.
Arc06 composition and all project/Operator gates remain open.

## Historical Initial Review (2026-09-15; Superseded Verdict)

Date: 2026-09-15. Verdict: changes required; bounded Iteration 01.
Reviewed CC endpoint: `78be7fabae79039ef3f24daa639d8e314ebcee0f`.
Original planning opening: `609f2f558b100a06df42e6a8b85ebfe200a27b22`.
Source: `e763c661592ff1097a94bb470db9cf924524579d`, unchanged and clean.
No semantic memberships are accepted. S13-1/S13-6 are verified; the other
four rows remain open. Slice14 is not opened.

## Findings

### R1: Replay Does Not Validate The Authored Registry

Priority: P2. At validation-evidence.md:94-132, the route hashes the evidence
list and checks a hard-coded assignment against the coverage register, but
never compares the actual memberships to the plan/assignment or resolves
member/shared meaning and evidence references. It also does not compare the
authored native_census to native observations. Therefore it does not establish
the claimed artifact integrity.

CDC redirected only the manifest input to a temporary copy with an invalid
member path and dangling member/shared evidence IDs. The complete published
replay still exited 0. The tracked registry was never modified.
Independent CDC checks on the ORIGINAL registry pass exact eight-pair
uniqueness and both reference layers: the bug is in promised verification,
not evidence that the submitted eight memberships are wrong.

Repair: bind the actual memberships, scope and both evidence layers to the
pinned plan and coverage. Derive and compare the declared census, including
family/state/label and exclusion claims. Resolve baseline mapping IDs/paths/
hashes against their manifests rather than only hashing manifests and comparing
two hard-coded files. Add isolated invalid-member and dangling-reference
controls using the same predicates; each must reject for the intended reason.

### R2: Historical Replay Still Reads Mutable Authority

Priority: P2. validation-evidence.md:45 reads the working-tree registry even
when CC_COMMIT identifies an older contribution. Lines 110-125 assert the
LIVE coverage digest and values equal the opening snapshot. The evidence
registry likewise marks currentCoverage live with a fixed opening hash.
Thus later authorized coverage advancement breaks historical replay, and
later committed registry changes can replace the reviewed manifest unnoticed.
This contradicts the Slice03 correction and Slice13 snapshot requirements.

Repair: provide a fail-closed wrapper selecting the recipe revision explicitly;
in committed mode consume the registry at the claimed CC endpoint. Pin
assignment authority to the appropriate opening snapshot; record live status
separately, without requiring obsolete live counts/hashes. Keep original
609f2f55-to-78be7fab history distinct from the new repair opening-to-endpoint
diff and from any dirty-state check. Do not include CDC plan/review changes
in CC's six-file contribution. Also correct the protected arc paths at
lines 210-211, which omit the project prefix (the existing full exact-scope
check currently protects those real paths indirectly).

### R3: Raw Actor Search Converts Errors Into Absence

Priority: P2. validation-evidence.md:189 uses
`test -z "$(rg -n '^actor:' ... || true)"`. Both no-match and a search error
become empty stdout and pass. CDC substituted a real missing-input search
only at that operation: rg emitted an IO error, but the complete replay
still returned 0. The separate missing-inventory jq control does not test
this failed search path.

Repair: distinguish match, successful no-match (rg 1), and error (rg >1),
with actual output/status capture and a failing real missing-file control.
Alternatively remove the redundant raw search explicitly and rely on the
hash-bound native field-state observation; no suppressed-error path may
remain advertised as evidence of absence.

### R4: Complete The Bounded Census And Correct Source Attribution

Priority: P2. The plan explicitly requires the legacy untyped actor-field
census; no artifact or replay currently supplies it. CDC independently found
2,054 parsed legacy mappings and zero actor parents (therefore no nested
actor.id values); no literal dotted actor.id keys were present either. This
does not establish absence of all legacy provenance. Add the authored result
and literal query rather than silently dropping that comparison.

At semantic-evidence.md:66-67, the claim that record-field-groups.md places
actor on claim/CQ/card/run is inaccurate: that table explicitly names actor
for extraction-run and preservation-decision; the four templates establish
the selected mapping placements. Correct attribution and cite concrete
sections/ranges for member-specific meaning. Keep missing-parent child lookup
distinct from semantic inapplicability; do not adopt requiredness rules.

The evidence entry named projectAgents resolves to planning-root AGENTS.md,
not project08-concept-card-metadata/AGENTS.md required by the read set.
Register the project instructions separately with the correct role and
snapshot. Do not relabel the root instructions as the project instructions.

## Reproduced Positives

- Exact six-file CC diff and required trailers; clean source/planning at entry.
- Original committed recipe exit 0, 40/40 registered hashes, both byte-equal
  original/copy witnesses, published native comparisons and controls.
- Eight unique registry pairs match the plan and assignment; member meanings
  and both evidence-ID layers resolve in the actual submitted registry.
- Independent native census: claim 1, CQ 2, card 31, run 3; parents absent 12,
  template object/null 4, object/string 21.
- Independent family breakdown: four template nulls; synthetic absent CQ 1,
  run 2 and card 3; expanded cards absent 6; pilot card codex-cc 4;
  rich card codex 7; teaching card codex 10.
- Raw pilot, expanded, rich and teaching witness bodies/frontmatter support
  the bounded recorded-label interpretation. Operator/extraction guidance
  and run examples support keeping actor, source, run, reviewer and worker
  scope distinct. No global principal or codex/codex-cc equivalence is proven.

## Literal Fault Probes

These probes reproduce the ORIGINAL weaknesses. Their expected status 0 is
the defect, not the acceptance condition for repaired validation. Only
temporary data is written; the published registry and prior packets stay intact.

~~~bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
s=project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics
t=$(mktemp -d /private/tmp/cdc-s13-review.XXXXXX)
trap 'rm -rf "$t"' EXIT
git show "78be7fab:$s/artifacts/semantic-membership.json" |
  jq '.memberships[0].field_path="deliberately-invalid-field" |
      .memberships[0].evidence_ids=["missing-evidence-id"] |
      .meanings["actor-claim"].evidence_ids=["missing-shared-evidence-id"]' > "$t/membership.json"
recipe=$(git show "78be7fab:$s/artifacts/validation-evidence.md" |
  awk '/^~~~bash$/{p=1;next} /^~~~$/{if(p){exit}} p')
test -n "$recipe"
mutant_recipe=$(printf '%s\n' "$recipe" | sed 's@^membership=.*@membership=$CDC_MUTANT@')
# The original recipe's final clean-tree test requires a clean checkout.
# Run after the CDC commit; later coverage advancement may independently
# trip R2 before these probes reach their target.
if CDC_MUTANT="$t/membership.json" CC_COMMIT=78be7fab bash <<< "$mutant_recipe"; then status=0; else status=$?; fi
printf 'invalid-membership replay status=%s (observed 0 at review)\n' "$status"
rg() {
  if [ "${2-}" = '^actor:' ]; then
    command rg -n '^actor:' /private/tmp/cdc-s13-deliberately-missing-input
  else
    command rg "$@"
  fi
}
export -f rg
if CC_COMMIT=78be7fab bash <<< "$recipe"; then status=0; else status=$?; fi
printf 'real-search-error replay status=%s (observed 0 at review)\n' "$status"
~~~

## Row Dispositions And Bubble-Up

| Row | CDC disposition | Basis |
| --- | --- | --- |
| S13-1 | done | Actual eight-pair scope and ownership independently reconciled, though reusable checks need R1 |
| S13-2 | open | 37-record counts confirmed; missing legacy comparison and incomplete executable family assertions, R1/R4 |
| S13-3 | open | Preserve substantive contextual work; correct bounded evidence attribution/registration, R4 |
| S13-4 | open | Native positives and wrong-ID comparison pass; raw-search error is hidden, R3 |
| S13-5 | open | Hash/scope positives retained; authored registry, snapshot and error checks require R1-R3 |
| S13-6 | done | Complement, sizing proposal and P-15 retained; no successor authorized |

Four artifacts and the CC close packet exist in their prescribed homes.
The silent-drop claim is incomplete for the legacy census and replay bindings.
Arc/project plans now record a bounded Iteration 01, not a new family or scope
reduction. The current coverage register remains 180/375/8/367 unchanged.

What worked: the eight-pair boundary made the contextual evidence readable,
and native labels/parent states were not generalized into unsupported identity
policy. Residual problems are chiefly replay integration plus small evidence
omissions. Repeated fail-closed/snapshot mistakes are real observations, not
proof of a model or effort-level cause. No settings change is made here.
