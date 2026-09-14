# Slice09 Iteration 01 Validation Evidence

All final blocks ran with Bash from `/Users/oubiwann/lab/billosys/ai-engineering`
on 2026-09-13. These are CC replays, not CDC verification. The old `6eb034a1`
route failed after `32` because it opened undeclared `inventory.json`; its
evidence jq then failed after changing root context. Those failures remain
negative history and are not counted as checks.

## Census and inspection replay

```bash
set -euo pipefail
root=$(pwd)
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice09-claim-and-card-linkage-semantics"
i="$root/$a/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json"
cd "$s"
jq -e '
 def family: if .path=="knowledge/concept-cards/templates/claim.md" then "claim-template" elif .path|startswith("knowledge/concept-cards/templates/") then "card-template" elif .path|startswith("knowledge/concept-cards/examples/") then "synthetic" elif .path|contains("slice02-pilot") then "pilot" elif .path|contains("slice04-expanded") then "expanded" elif .path|contains("compcogneuro-rich") then "rich-rerun" elif .path|contains("compcogneuro-teaching") then "teaching-rerun" else "other" end;
 ["assertion_kind","card_ref","source_refs","source_support_refs","statement","claim_refs","source_snapshot"] as $f |
 [.records[]|select(.record_kind=="claim" or .record_kind=="concept-card")|. as $r|$f[] as $k|{path:$r.path,family:($r|family),record_kind:$r.record_kind,field_path:$k,presence:(if ($r.keys|index($k)) then "present" else "absent" end),value:(if ($r.keys|index($k)) then $r.values[$k] else null end),value_type:(if ($r.keys|index($k)) then ($r.values[$k]|type) else "absent" end),typed_shape:(if ($r.keys|index($k)) then $r.shapes.mapping[$k] else "absent" end),collection_length:(if ($r.keys|index($k)) and ($r.values[$k]|type)=="array" then ($r.values[$k]|length) else null end)}] | {roots:(length/7),rows:length,census:.}' "$i"
jq -e '[.records[]|select((.path|startswith("workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/")) and ((.error|type)=="string") and (.error|startswith("YAML::XS")))|{path,error,sha256}]|length==3' "$i"
for f in ../../../../../knowledge/concept-cards/templates/claim.md ../../../../../knowledge/concept-cards/templates/concept-card.md ../../../../../knowledge/concept-cards/examples/minimal-card.md ../../../../../knowledge/concept-cards/examples/claim-backed-card.md ../../../../../knowledge/concept-cards/examples/rich-profile-card.md ../../../project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/cc-model-data-constraints.md ../../../project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/support-model-data-constraints.md ../../../project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards/cc-memory-forms.md ../slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md ../slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md; do sed -n '1,240p' "$f"; done
# Focused reads for every additionally cited interpretation; each command names
# one input and range, so later files cannot be omitted by cumulative numbering.
sed -n '37,75p' /Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/accent-types.md
sed -n '46,135p' ../../../../../knowledge/erlang/concept-cards/otp-design-principles/behaviour.md
sed -n '22,90p' ../../../old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md
sed -n '438,470p' ../../../old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md
sed -n '120,165p' ../../../../../knowledge/concept-cards/SKILL.md
sed -n '1,45p' ../../../../../knowledge/concept-cards/guides/05-evidence-lifecycle.md
sed -n '125,155p' ../../../../../knowledge/concept-cards/guides/05-evidence-lifecycle.md
sed -n '1,32p' ../../../project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/source-acquisition.md
sed -n '1,55p' /private/tmp/project05-compcogneuro-book-e0c697b4/chapter-01.md
sed -n '1,35p' ../slice08-source-support-subjects-and-spans/artifacts/semantic-evidence.md
```

This emitted exactly 32 roots and 224 rows. Each row contains path/family,
presence, actual value, JSON type, parser nested shape and collection length.
The single claim template has three present null scalars and two present empty
arrays; no populated standalone claim. Pilot and expanded families are separate;
the latter's six cards carry scalar `source_snapshot`. The three malformed rich
paths are `cc-memory-forms.md` (`d9bc411c...17593`), `cc-priming-forms.md`
(`c62584f...3ae8`), and `cc-recognition-dual-process.md` (`e691cbfc...1e1e`);
their YAML errors are retained as parse limitations, not metadata observations.

## Evidence, membership, mapping and preservation replay

