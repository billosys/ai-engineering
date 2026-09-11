# Load Contract

Use this guide to separate source preparation from downstream interpretation.
Read the [workflow](./02-workflow.md) when preparation is needed and the
[output contract](./03-output-contract.md) before defining deliverables.

## Positive Triggers

Load `document-extraction` for raw PDF, EPUB, HTML, converted Markdown, or a
converter-produced source bundle when the requested work needs one or more of:

- readable Markdown with traceability to the supplied source;
- inspection of converter text, metadata, navigation, or extracted media;
- section or chapter mapping, splitting, or repair of media references;
- explicit page, heading, anchor, line, or URI-fragment locators;
- manifests, source-readiness decisions, or conversion caveats.

A request to prepare a book for indexing is sufficient. Concept cards are not
required. A converter bundle without its original source is also a valid
input, but the missing original limits what fidelity can be verified.

## Negative Triggers

Do not load merely because a task mentions documents or provenance:

- Reading, summarizing, searching, or analyzing already usable source material
  stays with the requested reading or domain workflow.
- Creating or reconciling cards, claims, relationships, competency questions,
  or memory-admission records from prepared source routes to `concept-cards`
  when available.
- Authoring, typesetting, or visually redesigning a document belongs to the
  relevant document-authoring workflow.
- Building an index service, conversion server, graph database, or ontology
  lifecycle system needs a separate implementation or method scope.

If downstream work exposes broken media, missing structure, or ambiguous
locators, return here for that preparation gap. Do not automatically redo an
adequate prepared snapshot.

## Ownership Boundary

| This skill owns | Downstream consumers own |
| --- | --- |
| Preserved source identity and conversion lineage | Interpretation and domain conclusions |
| Prepared Markdown, structure maps, and split-file decisions | Index construction and search behavior |
| Media references and source locator records | Card/claim representation and use of source spans |
| Manifests, validation observations, readiness, and caveats | Evidence grading, card verification, reconciliation, and memory admission |

Preparation readiness describes fitness for a named use. It does not certify
that source claims are true, validate concept-card semantics, or admit material
to memory. `ontology-engineering` is reserved for a future adjacent capability;
it is not a dependency or an implemented route here.

## Entry Conditions

Establish the input paths or supplied artifacts, source identity, intended
downstream use, output home, and available tools. Inspect the raw or captured
input, converted text, metadata, and media before selecting transformations.
Reuse an established source layout; the output contract supplies a default
when the workspace has none.

Choose agent-direct operation when the assistant can inspect files and run the
needed tools. Choose human-assisted operation when an operator must perform
some checks or conversions. If access is incomplete, identify the missing
artifact or observation precisely and continue only work supported by the
available evidence. User reports remain distinguishable from direct checks.

## Handoff Boundary

Finish preparation with the snapshot identity, manifest, structure/media and
locator records, validation results, and readiness/caveat report. A later
`concept-cards` workflow consumes these as upstream provenance; retain their
identifiers and caveats rather than converting preparation status into a card
evidence grade. Standalone indexing, reading, source review, and analysis use
the same handoff without loading `concept-cards`.

Choose the live format and shared procedures in the
[entrypoint's guide map](../SKILL.md#guide-map), then use the
[templates and examples](../SKILL.md#templates-and-examples) to record the
handoff. Start with the [manifest](../templates/manifest.md); use the optional
[concept-card handoff](../templates/concept-card-handoff.md) only when that
consumer is requested. Package targets, generated zips, and public
discoverability are live for this skill. Package-path validation, isolated
installation, installed-content inspection, and final reconciliation are
Slice03 acceptance work. These are live source resources.
