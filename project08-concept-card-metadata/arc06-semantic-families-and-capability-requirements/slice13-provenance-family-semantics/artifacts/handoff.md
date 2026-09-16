# Slice13 handoff

Status: CC proposed-done; independent CDC verification is required. This
packet analyzes exactly eight actor/actor.id pairs and accepts zero new
coverage pairs. The CC contribution endpoint is recorded in the closing
report after the scoped commit; CDC must independently reproduce the literal
route against that endpoint.

## Pinned state and delivered files

- Source checkout: `e763c661592ff1097a94bb470db9cf924524579d`, clean and
  unchanged.
- Original planning opening: `609f2f558b100a06df42e6a8b85ebfe200a27b22`; original
  CC endpoint: `78be7fabae79039ef3f24daa639d8e314ebcee0f`.
- Repair planning opening: `e42419482aebabcdac9be9e3032daa8f72da09d3`, clean
  before this repair; the repair endpoint is recorded in `closing-report.md`.
- Opening/current accounting: 180 accepted / 375 remaining / eight assigned /
  367 outside. Assignment is not acceptance and the coverage register was not
  changed.
- Immutable transition accounting remains 115 accepted / 440 remaining / 35
  transition-assigned / 405 outside that transition snapshot.
- Six authorized files are the two semantic artifacts, validation evidence,
  handoff, slice ledger and closing report. No source, plan, coverage,
  previous-slice or CDC-verification file was changed.

The durable packet contains:

1. `artifacts/semantic-membership.json`: the exact eight pairs, eight
   member-specific meanings, 37-record native census, 51 registered inputs,
   two original/copy mappings, limits and unresolved questions.
2. `artifacts/semantic-evidence.md`: contextual rule/body/witness comparison,
   parse and parent/child state distinctions, operational consequences and
   outside ownership.
3. `artifacts/validation-evidence.md`: the complete Bash/jq/Git/hash route,
   independent expected values, native observations, R1 registry mutation
   controls, R2 endpoint/snapshot separation and R3/R4 negative controls.
4. This handoff and the six-row closeout in `closing-report.md`.

## Supported conclusions

1. The selected frozen population is 37 parsed mappings: one claim, two
   competency questions, 31 concept cards and three extraction runs.
2. Actor parent states are 12 absent, four object/null template states and 21
   object/string states. No null parent, empty parent, missing `id` child,
   empty string or unexpected type occurs in the selected parsed population.
3. The 21 populated card labels are bounded observations: four Arc07 pilot
   cards use `codex-cc`, while seven rich and ten teaching rerun cards use
   `codex`; all observed card role/mode pairs are `extractor` / `agent-direct`.
   The labels do not establish a unique human, model version, source author,
   tool, process or global principal.
4. Claim, standalone CQ and extraction-run actor meanings remain
   unpopulated in the frozen selection. Their templates expose object/null;
   the synthetic CQ and both synthetic run examples expose absent parents.
5. Root record identity is not actor identity. Source authorship, run
   identity, actual performer, recorder and reviewer remain distinct. A card
   actor does not silently populate an embedded claim/CQ actor, and a run ref
   does not supply a run actor.
6. The packet does not choose actor classes, role/mode semantics, requiredness,
   schema language, specification format, migration policy or operator
   acceptance. P-15 remains open.

## Iteration 01 repair dispositions

- **R1 — repaired in the CC route:** the expected eight pairs are derived from
  the repair-opening slice plan, compared with the authored scope and actual
  memberships, and checked for uniqueness, inclusion and disjointness against
  the repair-opening coverage snapshot. Meaning IDs and both member/shared
  evidence-ID layers resolve. Invalid-member and dangling-reference variants
  are rejected by the same predicates. Baseline mappings resolve through their
  registered manifests and native bytes.
- **R2 — repaired in the CC route:** the original `609f2f55 → 78be7fab`
  history, repair-opening `e4241948 → repair endpoint` history and current
  live status are recorded separately. The committed wrapper extracts its
  recipe by a separate revision and loads the registry from `CC_COMMIT`; the
  repair-opening plan, coverage and frozen inventory are Git-pinned. Live
  coverage is reported without requiring obsolete assignment bytes.
- **R3 — repaired by explicit removal:** the redundant raw actor `rg` search
  that swallowed errors is no longer presented as evidence. Hash-bound native
  field-state checks remain, and the jq missing-input control still records a
  real status-2 tool error with stderr. Successful no-match remains distinct.
- **R4 — repaired:** the native route reproduces the 2,054 parsed legacy
  untyped mappings with absent actor parents and not-applicable nested
  `actor.id`; compares every authored 37-record family/state/label cell and
  the three named YAML exclusions; registers the third synthetic card witness;
  corrects the field-group attribution; and registers Project08 instructions
  separately from planning-root instructions with precise source ranges.

These are CC repair attestations, not independent CDC closure. S13-1 and
S13-6 retain their prior CDC-verified status; S13-2 through S13-5 require a
fresh independent committed replay and review.

## Concrete unresolved decisions and tests

The next evidence must answer these questions with populated, scoped records
where possible:

- Which event does actor denote on each record kind: authoring, extraction,
  review, recording, operation or another activity?
- What direct evidence makes an `actor.id` label identify a human, model, tool,
  process or composite, and is that identity local to a record/revision or
  comparable across runs?
- How do run actors, worker actors and output-card actors relate without
  collapsing their scopes or turning agreement into verification?
- Are `codex-cc` and `codex` intentionally different session/process labels,
  and what evidence would permit or forbid a migration mapping between them?
- How should an absent actor parent, a present null actor object and a
  populated actor be represented and queried without invented requiredness?
- What evidence can connect an embedded CQ or claim to a standalone actor
  record without treating a card reference, question text or parent revision
  as identity proof?

Useful executable follow-ups are a populated claim/CQ/run actor witness, a
cross-revision label comparison with an independently authored expected
identity, and a worker/run/card provenance comparison. These are proposed
tests, not performed work.

## Ownership and proposed next sizing

The planned Slice14 complement retains all original provenance/shared-reference
responsibilities not assigned here. It includes actor and actor.id across the
other six actor-bearing kinds (12 pairs), actor.mode and actor.role across all
ten actor-bearing kinds (20 pairs), and the broader run, preparation, method,
shared-reference and remaining CQ-provenance interfaces. The actor-family
complement is therefore 32 pairs before the broader provenance fields are
counted.

Before any Slice14 prompt is issued, census its actual kinds and contexts and
split it with review headroom. A concrete proposal is:

- **Candidate Slice14A:** actor/actor.id across the remaining six kinds (12
  pairs), preserving parent/child and role-specific boundaries exposed here.
- **Candidate Slice14B:** actor.mode/actor.role across the ten kinds (20
  pairs), only after 14A establishes whether the observed actor labels and
  roles have enough distinct context for a coherent unit.
- **Later bounded provenance units:** created-at, run/preparation/method and
  shared-reference/CQ provenance families, sized from their native census and
  split again if their evidence layers exceed one context with review
  headroom.

This is a sizing proposal, not a new assignment, plan change or opened slice.
Other Arc06 family owners and the 367 not-yet-sliced pairs remain unchanged.
Arc06 composition, CDC acceptance and the P-15 operator schema/specification
discussion remain separate gates.
