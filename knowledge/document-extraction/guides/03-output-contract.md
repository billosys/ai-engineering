# Output Contract

Use this contract to define and inspect a prepared-source handoff. The records
may be sections of one report or separate files; keep stable cross-references
so a consumer can trace prepared content to preserved inputs. This is a core
content contract. Use [structure mapping](./08-structure-mapping-and-splitting.md),
[media normalization](./07-media-path-normalization.md), the
[locator model](./09-locator-model.md), and
[validation and reports](./10-validation-and-reports.md) for the live
procedures. Use the live [manifest template](../templates/manifest.md) and
[template/example map](../SKILL.md#templates-and-examples) to fill these
categories, or the [concept-card handoff](../templates/concept-card-handoff.md)
for an optional downstream transfer. Examples illustrate records; they are
not evidence that a source was converted or verified.

## Homes And Identity

Reuse the workspace's accepted source layout. If none is established, use:

- raw input: `knowledge/<kb>/sources/<format>/<SourceSlug>/`;
- prepared Markdown and any split files:
  `knowledge/<kb>/sources/md/<SourceSlug>/`;
- preparation evidence:
  `knowledge/<kb>/extraction-metadata/<SourceSlug>/`.

These are downstream workspace paths, not directories to create inside the
skill. Record any chosen alternative in the manifest. Preserve the supplied
raw input and unmodified converter output separately from derived files;
record their actual locations. Use distinct destinations for multiple runs
where needed to retain earlier snapshots and their evidence.

Give each source, prepared snapshot, and preparation run an identifier. Record
checksums when practical and label absent checksums or unknown identities.
Scope line numbers and generated filenames to a particular snapshot; a later
rewrite must not silently inherit the earlier locator identity.

## Required Records

| Output | Minimum content and checks |
| --- | --- |
| Prepared Markdown | Source/snapshot/run identity, prepared file list, reading order, retained headings/anchors and media references, transformation notes, and disclosed omissions or damaged content. Distinguish preserved converter text from corrected/normalized text. |
| Structure map | Ordered sections, original titles and identifiers where available, parent/child relationships, input and output spans/files, boundary evidence, and verified/inferred/unresolved status. Include unnumbered/front/back matter or explain exclusions. Keep a monolith if splitting cannot be justified. |
| Media references | Original reference/asset identity, preserved asset location, normalized target, containing prepared file, and resolution result. Paths must resolve relative to the file containing the reference. Record missing, remote, ambiguous, duplicate, or unchecked assets explicitly; remote references are not evidence of local capture. |
| Locator records | Source and snapshot identifiers, locator type/value/basis, original-to-prepared mapping, verification method and scope, and uncertainty. Preserve original locators alongside derived ones. |
| Manifest | Input identities, formats and paths; run identity/date; tool/converter identity and version if known; commands/settings or supplied conversion lineage; checksums where practical; generated file list; transformation/manual-edit record; and pointers to structure, media, locators, validation, readiness, and caveats. |
| Validation/readiness report | Requested uses, checks performed and their coverage, observed results, failed/unavailable checks, per-use disposition, caveat references, and next actions. Distinguish direct checks, operator reports, and inference. |
| Caveat records | Identifiable issue, affected source span/files and outputs, observed evidence, uncertainty or damage, downstream impact, current handling, and the inspection or input needed to resolve it. |

Every category must be accounted for. An empty media inventory can say no
media was found within the inspected scope; a missing original must say it was
unavailable. Do not confuse absence, inapplicability, unchecked content, and a
successful validation result. Do not create meaningless placeholder files
merely to represent an inapplicable record category.

## Locator Semantics

Keep these distinctions visible in each mapping:

- **PDF:** physical page index, its zero/one-based convention, and printed or
  document page label are distinct. Record the converter's value separately
  from any interpreted page value; leave the basis unresolved until checked.
- **EPUB/HTML:** retain available navigation targets, anchors, element IDs,
  resource paths, and URI fragments with their source capture identity. Do
  not fabricate fixed page numbers from reflowed content.
- **Markdown:** line spans refer to an identified file snapshot. Heading text
  alone may be ambiguous; retain order, hierarchy, and source anchors when
  available to distinguish repeated headings.

Conversion, splitting, and path repair can change derived locations. Record
the mapping and validation scope instead of replacing the original locator
with an apparently equivalent one. Follow the
[locator model](./09-locator-model.md) for mapping and verification; ambiguous
mappings stay caveated or blocked.

## Readiness By Intended Use

Assess requested uses separately: concept-card extraction, full-text indexing,
standalone reading/source review, and ordinary analysis. For each, state one:

- **Ready:** checks appropriate to the declared scope support this use, with
  no unresolved issue known to affect it; record what was actually checked.
- **Caveated:** the use can proceed within named limits, with affected content
  and implications made explicit.
- **Blocked:** a required property is missing or unverifiable; name the next
  inspection or repair needed before this use proceeds.
- **Not assessed:** this run did not evaluate readiness for that use.

Readiness is scoped to the checked snapshot and use. Text suitable for reading
may still lack the locators needed for provenance-bearing extraction. A
successful converter exit or a readable sample does not establish completeness
or accurate media, tables, OCR, and citations throughout the document.

If the original source is unavailable, record that fidelity comparison was
not performed. If a location is inferred or media cannot be verified, preserve
that caveat even when another use can proceed. Preparation readiness does not
establish the truth of source claims.

## Downstream Consumption

Hand off prepared content with its manifest, mappings, validation/readiness,
and caveats. `concept-cards` consumes these as upstream provenance and owns
its own extraction, card/claim semantics, evidence grading, reconciliation,
and memory-admission decisions. Keep preparation caveats attached to affected
spans so downstream work cannot erase uncertainty by copying text.

Indexing, reading, source review, and analysis consume the same records
independently of any concept-card workflow. The contract requires no graph
database, memory runtime, conversion service, or concept-card package.
