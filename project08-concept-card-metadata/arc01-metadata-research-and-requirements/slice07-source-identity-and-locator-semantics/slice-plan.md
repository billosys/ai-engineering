---
project: project08-concept-card-metadata
arc: arc01-metadata-research-and-requirements
slice: slice07-source-identity-and-locator-semantics
status: changes-required
version: "1.2"
---

# Source Identity And Locator Semantics

Compare legacy source attribution/location fields with the current source-locator
contract. Deliver supported meanings and actual lookup/preservation consequences
without designing a new schema or asserting that an address warrants a claim.

Current CDC review of `d077bbe8` (2026-09-13): useful contextual prose added,
but unchanged registry values/evidence, missing comparisons and executable
replay/closeout keep S7-R1/R2/R3 open. Follow
`artifacts/iteration-02-cc-prompt.md`. Was: Iteration 01 correction.
No criterion, pair or parent gate changes. Earlier review basis follows.

CDC review of `d8a3a6c0` (2026-09-13): exact pair coverage and preservation
pass; S7-R1/R2/R3 require field-specific meanings, missing contextual comparisons
and complete replay/closeout. Follow `artifacts/iteration-01-cc-prompt.md`.
Was: open for initial CC execution. All twenty pairs and seven criteria remain
unchanged; this correction does not open another slice or close a parent.

## Basis And Sizing

Consumes frozen Slice01 inventory, accepted Batch01 and CDC-closed Slice06
(e88e6c0b plus attributed CDC replay documentation). Source baseline e763c661.
Read current project/arc plans and ledgers, Project08 AGENTS.md and source
framework/work-verification/concept-cards guidance. Load document-extraction
for its locator contract only; no conversion operation is authorized.

Twenty pairs form one coherent bounded comparison: seven legacy fields and
thirteen root source-locator fields. This separates address/source identity
from later assertion-support, graph/CQ and lifecycle work, leaving room for
data inspection and corrective review. No informal batch hierarchy is added.

## Exact Pair Selection

The following table is exhaustive. Kind is the observed census label, not an
accepted semantic family or future schema. All twenty occur in the original
Slice04 allocation and are disjoint from the accepted 47 pairs.

| Field path | Record kind |
| --- | --- |
| `authors` | `untyped` |
| `chapter_number` | `untyped` |
| `chapter` | `untyped` |
| `context_hint` | `source-locator` |
| `locator_type` | `source-locator` |
| `locator_value` | `source-locator` |
| `mapping_evidence_refs` | `source-locator` |
| `numbering_basis` | `source-locator` |
| `original_locator_ref` | `source-locator` |
| `pdf_page` | `untyped` |
| `prepared_locator_ref` | `source-locator` |
| `prepared_source_refs` | `source-locator` |
| `range_convention` | `source-locator` |
| `representation` | `source-locator` |
| `resource` | `source-locator` |
| `section` | `untyped` |
| `source_ref` | `source-locator` |
| `source_slug` | `untyped` |
| `source_snapshot_ref` | `source-locator` |
| `source` | `untyped` |

The standalone locator's id/revision/record_type are accepted Slice06 context,
not new memberships here. Exclude actor, created_at, run_refs and validation_refs.
Other kinds' source_refs, inline spans and locator maps may be evidence but
their field memberships are not silently absorbed. A null reference/container
in this census remains a real observed pair; do not invent descendant paths.

## Required Comparison

Inspect legacy values/shapes using the frozen census, preserving music/Erlang
and source-family distinctions relevant to each claim. Inspect named source
attribution and body citations, including null/no-page or non-book-shaped
examples where available. Separate title, slug, attribution, chapter/section,
page label/index and source edition/snapshot; record missing distinctions.
An author string is not automatically a parsed person list. Null coordinates
are not automatically inapplicable; a filename or matching title is not an
edition identity.

Read relevant historical Provenance sections and checked predecessor differences,
using prior full-read evidence honestly. Read source-locator.md's body,
concept-cards' extraction locator guidance, and document-extraction's
09-locator-model.md and relevant templates/examples. Compare actual Arc07 or
captured rerun locator/support references as available. Label root-frontmatter,
embedded record, external map, template and synthetic evidence distinctly.

Inspect every selected field in its actual construct. Explain original versus
prepared addresses, source versus snapshot versus resource identity, representation,
locator kind/value, numbering and range basis, context, mapping evidence and
prepared provenance. Show at least one concrete PDF page-basis distinction and
one line/anchor/resource distinction from existing evidence. Synthetic examples
may establish convention, not real successful conversion or semantic support.
Preserve unavailable or ambiguous mappings; do not invent fixed offsets or
claim source fidelity from path resolution.

Report observed old/current dispositions and concrete lookup/body/preservation
consequences, including what is still unknown. No proof of migration equivalence
follows from representability. Standards selection remains later research.

## Artifacts And Exit

Write four artifacts under artifacts/:
- semantic-evidence.md: inspected contexts, meanings, evidence roles, comparisons,
  query/preservation implications and explicit limitations.
- semantic-membership.json: exactly twenty pairs, with resolvable meaning and
  evidence IDs, input paths/sections/hashes, explicit dispositions and explained
  finer contexts. This is a planning registry, not a production schema.
- validation-evidence.md: literal executable commands from a declared cwd,
  actual results, all input checksums, pair/reference and census checks,
  separately labeled semantic review, preservation and whitespace.
- handoff.md: integration boundary, concrete remaining questions and sizing
  implications for later source/support/graph/CQ and lifecycle work.

Independently derive the expected pairs from the table, compare to the registry,
assert uniqueness, frozen-inventory inclusion and disjointness from accepted
Batch01/Slice06. Validate meaning and membership evidence, and inspect every
meaning beyond structural presence. Run every documented command literally;
a prose description of a query is not a reproduction route.

Source, original corpus, Slice01, Slice04 and Slice06 evidence remain unchanged.
No extraction, source edit/version bump, standards/schema implementation,
package/install, runtime or semantic source-support verification. Prefer
existing tools; no new helper anticipated. If one is genuinely necessary,
raise it before expanding scope; approved scripting is Fennel, never Ruby/Python.

All seven ledger criteria must pass independently for closure. CC authors the
proposed-done report, walking every row and scope-as-specified/delivered.
CDC verifies and decides advancement. Of 555 pairs, 47 are already accepted,
20 assigned here, and 488 remain (236 original Slice04, 252 original Slice05).
Old allocation counts are accounting, not semantic endorsement. Slice04/01,
Arc01 and the project remain open.

## Version History

- 1.2 (2026-09-13): Iteration 01 review retains its useful prose additions
  and opens Iteration 02 for actual registry, evidence and replay repairs.
  The same three findings remain open; no scope or criterion change.

- 1.1 (2026-09-13): CDC review retains S7-2/S7-7 successes and opens
  Iteration 01 for S7-R1 through S7-R3. No scope or criterion reduction.

- 1.0 (2026-09-13): Opens twenty source/locator pairs after Slice06 CDC closure.
  Preserves the full Slice04 integration and later Slice05 replay obligations.
