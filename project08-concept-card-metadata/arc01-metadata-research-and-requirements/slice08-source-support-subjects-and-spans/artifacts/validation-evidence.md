# Slice08 Validation Evidence

Declared cwd: /Users/oubiwann/lab/billosys/ai-engineering. Every command below
was executed here. The expected table comes only from slice-plan.md.

~~~bash
set -eu
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice08-source-support-subjects-and-spans"
expected=$(awk -F '|' '/^\| \x60/ {gsub(/[\x60 ]/, "", $2); gsub(/[\x60 ]/, "", $3); print $2 "\t" $3}' "$s/slice-plan.md" | jq -Rsc 'split("\n")|map(select(length>0)|split("\t"))')
jq -en --argjson expected "$expected" \
  --slurpfile s "$s/artifacts/semantic-membership.json" \
  --slurpfile i "$a/slice01-metadata-inventory-and-research-questions/artifacts/field-dispositions.json" \
  --slurpfile b "$a/slice04-semantic-identity-source-and-graph-families/artifacts/batch01-identity-membership.json" \
  --slurpfile six "$a/slice06-record-identity-and-classification/artifacts/semantic-membership.json" \
  --slurpfile seven "$a/slice07-source-identity-and-locator-semantics/artifacts/semantic-membership.json" '
  ([$s[0].memberships[]|[.field_path,.record_kind]]|sort) as $actual |
  ([$i[0].field_paths[]|.field_path as $p|.record_kinds[]|[$p,.]]) as $inventory |
  ([$b[0].memberships[],$six[0].memberships[],$seven[0].memberships[]|[.field_path,.record_kind]]) as $accepted |
  ($expected|sort)==$actual and ($actual|length)==27 and
  ($actual|unique|length)==27 and ($actual-$inventory|length)==0 and
  ($actual-$accepted|length)==27'
jq -e '(.memberships|length)==27 and (.evidence as $e|.meanings as $m|
  all(.memberships[];$m[.meaning_id]!=null and .evidence_ids==$m[.meaning_id].evidence_ids and .disposition==$m[.meaning_id].disposition and all(.evidence_ids[];$e[.]!=null)) and
  all(.meanings[];all(.evidence_ids[];$e[.]!=null)))' "$s/artifacts/semantic-membership.json"
jq -r '.evidence[]|[.sha256,.path]|join("  ")' "$s/artifacts/semantic-membership.json" | shasum -a 256 -c -
jq '[.records[]|select(.values.record_type=="source-support")|
  {path,subject:.values.subject_ref,status:.values.source_support_status,
   spans:.values.source_spans,
   shapes:{subject:.shapes.mapping.subject_ref,status:.shapes.mapping.source_support_status,spans:.shapes.mapping.source_spans}}]' \
  "$a/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json"
for f in \
  .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/cc-emergent-explanation.md \
  .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/cc-memory-consolidation.md \
  .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/cc-model-data-constraints.md \
  .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/cc-pattern-separation.md
do test -f "$f"; done
rg -n '^### Claim' \
  .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/cc-{emergent-explanation,memory-consolidation,model-data-constraints,pattern-separation}.md
rg -n 'Prepared-source ID|Revision|e0c697b4|loc-ch01-model-constraints|loc-ch01-emergence|loc-ch07-pattern-separation|loc-ch07-consolidation' \
  .worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/{source-acquisition.md,prepared-source-manifest.md,locator-map.md}
sed -n '69,78p' /Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/accent-types.md
sed -n '126,140p' knowledge/erlang/concept-cards/otp-design-principles/behaviour.md
git -C .worktrees/planning diff --exit-code d977cb31 2dfe5577 -- \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics
git -C .worktrees/planning diff --exit-code d977cb31 -- \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics
git -C .worktrees/planning diff --check
git status --short
~~~

Results: the table-derived set is exactly 27 unique frozen pairs and is disjoint
from the 67 accepted pairs. Both evidence layers resolve and all registered
hashes pass. The heading, acquisition/manifest and locator-map queries produce
the matrix findings: heading/row lookup is observed, while literal fragments,
embedded claim revisions, locator revisions, and source-record ID/revision
declarations are unresolved. Historical body inspection confirms readable source
references/notes but not machine support tuples. The fixed d977cb31-to-2dfe5577
prior-packet diff is empty; the separate current-state check is empty for
Slice01/04/06/07. Whitespace is clean. These are same-context CC checks, not
independent source verification.
