# Concept Cards Version History

### Version 1.2.0 - 2026-09-06

Added evidence lifecycle and validation/verification guides. Evidence grade
records warrant and rationale on the actual claim/support subject; extraction
confidence remains a separate signal about the extraction act. The guides
cover attachment scope, insufficient/partial/conflicting/unassessed evidence,
revision applicability and separate lifecycle results without inventing a
final schema or automatic admission transition.

Added bounded structural validation and semantic verification procedures with
actor, method, target, evidence, coverage, outcome, caveats and revision
identity. Review boundaries distinguish same-context checks, independent
CDC/fresh-context reproduction, operator-reported observations, human review,
tool/process evidence and unavailable checks. Both operating modes retain
honest handoff and storage limits.

Made guides 05/08 live, cleaned the stale caller wording in guides 01–04, and
removed the temporary entrypoint availability qualification. Guides 06/07/09/10,
Arc04 support and Arc05 package/docs/install integration remain future work.
No executable validator, runtime or real-corpus validation/verification was
implemented or performed.

### Version 1.1.0 - 2026-09-06

Added source-faithful extraction and source-primary re-extraction/preservation
guides. They cover source and prepared-source identities, extraction-run and
worker provenance, one-concept boundaries, claim/span comparison before source
support assertions, typed locators, inference labels, extraction confidence,
and handoff evidence for human-assisted and agent-direct operation.

Re-extraction inventories prior constructs and results, derives against the
source before comparing old cards, distinguishes source drift and unavailable
or damaged inputs, and records preserved/superseded/rejected/unresolved prior
value without erasing its history. Evidence grade and lifecycle/admission
results remain separate from extraction confidence and preservation.

Made guides 03/04 live in the entrypoint's current guide map. Guides 05–10,
Arc04 support and Arc05 package/docs/install integration remain future work.
No live corpus extraction, executable validator, runtime or package changes
were performed as part of this source-guidance addition.

### Version 1.0.0 - 2026-09-06

Created the initial `concept-cards` source scaffold: thin entrypoint, load
contract and operator workflow for human-assisted and agent-direct use.
Preserved the Project03 v4.0 conceptual model's atomic cards, claims, source
support/spans/locators, relationship edges, competency questions, extraction
runs, separate evidence/lifecycle results, preservation and memory admission.
The model's v4.0 designation is historical method lineage, not this source
skill's version sequence.

Project05 translates the historical `concept-card-method` planning name into
`concept-cards` and its current source root. Historical `source-preparation`
routing is replaced by `document-extraction`, whose prepared outputs are
upstream provenance rather than claim support by themselves. Historical
under-guides support layouts and local-document histories are not introduced.

Only the entrypoint, this sibling history and guides 01/02 are implemented.
Guides 03 through 10 remain future Arc03 slices; sibling templates, examples,
validation/reference support and schemas remain Arc04 work; package/docs/
generated zip/install integration remains Arc05 work. No executable validator,
runtime service, database or memory automation was added.
