# Slice02 semantic evidence: competency questions and answerability

Status: CC proposed-done. This is an evidence-backed inventory interpretation,
not schema adoption, source-truth acceptance, extraction-quality acceptance, or
operator approval.

## Opening state and evidence boundary

- Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`, opening
  `e763c661592ff1097a94bb470db9cf924524579d`, clean.
- Planning checkout: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`,
  opening `a27c4d33a02d3e6047656b9ae0c17a145aa3f208`, clean.
- Frozen parsed population: 2,054 eligible legacy mappings, 31 parsed
  concept-card mappings across six families, two standalone competency-question
  mappings, and three malformed rich-card exclusions.
- Current accounting: 150 accepted, 405 remaining, 30 assigned here, 375
  remaining outside. The immutable transition snapshot remains 115/440/35.
- Every path/hash and role used by this packet is registered in
  `semantic-membership.json`. No generated copy was used without a stated
  original/copy role; the representative pilot is an existing preserved
  planning artifact, not a new extraction.

## Historical rule versus current observation

The two registered v3.2 prompts are historical authorities for what the old
workflow asked of cards, not a decision about the future profile.

| Evidence | Directly observed rule | Limit |
| --- | --- | --- |
| `v32Howto` | `answers_questions` is a readable string list; typed relationships use exact slugs; the quality checklist asks for at least one CQ and CQ coverage. | It does not provide standalone CQ identity/revision or prove that every frozen card was generated under the rule. |
| `v32Parallel` | CQ elicitation is a source-scoped question set; the historical template links cards to questions and the verification route asks whether a card actually contains enough information to answer. | Its 30–50 elicitation target is a historical workflow target, not a current field-requiredness decision. |
| `graphGuide` | A CQ needs identity, question text, origin/intended use, answer criteria, component coverage and bounded answerability; retrieval, verification and admission remain separate. | The guide is method guidance, not an adopted schema or runtime. |

The useful distinction is therefore: a legacy question string is a discovery
assertion; a CQ record is a typed construct with its own identity and scoped
criteria; a card reference is a declaration that still needs target and body
inspection; and coverage, answerability, status, retrieval and lifecycle
results cannot be collapsed.

## Frozen selected-field census

The census is the population, not the 30-pair assignment. Legacy mappings have
no literal `record_kind`; the `untyped` label below is normalized only after
selecting parsed mappings with object-valued `values`.

### Legacy question index

| Family | Parsed records | `answers_questions` root | Items | Item type | Distinct strings |
| --- | ---: | --- | ---: | --- | ---: |
| Complete Musician | 390 | populated array on 390 | 574 | string | 379 |
| Erlang | 1,664 | populated array on 1,664 | 4,059 | string | 3,265 |
| Total | 2,054 | populated array on 2,054 | 4,633 | string | 3,644 |

The selected `answers_questions[]` member therefore represents one stored
question string, not a CQ record. The current native reverse lookup found one
Complete Musician card for `What are the different types of accent in music?`
and one Erlang card for `What is a behaviour in OTP?`. The inspected bodies are
substantive and readable: `accent-types.md` explains temporal and nontemporal
accent types, while `behaviour.md` explains generic/callback division and lists
standard OTP behaviours. That is evidence of discoverability and body material,
not proof that either card satisfies every possible answer criterion.

### Six parsed card families

| Family | Cards | `competency_question_refs` | `cq_refs` | Interpretation |
| --- | ---: | --- | --- | --- |
| Arc07 expanded | 6 | absent 6 | absent 6 | No selected current CQ-reference field. |
| Arc07 pilot | 4 | absent 4 | empty 4 | The named pilot witness explicitly says no CQ is asserted. |
| Rich rerun | 7 | absent 7 | populated 7, one item each | Embedded CQ declarations are present in the selected generated family. |
| Synthetic examples | 3 | absent 2, empty 1 | absent 2, populated 1 | Minimal card preserves an empty legacy-named collection; rich profile has one declared external CQ tuple. |
| Teaching rerun | 10 | absent 10 | populated 10, one item each | Embedded CQ declarations are present, but lifecycle states remain candidate/unassessed. |
| Template | 1 | absent 1 | empty 1 | Template shape is not a real-corpus CQ extraction. |
| **Parsed total** | **31** | 30 absent / 1 empty | 12 absent / 1 empty / 18 populated | No requiredness or equivalence is inferred from these observations. |

The 18 populated `cq_refs[]` items all request revision `1`. The selected
`competency_question_refs` root has no populated items, so its nested item
meaning is not observed in this frozen population. The two names remain
distinct. The current generated cards use `cq_refs`, while the minimal example
uses an empty `competency_question_refs`; no migration equivalence is assumed.

