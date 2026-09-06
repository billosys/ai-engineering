# Evidence Lifecycle

Use this guide to record what supports a concept-card assertion, what that
support warrants, and which lifecycle questions remain open. Use
[extraction](./03-extraction.md) to capture claims and spans, and
[validation and verification](./08-validation-verification.md) to perform
checks and record their results. The [load contract](./01-load-contract.md)
defines the underlying constructs.

## Identify The Subject And Its Evidence

Start with the particular claim, support relationship or other assertion and
its revision. Record the intended use, source snapshot, extraction run and
available prior assessments. Do not begin by assigning a whole-card confidence
value; claims within the same card can have different evidence and review states.

A source locator addresses material in an identified resource/snapshot. A
source span is the selected material, including the context needed to interpret
it. Source support is the attachment that states which span supports which
assertion and why, after the span and assertion have been compared. It is not
the bibliography, a filename, or the extraction run's production history.

When `document-extraction` supplied the source, preserve its snapshot, manifest,
locator mapping, readiness and caveats as upstream provenance. Inspect the
selected material and limits before asserting support. A preparation report
can establish where text came from without establishing that it warrants a
claim. Unavailable originals or damaged tables remain limitations on what can
be assessed from the prepared representation.

## Place Each Signal On Its Actual Subject

Record stable IDs/revisions and explicit attachment scope. These attachment
points are conceptual guidance, not a finalized schema or fixed enum vocabulary.

| Subject | Appropriate attachment and scope |
| --- | --- |
| Claim | Source support, evidence grade, extraction confidence, and applicable validation, verification, reconciliation, preservation and admission records for this assertion |
| Claim-source support relationship | Selected source spans, rationale for the support relation, warrant attributable to that evidence, and checks of the relation itself |
| Concept card | Concept identity, provenance and summaries of constituent assessments with their actual coverage; card-level confidence describes extraction of the card, not every claim's warrant |
| Relationship edge | Evidence and scoped checks of the relation and endpoints, plus conflict/result references when applicable; supported endpoints do not automatically support the edge |
| CQ coverage assertion | Evidence and checks for the assertion that named material addresses a particular competency question; a reference count does not establish answerability |
| Extraction run | Source/method/actor and worker provenance, output set, run-level extraction confidence if useful, and links to scoped result records; the run cannot confer a common grade on its entire output |

Use finer-grained attachments when material differs. If one span supports only
one clause, do not attach its grade to an entire compound claim. Keep source
support attached to the relevant assertion even when the physical record is
stored inside a card or run document.

## Assess Evidence Grade As Warrant

Evidence grade describes warrant on a claim or claim-source support relationship.
It does not describe how sure the extractor feels. Assess it with a rationale:

1. State the exact assertion and intended scope. Distinguish “the source
   reports X” from “X is established”; the latter requires more than confirming
   the source's wording. Preserve attribution, conditions and uncertainty.
2. Inspect each cited span and necessary context in its identified snapshot.
   Check whether the evidence addresses the whole assertion, its qualifiers and
   the intended use. Record uninspected regions and unsupported parts.
3. Identify the kind of warrant actually available: a definition, an argument,
   an observation, a reported study, an example, or another stated basis.
   Explain limitations relevant to the claim using domain guidance when needed.
   Direct wording establishes explicitness, not universal reliability.
4. Inspect known counterevidence, competing interpretations and source
   dependencies within the authorized review scope. Repeated citations to the
   same underlying observation do not create independent corroboration. Do not
   imply an exhaustive literature search when only supplied sources were checked.
5. Record the grade or a descriptive warrant assessment, the rubric used if
   one is established, assessor, evidence references, revision, scope, date and
   rationale. Mark a provisional judgment as provisional and explain what could
   change it. If no rubric is defined, use an explicit rationale rather than
   inventing canonical labels, thresholds or a numerical conversion.

Keep per-support assessments distinct when sources warrant different parts or
have different limits. A claim-level synthesis must explain how those parts
compose and where disagreement remains; it is not an average of grades or a
count of agreeing sources. Do not silently broaden the claim or its use after
grading it. Record the assessment as unassessed when evidence or expertise is
unavailable, rather than copying a grade from another claim or earlier run.

## Record Extraction Confidence Separately

Extraction confidence concerns the extraction act: directness of wording,
ambiguity, difficulty locating context, synthesis across passages or conversion
uncertainty. Attach it to the claim, card or extraction run it describes, with
the extractor, basis, inspected scope and rationale. If an accepted scale is
used, preserve its meaning and identity; otherwise describe the uncertainty.

A plainly stated but weakly evidenced claim can have high extraction confidence
and weak warrant. A well-supported claim can be difficult to extract from a
damaged representation. Neither circumstance licenses deriving evidence grade
from extraction confidence or the reverse. Confidence does not establish source
support, a validation result, verification, reconciliation, preservation or
memory admission. Do not recalculate an old extractor's confidence as though
it were a new observation by that actor.

