# Load Contract

Load `concept-cards` when the task calls for concept-card method output or
review. Start the [operator workflow](./02-operator-workflow.md) once the
requested operation and source/card inputs are identified. This skill keeps
method representation distinct from document preparation and domain analysis.

## Positive Load Cases

- Create a card for a concept or extract a card set from specified sources.
- Re-extract from a source snapshot and compare against existing cards without
  silently dropping their unique value.
- Attach claims to source spans, assess source support and evidence grade, or
  capture extraction confidence and extraction-run provenance.
- Validate card structure, verify meaning/support, reconcile conflicts, or
  document preservation decisions and unresolved prior material.
- Model relationship edges, competency questions and coverage/answerability.
- Decide whether particular constructs qualify for memory admission under
  the applicable evidence and acceptance requirements.

Reviewing existing cards can load this method without a new extraction run.
Limit the work to the requested operation and record the reviewed revisions.

## Negative Load Cases And Routing

| Request | Route or boundary |
| --- | --- |
| Extract Markdown from raw PDF, EPUB or HTML; repair converted text, structure, images or locators | `document-extraction`; return here when prepared sources are needed for requested card work |
| Read, summarize or analyze already usable sources | Ordinary source-reading or relevant domain workflow; no automatic card creation |
| Correct domain reasoning or terminology | Relevant domain skill/practice remains primary; this method records claims and their evidence |
| Plan a project, package, release or installation | Project-management or implementation workflow; this method does not own source/package changes |
| Design generic ontologies, graph/ontology databases, GraphRAG or CCDP services | Relevant design/implementation work; representing an edge here does not implement a graph service |
| Look up memory or operate a memory runtime | Relevant memory workflow; admission decisions here do not implement storage, retrieval or enforcement |

For mixed requests, use each workflow for its own portion. Do not redo adequate
document preparation merely because concept-card work follows it.

## Prepared Sources Are Upstream Provenance

Before using `document-extraction` output, identify the prepared snapshot/run,
original or supplied source, manifest, structure map, media/locator mappings,
validation/readiness report and caveats. Preserve these identities and limits
with affected excerpts. Missing originals, ambiguous page bases, damaged tables
or unchecked figures stay visible in downstream work.

A source locator is an address; a source span is the selected material at
that address. Source support is the explicit attachment explaining which span
supports which assertion. A manifest, a resolving path, a readable conversion,
or upstream Ready status does not by itself establish source support. Compare
the relevant span and claim before making that assertion; an address without
accessible content leaves the support assessment unresolved.

## Construct Boundaries

These are conceptual attachment points, not a finalized schema or enum set.
Preserve the distinctions even when a simple card presents several in prose.

| Construct | Meaning and boundary |
| --- | --- |
| concept card | Durable organizing unit for one concept; may contain or reference multiple claims and their evidence/lifecycle records |
| claim | Substantive assertion, available as a finer-grained unit when support or lifecycle decisions differ within a card |
| source locator | Snapshot-bound address with its resource, kind, value and basis; does not state that content warrants a claim |
| source span | Identified portion of source material selected through locators; retain range conventions and preparation caveats |
| source support | Claim-to-span or other assertion-to-span attachment; distinct from bibliography, run provenance and extractor confidence |
| relationship edge | Identifiable relation with endpoints and meaning when support, provenance, conflict or lifecycle records must attach to the relation itself; simple card-local navigation need not become a runtime graph |
| competency question | First-class question used as a requirement, answerability/coverage target, verification target or retrieval probe; may also be obsolete or deferred |
| extraction run | Trace of source snapshot, method/prompt identity, actor scope, output set, old-card inputs and result references; includes worker provenance if parallel work actually occurs |
| validation result | Outcome and coverage of structural/consistency checks, such as required content and references; not semantic verification |
| verification result | Who or what checked which construct against which evidence, with scope and outcome; grounds the corresponding verification state |
| reconciliation result | Affected constructs, conflict, source support, disposition and rationale, with lifecycle/admission implications; grounds reconciliation state |
| preservation decision | Explicit disposition of prior-card value: preserved, superseded, rejected or unresolved with rationale; prior value must not disappear silently |
| memory admission | Decision about relying on a construct as durable semantic memory; separate from keeping an artifact or retrieving it |

CQ coverage records which cards, claims, support or edges address a question.
Coverage alone does not establish answerability: supporting assertions can
remain unverified, disputed or unsuitable for the intended use. A successful
retrieval probe is not memory admission.

## Distinct Evidence And Lifecycle Signals

| Signal | Question it answers |
| --- | --- |
| Evidence grade | What warrant does the claim or claim-source support have? |
| Extraction confidence | How direct, ambiguous or difficult was the extraction act? |
| Validation result | Which structural checks were performed, with what outcomes and coverage? |
| Verification state/result | What is currently verified, by whom or what, against which evidence, and within what scope? |
| Reconciliation state/result | Which conflicts were considered, resolved or left open, and why? |
| Preservation decision | What happened to each relevant piece of prior value? |
| Memory admission | May future cognition rely on this construct as durable semantic memory under the applicable gate? |

These are not one confidence score. Attach distinctions at the claim, support,
edge, CQ, card or run level where they matter. One supported claim does not
make every claim in its card verified. Passing validation cannot establish
semantic verification, resolve a conflict or authorize memory admission.
Admission depends on support, grade, validation, verification, reconciliation,
preservation and any human/operator acceptance required by the task.

## Operating Modes And Availability

**Human-Assisted:** the operator supplies source excerpts, artifacts or
observations that the assistant cannot directly inspect. Record who observed
what and the limits; a reported check remains distinct from direct inspection.

**Agent-Direct:** the assistant inspects accessible source and card artifacts
and records its own scoped observations. A same-context self-check is not an
independent verification result simply because it is performed later.

Both modes follow the [operator workflow](./02-operator-workflow.md) and the
same construct distinctions. In the [guide map](../SKILL.md#guide-map),
guides 01 through 10 are live. Use [extraction](./03-extraction.md),
[re-extraction and preservation](./04-re-extraction-preservation.md),
[evidence lifecycle](./05-evidence-lifecycle.md), and
[validation and verification](./08-validation-verification.md) as needed.
Use [relationships and CQs](./06-graph-cq.md),
[reconciliation](./07-reconciliation.md),
[memory admission](./09-memory-admission.md), and
[maintenance and package boundaries](./10-maintenance-packaging.md)
for those operations.
Sibling templates, representative examples, and reference/review support are
live. Consult the sibling reference index for documented field groups and review
boundaries. Package targets and generated zips now exist, including packaged
`references/`. README/docs discoverability remains Slice02 work; package-path
validation, isolated install smoke, and final package reconciliation remain
Slice03 work. Do not replace documented candidates with an invented canonical
schema or claim that an unavailable validator was run.
