---
arc: arc06-card-metadata-and-rendering
status: planned
depends-on: [arc01-portable-contract]
blocks: [arc04-guides-and-package, arc05-validation-and-release-readiness]
related: [arc02-theory-and-evidence, project08-concept-card-metadata]
---

# Arc06 — Card Metadata and GitHub Rendering

## Capability and Operator authority

Bring the existing metadata of every design concept card into a consistent,
readable representation aligned with the selected historical contract, and
make metadata plus Markdown render correctly in GitHub's repository file view.
The Operator added this requirement on 2026-10-10: normalize existing fields,
never fill missing fields, and use 3.2 if the unified replacement is not ready.
This is additive to the [project plan](../project-plan.md) and
[project ledger](../ledger.md), not a replacement for Arc02's full semantic review.

The 233-card Arc01 baseline is the complete denominator. Reconcile all later
additions/splits/merges/removals with it; do not omit malformed cards, extensions,
empty values or absent fields. The starting cohorts are 150 book-backed cards
(112 Arnheim, 19 Cleland, 19 Tschichold) and 83 web-backed cards (37 Butterick,
46 posts across four raw source identities). Refresh the actual source revision
and exact path sets before each execution assignment.

## Schema decision and bounds

Project08's project plan, ledger P-15 and discussion agenda still leave the
unified replacement architecture unadopted. The live concept-cards skill's
`metadata.version: 4.8.1` is a skill release, not a ready card-schema 4.0.
Use the preserved 3.2 field definitions as this arc's fallback; exact paths,
object identities and inspected ranges are recorded in
[preparation notes](slice01-schema-and-field-inventory/artifacts/preparation-notes.md).
Project08 references the legacy definition in its input register; the preserved
artifact copy is in Project05, not Project08's project-level artifacts directory.
Do not duplicate or rewrite those upstream definitions.

If an independently accepted unified contract becomes available before
Slice01's contract is accepted, CDC may record its exact authority, field mapping
and no-loss consequences before adopting it here. After that freeze, a change
requires an explicit plan amendment and renewed affected review; never mix
versions midway through normalization. Project08's design, discussion, UAT and
contributor gates are not inherited permissions to finalize its schema here.

Preserve every existing key, scalar value, list member, relationship/CQ string,
source identity, confidence, null and domain extension unless the accepted
crosswalk names a lossless representation correction. Missing means absent:
do not add guessed values, null placeholders, empty lists, IDs, dates, authors,
provenance, review states or template defaults. Record missing/unknown/ambiguous
fields in a separate gap register. Report partial alignment honestly when the
selected contract requires unavailable information; do not label it full schema
conformance. Existing fields are not automatically semantically correct.

Keep `layer`, `rosetta_stone` and `css_implementation` where present as existing
design extensions unless an accepted no-loss mapping says otherwise. Do not
stringify structured values, flatten relationships, invent support records or
convert extraction confidence into verification/admission. Preserve list order
and the distinction between absent, null, an empty sequence and a populated one.
For historical string-list slots, `[[]]` is a wrong-shape empty-list sentinel:
normalize it to `[]` only under the explicit accepted field rule, with original
value and reason retained in the change register. A nonempty nested value is
not covered by this rule and must be resolved separately.

## Slice breakdown and sizing

All four slices below are **planned**, not issued to CC. Their plans and ledgers
make the new requirement concrete; CDC completes each execution open set with a
fresh baseline, exact allowlist, author-readiness check and `cc-prompt.md` when it
becomes the next authorized work. Do not pre-fill closing/verification records.

| Slice | Coherent output | Dependency and sizing |
|---|---|---|
| [slice01-schema-and-field-inventory](slice01-schema-and-field-inventory/slice-plan.md) | Accepted contract selection, complete raw/typed field census, no-loss crosswalk, gap register, rendering diagnosis and exact batch recommendation | Arc01 baseline and inspected Project08 status; read-only. All 233 headers, no semantic body study. |
| [slice02-book-card-metadata](slice02-book-card-metadata/slice-plan.md) | Consistent existing metadata for all 150 baseline book cards, preservation records and source-scoped checks | Accepted Slice01 and representative pilot before bulk mutation; split into additional numbered children if needed. |
| [slice03-web-card-metadata](slice03-web-card-metadata/slice-plan.md) | Consistent existing metadata for all 83 baseline web cards, preserving section/null/source differences and extensions | Accepted Slice01 and the shared pilot contract; independent of book-original acquisition. |
| [slice04-github-rendering-and-handoff](slice04-github-rendering-and-handoff/slice-plan.md) | Complete normalization union, actual GitHub metadata/Markdown rendering evidence and downstream revision handoff | All book/web normalization children independently accepted; no loss or unreported rendering gap. |

