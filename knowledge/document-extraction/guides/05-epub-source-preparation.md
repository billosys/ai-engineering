# EPUB Source Preparation

Use this guide for an EPUB and its pandoc-style Markdown/media bundle when
preparing standalone indexing, reading, source review, analysis, or downstream
`concept-cards` provenance. Apply the [workflow](./02-workflow.md) and
[output contract](./03-output-contract.md). This is reusable preparation
guidance, not a request to create per-source scripts or run a conversion.

## Inputs And Preservation

Locate the preserved raw EPUB, converted Markdown (often `book.md`), extracted
`media/`, and any supplied conversion logs or metadata. Inspect actual output
paths: `media/media/` nesting occurs in the preserved workflow, but must not
be assumed for every book or invocation. Where available, inspect the EPUB's
content resources, reading order, navigation document or TOC, and original IDs
through read-only tooling or a separate extracted copy.

Record source identity/checksum when practical, conversion date, pandoc and
wrapper versions, output Markdown dialect/extensions, media extraction
destination, filters/options, and command or reported invocation. Unknown
lineage remains unknown. Keep the EPUB and original conversion bundle intact;
edit derived copies and retain source/snapshot/run identifiers. Follow the
accepted workspace layout or the output contract's default destinations.

If only the conversion bundle is available, it can be inspected and prepared,
but source fidelity and original navigation checks may remain unavailable.
Identify missing conversion output before proceeding; no particular wrapper
script is a prerequisite supplied by this skill.

## First-Pass Inspection

Before editing or choosing chapter boundaries:

1. Read the opening material, inline TOC, several body sections, and back
   matter. Inspect actual heading forms, including numbered chapters, parts,
   appendices, prefaces, and unnumbered headings. A source may have no `# N`
   chapter pattern at all.
2. Inspect navigation anchors, resource references, heading attributes, span
   anchors, and HTML IDs. Cross-check available original navigation targets
   and reading order against the converted body. Do not assume that an inline
   TOC occurrence is the start of the content it names.
3. Inventory media references and assets, including SVG, image attributes,
   reference-style links, and raw HTML. Check the actual location of several
   assets, including any nested `media/media/` paths.
4. Inspect pandoc div markers, code fences, raw HTML/SVG blocks, footnotes,
   link definitions, and existing metadata. Identify constructs spanning a
   proposed split so that cutting at a heading does not strand their content.

