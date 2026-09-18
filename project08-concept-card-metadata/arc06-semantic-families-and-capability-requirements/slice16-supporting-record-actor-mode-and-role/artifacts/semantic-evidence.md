# Slice16 semantic evidence: supporting-record actor mode and role

Status: CC proposed-done; independent CRC verification and CDC composition
review remain required. This is an evidence-backed semantic inventory, not a
schema, vocabulary, runtime, memory-admission or acceptance decision.

## Intake and contract readback

The intake loaded the active Project08 instructions, this Slice16 prompt,
slice plan and ledger, the current project and Arc06 plans and ledgers, the
CDC directive, current/frozen coverage, the complete Slice15 registry,
semantic evidence, handoff, CRC verification and mechanical validation route.
Required extents were: project instructions 1-90; prompt 1-185; slice plan
1-137; slice ledger 1-14; CDC directive 1-233; project plan sections 39-269;
Arc plan sections 22-91 and 153-309; project ledger 1-43; Arc ledger 1-37;
current coverage 1-640; transition coverage 1-637; frozen inventory one JSON
document; Slice15 membership 1-266, semantic evidence 1-149, handoff 1-69,
CRC verification 1-103 and validation route 1-375.

Required source records were read completely: the six selected templates at
81, 62, 65, 61, 69 and 59 lines; the memory-admission and relationship-edge
examples at 36 and 37 lines; the four Arc07 pilot support witnesses at 55,
55, 56 and 56 lines. The source reference and guides were loaded at these
complete extents: record-field-groups 1-31; operator workflow 1-166;
extraction 1-248; preservation 1-222; evidence lifecycle 1-204; graph/CQ
1-177; validation/verification 1-231; memory admission 1-153; testing 1-91;
prompt authoring 1-440; row closure 1-78; concept-cards skill 1-158;
collaboration framework 1-538; project management 1-65 and its wayfinder
1-178. The conditional Slice15 route trigger applied because its hashing,
range, wrapper and preservation mechanics are reused; its complete route was
loaded and reused mechanically, without importing its eight-pair semantics.

The source checkout was clean at `ce3f77103eff5e07b3533a03c65f158684fc1039`.
The planning checkout was clean at
`3b7790f88cd30fa6c4988a6950b4989ae1933b7d`, the Slice16 opening commit. The
source baseline named by the prompt matches the live source. The frozen
inventory hash is
`afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`; current
coverage at opening is `54c79814ba4ef7cca0b038274249d5e8738df928afa7588ffe6686f3490a3cc7`.
The raw inventory records the four planning pilot paths with a
`.worktrees/planning/` prefix because of its acquisition context. The registry
removes only that checkout prefix when addressing the same committed planning
files; the raw inventory and its hash remain unchanged.

The binding contract connects the six rows to six record-local actor slots:
memory admission must not collapse actor role/mode into decision authority or
operator acceptance; preservation must not collapse them into disposition or
review; edges must not collapse them into endpoint roles; locators must not
collapse them into address or resolution; source support must not propagate its
actor to `subject_ref`; and validation results must not collapse them into
`validator_identity`. The native query, same-predicate mutations and route
controls below make those distinctions observable. The easily missed rule is
that the repeated pilot `agent-direct`/`extractor` label is only a support-record
observation: it cannot become a global vocabulary, a source author, a claim or
card actor, a validator, an admission authority, or an acceptance decision.

## Native census and exclusions

The frozen native query selected only parsed, object-valued records whose
`record_kind` is one of the six assigned kinds. It returned twelve records:

| record kind | records | parent absent | template child-null | populated actor |
| --- | ---: | ---: | ---: | ---: |
| memory-admission | 2 | 1 | 1 | 0 |
| preservation-decision | 1 | 0 | 1 | 0 |
| relationship-edge | 2 | 1 | 1 | 0 |
| source-locator | 1 | 0 | 1 | 0 |
| source-support | 5 | 0 | 1 | 4 |
| validation-result | 1 | 0 | 1 | 0 |
| **total** | **12** | **2** | **6** | **4** |

The two parent-absent records are the synthetic memory-admission and
relationship-edge examples. The six template records reserve actor objects
with null `id`, `mode` and `role`. The four populated records are the exact
Arc07 pilot source-support paths:

- `support-emergent-explanation.md`
- `support-memory-consolidation.md`
- `support-model-data-constraints.md`
- `support-pattern-separation.md`

Each populated support records
`{id: codex-cc, mode: agent-direct, role: extractor}`. These are direct
support-record observations. Their `subject_ref` points to a claim, but the
support actor does not populate or authorize that claim's actor.

