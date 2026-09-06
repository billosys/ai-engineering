# Workflow

Use this guide after the [load contract](./01-load-contract.md) identifies a
preparation need. Both operating modes produce the
[same output records](./03-output-contract.md); the difference is who performs
each action and what evidence the assistant can inspect.

## Inspect Before Writing

1. Identify the source and requested use: indexing, reading, source review,
   analysis, or downstream `concept-cards`. Inspect the existing workspace
   layout and output files before choosing destinations.
2. Inventory the supplied raw source, converted Markdown, converter metadata,
   navigation/TOC data, and media. Record unavailable inputs explicitly.
3. Read representative content and boundaries, including front/back matter,
   headings, figures or tables, and any suspected conversion damage. Inspect
   metadata and actual referenced paths rather than trusting filenames alone.
4. Compare available structure evidence. Keep converter metadata, source
   navigation, and observed content distinct. Do not resolve disagreements by
   treating an inferred boundary as a verified one.
5. Define the transformation and validation scope. Record which files will be
   derived, which inputs remain preserved, the locator basis to investigate,
   and which ambiguities need operator inspection.

Missing original inputs do not prohibit inspecting a converter bundle. They
do prohibit claiming comparison against that original. Record that limit in
the manifest and readiness report.

## Human-Assisted Operation

- Give the operator a bounded next action tied to an identified path or source
  location. Request the observations or output needed to choose the next step,
  such as a directory listing, conversion command/result, or inspection of a
  disputed boundary. Avoid asking for another confirmation of settled scope.
- Inspect supplied results before recommending a dependent transformation.
  Label operator-reported checks as such, including their scope; do not claim
  that the assistant inspected a PDF or ran a tool it could not access.
- Explain material choices in terms of source use: preserve a monolith while
  boundaries are uncertain, retain anchors needed for citations, or leave a
  media reference unresolved pending identification.
- Return records the operator can save in the evidence home. If file access
  is unavailable, provide their intended paths and contents and state that
  durable writing has not been verified.

## Agent-Direct Operation

- Inspect tools and input artifacts available in the environment; record the
  converter identity/version and invocation actually used. If conversion
  already happened, preserve its reported lineage and mark unknown details.
- Preserve original and converter-produced inputs before modifying derived
  text. Use a separate working copy or new run destination; do not overwrite
  the only raw source or the only unmodified conversion output.
- Perform supported transformations, maintaining mappings from inputs to
  generated files. Record manual edits as well as converter/helper commands
  so the result is explainable and can be regenerated where practical.
- Validate the produced files themselves, including media resolution relative
  to each containing file, structure coverage/order, and locator targets.
  Capture errors and incomplete checks in durable reports.

Detailed PDF/Marker, EPUB/pandoc, HTML/converted-Markdown, media, splitting,
locator, and reporting procedures are future routes in the
[guide map](../SKILL.md#guide-map). This core workflow supplies no verified
converter command recipe or executable helper. Use available tool guidance
and inspect actual outputs before trusting a conversion.

## Regeneration And Ambiguity

Keep a source/snapshot identity and a run identity. Repeating a preparation run
with unchanged inputs and settings should not accumulate duplicated media,
repeated path rewrites, or newly renamed sections. Prefer regeneration into a
fresh derived destination and comparison with the previous run. Retain earlier
snapshots and manual corrections as evidence; record changed settings, edits,
or tool behavior when outputs differ. Do not promise byte identity from an
unverified converter.

Stop the affected transformation when structure, media identity, page basis,
or conversion fidelity cannot be verified. Keep the original representation,
record the alternatives and downstream impact, and name the check that would
resolve the issue. Continue independent, supported work where useful. Do not
invent page numbers, section boundaries, missing text, or media matches to
make the output appear complete.

## Validate And Hand Off

Record what was inspected, how it was checked, and the result, distinguishing
whole-output checks from sampled checks. Account for missing or duplicate
sections, text gaps, unresolved media, and locator uncertainty. Recheck affected
references after splitting or changing paths.

Write the manifest and readiness/caveat records with a separate disposition
for each requested downstream use. Report prepared files and evidence paths,
remaining limits, and the next required inspection. If concept-card work is
requested, pass this handoff to `concept-cards` when available; completion of
preparation alone makes no claim about extracted cards or memory admission.
