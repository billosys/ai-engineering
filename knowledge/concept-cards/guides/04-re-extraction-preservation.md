# Source-Primary Re-Extraction And Preservation

Use this guide to derive a new extraction from an identified source and then
compare it with prior cards without silently losing prior value. Apply
[source-faithful extraction](./03-extraction.md) for concept boundaries,
claims, source locators/spans, support and extraction-run records. Preserve the
[load contract's distinctions](./01-load-contract.md#construct-boundaries).

## Inventory Before Rewriting

Identify the requested card set and re-extraction scope. Preserve the prior
snapshot, including its paths and revision identity, before producing a new
candidate set. Inventory all affected material, not just the visible card text:

- prior cards and claims, concept identities, titles/aliases and filenames;
- source support attachments, source locators, source spans and their source
  snapshots, including missing or damaged references;
- relationship edges, endpoints and incoming/outgoing references; competency
  questions, coverage assertions and affected answerability dependencies;
- extraction run records, old-card inputs, method/prompt identities and actor
  scopes; prior validation, verification, reconciliation and admission records;
- preservation decisions, operator annotations, qualifications, examples,
  counterexamples or explanations that may be unique prior value.

Record missing records, inaccessible dependencies and the scope of the inventory.
An unavailable prior card is not evidence that it had no value. Inventorying
the prior set establishes what must later be accounted for; it must not make
old prose the template from which new claims are derived.

## Establish The Source Baseline And New Run

Compare source identity across the old and intended new run: source edition,
capture, file revision, selected coverage and prepared-source snapshot. Check
whether change is in the original source, the conversion, a locator mapping,
or merely the filename. A stable title or URL does not rule out source drift.
Keep the old and new identities even when their text appears similar.

When document preparation is needed, route it to `document-extraction` and
retain its manifests, maps, readiness reports and caveats as upstream provenance.
Do not normalize the only old snapshot in place or transfer old line numbers
onto regenerated text. Record any observed equivalence and its check scope.

Give the re-extraction run its own ID. Record its source/prepared snapshot,
method/prompt identity, actor, scope and time, prior run references, exact
old-card input revisions, expected candidate output set and actual output
revisions. Capture source drift, unavailable inputs and preparation caveats.
The new run must refer to the old run without rewriting the old run's evidence.

If parallel work actually occurs, retain each worker's inputs, source coverage,
old-card access, prompt variation, returned candidates and unresolved findings.
Record overlap and integration decisions. A worker's agreement with old prose
is not source support or independent verification; disagreements remain inputs
to reconciliation rather than being silently resolved by majority count.

## Derive Against Source First

1. Read the identified source within the requested scope, including context
   needed for qualifications and support. If the source is unavailable, record
   that limitation; do not call a rewrite of old cards source re-extraction.
2. Derive candidate concept boundaries and claims from that source using
   guide 03. Record source locators, source spans and support comparisons,
   separating source statements from assistant inference.
3. Keep that source-derived candidate set identifiable before integrating
   prior-card content. Existing cards may have been inventoried, but their
   wording and prior lifecycle status cannot substitute for this source check.
4. Compare the candidate set with prior cards by concept identity, claim meaning,
   scope and support, not just title, slug or string similarity. Record matches,
   changes, absent candidates, new coverage and unresolved boundary choices.
5. For each relevant piece of unique prior value, inspect its source basis or
   retain the lack of one explicitly. Give it a preservation decision before
   finalizing the affected output; an empty diff or a shorter new card is not
   proof that all prior value survived.

New extraction is source-primary. Prior cards are comparison inputs, not the
authority for what the source says. When a prior insight remains useful but is
an inference or an unsupported annotation, preserve its history and identity
without relabelling it as a source statement.

## Compare Changed, Unchanged And Unavailable Material

| Situation | Required treatment |
| --- | --- |
| Unchanged claim and source | Compare the claim's meaning, qualifications and support span; record the match and inspected scope. Preserve identity where appropriate, but do not claim new verification merely because text matches. |
| Changed claim | Record old/new assertions and the reason: source change, corrected extraction, changed scope or an unresolved interpretation. Attach new support as justified; keep the old assertion and result references recoverable. |
| New source coverage | Identify the newly inspected span and new candidates separately from revisions to existing concepts. Do not describe the old run as deficient for coverage it never attempted. |
| Source drift | Identify old/new snapshots and affected constructs. If the old source is accessible, compare both; if not, leave the explanation of the difference uncertain rather than asserting that the author changed a claim. |
| Unavailable source | Preserve old material and its recorded evidence as historical inputs; current source support assessment remains unchecked. Report partial comparison or blocked re-extraction, and name the missing source needed. |
| Damaged conversion or ambiguous locator | Withhold affected support conclusions; retain old and damaged representations. Request a bounded source comparison or preparation repair, then use a new snapshot/mapping when appropriate. |
| Unsupported prior material | Record whether no support is recorded, recorded support is inaccessible, or inspected material fails to support it. These are different findings; absence from a sample is not proof of falsehood. Preserve unique value as historical/unresolved material unless a justified disposition says otherwise. |
| Prior concept absent from new candidates | Check old scope, synonyms, changed boundaries and missed source regions before disposition. Distinguish genuinely out-of-scope content from an extraction omission; do not delete by absence alone. |
| Split or merged concept boundary | Map old IDs to new candidates and affected claims, edges and CQ references; do not silently reuse one old identity for a different concept. Preserve alternatives for later reconciliation when unresolved. |

An unchanged claim can acquire changed support or caveats. A changed filename
can leave meaning unchanged while breaking references. Record these dimensions
separately and check the affected mappings rather than assigning one undifferentiated
“changed” status to the whole card.

## Record Preservation Decisions

Make each preservation decision retrievable by a stable ID or unambiguous
record reference. Name the old constructs/revisions, the unique value at issue,
the inspected source basis or missing evidence, the new destination/replacement
if any, the decision, rationale, actor/run and downstream implications.

| Disposition | Meaning and record needed |
| --- | --- |
| preserved | Value is retained at a named destination or remains explicitly retained historical material. Specify which, with limitations; retention does not imply support, truth or admission. |
| superseded | A named new construct/revision replaces the old representation for a stated reason. Keep old/new links and prior evidence; do not overwrite the history of what was asserted. |
| rejected | Value is intentionally excluded from the new active set with explicit evidence and rationale. Preserve its old record and decision trail; exclusion for scope is not the same as proving a claim false. |
| unresolved | Evidence or a boundary/conflict decision is insufficient. Keep the material identifiable, explain what remains undecided and name the re-entry inspection. Do not quietly select a winner in the active output. |

These are preservation meanings, not a finalized schema or executable decision
rule. Record separate decisions when parts of one card have different outcomes.
A grouped decision is acceptable only when it names every affected construct
and the same rationale applies to all of them.

Trace unique prior examples, explanations, qualifications and annotations to
their destinations or dispositions. If their source support is absent or
memory admission was never granted, that limits reliance but does not authorize
silent loss. Keep unresolved material distinguishable from active supported
claims so future readers do not mistake historical retention for endorsement.

## Review The Candidate Set And Its Dependencies

Account for every in-scope prior construct using an old-to-new/decision map;
list unavailable or uninspected inputs separately. Check whether a retained,
superseded or split card leaves dangling relationship endpoints, claim support
attachments or CQ coverage references. Record the needed changes and unresolved
dependencies. Do not invent replacement edges or CQ answers to make the map
look closed; follow the [relationship/CQ guide](./06-graph-cq.md) for their
semantic handling.

Keep extraction confidence about this run separate from evidence grade about
warrant. Preserve prior validation result, verification result and reconciliation
result records with the revisions and evidence they assessed. Before treating
an old result as applicable to a new output, inspect whether its target,
support and scope still match and record that applicability check. Changes do
not automatically erase historical evidence or confer its status on new claims.

A preservation decision does not resolve every conceptual conflict. Record
competing claims and affected dependencies for
[reconciliation](./07-reconciliation.md); do not report a
reconciliation result that has not been produced. Likewise, retaining an old
[memory admission](./09-memory-admission.md) record documents a prior decision,
not a fresh admission for
revised claims. State what needs renewed assessment without claiming to update
a memory runtime.

## Human-Assisted Operation

Ask for the identified source span and the relevant old/new card or claim
revisions, including source support and prior result references. For source
drift, request the particular old/new passages and snapshot identities needed
to distinguish edition changes from conversion or interpretation changes.
For missing prior value, ask for the annotation or explanation itself rather
than relying on a summary that it was “preserved.”

Label operator-reported observations and partial inventories distinctly from
direct inspection. If the operator cannot supply the source, produce an
inventory, proposed comparison or unresolved preservation record with that
limit; do not claim completed source-primary re-extraction. When unable to save
records, provide intended paths and state that durable storage is unverified.

## Agent-Direct Operation

Inspect and identify accessible old artifacts and source snapshots, derive the
source-first candidate set, then perform the comparison and preservation steps.
Write new candidates and decision records separately from preserved prior
inputs; use the workspace's revision convention without destructive replacement.
Reopen outputs and follow old/new, source/support and decision references.

Record omissions, unresolved comparisons and affected dependencies before
finalizing the output set. Continue supported source regions while stopping
the affected unsupported assertion or disposition. If a source repair or new
snapshot changes the basis, recheck affected claims and mappings rather than
retroactively updating an old locator's meaning.

## Handoff

Report the re-extraction run ID, old/new source and card revisions, actual
coverage and output paths; the source-derived candidates; claim/support/span/
locator comparisons; and every preservation decision with its destination,
rationale and unresolved work. Include worker scopes when present, unique
prior value retained outside the active set, source drift and conversion
caveats, changed dependencies and the bounded checks needed next.

Keep validation result, verification result, reconciliation result, evidence
grade, extraction confidence and memory admission distinct in the report.
Explicitly state which were not assessed. Completing re-extraction and
preservation does not establish full validation, independent verification,
reconciliation or durable-memory eligibility.

Use the live [evidence lifecycle](./05-evidence-lifecycle.md) guide for
assessments and [validation and verification](./08-validation-verification.md)
for checks of revised outputs and prior-result applicability. In the
[guide map](../SKILL.md#guide-map), guides 01 through 10 are live. Follow
[relationships and CQs](./06-graph-cq.md),
[reconciliation](./07-reconciliation.md),
[memory admission](./09-memory-admission.md), and
[maintenance and package boundaries](./10-maintenance-packaging.md)
for changed dependencies and subsequent decisions. Sibling templates and
representative examples are live support. Schema/reference and validation-review
support remain future until Slice03; Arc05 owns package targets, generated zips,
docs and install integration. This guide supplies no executable
validator, runtime service or real-corpus execution evidence.
