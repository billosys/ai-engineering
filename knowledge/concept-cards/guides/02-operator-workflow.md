# Operator Workflow

Use this foundation after the [load contract](./01-load-contract.md) identifies
concept-card method work. It establishes actor roles, inputs, provenance and
result boundaries. Use the live [extraction](./03-extraction.md),
[re-extraction and preservation](./04-re-extraction-preservation.md),
[evidence lifecycle](./05-evidence-lifecycle.md), and
[validation and verification](./08-validation-verification.md) procedures
for the requested operation. The [guide map](../SKILL.md#guide-map) identifies
all live core routes. Choose only the work the operator requested.

## Establish The Task And Inputs

Identify the requested operation: creation/extraction, re-extraction,
validation, semantic verification, reconciliation, preservation, relationship/
competency question work, or memory admission. Record the target source/card
set, intended use and expected deliverable. Reviewing existing cards need not
be turned into a new extraction or a memory-admission task.

Inspect available source snapshots, prepared-source records, existing cards,
claims, support attachments, edges, CQs and prior result records. Identify
which revisions are inputs and where derived results belong. Preserve prior
inputs so later comparison can recover what changed. Missing material should
be named precisely, with the operation it prevents.

If raw PDF/EPUB/HTML or a converted bundle needs preparation, route that work
to `document-extraction`. Return with the prepared snapshot, manifest,
structure/media/locator records, readiness and caveats. Treat them as upstream
provenance: they identify content and preparation limits, not source support
for concept-card claims. If preparation is already adequate, consume its
records without repeating conversion. If the preparation skill is unavailable,
record the missing capability and continue only supported independent work.

## Record Scope Before Deriving Content

For extraction or re-extraction, identify an extraction run with the source
snapshot, method/prompt identity, actor and scope, expected output set, old-card
inputs and preparation-record references. Capture worker scopes and output
provenance if parallel work is part of the actual task; this foundation does
not prescribe a worker count or initiate delegation.

For other operations, identify the reviewed card/claim/edge/CQ revisions and
the relevant prior runs instead of inventing a new extraction event. Establish
what will count as a result and what remains unassessed. Use an existing
accepted record format when available; this scaffold does not supply a schema.

Keep the source primary when comparing new extraction with old cards. Prior
cards are comparison inputs, not substitutes for the source. Track their
unique value for an explicit preservation decision, including value that is
unsupported or unresolved; retaining its history does not endorse its truth.

## Maintain The Construct Boundaries

Organize a concept card around one concept. Retain claims as distinguishable
assertions wherever support, evidence grade or lifecycle state differs.
Identify the source span and source locator behind each proposed source
support attachment, then inspect whether the span warrants the assertion.
Do not introduce an inference as though it were a source statement.

Carry ambiguous locators, damaged conversions and unavailable originals into
the affected support assessment. Extraction confidence describes the extraction
act; it does not repair missing source support or raise evidence grade.

Identify relationship endpoints and whether the relation needs its own edge
identity for evidence, provenance or lifecycle handling. Keep competency
question coverage separate from answerability and retrieval success. Detailed
relationship and CQ rules are in the [relationship/CQ guide](./06-graph-cq.md).

When preserving or revising prior material, record what is retained,
superseded, rejected or unresolved and why. A rewritten card must not silently
erase a competing claim, prior source attachment or unique explanatory value.
Follow the live [re-extraction and preservation guide](./04-re-extraction-preservation.md)
for those detailed procedures.

## Human-Assisted Operation

Use this mode when the operator must supply files, source observations or
checks unavailable to the assistant. Request the bounded evidence needed for
the affected decision: the named card revision, a claim with its source span,
a typed locator and excerpt, the prior/new pair, or the relevant check result.
Do not treat a short excerpt as full-source inspection.

Label operator-reported observations, direct assistant inspection and
inference separately. Record which checks could not be reproduced and how
that limits the requested result. Return proposed record contents and intended
paths when file writing is unavailable; storage and delivery remain unverified
until established. An operator report is usable evidence with stated provenance,
not a reason to claim that the assistant performed the underlying check.

## Agent-Direct Operation

Inspect accessible files and their recorded identities before deriving or
reviewing content. Work within the requested scope and preserve inputs and
earlier results. Record the actual source/card set inspected, actions taken,
output revisions and unresolved material. Save results to the accepted home
and reopen them to check their references and snapshot associations.

Distinguish the assistant's own structural or semantic checks from independent
verification. Record another verifier's identity, evidence access and scope
only when that review actually happened. Do not claim that a check, memory
write or consumer handoff occurred merely because a plan names it.

## Keep Results Separate

Produce or update only the result records required by the operation, and mark
unperformed work as not assessed rather than implicitly successful:

- A validation result records structural and reference-consistency checks
  and their coverage. It does not settle semantic warrant.
- A verification result records the verifier, target, evidence, method, scope
  and outcome. Verification state must remain tied to that result and revision.
- A reconciliation result records conflicts, affected constructs, decisions,
  rationale and remaining issues. Reconciliation state does not become resolved
  merely because each competing card passes structural validation.
- A preservation decision records the disposition of prior value and its
  effect on the new output. Unresolved value stays traceable.
- A memory admission decision assesses the applicable source-support,
  evidence-grade, validation, verification, reconciliation and preservation
  requirements, plus any required operator acceptance. A valid file or completed
  extraction run is not automatic admission or a memory-runtime write.

Keep extraction confidence and evidence grade attached to their appropriate
subjects alongside these results. Do not average or overwrite these distinct
concerns into one card confidence field. Follow
[evidence lifecycle](./05-evidence-lifecycle.md) for assessments and
[validation and verification](./08-validation-verification.md) for scoped
checks and review provenance. Record schemas are not supplied by this foundation.

## Compose The Rich Readable Body

For real-corpus extraction, populate the rich body in the concept-card template
after establishing the one-concept boundary and claim/support plan. Cover the
definition, properties, recognition or construction, context, source-specific
examples, relationships/CQs, confusions, source/support map, and extraction
review boundaries. Write the main sections for someone learning or looking up
the concept: concise definition, usable properties, recognition cues, concrete
examples and helpful confusions first; compact audit detail second. Keep every
section, but record `not applicable`, `not established in the selected source`,
or `unresolved` with a reason instead of inventing generic prose.

Use the source/support map to make substantive body statements inspectable
without turning every teaching paragraph into a provenance paragraph. Examples
must identify their source-specific case, locator, and support rather than
merely sounding plausible. A rich explanation may describe a relationship or
question locally, but it does not create a typed edge or CQ record. Its
extraction/review-boundary section can point to actual results; it cannot report
validation, verification, reconciliation, acceptance, or admission by prose.

## Report The Handoff And Remaining Work

State the operation performed, input and output revisions/paths, run and source
identities, support/span references, preparation caveats, result records and
their scope. Name unresolved conflicts and preservation decisions, unperformed
checks, storage/delivery limits, and the next bounded inspection needed.
Make clear whether memory admission was requested or assessed at all.

All guides 01 through 10 are live. Use [relationships and CQs](./06-graph-cq.md),
[reconciliation](./07-reconciliation.md),
[memory admission](./09-memory-admission.md), and
[maintenance and package boundaries](./10-maintenance-packaging.md)
for the corresponding requested work. Sibling templates, representative examples,
and reference/review support are live. Package targets, generated zips, docs
and install integration, including package support for `references/`, are live.
No
executable validator or runtime enforcement is implied by a documentary result
record.
