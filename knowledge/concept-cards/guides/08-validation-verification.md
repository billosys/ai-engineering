# Validation And Verification

Use this guide for bounded checks of concept-card artifacts and their evidence.
Use [evidence lifecycle](./05-evidence-lifecycle.md) to interpret warrant and
extraction confidence, [extraction](./03-extraction.md) for source support
capture, and [re-extraction](./04-re-extraction-preservation.md) when revisions
or prior value require comparison.

Structural validation asks whether the representation meets its declared
contract and references are consistent. Semantic verification asks whether the
identified assertion or relationship is warranted by the inspected evidence
within the stated scope. Keep their results separate from reconciliation and
memory admission. Do not label a file simply “verified” without specifying
which of these questions was answered and for which revision.

## Define The Review Before Checking

Identify the requested review, its target IDs/revisions and intended use, source
snapshots, support attachments, extraction runs and relevant prior results.
Record the actual contract or criteria to apply. An existing workspace format
can supply structural requirements; this guide does not invent a final schema.

List the properties and coverage the review needs, the evidence available and
the checks that cannot be performed. Separate whole-set reference inspection
from sampled semantic inspection. Name sampled claims/spans and why they were
selected; neither an unlabelled sample nor matching file counts establishes
full coverage. Keep the original requested scope visible if only part can be
checked. Agreeing on a smaller reported scope does not silently satisfy the
larger request.

## Record Review Actors And Evidence Provenance

| Actor or evidence context | What the result can claim |
| --- | --- |
| Same-context assistant check | The producing assistant performed the named structural or semantic checks; this can find errors and provide useful evidence, but is not independent verification. A new heading or later pass does not create independence. |
| Independent CDC or fresh-context check | A separate reviewer inspected/reproduced the named checks against identified artifacts and evidence. Record reviewer identity, access, context shared and actual observations; a fresh context or CDC label alone is insufficient. |
| Operator-reported observation | The operator reports the named observation with source/revision and scope. The assistant may assess that report but must not claim direct inspection of unseen material. |
| Direct human review | A human inspected the stated targets/evidence; record their role, method, scope, outcome and any relevant independence from authorship. Being human does not automatically make a review independent or exhaustive. |
| Tool/process check | A named tool/process with recorded version/settings checked particular properties on particular inputs. Its output is scoped evidence; a successful exit does not automatically establish semantic correctness or a final method verdict. |
| Unavailable evidence or reviewer | Record the gap and the result it prevents. A requested or scheduled review is pending, not performed; an inaccessible source is not silently counted as checked. |

If independent verification is requested or required, provide the reviewer the
target revisions, relevant source evidence, contract/criteria and enough context
to reproduce the work. Keep the producer's assertions identifiable as claims
to check. The reviewer must inspect evidence rather than merely endorse the
producer's report. Record what context and prior reasoning were shared so the
independence claim can be assessed. This guide does not itself commission
delegation or require a separate reviewer for every ordinary self-check.

Worker agreement is not independent verification: workers may share a prompt,
source error or earlier conclusion. Distinguish separate performance of a
check from independent origins of its evidence. Two reviews of the same source
can reproduce a support comparison without supplying two independent sources
for the underlying claim.

## Perform Structural Validation

1. Identify the accepted representation requirements and exact artifact set.
   Record which contract/revision is being checked. If required structure has
   not been defined, identify that gap instead of claiming schema conformance.
2. Check required fields/sections, IDs, declared types or allowed values where
   a contract defines them, and local path/slug uniqueness. List malformed,
   duplicate, missing or ambiguous records with their locations.
3. Follow source/support/run/result references and identify their target
   revisions. Check locator completeness and resolvable targets where accessible;
   record inaccessible or ambiguous references separately. Presence of a support
   field does not establish that its text supports the claim.
4. Check relationship endpoints, CQ coverage references and local dependencies
   for existence and structural consistency under the declared contract. This
   does not establish relationship meaning, answerability or runtime graph closure.
5. Check preservation and lifecycle references where required: do prior/new
   revisions and result subjects agree, and are claims of validation, verification
   or admission backed by the corresponding records? Presence of an admission
   record is not an admission decision by this validation pass.
6. Record each check's observed outcome and evidence. Identify omissions,
   unavailable checks and the limits of any tool used. Produce a validation
   result for the named contract, artifact revision and actual coverage.

Use pass/fail/not checked/not applicable with reasons, or the accepted local
equivalents. These descriptive outcomes are not a newly supplied enum schema.
A required field that is missing can fail a structural check even if the
underlying content is unknown; inability to inspect whether a source supports
a claim is a different, unresolved semantic question.

## Check The Rich Profile At The Correct Layer

For a rich-card contract, structural validation can check that every required
body section is present; sections without supported content carry an explicit
applicability reason; source-specific examples link recoverable locator/support
material; and extraction/review notes do not masquerade as lifecycle results.
It can also check that claims, source support, typed edges/CQs, and result
references remain separate rather than being replaced by rich prose.

For a teaching-oriented rich profile, review can also record a qualitative
readability observation: whether the main body is concise, concept-first,
source-specific, example-bearing and useful for lookup before audit. That
observation is not structural validation or semantic verification unless the
review defines and checks those criteria separately.

These checks do not determine whether prose is useful, an example is faithfully
represented, or support warrants an assertion. Those are semantic questions
against the identified source and its context. A rich body is not completed
review evidence, and its presence never supplies independent verification,
operator acceptance, reconciliation, or memory admission.

## Perform Semantic Verification

1. Select the exact claim, support relation, card assertion, edge or CQ coverage
   assertion and its revision. State what is being tested: faithful source
   representation, sufficiency of warrant for a named use, or another explicit
   semantic criterion. Do not promise every kind of correctness in one label.
