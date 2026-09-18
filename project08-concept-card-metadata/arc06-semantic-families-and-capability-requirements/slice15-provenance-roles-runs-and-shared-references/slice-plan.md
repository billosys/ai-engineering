---
project: project08-concept-card-metadata
arc: arc06-semantic-families-and-capability-requirements
slice: slice15-provenance-roles-runs-and-shared-references
status: open
depends-on: [slice13-provenance-family-semantics, slice14-provenance-context-and-reference-semantics]
version: "1.0"
---

# Actor Mode And Role In Four Record Kinds

Interpret exactly eight `actor.mode`/`actor.role` field-path/record-kind
pairs across claim, competency-question, concept-card and extraction-run.
This is contextual semantic inventory, not a prescribed actor schema. The
stable slice slug predates the narrower approved assignment; the slug does
not authorize run/preparation/method/shared-reference work in this slice.

## Authority And Assignment

The Operator selected CDC + CRC + CC with Expedited Mode. CRC independently
closed Slice14; CDC's [arc directive](../cdc-directive01.md) answers the
[sizing escalation](../crc-escalation01.md) and approves this exact boundary.
CRC acknowledged it in arc-plan.md v1.18. CC executes the initial
`cc-prompt.md` and returns proposed-done to CRC through the Operator. CDC
retains design, structural scope and arc/project composition authority.

### Assignment History

| Prompt | Issued | Predecessor | Reason | Disposition |
| --- | --- | --- | --- | --- |
| cc-prompt.md | 2026-09-17 | arc directive01 and closed Slice14 | Eight kind-aligned mode/role pairs with native census, contextual meanings and replay | Current initial CC assignment; no execution recorded |

## Exact Scope And Ownership

~~~json
[
  ["actor.mode","claim"],
  ["actor.mode","competency-question"],
  ["actor.mode","concept-card"],
  ["actor.mode","extraction-run"],
  ["actor.role","claim"],
  ["actor.role","competency-question"],
  ["actor.role","concept-card"],
  ["actor.role","extraction-run"]
]
~~~

At opening: 555 frozen full / 200 independently accepted / 355 remaining /
eight assigned / 347 outside. Assignment is not acceptance. The frozen
transition, accepted Slice13/14 registries and source skills remain read-only.

Slice16 owns twelve mode/role pairs in the other six actor-bearing kinds.
Slice17 retains run identity/scope/workers/outputs, preparation, method/prompt/
time, shared reference and remaining CQ provenance interfaces for a later
CDC-approved split. Arc06's other named families retain primary ownership.
All 347 outside pairs remain Arc06-owned; they are not all Slice17 pairs.
P-15's operator schema/spec discussion and all UAT gates stay open.

## CRC Pre-Opening Reconnaissance

At authoring, planning `41e1383090fca7bf6e3723d5b5ade6ac138550d4`
and source `76a69fd9c295e78f23faa651746c2e36646e0ebd` were clean.
The frozen frontmatter inventory SHA-256 is
`afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`;
pre-assignment current coverage SHA-256 is
`cf2a8cb5455b48d9803bde3d6f8d41b7f3c577398d44f2141644d49dd9f382d7`.
CRC independently compared accepted plus remaining to the frozen 555-pair
set, verified unique counts, and found exactly twenty remaining mode/role
pairs: the eight above plus Slice16's twelve, with no accepted overlap.

The inventory's parsed object-valued selected population is 37 records:
claim 1, CQ 2, card 31, run 3. For **each** child field, 12 records have
actor parent absent, four templates have actor object/child null, and 21
generated cards have a populated string. All 21 populated cards record
`mode: agent-direct` and `role: extractor`: four Arc07 pilot, seven rich
rerun and ten teaching rerun. The absent parents are six synthetic and six
Arc07 expanded records. No populated claim, standalone CQ or extraction-run
actor occurs in this selected population. Three rich-rerun YAML errors are
excluded from parsed records, separately from 15 no-frontmatter files.
The 2,054 parsed untyped legacy records have no actor parent; nested children
are not applicable, not null. These are population observations, not a
complete actor vocabulary or requiredness rule.

CRC read all four current templates with their body instructions and inspected
synthetic CQ/run examples plus populated pilot, rich and teaching card bodies
and one expanded absent-parent card. Source anchors:

| Witness/guidance | Observed consequence for this slice |
| --- | --- |
| Source `knowledge/concept-cards/templates/{claim,competency-question,concept-card,extraction-run}.md`, full files at source HEAD above | Four actor objects expose null `id`, `role`, `mode`; root record identity, CQ `roles`, run scope, support and lifecycle fields are distinct. |
| Source `knowledge/concept-cards/guides/01-load-contract.md`, `Operating Modes And Availability`; `guides/02-operator-workflow.md`, `Record Scope Before Deriving Content`; `guides/03-extraction.md`, `Establish The Extraction Run`; `guides/06-graph-cq.md`, `Establish A Competency Question`; `references/record-field-groups.md` | Human-assisted/agent-direct are workflow descriptions; CQ roles describe question use; worker roles describe assigned work; none automatically defines the actor.mode/role field contract or identity authority. |
| Planning Arc07 pilot `cc-pattern-separation.md`; source rich `cc-pattern-separation.md` and teaching `cc-memory-forms.md` at their inventoried hashes | Populated actor mapping is on the card revision; its `extractor` label does not populate claim, CQ or run actors or prove source authorship/verification. |
| Planning Arc07 expanded `cc-memory-forms.md`; source synthetic `cq-coverage.md` and `extraction-run-trace.md` | Parent absence is real and cannot be normalized to the template's child null. `worker_scope.mode` is not a populated `actor.mode`. |

Detailed inventory queries, semantic interpretation and falsifying controls
are supplied in `cc-prompt.md`; this reconnaissance is CRC preparation, not
CC evidence or independent acceptance of the eight pairs. The only material
unknown is the exact event/class, vocabulary and cross-record applicability
of a future populated mode/role outside concept cards; CC must record that
unknown rather than choose a policy. If native evidence changes materially,
CRC returns to CDC before altering this approved scope.

## CC Output And Verification

CC may edit exactly six files in this slice: `artifacts/semantic-membership.json`,
`artifacts/semantic-evidence.md`, `artifacts/validation-evidence.md`,
`artifacts/handoff.md`, `ledger.md`, and `closing-report.md`. The default
durable artifact home is this slice's `artifacts/`. No source implementation,
schema, helper/parser, runtime, package, extraction or memory work is in scope.

The ledger's six rows require exact scope/ownership, native census and legacy
comparison, per-member meaning and consequences, native diagnostics with
wrong-value/state and real-error controls, pinned reproducible evidence, and
complete downstream handoff. CC records proposed-done only; CRC independently
replays and verifies before moving any pair to accepted coverage. A reviewer
who authors an implementation repair needs another verifier.

## Prompt Author Readiness

- **Source-grounded:** inspected four templates, relevant guide sections and
  representative synthetic/generated bodies; compared frozen inventory and
  current coverage by direct lookup. The input hashes and counts above are
  CRC's reproducible opening checks, not CC results.
- **Design-complete:** eight pairs and their outside owners are fixed by CDC;
  meanings are bounded to observed record-local contexts. No schema,
  requiredness, role vocabulary or global principal is chosen by this prompt.
- **Guideline-applied:** operator workflow and extraction guidance keep actor
  versus run/source distinct; CQ guidance keeps `roles` versus actor.role
  distinct; validation/testing guidance drives observed-value controls.
- **Executable:** `cc-prompt.md` gives exact six output paths, registry shape,
  Bash/jq query sketches, reading manifest, sequence and commit/replay route.
- **Falsifiable:** the prompt predeclares 37/12/4/21, 2,054 and parse-exclusion
  oracles and controls that fail on wrong mode, wrong role, child swap,
  absence-as-null, dangling evidence and missing-input-as-no-match.
- **Coherent/portable:** active prompt/plan/ledger and directive are separately
  identified; CC's bounded reading manifest leaves implementation/recovery
  headroom. No historical recipe is current authority. This is author
  self-review, not independent acceptance.

## Version History

- 1.0 (2026-09-17): CRC opens the CDC-approved eight-pair actor mode/role
  unit after direct recount and witness inspection. Slice16/17 and all
  outside obligations remain owned; no pair is accepted by opening.