## Record Evidence Gaps Without Upgrading Them

| Observation | Record and next step |
| --- | --- |
| Insufficient evidence | Name the missing support, inaccessible source or failed support comparison and its affected assertion; distinguish these causes. Withhold the unwarranted conclusion and identify the bounded input/check needed. |
| Partial support | Name supported and unsupported clauses or use conditions. Narrow/split the assertion with traceable revisions when appropriate, or leave the remainder unresolved; do not report whole-claim support. |
| Conflicting evidence | Retain the competing spans, source identities, interpretations and their limitations. Record the disputed assertion and conflict for reconciliation; agreement counts do not settle it. |
| Unassessed evidence | State what was not inspected and why. A pending check is not a failed check, but neither is it a successful result. |
| Stale assessment | Identify the changed claim, source, mapping or method assumption; retain the old assessment with its revision and assess applicability before reusing it. |

These are descriptions of evidence conditions, not a replacement status schema.
Attach caveats to affected claims/support records and carry their IDs through
the handoff. If new evidence resolves a gap, retain the prior observation and
record the evidence, actor and scope that changed the assessment. Do not erase
history merely because the current candidate reads more confidently.

## Maintain Separate Lifecycle Records

Use [guide 08](./08-validation-verification.md) for the validation result and
verification result. The validation result records structural/reference checks;
the verification result records who checked meaning or support, against what,
and with what outcome. Verification state is a current scoped summary grounded
in applicable results; the result record is the durable observation. A pending
review, same-context check and independently reproduced check must remain
distinguishable, including when their outcome wording is similar.

Reconciliation state describes conflict handling; the reconciliation result
records a particular disposition and rationale. A preservation decision records
what happened to prior value, as described in
[re-extraction and preservation](./04-re-extraction-preservation.md). Memory
admission concerns permission to rely on material as durable semantic memory.
None is inferred from a grade, a valid file or successful extraction.

On a material revision, identify the changed targets and dependent claims,
support relations, edges or CQ coverage assertions. Keep old records attached
to their old revisions. Check whether each prior result still applies and
record that check; require a new assessment where its basis no longer matches.
Do not silently transfer a verified state to revised content or downgrade the
historical record by overwriting it. A path-only move still needs identity and
mapping evidence if consumers cite the previous location.

Do not force the concerns into a single linear completion flag. A structurally
valid card may have unresolved support; a verified assertion may still have a
conflict or preservation issue. Report the actual combination. Follow
[reconciliation](./07-reconciliation.md) and
[memory admission](./09-memory-admission.md) for those decisions; recording open
questions here does not perform them or implement runtime enforcement.

## Human-Assisted Operation

Request the specific evidence needed for the assessment: the claim revision,
source span with context, locator basis, prior grade rationale or disputed
observation. Label operator-reported source inspections separately from what
the assistant can directly read. A screenshot or summary may establish an
observation without supplying the complete source or its recoverable locator.

Return the proposed assessment, rationale, scope and missing checks when access
is partial. Do not manufacture an independent result from an operator's general
agreement. If records cannot be saved, provide intended locations and state
that durable storage and cross-reference checks remain unverified.

## Agent-Direct Operation

Inspect accessible target revisions and evidence, then record assessments and
their attachments using the accepted workspace representation. Preserve prior
results and source snapshots. Reopen records, follow their references and check
that grade, confidence and lifecycle summaries name the intended subjects.

Record unavailable evidence before proceeding with supported independent
checks. A failed source comparison limits the affected assessment; it does not
justify inventing a replacement span or refreshing an entire corpus. Keep the
assistant's own observations distinguishable from external review results.

## Handoff

Report target IDs/revisions, source spans/locators, support attachments,
evidence grade with rubric/rationale, extraction confidence with its separate
reason, check/result references and coverage. Include insufficient, partial,
conflicting, stale and unassessed evidence, applicable caveats, preservation
decisions and the next bounded inspection. State verification and reconciliation
states separately from their result records and leave memory admission
unassessed unless the authorized [admission procedure](./09-memory-admission.md)
supplied a decision.

In the [guide map](../SKILL.md#guide-map), guides 01 through 10 are live. Use
[relationships and CQs](./06-graph-cq.md),
[reconciliation](./07-reconciliation.md),
[memory admission](./09-memory-admission.md), and
[maintenance and package boundaries](./10-maintenance-packaging.md)
for the corresponding follow-up work. Arc04 owns future templates,
examples, validation/reference support and schemas; Arc05 owns package targets,
generated zips, docs and install integration. This guide is not a validator
program, runtime service or evidence of validation against a real corpus.
