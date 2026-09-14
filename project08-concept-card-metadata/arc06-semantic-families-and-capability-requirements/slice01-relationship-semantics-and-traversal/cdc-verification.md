# CDC Verification: Arc06 Slice01

Current verdict: changes required after 904a5a0d; see Iteration 01 Independent
Review below. The initial review is preserved as history.

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

## Iteration 01 Independent Review (904a5a0d)

Date: 2026-09-14. Repair opening head: 46f60e46. Source remains e763c661.
Verdict: **changes required**; S1-1 remains done and S1-2 through S1-7
remain open. No new accepted memberships; 115 accepted / 35 assigned / 405
outside. Earlier findings and successful checks above are retained as history.
This section is the current review, not an acceptance of CC's row attestations.

### R1 Remaining: Context And Target Evidence (Serious)

Locations at 904a5a0d: artifacts/semantic-evidence.md:41-80;
artifacts/semantic-membership.json evidence register;
artifacts/query-cases.json:7; artifacts/validation-evidence.md:65-66.

The repaired headline counts and quoted legacy/card presence counts reproduce.
The register grows from seven to fourteen inputs, adding named Music/Erlang
cards and current card examples. These are useful gains. However:

- No Arc07, rich-rerun or teaching-rerun card/body is registered or compared;
  no named null/absent anomaly is inspected. The current 31-card total combines
  distinct families. Full selected-field values/shapes/components and family
  breakdown are not durably replayed. Three malformed rich cards remain an
  explicit inventory limitation, not parsed negative examples.
- Actual synthetic-edge endpoints are available: minimal-card.md declares
  cc-prepared-source-provenance revision 1; claim-backed-card.md declares
  cc-claim-support-is-assertion-specific revision 1. Both match the populated
  edge's endpoint requests. The packet does not follow those declarations;
  the latter input is not registered. Synthetic status limits warrant, not
  the ability to check declared identity and revision.
- The rich-card case reports support_target not found, while the replay tests
  records/support-synthetic-edge-001.md. That ID comes from the separate
  relationship-edge example, which declares no support path. The rich card
  instead declares support-evidence-map-definition-001 at its own records/
  path; that is card/claim support, not proof of its missing edge's support.
  The tested path is an adapter guess, not a declared native path. A missing
  rich edge leaves its own support declaration unavailable, not inspected.
- Full-prompt inspection is still attested without a complete current or
  cited prior read route. The repair's visible calls read selected ranges
  (howto 1-130/175-215; parallel 1-140/650-690/855-885), not both full prompts.
  Do not infer hidden prior work; supply the required comparison with an
  attributable route, and keep useful focused citations.

These are incomplete original R1 obligations, not an expanded corpus or demand
for new extractions. Preserve lookup, declaration, revision and warrant as
separate outcomes. Do not conflate rich-card support with synthetic-edge support.

### R2 Remaining: Native Execution And Replay (Serious)

Locations: artifacts/query-cases.json:3-7;
artifacts/validation-evidence.md:39,61-66.

All three Bash blocks were executed separately and literally. Block 1 exits 0;
block 2 exits 1 at line 39 because the revised cases no longer have input and
provenance keys; block 3 exits 0. Block 2 reaches and passes exact membership,
transition inclusion/disjointness and all fourteen hashes before failing.
Its later preservation checks therefore do not execute in that block.

Block 3 compares literal strings in the authored observed objects. It does
not derive those objects from the native inputs or compare computed results
to expected results. It separately tests one real filename and two synthetic
paths, but does not replay the Erlang lookup or predicate traversal. The case
operation strings are descriptions, not literal executable queries.

The empty extends list is a useful negative case but cannot demonstrate
extension orientation. There are 519 populated legacy extends lists (210 Music,
309 Erlang); for example accented-incomplete-neighbor.md lists
incomplete-neighbor. Select and inspect a suitable actual pair. Symmetry needs
an exercised two-endpoint view rather than only an authored direction label.
These remain diagnostic adapters, not a production graph or final profile.

