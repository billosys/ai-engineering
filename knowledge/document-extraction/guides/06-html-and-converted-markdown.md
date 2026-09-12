# HTML And Converted Markdown

Use this guide to prepare captured HTML or supplied converted Markdown for
standalone indexing, reading, source review, analysis, and downstream
`concept-cards` upstream provenance. Follow the [output contract](./03-output-contract.md)
for identities and evidence homes; use the PDF or EPUB guide for their
format-specific checks when those are the actual originals.

## Establish What Was Captured

Inventory the supplied raw files, saved HTML, resources, converted Markdown,
converter logs, and any rendered-page observations before editing. Preserve
each input as received. Record source URL/path, requested and final URL when
known, capture time, title/edition, capture tool/method, and checksums where
practical. Distinguish a server response, browser-saved document, rendered DOM
snapshot, screenshot, and text-only export: each preserves different evidence.
A URL or page title alone does not identify the captured bytes.

For a page with changing content, identify the captured state: expanded panels,
selected tab, pagination, loaded sections, language, and relevant view settings.
Record state facts, not authentication secrets. Retain separately supplied
states as separate snapshots; do not silently join content observed at different
times into one purported original. A screenshot supports a visual observation
but cannot supply missing link targets, text bytes, or off-screen content.

For converted Markdown with no original, record the supplied file as the
available snapshot and original fidelity as unchecked. Record the converter,
version, dialect, settings, and transformations only when known. Missing
lineage is a caveat, not permission to invent a source URL or conversion step.

## Inspect Before Preparing

1. Read representative opening/body/closing content and inspect headings,
   navigation, anchors/IDs, tables, code, figures, and resource references.
   Compare the visible page with the saved material when both are available.
2. Identify the content region and navigation/boilerplate separately. Log any
   excluded spans and why; menus, notes, or repeated headings may carry useful
   context and must not disappear through an unexplained cleanup rule.
3. Record the base used to resolve relative URLs. An HTML `base` element can
   change that base; a saved file's local directory does not automatically
   reproduce its original web context. See the [HTML document-base rules](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-urls).
4. Inspect heading attributes, anchor targets, inline/reference links, HTML
   blocks, and asset locations in the Markdown. For citation-bearing Markdown,
   inventory declared bibliography resources (including frontmatter fields),
   available bibliography files, and the cited keys needed by the requested
   scope. Verify a mapping only by direct key lookup; a filename mismatch or a
   missing resource remains a dependency caveat, not a reason to invent a
   bibliography mapping. Note which original structures have no converted
   counterpart. Do not strip embedded markup to make text look cleaner before
   understanding the locators and content it carries.
5. Identify capture gaps: script-loaded text, collapsed content, pagination,
   lazy-loaded assets, embedded frames, canvas, or external resources absent
   from the saved material. Report the observed scope; a static snapshot is
   not proof that every state of the page was captured.

## Human-Assisted Operation

Request the capture method/time, file inventory, and bounded excerpts around
the specific heading, link, or missing region. Ask for a screenshot of the
relevant rendered state plus the corresponding saved markup or link target
when both appearance and identity matter. Have the operator check a named
collapsed or paginated section if its omission affects the requested use.

Compare the returned evidence before selecting a transformation. Label
operator reports distinctly from direct inspection. If a full capture cannot
be obtained, retain the partial snapshot and explain the affected content and
readiness limits rather than repeatedly requesting the whole site.

## Agent-Direct Operation

Inspect accessible files and available browser/capture tools. When capture is
part of the requested task, save the authorized page/state and its relevant
resources into a new raw snapshot, documenting the method and scope. Do not
expand one-page preparation into a site crawl or silently refresh an existing
capture. Record unavailable content and tools explicitly.

Work on derived copies. Maintain original-resource-to-local-path mappings,
preserve anchors and meaningful attributes, and compare prepared content with
the captured input. Use [media normalization](./07-media-path-normalization.md)
for references and [structure mapping](./08-structure-mapping-and-splitting.md)
for splits. Keep original locators alongside generated ones under the
[locator model](./09-locator-model.md).

## Prepare, Check, And Regenerate

Preserve the raw capture and unmodified conversion while producing Markdown
with ordered content, retained source identifiers, and explicit transformation
notes. Choose a monolith if boundaries or markup dependencies remain uncertain.
Do not reconstruct dynamic content from a screenshot or a guessed API response
and label it source text. Stop the affected transformation and record what
additional capture or inspection would resolve it.

Validate coverage against the captured scope: content spans, headings,
anchors, media, code/table fidelity, and any references changed by splitting.
If rendering is unavailable, say which visual checks were not performed.
Regenerate derived output from the preserved snapshot into a new destination;
a new web retrieval is a new snapshot, not proof of reproducibility of the old
one. Compare inventories and mappings to prevent duplicate assets or drift.

Write the manifest and [validation/readiness report](./10-validation-and-reports.md),
including dynamic-content, source-identity, resource, and conversion caveats.
Assess each requested use separately. Indexing a captured excerpt does not
establish completeness of the article or site; a readable page may still lack
the source locators needed for provenance-bearing concept-card work.
