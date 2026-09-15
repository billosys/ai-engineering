# CDC Verification: Arc06 Slice01

Current verdict: changes required after a24758b4; see Iteration 03 Independent
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

## Iteration 02 Independent Review (7de68374)

Date: 2026-09-14. Repair opening head: cc096c02. Source: e763c661.
Verdict: **changes required**. Same 35-pair scope, seven criteria and
115 accepted / 35 assigned / 405 outside accounting. Earlier reviews remain
history; this is the current verdict. The heartbeat observation of this commit
was preliminary, not a separate submission or independent closure.

### R2: Green Checks Still Do Not Replay Native Operations (Serious)

Locations: artifacts/validation-evidence.md:61-66;
artifacts/query-cases.json:3-6.

All three published Bash blocks now run literally and independently with exit
0. The previously broken case-key check is repaired. However, the outcome
check only compares authored expected and observed objects in query-cases.json.
It never derives those objects from the referenced native values or executes
the described operations. The operation strings remain instructions in prose.

CDC's in-memory negative control changes both extension targets to the same
deliberately wrong string. The published outcome predicate still returns true:

~~~bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
jq '.cases[1].expected.to="CDC-deliberately-wrong-target" |
    .cases[1].observed.to="CDC-deliberately-wrong-target"' "$s/artifacts/query-cases.json" |
  jq -e '.cases[0].expected==.cases[0].observed and
         .cases[1].expected==.cases[1].observed and
         .cases[2].expected==.cases[2].observed and
         .cases[3].expected==.cases[3].observed'
~~~

This changes no files. It demonstrates the missing native-input dependency,
not that the genuine examples are wrong. CDC separately read the frozen
values: accented-incomplete-neighbor extends incomplete-neighbor and is
reciprocally related to appoggiatura. The local extension target exists.
Both synthetic endpoint IDs/revisions match the referenced example cards;
the support reference has no path. These gains are retained. CC still needs
literal native queries with computed outcomes compared to independent
expectations, including bounded filesystem/declaration lookup results.
No universal test harness or production graph is requested.

### R1: Required Reading And Contextual Comparison Remain Incomplete (Serious)

Locations: artifacts/semantic-evidence.md:59-65,69-90;
artifacts/semantic-membership.json evidence register.

The claimed full v3.2 inspection is not established by the recorded execution.
The actual segmented command ran sed for each 120-line range with stdout
redirected to /dev/null, then printed "full v3.2 segmented reads completed".
Reading bytes in a shell process is not presenting their contents for semantic
inspection. This is an unsupported completion claim, regardless of intent.
Required reading must be visible to the analyzing context or explicitly
attributed to reusable prior inspected evidence; do not simulate it with a
completion marker. Tool-output truncation must be handled with smaller reads.

The registry now has seventeen inputs, adding three useful witnesses. It still
has no named Arc07/rich/teaching generated card or absent/null anomaly, no
baseline mapping used for such reads, and no reproducible complete selected-
field family/component census. The added Arc07 paragraph is not a substitute
for the named body/metadata comparisons already required by the slice.
These omissions are unchanged obligations, not a request for more source types
or new extraction. Preserve malformed exclusions and the correct headline counts.

### R3/R1: New Prose Is Not Integrated With The Registry (Serious)

Locations: artifacts/semantic-membership.json meanings/memberships;
artifacts/semantic-evidence.md:25-31,42-49,92-96; closing-report.md:13-17.

The new paragraph correctly distinguishes the synthetic edge's pathless
support ID from the rich card's different support. Yet the old paragraph still
reports "Its support target is likewise not found" without specifying owner
or lookup; the replay retains the invented records/support-synthetic-edge-001.md
test. The earlier shape-only statement also conflicts with the new matching
endpoint declarations. Clearly supersede or reconcile these live claims.

No shared meanings or memberships changed in this commit. Thus historical
common-confusion semantics are now in the handoff, but contrasts_with's
effective registry meaning still broadens to generic contrast; card-reference
meanings still lack their newly registered witnesses and retain the previously
reported self-excluding edge-ref definition. Align the evidence, effective
interpretation and consequences; shared concise definitions are still allowed.

The closing report still describes the removed empty-extension case, and the
ledger mixes new proposed-done claims with previous blocker notes. Reconcile
attestations to the actual current packet, keeping unperformed work open.
Do not treat merely mentioning a requirement as satisfying it.

