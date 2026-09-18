# Slice15 semantic evidence: provenance roles, runs, and shared references

Status: CC proposed-done; independent CRC verification and CDC composition
review remain required. This report records source-grounded observations. It
does not accept a field vocabulary, authorize a schema change, or close P-15.

## Scope and evidence boundary

The opening source checkout was clean at
`76a69fd9c295e78f23faa651746c2e36646e0ebd`. The opening planning checkout was
clean at `4db8d8829185ac8fa0a9d9c74783466cfd45682a`. The assignment is the
initial Slice15 prompt and its exact eight pairs:

| field | record kind |
| --- | --- |
| `actor.mode` | `claim` |
| `actor.mode` | `competency-question` |
| `actor.mode` | `concept-card` |
| `actor.mode` | `extraction-run` |
| `actor.role` | `claim` |
| `actor.role` | `competency-question` |
| `actor.role` | `concept-card` |
| `actor.role` | `extraction-run` |

The native inventory is the frozen Slice01 inventory at the opening planning
commit. The selected parsed denominator is 37 records: one claim, two
competency questions, 31 concept cards, and three extraction runs. Three
records with YAML parse errors are exclusions from that denominator; 15
records have no opening frontmatter and are a separate availability state.
The registry in `semantic-membership.json` is the machine-readable companion
for every count, witness, hash, and membership below.

## Native census

| selected records | count |
| --- | ---: |
| parsed object mappings | 37 |
| actor parent absent | 12 |
| actor parent object with both children null | 4 |
| actor parent object with populated mode and role | 21 |
| actor mode `agent-direct` | 21 |
| actor role `extractor` | 21 |

The four template records carry `actor: {id: null, mode: null, role: null}`.
The 12 absent parents are not converted to null. All 21 populated actor
children occur on generated concept cards: four pilot cards, seven rich-rerun
cards, and ten teaching-rerun cards. Their literal IDs are `codex-cc` for the
four pilot cards and `codex` for the 17 workbench cards. This is a provenance
observation about these generated artifacts, not a principal, authority, or
global vocabulary decision.

The selected family/kind cells are:

| kind | family | actor.mode / actor.role state | n |
| --- | --- | --- | ---: |
| claim | template | child-null / child-null | 1 |
| competency-question | synthetic | parent-absent / parent-absent | 1 |
| competency-question | template | child-null / child-null | 1 |
| concept-card | expanded | parent-absent / parent-absent | 6 |
| concept-card | pilot | `agent-direct` / `extractor` | 4 |
| concept-card | rich | `agent-direct` / `extractor` | 7 |
| concept-card | synthetic | parent-absent / parent-absent | 3 |
| concept-card | teaching | `agent-direct` / `extractor` | 10 |
| concept-card | template | child-null / child-null | 1 |
| extraction-run | synthetic | parent-absent / parent-absent | 2 |
| extraction-run | template | child-null / child-null | 1 |

The legacy comparison contains 2,054 parsed untyped mappings. Every one has
an absent `actor` parent; none has a null or object parent, a nested
`actor.mode`, a nested `actor.role`, or a literal dotted `actor.id` key. This
is a bounded inventory result, not evidence that legacy provenance never
existed. YAML failures are not negative actor observations, and no-frontmatter
records are not parsed objects.

## Source-grounded distinctions

The concept-card load contract defines construct boundaries and availability
states. The operator workflow requires scope and construct boundaries to be
recorded before deriving content. The extraction guidance establishes an
extraction run and separates run context from worker scope. The graph/CQ
guidance treats CQ roles, coverage, and answerability as CQ-local structures.
The validation guidance distinguishes observed values from expected values and
requires recoverable review evidence. The record-field reference groups
`actor` as a provenance/operational group rather than as a source-author or
claim-verification substitute.

