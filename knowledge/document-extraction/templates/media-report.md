# Media Record And Report Template

Use the [media guide](../guides/07-media-path-normalization.md). Keep reference
and asset inventories separate: a reference can be missing, and a captured
asset can be unreferenced. See the [EPUB example](../examples/epub-pandoc-handoff.md)
for a nested path after splitting.

## Context

- Report ID / manifest: <id / reference>.
- Source / input snapshot / prepared snapshot / run: <IDs>.
- Path root / inspected syntax and file scope: <root; Markdown, HTML, SVG,
  srcset, CSS or other observed mechanisms; unchecked mechanisms>.
- Observer / evidence kind and record: <direct, operator-reported, inferred>.

## Assets

| Asset ID | Original full resource identity / snapshot | Preserved path | Derived path | Format / size / checksum | Dependencies / observation / caveat |
| --- | --- | --- | --- | --- | --- |
| <id> | <full archive path, local path, or URI; snapshot> | <path or not captured> | <path or unchanged/not copied> | <observed values or unknown reasons> | <SVG/CSS dependencies, unreferenced/duplicate/corrupt/unchecked; evidence and IDs> |

## References

Repeat for each occurrence, including separate srcset candidates and their
descriptors. Do not deduplicate merely by basename.

| Field | Value |
| --- | --- |
| Reference ID / containing input file and snapshot | <id / file / snapshot> |
| Original syntax / exact target / locator | <verbatim syntax including alt/title/attributes; location> |
| Kind / original resolution base | <local, remote, data, fragment, other; actual directory/base URL> |
| Resolved original resource / asset ID | <full identity; linked asset or unresolved candidates> |
| Final containing file / prepared snapshot | <path / snapshot> |
| Emitted target / resolved destination | <relative target from that file / full path or URI> |
| Preserved attributes / target-only changes | <alt, title, IDs, dimensions, candidate descriptors, fragments; explicit changes> |
| Disposition | <changed, unchanged, missing, remote, embedded, ambiguous, unchecked> |
| Existence / identity / appearance checks | <separate outcomes, methods, scopes and evidence; not checked where unavailable> |
| Caveat IDs / next action | <IDs and bounded check> |

## Reconciliation

- Enumerated references: <total and counts by mutually exclusive disposition;
  additional quality flags separately>. Assets: <total, referenced, unreferenced>.
- After-split resolution: <all output references or exact sample; outcome/evidence>.
- Definitions, fragments, encoding and dependencies: <checked scope; gaps>.
- Collision handling: <full-identity decisions; no overwrites; unresolved alternatives>.
- Regeneration: <fresh-input mapping; unchanged references remain unchanged;
  no accumulating prefixes or assets; comparison evidence or untested>.
- Empty inventory if applicable: <what was inspected, how, and why no media
  was found; not a substitute for uninspected content>.
- Readiness effects: <use, affected spans, caveats and report reference>.

Path resolution does not establish visual equivalence or source fidelity.
Retain uncaptured remote references without pretending they are local assets.
