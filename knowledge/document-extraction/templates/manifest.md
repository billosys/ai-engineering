# Preparation Manifest Template

Copy into the accepted evidence home and replace angle-bracket placeholders.
These are fillable records, not an executable schema. Use explicit unknown,
not checked, or not applicable with a reason; never leave a blank that could
mean success. Keep stable IDs and file/section references across records.
Combine records in one report when useful. Follow the
[output contract](../guides/03-output-contract.md) and
[reporting guide](../guides/10-validation-and-reports.md).

Human-assisted: name the operator behind supplied observations; if returning
text only, mark storage unverified. Agent-direct: save, reopen, and follow the
record references against the identified snapshot. Both modes support
standalone indexing, reading, source review, and analysis; concept-card work
is optional. See the [PDF example](../examples/pdf-marker-handoff.md).

## Identity And Requested Work

| Field | Value |
| --- | --- |
| Manifest ID / source ID | <manifest-id> / <source-id> |
| Source title, author, edition and identity evidence | <observed values or unknown; evidence pointer> |
| Preserved input snapshot / conversion snapshot | <input-id> / <conversion-id or unavailable> |
| Prepared snapshot / run ID / preceding run | <prepared-id> / <run-id> / <prior record or first run> |
| Run date / preparer / operating mode | <date and timezone> / <actor> / <human-assisted or agent-direct> |
| Requested uses and full requested scope | <consumer, purpose, content range, required properties> |
| Workspace root / path convention / evidence home | <absolute root; how relative paths resolve; evidence directory> |
| Record storage and reference check | <saved path and observed check, or draft storage unverified> |

## Preserved Inputs And Lineage

Repeat for raw sources, captures, unmodified conversion files, metadata, and
assets. Inventory a directory through an attached enumerated listing, not an
unexamined wildcard. Missing originals need a caveat.

| Input ID / snapshot | Role / format | Preserved path or URI | Capture or conversion lineage | Checksum / method | Availability / caveat |
| --- | --- | --- | --- | --- | --- |
| <id / snapshot> | <raw, rendered DOM, conversion, metadata, asset; format> | <path; URL alone does not identify bytes> | <capture time/state/method; tool and version; actual command/settings or reported/unknown> | <digest and algorithm or unavailable reason> | <observed, operator-reported, missing; caveat ID> |

## Derived Inventory And Transformations

| Output ID / prepared snapshot | Path / role | Reading order / section IDs | Input spans / locator IDs | Transformations / evidence |
| --- | --- | --- | --- | --- |
| <id / snapshot> | <file; Markdown, media, sidecar> | <order and IDs or not applicable> | <input IDs and typed locations> | <conversion, split, path rewrite, manual edit; exact rule and record> |

Record generated headers and their line effects, omissions, corrections, and
unchanged copies. Separate actual commands/results from proposed commands.
Record regeneration destination, comparison scope/result, naming/map reuse,
and any untested repeatability: <details and evidence>.

## Record Register And Handoff

| Category | Record ID / path or section | Same source / snapshot / run verified by |
| --- | --- | --- |
| Structure | <structure-map reference> | <check/evidence> |
| Media | <media-report reference or scoped no-media observation> | <check/evidence> |
| Locators | <locator-map reference> | <check/evidence> |
| Validation and per-use readiness | <validation-readiness reference> | <check/evidence> |
| Caveats | <record references or explicit scoped none found> | <check/evidence> |
| Optional concept-card handoff | <reference or not requested> | <check/evidence or not applicable> |

Final handoff: <prepared locations, reading order, per-use decisions, blocking
caveat IDs, next actions, and recipient>. Do not infer readiness from a filled
manifest. Use the [readiness template](./validation-readiness.md).
