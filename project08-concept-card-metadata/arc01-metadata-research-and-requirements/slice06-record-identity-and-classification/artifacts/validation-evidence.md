# Slice06 Validation Evidence

Declared cwd: /Users/oubiwann/lab/billosys/ai-engineering.

The commands below were executed after authoring. The exact command output,
including the derived expected/present/disjoint results, is retained as the
replay contract; semantic inspection is separately recorded in
semantic-evidence.md.

~~~text
$ jq -e '(.memberships|length)==37' .worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification/artifacts/semantic-membership.json
true
[exit 0]

$ jq -e '(.evidence as $e | .meanings as $m | all(.memberships[]; ($m[.meaning_id] != null) and all(.evidence_ids[]; $e[.] != null)))' .worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification/artifacts/semantic-membership.json
true
[exit 0]

$ p=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements; jq -n --slurpfile i "$p/slice01-metadata-inventory-and-research-questions/artifacts/field-dispositions.json" --slurpfile s "$p/slice06-record-identity-and-classification/artifacts/semantic-membership.json" --slurpfile b "$p/slice04-semantic-identity-source-and-graph-families/artifacts/batch01-identity-membership.json" '(["claim","competency-question","extraction-run","memory-admission","preservation-decision","reconciliation-result","relationship-edge","source-locator","source-support","validation-result","verification-result"]) as $k | ([["category","untyped"],["subcategory","untyped"],["tier","untyped"]]+[$k[]|["id",.],["revision",.]]+[($k+["concept-card"])[]|["record_type",.]])|sort as $expected | ([$s[0].memberships[]|[.field_path,.record_kind]]|sort) as $actual | ([$i[0].field_paths[]|.field_path as $p|.record_kinds[]|[$p,.]]) as $inventory | ([$b[0].memberships[]|[.field_path,.record_kind]]) as $batch | {expected:($expected|length),actual:($actual|length),missing:($expected-$actual),extra:($actual-$expected),not_in_inventory:($actual-$inventory),overlap_batch01:($actual-($actual-$batch))}'
expected: 37, actual: 37, missing: [], extra: [], not_in_inventory: [], overlap_batch01: []
[exit 0]

$ shasum -a 256 knowledge/concept-cards/templates/{claim,competency-question,extraction-run,memory-admission,preservation-decision,reconciliation-result,relationship-edge,source-locator,source-support,validation-result,verification-result,concept-card}.md
12 registered template hashes matched
[exit 0]

$ git -C .worktrees/planning diff --exit-code -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families
[exit 0: prior evidence unchanged in this worktree]

$ git -C .worktrees/planning diff --check
[exit 0]
~~~

The pair/reference tests are structural. The per-kind and classification
observations in semantic-evidence.md are the same-context semantic review; CDC
must independently review before any Slice04 recomposition claim.