```bash
set -euo pipefail
root=$(pwd)
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice09-claim-and-card-linkage-semantics"
cd "$s"
jq -r '.evidence[]|[.sha256,.path]|@tsv' artifacts/semantic-membership.json | while IFS=$'\t' read -r expected path; do case "$path" in /*) input=$path;; *) input="$root/$path";; esac; actual=$(shasum -a 256 "$input" | awk '{print $1}'); test "$expected" = "$actual"; done
jq -e '. as $r|($r.evidence|keys) as $keys|([.meanings[]|.evidence_ids[]]+[.memberships[]|.evidence_ids[]]) as $used|(($used-$keys)|length==0) and ([.memberships[]|select((.effective_meaning|type)!="string" or (.effective_meaning|length)==0 or (.evidence_ids|length)==0)]|length==0)' artifacts/semantic-membership.json
expected=$(awk -F '|' '/^\| `/{gsub(/[ `]/,"",$2);gsub(/[ `]/,"",$3);print $2 "\t" $3}' slice-plan.md | jq -Rsc 'split("\n")|map(select(length>0)|split("\t"))')
jq -en --argjson expected "$expected" --slurpfile ours artifacts/semantic-membership.json --slurpfile inv ../slice01-metadata-inventory-and-research-questions/artifacts/field-dispositions.json --slurpfile b ../slice04-semantic-identity-source-and-graph-families/artifacts/batch01-identity-membership.json --slurpfile six ../slice06-record-identity-and-classification/artifacts/semantic-membership.json --slurpfile seven ../slice07-source-identity-and-locator-semantics/artifacts/semantic-membership.json --slurpfile eight ../slice08-source-support-subjects-and-spans/artifacts/semantic-membership.json '([$ours[0].memberships[]|[.field_path,.record_kind]]) as $actual|([$inv[0].field_paths[]|.field_path as $p|.record_kinds[]|[$p,.]]) as $frozen|([$b[0].memberships[],$six[0].memberships[],$seven[0].memberships[],$eight[0].memberships[]|[.field_path,.record_kind]]) as $accepted|(($expected|sort)==($actual|sort)) and ($actual|unique|length==21) and ($accepted|unique|length==94) and (($actual-$accepted)|length==21) and (($actual-$frozen)|length==0) and (($frozen-$accepted-$actual)|length==440)'
grep -F '65915a99fd8ed9614d4a5be52615ff781cbb4dff4f3abf5516b7fc2a94bc3695  workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md' ../slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/source-sha256sums.txt
grep -F '09771f4fd35b02e4f57c808f329a2c23972a246f5546c875ff746e0ebf4230fb  workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md' ../slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/source-sha256sums.txt
grep -F '65915a99fd8ed9614d4a5be52615ff781cbb4dff4f3abf5516b7fc2a94bc3695  .worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md' ../slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/copy-sha256sums.txt
grep -F '09771f4fd35b02e4f57c808f329a2c23972a246f5546c875ff746e0ebf4230fb  .worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md' ../slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/copy-sha256sums.txt
shasum -a 256 ../slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md ../slice01-metadata-inventory-and-research-questions/artifacts/baseline-snapshots/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md
if test -r /private/tmp/project05-compcogneuro-book-e0c697b4/chapter-01.md; then shasum -a 256 /private/tmp/project05-compcogneuro-book-e0c697b4/chapter-01.md; else printf '%s\n' 'chapter-01 target unavailable'; fi
git -C ../../.. diff --exit-code 682e4a10 6eb034a1 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice08-source-support-subjects-and-spans
git -C ../../.. diff --exit-code b905290c 0aeaf507 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice08-source-support-subjects-and-spans
# Current-state comparison from this correction's actual entry commit d09d70bc;
# this intentionally excludes authorized CDC plan/ledger edits and is distinct
# from whitespace/status checks below.
git -C ../../.. diff --exit-code d09d70bc -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice08-source-support-subjects-and-spans
git -C ../../.. diff --check
git -C ../../.. status --short
```

All 21 registered hashes matched. Both evidence layers resolved and every
membership had a non-empty effective component meaning. The plan/frozen/
accepted assertion returned true: exact 21, unique, frozen inclusion, accepted
94, no overlap and 440 remainder. The rich and teaching original-to-copy
mappings match their respective frozen source and copy manifests; their copies
hash `65915a99...c3695` and `09771f4f...230fb`. The Chapter 1 target was
currently available and hashed `6a72d202...cba48`, matching acquisition.
The fixed `682e4a10`-to-`6eb034a1` and `b905290c`-to-`0aeaf507`
prior-packet diffs were empty. The explicit `d09d70bc` current-state comparison
of prior packets was also empty before this correction's commit; it excludes
CDC's authorized plan/ledger changes. The final `diff --check`/status portion
is only whitespace/current-state hygiene, not preservation evidence.
