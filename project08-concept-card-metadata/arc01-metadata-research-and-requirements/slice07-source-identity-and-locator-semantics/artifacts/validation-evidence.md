# Slice07 Validation Evidence

Declared cwd: /Users/oubiwann/lab/billosys/ai-engineering. The following
literal commands are the CC replay for this packet. The expected table is
derived independently from slice-plan.md; no registry values seed it.

~~~bash
set -eu
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice07-source-identity-and-locator-semantics"
expected=$(awk -F '|' '/^\| \x60/ {gsub(/[\x60 ]/, "", $2); gsub(/[\x60 ]/, "", $3); print $2 "\t" $3}' "$s/slice-plan.md" | jq -Rsc 'split("\n") | map(select(length>0) | split("\t"))')
jq -en --argjson expected "$expected" \
  --slurpfile s "$s/artifacts/semantic-membership.json" \
  --slurpfile i "$a/slice01-metadata-inventory-and-research-questions/artifacts/field-dispositions.json" \
  --slurpfile b "$a/slice04-semantic-identity-source-and-graph-families/artifacts/batch01-identity-membership.json" \
  --slurpfile six "$a/slice06-record-identity-and-classification/artifacts/semantic-membership.json" '
  ([$s[0].memberships[] | [.field_path,.record_kind]] | sort) as $actual |
  ([$i[0].field_paths[] | .field_path as $p | .record_kinds[] | [$p,.]]) as $inventory |
  ([$b[0].memberships[], $six[0].memberships[] | [.field_path,.record_kind]]) as $accepted |
  ($expected | sort)==$actual and ($actual|length)==20 and
  ($actual|unique|length)==20 and ($actual-$inventory|length)==0 and
  ($actual-$accepted|length)==20'
jq -e '(.memberships|length)==20 and
  (.evidence as $e | .meanings as $m |
   all(.memberships[];
     $m[.meaning_id] != null and
     .evidence_ids == $m[.meaning_id].evidence_ids and
     .disposition == $m[.meaning_id].disposition and
     all(.evidence_ids[]; $e[.] != null)) and
   all(.meanings[]; all(.evidence_ids[]; $e[.] != null)))' \
  "$s/artifacts/semantic-membership.json"
jq -r '.evidence[] | [.sha256,.path] | join("  ")' \
  "$s/artifacts/semantic-membership.json" | shasum -a 256 -c -
jq '[.records[] | select(.path|test("concept-cards/complete-musician/|knowledge/erlang/concept-cards/")) | . + {corpus:(if (.path|contains("complete-musician/")) then "music" else "erlang" end)}]
  | group_by(.corpus)
  | map(. as $r | {corpus:$r[0].corpus,total:($r|length),
    fields:(["authors","chapter_number","chapter","pdf_page","section","source_slug","source"]
      | map(. as $f | {field:$f,present:([$r[]|select(.values|has($f))]|length),
        shapes:([$r[]|if (.values|has($f)) then .shapes.mapping[$f] else "ABSENT" end]
          | group_by(.) | map({shape:.[0],count:length}))}))})' \
  "$a/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json"
git -C .worktrees/planning diff --exit-code 1bacd954 08d682b0 -- \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification
git -C .worktrees/planning diff --exit-code 08d682b0 -- \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification
git -C .worktrees/planning diff --check
git status --short
~~~

Executed results: expected-table equality, length, uniqueness, frozen inventory
inclusion, and accepted-47 disjointness returned true. Both evidence layers
resolved and every registered hash returned OK. The full census produced the
two seven-field families summarized in semantic-evidence.md. The historical
preservation comparison is pinned from 1bacd954 to 08d682b0, and the separate
current-status comparison against 08d682b0 is empty for Slice01, Slice04, and
Slice06. Whitespace is clean. The final status listing is the six authorized
Slice07 files until this commit is made; the source worktree remains unchanged.
These are CC-executed checks, not a replacement for CDC reproduction.
