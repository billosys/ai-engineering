# Source-Faithful Extraction

Use this guide to derive concept cards and claims from identified source
material. Apply the [load contract](./01-load-contract.md) and use the
[operator workflow](./02-operator-workflow.md) for task and actor boundaries.
When prior cards are comparison inputs, also use
[re-extraction and preservation](./04-re-extraction-preservation.md).

## Establish Source And Preparation Identity

1. Identify the requested source coverage and purpose, including exclusions.
   Inspect what is actually accessible before promising a complete card set.
   Distinguish the full requested scope from a supplied excerpt or sample.
2. Identify the source snapshot: title/edition if known, stable source ID,
   file/resource, revision or capture identity, and a checksum when practical.
   Record unknown identities explicitly. A title or URL alone does not identify
   the bytes inspected; a new edition or web retrieval is a new input snapshot.
3. If prepared-source records are present, retain their prepared snapshot/run,
   original or supplied input, manifest, locator/structure/media maps,
   readiness report and caveats. Check which files and regions they cover.
   A preparation run and this concept-card extraction run are separate traces.
4. Read source structure and representative content: definitions, qualifications,
   examples, counterexamples, tables, figures and closing context relevant to
   the task. Account for content outside the readable text representation.
5. Route raw PDF/EPUB/HTML preparation, damaged conversion, media repair or
   locator-basis investigation to `document-extraction` when needed. Do not
   alter prepared source text to make it support a preferred claim. Preserve
   the original snapshot and cite any later repaired snapshot separately.

Usable source material need not first acquire a document-extraction manifest.
Record the identities and limitations available for the actual source. When
that skill's outputs are used, they are upstream provenance, not source
support by themselves. Its Ready status neither warrants a claim nor supplies
a concept-card verification result. If original fidelity is unchecked, retain
that caveat even when extraction from the supplied representation can proceed.

## Establish The Extraction Run

Give the extraction run an ID before producing derived content. Record:

- source IDs and input snapshot/revision identities, prepared-source record
  references if any, and old-card inputs when applicable;
- method/prompt identity and revision, material settings or instructions that
  affect extraction, actor identity, time and bounded source/task scope;
- intended outputs: card set or concept area, claims, support attachments and
  any requested edge/CQ candidates; use provisional scope when the number of
  concepts is not yet known rather than imposing an arbitrary card count;
- the actual generated/updated output IDs, revisions and paths as work proceeds,
  including partial output, omissions and remaining coverage;
- references to check observations, caveats, preservation decisions and any
  separately performed validation, verification or reconciliation results.

If parallel work actually occurs, record each worker's identity, input
snapshots, assigned coverage, relevant prompt variation and returned outputs.
Keep overlap, gaps, disagreements and integration decisions visible in the
parent run. Do not present overlapping worker output as independent support
for a claim, or infer a verification result from worker agreement. No worker
count or delegation is required by this guide.

## Select Concept Boundaries

Work through the requested source scope in its meaningful order. Identify
candidate concepts from definitions and explanatory relationships, not every
heading, keyword or paragraph. For each candidate, state what the concept is
and what adjacent material belongs elsewhere. A section may contain several
concepts; one concept may draw on several sections.

Keep one concept per card. Group claims that explain that concept together,
but separate concepts with distinct definitions, mechanisms or use conditions
when one summary would obscure their identity. Record unresolved boundary
choices instead of choosing a broad umbrella merely to avoid a split. Do not
turn every finer-grained claim into a separate card without a concept reason.

Compare repeated terms in context before merging them: aliases can name the
same concept, while identical labels can have different senses or source-specific
definitions. Keep the source terminology and qualifications recoverable.
Assign stable candidate/card identities using the accepted workspace convention;
do not repoint an existing ID solely because a title or filename is convenient.
Send competing identities or definitions to later reconciliation with evidence.

## Extract Claims And Respect The Source

For each concept, formulate substantive claims in concise, source-faithful
language. Retain conditions, quantifiers, modality, scope, units and exceptions.
Distinguish the author's definition, reported observation, hypothesis,
recommendation and illustrative example. An example is not automatically a
universal rule; a reported hypothesis is not an established fact.

Separate claims when different clauses need different spans, caveats or
evidence assessments. A compound claim must not inherit support for all its
parts from a span that supports only one. Keep supporting context for a
paraphrase; do not strengthen “may” into “does” or erase a limiting condition.

Prefer synthesis over copying prose. Retain short verbatim excerpts only when
needed to inspect wording or support, with their exact locations and surrounding
context. Mark quotations, omissions and editorial additions clearly. Inspect
table headers, units, notes, captions and figure context before asserting a
claim derived from them; an image path or OCR string is insufficient.

Label a source statement separately from assistant inference, external domain
knowledge or a proposed explanation. If an inference is relevant to the task,
record its premises and reasoning as an inference with its own unresolved or
reviewed status; do not attach a span as though the source states the inference.
Do not add plausible missing content to complete a damaged extraction. Retain
the candidate and its limitation, or withhold the unsupported assertion.

## Capture Locators, Spans And Source Support

