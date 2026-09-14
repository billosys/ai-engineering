# CDC Verification: Arc06 Slice01

Date: 2026-09-14
Reviewed CC commit: `400b847a`
Opening plan commit: `355d037f`
Source: `e763c661`, clean and unchanged.
Verdict: **changes required**. One of seven full criteria is reproduced;
six remain open. Scope remains 115 accepted / 35 assigned / 405 outside.
No next slice opens and no new semantic memberships are accepted.

## Findings

### A6S1-R1: Missing Contextual Census, Reads And Target Evidence (Serious)

Locations: artifacts/semantic-evidence.md:16-31;
artifacts/semantic-membership.json:4-13,22;
artifacts/validation-evidence.md:18-48.

The reported 8/21/6 numbers are assigned membership counts, not the required
selected-field corpus census. Neither published replay computes presence,
types, shapes or values across the legacy/card/edge populations.
The evidence register has seven inputs: transition, inventory, edge template,
edge example, graph guide and two prompts. It contains no named legacy card,
current card template, minimal/rich card example, generated card or inspected
target, despite prose and closing-report claims about those contexts.

Independent inspection gives 2,054 eligible untyped mappings, 31 concept-card
mappings and two relationship-edge mappings. The frozen raw legacy records
omit record_kind; `.record_kind == "untyped"` matches zero records.
Normalize that label only after confirming a parsed mapping, then separate
music/Erlang and current source families. The reviewed CC command history
contains the literal-untyped filter and no durable successful full census.
Absence of a registered comparison is not evidence of an unavailable corpus.

Concrete accessible inputs include Complete Musician accent-types.md
(prerequisite meter) and OTP Design Principles behaviour.md (prerequisite
supervision-tree). Current minimal-card.md has relationship_edge_refs;
rich-profile-card.md contains a populated relationship_refs tuple to
records/edge-evidence-map-related-to-claim.md. These are inspectable differences
and target questions, not grounds for a blanket unspecified conclusion.
Do not infer target absence, fragment failure or revision behavior without
recording the actual bounded lookup.

Repair: produce the selected-field census and named representative/anomalous
reads, actual target matrix and specific body/metadata consequences; register
and hash each input used for a claim. Read both full v3.2 prompts in bounded
segments and record relevant observations. Reuse accepted input evidence with
attribution; do not replace semantic work with more generic caution text.

### A6S1-R2: Diagnostic Cases Do Not Exercise Lookup (Serious)

Locations: artifacts/query-cases.json:3-6;
artifacts/validation-evidence.md:8,36.

Three cases use abstract A/B strings; every observed value is a narrative
description of a guide/template. The fourth likewise describes the synthetic
example without a target lookup. No source-connected legacy query or native
reference inspection result is present. The checks assert case count and
presence of keys, not expected versus executed behavior.

Repair: run at least four bounded cases from actual selected native records
and/or explicitly synthetic diagnostic fixtures as allowed by the original
plan. Include real legacy lookup, predicate orientation, symmetric reading
and unresolved/unsupported-reference behavior. Record input identities, exact
query/adapter, expected result, actual result and interpretation. Do not
invent relationships from prose or claim final-profile/corpus equivalence.
A case with an observed unresolved target can be valid; an unperformed lookup
must be labeled unperformed, not an observed result.

### A6S1-R3: Legacy Relation Assertions Are Demoted To Navigation (Serious)

Locations: artifacts/handoff.md:7-9;
artifacts/semantic-membership.json:14-17,20;
closing-report.md:21-25.

The handoff says legacy lists "are not edge assertions." The old v3.2 howto
explicitly calls them typed relationships, requires exact slugs, and defines
prerequisites as concepts that must be understood first, extension as building
upon/elaboration, related as non-hierarchical association and contrast as
commonly confused concepts (old 0009 prompt:183-207). The parallel prompt
provides graph cross-reference/orphan checks and direction semantics
(old 0010 prompt:663-683,868-875).

Lack of an independently identified edge/support record does not erase the
relationship assertion encoded by a typed list. It limits revision tracking,
warrant and lifecycle evidence. Do not collapse assertion, representation,
resolvability and source verification. Also preserve the historical
commonly-confused meaning of contrasts_with alongside the current guide's
more general qualified comparison; do not silently broaden the former.

Repair the registry, comparisons and handoff with those distinctions and
concrete lookup/migration consequences. Keep the valid boundary that endpoint
support does not independently warrant a relation. This is substantive work
for CC, not a minor CDC-authored replay completion.

