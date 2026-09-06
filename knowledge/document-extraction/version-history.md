# Document Extraction Version History

### Version 1.1.0 - 2026-09-06

Placed the skill version inside entrypoint metadata for compatibility with the skill-creator frontmatter validator.

Added reusable PDF/Marker and EPUB/pandoc preparation guides and made their
entrypoint routes live. Both support human-assisted and agent-direct use,
preserved raw/converter inputs, inspection before edits, structure and media
validation, snapshot-bound locators, regeneration, and per-use readiness.

Modernized the preserved PDF/EPUB preparation prompts: metadata and headings
are cross-checked rather than treated as infallible, PDF index bases remain
distinct from document page labels, and EPUB navigation/markup survives
preparation. Source-specific helper creation and automatic readiness claims
are replaced with explicit decisions and caveats. No real conversion was run.
Shared guides, sibling templates/examples, and package/install integration
remain later work.

### Version 1.0.0 - 2026-09-06

Created the initial `document-extraction` source scaffold: entrypoint, load
contract, human-assisted and agent-direct workflow, and prepared-source output
contract. Defined preservation, structure, media, locator, manifest, readiness,
and caveat responsibilities for standalone use and downstream `concept-cards`
provenance.

The design draws on Project05's accepted source-preparation architecture and
current layout reconciliation. The historical `source-preparation` name is
superseded by `document-extraction`; historical inputs remain planning
provenance. Detailed PDF/Marker, EPUB/pandoc, and shared preparation guides,
sibling templates and examples, and package/install integration remain later
work. This entry records source contracts, not a completed conversion tool or
packaged release.