### Reproduced Checks And Row Walk

- All three published blocks pass, including exact plan-derived 35-pair set,
  frozen inclusion/disjointness, all seventeen hashes, JSON and whitespace.
- Both meaning/member reference layers resolve. Reference integrity is not
  substantive adequacy.
- CDC independently corroborates populated extension, native reciprocity,
  endpoint identity/revision matches and absent support path. A bounded
  examples-directory search finds no root id declaration for that support.
- Exact seven-file CC scope; cc096c02 -> 7de68374 preserves Arc01/project
  artifacts. Source and planning were clean before CDC edits.
- No source, extraction, package, runtime or accepted-baseline changes.

| Row | CDC status | Current reason |
| --- | --- | --- |
| S1-1 | done, reproduced | Exact coverage and scoped preservation retained |
| S1-2 | open | R1: discarded full-read output, missing generated/anomalous comparison and full field replay |
| S1-3 | open | R3: unchanged effective interpretations and contextual evidence attachment |
| S1-4 | open | Endpoint gains reproduced; contradictory live support/path/target outcomes remain |
| S1-5 | open | Useful native witnesses, but R2 replay and required body comparisons incomplete |
| S1-6 | open | Ownership and improved contrast handoff retained; incomplete case/evidence dependency |
| S1-7 | open | Structural checks repaired; native replay, current preservation record and consistent attestation incomplete |

### Bubble-Up And Workload Decision

Open Iteration 03 with unchanged requirements, not Slice02. No accepted pair
count changes. Use the concise next packet together with the original slice
contract; do not restart accepted Arc01 work. The remaining work is substantive
and cannot be supplied as an uncredited CDC documentation correction.

The same long-running task was used again: gpt-5.6-terra / medium, 202366 ms,
eleven command executions, one nonzero exit, no observed repair compaction.
The execution record is described in the project workload artifact, not treated
as portable semantic acceptance evidence. No inference of intent, internal
load or model inadequacy follows from these observations.

A genuinely new execution context remains the untested adjustment. Require
that before another full completion attempt; if unavailable, stop and tell the
operator. If the residual evidence cannot fit, return a concrete sizing
proposal instead of another global completion claim. No model/effort change
has been made; the operator retains that decision.

## Iteration 03 Independent Review (a24758b4)

Date: 2026-09-14. Opening planning head: 91db42fa; source: e763c661.
Verdict: **changes required**, with substantive gains. S1-1 and S1-6 are now
done; five full criteria remain open. No new semantic memberships are accepted:
115 accepted / 35 assigned / 405 outside. Earlier reviews are history.

### What Is Now Reproduced

The first three published blocks pass. All nineteen registered hashes, both
reference layers, exact plan-derived membership, frozen inclusion/disjointness,
JSON and whitespace pass. Prerequisite and extension now extract native values
and compare complete expected/observed structures against them. Populated
extension, actual reciprocal related lists and matching synthetic endpoint
declarations remain correct. Historical common-confusion meanings and their
contextual evidence are now in the registry; the central R3 loss is repaired.
The handoff preserves all 405 other pairs and concrete CQ/resolver/research
questions, with no claim that Slice02 is open. S1-6 is independently satisfied.

The new task emits the historical prompt text instead of discarding it.
Do not repeat the former /dev/null finding. The API's truncation of this
reviewer's retrieved task output is not evidence of CC context loss.
The added generated witnesses are useful, subject to the interpretation
correction below. No further full-prompt reread is required just to repeat
this repair; retain the attributable read evidence and focused source citations.

### R2 Remaining: Two Case Results Still Bypass Native Comparison (Serious)

Locations: artifacts/validation-evidence.md:108-121;
artifacts/query-cases.json:5-6.

The symmetry and endpoint cases still compare authored expected/observed values
to each other, after separate hard-coded source checks. They do not compare
every reported component with a native-derived result. Target card revisions
are not inspected by the published endpoint recipe; it checks requested edge
revisions and target IDs, then accepts the authored revision_match value.
The fixed grep context also is not a structured from/to revision association.

Two in-memory counterexamples reproduce the remaining weakness:

~~~bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
s=.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal
jq '.cases[3].expected.revision_match=false | .cases[3].observed.revision_match=false' "$s/artifacts/query-cases.json" |
  jq -e '.cases[] | select(.id=="edge-endpoints") | .expected == .observed and .observed.support_path == "unavailable"'
