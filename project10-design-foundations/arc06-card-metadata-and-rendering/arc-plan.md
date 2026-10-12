---
arc: arc06-card-metadata-and-rendering
status: planned
depends-on: [arc01-portable-contract]
blocks: [arc04-guides-and-package final release readiness]
related: [arc02-theory-and-evidence, project08-concept-card-metadata]
---

# Arc06 — Card Metadata and GitHub Rendering

## Capability and Operator authority

Normalize existing metadata across the full 233-card baseline and demonstrate
correct metadata/Markdown rendering on GitHub, without inventing missing fields.
The 2026-10-10 addition remains binding. The Operator's 2026-10-12 amendment in the
[project plan](../project-plan.md) reduces this arc from four planned stages to
**two execution slices**. It changes work grouping, not preservation, coverage,
hosted-rendering or independent-review requirements. [Arc ledger](ledger.md)
and [project ledger](../ledger.md) govern.

**Was:** contract/inventory → book migration → web migration → separate rendering
handoff. **Now:** contract plus exercised pilot → whole-population normalization
plus rendering. Source type alone does not justify two mutation assignments.
Split only if actual field complexity or execution/review headroom requires it.
Keep all 150 book-backed and 83 web-backed cards in the resulting union.

## Schema decision and preservation

Use the historical 3.2 field definitions unless an explicitly accepted unified
Project08 replacement is available when selecting the contract. Recheck actual
Project08 authority then; skill release numbers are not schema versions.
[Existing preparation notes](slice01-schema-and-field-inventory/artifacts/preparation-notes.md)
locate the preserved definition and preliminary census; reuse those inputs,
without recreating their reports. Freeze one mapping before bulk normalization.
A later schema change needs an explicit amendment and affected revalidation.

Preserve all existing keys, typed values, list order, source identities,
relationships/CQs, confidence, null/empty distinctions and domain extensions,
including `layer`, `rosetta_stone` and `css_implementation`. Missing stays absent:
no guessed facts, IDs, dates, null/default placeholders or new review states.
A documented wrong-shape `[[]]` sentinel may become `[]` only under the accepted
specific field rule; retain its original value/reason. Nonempty nested values
need their own lossless mapping. Ambiguities and missing required information
are reported, not filled or called full schema conformance.

Use one leading UTF-8 YAML mapping with unindented `---` delimiters, consistent
indentation/quoting, no BOM/duplicate keys, and separation from the body. Keep
one metadata authority. Select the concrete serialization from actual field
shapes and GitHub behavior, not copied values from newer cards.

## Revised slice breakdown

No CC prompt has been issued in this arc. These are the current execution units:

| Unit and retained identifier | Delivery | Gate |
|---|---|---|
| [Slice01](slice01-schema-and-field-inventory/slice-plan.md) — contract and pilot | Inspect all headers; select the no-loss mapping; exercise a small candidate conversion across distinct field shapes and source identities; diagnose GitHub rendering | Independent acceptance of mapping and pilot before bulk mutation |
| [Slice02](slice02-book-card-metadata/slice-plan.md) — all-card normalization and rendering | Apply the accepted procedure to all 233 cards; verify preservation/idempotence; inspect exact-revision GitHub views and deliver the complete revision bridge | Accepted Slice01, exact fresh main scope; independent review of final complete population |

The retained Slice02 directory name is a historical identifier, not a 150-card
limit. Its current assignment will cover both source cohorts. The unissued
Slice03/web and Slice04/rendering drafts are **superseded**, not completed;
their entire coverage and checks move to Slice02. All four existing child drafts
are marked for this amendment; the surviving Slice01/02 open sets must be revised
fully before any prompt is issued. Their former output lists are not instructions
to produce duplicate inventories, contracts, gap registers and handoff reports.

Prefer one compact mapping/pilot record in Slice01 and one complete generated
before/after result record plus concise validation evidence in Slice02. Retain
raw/typed preservation evidence and gaps where needed. A reusable conversion
helper is justified for the repeated operation; no general schema framework is
required. The current source diff and actual rendering are the main deliverables.

## Verification and source interaction

For every card compare complete before/after typed metadata against the accepted
mapping, body bytes independently, and paths/reference targets. Prove deterministic
and idempotent output. Exercise failures that could actually lose data: dropped
extensions/list items, null/empty confusion, injected fields, duplicate keys and
malformed/fenced/BOM frontmatter. The pilot covers actual distinct shapes and all
raw source identities, including structured extensions and non-ASCII strings.

Observe actual hosted repository file views at the exact changed revision for
all final cards. Local YAML/GFM parsing supports the check but does not prove
GitHub rendering. Hosting/publication needs the existing Operator authority;
unavailable hosted evidence leaves that gate open while local fixes can land.
Do not add a separate rendering-only slice automatically for this dependency.

Metadata-only mutation preserves teaching bodies exactly. Diagnose Markdown
body presentation issues separately; fix them only under an explicit bounded
content-preservation scope. Substantive claim/example/relationship repairs belong
to Arc02. Book originals are unnecessary for lossless formatting and remain
required for dependent semantic fidelity under P10-11.

Preserve baseline/historical hashes and supply old/new revision and locator
bridges. Refresh only affected evidence after an applicability check; do not
rewrite accepted historical inputs. Owning design skill version/history and
applicable source/package gates remain required. Project08's schema or skill
release is not changed by this migration.

## Sequencing, composition and workflow

Arc06 can run at the next ready handoff after the first live-correction batch,
without waiting for Arc02's entire corpus/input work. Two contributors, CDC Sofie
and separate CC via Operator relay; Expedited Mode remains active. No competing
assignment is issued here, and current Arc02/Slice05 work is preserved.

Arc04 consumes accepted normalization/rendering revisions and owns package/final
release validation, including applicability after any later source edits. Former
Arc05 responsibilities are consolidated there. Arc06 closure retains the complete
baseline-to-final union and attributed independent/Operator composition gate.
No ledger row is accepted by this amendment.

## Version History

- 1.1 (2026-10-12): Operator workload/latency amendment after Arc02 evidence-only
  slices; combine contract with pilot and combine book/web mutation with hosted
  rendering. Supersede unissued child drafts explicitly; retain all 233 cards,
  no-fill/no-loss and actual GitHub checks. Final validation transfers to Arc04.

- 1.0 (2026-10-10): Operator adds existing-field schema harmony and mandatory
  GitHub rendering; planned four slices, selected historical 3.2 fallback and
  preserved Project08, semantic-review and source-readiness boundaries.