For every proposed support attachment:

1. Identify the claim and the source snapshot/resource being inspected.
2. Record a source locator with kind, original value, basis and target context.
   For PDF, keep physical ordinal/base, converter page index and printed label
   distinct. For EPUB/HTML, retain resource paths and anchors/fragments with
   capture identity. For text lines, name the file revision, numbering base
   and inclusive/exclusive endpoints. Heading text alone may be ambiguous.
3. Select the source span: the actual portion of material needed to assess the
   claim, including qualifications and necessary context. Record start/end or
   other recoverable boundaries. Multiple spans may support different aspects
   of one claim; retain each rather than pretending they form one quotation.
4. Keep original and prepared/output locators separate and retain mapping
   evidence. If only prepared-source coordinates are known, state that scope;
   never invent an original page or silently assume a page-number offset.
5. Compare the selected span with the proposed claim. Record what it supports,
   the basis for that reading, who inspected it and the coverage of the check.
   Consider contrary or qualifying context in the inspected material. A shared
   word, topic match or bibliographic citation is not sufficient source support.
6. Assert a source support attachment only to the extent justified by that
   comparison. If partial, narrow or separate the claim, or retain the unsupported
   portion explicitly unresolved. If the span is missing, ambiguous or damaged,
   record the failed attempt, alternatives and next bounded inspection without
   representing it as a successful support assertion.

The source locator addresses material; the source span selects it; source
support states its relation to a particular assertion. Extraction run provenance
records how the output was produced. None substitutes for the others. A check
that the source says something also does not establish that the source's claim
is true in the world or has adequate evidence grade for every downstream use.

## Record Confidence And Check The Output

Record extraction confidence at the claim, card or run level where it is
informative, with a reason tied to the extraction act: direct definition,
ambiguous wording, synthesis across passages, or uncertain conversion. If a
workspace uses a scale, name its meaning; do not invent precise numeric
certainty. A clear extraction from a weak source can still have weak warrant.

Inspect the actual output for one-concept boundaries, claim/span correspondence,
recoverable locators, retained qualifications, inference labels and caveats.
Reconcile intended versus inspected coverage and list omitted/unresolved material;
counts alone do not establish completeness. Check referenced output identities
and revisions rather than assuming a saved file is the intended card.

Keep extraction confidence separate from evidence grade and verification state.
A validation result concerns structural checks; a verification result records
semantic checking with its actor, evidence and scope; a reconciliation result
handles conflicts; a preservation decision accounts for prior value; memory
admission is a separate reliance decision. Record what was performed and leave
unperformed work unassessed. Follow the live
[evidence lifecycle](./05-evidence-lifecycle.md) and
[validation and verification](./08-validation-verification.md) guides for
those assessments and checks. Extraction self-review is not independent
verification; use [memory admission](./09-memory-admission.md) for a
separately requested reliance decision.

## Human-Assisted Operation

Ask the operator for the bounded missing input: source identity and locator,
the passage with surrounding qualifications, a table with headers/notes, or
the relevant prepared-source caveat and mapping. Establish which part of the
requested coverage those observations represent before deriving claims.

Record operator-reported checks separately from directly inspected excerpts and
assistant inference. Return candidate cards, support rationale and unresolved
questions with intended output paths when unable to write. State that storage
and file references remain unverified. Do not claim to have read the full source
or compared a figure because an operator supplied a summary.

## Agent-Direct Operation

Inspect accessible snapshots and use the steps above to derive candidates and
support attachments within the requested scope. Keep source inputs unchanged,
write derived records to the accepted destination, and record actual paths and
revisions in the run. Reopen the outputs and follow their source/span references
against the identified snapshot. Capture gaps and failed checks as observations
before attempting a bounded repair through the appropriate workflow.

Stop the affected claim/support assertion when evidence is insufficient;
continue independent supported work. Do not widen a corpus, refresh a source or
rewrite previous cards merely to eliminate a caveat from the report.

## Handoff

Report the extraction run, source/prepared snapshots, actual output set and
coverage; candidate concept boundaries and claims; locator/span and source
support references; extraction confidence reasons; inference labels; preparation
caveats and unresolved support. Identify any attached validation result,
verification result, reconciliation result or preservation decision by its own
scope and provenance. State whether memory admission was requested or assessed;
completed extraction is not automatic admission.

Name the next inspection for each blocking gap and preserve the partial output
for review. Use the live [evidence lifecycle](./05-evidence-lifecycle.md) and
[validation and verification](./08-validation-verification.md) routes when
assessing these outputs. In the [guide map](../SKILL.md#guide-map), guides
01 through 10 are live. Route edge/CQ work, conflicts and reliance decisions to
[relationships and CQs](./06-graph-cq.md),
[reconciliation](./07-reconciliation.md),
[memory admission](./09-memory-admission.md), and
[maintenance and package boundaries](./10-maintenance-packaging.md).
Arc04 owns future templates,
examples, validation/reference support and schemas; Arc05 owns package targets,
generated zips, docs and install integration. This is procedural guidance,
not an executable validator, runtime service or claim of a completed corpus run.