The three exact YAML::XS exclusions remain outside the parsed denominator:

- `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-memory-forms.md`
- `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-priming-forms.md`
- `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-recognition-dual-process.md`

Fifteen no-frontmatter records are a separate availability state. The legacy
untyped parsed population is 2,054 records; every one has an absent actor
parent, with no nested mode/role and no dotted `actor.id` key. Neither parse
failure nor legacy absence is a negative observation about a typed actor slot.

## Kind-specific meanings and consequences

The registry contains twelve definitions, applicability statements, observed
states, evidence IDs, exceptions, and reader/extractor/query/migration
consequences. The concise row walk is:

| pair | observed state and bounded meaning | consequence / unresolved question |
| --- | --- | --- |
| `actor.mode` / memory-admission | template null; synthetic parent absent; admission-local operation slot | keep decision authority, acceptance and stage separate; what activity would populate it? |
| `actor.mode` / preservation-decision | template null only; preservation-local operation slot | keep disposition/review separate; comparison, decision-recording or application? |
| `actor.mode` / relationship-edge | template null plus synthetic parent absence; edge-local operation slot | keep endpoint roles/direction separate; source-reported versus editorial creation? |
| `actor.mode` / source-locator | template null only; locator-local resolution/reporting slot | keep address and resolution observation separate; resolution, extraction or reporting? |
| `actor.mode` / source-support | four pilot `agent-direct`, one template null; support-record slot | do not propagate to subject claim/card; extraction, comparison or whole-pilot activity? |
| `actor.mode` / validation-result | template null only; result-local check activity slot | keep validator identity/method/outcome separate; what result actor activity? |
| `actor.role` / memory-admission | template null plus synthetic parent absence; admission-local activity role | not decision authority or admit/reject/defer; assessment, authorization or recording? |
| `actor.role` / preservation-decision | template null only; preservation-local activity role | not disposition or operator review; how distinct from reconciler/operator? |
| `actor.role` / relationship-edge | template null plus synthetic parent absence; edge-local activity role | not endpoint roles; how distinguish source-reported and editorial roles? |
| `actor.role` / source-locator | template null only; locator-local resolution/reporting role | not source author or locator status; what direct witness warrants a role? |
| `actor.role` / source-support | four pilot `extractor`, one template null; support-record activity role | not subject claim actor, source author or validator; span selection or support writing? |
| `actor.role` / validation-result | template null only; result-local check activity role | not `validator_identity` or independent verification; what direct role is warranted? |

The shared rule is limited to preservation of exact parent state, child state,
record kind, family and revision. It applies to all twelve members only as a
state-preservation rule. The effective semantic role differs by member: a
support actor is attached to a support-to-span comparison; a validation actor
is attached to a result record; an edge actor is not an endpoint role; and an
admission actor is not a decision authority. No populated mode/role policy is
justified for the eight null/absent non-support records.

## Slice15 comparison and capability implications

Slice15 observed `agent-direct`/`extractor` on 21 generated concept cards,
across pilot, rich and teaching families, with `codex-cc` and `codex` IDs. This
slice observes the same spelling only on four Arc07 source-support records,
all with `codex-cc`. The repeated label is therefore a cross-group comparison
witness, not evidence of actor equivalence or inheritance. Slice15's template
null and synthetic absent distinctions recur here, but the six support-record
contexts supply different field-specific boundaries.

For readers and auditors, preserve exact actor values, IDs, family, kind,
revision and parent/child state while showing decision authority, disposition,
endpoint role, locator resolution, support subject, validator identity and
operator acceptance separately. Extractors must preserve support actor and
source-span caveats without filling absent admission, preservation, edge,
locator or validation actors. Queries must scope actor fields to their record
kind and revision; migration must not normalize the pilot strings into a
global enum, principal registry or inheritance rule.

Slice17 retains run identity/scope/workers/outputs, source preparation links,
method/prompt/time provenance, shared references and remaining CQ provenance
interfaces. Existing evidence/lifecycle owners retain evidence/confidence,
validation/verification, reconciliation, preservation and admission meanings;
this packet cross-references those boundaries but does not reassign them.

## Validation limitations

The route is structural evidence. It proves retrievability, counts, state
distinctions, references, scope and control behavior; hashes and ranges do not
prove semantic warrant. Same-context CC checks are not CRC verification. No
schema, actor enum, source implementation, parser, graph/runtime, package,
extraction, memory admission, UAT or coverage acceptance was performed.