The templates make the strongest direct observation available here: claim,
CQ, concept-card, and extraction-run templates reserve the actor object with
null children. The CQ coverage example and extraction-run trace demonstrate
real records with absent actor parents. The parallel-worker recipe provides
worker scope, role, and mode fields; those are not silently promoted to a
run's `actor.mode` or `actor.role`. The generated card witnesses are the only
populated values in the selected native census.

## Pair meanings and membership observations

Each pair below is a distinct record-local slot. The exact effective meanings,
exceptions, and evidence IDs are also recorded in the registry.

| pair | observed meaning | operational consequence |
| --- | --- | --- |
| `actor.mode` / claim | claim-local provenance mode slot; template null only | retain bounded absence; do not invent a mode enum or inherit source-author mode |
| `actor.mode` / competency-question | CQ-local activity mode slot; template null and parent absence | keep distinct from the CQ's query/coverage structures; no inferred query authority |
| `actor.mode` / concept-card | card-revision operation-mode label; populated cards say `agent-direct` | preserve exact value plus family and parent state; do not generalize to every card or principal |
| `actor.mode` / extraction-run | run-local actor mode; only absent/null states | keep distinct from worker-scope mode; defer a run-mode vocabulary |
| `actor.role` / claim | claim-local activity-role slot; template null only | do not substitute author/verifier roles or adopt a role enum |
| `actor.role` / competency-question | CQ-local activity role; template null and parent absence | preserve distinction from the CQ roles array; defer authority |
| `actor.role` / concept-card | card actor activity label; populated cards say `extractor` | preserve exact label and card-local context; do not treat it as source author, verifier, or principal |
| `actor.role` / extraction-run | run-local actor role; only null/absent states | keep distinct from worker roles, methods, and output-card roles |

The populated card witnesses show correlation, not inheritance: all 21 have
the same mode/role pair, but they span pilot, rich, and teaching families and
two literal IDs. The template and absent examples show that parent omission
and child null are separate states. Therefore the safest current capability
requirements are preservation and queryability of exact values, families,
record kind, and parent/child state; no requirement is justified for a global
actor vocabulary, cross-record inheritance, or principal identity.

## Capability implications

| consumer | supported now | must remain unresolved |
| --- | --- | --- |
| reader/auditor | report exact `actor` presence, mode, role, ID, family, kind, and null/absent state | authority, human identity, and semantic enum membership |
| extractor | preserve populated card provenance and template reservations without filling absent run/CQ/claim actors | run-to-card inheritance and default actor values |
| competency-question tooling | retain CQ-local role-array/query distinctions and actor slots independently | whether a CQ actor is an author, asker, reviewer, or executor |
| migration/query tooling | distinguish absent, null, and populated children; exclude parse failures from parsed denominators | backfill rules, vocabulary normalization, and acceptance criteria |

No source evidence permits treating `agent-direct`, `extractor`, `codex`, or
`codex-cc` as an accepted universal vocabulary. No evidence permits treating
worker scope fields as run actor fields. No evidence permits treating the
legacy absence census as proof of historical nonexistence.

## Validation and limitations

The companion validation route derives the census from the native inventory,
recomputes registered hashes and ranges, checks the exact eight-pair
assignment, exercises wrong-mode (`human-assisted`), wrong-role (`validator`),
swapped mode/role, absent-as-null, dangling-membership, a wrong registered
SHA-256 candidate, a wrong three-path YAML-exclusion candidate, no-match, and
missing-input controls, and separates precommit from committed replay. The
hash and YAML mutations run through the same predicates as their positive
checks; they do not mutate registered source/planning files. A failed
exploratory predicate that incorrectly required the eight assigned pairs to
equal all 20 remaining mode/role pairs was discarded; the correct predicate
is subset, disjoint from accepted, and exact in length.

The report is intentionally bounded by the opening source/planning bytes and
the frozen inventory. It does not alter the source schema or parser, update
coverage acceptance, admit memory, run UAT, or claim independent verification.
