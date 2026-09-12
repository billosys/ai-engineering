---
project: project08-concept-card-metadata
arc: arc01-metadata-research-and-requirements
slice: slice01-metadata-inventory-and-research-questions
status: ready-for-cc
version: "1.0"
---

# Metadata Inventory And Research Questions

Reproduce the metadata and capability comparison before selecting a schema.
Turn the operator's concerns into a complete, evidence-backed research agenda.

Read the project and arc plans and ledgers, then the
[planning brief](./artifacts/planning-brief.md). This is a planning/evidence slice;
source skills and historical cards are read-only inputs.

## Work

1. Confirm both worktrees and source versions. Register exact paths, Git revisions
   where available, file hashes, corpus availability and historical version labels.
   Include the current 4.8.1 source and both ignored workbench reruns. Preserve
   referenced workbench baselines as byte-identical, path-mapped evidence copies
   under `artifacts/baseline-snapshots/`; retain hashes and original labels.
   Preserve only task-relevant cards, indexes, run descriptions and comparisons.
2. Read both original v3.2 prompts in full and inspect their predecessors for
   metadata definitions and changed semantics. Parse frontmatter across available
   Complete Musician, Erlang, Arc07 and workbench card sets, plus current templates,
   examples and references. Use a YAML parser; report failures and nested value
   shapes as well as top-level keys. Do not silently omit malformed records.
3. Inspect representative real values and bodies, including unusually rich,
   minimal, missing and inconsistent cases. Distinguish field absence in a
   template, missing generation behavior, and information relocated to a record.
4. Map every discovered field and capability to preserved, renamed, relocated,
   weakened, absent, ambiguous, or intentionally changed behavior, with evidence.
   A pointer to prose does not prove preservation of machine lookup capability.
   Trace meaningful values and relationships, not just matching key names.
5. Form prioritized research questions and candidate acceptance checks, including
   all operator concerns and additional gaps discovered by the inventory. Define
   the research handoff for Slice02 without declaring an accepted architecture.

## Artifacts

Home: this slice's `artifacts/` directory.

- `planning-brief.md`: planner-authored input; already present, not CC completion evidence.
- `input-register.md`: exact inputs, revision/hash identities, availability and copy map.
- `metadata-inventory.md`: parsed coverage, keys/value shapes and representative observations.
- `capability-crosswalk.md`: field/meaning/query preservation, gaps and body interactions.
- `research-agenda.md`: prioritized questions, standards candidates and verification needs.
- `validation-evidence.md`: commands, outputs/counts, failures, limitations and worktree hygiene.
- `baseline-snapshots/`: preserved local workbench evidence; retain provenance and original bytes.

Do not vendor whole external books or corpora. Register historical music/Erlang
inputs and record bounded evidence excerpts needed for review. Source acquisition
for future trials belongs in their declared run protocols.

## Verification And Exit

Reproduce parsed file counts and field unions, spot-check every mapping category
against actual files, verify copied evidence hashes, and check all cited local
paths. Run planning `git diff --check`; verify source status before/after. No
source/package gates are needed unless this slice's scope is explicitly changed.
The [ledger](./ledger.md) defines seven acceptance rows. CC writes a proposed-done
closing report with row evidence and Arc01 bubble-up; CDC verifies separately.

## Version History

- 1.0 (2026-09-12): Opens a bounded inventory and question-formulation slice;
  preserves ignored baseline evidence before architecture and future CC trials.
