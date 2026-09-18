---
project: project08-concept-card-metadata
arc: arc06-semantic-families-and-capability-requirements
slice: slice14-provenance-context-and-reference-semantics
status: closed
depends-on: [slice13-provenance-family-semantics, slice03-provenance-and-shared-reference-contracts]
version: "1.5"
---

# Actor Identity In Supporting And Result Records

Determine what actor and actor.id denote in the six remaining record kinds,
without treating record authorship, source support, validation, preservation
or admission authority as interchangeable. This is contextual inventory work,
not a normative actor model. Source and earlier evidence remain read-only.

## Current Assignment And Authority

Three-Contributor Workflow, authorized by the Operator on 2026-09-17:
CC implements; separate CRC reviews and handles routine advancement; CDC
retains design/escalation and arc/project composition. Expedited Mode applies.
See [the initial CRC directive](../../cdc-directive01.md) and the project
Design Handoff History. P-15 and every semantic criterion remain unchanged.

Final assignment: cc-prompt-iteration03.md, the bounded registered-range
correction after CRC review of executed iteration02. CC committed b10bb1ec
and separate recipe a4a7047c. CRC independently accepted all six rows in
crc-verification.md. No routine second CDC slice approval is required.
Slice15 remains unopened pending CDC sizing of the retained obligations.
The arc-level [CRC escalation](../crc-escalation01.md) requests that decision;
it does not reopen this slice or assign a successor.

### Assignment History

| Prompt path (slice-relative) | Issued | Predecessor | Reason | Disposition |
| --- | --- | --- | --- | --- |
| cc-prompt.md | 2026-09-17 | none | Initial 12-pair complement under CDC/CC | Superseded for routing; preserved unchanged; no execution recorded |
| cc-prompt-iteration01.md | 2026-09-17 | cc-prompt.md | Operator-selected CRC review and three-contributor transition | Executed at 60039753; CRC changes required in crc-verification.md |
| cc-prompt-iteration02.md | 2026-09-17 | cc-prompt-iteration01.md | Correct four CRC findings within the same six-row contract | Executed at ee80f914 with replay revision 3372da88; CRC R1-R4 resolved, R5 changes required |
| cc-prompt-iteration03.md | 2026-09-17 | cc-prompt-iteration02.md | Correct out-of-bounds registered reading ranges and make replay reject them | Executed at b10bb1ec with recipe a4a7047c; independently accepted by CRC; second corrective pass |

The routing replacement did not consume a refinement pass. Iteration02 was
the first executed corrective pass; iteration03 is the second requested pass.
Preserve all issued predecessors unchanged. CC does not write either reviewer
verdict, accept memberships, amend plans or open the next slice.

### Iteration03 Author Readiness

