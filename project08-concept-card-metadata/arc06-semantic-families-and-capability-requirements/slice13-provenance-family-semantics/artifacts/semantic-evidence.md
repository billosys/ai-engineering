# Slice13 semantic evidence: actor identity across four record kinds

Status: CC proposed-done; this is a bounded evidence-backed inventory
interpretation, not semantic acceptance, schema adoption, source-truth
acceptance, extraction-quality acceptance, operator approval or memory work.

## Opening state and exact boundary

- Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`, opening
  `e763c661592ff1097a94bb470db9cf924524579d`, clean and read-only.
- Planning checkout: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`,
  original opening `609f2f558b100a06df42e6a8b85ebfe200a27b22` and repair opening
  `e42419482aebabcdac9be9e3032daa8f72da09d3`; both were clean before their
  respective scoped contributions.
- Repair-opening coverage authority: 180 accepted / 375 remaining / eight
  assigned / 367 not yet sliced. Its pinned snapshot SHA-256 was
  `5d4413abe585274750544784627f65b6f83668596815d55c6a1e9dbcd9339070`.
- The repair derives the assignment from the pinned slice plan and checks it
  against the repair-opening coverage snapshot. Assignment is not acceptance;
  no coverage register was edited. Current live coverage is reported separately
  and is not required to retain obsolete assignment bytes.
- The frozen transition register remains the immutable 555-pair, 115/440
  baseline. This packet does not add memberships to accepted coverage.

The complete registered input and hash manifest is in
`semantic-membership.json`. The original contribution boundary is `609f2f55`
to `78be7fab`, exactly six CC files. This repair boundary is `e4241948` to its
new CC endpoint, restricted to the authorized subset of those six files;
intervening CDC plans, review and prompt files are excluded. The repair-opening
planning authority is pinned to `e4241948`; live status and current coverage are
reported separately. The original/copy mappings for the rich and teaching
witnesses are retained without treating a byte-equal copy as an independent
source read.

## Native frozen census

The native frozen inventory contains 37 parsed mappings for the four selected
record kinds: one claim, two competency questions, 31 concept cards and three
extraction runs. All 37 selected mappings have object-valued parsed `values`;
the three malformed rich-rerun cards remain excluded from the parsed
denominator, as recorded by the accepted Slice02 boundary.

| Record kind | Parsed records | Actor parent absent | Actor object with null `id` | Actor object with string `id` |
| --- | ---: | ---: | ---: | ---: |
| claim | 1 | 0 | 1 | 0 |
| competency-question | 2 | 1 | 1 | 0 |
| concept-card | 31 | 9 | 1 | 21 |
| extraction-run | 3 | 2 | 1 | 0 |
| **Total** | **37** | **12** | **4** | **21** |

The child census is not normalized away from its parent state:

| `actor.id` state | Count | Interpretation |
| --- | ---: | --- |
| Parent absent / child not applicable | 12 | No embedded actor mapping was parsed; this is not a null child. |
| Parent object / child null | 4 | The four current templates expose an actor object with null `id`, `mode` and `role`. |
| Parent object / child string | 21 | Four Arc07 pilot cards use `codex-cc`; seven rich-rerun cards and ten teaching-rerun cards use `codex`. |
| Missing child in an actor object | 0 | No selected object omits `id`. |
| Empty string or unexpected type | 0 | No such native selected value was observed. |
| Null or empty parent mapping | 0 | Neither a null parent nor an empty actor object occurs in this population. |

The 12 absent parents are nine cards, one synthetic CQ and two synthetic
extraction-run examples. The four object/null parents are the claim, CQ,
concept-card and extraction-run templates. No populated claim, standalone CQ,
or extraction-run actor is present in the frozen selected population.

The parse exclusions are not negative actor evidence. The three named rich
rerun cards failed the frozen YAML parse and therefore do not contribute
records; `INDEX.md` is a non-card index, not a malformed-card substitute.

The native family breakdown is: four template object/null records; six
synthetic records with absent parents (one CQ, three cards and two runs); six
expanded Arc07 cards with absent parents; four Arc07 pilot cards with
`codex-cc`; seven rich-rerun cards with `codex`; and ten teaching-rerun cards
with `codex`. All 21 populated actor objects carry `mode: agent-direct` and
`role: extractor`. The registered synthetic card witnesses include
`claim-backed-card.md`, `minimal-card.md` and `rich-profile-card.md`; none is
silently counted as a template or generated rerun.

