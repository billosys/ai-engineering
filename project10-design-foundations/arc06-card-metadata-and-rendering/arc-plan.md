---
arc: arc06-card-metadata-and-rendering
status: active
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

Slice01 is independently closed at `4ccc6f60` / `9934079a`, all six done.
A06-01 is done after complete mapping/authority review; six arc rows remain open.
Slice02 local223 normalization and233 preservation are independently accepted
at `b49f4589` / `877cd9d2`; five child rows done, hosted S02-05 open.
That publication handoff is complete. Current hosted review finds46 body escape
defects; Arc02/Slice09 repairs them while Arc06 remains open.
These are the current execution units:

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
and separate CC via Operator relay; Expedited Mode remains active. Arc02/Slice08
is independently closed. Arc06/Slice02 initial
[cc-prompt.md](slice02-book-card-metadata/cc-prompt.md) returned source `b49f4589` /
planning `877cd9d2`; local work accepted, hosted gate open. Next action is
the current hosted re-entry below. The earlier publication/access proposal
and source-repair handoff are historical; the issued rendering follow-up resumes
after CC executes the approved corrected-source publication.
Slice01 has accepted ten pilots, complete233
inventory and safe helper; its historical3.2 mapping is frozen for this batch.
Other Arc02 work and Project08 schema adoption remain distinct/open. Hosted
unavailability permits local checked delivery but leaves S02-05/A06-05 open.

Arc04 consumes accepted normalization/rendering revisions and owns package/final
release validation, including applicability after any later source edits. Former
Arc05 responsibilities are consolidated there. Arc06 closure retains the complete
baseline-to-final union and attributed independent/Operator composition gate.
A06-01 is independently accepted by the linked complete mapping review; no
other arc or project criterion is promoted by the slice close.

## Version History

- 1.6 (2026-10-13): Slice02 local return independently accepted, five child rows
  done/one hosted row open. Record concrete Operator publication handoff; preserve
  all seven arc criteria and composition/release gates.

- 1.5 (2026-10-13): Slice01 I2 independently closes all six criteria and freezes
  mapping/helper; accept A06-01 at complete233 review scope, activate approved
  Slice02 all-card delivery with225 source paths and whole hosted gate retained.

- 1.4 (2026-10-13): I1 preserves233/ten and resolves F02; Unicode recovery
  F03 holds bulk. Issue two-site I2; three slice rows done/three open and all
  seven arc criteria retained. Slice02 remains unissued.

- 1.3 (2026-10-12): Slice01 initial review accepts intake/census/crosswalk;
  reproduced write-time drift and partial-write failure hold bulk mutation.
  Issue narrow helper I1; preserve all233 coverage and seven parent criteria.


- 1.2 (2026-10-12): Activate combined Slice01 after Slice08 closure; authorized
  3.2 fallback, complete census and ten actual source cards/helper. Retain all
  seven arc criteria and all233 hosted/body/no-fill obligations.


- 1.1 (2026-10-12): Operator workload/latency amendment after Arc02 evidence-only
  slices; combine contract with pilot and combine book/web mutation with hosted
  rendering. Supersede unissued child drafts explicitly; retain all 233 cards,
  no-fill/no-loss and actual GitHub checks. Final validation transfers to Arc04.

- 1.0 (2026-10-10): Operator adds existing-field schema harmony and mandatory
  GitHub rendering; planned four slices, selected historical 3.2 fallback and
  preserved Project08, semantic-review and source-readiness boundaries.

## Slice02 local review — 2026-10-13

[CDC review/Operator handoff](slice02-book-card-metadata/cdc-verification.md#hosted-blocker-and-concrete-operator-handoff)
accepts local source preservation. At that earlier review, all233 hosted observations were unperformed;
remote integration/publication has since completed. See current hosted status below.
No new CC source repair or next slice is issued while that binding gate is open.

## Current hosted status — 2026-10-13

[Slice02 CDC review](slice02-book-card-metadata/cdc-verification.md#hosted-return-independent-review--2026-10-13)
fetched all233 published views at `c4cc7427`: metadata renders correctly;46 post
bodies still show literal Unicode escapes. Was: unavailable hosting. Now: actual
body correctness fails, with [Arc02/Slice09](../arc02-theory-and-evidence/slice09-post-card-unicode-presentation/slice-plan.md)
as its existing content-owner repair. The two-slice Arc06 grouping and all seven
criteria survive. Slice02 remains five done/one open; no arc composition close.

- 1.7 (2026-10-13): Slice02 hosted return reveals falsely passing body escapes;
  retain whole233 rendering gate and route a direct source correction to Arc02.

## Slice09 source result and hosted re-entry — 2026-10-13

Was: Arc02/Slice09 had one Operator evidence gate open. Now: Slice09 is closed
with all four rows done: source589d7c21 independently accepted, five CDC evidence
fields at b3aabcdf Operator-accepted on2026-10-13. All233 metadata and187 other
cards are preserved;46 bodies now contain intended glyphs. Arc06 remains open:
CC's normal publication is authorized, with execution pending; its actual233-view
Iteration01 follow-up still gates rendering. CDC has not pushed or observed that
corrected revision on GitHub.
A06-01 remains done; other six parent rows stay open.

- 1.8 (2026-10-13): Record reviewed Slice09 source delivery and gated hosted
  re-entry; no implied publication, corrected-revision view or composition acceptance.

- 1.9 (2026-10-13): Operator accepts the prepared Slice09 evidence repair and
  authorizes CC publication; child closes, hosted Iteration01 resumes after push.
  Preserve seven arc criteria/statuses and independent composition obligation.
