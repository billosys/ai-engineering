# Slice07 Validation Evidence

Declared cwd: /Users/oubiwann/lab/billosys/ai-engineering.

~~~bash
set -eu
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice07-source-identity-and-locator-semantics"
jq -e '(.memberships|length)==20 and (.evidence as $e | .meanings as $m | all(.memberships[]; $m[.meaning_id]!=null and all(.evidence_ids[];$e[.]!=null)) and all(.meanings[];all(.evidence_ids[];$e[.]!=null)))' "$s/artifacts/semantic-membership.json"
jq -r '.evidence[]|[.sha256,.path]|join("  ")' "$s/artifacts/semantic-membership.json" | shasum -a 256 -c -
git -C .worktrees/planning diff --exit-code 1bacd954 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification
git -C .worktrees/planning diff --check
~~~

Executed results: membership/reference assertion true; all registered hashes OK;
prior packets unchanged and whitespace clean. Semantic comparisons are
same-context observations in semantic-evidence.md, not independent verification.