### Legacy untyped comparison

The frozen inventory also contains 2,054 parsed legacy mappings whose
`record_kind` is untyped. A native query over those object-valued mappings
found actor parent absent in all 2,054 records, with zero null, empty-object,
populated-object, unexpected-type or literal dotted `actor.id` keys. Because
the parent is absent, nested `actor.id` is explicitly not applicable in all
2,054 records; it is not a child-null observation. This is a bounded result for
the inspected frozen inventory, not a claim that legacy provenance never
existed outside it.

## Rules and contextual readings

The field-group reference is narrower than the prior wording claimed:
`record-field-groups.md` lines 7-20 explicitly name `actor` in the
extraction-run row (line 15) and preservation-decision row (line 19); the
table does not itself list actor for claim, competency-question or concept-card.
The four selected placements come from the template frontmatter instead:
claim `claim.md:1-22`, CQ `competency-question.md:1-35`, concept card
`concept-card.md:1-27`, and extraction run `extraction-run.md:1-35`. Those
templates expose a common `{id, role, mode}` shape with null placeholders.
The operator-workflow guidance (`02-operator-workflow.md:3-10,36-43,98-127`)
and extraction guidance (`03-extraction.md:40-58,135-163`) require actual
actor/provenance observations to remain separate from source identity, run
identity, support, validation, verification and admission. The extraction
guide specifically describes an extraction run as recording actual actor and
scope; it does not establish the identity class or a global principal registry.

The accepted Slice06 identity finding is load-bearing here: a root `id` and
`revision` identify the record of that kind. They do not become actor, source,
subject, endpoint, target or input identities. Slice02 supplies the parallel
CQ boundary: a question string, a card `cq_refs` tuple, a standalone CQ and
its answerability/coverage records are related surfaces, not automatically
the same construct. Therefore an actor on a card cannot silently become the
actor of an embedded CQ, and a card or run reference cannot fill an omitted
claim actor.

## Witness comparisons

The selected witnesses were read as records with their surrounding body and
provenance sections, not only as frontmatter:

| Witness | Native observation | What it supports | What it does not support |
| --- | --- | --- | --- |
| Arc07 pilot `cc-model-data-constraints.md` | `actor: {id: codex-cc, mode: agent-direct, role: extractor}`; candidate card, claim and run references; body says the claim was extracted from one bounded chapter span. | A populated card-local actor label and its recorded role/mode in that revision. | A unique human, model version, source author, globally stable principal, or operator acceptance. |
| Arc07 expanded `cc-complementary-learning-systems.md` | Source snapshot, candidate/lifecycle fields and a readable support body are present, but the actor parent is absent. | A real absent-parent witness distinct from template null. | That no actor existed during extraction, or that actor is inapplicable. |
| CompCogNeuro rich rerun `cc-model-data-constraints.md` | Revision 2; `actor.id: codex`, `agent-direct`, `extractor`; run ref and source snapshot; body identifies direct extraction and review limits. | A generated rich-family actor observation, tied to its card revision and preserved original/copy mapping. | Equivalence of `codex` with `codex-cc`, source authorship, verification or admission. |
| CompCogNeuro teaching rerun `cc-model-data-constraints.md` | Revision 3; `actor.id: codex`, `agent-direct`, `extractor`; a different CQ id and body/profile framing. | A generated teaching-family actor observation and family-specific context. | That the same label denotes one globally identified principal or that the rich/teaching CQ identities are equivalent. |
| `cq-coverage.md` | Synthetic CQ body and populated component refs, but no actor parent. | A standalone CQ absent-parent observation and the boundary between coverage and answerability. | A CQ actor, reviewer identity or source authority. |
| `extraction-run-trace.md` / `parallel-worker-default-recipe.md` | Synthetic run traces with worker scope but no actor parent. | The distinction between worker-scope/recipe roles and a run actor mapping. | A populated run actor or evidence that the recipe was an actual run. |
| `claim-backed-card.md`, `minimal-card.md`, `rich-profile-card.md` | Three synthetic concept-card records omit the actor parent. | Three synthetic absent-parent card observations, distinct from the template object/null. | That an actor was never present, or that the field is inapplicable. |
| Four current templates | Actor object is present with null `id`, `mode` and `role`. | Explicit template object/null state. | Requiredness, actor class, or a populated identity contract. |

