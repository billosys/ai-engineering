---
slice: slice04-github-rendering-and-handoff
status: planned
depends-on: [slice02-book-card-metadata, slice03-web-card-metadata]
blocks: [arc04-guides-and-package, arc05-validation-and-release-readiness]
---

# Slice04 — GitHub Rendering and Revision Handoff

## Goal and complete scope

Demonstrate that all normalized design-card metadata and Markdown render
correctly on GitHub, reconcile the complete baseline-to-final union and supply
safe source/revision handoffs. Consume every accepted normalization child,
including any additional bounded batches. Scope starts at 233 baseline cards;
all documented population changes are mapped, never used to reduce coverage.

## Authority and preservation

The [arc plan](../arc-plan.md), [arc ledger](../ledger.md),
[project plan](../../project-plan.md) and [project ledger](../../ledger.md) govern.
Operator addition 2026-10-10; Two-Contributor Workflow, Expedited Mode.
This is a planned slice, not a CC assignment. At activation CDC issues a complete
`cc-prompt.md` with exact pins/read manifest, paths and commit instructions.
There is no current prompt or implied permission to modify SOURCE.

All existing values/extensions and absent/null/empty states remain explicit.
No missing-field population or source/semantic acceptance. Preserve original
233-card lineage, all issued Arc01/02 records, source originals and unrelated
Project12/knowledge/lfe. Per-card metadata-only changes must leave body bytes
unchanged and record new whole-file hashes/line locators. No close/CDC record
is created before actual delivery and review.

## Verification procedure

1. Freeze the composed source candidate and accepted contract; reconcile every
   card's metadata-change, body-preservation and field-state record. Repeat the
   full syntax/type/duplicate-key/no-invention/idempotence checks and resolve
   exact current paths/slugs/anchors. Preserve all original values and gaps.
2. Build one coverage row for every current card, mapped to its baseline identity.
   Record exact source blob/hash, hosted repository/commit/path, retrieval date,
   observation/evidence pointer and pass/fail/blocked result. Inspect GitHub's
   rendered repository file view, including native metadata presentation and the
   existing body, not just raw text, GitHub Pages or a generic Markdown renderer.
3. Check displayed labels/values, non-ASCII and special-character strings,
   null/empty/populated lists, structured extensions, frontmatter separation and
   body headings/lists/code/links. Compare with parsed metadata and the actual
   preserved body; no blanket pass based on one representative card. Collect
   observations in bounded batches if necessary and compose the full union.
   Body presentation failures get a bounded Arc06 formatting child with exact
   before/after content and markup checks; changes to substantive claims go to
   Arc02. Reconcile authorized presentation deltas separately from metadata-only
   body-byte equality and rerun rendering at the repaired revision.
4. Record reference-card comparisons and discriminating syntax/field-loss controls.
   Automated local GFM/HTML checks support coverage but cannot stand in for the
   hosted metadata layer. GitHub's official rendering documentation is linked in
   preparation notes; do not claim a local library reproduces all host filters.
   If corrected source is not available at a hosted commit, prepare all local
   evidence and name the missing host observation; do not claim rendering passed
   or infer a publication/push approval from the need for a test.
5. Bridge old and new fields/body locators and evidence applicability into Arc02.
   Formatting does not upgrade source support, confidence or five-dimension
   verdicts. Report semantic findings and unresolved gaps to their owners.
6. Return accepted source representation and rendering results to Arc04 for
   package composition and Arc05 for final-revision regression. Determine actual
   package contents then: preserve metadata if cards are included, and verify
   routes to canonical source cards otherwise. Do not make Arc06 closure depend
   on a not-yet-built Arc04 package. Later edits invalidate affected observations
   and require fresh checks before final Project10 acceptance.

## Outputs and closure boundary

Durable outputs under `artifacts/`: `final-card-coverage.jsonl`,
`github-rendering-evidence.md`, `revision-and-package-handoff.md`,
`execution-notes.md`. This is verification/handoff, not an automatic source repair;
a discovered defect gets an exact corrective assignment with affected checks.
No success placeholders. CDC independently reviews all rows and actual evidence;
formal arc composition and the attributed independent/Operator gate follow.

All [six ledger rows](ledger.md) must be accounted for. Missing metadata facts
can remain gaps under the Operator no-fill boundary; an untested or failing
required rendering property cannot be silently converted into success.

## Version History

- 1.0 (2026-10-10): Planned whole-population GitHub rendering and revision
  composition; Arc04 package and Arc05 release gates remain separately owned.
