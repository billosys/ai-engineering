---
project: project08-concept-card-metadata
arc: arc06-semantic-families-and-capability-requirements
slice: slice03-provenance-and-shared-reference-contracts
status: active
depends-on: [slice02-competency-questions-and-answerability]
version: "1.0"
---

# Reusable Evidence And Replay Contract

Make the next semantic-family packets easier to produce and independently
verify, using working examples rather than a general-purpose framework.
This is a local planning-evidence contract, not the future concept-card schema
or specification. P-15 remains open.

## Sizing And Ownership

The former combined Slice03 hypothesis mixed actor/run/preparation semantics
with replay infrastructure. Even actor/actor.id/actor.mode/actor.role alone
span ten record kinds (40 remaining pairs); adjoining run, method, preparation
and result references add many more contexts. That is not one bounded task
with comfortable review headroom.

Split before execution: this slice owns reusable evidence/replay mechanics.
New Slice13 (provenance-family semantics, to size/split before opening) inherits
ALL original actor/run/preparation/shared-reference semantic analysis, including
CQ provenance interfaces from Slice02. Arc06 retains primary ownership of all
375 remaining pairs until exact future assignments are opened. No obligation
is deleted and this slice accepts zero semantic pairs.

Do not build a parser, checker framework, source-skill update, package or
production runtime here. Do not reinterpret the accepted 180 pairs.
If new reusable tooling is justified, describe its bounded follow-up scope
and tests; do not implement it inside this documentation slice.

## Read Set

Read project/arc plans and ledgers, project AGENTS, this open set, current
project-management/work-verification guidance, and the final Slice02 CDC closure.
Inspect Slice02's current registry, validation block and query cases. Read
Slice01/Slice12 final findings only for the matching failure mechanism.
Reuse registered inputs and prior conclusions; do not reload every iteration.

Use the frozen Arc01 inventory and the existing rich/teaching manifests as
evidence examples. Source and prior packets are read-only. Pin any additional
input actually used. Neither changing status nor a hash establishes semantics.

## Deliverables

Exactly three durable artifacts under artifacts/:

1. evidence-replay-contract.md: a compact copyable convention for evidence
   identity and reproduction. Separate source versus planning roots, original
   versus copy, Git snapshot versus live status, path/hash versus semantic
   authority, expected versus native observed results, command output/status
   versus interpretation, and member versus shared-meaning evidence references.
   Identify existing fields reused and proposed local extensions explicitly.
   Reference shape alone must never establish role or authority.
2. worked-replay.md: one literal executable route, using established Bash/jq/
   Git/hash tools, with two bounded worked cases and the controls below.
   Include exact inputs, digests/revisions, prerequisites/cwd, expected results,
   observed outputs and limits. No new script file or parser.
3. handoff.md: how the next family reuses this recipe, which observations still
   require human semantic judgment, and a bounded sizing recommendation for
   Slice13. Retain all original provenance/shared-reference responsibilities
   and identify cross-owner interfaces. Do not assign or accept new pairs.

CC also updates ledger.md and creates closing-report.md. No other files.

## Two Worked Cases

**Committed authority versus live status.** Read a historical Slice02 plan,
ledger and coverage register by explicit commit. Demonstrate that current
review/coverage advances do not alter those historical bytes. Compare a live
read to its own stated purpose, never a stale expected digest. Use existing
commits; do not edit prior packets or manipulate branches. A deliberately
incorrect digest and an invalid commit/path must fail as distinct outcomes,
not be reported as a successful semantic absence.

**Native query versus authored expectation.** Reuse the accepted exact legacy
question lookup and one current CQ tuple from the frozen inventory. Compare
parsed JSON structurally, not as key-order-sensitive strings. Exercise an
equal object with different key order (passes), wrong question (empty result
from the same query), wrong expected identity/revision (comparison fails),
and missing input (actual tool error, not no-match). Preserve missing/null/
empty distinctions in the selected data. This is not a new extractor or
a claim that a returned card adequately answers the question.

Each case must record the operation actually executed and compare its actual
output to an independently stated expectation. Verify stdout and status where
both matter. Do not invent observations, suppress errors into success, or
compare two authored copies. Temporary diagnostic files may live under
/private/tmp; remove only files created by this run. Source inputs stay read-only.

## Verification And Exit

All five rows must pass: focused contract, both worked cases and controls,
literal replay/preservation, concrete semantic-work handoff. Pin the CC
opening and endpoint separately from CDC edits. Provide distinct pre-commit
and committed modes only where needed: pre-commit scope must include staged
AND unstaged tracked changes plus explicitly named new outputs. A clean-tree
check is not a substitute for scoped diff inspection. Committed mode must
read its claimed snapshot rather than silently reuse a later working tree.

Preserve Arc01, both coverage registers, and accepted Slice01/02/12 packets.
Report unchanged source status, JSON outcomes, whitespace and exact five-file
CC scope. Source/package gates do not apply to this planning-only unit.
CDC independently checks operational behavior before the next semantic slice.
No schema adoption, extraction run, RAG/MCP/graph service or memory admission.

## Version History

- 1.0 (2026-09-15): Opens the bounded replay portion of former Slice03 after
  CQ closure; transfers provenance semantics intact to planned Slice13.
  Zero semantic memberships, two worked cases, no new helper/framework.
