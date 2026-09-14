# CDC Verification: Slice09

Reviewed `6eb034a1` on 2026-09-13 against the seven original criteria.
**Changes required.** Exact coverage and scoped preservation pass. Retain the
useful template-only and assertion-support distinctions; correct the bounded
issues below before closure. No next slice opens.

## S9-R1: Replay And Census Do Not Establish The Reported Checks

Correctness-grade; artifacts/validation-evidence.md:15, 27-38, 49-78.

The literal replay from the declared source cwd prints 32, then exits 2:
`Could not open file inventory.json`. Later commands use slice-relative
`artifacts/` and sibling paths without changing cwd. Independently trying
the evidence check at line 51 from the slice directory exits 5:
`Cannot index array with string "evidence"`. Its pipeline has replaced the
root object with an array before reading .evidence. These are actual replay
failures, not hypothetical portability concerns.

Even after correcting paths, the 224-row census emits only kind/family/key/
JSON type. It does not emit values, nested typed shapes, collection length
or record path, and cannot distinguish empty from populated arrays. It also
merges pilot and expanded contexts into Arc07. Supply the required full
selected-field presence/value/shape census with attributable input paths and
separate meaningful families. Account for the three malformed inputs by
identity and parse limitation, not a repeated count alone.

The multi-file `sed -n '1,180p'` commands use cumulative line numbering.
The rerun command therefore omits the teaching card's claim/support body;
the five-file template/example command omits later examples. Use per-file
reads with bounds that include every claimed section. The blocks are labeled
sh but rely on Bash brace expansion; name the actual shell.

The listed hash command prints 13 hashes, whereas the register has 16 inputs;
it neither compares them to registered values nor includes frozenInventory,
skillRules or lifecycle. CDC separately checked all 16 successfully, but this
does not make the published route complete. Resolve both membership and
meaning evidence layers in the replay, derive expected pairs from the plan
and assert frozen inclusion, accepted-set disjointness and remainder counts.
A JSON object containing false check results must not still count as success.

Preservation is prose with an omitted path list, not a literal command.
Record fixed 682e4a10-to-6eb034a1 prior-packet preservation, and clearly label
the repair's pre-commit current-state check. Reconcile the closing report's
claim that all checks ran as documented. Keep previous failures visible.

## S9-R2: Target Evidence And Baseline Mapping Are Incomplete

Serious; artifacts/semantic-evidence.md:33-54 and
artifacts/semantic-membership.json evidence register.

The inspected rerun copies do contain claim/support headings and request
revision 1. The report correctly refuses to infer embedded revisions from
the containing cards' revisions 2 and 3. Preserve that result.

The matrix does not cover the reruns' source reference: its path addresses
an absolute temporary chapter file rather than the pilot acquisition record.
Record the actual requested tuple, current availability, applicable target
declarations and known snapshot evidence, or explicit unresolved components.
A copied source path is not evidence that its target was checked. This is
reference/identity inspection, not permission to verify neuroscience claims.

The pilot acquisition target is described but not registered. Slice08 is
named as prior evidence without a registered exact artifact/section/hash.
Register the evidence actually relied upon, with explicit attribution when
reusing accepted findings. Do not recursively copy the entire prior packet.

Likewise, registered rerun-copy hashes show which copies were read; they do
not establish the asserted mapping back to frozen workbench records. Record
the two exact original-path -> copy-path associations and compare copy hashes
to the frozen entries/manifests. No current workbench dependency is required.
Complete the selected reference matrix with actual IDs/paths/revisions rather
than only `*-r2`/`*-r3` placeholders. Keep synthetic targets fictional.

## S9-R3: Component Meanings Still Inherit Collection Definitions

Serious; artifacts/semantic-membership.json:31-54.

The registry has 21 memberships but nine meanings. Sharing definitions is
allowed; the problem is their applicability. For example,
claim_refs[].revision resolves to card-claim-refs, whose definition is
"collection of claims a card makes discoverable." source_refs[].path and
source_support_refs[].id likewise resolve to collection definitions.
The membership dispositions are more specific and useful; preserve them,
but supply an accurate effective meaning for the entry/component itself.

Use separate meanings or explicit component definitions composed with a
shared family rule. Do not require one meaning ID per pair for its own sake.
Keep evidence at both layers appropriate to the actual field and observed
context, not just the containing family.

The assertion_kind and card_ref definitions also call them optional.
Null template defaults show unfilled/unknown values, not by themselves an
optional-field policy. Cite a supporting rule or leave requiredness unresolved.
Keep intended claim mode and containing-card role distinct from observed
populated usage.

The historical comparison identifies useful teaching bodies, but the selected
statement/assertion-kind discussion remains mostly a general preservation
instruction. Ground it in a bounded named definition/assertion passage from
the required music/OTP samples and the current claim/template examples:
what wording/scope is readable, what is structured, and what cannot be
mechanically inferred. This is not a new historical corpus audit or a source
truth judgment.

## Independent Results

- Exact 21 plan-derived unique pairs, frozen inclusion, no accepted-94 overlap
  and 440 other pairs: pass with CDC-authored checks.
