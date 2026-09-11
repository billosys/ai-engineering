# Document Extraction Version History

### Version 1.4.3 - 2026-09-11

Corrected remaining live guide handoffs after CDC found stale Slice02
discoverability wording in load-contract, PDF, and EPUB preparation guides.
No preparation procedure, package support shape, executable validator, or
runtime capability changed.

### Version 1.4.2 - 2026-09-10

Clarified the current package handoff after the Slice02 documentation close:
package targets, generated zips, and public discoverability are live, while
package-path validation, isolated installation, installed-content inspection,
and final reconciliation are Slice03 acceptance work. No preparation procedure
or package support shape changed.

### Version 1.4.1 - 2026-09-10

Corrected live-guide handoffs after the Arc05 package targets landed. Package
targets and generated zips now exist; README/docs discoverability remains
Slice02 work, while package-path validation, isolated install smoke, and final
package reconciliation remain Slice03 work.

### Version 1.4.0 - 2026-09-10

Added Makefile package-target support for the entrypoint, sibling guides,
templates, and examples. Docs/discoverability and isolated install-smoke
evidence remain later Arc05 work. No conversion helper, executable validator,
runtime behavior, or real-corpus extraction was added.

### Version 1.3.0 - 2026-09-06

Added sibling fillable templates for manifests, structure maps, media reports,
locator maps, validation/readiness, caveats, and downstream concept-card
handoffs, plus a non-executable per-extraction helper-script plan. The helper
plan keeps source-specific boundary, naming, media, dry-run, regeneration and
validation assumptions auditable rather than making historical scripts canonical.

Added explicitly synthetic PDF/Marker, EPUB/pandoc, HTML/converted-Markdown,
and concept-card handoff examples with scoped checks, unknown lineage,
source/output locator distinctions, and visible per-use limitations. No real
conversion or source-validation run is asserted by those examples.

Made templates/examples live in the entrypoint and relevant guide routes;
cleaned remaining future-format and shared-reporting caller text. Source
support remains standalone and usable in both operating modes. Package/docs/
install integration stays future Arc05 work; no executable scripts were added.

### Version 1.2.0 - 2026-09-06

Added shared guides for HTML and converted-Markdown preparation, media path
normalization, structure mapping/splitting, typed locators, and validation,
readiness, and caveat reports. Each supports human-assisted and agent-direct
operation for standalone document work and downstream concept-card provenance.

Made guides 06 through 10 live in the entrypoint and replaced stale future
routing in the core workflow and output contract. Preserved raw/snapshot
identity, complete container boundaries, source/output locator distinctions,
per-use readiness, and evidence limits. Templates/examples and package/install
integration remain later work; no conversion helpers or executable validators
were added.

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
