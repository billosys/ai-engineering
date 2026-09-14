---
project: project08-concept-card-metadata
arc: arc06-semantic-families-and-capability-requirements
slice: slice01-relationship-semantics-and-traversal
status: changes-required
version: "1.2"
---

# Relationship Semantics And Traversal

Explain how historical card-local links and current typed records represent
usable concept relationships, where they differ, and what evidence supports
each interpretation. Exercise bounded diagnostic query cases. This is semantic
inventory and capability analysis, not schema adoption or extraction.

## Current Review

CDC reviewed repair 904a5a0d: membership, hashes and reported counts reproduce,
but required contexts/targets, computed diagnostics and registry alignment
remain incomplete. One published block fails. Follow
[Iteration 02](./artifacts/iteration-02-cc-prompt.md) in a new CC session,
not the previous history-bearing task. Was: 400b847a review / Iteration 01.
All original R1/R2/R3 obligations and seven criteria remain; Slice02 is unopened.

## Exact Scope

Author the 35 observed pairs below: eight legacy relation-list pairs, 21
relationship-edge pairs and six card-to-edge linkage pairs. Confirm against
the project transition snapshot; do not derive expected coverage solely from
the registry being tested.

| Field path | Record kind |
| --- | --- |
| `contrasts_with` | `untyped` |
| `contrasts_with[]` | `untyped` |
| `directed` | `relationship-edge` |
| `direction` | `relationship-edge` |
| `endpoint_roles` | `relationship-edge` |
| `endpoint_roles.from_role` | `relationship-edge` |
| `endpoint_roles.to_role` | `relationship-edge` |
| `extends` | `untyped` |
| `extends[]` | `untyped` |
| `from_ref` | `relationship-edge` |
| `from_ref.id` | `relationship-edge` |
| `from_ref.revision` | `relationship-edge` |
| `graph_closure_state` | `relationship-edge` |
| `inverse_reading` | `relationship-edge` |
| `meaning` | `relationship-edge` |
| `prerequisites` | `untyped` |
| `prerequisites[]` | `untyped` |
| `related` | `untyped` |
| `related[]` | `untyped` |
| `relation_type` | `relationship-edge` |
| `relationship_edge_refs` | `concept-card` |
| `relationship_refs` | `concept-card` |
| `relationship_refs[]` | `concept-card` |
| `relationship_refs[].id` | `concept-card` |
| `relationship_refs[].path` | `concept-card` |
| `relationship_refs[].revision` | `concept-card` |
| `relationship_type` | `relationship-edge` |
| `source_support_refs` | `relationship-edge` |
| `source_support_refs[]` | `relationship-edge` |
| `source_support_refs[].id` | `relationship-edge` |
| `source_support_refs[].revision` | `relationship-edge` |
| `symmetry` | `relationship-edge` |
| `to_ref` | `relationship-edge` |
| `to_ref.id` | `relationship-edge` |
| `to_ref.revision` | `relationship-edge` |

The other 405 pairs remain Arc06-owned. Only CDC can add this slice's verified
set to accepted coverage. Reading adjacent evidence does not absorb its fields.
Unobserved components such as endpoint `path` may be discussed as documentary
expectations without inventing frozen memberships. Finer corpus/role contexts
are required where one pair hides distinct meanings.

## Required Context

Read project plan/ledger/AGENTS, Arc06 plan/ledger, assessment and transition
artifacts, then this open set. Load source concept-cards SKILL and guides
01-load-contract, 05-evidence-lifecycle, 06-graph-cq; consult record-field-groups,
vocabulary and structural-validation-candidates references where relevant.

Inputs:
- Frozen Arc01 Slice01 frontmatter-inventory.json and field-dispositions.json;
  transition snapshot and accepted Batch01/Slice06-09 registries/reviews.
- Both full v3.2 prompts in planning `old/dev/concept-cards/`:
  `0009-howto-concept-card-extraction-with-claude-code-v3.2.md` and
  `0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`.
  Inspect v3.1 predecessors when claiming a historical change.
- Live templates/concept-card.md and templates/relationship-edge.md;
  examples/relationship-edge.md and examples/rich-profile-card.md.
- Frozen legacy music/Erlang and Arc07/rerun contexts. Choose named examples
  from the selected-field census: populated relations plus absent/empty or
  anomalous cases per available family. Inspect targets where available;
  disclose inaccessibility instead of inventing identities.

The frozen edge population is a template and a populated synthetic example,
not demonstrated generated edge records. Census all eligible legacy/card/edge
records for selected-field presence/type/shape, separating source families.
Use explicit key presence, not a missing lookup returning null. Preserve
malformed rich-card limitations. Actual originals are read-only; use preserved
baseline copies with original/copy mapping when needed.