Pandoc supports explicit heading attributes and fenced divs, including nested
divs. Preserve these constructs while mapping structure; their syntax is
documented in the [Pandoc User's Guide](https://www.pandoc.org/demo/example2.html#extension-header_attributes)
and [fenced-div section](https://www.pandoc.org/demo/example2.html#extension-fenced_divs).

## Human-Assisted Operation

Request the relevant heading/TOC excerpts with snapshot line numbers, adjacent
navigation anchors, and a bounded media listing. For a disputed duplicate
heading, have the operator open the corresponding navigation target and body
resource, reporting the resource path and ID as well as the title. For a
media ambiguity, ask for the exact original reference, filesystem target, and
visual comparison to the EPUB rendering.

Inspect supplied results before proposing path changes or splits. Label these
as operator-reported observations where appropriate. Explain which structure
decision they support and which checks remain unavailable. If file writing is
unavailable, return the proposed record paths and contents without claiming
they were saved or that unseen source content was verified.

## Agent-Direct Operation

Inspect the accessible bundle and, when available, original EPUB navigation
and content resources before changing derived output. Use available tools to
collect an ordered structure/locator map, candidate media rewrites, and
validation results. Preserve the original archive and conversion output.

Apply verified transformations to a working copy, re-open the generated files,
and compare them with mapped source spans. Use existing suitable tools rather
than assuming a source-specific helper exists. If raw-resource or rendering
inspection is unavailable, continue supported bundle checks and record the
fidelity limit; switch unresolved checks to human-assisted operation as needed.

## Map Structure And Locators

Build an ordered map of real body sections, cross-checking headings against
available navigation targets, original resource IDs, and content. Record:

- source/snapshot/run identity and the original resource path;
- title, original chapter/part/appendix label when present, hierarchy and order;
- Markdown input file and start/end lines with an explicit numbering base;
- original anchors, HTML IDs, URI fragments, and their converted counterparts;
- proposed output filename and local target, boundary evidence/status, and
  unresolved discrepancies.

Mark the inline TOC's span separately and preserve it as front/navigation
matter. Its repeated titles are not additional chapters. Duplicate headings
in the body need distinct resource/anchor identities or hierarchy and order;
do not deduplicate on title text or pick the first string match. Reconcile
unmatched navigation entries and body sections explicitly. An absent
`metadata.json` is normal for the preserved pandoc workflow, not a reason to
ignore other available EPUB structure evidence or demand a Marker-style file.

Reflowable EPUB content has no assumed fixed page-number basis. Use line,
heading, anchor, resource path, and URI-fragment locators tied to the source
and converted snapshots. If the EPUB supplies page labels, preserve them as
source-provided navigation evidence with their basis; do not reinterpret them
as PDF physical pages or use renderer screen numbers as stable citations.

Retain original-to-converted-to-split mappings. Line numbers refer to the
identified input snapshot, not a later rewrapped file or generated header.
Keep original resource paths with fragment IDs: an ID alone may recur across
resources. Check that converted anchors actually exist and point to the
intended content. Leave lost or ambiguous mappings unresolved rather than
inventing replacements.

## Normalize Media References

Resolve original references against the actual bundle, then compute paths
relative to the containing prepared file. A project-relative reference ending
in `<SourceSlug>/media/media/file0.svg` may become
`./media/media/file0.svg` when that is the actual local target. Preserve the
second `media/` if it identifies a real directory; do not flatten nesting just
because it looks redundant.

Pandoc's media extraction option rewrites references to extracted files and
can retain original relative paths within the extraction destination. Inspect
the invocation and output rather than treating any particular nesting as
universal. See [pandoc media extraction](https://www.pandoc.org/demo/example2.html#option--extract-media).

Preserve image alt text, titles, sizing attributes, and raw HTML/SVG. Match
the full resolved target, not just a basename shared by multiple resources.
Leave already-correct references unchanged, avoid repeated prefixes, and
distinguish remote/data references from local assets. Missing assets, ambiguous
identity, or invalid paths need caveat records rather than guessed fixes.

After splitting, validate every local media reference relative to its actual
containing file, including reference definitions and embedded markup. Record
resolution checks separately from visual identity checks against the EPUB and
their coverage. A preserved SVG may still depend on other assets or unsupported
rendering features; report unchecked dependencies or visual differences rather
than claiming fidelity from file existence alone.

## Choose Splits And Preserve Markup

Split only at verified body boundaries. Include numbered chapters, parts,
appendices, prefaces, cover/title matter, inline TOCs, and unnumbered sections
according to the actual structure. Give every retained input span an output
destination. Compare expected split count with accepted boundary count, not
with every TOC entry or heading in the file.

Preserve pandoc div markers, heading attributes, navigation anchors, HTML IDs,
and raw HTML/SVG as-is unless a separate cleanup is explicitly scoped. Do not
cut through a nested div, fenced code block, table, or raw block and leave
invalid fragments. If the desired chapter boundary falls inside a spanning
container, retain the enclosing unit or monolith and report the limitation
until a structure-aware transformation is scoped. Do not silently remove the
container to make the split work.

Track footnotes, link definitions, and cross-section navigation dependencies.
For references that cross new file boundaries, preserve the original locator
in the map and record a verified rewrite to the correct output file/anchor.
If this cannot be done without unscoped cleanup, keep the relevant material
together and caveat the proposed split. Do not delete the inline TOC or anchors
merely because navigation repair is inconvenient.

Use stable order-plus-slug filenames with collision checks after shortening;
store original titles and labels in metadata, including those unsuitable for
filenames. Split files default to the prepared-source directory under the
output contract. A filename sequence is a reading-order key, not evidence
that the author numbered every section.

Each output needs metadata or a linked sidecar recording `source_format: epub`,
source/snapshot/run identity, original section title/label, order, input
Markdown span, original resource/anchor locators, output target, and
manifest/caveat references. Do not require a fabricated `pdf_page`. If using
YAML frontmatter, serialize titles and labels safely, preserve existing source
metadata, and distinguish generated headers from the book's front matter.
Retain original headings and content, and account for generated header lines
when interpreting output line numbers.

## Validate, Regenerate, And Report

Compare the generated file inventory, content spans, and reading order with
the accepted structure map. Check starts and ends, front/back matter coverage,
duplicate/missing sections, metadata, media resolution, anchor targets, and
cross-file references. Counts alone do not prove preservation. Distinguish
whole-bundle checks from samples and operator observations from direct checks.

Record lost formatting or anchors, changed reading order, missing navigation,
duplicate IDs, unsupported HTML/SVG, footnote damage, missing assets, or
conversion loss affecting code, tables, math, or styled content. Stop the
affected transformation when structure, media identity, locator basis, or
conversion fidelity cannot be verified. Retain the original representation
and name the inspection or repair needed; proceed only with independent work
supported by the available evidence.

Regenerate derived files from the preserved conversion snapshot into a fresh
destination when practical. Reuse recorded mappings/settings/names and preserve
manual corrections as explicit transformations. Compare inventories and
content; avoid duplicate media, repeated path rewrites, and filename drift.
A later reconversion or changed Markdown dialect creates a new snapshot whose
line/anchor maps must be checked again. Do not overwrite earlier provenance or
promise identical bytes across converter settings or versions.

Write the manifest, structure/media/locator records, checks, and caveats in
the evidence home. Assign Ready, Caveated, Blocked, or Not assessed separately
for indexing, reading/source review, analysis, and `concept-cards` under the
output contract. A readable text bundle may still have unresolved anchors or
SVG fidelity that limit another use. Pass the records as upstream provenance;
card semantics, source-claim verification, and memory admission remain
downstream responsibilities. Follow
[validation and reports](./10-validation-and-reports.md), fill the
[structure map](../templates/structure-map.md) and
[media report](../templates/media-report.md), and compare the representative
[EPUB/pandoc handoff](../examples/epub-pandoc-handoff.md). Other live
[templates and examples](../SKILL.md#templates-and-examples) include the
non-executable helper plan and optional concept-card handoff. Package targets
and generated zips now exist, and public discoverability is live.
Package-path validation, isolated installation, installed-content inspection,
and final package reconciliation are Slice03 acceptance work.
