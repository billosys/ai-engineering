# Validation Evidence — Iteration 02

Run from `/Users/oubiwann/lab/billosys/ai-engineering`.

```sh
slice_dir=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions
fennel --version
perl -MYAML::XS -MJSON::PP -e 'print "YAML::XS=$YAML::XS::VERSION JSON::PP=$JSON::PP::VERSION\n"'
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" --field-index /private/tmp/project08-i02-fixture-index.json /private/tmp/project08-i02-fixture.json "$slice_dir/artifacts/cdc-type-probes" "$slice_dir/artifacts/inventory-fixtures" /private/tmp/project08-missing-root
jq -e '[.records[] | select(.path | endswith("types.md")) | .values] | .[0] | (.truth == true and .falsehood == false and .one == 1 and .zero == 0 and .text_one == "1" and .empty_text == "" and .null_value == null and .items[0].id == null)' /private/tmp/project08-i02-fixture.json
jq -e '[.field_paths[].field_path] | (index("items[].id") and index("items[].refs") and index("empty_list") and index("truth"))' /private/tmp/project08-i02-fixture-index.json
mapfile -t roots <<'EOF'
/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician
knowledge/erlang/concept-cards
.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards
.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards
workbench/compcogneuro-rich-rerun-2026-09-12
workbench/compcogneuro-teaching-rerun-2026-09-12
knowledge/concept-cards/templates
knowledge/concept-cards/examples
knowledge/concept-cards/references
EOF
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" --field-index /private/tmp/project08-i02-index-a.json /private/tmp/project08-i02-a.json "${roots[@]}"
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" --field-index /private/tmp/project08-i02-index-b.json /private/tmp/project08-i02-b.json "${roots[@]}"
cmp /private/tmp/project08-i02-a.json /private/tmp/project08-i02-b.json
cmp /private/tmp/project08-i02-index-a.json /private/tmp/project08-i02-index-b.json
jq -e '[.records[] | select(.frontmatter) | .values | paths | select(.[-1] | type == "string") | map(if type == "number" then "[]" else . end) | join(".")] | unique as $expected | [.field_paths[].field_path] | unique as $actual | {missing: ($expected - $actual), extraneous: ($actual - $expected)} | (.missing == [] and .extraneous == [])' "$slice_dir/artifacts/field-dispositions.json"
shasum -a 256 -c "$slice_dir/artifacts/baseline-snapshots/source-sha256sums.txt" "$slice_dir/artifacts/baseline-snapshots/copy-sha256sums.txt"
git -C /private/tmp/project05-compcogneuro-book-e0c697b4 rev-parse HEAD
git -C /private/tmp/project05-compcogneuro-book-e0c697b4 status --short
git diff --check
git -C .worktrees/planning diff --check
```

Observed on 2026-09-12: Fennel 1.6.1 on Lua 5.5, YAML::XS 0.82 and JSON::PP
4.06. The fixture assertion passed: booleans, numbers, quoted numeric strings,
empty text, nulls, empty maps/lists and nested mappings remain distinct. The
fixture reports malformed, non-mapping, unterminated and missing-root input
without crashing. The full census reports 2,124 files, 2,106 parsed mappings,
15 no-opening-frontmatter files and three preserved YAML failures; it has 169
top-level keys, 52 typed records and 308 normalized field paths. The current
CompCogNeuro checkout is present at `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d`.

The parser is a narrow YAML::XS bridge. It implements YAML 1.1-style implicit
typing, preserves JSON-compatible booleans/numbers/strings/nulls, renders
timestamps as strings, and does not retain explicit YAML tags. This is syntax
and representation evidence only; it is not semantic source verification.

## Iteration 03 focused regression evidence

The following was run in macOS `/bin/bash` 3.2 without `mapfile`:

```sh
probe_dir=$(mktemp -d /private/tmp/project08-i03.XXXXXX)
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" --field-index "$probe_dir/index.json" "$probe_dir/out.json" "$slice_dir/artifacts/cdc-edge-probes" "$slice_dir/artifacts/inventory-fixtures"
jq . "$probe_dir/out.json" >/dev/null
jq -e '[.records[] | {name:(.path|split("/")|last), frontmatter, error}] as $r | ($r|any(.name=="json-controls.md" and .frontmatter)) and ($r|any(.name=="blank-mapping.md" and .frontmatter)) and ($r|any(.name=="null-root.md" and .error=="null-frontmatter")) and ($r|any(.name=="empty.md" and .error=="empty-frontmatter")) and ($r|any(.name=="non-mapping.md" and .error=="non-mapping-frontmatter")) and ($r|any(.name=="unterminated.md" and .error=="unterminated-frontmatter"))' "$probe_dir/out.json"
```

Both commands exit 0. The JSON-control probe is parseable by `jq`; the valid
empty mapping is a mapping, while empty and null documents are separate
non-mapping classifications. The remaining R2 semantic-family annotation and
R4 complete literal nine-root recipe are not claimed complete by this focused
repair.
