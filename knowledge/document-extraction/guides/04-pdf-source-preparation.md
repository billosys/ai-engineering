# PDF Source Preparation

Use this guide for a PDF and its Marker-style conversion bundle when preparing
standalone indexing, reading, source review, analysis, or downstream
`concept-cards` provenance. Apply the [workflow](./02-workflow.md) and
[output contract](./03-output-contract.md) throughout. This guide supplies PDF
preparation decisions; it does not require a source-specific helper script.

## Inputs And Preservation

Locate the preserved raw PDF, converted Markdown (often `book.md`), converter
metadata (often `metadata.json`), and extracted assets (often `images/`). These
names describe the accepted bundle convention, not a guarantee about every
Marker release or wrapper. Inventory the actual files and record any wrapper
renaming or missing output. Use the workspace's accepted source layout; the
output contract provides a default.

Record the PDF identity and checksum when practical, conversion date, Marker
version, wrapper identity, command/settings, conversion page range, and any
reported OCR or model-assisted processing. Mark unavailable lineage as unknown;
do not reconstruct an invocation from output filenames. Keep raw PDF and
unmodified conversion text, metadata, and images intact. Normalize and split
derived copies in a separate destination, with source/snapshot/run identifiers.

If conversion has not happened, identify the missing inputs and the available
conversion workflow before proceeding. Do not treat this guide as evidence
that any particular converter invocation has been run or validated.

## First-Pass Inspection

Before changing text or paths:

1. Inspect the PDF's opening material, navigation or printed contents, several
   chapter starts, and representative pages with columns, tables, equations,
   and images. Record which portions were actually inspected and with what
   viewer/tool. If the PDF is unavailable, restrict conclusions to the bundle.
2. Read corresponding Markdown, including front/back matter, headings, image
   syntax, and text around apparent boundaries. Check for missing text,
   repeated page furniture, broken reading order, and conversion artifacts.
3. Inspect the metadata's actual schema. When `table_of_contents` exists,
   retain each candidate's title, level, order, raw `page_id`, and any location
   evidence. Record missing/empty metadata explicitly.
4. Inventory actual assets and reference forms, including nonempty alt text,
   reference-style images, and embedded HTML. Do not infer a PDF location or
   image identity solely from a `_page_` filename.

Marker documents computed TOC metadata with title, heading level, `page_id`,
and polygon fields. That makes it useful boundary evidence, not an infallible
copy of the author's structure. See [Marker metadata](https://github.com/datalab-to/marker#metadata)
and inspect the output of the installed version.

## Human-Assisted Operation

Ask for bounded observations that resolve the next decision: the bundle file
list, relevant TOC records, the Markdown around a proposed start, and the PDF
viewer's physical page position and displayed label for that same content.
Include the title or opening passage to match, rather than asking only whether
the page number looks correct. Have the operator check several separated
starts, especially around front-matter numbering changes and appendices.

Inspect those results before proposing a split or page interpretation. Record
operator-reported evidence separately from assistant-inspected evidence. If an
image match is unclear, request inspection of that particular asset and source
figure. Supply the intended manifest/report contents when unable to write
files; identify which writes and checks remain unverified.

## Agent-Direct Operation

Inspect accessible PDF pages, text, metadata, and assets with available tools,
then build the candidate map before editing derived files. Capture inspection
locations and command results. Use existing tools when they fit; inspect any
helper's assumptions before use rather than copying a source-specific heading
pattern. Do not execute conversion commands merely to compensate for unknown
lineage of an otherwise inspectable bundle.

Preserve inputs, apply only verified mappings to derived output, and re-open
the generated files for validation. When the environment cannot display the
PDF or an asset, record the missing fidelity check and switch that check to
human-assisted mode or leave the affected use blocked/caveated.

## Establish The PDF Page Basis

Keep converter identifiers, physical page positions, and document page labels
as separate values. Zero-based versus one-based describes an index convention;
physical-page-based versus document-label-based describes what is being
identified. They are not four interchangeable numbering schemes.

1. Retain the original metadata value unchanged. Inspect its type, range,
   page statistics, selected conversion range, and any converter documentation
   for the version used. A `page_id` of zero is a clue, not sufficient proof.
2. Match a candidate chapter's heading and opening content in the raw PDF.
   Record the physical index with an explicit base and the displayed/printed
   label separately. A Roman-numeral preface or restarted numbering must not
   be silently converted to an Arabic physical page number.
3. Repeat at several separated chapter starts, including numbering transitions
   and late material. Check that the proposed interpretation explains those
   observations. Distinguish original-PDF positions from positions within a
   converted subset; do not assume a global offset from a single match.
4. Record the mapping rule, check locations, coverage, and unresolved values.
   Apply a zero-to-one adjustment only to an index whose basis is verified.
   Do not flatten these fields into an unexplained `pdf_page` scalar.

