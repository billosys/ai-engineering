---
project: project08-concept-card-metadata
arc: arc01-metadata-research-and-requirements
slice: slice09-claim-and-card-linkage-semantics
status: open
version: "1.0"
---

# Claim And Card Linkage Semantics

Explain how assertions and their source/support references are represented
within and alongside concept cards. Preserve readable assertion scope and
machine lookup capability without conflating a card, its claims, a source,
and the evidence that supports a particular assertion.

## Basis And Sizing

Consumes the frozen Slice01 inventory and accepted Batch01/Slice06/Slice07/
Slice08 evidence, not Slice04 formal closure. Read the project plan/ledger,
arc plan/ledger and Project08 AGENTS.md first. Source baseline is e763c661;
record actual source/planning commits and status at execution.

The frozen census has one claim root (the template) and 31 parsed concept-card
roots. A template-only claim field is not demonstrated populated usage.
Cards span templates/synthetic examples, Arc07 pilot/expanded candidates and
the usable rich/teaching reruns. Three malformed rich cards remain parse
limitations, not missing/null metadata. A census of these contexts plus the
bounded body/target sample below fits one execution context with review headroom.
Do not turn this into an all-card body audit or a schema implementation.

## Exact Pair Selection

This exhaustive table selects 21 pairs, all in the original Slice04 allocation,
disjoint from the 94 accepted pairs. The old allocation is accounting only.
Observed record kinds are not a proposed future schema.

| Field path | Record kind |
| --- | --- |
| `assertion_kind` | `claim` |
| `card_ref` | `claim` |
| `source_refs` | `claim` |
| `source_support_refs` | `claim` |
| `statement` | `claim` |
| `claim_refs` | `concept-card` |
| `claim_refs[]` | `concept-card` |
| `claim_refs[].id` | `concept-card` |
| `claim_refs[].path` | `concept-card` |
| `claim_refs[].revision` | `concept-card` |
| `source_refs` | `concept-card` |
| `source_refs[]` | `concept-card` |
| `source_refs[].id` | `concept-card` |
| `source_refs[].path` | `concept-card` |
| `source_refs[].revision` | `concept-card` |
| `source_snapshot` | `concept-card` |
| `source_support_refs` | `concept-card` |
| `source_support_refs[]` | `concept-card` |
| `source_support_refs[].id` | `concept-card` |
| `source_support_refs[].path` | `concept-card` |
| `source_support_refs[].revision` | `concept-card` |

Claim statement/kind/card_ref are only observed null roots here; do not add
unobserved descendants to achieve symmetry with populated card references.
Collections, entries and entry components remain distinct memberships.
Exclude card status, actor/run, method, preparation references, graph/CQ,
assessment/lifecycle and all other record-kind memberships. They may be read
as context, not silently accepted or reassigned.

## Required Comparison

Load live concept-cards SKILL.md, claim and card templates, extraction,
evidence-lifecycle and validation guidance, plus specific references that
actually define the selected fields. Load collaboration-framework and the
project-management/work-verification routes for planning and evidence rules.

1. Query all 32 parsed claim/card roots for selected-field presence, values
   and shapes by input family. Distinguish absent keys from present null,
   empty collections, strings and populated mappings/lists. Use presence and
   typed shapes, not jq's missing-key-as-null projection. Account separately
   for the three malformed rich inputs without repairing/reinterpreting them.
2. Inspect the claim/card templates and minimal, claim-backed and rich-profile
   synthetic examples. Inspect Arc07 Slice02 Model Data Constraints and its
   support record, Arc07 Slice04 Memory Forms, and Model Data Constraints
   in both the usable rich and teaching rerun baseline copies. These samples
   expose standalone-template, embedded-claim, body-only-support, explicit
   reference and scalar-snapshot contexts. Expand only for a named census
   anomaly or uncovered selected-field meaning; explain the selection.
3. Use Slice01's committed baseline-snapshots/ and hash manifests for reruns,
   retaining the mapping back to original workbench paths. Register every
   input path, hash, inspected section and evidence role used for a conclusion.
   Preserve malformed originals and distinguish raw-text observations from
   parsed metadata. Do not require unavailable temporary inputs to exist;
   report availability, identity and revision limitations separately.
