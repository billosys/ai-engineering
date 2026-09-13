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
git -C .worktrees/planning rev-parse 1bacd954 d977cb31
git -C .worktrees/planning diff --exit-code d977cb31 -- \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics
git -C .worktrees/planning diff --check
git status --short
~~~

Results: the table-derived set is exactly 27 unique frozen pairs and is disjoint
from the 67 accepted pairs. Both evidence layers resolve. All registered hashes
and all four declared claim-target paths pass. The census returns the five
roots with the null/empty template and populated pilot shapes described in
semantic-evidence.md. Historical endpoints 1bacd954 and d977cb31 are pinned;
the separate current-state check is empty for Slice01/04/06/07. Whitespace is
clean. These are same-context CC checks, not independent source verification.