Register paths, hashes, origin/copy mappings, sections/line ranges and roles.
Reuse accepted evidence with attribution and recheck inputs for new conclusions.
A hash alone is not semantic inspection.

## Work And Acceptance Questions

1. Compare four legacy relations with current predicates/direction/roles.
   Preserve prerequisite versus extension orientation, inverse/symmetric views
   and contextual meanings. Distinguish the synthetic `precedes` example
   from established domain prerequisite assertions.
2. Compare slug/filename lookup with endpoint identity/revision and card-edge
   references. Trace actual target declarations, locations and unresolved parts.
   Reuse Arc01 findings without assuming global uniqueness, mandatory composite
   keys, embedded revision inheritance or literal-fragment validity.
3. Explain `relation_type` versus `relationship_type`, `directed` versus
   `direction`, and `relationship_edge_refs` versus `relationship_refs`
   from rules and actual usage. Naming alone proves neither equivalence nor
   loss. Distinguish absent, null, empty and populated cases.
4. Separate edge support from endpoint support and reference closure from truth.
   This slice owns edge-support linkage roles, not every adjacent assessment.
5. Inspect relationship prose and explain its teaching contribution versus
   machine lookup. Never invent an edge from prose. Record concrete
   preservation/migration risks without choosing the future profile.
6. Author at least four diagnostic cases covering prerequisites, extension,
   symmetry and unresolved/unsupported edges. Include source-connected legacy
   lookup and current synthetic/template limits. Keep native values; declare
   every adapter mapping without inventing relations. Record expected versus
   observed outcomes, including unavailable operations. Tiny abstract fixtures
   may isolate direction but must be labeled synthetic. These are not new
   extractions, whole-corpus audits or final-profile acceptance.
7. Give concrete CQ/shared-reference interfaces and primary-source research
   questions. Browse primary sources if making new external standards claims;
   full standards synthesis is not required here. An evidenced unknown is an
   acceptable analysis outcome; unsupported certainty is not.

## Artifacts And Registry Contract

Durable home: this slice's `artifacts/`.
- `semantic-membership.json`: evidence register, reusable meanings and 35
  memberships. Reuse `field_path`, `record_kind`, `meaning_id`,
  `effective_meaning`, `evidence_ids`, `disposition` from prior registries.
  Shared meanings are allowed; each member needs its specific role/exception.
  Make documented/observed/conflicting/unspecified status explicit.
- `semantic-evidence.md`: contextual comparisons, census, named reads,
  body/query consequences, conclusions and limitations.
- `query-cases.json`: inputs/provenance, interpretation/adapter, expected and
  observed outcomes and limitations for each diagnostic case.
- `validation-evidence.md`: literal executed recipes, cwd/dependencies,
  census/hash/reference/query results, failures and preservation checks.
- `handoff.md`: proposed versus accepted boundary, remaining ownership,
  concrete CQ/research questions and any sizing proposal.

Do not build a universal validator here. Use established jq/shell/YAML tools
for bounded checks and preserve reusable queries for Slice03 integration.
No new custom helper, Ruby/Python, or frozen-inventory edits. Do not change
a semantic claim merely to satisfy a structural checker.

## Verification And Exit

Derive exact 35-pair equality, uniqueness, inclusion in frozen 440,
disjointness from accepted 115 and 405 outside assignment. Check both meaning
and membership evidence references, all registered hashes, selected-field
census and actual query results. Run published recipes literally with declared
cwd/tools/versions; avoid undeclared shell features. Pin preservation endpoints
and label uncommitted current-state checks honestly, excluding later CDC edits.

Reopen JSON and inspect named evidence, not just file existence. Check planning
whitespace and unchanged source/corpora/accepted packets/frozen inputs.
Record limitations. No skill/version/schema/package/install/runtime edits,
extraction, semantic source verification or operator acceptance are authorized.

CC supplies an attested seven-row close report. CDC decides acceptance.
Raise concrete sizing needs before expanding scope or substituting generic
dispositions. No other slice opens automatically from CC's proposed-done report.

## Version History

- 1.2 (2026-09-14): Repair 904a5a0d independently reviewed; preserves gains,
  requires native target/query evidence and consistent registry/replay before
  closure. Opens Iteration 02 with unchanged scope and criteria; was: Iteration
  01. Fresh-session requirement clarified after same-task reuse.

- 1.1 (2026-09-14): Initial CC review retains exact-set success and opens
  Iteration 01 for substantive contextual evidence, diagnostic lookup and
  assertion/warrant distinctions. No added pairs or weakened criteria.

- 1.0 (2026-09-14): Opens the 35-pair relationship family under the approved
  semantic/capability pivot; reuses evidence and leaves all other work owned.