The 150/83 rows are complete coverage obligations, not mandates for giant
single-context CC assignments. Slice01 recommends exact disjoint batches based
on actual field shapes and headroom. CDC records any additional slice numbers,
paths, memberships, predecessors and recomposition owners before issuing them.
The original cohort rows retain their whole population until the expanded child
union meets it. No fixed extra count or artificial iteration-budget reset.

## Preservation and test design

One leading YAML mapping between unindented `---` delimiters, UTF-8 without BOM,
consistent indentation/key ordering/quoting, blank line before the existing body
and no duplicate keys. Select the concrete serialization style in Slice01 and
prove it with the pilot. Maintain one authoritative machine-readable metadata
block; any human presentation must derive from it without becoming competing
metadata. Local parsing/GFM output alone is not GitHub-hosted frontmatter proof.

For every card, compare complete before/after typed metadata with the accepted
mapping, retain original raw fields/bytes, and hash the body independently.
Metadata-only work must preserve body bytes, paths, slugs and reference targets.
Demonstrate deterministic output and an idempotent second pass. Negative controls
must expose dropped extension/list members, null-to-empty conversion, injected
missing fields, unquoted colon strings, duplicate keys and hidden/BOM/fenced
frontmatter. Check nested arrays/maps and escaped/non-ASCII strings without
assuming a generic YAML loader enforces GitHub behavior or a closed schema.

Run a pilot covering actual distinct metadata shapes, all raw source identities,
null/empty/populated lists and structured extensions. Compare a newer readable
card as a rendering reference without importing its extra values or lifecycle
fields. Diagnose the Operator-reported rendering defect on actual pinned GitHub
file views; the preliminary local census proves no rendering cause by itself.

## Interaction with source and semantic review

Source originals are not needed for a lossless formatting operation on existing
metadata; their absence does not block that operation. They remain required for
Arc02/P10-11-dependent fidelity results. Do not repair bibliographic meaning,
relationship truth or teaching bodies under a formatting label. Route those
findings to Arc02 with the exact affected occurrence/revision and keep them open.

Preserve Arc01's raw index, manifests, issued prompts and historical hashes.
If diagnosis finds a defect in Markdown body presentation, CDC allocates a
bounded formatting child here with exact existing-content preservation checks;
metadata-only cohorts do not silently rewrite body text. Changes to assertions
or examples remain Arc02-owned. Slice04 cannot close over an uncorrected required
rendering defect, and no common-error/definition section is populated as filler.

Formatting changes invalidate whole-file hashes and can shift body line numbers;
provide an old-to-new field/locator/revision bridge and refresh dependent evidence
only after an applicability check. Never rewrite the baseline to match delivery
or carry old verification forward by a blanket claim that meaning is unchanged.

Identify `knowledge/design/SKILL.md` and sibling history as the owning skill;
assess version/history and applicable source gates under AGENTS.md before mutation.
Do not bump concept-cards or claim a new schema release for editing design cards.

## Sequencing, composition and workflow

Arc02's current colour-pipeline assignment remains active. This arc is queued,
with no competing CC prompt or changes to its issued files. Read-only Slice01
can be activated at a later explicit handoff without waiting for missing book
originals; source mutation follows accepted contract/pilot and freshly issued
scope. Numeric arc IDs are stable identifiers, not dependency order.

Arc06 supplies the accepted source representation and rendering evidence before
Arc04 freezes the package. Arc04 owns package generation/installation and tests
metadata preservation if cards are included; Arc05 repeats the relevant checks
on the final composed revision and owns release acceptance. This avoids a
package dependency cycle and preserves every previous project gate.

Two contributors, CDC Sofie + separate CC, Operator relay; Expedited Mode stays
selected for Project10. Slice reviews use `cdc-verification.md`. Arc closure
requires the full baseline-to-final union, findings/gap dispositions and an
attributed independent/Operator composition gate. No success record is created
by this planning change. See the [arc ledger](ledger.md).

## Version History

- 1.0 (2026-10-10): Operator adds existing-field schema harmony and mandatory
  GitHub rendering; planned four slices, selected historical 3.2 fallback and
  preserved Project08, semantic-review and source-readiness boundaries.
