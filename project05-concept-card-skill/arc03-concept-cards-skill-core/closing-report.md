# Arc03 Closing Report: Concept Cards Skill Core

```yaml
project: project05-concept-card-skill
arc: arc03-concept-cards-skill-core
status: closed
closed-by: Codex CDC
closed-on: 2026-09-06
composition-verdict: delivered
```

## Capability Verdict

Arc03 delivered the source-level `concept-cards` core capability promised in
the Arc03 plan. The skill now exists under `knowledge/concept-cards/` with a
live entrypoint, sibling `version-history.md`, and ten focused guides covering
load contract, operator workflow, extraction, re-extraction, evidence
lifecycle, relationship/CQ semantics, reconciliation, validation,
verification, memory admission, and maintenance/promise boundaries.

The capability is standalone as a method skill. It creates and reviews
provenance-bearing concept-card work products while routing raw PDF, EPUB,
HTML, and converted-source cleanup to `document-extraction`. It does not claim
templates, examples, schemas, package targets, generated zips, docs,
installation, executable validators, runtime graph services, memory runtime
automation, CCDP services, or live corpus extraction.

## Slice Walk

| Slice | Status | Outcome |
| --- | --- | --- |
| Slice01: Source Scaffold And Load Contract | verified closed | Created `knowledge/concept-cards/` with `SKILL.md`, sibling `version-history.md`, and load/operator workflow guides. |
| Slice02: Extraction, Re-Extraction, And Provenance | verified closed | Added source-faithful extraction, source span/support, extraction-run, re-extraction, and preservation guidance. |
| Slice03: Evidence, Validation, And Verification | verified closed | Added evidence lifecycle and validation/verification guidance while preserving evidence grade, extraction confidence, validation, verification, reconciliation, preservation, and memory-admission distinctions. |
| Slice04: Relationships, CQs, Reconciliation, And Memory | verified closed | Added relationship/CQ, reconciliation, memory-admission, and maintenance/promise-boundary guides; all ten guide routes are live. |

Slices planned: 4. Verified closed: 4. Deferred: 0. Dropped: 0.

## Composition Check

The slices recompose into the Arc03 capability:

- `SKILL.md` routes the `concept-cards` skill and preserves the standalone
  method boundary.
- Guides 01 through 10 cover the full Arc03 source-guidance surface.
- The skill preserves Project03 v4.0 distinctions among concept card, claim,
  source support, source span/source locator, relationship edge, competency
  question, extraction run, validation result, verification result,
  reconciliation result, preservation decision, and memory admission.
- Evidence grade, extraction confidence, validation result, verification
  state/result, reconciliation state/result, and memory admission remain
  distinct.
- `concept-cards` routes document cleanup and extraction preparation to
  `document-extraction` and consumes prepared outputs as upstream provenance.
- `knowledge/concept-card-method/` and `knowledge/source-preparation/` remain
  absent.
- Arc03 does not add or claim templates, examples, schemas, package/docs/
  install wiring, executable validators, or runtime systems.

Arc-level checks reproduced:

```text
find knowledge/concept-cards -maxdepth 2 -type d -print | sort
test -d knowledge/concept-cards && test ! -d knowledge/concept-card-method && test ! -d knowledge/source-preparation
rg -n "document-extraction|PDF|EPUB|HTML|converted-source|prepared source|preparation|upstream provenance|not source support|does not establish" knowledge/concept-cards
```

The source tree contains 12 Markdown files under `knowledge/concept-cards/`.
The final Slice04 local-link check verified all 111 local links and anchors
inside that tree.

## Ledger Walk

| Row | Status | Evidence |
| --- | --- | --- |
| A3-1 | done | Slice01 CDC verification reproduced the scaffold, entrypoint, sibling history, and load/operator workflow guides against source commit `31d96b151781c63004370569d14db556ce21a604`. |
| A3-2 | done | Slice02 CDC verification reproduced extraction, re-extraction, preservation, source span/source support, and extraction-run provenance guidance against source commit `79664fc8751f5fe33d28a4221431caccc4222d37`. |
| A3-3 | done | Slice03 CDC verification reproduced evidence lifecycle and validation/verification guidance against source commit `3fbfcef25145fb47fd2b67d8dd847e9b4cb9d28c`. |
| A3-4 | done | Slice04 CDC verification reproduced relationship/CQ, reconciliation, memory admission, and maintenance/promise-boundary guidance against source commit `3ac312fcbad66dae8d15679e21aa868cb2115626`. |
| A3-5 | done | Arc03 close reproduced `document-extraction` routing and confirmed `concept-cards` does not own raw document conversion or prepared-source cleanup. |
| A3-6 | done | Arc03 close reproduced current Project05 naming and layout: `knowledge/concept-cards/` exists with `SKILL.md`, `version-history.md`, and `guides/`; old roots and support/package/runtime surfaces remain absent. |

Rows: 6. Done: 6. Deferred: 0. No-op: 0.

## Arc-Plan Change Log

No Arc03 plan changes were required during the arc. Slice close bubble-up
findings were handled inside later already-planned slices:

- Slice02 surfaced stale caller wording; Slice03 cleaned it while making
  evidence and review guidance live.
- Slice03 left relationship/CQ, reconciliation, memory admission, and
  maintenance boundaries to the already-planned Slice04; Slice04 implemented
  them.

These were not changes to the Arc03 slice breakdown or capability.

## Bubble-Up To Project05

Arc03 delivered the source-level `concept-cards` core guidance required by the
Project05 roadmap. It advances Project05 toward P-3 and P-5 but does not close
P-3, because P-3 also requires sibling support files, package target,
generated zip, and install surface evidence assigned to Arc04 and Arc05.

No project-plan scope reduction is required. Arc04 should now implement the
concept-card record templates, examples, schema/reference material, and
validation review surfaces using the current `knowledge/concept-cards/` name
and sibling layout. Historical Project03 paths that place support material
under `guides/` are evidence, not current layout instructions.

## Closure

Arc03 is closed.
