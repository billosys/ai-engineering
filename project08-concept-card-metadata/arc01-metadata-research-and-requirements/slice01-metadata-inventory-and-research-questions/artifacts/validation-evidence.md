# Validation Evidence

## Iteration 01 reproducible route

Run from `/Users/oubiwann/lab/billosys/ai-engineering` with
`slice_dir=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions`.

```sh
fennel --version
perl -MYAML::XS -MJSON::PP -MDigest::SHA -e 'print "$YAML::XS::VERSION $JSON::PP::VERSION\n"'
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" /private/tmp/run1.json <the nine roots from input-register.md>
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" /private/tmp/run2.json <the same nine roots>
cmp /private/tmp/run1.json /private/tmp/run2.json
jq '[.records[].keys // []] | add | unique | length' /private/tmp/run1.json
jq '[.records[] | select(.values.record_type) | .values.record_type] | group_by(.) | map({kind:.[0],count:length})' /private/tmp/run1.json
shasum -a 256 -c "$slice_dir/artifacts/baseline-snapshots/source-sha256sums.txt" "$slice_dir/artifacts/baseline-snapshots/copy-sha256sums.txt"
git -C /private/tmp/project05-compcogneuro-book-e0c697b4 rev-parse HEAD
git -C /private/tmp/project05-compcogneuro-book-e0c697b4 status --short
```

Observed exit status was 0 for every command; Fennel 1.6.1/Lua 5.5,
YAML::XS 0.82 and JSON::PP 4.06 produced 2,124 files, 2,106 parsed mappings,
52 typed records, 31 concept cards and 169 top-level keys. The fixture command
also reports malformed/non-mapping/empty/unterminated/missing-root conditions.

| Check | Attested result |
| --- | --- |
| `make help` | Passed; confirmed repository Make targets. No source/package gate applies to this planning/evidence-only slice. |
| Worktree/revision check | Source main was `e763c661`; planning was `03c5b207` before slice writes. |
| Ruby Psych inventory | 2,106 of 2,124 Markdown files parsed; 15 no-frontmatter files and three exact YAML failures reported. |
| Field-union reproduction | 2,054 legacy records: Complete Musician 390, Erlang 1,664. `extends` absent on 66; all other legacy-profile fields occur on 2,054. |
| Baseline preservation | Two SHA-256 manifests cover 27 files; normalized comparison returned `byte-identical file manifest: 27 files`. |
| Representative review | Read legacy music/Erlang cards, Arc07 candidates, rich/teaching candidates, current template/example/reference groups, both v3.2 prompts and v3.1 predecessors. |

## Limits

- YAML parsing establishes syntax and shapes only, not support, resolved refs,
  body quality or graph behavior.
- The `/private/tmp/project05-compcogneuro-book-e0c697b4` source snapshot is
  unavailable; candidate line locators were not rechecked.
- Complete Musician was not copied; it remains a revision-pinned external input.
- Invalid rich candidates were preserved, not repaired.

Final hygiene results, the exact artifact inventory and the final worktree state
are recorded in `../closing-report.md` after those artifacts are complete.