jq '.cases[2].expected.a="CDC-wrong-endpoint" | .cases[2].observed.a="CDC-wrong-endpoint"' "$s/artifacts/query-cases.json" |
  jq -e '.cases[] | select(.id=="symmetry") | .expected == .observed and .observed.reciprocal == true'
~~~

Both return true with unchanged native inputs. The corresponding native
preconditions also still hold; this does not mutate inputs or their hashes.
Repair only the incomplete case wiring, retaining the genuinely improved first
two cases. Derive all result fields from structured native/frozen data and
actual bounded lookups, including each target revision. Exercise the same
comparison with wrong endpoint/revision expectations and require failure.
The existing shell inequality on the extension value is useful but does not
test these other result components. No production graph is needed.

### R1 Remaining: Complete Context Census And Accurate Provenance (Serious)

Locations: artifacts/semantic-evidence.md:18-25,65-89,107-118;
artifacts/validation-evidence.md:123-125; semantic-membership.json evidence.

The durable census still supplies population totals and selected aggregate
counts, not the promised selected-field presence/type/shape/value/component
comparison by family. No named legacy absent/null witness or teaching-rerun
body is registered; the two added generated witnesses both have empty lists.
Template nulls and malformed rich records do not substitute for those contexts.
The frozen data contains accessible Erlang absent/nullable relationship fields;
for example erlang-in-anger/allocation-strategy.md lacks extends. Complete the
already scoped census and use it to select the remaining distinct witnesses,
not another arbitrary larger corpus or an exhaustive body read of every card.

The new body comparison also says both generated examples name relationship
candidates, and calls them not real extraction. In fact Arc07
cc-emergent-explanation says no relationship edge is asserted and proposes a
future CQ; rich-rerun cc-model-data-constraints names actual relationship
candidates. Both are outputs of real-corpus extraction efforts, still unverified
candidates. Candidate, synthetic, extracted, verified and admitted are separate
axes. Preserve that provenance and distinguish a future CQ from a relationship
proposal. No source-truth verification or new extraction is requested.

### Pre-Commit Replay And Preservation

Block 4 passes its substantive checks, then exits 1 because its final
comparison expects seven unstaged files in a now-clean committed checkout.
CC explicitly labeled this a pre-commit/current-worktree check. This failure
does NOT refute the data or the recorded pre-commit result.

CDC separately reproduced the fixed 91db42fa -> a24758b4 diff: exactly the
seven authorized CC files, with Arc01 and project artifacts unchanged. Source
and planning were clean before CDC changes. Supply a committed-review route
as well as the labeled pre-commit check; this is a small reproducibility
completion, not another substantive finding or scope expansion.

### Seven-Row Review And Next Work

| Row | CDC status | Current evidence / remainder |
| --- | --- | --- |
| S1-1 | done, reproduced | Exact 35-pair scope, no overlap or baseline edits |
| S1-2 | open | Nineteen hashes and new witnesses pass; missing contextual census/witnesses and provenance correction |
| S1-3 | open | Contrast/card-reference repairs retained; unexamined state/context exceptions still need census-backed interpretation |
| S1-4 | open | Correct native endpoint matches; complete revision/result wiring and contextual limits remain |
| S1-5 | open | First two native comparisons improved; two case counterexamples and body distinctions remain |
| S1-6 | done, reproduced | Explicit remaining ownership, separate assertion/warrant, and concrete CQ/resolver/research questions |
| S1-7 | open | Structural/scope checks pass; full census/case replay and post-commit route remain |

The previous shared edge-ref wording can be clarified during integration, but
is not a separate reason to withhold closure now that member-specific roles
and actual evidence are supplied. Do not resurrect repaired R3 obligations.
S1-6 acceptance is a handoff criterion, not semantic acceptance of 35 pairs.

Open bounded Iteration 04 for these two residual areas and final replay.
Original seven criteria and scope remain unchanged; Slice02 stays unopened.
Retain the accepted reads and improvements; avoid restarting the inventory.
If the remaining work cannot fit, return a concrete sizing proposal before
another full completion claim. The five-iteration sizing safeguard remains.

### Workload Follow-Up

This was a genuinely new task at gpt-5.6-terra / medium, with no observed
compaction. Native checks and contextual integration improved, but incomplete
case testing and census work remain. The project workload record counts the
earlier interrupted fresh task separately and deduplicates the heartbeat.