Repair the current replay contract, keeping prior failed attempts as history.
Derive observations from frozen native values (with original identity/hash
checks) or actual parsed inputs; compare computed outputs to expectations.
Keep null/absent/empty distinctions and negative cases. No custom helper is
required: bounded existing-tool recipes suffice.

### R3 Remaining: Registry Meaning Alignment (Serious)

Locations: artifacts/semantic-membership.json contrasts_with and
contrasts_with[] memberships; closing-report.md final Key findings paragraph.

The shared legacy-list meaning and handoff now correctly recognize typed
relationship assertions. That part of R3 is repaired. The historical
common-confusion meaning is also correctly cited in the evidence report.
But the registry still says generic symmetric contrast / body-dependent basis,
without preserving common-confusion versus the current qualified-comparison
meaning in the effective interpretation. The final closeout still foregrounds
navigation rather than the repaired assertion distinction. Align these
surfaces so a consumer of the registry cannot silently broaden the old field.

The added card inputs are registered but not attached to the card-reference
meaning/member evidence; the shared edge-ref definition even calls its own
relationship_edge_refs member distinct from that collection. Reconcile the
actual template/minimal/rich/generated usage with specific evidence and roles.
Shared groups remain welcome; generic group membership is not contextual proof.

### Independently Reproduced Successes

- Exact plan-derived 35 unique memberships; in frozen 440, disjoint from 115.
- All fourteen registered SHA-256 hashes and both evidence-reference layers.
- Eligible 2,054 legacy / 31 card / 2 edge populations and published counts.
- Legacy Music array empty/nonempty counts: prerequisites 5/385, extends
  180/210, related 16/374, contrasts_with 262/128.
- Erlang: prerequisites 306 empty/1357 populated/1 null; extends 66 absent/
  1289 empty/309 populated; related 21 empty/1642 populated/1 null;
  contrasts_with 1133 empty/528 populated/3 null.
- Current card relationship_edge_refs: 1 empty, 30 absent; relationship_refs:
  6 empty, 1 populated, 24 absent. These totals do not replace family analysis.
- Native synthetic endpoint identities above match; source guide and historical
  prompt passages corroborate the assertion/direction distinctions.
- JSON parses; exactly seven authorized CC paths changed. Fixed 355d037f ->
  400b847a and repair 46f60e46 -> 904a5a0d preserve Arc01/project artifacts.
  Source and planning were clean before CDC edits; whitespace checks pass.

### Seven-Row Review And Bubble-Up

| Row | CDC status | Current reason |
| --- | --- | --- |
| S1-1 | done, reproduced | Exact membership and preservation remain correct |
| S1-2 | open | R1: generated/anomalous contexts, full family census and prompt-read evidence incomplete |
| S1-3 | open | R1/R3: effective meanings and referenced contexts not fully reconciled |
| S1-4 | open | R1: available endpoints untraced; unrelated support/path conflation |
| S1-5 | open | R2: no source-derived replay of predicate behavior; empty extension cannot test direction |
| S1-6 | open | Ownership preserved, but handoff relies on incomplete cases and target interpretation |
| S1-7 | open | One published block fails; successful observed-string checks are insufficient |

Open Iteration 02 with unchanged exact scope and original criteria. Retain the
real improvements instead of restarting the inventory. Use three evidence-first
work units within this repair: contextual witnesses, native diagnostics, then
registry/replay reconciliation. If that cannot fit, return a concrete sizing
proposal with outstanding criteria, not another proposed-done packet. Slice02
remains unopened; all transferred and UAT obligations remain unchanged.

Workload follow-up is recorded in the project running artifact. The repair
used the same existing task and settings, not the recommended fresh context.
No compaction was observed during this repair. We cannot attribute these
remaining omissions to context exhaustion, nor infer model incapability.