- Both meaning/member evidence IDs resolve: pass. Resolution alone does not
  establish the effective component meanings under R3.
- All 16 registered SHA-256 values match their current inputs.
- Inspected both pinned rerun cards separately, current extraction guidance,
  the claim template and the prior reviewed pilot contexts. The heading/
  embedded-revision distinction and template-only claim boundary hold.
- Fixed 682e4a10-to-6eb034a1 comparison of Slice01/04/06/07/08 is empty.
  Commit touches exactly the six authorized Slice09 delivery files.
- Source checkout is clean; commit whitespace check passes.

Literal failure reproduction from the source cwd:

~~~bash
set -o pipefail
s=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice09-claim-and-card-linkage-semantics
awk '/^```sh$/ {active=1;next} /^```$/ {active=0;next} active {print}' "$s/artifacts/validation-evidence.md" | bash -e
~~~

Expected on reviewed 6eb034a1: exit 2 after 32 and missing inventory.json.
This is a recorded negative check, not a successful acceptance command.

Independent all-input verification from the same cwd:

~~~bash
set -euo pipefail
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice09-claim-and-card-linkage-semantics"
jq -r '.evidence[]|[.sha256,.path]|join("  ")' "$s/artifacts/semantic-membership.json" | shasum -a 256 -c -
jq -e '.evidence as $e | .meanings as $m |
 all(.memberships[];$m[.meaning_id]!=null and all(.evidence_ids[];$e[.]!=null)) and
 all(.meanings[];all(.evidence_ids[];$e[.]!=null))' "$s/artifacts/semantic-membership.json"
expected=$(awk -F '|' '/^\| \x60/ {gsub(/[\x60 ]/,"",$2);gsub(/[\x60 ]/,"",$3);print $2 "\t" $3}' "$s/slice-plan.md" | jq -Rsc 'split("\n")|map(select(length>0)|split("\t"))')
jq -en --argjson expected "$expected" --slurpfile ours "$s/artifacts/semantic-membership.json" \
 --slurpfile i "$a/slice01-metadata-inventory-and-research-questions/artifacts/field-dispositions.json" \
 --slurpfile b "$a/slice04-semantic-identity-source-and-graph-families/artifacts/batch01-identity-membership.json" \
 --slurpfile six "$a/slice06-record-identity-and-classification/artifacts/semantic-membership.json" \
 --slurpfile seven "$a/slice07-source-identity-and-locator-semantics/artifacts/semantic-membership.json" \
 --slurpfile eight "$a/slice08-source-support-subjects-and-spans/artifacts/semantic-membership.json" '
 ([$ours[0].memberships[]|[.field_path,.record_kind]]) as $actual |
 ([$i[0].field_paths[]|.field_path as $p|.record_kinds[]|[$p,.]]) as $inventory |
 ([$b[0].memberships[],$six[0].memberships[],$seven[0].memberships[],$eight[0].memberships[]|[.field_path,.record_kind]]) as $accepted |
 ($expected|sort)==($actual|sort) and ($actual|unique|length)==21 and
 ($accepted|unique|length)==94 and ($actual-$accepted|length)==21 and
 ($actual-$inventory|length)==0 and ($inventory-$accepted-$actual|length)==440'
git -C .worktrees/planning diff --exit-code 682e4a10 6eb034a1 -- \
 project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions \
 project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families \
 project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification \
 project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics \
 project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice08-source-support-subjects-and-spans
git -C .worktrees/planning show --check 6eb034a1
~~~

These pass; they do not substitute for R1's complete repaired replay.

## Seven-Row Walk

| Row | CDC disposition | Reason |
| --- | --- | --- |
| S9-1 | open | 16 hashes pass; target/prior-evidence registration and exact baseline mapping incomplete under R2 |
| S9-2 | done, reproduced | Plan-derived exact 21, unique/frozen inclusion, disjoint accepted 94 and 440 remainder |
| S9-3 | open | R1 value/shape/empty-vs-populated census; R3 contextual component meanings |
| S9-4 | open | Useful pilot/embedded-heading limits stand; R2 rerun source-target evidence incomplete |
| S9-5 | open | R3 effective field definitions and bounded assertion/body comparison |
| S9-6 | open | R1 literal replay fails and omits substantive checks; report overstates completion |
| S9-7 | done, reproduced | Six-file scope, fixed prior-packet preservation, clean source and whitespace |

## Bubble-Up

All four assigned artifacts exist in artifacts/, but their required evidence
is incomplete. Correct S9-R1/R2/R3 in Iteration 01; do not rewrite the input
cards or prior accepted packets. Retain exact pair coverage, distinct
membership dispositions, template-only limits and the useful qualified
reference findings. No scope reduction or ownership transfer is required.

Arc01's plan records the correction before further execution. 94 pairs remain
accepted, 21 assigned here and 440 others remain. Slice04/05 integration,
Slice01 and research gates, P-14 and all repeated-run quality goals remain
unchanged. This review neither closes a parent nor repairs the underlying
metadata profile.