Recommendation, not a setting change: try the same model at high effort for
the next bounded repair, retaining a fresh session and unchanged criteria.
Measure complete evidence and native-negative-control behavior, not elapsed
time or output length. Additional instructions and accumulated evidence are
confounds; this is not a controlled causal model comparison.

## Iteration 04 Independent Review (91c7f5f3)

Date: 2026-09-14. CC opening/closing planning endpoints:
3cf075ff -> 91c7f5f3; source remains e763c661.
Verdict: **changes required**, with S1-4 newly reproduced/done alongside
S1-1 and S1-6. Four criteria remain open. No acceptance of the 35-pair semantic
set: 115 accepted / 35 assigned / 405 outside still applies.

### Reproduced Gains

- Published Bash blocks 1, 2, 3 and 5 pass literally from source cwd. Block 4
  is labeled historical; CDC separately reran its retained prerequisite and
  extension native comparisons through the reciprocal-lookup section boundary.
- Exact plan-derived 35 unique pairs, frozen inclusion and accepted-set
  disjointness pass. Both registry reference layers and all 23 hashes pass.
- The four added Erlang originals really have the stated absent/null fields.
  All eight Music/Erlang rows' state counts, item totals, distinct targets and
  item types reproduce from frozen parsed values. The card aggregate and
  template/example component values agree with the frozen records.
- Symmetry and endpoint expected AND observed objects now compare with native
  results. Each requested endpoint ID/revision is compared to its actual target
  declaration separately. Wrong expectation controls fail as intended.
  CDC also used structured frozen values to reproduce both objects and rejected
  mutations of BOTH authored objects, not just one side of the comparison.
  R2's authored-self-comparison defect is repaired for these bounded inputs.
- Bounded endpoint declarations, unresolved rich-card edge path, pathless edge
  support and unknown relation warrant remain distinct. S1-4 is satisfied.
- The report/handoff now correctly distinguish the real Arc07 no-edge/future-CQ
  candidate from the real rich-rerun body-relationship candidate. Candidate
  status no longer makes these outputs synthetic in that prose.
- Exact seven-file CC commit scope, fixed prior preservation
  91db42fa -> a24758b4, repair preservation 3cf075ff -> 91c7f5f3,
  Arc01/project-artifact preservation and whitespace pass. Both checkouts were
  clean before CDC edits. No source/package/install gates were applicable.

### R1 Residual: Context And Meaning Completion

Locations: artifacts/semantic-evidence.md:113-118,158-162,176-190;
artifacts/semantic-membership.json evidence register; Iteration 04 prompt A.

The explicitly requested teaching-rerun body/metadata witness is still absent
from the report and the 23-input registry. This is not a demand to read more
arbitrary cards: the already frozen teaching population has ten cards with
both relationship-reference keys absent, unlike the two registered generated
examples with empty lists. The combined 31-card table hides that family
distinction. For example, existing teaching cc-memory-forms has relationship
prose ("Contains or routes to" and "Related") despite absent structured edge
references. It is accessible, not an unavailable or malformed input.
Inspect/register one such witness and reconcile its meaning and consequences;
do not infer stored edges or source verification from its prose.

The four new legacy witnesses support observed presence/null/absence, not the
sentence "they do not share requiredness." Requiredness is an instruction or
schema rule, not a frequency inference; describe the observed variation and
leave the policy question explicitly unsettled unless documented evidence
establishes it. At least one new null-field body also merits the already
required body/metadata comparison: data-type-sizes names prerequisites in its
body despite null prerequisites metadata; sc-hbase-protocol and
error-handling-philosophy likewise have relevant prose despite their null
fields. This is not permission to manufacture slug relations from prose.

The Arc07 evidence-register role still says "body candidates" while the report
correctly says no asserted edge and a future CQ. Align that specific role and
affected dispositions with the inspected evidence. No wholesale registry
rewrite or reopening of the repaired historical contrast meaning is required.

### R4 Residual: Complete Current Replay (Correctness-Grade)

Locations: artifacts/validation-evidence.md:174-218;
artifacts/query-cases.json:3-6; semantic-evidence.md:161-162.