The rich and teaching original files are registered with their preserved
planning copies and both manifests. Direct hash/copy checks are replayed in
`validation-evidence.md`; the copy is preservation evidence, not an additional
extraction or independent actor observation.

## Per-member semantic dispositions

The complete member records, evidence references, exceptions and unresolved
questions are in `semantic-membership.json`. The bounded conclusions are:

| Member | Effective meaning in this population | Specific disposition |
| --- | --- | --- |
| `actor` / claim | Claim-local provenance slot; only template object/null is observed. | Preserve the explicit null state. Do not infer whether it names authoring, extraction, review or another activity, and do not inherit a card/run/source actor. |
| `actor` / competency-question | Standalone CQ-local provenance slot; template object/null and synthetic absent-parent states are observed. | Preserve null versus absent. A card CQ reference, question text, requirement source, coverage state or answerability result does not supply the CQ actor. |
| `actor` / concept-card | Card-revision provenance mapping; populated cards record `codex-cc` or `codex` with `agent-direct` / `extractor`, while template and absent families remain distinct. | Retain exact family/revision labels and role/mode observations. Do not promote them to unique principals, source authors, model versions or inherited embedded actors. |
| `actor` / extraction-run | Run-local actual-actor-and-scope slot; only template object/null and synthetic absent-parent states are observed. | Preserve both states. Worker-scope roles, output-card actors and source identities do not fill a missing run actor. |
| `actor.id` / claim | Identity child within a claim actor object; selected value is template null. | Retain null as unfilled and separate it from root claim `id`; no global identity or source-author meaning. |
| `actor.id` / competency-question | Identity child within a standalone CQ actor object; template null, synthetic CQ child not applicable. | Retain null versus not-applicable; do not derive identity from CQ text, `cq_refs`, component refs or parent-card actor. |
| `actor.id` / concept-card | Recorded card actor label; 21 strings are `codex-cc` or `codex`, one template is null and nine parents are absent. | Preserve spelling, family, revision and parent state. Do not normalize the two labels or assert a unique human/model/tool/process principal. |
| `actor.id` / extraction-run | Identity child within a run actor object; template null, synthetic run child not applicable. | Retain null versus not-applicable. Future populated identity requires direct run evidence; worker roles and output-card labels are not substitutes. |

## Source author versus actor identity

The witnesses carry source refs and source snapshots such as `ccn-book`, but
the selected actor evidence does not identify a source author. The labels
`codex-cc` and `codex` are recorded actor values in generated card
frontmatter; they are not source-author values and do not identify a human,
model version, tool version or globally unique process. A source author, an
actor that performed extraction, an actor that reviewed a result, a run
identity and a record identity remain separate until a populated, scoped
provenance witness connects them.

Likewise, the card bodies' claim/CQ/run references are declarations or local
navigation. They do not create embedded actor mappings. The absent CQ and run
parents therefore remain absent, and the template nulls remain null; no actor
is manufactured from a parent card or referenced run.

## Operational consequences

| Surface | Consequence |
| --- | --- |
| Reader | Render the actor label, role, mode and record/revision context when present; show absent/null as an explicit provenance limitation. Do not label it source authorship or verification. |
| Extractor | Preserve parent and child states, record direct actor evidence when available, and keep actor separate from source snapshots, method, run, claims, CQs and lifecycle results. |
| Query | Scope actor lookup to the record kind and revision. A matching label is a bounded observation, not a global principal join; an absent parent is not a null child match. |
| Migration | Preserve exact label spelling, family context and absent/null/populated state. Do not normalize `codex-cc` to `codex`, map a source author into actor, or inherit card actor into embedded claims/CQs/runs. |

## Bounded unknowns and outside ownership

This slice does not decide:

- whether an actor is a human, model, tool, process or composite;
- whether the actor on each record kind means author, extractor, reviewer,
  recorder, operator or another activity;
- the relation among run actors, worker actors and output-card actors;
- the meanings or requiredness of `actor.mode` and `actor.role`; or
- any future schema language, field structure, identity authority,
  specification format or publication policy.

The remaining 32 actor-family pairs (`actor` and `actor.id` across the other
six kinds, plus `actor.mode` and `actor.role` across the ten actor-bearing
kinds) remain with the planned Slice14 complement. Slice14 also retains the
broader run, preparation, method, shared-reference and CQ-provenance work
from Slice03. Its workload must be censused and split before execution; this
handoff does not open it. P-15 remains a mandatory operator design discussion.
