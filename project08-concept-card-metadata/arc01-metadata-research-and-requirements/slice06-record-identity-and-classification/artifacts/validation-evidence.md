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
git -C .worktrees/planning diff --exit-code 285933a6 e88e6c0b -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families
git -C .worktrees/planning diff --check
~~~

Executed results: both jq assertions returned true; every registered input hash
reported OK; the preservation and whitespace checks exited 0 without output.
The historical 285933a6 comparison intentionally excludes this slice.
CDC pinned its endpoint to reviewed delivery e88e6c0b during closure, so later
authorized parent-plan updates do not invalidate historical preservation replay.
It detects alterations to Slice01/Slice04 within the reviewed delivery interval,
not all future edits.
The checks do not establish semantic correctness or independent verification.

Iteration 02 additionally ran the frozen-inventory per-corpus query: it groups
records by Complete Musician/Erlang path root and emits each field's presence,
JSON types, distinct values and value/frequency list. It returned 390 + 1,664
= 2,054, with all keys present and only Erlang subcategory having 80 nulls.

## CDC-Authored Literal Census Replay

Added by CDC on 2026-09-13 after reviewing `e88e6c0b`. CC supplied the
analysis and the query summary above, but omitted the literal command. This
section supplies and independently tests that missing documentation; CDC also
pinned the historical preservation comparison above to the reviewed commit. It does
not retroactively attribute this command to CC or alter the captured census.
Run from the same source-root cwd. Output is the complete per-corpus,
per-field raw vocabulary/frequency list, including JSON null; no output file
or helper is required.

~~~bash
set -eu
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
jq -e '[.records[] | select(.path|startswith("/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/") or startswith("knowledge/erlang/concept-cards/")) | . + {corpus:(if (.path|startswith("knowledge/erlang/")) then "erlang" else "music" end)}] |
group_by(.corpus) | map(. as $r | {corpus:.[0].corpus,records:length,fields:(["category","subcategory","tier"]|map(. as $f | {field:$f,present:([$r[]|select(.values|has($f))]|length),missing:([$r[]|select(.values|has($f)|not)]|length),types:([$r[]|select(.values|has($f))|.values[$f]|type]|group_by(.)|map({type:.[0],count:length})),values:([$r[]|select(.values|has($f))|.values[$f]]|group_by(.)|map({value:.[0],count:length}))}))}) |
. as $report |
if (map(.records)|add)==2054 and map(.corpus)==["erlang","music"] and
.[0].records==1664 and .[1].records==390 and all(.[]; .records as $n | all(.fields[]; .present==$n and .missing==0 and ([.values[].count]|add)==$n))
then $report else error("classification coverage or frequency mismatch") end' "$i"
~~~

CDC result: exit 0. Music: 390 records; category/subcategory/tier distinct
counts 10/67/3, all strings. Erlang: 1,664 records; distinct counts 16/341/3;
subcategory has 1,584 strings and 80 nulls; category/tier are strings.
Every key is present, and every frequency sum equals its corpus count.
Tier counts match the semantic report: music advanced/foundational/intermediate
141/79/170; Erlang 330/403/931. These are summaries of actual output.
