# CDC Verification: Slice07

Reviewed CC commit `d8a3a6c0` on 2026-09-13 against the unchanged twenty-pair
scope and seven criteria. **Changes required; Slice07 does not close.**
This is independent CDC review, not an amendment to CC's original attestation.

## Findings

### S7-R1: Field Meanings Remain Generic (Serious)

`artifacts/semantic-membership.json:36-230` has twenty meaning IDs but just
two definition patterns: seven "source attribution or coordinate metadata"
sentences and thirteen "one locator component" sentences. Dispositions also
repeat by group. Field substitution does not deliver the required meanings
or old/current lookup and preservation consequences (S7-4/S7-5).

For example, line 95 describes `mapping_evidence_refs` as addressing a
source/snapshot/resource position. The source-locator template's **Original
And Prepared Mapping** instead calls for evidence of counterpart correspondence.
`range_convention` (line 154) describes endpoint interpretation, not another
address; `numbering_basis` concerns base/sequence. Source identity, snapshot,
resource, representation, kind/value, contextual hints and prepared provenance
also require distinct explanations. The legacy sentence does not even
distinguish author attribution from chapter ordinal.

Correct each meaning/disposition with inspected, field-specific evidence and
an operational consequence. Do not invent a schema, parser or populated record
to cover a limitation. Shared cautions may remain shared.

### S7-R2: Required Contextual Comparisons Are Missing (Serious)

The five registered inputs at `semantic-membership.json:4-34` cover one
music card, the locator template, two guides and one Arc07 card's references.
`semantic-evidence.md:3-17` does not supply the required frozen census,
Erlang/source-family differences, historical Provenance/predecessor comparison,
concrete PDF basis case, or populated locator-map inspection (S7-1/S7-3/S7-4).

CDC's frozen census check finds 390 music and 1,664 Erlang records. Music
`pdf_page` is numeric in all 390; Erlang has 224 numeric and 1,440 null.
Erlang `chapter_number` has 1,108 numeric and 556 null; `section` is null
in 48 music and 13 Erlang records. These are observed shapes, not proof of
inapplicability or format. Accent Types alone cannot establish those contexts.

Existing bounded evidence is available without a new extraction:
- `knowledge/document-extraction/examples/pdf-marker-handoff.md`, **Locators**:
  P-L1 converter index with unknown base, P-L2 physical PDF page 2, P-L3
  printed label 1 and P-L4 output lines 13-20; P-M1 is a bounded mapping.
- `knowledge/document-extraction/examples/epub-pandoc-handoff.md`, **Locators**:
  resource-scoped anchor E-L1, conversion/output ranges E-L2/E-L3 and E-M1/E-M2.
  Both examples are synthetic conventions, not successful real conversions.
- Project05 Arc07 Slice02 `artifacts/locator-map.md`: actual generated map
  with snapshot/resource, heading and one-based inclusive source ranges.
  `loc-ch01-emergence` identifies chapter-01.md lines 53-57. Inspect the map,
  not just a card's references; an external map is not populated standalone
  source-locator frontmatter or independently verified claim support.

Register and inspect the relevant evidence, including exact sections used.
The template evidence currently names only **Source Identity And Address**,
although original/prepared mapping and preservation claims need other sections.
Name unavailable original-source or reference resolution evidence honestly.

### S7-R3: Replay And Closeout Are Incomplete (Correctness-Grade)

`artifacts/validation-evidence.md:5-13` passes its length/reference/hash
checks but omits exact-set comparison, uniqueness, inventory inclusion,
accepted-pair disjointness and census commands. CDC independently reproduces
the set checks; this does not make the missing CC replay present.

`closing-report.md:3-8` groups all seven rows into one attestation instead
of walking each criterion and comparing delivered scope to required scope.
The four artifacts are not individually inventoried. `artifacts/handoff.md`
retains the count but supplies no concrete remaining questions or sizing
consequences. Complete these deliverables under S7-6. Pin both endpoints of
historical preservation comparisons so later authorized review edits do not
invalidate their meaning.

## Independently Reproduced Checks

The CC replay ran literally from the source root: reference assertion true,
five hashes OK, prior packets unchanged and whitespace clean.
The following additional CDC route ran from the same cwd:

~~~bash
set -eu
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice07-source-identity-and-locator-semantics"
expected=$(awk -F '|' '/^\| `/ {gsub(/[` ]/, "", $2); gsub(/[` ]/, "", $3); print $2 "\t" $3}' "$s/slice-plan.md" | jq -Rsc 'split("\n") | map(select(length>0) | split("\t"))')
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
  ($actual-($actual-$accepted)|length)==0'
jq '[.records[] | select(.path|test("concept-cards/complete-musician/|knowledge/erlang/concept-cards/"))]
  | group_by(if (.path|contains("complete-musician")) then "music" else "erlang" end)
  | map({corpus:(.[0].path|if contains("complete-musician") then "music" else "erlang" end),
    count:length, fields:([ "pdf_page","chapter_number","section" ] as $fields |
      . as $records | $fields | map(. as $f | {field:$f,
        shapes:([$records[] | if (.values|has($f)) then .shapes.mapping[$f] else "ABSENT" end]
          | group_by(.) | map({shape:.[0],count:length}))}))})' \
  "$a/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json"
git -C .worktrees/planning diff --exit-code 1bacd954 d8a3a6c0 -- \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification
git -C .worktrees/planning diff-tree --no-commit-id --name-only -r d8a3a6c0
git -C .worktrees/planning show --check d8a3a6c0
git status --short
~~~

Results: exact twenty unique pairs, all in the frozen inventory, no overlap
with the accepted 47; true. Census results as above. Prior-packet diff empty;
six authorized CC paths only; commit whitespace clean; source status empty at
`e763c661`. No source/package/install gate was needed for this planning-only
delivery. Structural checks do not independently establish semantic adequacy.

## Seven-Row Walk

| Row | CDC disposition | Evidence |
| --- | --- | --- |
| S7-1 | open | S7-R2; five identities/hashes resolve, required contexts absent |
| S7-2 | done, reproduced | Exact-set, uniqueness, frozen inclusion and disjointness above |
| S7-3 | open | S7-R2; census and source-family/body comparison absent |
| S7-4 | open | S7-R1/R2; per-field and concrete locator meanings incomplete |
| S7-5 | open | S7-R1/R2; generic dispositions do not demonstrate consequences |
| S7-6 | open | S7-R3; replay, row walk and handoff incomplete |
| S7-7 | done, reproduced | Six-file commit, preserved inputs/source and whitespace checks |

## Bubble-Up And Next Work

The four named CC artifacts exist; presence is not completion of the promised
comparison. Exact scope and address-versus-support cautions worked. Missing
semantic content and replay are corrections within this slice, not accepted
deferrals, new memberships or grounds to reopen accepted Slice06.

Open Slice07 Iteration 01 using `artifacts/iteration-01-cc-prompt.md`.
Arc01's route changes from initial execution to correction; no new slice opens.
The 47 accepted / 20 assigned / 488 other pairs, parent integration/research
gates and Project08 P-14 Complete Musician trial requirement remain unchanged.
