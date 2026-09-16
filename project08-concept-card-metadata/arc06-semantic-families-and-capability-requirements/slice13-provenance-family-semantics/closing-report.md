# CC Proposed-Done: Arc06 Slice13

Status: proposed-done pending independent CDC verification. This packet
performs contextual semantic analysis of exactly eight actor/actor.id pairs
across claim, competency-question, concept-card and extraction-run records.
It accepts zero semantic pairs, does not close the slice, does not open
Slice14 and does not adopt a schema or specification.

## Pinned state and endpoints

- Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`, opening and
  current commit `e763c661592ff1097a94bb470db9cf924524579d`; source remained
  clean and read-only. No source commit was made.
- Planning checkout: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`,
  opening commit `609f2f558b100a06df42e6a8b85ebfe200a27b22`, clean before this
  packet.
- CC planning endpoint: pending until the exact six-file planning commit is
  created. The committed replay must use that actual SHA as `CC_COMMIT`.
- Coverage remains 180 accepted / 375 remaining / eight assigned / 367
  outside. The current coverage register and immutable transition register
  were not changed; assignment is not acceptance.
- P-15 remains open. CDC acceptance, Arc06 composition, real extraction/UAT,
  operator card-quality acceptance and memory admission remain separate gates.

## Validation and controls

The complete literal route is in `artifacts/validation-evidence.md`. CC
replayed it in staged precommit mode before the commit and must replay it
again after commit against the actual endpoint. Its claimed checks are:

- all 40 registered input hashes, the frozen inventory hash and the opening
  planning/current-coverage authority;
- exact six-file scope and whitespace, with source and protected prior
  planning history unchanged;
- current coverage's exact eight-pair assignment, inclusion in the remaining
  set, disjointness from 180 accepted pairs and 180/375/8/367 accounting;
- the native 37-record census: one claim, two CQ, 31 card and three run
  mappings, with 12 absent parents, four object/null templates and 21
  object/string card actors;
- byte-equal rich/teaching original and preserved-copy mappings;
- independently authored expected generated actor versus native `codex`
  observation, deliberately wrong expected identity as comparison failure;
- template object/null versus expanded-card parent absence, successful bounded
  no-match, and missing-input jq tool error with non-empty stderr.

Expected values are authored separately from native results. These diagnostics
test observation and state/error distinctions; they do not prove actor
authority, identity uniqueness, semantic support, verification, answerability
or schema conformance.

## Six-row CC walk

All six opening rows are addressed exactly once and are CC-attested, not
independently closed.

| Row | CC disposition | Evidence and limit |
| --- | --- | --- |
| S13-1 | done (CC-attested) | Exact eight pairs, current 180/375/8/367 accounting, remaining-set inclusion and accepted-set disjointness are recorded in `semantic-membership.json` and the literal route. |
| S13-2 | done (CC-attested) | Native 37-mapping census preserves record-kind, parent/child, template/synthetic/generated and malformed-parse distinctions; selected raw witnesses are registered and read. |
| S13-3 | done (CC-attested) | All eight member meanings include applicability, effective meaning, exceptions, disposition, operational consequences and unresolved questions; root record identity is kept separate from actor identity. |
| S13-4 | done (CC-attested) | Native generated match, wrong expected identity, template-null/actual-absent comparison, successful no-match and missing-input tool error are captured without collapsing classifications. |
| S13-5 | done (CC-attested) | The literal route registers and rehashes every input, checks original/copy mappings, fixed opening history, exact six-file scope and whitespace. Committed-endpoint reproduction remains a CDC gate. |
| S13-6 | done (CC-attested) | Handoff preserves the 32-pair actor-family complement, broader Slice14 provenance work, other family owners and P-15, with concrete candidate sizing and no opened successor slice. |

## Artifact inventory and exact scope

Exactly six planning-root-relative files are in the contribution:

1. `project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/semantic-membership.json`
2. `project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/semantic-evidence.md`
3. `project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/validation-evidence.md`
4. `project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/handoff.md`
5. `project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/ledger.md`
6. `project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/closing-report.md`

No durable artifacts were written outside the declared `artifacts/` home. No
`cdc-verification.md` is created by CC. No project/arc/slice plan, coverage
register, transition register, prior slice, source skill, package/install,
schema, extraction, runtime, graph, task-dispatch, model-setting or memory
file changed.

## Bubble-up to Arc06

Slice13 delivered the bounded actor/actor.id piece assigned by the current
arc-plan: eight pairs across four record kinds, with native family/state
census, contextual meanings, operational consequences and replayable controls.
The findings confirm the existing Arc06 split rather than requiring a plan
change: actor.mode/actor.role and the other six kinds remain outside this
slice, and the broader run/preparation/method/shared-reference work remains
with the planned Slice14 complement.

The concrete sizing proposal is to census and, if still coherent, split that
complement into candidate Slice14A (actor/actor.id across the remaining six
kinds, 12 pairs), candidate Slice14B (actor.mode/actor.role across ten kinds,
20 pairs), and later bounded run/preparation/method/shared-reference/CQ
provenance units. This is a proposal only. Slice14 must be sized and opened by
the planning authority before execution; it is not opened here.

Silent-drop check: specified scope is eight pairs, four artifacts, six ledger
rows, two diagnostics, registered inputs, literal replay, exact six-file
scope, preserved prior work and explicit P-15 boundary. Delivered scope is the
same. Zero semantic pairs are accepted, and all 367 outside current pairs stay
Arc06-owned. CDC must independently rerun the committed route, inspect the
actual six-file diff and decide all six rows before this slice can close.
