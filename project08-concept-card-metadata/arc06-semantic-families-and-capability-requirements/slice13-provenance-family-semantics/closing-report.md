# CC Proposed-Done: Arc06 Slice13

Status: proposed-done pending independent CDC verification. This repair
performs bounded R1-R4 evidence/replay repair for the original contextual
analysis of exactly eight actor/actor.id pairs across claim,
competency-question, concept-card and extraction-run records. It accepts zero
semantic pairs, does not close the slice, does not open Slice14 and does not
adopt a schema or specification.

## Pinned state and endpoints

- Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`, opening and
  current commit `e763c661592ff1097a94bb470db9cf924524579d`; source remained
  clean and read-only. No source commit was made.
- Planning checkout: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`,
  original opening commit `609f2f558b100a06df42e6a8b85ebfe200a27b22`; original
  CC endpoint `78be7fabae79039ef3f24daa639d8e314ebcee0f`.
- Repair opening commit: `e42419482aebabcdac9be9e3032daa8f72da09d3`; the repair
  CC endpoint is the commit containing this six-file packet and is returned
  with the handoff. The committed replay must use that actual SHA as both
  `CC_COMMIT` and, independently, `REPLAY_COMMIT`.
- Coverage remains 180 accepted / 375 remaining / eight assigned / 367
  outside. The current coverage register and immutable transition register
  were not changed; assignment is not acceptance.
- P-15 remains open. CDC acceptance, Arc06 composition, real extraction/UAT,
  operator card-quality acceptance and memory admission remain separate gates.

## Validation and controls

The complete literal route and fail-closed wrapper are in
`artifacts/validation-evidence.md`. CC replayed the route in staged precommit
mode before the commit and must replay it again after commit against the actual
endpoint. Its claimed checks are:

- all registry-derived input hashes, the frozen inventory hash and the
  repair-opening planning/coverage authority;
- exact six-file scope and whitespace, with source and protected prior
  planning history unchanged;
- plan-derived exact eight-pair assignment, inclusion in the repair-opening
  remaining set, disjointness from accepted pairs and 180/375/8/367 accounting;
- the native 37-record census: one claim, two CQ, 31 card and three run
  mappings, with family/state/label breakdown and three named parse exclusions;
- the 2,054 parsed legacy untyped mapping census, explicit parent absence and
  not-applicable nested `actor.id` state;
- byte-equal rich/teaching original and preserved-copy mappings resolved
  through their registered manifest entries;
- independently authored expected generated actor versus native `codex`
  observation, deliberately wrong expected identity as comparison failure;
- valid-registry, invalid-member and dangling-reference controls;
- template object/null versus expanded-card parent absence, successful bounded
  no-match, and missing-input jq tool error with non-empty stderr.

Expected values are authored separately from native results. These diagnostics
test observation and state/error distinctions; they do not prove actor
authority, identity uniqueness, semantic support, verification, answerability
or schema conformance.

## Six-row CC walk

All six rows are addressed exactly once. S13-1 and S13-6 retain their prior
CDC-verified status; S13-2 through S13-5 are CC-attested proposed-done by this
repair and remain pending independent CDC closure.

| Row | CC disposition | Evidence and limit |
| --- | --- | --- |
| S13-1 | done (CC-attested) | Exact eight pairs, current 180/375/8/367 accounting, remaining-set inclusion and accepted-set disjointness are recorded in `semantic-membership.json` and the literal route. |
| S13-2 | proposed-done (CC-attested) | Native 37-mapping family/state/label census, three named YAML exclusions and 2,054 legacy untyped comparison reconcile to the frozen inventory; pending independent CDC. |
| S13-3 | proposed-done (CC-attested) | All eight meanings retain applicability, exceptions, consequences and unknowns; corrected field-group and project-instruction evidence attribution remains bounded; pending independent CDC. |
| S13-4 | proposed-done (CC-attested) | Native match, wrong expected identity, template-null/actual-absent comparison, successful no-match and jq tool error are retained; swallowed raw search removed; pending independent CDC. |
| S13-5 | proposed-done (CC-attested) | Fail-closed wrapper, endpoint registry binding, derived evidence count, manifests/native bytes, fixed history boundaries, protected paths and exact six-file scope are checked; pending independent CDC. |
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
rows, R1-R4 repair controls, registered inputs, literal replay, exact six-file
scope, preserved prior work and explicit P-15 boundary. Delivered scope is the
same. Zero semantic pairs are accepted, and all 367 outside current pairs stay
Arc06-owned. CDC must independently rerun the committed wrapper, inspect the
actual repair diff and decide S13-2 through S13-5 before this slice can close.