## Reproduced Checks And Limits

- Both published Bash blocks ran literally and separately from source cwd
  under /bin/bash and exited 0. Their scope/hash/shape checks really pass.
- Exact plan-derived 35-pair set, unique membership, frozen inclusion,
  accepted-set disjointness and 115/35/405 accounting pass.
- All seven registered hashes pass; all referenced meaning/evidence IDs resolve
  at both registry layers. This does not establish sufficient semantic evidence.
- Both JSON artifacts parse; four cases have the required keys.
- Commit diff contains exactly the seven authorized CC files.
- Arc01 and project transition artifacts are unchanged from 355d037f to
  400b847a. Source status is clean; no source version/package change.
- The supplementary query below reproduces the eligible populations and real
  counterexamples. It is a diagnostic, not the missing full selected-field
  comparison and not a CDC replacement of CC's analysis.

~~~bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
jq '{
  eligible: ([.records[] | select(.values | type == "object") |
    select((.record_kind // "untyped") as $k |
      ["untyped","concept-card","relationship-edge"] | index($k))] |
    group_by(.record_kind // "untyped") |
    map({kind:(.[0].record_kind // "untyped"),count:length})),
  literal_untyped: ([.records[] | select(.record_kind == "untyped")] | length),
  counterexamples: [.records[] | select(
    (.path | endswith("/complete-musician/accent-types.md")) or
    .path == "knowledge/erlang/concept-cards/otp-design-principles/behaviour.md") |
    {path,prerequisites:.values.prerequisites,related:.values.related}]
}' "$i"
jq -e '. as $r |
  all(.memberships[]; .meaning_id as $m | $r.meanings | has($m)) and
  all((.meanings[].evidence_ids[], .memberships[].evidence_ids[]);
      . as $id | $r.evidence | has($id))' "$s/artifacts/semantic-membership.json"
git -C .worktrees/planning diff --exit-code 355d037f 400b847a -- \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements \
  project08-concept-card-metadata/artifacts
~~~

The direct legacy/current source reads described above corroborate the findings.
CC must preserve a complete replay of its repaired analysis and actual cases.
The available task history also shows only a partial parallel-prompt read and
hashing of the howto in this turn; the claimed full-prompt comparison is not
demonstrated by the submitted artifacts. This review does not infer private
reasoning or use unavailable context as proof.

## Seven-Row Review

| Row | CDC state | Evidence / reason |
| --- | --- | --- |
| S1-1 | done, reproduced | Exact 35-pair equality, uniqueness, frozen inclusion and disjointness pass |
| S1-2 | open | R1: no actual selected-field corpus comparison and insufficient registered contextual reads |
| S1-3 | open | R1/R3: component summaries need actual contexts; legacy assertion and contrast semantics need repair |
| S1-4 | open | R1: conceptual boundaries stated but actual target comparisons not supplied |
| S1-5 | open | R2: descriptive examples are not executed diagnostic queries or real body comparisons |
| S1-6 | open | R3/R1/R2: ownership count retained, but handoff inherits unsupported semantics and unexecuted cases |
| S1-7 | open | Structural replay/scope pass; full census/query/evidence reproduction does not exist yet |

## What Worked And Bubble-Up

The exact set, explicit commit scope, preserved baseline, separate support/
endpoint concepts, and caution against automatic revision inheritance are
useful and retained. The three shared meaning groups are not rejected merely
for being shared or concise; the missing contextual support and incorrect
semantic generalization are the problems.

The family-oriented plan remains appropriate. This submission does not justify
reducing its acceptance bar or abandoning the approach. Open Iteration 01
within the same slice; preserve all seven criteria and the exact 35 pairs.
Arc06 and the project plan receive status/history updates only. CQ Slice02
remains unopened. If the repair cannot fit with review headroom, return a
specific decomposition proposal before another broad completion claim.

## Workload Observation

See [the project running record](../../artifacts/cc-workload-observations.md).
Observed run metadata: gpt-5.6-terra, medium effort, one compaction, 25 command
executions, three nonzero command exits subsequently repaired, approximately
ten minutes elapsed. Those are observations, not a measurement of cognition.
Substantive omissions remain after structural checks turn green.

Recommendation: use a fresh context for the evidence-first repair, without
changing model/effort yet. Sparse current examples, input-schema mismatch,
inherited task context, prompt interpretation and analysis allocation remain
plausible contributors. No causal model comparison or automatic setting change
is claimed. Tool-display truncation during CDC inspection is not counted as
CC context loss.
