# Metadata Inventory

Fresh Fennel/YAML::XS census: 2,124 Markdown files; 2,106 parsed mapping
frontmatters; 15 no-frontmatter files; and three preserved rich-rerun YAML
failures caused by unquoted colon-bearing titles. Two unchanged-input runs were
byte-identical.

| Population | Files | Parsed mappings | Interpretation |
| --- | ---: | ---: | --- |
| Complete Musician | 390 | 390 | Legacy cards. |
| Wider Erlang | 1,664 | 1,664 | Legacy cards; includes 224-file `design-scale-erlang-otp/` subset. |
| Arc07 candidates | 16 | 14 | Ten cards, four supports, two READMEs. |
| Rich / teaching workbench | 27 | 17 | Rich: 7 structured, 4 prose, 3 malformed; teaching: 10 structured, 3 prose. |
| Templates/examples/references | 27 | 21 | 12 templates, 9 synthetic examples, 6 prose references. |

There are 52 typed records: 31 concept-card, 5 source-support, 3 extraction-run,
2 each CQ/memory-admission/reconciliation-result/relationship-edge, and one each
claim/preservation-decision/source-locator/validation-result/verification-result.
These include templates/examples and are not real-extraction card totals.

The inventory has 169 distinct top-level keys and 308 normalized field paths.
Arrays use `[]`, while the array container, every member path, null, false and
empty values remain present in the index. `field-dispositions.json` mechanically
covers every path, records typed values/shapes and context evidence, and assigns
an observed meaning/disposition plus a field-specific query consequence. The
readable crosswalk remains the semantic synthesis; Arc02 still chooses no schema.