Three rich-rerun inputs are malformed and excluded from the parsed denominator:
`INDEX.md` has no opening frontmatter, and `cc-memory-forms.md` and
`cc-priming-forms.md` fail the frozen YAML parser. They are limits, not parsed
absence witnesses and not negative CQ evidence.

### Standalone competency-question population

There are only two standalone CQ records in the frozen population: the current
template and the synthetic `cq-coverage` example. They are not successful
real-corpus CQ extraction.

| Selected field/state | Template | Synthetic `cq-coverage` |
| --- | --- | --- |
| `question` | null | one string: “Can a reviewer locate the source support for a claim?” |
| `roles` | empty array | absent |
| `requirement_source_ref` | null | absent |
| `intended_use` | null | absent |
| `answer_criteria` | null | absent |
| `coverage_assertions` | one item; id/revision/component/assertion null, covered/support refs empty, state `unassessed` | absent |
| `component_refs` | absent | three object items: concept, claim, source-support; all revision 1 |
| `coverage_state` | absent | `partial` |
| `answerability_state` | `unassessed` | `partially-answerable` |
| `cq_status` | `draft` | absent |

The synthetic record is deliberately partial: its body says the references
are fictional and retrieval is unassessed. The three component IDs being
written down does not create a source-support record, and the template's
coverage assertion slot does not establish that the synthetic component list
conforms to it.

## Representative body and reference readings

- The legacy Music and Erlang cards retain actual `answers_questions` strings
  and readable bodies. Reverse lookup is executable against the frozen native
  inventory; it should not be replaced by a title or slug search.
- The preserved Arc07 pilot card for `cc-model-data-constraints` explicitly
  says no CQ is asserted and leaves the candidate without CQ coverage or
  answerability. This is a useful negative observation, not an extraction
  failure converted into absence across every family.
- The rich rerun card declares `cq-model-constraint-trust`, revision 1, with
  fragment `#cq-model-constraint-trust`; its literal heading and expected
  answer text are present. The teaching rerun declares a different identity,
  `cq-model-data-constraint`, revision 1, with its own literal heading and
  answer text. Their same concept-card ID does not make their CQ identities or
  wording equivalent.
- The rich-profile synthetic card declares
  `cq-inspect-support-for-card-statement`, revision 1, at
  `records/cq-inspect-support-for-card-statement.md`. The bounded source root
  has no such `records/` parent, so the direct path check fails as a path/tool
  error. That is not a successful semantic no-match and does not prove that a
  different source root or rendered anchor would fail.
- The current template and examples preserve readable body sections and make
  explicit that component references, coverage, answerability, verification,
  reconciliation, preservation and admission have different scopes. The body
  carries teaching value; frontmatter presence alone cannot establish it.

## Operational consequences

| Concern | Preserved capability | Limit or migration question |
| --- | --- | --- |
| Reader | Readable legacy questions and current CQ/answer sections remain discoverable; generated cards retain body-level explanation. | A question string or heading does not show that the answer meets criteria. |
| Extractor | Can retain exact question strings, stable current tuples, component roles, coverage assertions and explicit unknown states. | Must not synthesize CQ identity from matching text, inherit revisions from a parent card, or turn prose into coverage/support. |
| Query | Exact legacy reverse lookup works; current tuple lookup can separate id, revision, path availability, literal heading and body text. | External target paths, embedded fragments and rendered anchors require their own resolver policy; no graph/RAG/runtime is implied here. |
| Migration | Can preserve absent/empty/populated states and map legacy discovery to candidate references for later review. | A legacy string has no stable id/revision; `competency_question_refs` and `cq_refs` are not silently merged; migration needs identity, deduplication and target-anchor policy. |

## Bounded unknowns and outside owners

This packet intentionally does not assign actor/created-at/run or broader
requirement-provenance mechanics (Slice03); evidence grade and extraction
confidence (Slice04); validation/verification and retrieval-result fields
(Slice05); reconciliation and replacement (Slice06); preservation (Slice07);
or admission (Slice08). Surface-class and synthetic-discovery integration is
owned by Slice09. Those fields share a CQ record but are not absorbed by the
30 selected pairs.

The packet poses, but does not decide, architecture questions: whether a CQ
should have one canonical reference shape or multiple explicitly named
surfaces; whether embedded fragments need declared heading/anchor policy; how
legacy question strings are assigned stable identities; and how answer criteria
map to assertion-level support. P-15 still requires operator schema and
specification discussion before any normative field structure is chosen.