The published census code tests selected anchors, not the complete tables it
claims to reproduce: it does not emit/check most Music/Erlang counts, item
types/totals/distinct values, or the card-family breakdown. CDC independently
reproduced the existing values; they are not rejected as numerically wrong.
Publish the actual bounded census operation and tie every reported table to
that output. Count parsed records separately from selected memberships.

The current Iteration 04 block extracts prerequisite/extension targets and
checks existence but omits comparison against their expected/observed JSON.
Those comparisons survive only in the block labeled historical, which also
contains the superseded symmetry/endpoint checks and a pre-commit-only tail.
Make one complete current replay cover all four cases and both controls.
Preserve historical evidence, but do not make readers splice accepted pieces
out of superseded recipes to obtain the current contract.

The prompt explicitly permitted structured frozen values plus original hashes
or an established YAML parser. Instead, the new route extends awk extraction
and retains grep -A4. These happen to read the registered inputs correctly;
this is not another claim that the observed endpoint results are wrong.
Use the already available structured values for the bounded current route,
retaining hashes and actual file/search outcomes, and align case operation text
with what executes (the symmetry recipe uses grep, not the reported awk).
No custom helper or generic parser is needed.

### Independent Census Cross-Check

CDC executed this read-only query from source cwd; its eight objects match the
legacy table, including null versus absence and all item counts:

~~~bash
set -euo pipefail
cd /Users/oubiwann/lab/billosys/ai-engineering
i=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
jq '
[.records[]|select(.values|type=="object")|select((.record_kind//"untyped")=="untyped")
 |. + {family:(if (.path|contains("complete-musician")) then "music" else "erlang" end)}]
|group_by(.family)[]|. as $rows
|["prerequisites","extends","related","contrasts_with"][] as $f
|{family:$rows[0].family,field:$f,n:($rows|length),
 absent:([$rows[]|select(.values|has($f)|not)]|length),
 null:([$rows[]|select(.values|has($f))|select(.values[$f]==null)]|length),
 empty:([$rows[]|select(.values[$f]|type=="array" and length==0)]|length),
 populated:([$rows[]|select(.values[$f]|type=="array" and length>0)]|length),
 items:([$rows[]|.values[$f][]?]|length),
 distinct:([$rows[]|.values[$f][]?]|unique|length),
 itemtypes:([$rows[]|.values[$f][]?|type]|unique)}
' "$i"
~~~

This is a CDC cross-check, not a retroactive claim that CC published that
reproduction route. CC still owns contextual interpretation and its final
current replay. The three malformed rich inputs remain exclusions, not absence
examples or evidence against their body content.

### Row Walk And Bubble-Up

| Row | CDC status | Evidence / remaining condition |
| --- | --- | --- |
| S1-1 | done | Exact 35, both evidence layers, frozen disjointness retained |
| S1-2 | open | 23 hashes and table values reproduced; teaching/body and family-context omissions remain |
| S1-3 | open | Existing roles/contrast retained; observed-required distinction and specific registry role need reconciliation |
| S1-4 | done | Requested/declaration identity/revision, missing-path/support limits and native controls reproduced |
| S1-5 | open | All four bounded case outcomes reproduced; teaching/null-field body comparison remains |
| S1-6 | done | Ownership and concrete CQ/research handoff retained |
| S1-7 | open | Literal current checks pass but do not reproduce the complete advertised census/four-case contract |

Artifact inventory remains the five CC evidence artifacts plus close report
and ledger; CDC has not rewritten CC's semantic interpretation or attestation.
This slice has not yet delivered the full assigned contextual capability.
The remaining work is the existing context/replay obligation, not another
corpus, architecture decision or new extraction. Update parent status and open
Iteration 05 only. Slice02 stays unopened; no frozen membership transfer occurs.

Iteration 05 is the final ordinary corrective iteration under the sizing
safeguard. If incomplete, stop with a concrete replan/split proposal, retained
evidence and exact remaining criteria. Do not create an automatic Iteration 06,
silently defer quality, or close by exhaustion.

### Workload Outcome

This submission is independently observed as a new gpt-5.6-terra / high task
with no compacted event. Compared with Iteration 03, result wiring and census
detail improved, but explicit context coverage and replay integration still
missed. Internal cognitive load is not measured; revised instructions, prior
evidence and task complexity remain confounds. The operator proposed a possible
Luna/xhigh trial next. Record it as a configuration trial if chosen, not proof
that either model or effort alone caused a result. No settings were changed.