When metadata and PDF content disagree, preserve both observations and stop
the affected page mapping. A Markdown line locator can remain usable if bound
to its snapshot, but it does not replace a verified PDF citation. Without raw
PDF access, label the page interpretation unverified and name the needed check.

## Map Structure And Choose Splits

Build an ordered map from TOC candidates to actual content spans in the
preserved Markdown snapshot. Include section identity, original title and
number/label if present, hierarchy, candidate PDF locator, Markdown start/end
lines and their base, proposed output filename, and boundary evidence/status.

Cross-check TOC entries against body headings and opening text. Printed or
converted TOC entries can repeat headings without starting a chapter. Parts,
appendices, prefaces, introductions, bibliography, index, unnumbered material,
and unusual headings such as an abstract require source-specific inspection.
Do not apply a single `Chapter N` pattern or a handbook-specific marker to all
books. Keep unmatched entries and unmatched body sections visible in the map.

If TOC metadata is absent or unusable, derive candidates from body structure
and verify against the PDF where possible. Record which decisions are inferred.
Do not invent missing page locators or discard front/back matter to force a
chapter count to equal the total TOC count; TOCs include multiple levels and
non-chapter entries.

Split only at justified boundaries that preserve complete content. Keep a
monolith or a larger intact section when a boundary is uncertain or cuts a
table, note, code fence, or other dependent block. Give every retained input
span one output destination; disclose omissions and intentional duplication.
Choose stable order-plus-slug names with collision checks, including after
truncation. Original titles and labels belong in metadata even if filenames
need shortening. Files default to the prepared-source directory itself under
the output contract, unless the accepted workspace layout says otherwise.

Each split file needs metadata or a linked sidecar recording source format,
source/snapshot/run identity, section title and order, original chapter label
when present, input Markdown span, PDF locator records with basis/status, and
manifest/caveat references. If using YAML frontmatter, serialize titles safely
and distinguish that generated metadata from the book's front matter. Retain
the original heading and content; document any normalization. Generated header
lines must not change the meaning of input-snapshot line locators.

## Normalize And Validate Images

Resolve each original reference against the conversion bundle before proposing
a replacement. A bare `_page_5_Picture_1.jpeg` may become
`./images/_page_5_Picture_1.jpeg` only when that asset exists at the mapped
location relative to the prepared file. Preserve alt text, titles, and relevant
attributes. Already-correct references should remain unchanged.

Check all observed reference forms rather than replacing only `![](_page_`.
Do not prefix paths twice, match solely by basename across ambiguous assets,
or rewrite remote/data references as local files. Record changed, unchanged,
unresolved, and unchecked references with their containing files. A file's
existence proves resolution; visual comparison to the PDF/caption supports
identity. Keep those checks distinct.

After splitting, resolve every local media reference from its containing
file's directory, including reference definitions used in that file. Inspect
representative figures against the PDF and report coverage. If an asset is
missing, damaged, or of uncertain identity, retain the uncertainty and stop
that replacement. Do not delete its reference or substitute a plausible image.

## Validate, Regenerate, And Report

Compare generated files with the mapped input spans for coverage and order,
including front/back matter and each accepted split. Counts are a consistency
check, not proof of content preservation. Inspect starts and ends, verify
metadata against the map, and report missing/extra sections or assets. Check
local links and note/reference targets affected by splitting as well as images.

Record OCR substitutions, lost symbols, equations, table cell/column order,
multi-column reading order, repeated headers/footers, cropped figures, missing
captions, and any model-assisted correction uncertainty. A successful process
exit does not establish fidelity. Stop affected transformations when structure,
media identity, locator basis, or conversion fidelity cannot be verified;
retain the original representation, affected scope, and resolution step.

Regenerate from preserved conversion output into a fresh derived destination
when practical. Reuse recorded settings, mappings, naming, and manual-edit
decisions; compare output inventories and content rather than accumulating
rewrites. If the PDF must later be reconverted, record a new conversion lineage
and snapshot and revalidate locators. Do not promise byte identity across
converter versions or overwrite earlier evidence.

Write the manifest, structure/media/locator records, validation results, and
caveats in the evidence home. Use the output contract's Ready, Caveated,
Blocked, or Not assessed statuses separately for indexing, reading/source
review, analysis, and `concept-cards`. Explain, for instance, which inspected
text remains readable when PDF page mappings are unverified, and why a
provenance-dependent use may still be blocked. Pass the records as upstream
provenance; preparation does not validate source claims or admit cards to
memory. Follow [validation and reports](./10-validation-and-reports.md), fill
the [manifest](../templates/manifest.md) and
[locator map](../templates/locator-map.md), and compare the representative
[PDF/Marker handoff](../examples/pdf-marker-handoff.md). Other live
[templates and examples](../SKILL.md#templates-and-examples) include the
non-executable helper plan and optional concept-card handoff. Package targets
and generated zips now exist, and public discoverability is live.
Package-path validation, isolated installation, installed-content inspection,
and final package reconciliation are Slice03 acceptance work.
