# Slice02 handoff

Status: CC proposed-done; independent CDC review is required.

## Pinned state

- Source opening HEAD: `e763c661592ff1097a94bb470db9cf924524579d`, clean and
  unchanged.
- Original CC endpoint: `753bacb051c041a75d0c4d36595cfbadd5a9b5eb`.
- Repair opening planning HEAD: `f15c896bfeec4c3618387413e63c95dfe9fc6771`,
  clean before this repair.
- The opening slice-plan authority is read from `a27c4d33…`; the pre-review
  six-row ledger authority is read from `753bacb0…`. Live plan/ledger status
  hashes are reported separately because CDC updates them.
- CC repair endpoint: the explicit seven-file commit reported with this packet;
  CDC must resolve and set it as `CC_COMMIT` in the designated replay.
- Current accounting: 150 accepted, 405 remaining, 30 assigned here, 375
  outside. No membership is accepted by assignment.
- Source, frozen inventory, transition register, accepted Slice01/Slice12
  packets, plans and coverage register were not edited.

## Preserved capability

1. Legacy `answers_questions` strings remain exact and reverse-queryable. The
   native Music and Erlang witnesses return their source card paths, after
   which their readable bodies can be inspected.
2. Current CQ references retain id, path/fragment and requested revision as
   separate declarations. Rich and teaching embedded CQs demonstrate that a
   literal heading can be inspected without claiming a rendered anchor or
   standalone target record.
3. CQ component roles, coverage summaries, answerability and question status
   remain separate. The synthetic partial example demonstrates that a
   component list and a partial answerability state do not supply source
   warrant or verification.
4. Absent, empty and populated states remain visible across all six card
   families. Three malformed rich inputs remain explicit exclusions rather
   than being turned into semantic absence evidence.
5. Historical body value is retained: legacy card bodies explain their
   questions, the pilot explicitly records no CQ, and generated rich/teaching
   cards retain question-specific expected-answer text.

## Limits and loss risks

- A legacy question string has no stable CQ identity, revision, role or answer
  criterion. Exact reverse lookup proves discoverability, not answer adequacy.
- `competency_question_refs` and `cq_refs` have different observed names and
  populations. The frozen population has no populated
  `competency_question_refs` item to establish equivalence.
- A card CQ tuple may name an unavailable external path. The rich-profile
  target's parent path is absent; the bounded `test ! -d` observation succeeds
  with unresolved availability. It is distinct from the separate rg tool-error
  control and is not a semantic no-match.
- An embedded fragment and literal heading are not automatically a rendered
  anchor. The rich and teaching cards also use different CQ IDs despite the
  same card concept ID.
- Coverage, answerability, retrieval, verification, reconciliation,
  preservation and admission remain different claims. No completed answer,
  source support, schema conformance or memory admission is claimed here.

## Outside owners and re-entry

The following fields share CQ records but are outside this assignment:

| Boundary | Owner | Re-entry question |
| --- | --- | --- |
| actor, created_at, run and requirement-provenance mechanics | Slice03 | What shared reference contract gives each role stable scope and provenance? |
| evidence_grade and extraction_confidence | Slice04 | What subject, rubric and scope justify each assessment? |
| validation/verification and retrieval result fields | Slice05 | Which structural and semantic checks are independently applicable? |
| reconciliation and replacement | Slice06 | What conflict, revision and replacement effects attach to this CQ? |
| preservation/prior value | Slice07 | What old question/coverage value must survive a revision? |
| admission/authority | Slice08 | What reliance or approval scope, if any, is authorized? |
| surface class and synthetic discovery markers | Slice09 | How do family-specific origins compose without a catch-all? |

## Architecture and research questions

These are questions for later research and the P-15 operator discussion, not
decisions made by this inventory packet:

1. Should the future representation use one canonical CQ reference shape, or
   retain explicitly named legacy/current surfaces with a migration mapping?
2. How should a legacy question string receive stable CQ identity without
   treating equal text as equal requirement, revision or intended use?
3. What target-path, fragment and rendered-anchor policy makes an embedded CQ
   resolvable and testable without claiming a renderer was run?
4. Should answer criteria be required at CQ root, assertion level, or both,
   and how will each component's support be inspected?
5. Which state vocabulary distinguishes coverage, answerability, retrieval,
   verification and admission without implying more than the evidence shows?

The operator must discuss schemas and the creation of a specification before
normative adoption. This packet supplies evidence and concrete questions only;
it does not choose a schema language, field structure, requiredness policy or
specification publication format.

## Verification handoff

Run the fenced block in
`.worktrees/planning/project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/artifacts/validation-evidence.md`
from the source checkout. Use `CC_PRECOMMIT=1` for the working-tree rehearsal
and the exact committed repair endpoint as `CC_COMMIT` for CDC. Check the
seven-file scope, both pinned planning authorities, all registered hashes and
original/copy manifests, the full census, the four native cases and their
wrong-target/tool-error and altered-value controls, and the preservation diff.
CDC writes `cdc-verification.md` later; CC must not create it in this slice.
