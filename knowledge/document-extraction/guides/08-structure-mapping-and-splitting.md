# Structure Mapping And Splitting

Use this guide to turn an inspected document into an ordered section map and,
where justified, complete split files. Standalone indexing, reading, source
review, and analysis use this map independently of `concept-cards`, which can
consume it as upstream provenance. Apply the [output contract](./03-output-contract.md)
without treating a split as mandatory for every source.

## Build The Section Inventory

Preserve raw and converted inputs and identify the snapshot being mapped.
Inspect actual body boundaries alongside available PDF metadata, EPUB
navigation, HTML resource structure, or Markdown headings. None is infallible.
For each candidate section, record a stable ID, title, original label, parent,
reading order, input start/end locators, boundary evidence/status, proposed
output, and caveats. Keep inferred boundaries distinguishable from verified
ones. Use the [locator model](./09-locator-model.md) for typed locations.

Account for title/cover matter, inline contents, prefaces, numbered chapters,
parts, appendices, unnumbered sections, references, notes, and back matter.
Distinguish a TOC occurrence from its body target. Duplicate headings need
resource/anchor identity or hierarchy and order; title text alone cannot
select a unique split point. Preserve original labels even when they are not
numeric or differ from filename order.

List unmatched navigation entries, missing body sections, and additional body
content. Counts help reconcile the map but cannot establish completeness:
TOCs may contain multiple levels or omit unnumbered material. Give every
retained input span a destination and explicitly justify exclusions.

## Choose Complete Units

Inspect both sides of each proposed boundary. Keep code fences, nested divs,
raw HTML/SVG, tables, lists, block quotes, and other spanning containers intact.
Preserve anchors attached before a heading and definitions needed by the
section. A heading inside a container is not automatically a safe cut point.

Track cross-section links, footnotes, media references, and shared definitions.
Choose a larger intact unit or retain the monolith when dependencies cannot
be represented faithfully within the preparation scope. A structure-aware
rewrite may be appropriate when authorized, but must retain original spans,
record changes, and validate resulting dependencies; silently deleting a
wrapper or note to permit a split is not a repair.

Write an ordered span map before generating files. Specify start/end line
conventions or other boundaries explicitly. Check for unintended gaps,
overlap, reordering, or duplication. Front/back matter belongs in that map,
not in an unexamined remainder discarded after the last chapter.

## Names And Metadata

Use stable order-plus-slug filenames appropriate to the accepted output layout.
Keep the original title in metadata; shortening or transliteration for a
filesystem must not replace the author's title. Check collisions after
normalization/truncation, including duplicate titles and case-insensitive
filesystems. Persist the selected ID-to-filename mapping for regeneration;
adding one section should not silently repoint old provenance to new content.

Use embedded metadata or a linked sidecar containing source/snapshot/run IDs,
section identity, title and original label, parent/order, input span, output
path, and locator/manifest/caveat references. Keep original source metadata
distinct from generated fields. Serialize embedded YAML safely and record
its effect on output line positions. Book front matter and YAML frontmatter
are different things; preserve both where present.

## Human-Assisted Operation

Ask for the ordered heading/navigation inventory plus excerpts immediately
before and after disputed boundaries, including enclosing markup and anchors.
For duplicate titles, request resource paths or surrounding section context.
Ask the operator to inspect one proposed unit with its dependencies before
recommending a larger batch of splits under the same rule.

Return candidate boundaries, unresolved alternatives, and the content that
must stay together. Label observations as operator-reported and identify
missing full-document coverage rather than claiming a complete inventory
from a few excerpts.

## Agent-Direct Operation

Read accessible input and navigation/metadata; build the ordered span map and
inspect complete container boundaries. Generate into a fresh derived directory
or distinct run home, preserving originals and prior snapshots. Use existing
tools only after checking their boundary and metadata assumptions.

Compare each generated body with its mapped input span, accounting for named
normalizations and generated metadata. Reconcile section order/count, inspect
starts and ends, and check that all retained content appears as intended.
Validate cross-file anchors and definitions, then apply
[media validation](./07-media-path-normalization.md) from each output location.
Stop an ambiguous split while continuing independent, verified units.

## Regeneration And Reporting

Keep the boundary rules, accepted map, output-name assignments, and manual
decisions with the manifest. Regenerate from the preserved snapshot and compare
inventories, bodies, and mappings. Preserve earlier mappings when content or
settings change; reusing a filename does not prove that it identifies the same
span. Report intentional changes rather than silently shifting line locators.

Send unresolved boundaries, missing sections, unsupported containers, broken
dependencies, and coverage limits to the
[validation/readiness report](./10-validation-and-reports.md). A retained
monolith can be ready for reading while chapter-based indexing remains blocked.
An apparently tidy set of files is not evidence that source structure or
content was preserved.
