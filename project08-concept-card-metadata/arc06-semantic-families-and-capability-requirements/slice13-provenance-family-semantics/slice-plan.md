---
project: project08-concept-card-metadata
arc: arc06-semantic-families-and-capability-requirements
slice: slice13-provenance-family-semantics
status: active
depends-on: [slice03-provenance-and-shared-reference-contracts]
version: "1.0"
---

# Actor Identity Across Four Record Kinds

Determine what the actor mapping and its identity actually mean in claim,
competency-question, concept-card and extraction-run records. Compare documented
rules, template placeholders, populated examples and generated observations.
This is inventory interpretation, not a new actor model or normative schema.
P-15 remains open.

## Exact Assignment And Sizing

Exactly eight [field_path, record_kind] pairs:

~~~json
[
  ["actor","claim"],
  ["actor","competency-question"],
  ["actor","concept-card"],
  ["actor","extraction-run"],
  ["actor.id","claim"],
  ["actor.id","competency-question"],
  ["actor.id","concept-card"],
  ["actor.id","extraction-run"]
]
~~~

The CDC opening census found 37 parsed mappings across these kinds: one
claim, two CQs, 31 cards, three extraction runs. Reproduce rather than assume
these denominators; report excluded malformed records separately. Eight pairs
are coverage units, not eight files or eight independent meanings.

Current coverage: 180 accepted / 375 remaining; eight assigned / 367 outside.
Assignment does not accept these eight. Source and all prior packets are read-only.

This is the first bounded unit recommended by Slice03's handoff; the stable
Slice13 directory is retained. Planned Slice14 owns the complement of the
original provenance scope: actor/actor.id across the other six kinds, all
actor.mode/actor.role memberships, and all original run/preparation/method/
shared-reference responsibilities including remaining CQ provenance interfaces.
Slice14 must be sized/split before execution. Other evidence/lifecycle families
keep their existing owners; all 367 outside pairs remain Arc06-owned.

Inspect sibling mode/role, run and source fields as necessary to understand
the selected identities. That context is mandatory when relevant but does not
add their pairs to this slice. Shared component rules need explicit applicability
and exceptions; do not infer that an actor always means creator or verifier.

## Read Set

Read project AGENTS, project/arc plans and ledgers, this open set, current
project-management/work-verification guidance, and concept-cards SKILL.md.
Then read the closed Slice03 contract, corrected replay, handoff and CDC report.
Reuse their mechanics; do not replay every past repair or start a new framework.

Planning inputs:
- Current semantic-coverage-current.json and frozen semantic-transition-coverage.json.
- Arc01 Slice01 artifacts/frontmatter-inventory.json and input-register.md.
- Arc01 Slice01 artifacts/baseline-snapshots/source-sha256sums.txt and
  copy-sha256sums.txt when using rich/teaching originals or frozen copies.
- Accepted identity findings in Arc01 Slice06; accepted CQ distinctions in
  Arc06 Slice02. Read specific relevant evidence and final CDC decisions.

Source inputs:
- knowledge/concept-cards/guides/02-operator-workflow.md and 03-extraction.md.
- knowledge/concept-cards/references/record-field-groups.md.
- The four selected templates and their full bodies.
- Examples cq-coverage.md, extraction-run-trace.md, parallel-worker-default-recipe.md,
  minimal-card.md and rich-profile-card.md; distinguish synthetic from generated.
- At least one original Arc07 pilot card with populated actor and one expanded
  Arc07 card without it; one valid rich and one teaching rerun witness using
  registered original/copy mappings. Read surrounding provenance/body context.

Use the inventory to select actual witness paths. Register and visibly read
every cited input, with root, exact path, hash, role and applicable range/section.
Shared evidence IDs and member-specific roles are preferable to duplicated prose.
Pin mutable planning authority to the opening Git commit and distinguish live
status. Do not refresh old accepted hashes or modify baseline files.

## Work And Deliverables

Exactly four artifacts, plus ledger.md and closing-report.md:

1. artifacts/semantic-membership.json: eight exact pairs, per-member effective
   meaning, evidence references and specific disposition. Reuse the accepted
   evidence/meanings/memberships shape with explicit applicability, exceptions
   and unknowns. Register all actual inputs and baseline mappings.
2. artifacts/semantic-evidence.md: contextual comparison, native census,
   consequences for readers/extractors/queries/migration, and bounded findings.
3. artifacts/validation-evidence.md: literal Bash/jq/Git/hash replay, native
   diagnostics/controls, expected and actual outputs/status, fixed history
   versus current-state preservation, opening and CC endpoint distinction.
4. artifacts/handoff.md: supported conclusions and concrete unresolved
   decisions/tests, owners and a sized next provenance unit recommendation.

Census all selected records for actor parent and actor.id. Preserve parent
absence/null/empty mapping, missing/null/populated identity, unexpected types
and parse exclusions; never manufacture child absence from an unreadable parent.
Separate templates, synthetic examples, Arc07 pilot/expanded, rich and teaching
families. State whether legacy untyped mappings contain these exact fields
using the frozen inventory; absence does not mean legacy provenance never existed.

Distinguish record ID, source author, run identity, actual performer, recorder
and reviewer where evidence permits. A familiar actor label does not identify
a specific human, model version or globally unique principal without evidence.
Parent-card or run provenance must not silently supply an omitted embedded
claim/CQ actor. Document unknowns with inspected scope and a concrete question,
not generic preservation language.

Two bounded diagnostics suffice:
- Select one populated generated actor identity from native input; compare an
  independently authored expected observation and reject a deliberately wrong
  expected identity. State what the label does and does not identify.
- Compare a template null identity with an actual absent actor witness, retaining
  parent/child state distinctions. Missing input must cause a real tool error,
  not the same result as absent metadata. If a target/declaration is looked up,
  retain match, successful no-match and tool-error separately.

These diagnostics test observation and lookup, not authority or future schema
conformance. Expected results must not be supplied as observed objects. Native
reads may use the hashed frozen inventory plus registered raw-context reads;
no new parser/helper implementation or invented populated records.

## Verification And Boundaries

Walk all six ledger rows. Derive exact assignment from this plan and the pinned
current coverage register; verify inclusion in the frozen full set, disjointness
from accepted pairs and 180/8/367 accounting. Resolve both membership and shared
meaning evidence references. Recompute every registered hash using its declared
live/snapshot mode; show original/copy mapping when a frozen copy is read.

Provide one complete route with explicit cwd/tools and fail-closed extraction.
Keep expected fixture values independent from native outputs. Use JSON value
equality, not object-key-order text comparison. Pin the CC contribution endpoint
separately from any later replay revision. Include staged/unstaged and named-new
scope before committing; compare fixed opening-to-CC history separately from
current dirty-state preservation afterward.

Protect Arc01, both coverage registers and all earlier Arc06 slices. Source,
schema, runtime, package/install, extraction and memory changes are forbidden.
No Ruby, Python, custom helper/parser, task dispatch or model-setting changes.
Use existing bounded Bash/jq/Git tools. Temporary files may be created under
/private/tmp; remove only this run's own files.

Stop with a concrete sizing proposal if the evidence cannot fit with review
headroom. Do not expand scope or reduce criteria. CC marks proposed-done only;
CDC acceptance, Arc06 composition and P-15 remain separate gates.

## Version History

- 1.0 (2026-09-15): Opens the eight-pair actor-identity unit after Slice03
  replay closure. Was: unsized full provenance family; complement explicitly
  retained by planned Slice14, no scope removed or normative design adopted.