CRC inspected the current 42-row registry and literal route at planning
`eab5e69c`, independently replayed contribution `ee80f914` with recipe
`3372da88`, and resolved every numeric range at its declared evidence
revision. Four ranges exceed their pinned file lengths; the route does not
read `source_range`. The new prompt's `Inspected Baseline`, `Implementation
Spine And Code Shape`, and `Test Oracles And Required Gates` sections record
the source-grounded design, exact correction sites, an illustrative Bash/jq
predicate and falsifiable controls. Its `Baseline And Required Reading`
manifest bounds current plans and heavy artifacts while retaining full active
prompt/plan/ledger/registry/route reads and intake headroom. Applied source
guidance is cited in the prompt; JSON descriptors and historical prompts
remain explicit boundaries. This is author self-review, not acceptance.

## Exact Scope And Sizing

Exactly these 12 [field_path, record_kind] pairs:

~~~json
[
  ["actor","memory-admission"],
  ["actor","preservation-decision"],
  ["actor","relationship-edge"],
  ["actor","source-locator"],
  ["actor","source-support"],
  ["actor","validation-result"],
  ["actor.id","memory-admission"],
  ["actor.id","preservation-decision"],
  ["actor.id","relationship-edge"],
  ["actor.id","source-locator"],
  ["actor.id","source-support"],
  ["actor.id","validation-result"]
]
~~~

Opening live accounting: 188 accepted / 367 remaining / 12 assigned /
355 outside this slice. Assignment is not acceptance.
CDC sizing from the frozen inventory found 12 parsed object mappings:
memory-admission 2, preservation-decision 1, relationship-edge 2,
source-locator 1, source-support 5, validation-result 1.
Six templates have actor objects with null children; two synthetic examples
omit actor; four original Arc07 pilot supports record codex-cc / agent-direct /
extractor. Reproduce these as observations, not assumed fixtures or a rule
that an actor always means extractor. Record unexpected states and exclusions.

This stable directory was previously the unsized provenance complement.
Current assignment is only the 12 identity pairs. Planned Slice15 inherits
ALL remaining actor.mode/actor.role, run/preparation/method/shared-reference
and remaining CQ provenance responsibilities; size/split before execution.
Later evidence/validation/reconciliation/preservation/admission semantics
keep their Arc06 owners. All 355 outside pairs remain explicitly Arc06-owned.

Role/mode, validator_identity, decision_authority_ref, operator_acceptance,
source/subject/run identities and body content are mandatory context when
relevant, not added memberships. Do not borrow the four-kind Slice13 meanings
merely because these templates share the same mapping shape.

## Read Set

Read project AGENTS, current project/arc/slice plans and ledgers, source
collaboration-framework and project-management wayfinder with applicable
planning/work-verification guides, and concept-cards SKILL.md.
Read Slice13's final CDC review, semantic registry/evidence and handoff; reuse
the accepted limits and explicitly disclosed replay mechanics. Read Slice03's
evidence replay contract and final CDC notes selectively. Do not rerun every
historical iteration or rebuild an inventory framework.

Register and visibly read the relevant native inputs:

- Current and frozen project coverage registers; Arc01 Slice01
  artifacts/frontmatter-inventory.json and input-register.md.
- All six selected concept-cards templates, including full bodies.
- examples/memory-admission.md and examples/relationship-edge.md.
- All four populated original Arc07 Slice02 support records, their body context
  and at least one corresponding card for the actor/support-subject boundary.
  Locate exact paths from the inventory; distinguish synthetic from generated.
- references/record-field-groups.md; guides/02-operator-workflow.md,
  05-evidence-lifecycle.md, 08-validation-verification.md,
  09-memory-admission.md, and relevant preservation/edge guidance in
  04-re-extraction-preservation.md and 06-graph-cq.md.
  Full selected templates/examples/support records are required; focused
  guide sections are enough when registered with precise roles and ranges.
- Accepted Arc01 Slice07/08/09 and Arc06 Slice01 evidence only where actually
  cited to interpret locator, support subject, card linkage or edge endpoints.

For any cross-record inference, register/read its native target or explicitly
report no match/tool error. Do not add target-resolution work unrelated to
actor meaning. No new full-book or neuroscience support review.

## Semantic Work And Outputs

Exactly four supporting artifacts under artifacts/, plus ledger.md and
closing-report.md; no new helper, parser or schema:

1. semantic-membership.json: exact 12 memberships, effective field-specific
   meanings/dispositions, shared meanings with explicit applicability,
   exceptions and unresolved questions, and both layers of evidence IDs.
   Evidence includes root/path/hash/read mode/authority/role/reading range.
2. semantic-evidence.md: complete scoped native census, contextual comparison
   and concrete consequences for readers, extraction, queries and migration.
3. validation-evidence.md: a complete literal existing-tool replay with
   independently authored expected observations, actual outputs/statuses,
   fail-closed wrapper and committed/precommit modes.
4. handoff.md: conclusions/limits, concrete decision/test questions with owners,
   and a sized next provenance unit recommendation; no implementation authority.

Distinguish actor parent absence, null, empty mapping, unexpected type and
child missing/null/empty/populated/uninspectable states. Census all 12 native
records by kind and template/synthetic/generated family. Compare the exact
fields against 2,054 frozen legacy parsed mappings, reusing Slice13's result
only with explicit provenance and independently reproducible query.
Child-not-inspectable because parent is absent is NOT semantic inapplicability.
Do not count malformed inputs as parsed or infer denominator-wide absence
from sampled frontmatter.

For each kind ask what activity an actor might be attached to, what the
guidance actually specifies, what populated records demonstrate, and what
remains unknown. In particular:

- Source-support actor is not automatically source author, supported claim's
  actor, semantic verifier or truth authority.
- Locator actor is not addressed-resource identity or evidence of resolution.
- Edge actor is not an endpoint identity, relation direction or warrant.
- Validation actor and validator_identity are distinct slots until evidence
  establishes a relationship; do not invent equality or precedence.
- Preservation actor is not automatically an operator acceptance.
- Memory-admission actor, decision authority and operator-acceptance actor
  must be compared without inferring authorization from a populated label.

Retain exact labels and absent/null distinctions. Template-only meanings are
acceptable findings with inspected scope and concrete follow-up questions;
invented populated examples or vague blanket preservation are not evidence.

## Diagnostics And Replay

Two focused native diagnostics, not a new test framework:

1. Select a populated pilot support actor and inspect its subject/card context.
   Compare native actor value against an independently written expectation.
   Reject a wrong expected identity. Show why subject_ref/source_ref identifies
   something other than actor; equal labels do not prove principal equivalence.
2. Compare one result-record template object/null actor with the actual absent
   synthetic memory-admission actor. Inspect authority/acceptance context.
   Reject an expectation that collapses absence to null. Include successful
   no-match versus a real missing-input error on the actual lookup route.

Use the same predicates for positive cases and negative controls. Expected
objects must not be recycled as observations. No raw-search errors suppressed
as absence. Resolve both member and shared evidence layers; mutation controls
must reject an invalid member and a dangling reference. Derive/compare authored
census cells and hash every registered input. If using original/copy witnesses,
validate mappings through their manifests and bytes, not just filenames.

Pin opening planning authority using the actual clean opening HEAD after
CRC acknowledges/releases this assignment, and source evidence to its actual
source commit. The source
at planning was 020268248882358075b678bb855c0ac8d11b532a; the frozen inventory
is older evidence. Check relevant content before claiming correspondence.
A global HEAD advance alone is not relevant-source drift: compare registered
inputs and affected paths, report old/current commits and hashes, and stop on
material evidence change. Do not silently refresh the frozen inventory or
require live coverage to retain obsolete opening bytes.

Committed replay loads registry from CC_COMMIT; recipe revision is a separate
explicit REPLAY_COMMIT. Fail closed for missing commit/file/empty code. Keep
opening-to-CC contribution checks separate from later reviewer status. Record
source and planning cleanliness without overwriting unrelated work.
Precommit checks cover staged/unstaged/named-new union; committed checks name
all six files. Protect project/arc plans, coverage, Arc01, all earlier Arc06
packets and issued prompts. Check whitespace and JSON structure.

## Completion And Boundaries

Walk all six ledger rows against evidence. Commit only the six permitted files
with explicit names and required trailers, replay the committed endpoint,
then report CC proposed-done to CRC through the Operator. Do not claim
independent acceptance.
A reviewer who implements a repair needs another verifier.

No source edits, schema adoption, package/install/runtime changes, extraction,
memory writes, new parser/helper, Ruby/Python, task dispatch or model changes.
Use bounded Bash/jq/Git and existing tools. If this cannot fit with review
headroom, stop with an evidence-backed sizing proposal; keep requirements and
ownership, and do not start an unbounded batch hierarchy.

## Version History

- 1.5 (2026-09-17): Links the arc-level CRC sizing escalation after this
  slice's accepted closure. No Slice14 acceptance criterion or CC assignment
  changes; Slice15 remains unopened.

- 1.4 (2026-09-17): CRC independently accepts iteration03 and closes all six
  rows. Exactly twelve actor/actor.id pairs enter accepted coverage once:
  200 accepted / 355 remaining / zero assigned. Slice15 still requires CDC
  sizing; P-15 and arc/project gates remain open.

- 1.3 (2026-09-17): CRC review of the executed iteration02 packet reproduced
  R1-R4 repairs but found out-of-bounds registered reading ranges under S14-5.
  Issues preserved iteration03 with the same twelve pairs, six-row contract
  and six-file output fence. No acceptance or Slice15 opening occurred.

- 1.2 (2026-09-17): CRC review of iteration01 found R1-R4, recorded a
  changes-required verdict and issued iteration02 without changing scope.
  This history entry records the already-made 1.2 plan change; it does not
  retroactively alter that issued assignment.

- 1.1 (2026-09-17): Operator-selected three-contributor transition changes
  routine reviewer to CRC and current assignment to preserved sibling
  iteration01. Was: CDC/CC initial prompt. All 12 pairs, six rows, six-file
  implementation scope and evidence requirements remain unchanged.

- 1.0 (2026-09-17): After Slice13's independent closure, opens the 12-pair
  actor-identity complement. Was: unsized broader provenance owner; all other
  responsibilities move intact to planned Slice15 for sizing, not deferral.
