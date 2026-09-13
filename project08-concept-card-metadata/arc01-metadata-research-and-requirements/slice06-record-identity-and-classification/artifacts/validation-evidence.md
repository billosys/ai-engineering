# Slice06 Validation Evidence

Declared cwd: /Users/oubiwann/lab/billosys/ai-engineering. These are
same-context structural checks; semantic observations are in semantic-evidence.md.

~~~bash
set -eu
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice06-record-identity-and-classification"
i="$a/slice01-metadata-inventory-and-research-questions"
b="$a/slice04-semantic-identity-source-and-graph-families"

jq -e '.evidence as $e | .meanings as $m |
  (.memberships|length)==37 and
  all(.memberships[]; ($m[.meaning_id] != null) and
    all(.evidence_ids[]; $e[.] != null) and (.disposition|type)=="string" and
    (.disposition|length)>0) and
  all(.meanings[]; all(.evidence_ids[]; $e[.] != null))' "$s/artifacts/semantic-membership.json"

jq -en --slurpfile i "$i/artifacts/field-dispositions.json" --slurpfile s "$s/artifacts/semantic-membership.json" --slurpfile b "$b/artifacts/batch01-identity-membership.json" '
  ([$i[0].field_paths[] | .field_path as $p | .record_kinds[] |
    select((($p=="id" or $p=="revision") and .!="concept-card") or $p=="record_type" or
      (($p=="category" or $p=="subcategory" or $p=="tier") and .=="untyped")) | [$p,.]] | sort) as $expected |
  ([$s[0].memberships[]|[.field_path,.record_kind]]|sort) as $actual |
  ([$b[0].memberships[]|[.field_path,.record_kind]]) as $batch |
  ($expected|length)==37 and $expected==$actual and ($actual|unique|length)==37 and
  ($actual-($actual-$batch)|length)==0'

jq -r '.evidence[] | [.sha256,.path] | join("  ")' "$s/artifacts/semantic-membership.json" | shasum -a 256 -c -
git -C .worktrees/planning diff --exit-code 285933a6 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families
git -C .worktrees/planning diff --check
~~~

Executed results: both jq assertions returned true; every registered input hash
reported OK; the preservation and whitespace checks exited 0 without output.
The historical 285933a6 comparison intentionally excludes this slice, so it
detects any alteration to Slice01/Slice04 packets since the pre-delivery base.
The checks do not establish semantic correctness or independent verification.