4. Explain statement versus paraphrase/definition/inference, qualifications,
   exceptions and body duplication; assertion_kind's intended role is not a
   closed vocabulary or a populated census result. Explain card_ref's
   containing-card role versus a claim's own ID/revision and card claim_refs.
   Do not assume reciprocal links, globally unique IDs, embedded-claim
   revision inheritance or that each body assertion has a structured claim.
5. Compare card-level source_refs, a scalar source_snapshot commit and
   claim-level source/support lists with the source-support subject/span model
   already reviewed in Slice08. A source citation or snapshot token is not
   selected assertion support; a card's support list is not proof that every
   claim is supported. Trace at least the named pilot card -> embedded claim
   -> support -> subject/source reference path, stating what is structured,
   what needs body lookup, and what remains unresolved.
6. For the selected real and synthetic reference samples, record requested
   ID/revision/path, target declarations, lookup convention and agreement/
   mismatch/unknown. Distinguish file, heading text, literal fragment and
   record identity checks. Reuse Slice08 findings with attribution, but do
   not assume every later rerun uses the same paths or conventions. Fictional
   synthetic targets illustrate conventions, not missing real generated work.
7. Compare historical Accent Types (Complete Musician) and OTP Behaviour
   already registered in Slice08, reading their substantive definition and
   source/review bodies as well as metadata. Use the historical v3.2 extraction
   guidance for intended assertion/provenance behavior. Explain readable
   historical strengths and observed machine-link differences without claiming
   global absence, losslessness or current query equivalence. No re-reading
   the textbook to issue new semantic-support verdicts is authorized here.
8. Author a meaningful definition and concrete lookup, preservation and body
   consequence for every pair in the registry itself, linked to actual
   evidence. General reference rules can be shared, but field-specific
   applications cannot be replaced by one preservation slogan. Keep
   template-only limits, actual usage differences and unresolved design
   questions explicit in both registry and prose.

## Artifacts And Exit

Four CC artifacts belong under artifacts/:

- semantic-membership.json: exactly 21 selected pairs; authored meanings,
  dispositions and resolvable evidence links at both meaning/member layers;
  registered input identities, sections, roles and hashes.
- semantic-evidence.md: census/context observations, bounded body/reference
  comparison, reference matrix, consequences and limits with prior attribution.
- validation-evidence.md: every literal executed check and result, including
  presence/type census, body/target inspection, all hashes and preservation.
- handoff.md: concrete research/integration questions and remaining boundaries.

Derive the expected set independently from the table, assert equality,
uniqueness, frozen inclusion, disjointness from all 94 accepted pairs and
accounting against the old allocation. Resolve both evidence layers and
check meaning, not merely JSON validity. Run every documented command from
its declared cwd. Hash all registered inputs, including newly used guidance.
Record the expected interpretation of diagnostics; a diagnostic may correctly
report an unresolved target without asserting that the reference is valid.

Use fixed entry/delivery endpoints for historical preservation; record any
pre-commit current-state check as such. Preserve all of Slice01/04/06/07/08
and source/corpus bytes. Pin the actual new Slice09 opening commit as the
entry baseline, not the older 3436020a before authorized CDC plan changes.
If a block cannot yet know its own commit, distinguish the executed
current-state comparison from the future fixed-endpoint replay explicitly.

The seven-row ledger is the unchanged exit contract once opened. CC reports
each row individually, the four artifacts, exact commit scope and an honest
scope-as-specified/delivered bubble-up. CDC independently decides closure.

## Boundaries And Remainder

No new helper is anticipated: existing jq/shell/parsers suffice. No Ruby/
Python helpers, source edits, schema/validator implementation, package/install
work, new extraction, corpus vendoring, graph/MCP runtime, input repair or
memory admission. New scripts, if separately authorized, use Fennel; serious
tooling Rust/LFE. Raise specific sizing issues before expanding this unit.

94 pairs are accepted, 21 assigned here, 440 others remain (188 original
Slice04, 252 original Slice05). These counts do not endorse old semantic
ownership. Slice04 retains complete-artifact integration; Slice05 retains
remaining semantics/final replay. Slice01, Arc01 and Project08 are not closed.
Research Slice02/03 and P-14's same-chapter Complete Musician trial keep their
existing gates. No new card-quality trial is executed by this slice.

## Version History

- 1.0 (2026-09-13): Opens 21-pair claim/card linkage comparison after
  Slice08 CDC closure. Preserves all remaining semantics and parent/UAT gates.
