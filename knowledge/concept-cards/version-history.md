# Concept Cards Version History

### Version 4.8.1 - 2026-09-12

Refined the rich real-corpus card profile toward teaching and lookup use before
audit use. Updated the entrypoint, load contract, operator workflow, extraction
guide, validation guidance, concept-card template and synthetic rich example so
main card sections remain concise, source-specific and pedagogically useful
while support maps, provenance, lifecycle state and handoff notes retain the
v4 evidence controls. No schema, executable validator, runtime capability,
memory admission, graph operation or corpus extraction was added.

### Version 4.8.0 - 2026-09-11

Added the rich real-corpus card profile: a readable, one-concept body with
source-faithful definitions, properties, recognition or construction, context,
source-specific examples, relationships/CQs, confusions, source/support map,
and explicit extraction/review boundaries. Updated extraction, re-extraction,
evidence, relationship/CQ, and validation guidance plus review surfaces so rich
prose cannot replace claim support, typed records, or separate lifecycle and
admission controls. Added a synthetic rich-profile example. No executable
validator, completed review, runtime capability, or live-corpus extraction was
added.

### Version 4.7.4 - 2026-09-11

Corrected a remaining live operator-workflow handoff after final Project05
closure scanning found it still assigned delivered package/docs/install work to
Arc05. No method, package support shape, schema, validator, or runtime
capability changed.

### Version 4.7.3 - 2026-09-11

Corrected remaining live load-contract handoff wording after CDC found stale
Slice02 discoverability language. No method, schema, validator, package
support shape, or runtime capability changed.

### Version 4.7.2 - 2026-09-10

Clarified the current package handoff after the Slice02 documentation close in
the entrypoint and extraction guide: package targets, generated zips,
`references/` support, and public discoverability are live; package-path
validation, isolated installation, installed-content inspection, and final
reconciliation are Slice03 acceptance work. No method, schema, validator, or
runtime capability was added.

### Version 4.7.1 - 2026-09-10

Corrected live-guide handoffs after the Arc05 package targets landed. Package
targets and generated zips now exist, and `references/` is included in the
generated package. README/docs discoverability remains Slice02 work; package-
path validation, isolated install smoke, and final package reconciliation remain
Slice03 work.

### Version 4.7.0 - 2026-09-10

Added Makefile package-target support for the entrypoint, sibling guides,
templates, examples, and references. Docs/discoverability and isolated
install-smoke evidence remain later Arc05 work. No executable validator,
runtime behavior, or real-corpus work was added.

### Version 4.6.0 - 2026-09-10

Added sibling reference/review support for record field groups, vocabulary,
structural-validation candidates, semantic audit boundaries, and operator review
gates. The material documents Markdown/YAML record conventions and review
boundaries without adding JSON Schema, executable validation, runtime behavior,
or real-corpus review evidence.

Updated entrypoint and guide handoffs to mark all Arc04 source support live.
The references README and maintenance guidance record that current Makefile helper
macros do not copy `references/`; Arc05 owns package support, generated-zip,
docs/discoverability, and installation work.

### Version 4.5.0 - 2026-09-10

Added eight sibling synthetic representative examples covering a minimal card,
claim-specific source support, CQ coverage, a relationship edge, extraction-run
provenance, reconciliation, memory admission, and a parallel-worker default
recipe. The examples keep construct identities, source/prepared-source
provenance, lifecycle results, preservation and admission decisions distinct.

Updated the entrypoint and guide handoffs to mark templates and examples as live
source support. Schema/reference and validation-review support remain future
Slice03 work. Raw document cleanup remains owned by document-extraction; no
schema, executable validator, runtime, package, installation, or real-corpus
work was added.

### Version 4.4.0 - 2026-09-06

Added twelve sibling Markdown/YAML record templates for concept cards, claims,
source locators, source support with embedded spans, relationship edges,
competency questions, extraction runs, validation results, verification results,
reconciliation results, preservation decisions and memory admission. Templates
retain distinct construct identities, source/prepared provenance, evidence
grade, extraction confidence, lifecycle results/state and scoped reliance.

Added a live template map and shared copying/reference conventions to the
entrypoint. The current map supersedes earlier guide availability notes;
existing guides are preserved for a later caller-wording cleanup. Placeholder
records make no successful review or admission claim. Examples, schema/reference
and validation-review support remain future Arc04 work; packaging, docs and
installation remain Arc05 work. No executable validators, runtime integration
or live corpus processing was added or performed.

### Version 4.3.0 - 2026-09-06

Added detailed relationship/CQ, reconciliation, memory admission and maintenance
guides. Relationships retain edge identity, endpoint roles, direction/inverse/
symmetry, support and scoped lifecycle attachments. Competency questions retain
component coverage, answerability, retrieval limits and changed/obsolete/deferred
history. Reconciliation compares sources and prior value, records dispositions
and preserves unresolved conflicts without automatic winners.

Memory admission now has a scoped evidence and acceptance workflow with
admit/reject/defer outcomes, revision applicability and re-entry checks,
separate from artifact retention or runtime writes. Maintenance guidance names
source-core ownership and preserves future Arc04 support and Arc05 package,
docs and install boundaries. All new procedures cover both operating modes and
honest handoff of results and remaining work.

Made all ten guides live and updated the existing guide callers. No support
assets, schema, executable validator, package integration, runtime or real-corpus
processing was added or performed.

### Version 4.2.0 - 2026-09-06

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

### Version 4.1.0 - 2026-09-06

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

### Version 4.0.0 - 2026-09-06

Created the initial `concept-cards` source scaffold: thin entrypoint, load
contract and operator workflow for human-assisted and agent-direct use.
Preserved the Project03 v4.0 conceptual model's atomic cards, claims, source
support/spans/locators, relationship edges, competency questions, extraction
runs, separate evidence/lifecycle results, preservation and memory admission.
The concept-card skill version sequence intentionally continues the public
v3.2 proto-skill lineage as the v4.x method line.

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