2. Retrieve the cited source span and necessary context from the identified
   snapshot. Check locator interpretation and preparation caveats. If material
   is inaccessible or damaged, identify the blocked criterion and continue only
   independent checks whose evidence is available.
3. Compare the assertion with the span, including scope, conditions, negation,
   modality, units, exceptions and attribution. Distinguish source statements
   from assistant inference. Locate support for every substantive clause or
   name the unsupported parts. Use domain guidance where interpreting warrant
   requires it; record missing expertise rather than inventing confidence.
4. Inspect known contradictory or qualifying material within the agreed scope.
   Record what was searched/compared and what was not. An assertion that a source
   says X and an assertion that X is true need different warrant; do not upgrade
   a faithful paraphrase to an independently established fact.
5. For edge or CQ coverage targets, check the stated relation or coverage
   assertion against its own evidence and criteria. A valid endpoint reference
   is insufficient. Follow the [relationship/CQ guide](./06-graph-cq.md) for
   those procedures and identify unresolved questions without claiming a full
   graph or answerability audit.
6. Record the semantic observation, rationale, caveats and outcome: supported
   within scope, partial, not supported by inspected evidence, contradicted in
   the inspected context, or unresolved/unassessed as appropriate. Explain the
   distinction; lack of accessible evidence is not proof of falsity.
7. Produce a verification result and set or propose verification state only
   for the covered target/revision and review context. If independent checking
   remains required, leave that requirement pending even after a useful self-check.

Evidence grade may change following this work, but record the revised warrant
assessment separately with its rationale. Extraction confidence remains the
extractor's signal about the extraction act. Verification does not overwrite
either signal or resolve every conflict merely by having a successful outcome.

## Make Each Result Recoverable

For each validation result and verification result, record:

- result identity and kind; actor/reviewer, role, date and review context;
- exact target IDs, paths and revision identity, source/prepared snapshots and
  relevant extraction-run references;
- criterion/contract, method, tool/process version and settings if used;
- evidence pointers and observations, including who supplied them and what
  the reviewer actually inspected;
- intended scope, actual coverage, samples, exclusions and unavailable inputs;
- outcome and rationale, failed or unresolved properties, caveats and next checks;
- the resulting or proposed state on each covered target, with links to prior
  results and explicit applicability limits.

A result is a durable account of a check; verification state summarizes the
applicable checking status of a subject. Pending, self-checked, independently
checked, failed, unresolved and superseded observations must remain distinguishable
without assuming these words are the final schema vocabulary. A state label
without an applicable result is not evidence that checking happened.

Keep failures and later repairs traceable. If review finds a defect, record the
finding before an authorized repair; identify the repaired revision and rerun
affected checks. Do not edit a source or candidate and leave a pre-edit result
appearing to cover the new bytes. Unaffected results may remain applicable only
with an explicit identity/scope check. Preserve earlier observations rather than
rewriting them into successes.

## Prevent False Upgrades

- Valid structure is not semantic verification. Tool success and a resolving
  locator can support structural findings without establishing warrant.
- Support for one claim does not verify every claim in its card. Summaries must
  retain target-level coverage; a whole-card verdict needs evidence for its
  declared whole-card criteria.
- Successful extraction is not verification. Repeating the same reasoning,
  worker agreement or changing the reviewing actor's label does not establish
  independent verification.
- A validation result or verification result is not a reconciliation result.
  Competing supported assertions may still require a conflict disposition.
- Validation or verification is not memory admission. Preserve unresolved
  support, reconciliation and preservation questions; do not claim admission
  or a memory-runtime write from these checks.

## Human-Assisted Operation

In human-assisted work, ask for the bounded artifact, source context, tool log
or reviewer observation needed for a named criterion. Keep operator-reported
observations separate from direct reading of supplied records. An operator's
“looks good” does not establish the target, method or coverage of a full review.

Return a scoped result with unavailable checks and next actions. If unable to
write it, identify the intended destination and label storage unverified.
Do not claim an independent CDC result or direct source comparison that neither
the assistant nor the identified reviewer performed.

## Agent-Direct Operation

In agent-direct work, inspect the exact inputs, apply the relevant structural
and semantic steps, and retain actual observations from any available tools.
Write results separately from immutable prior evidence or as new revisions
under the workspace convention. Reopen them and follow target/evidence links.

Report the assistant's own review context honestly. If an independent reviewer
or necessary evidence is unavailable, leave that part pending and state the
bounded next step; do not manufacture independence by rerunning a check in the
same context. Continue checks that can be supported within the assigned scope.

## Handoff

Report the target revisions and intended/actual scope, validation results,
verification results and resulting states, actor and evidence provenance,
failures, partial or unavailable checks, caveats and next actions. Link any
separately revised evidence-grade assessment. Keep reconciliation state/result,
preservation decision and memory admission separately identified or unassessed.
State what additional work would support any broader or independent verdict.

In the [guide map](../SKILL.md#guide-map), guides 01 through 10 are live. Use
[relationships and CQs](./06-graph-cq.md),
[reconciliation](./07-reconciliation.md),
[memory admission](./09-memory-admission.md), and
[maintenance and package boundaries](./10-maintenance-packaging.md)
for their distinct follow-up decisions and boundaries. Sibling templates,
representative examples, and reference/review support are live. Package targets
and generated zips now exist, including packaged `references/`. README/docs
discoverability remains Slice02 work; package-path validation, isolated install
smoke, and final package reconciliation remain Slice03 work. This guide does
not supply an executable validator, runtime service or a claim of live
verification against a real corpus.
