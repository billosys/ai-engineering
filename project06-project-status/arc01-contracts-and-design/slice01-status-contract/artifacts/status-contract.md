# Proposed status data contract

Operator review update, 2026-09-10: CDC recommendations for Q-01, Q-02, Q-04,
Q-05 and Q-06 are accepted as recorded in the
[project plan](../../../project-plan.md). Q-03 is now settled by the
[operator's hierarchical progress correction](progress-decision.md): project
progress weights planned arcs equally and incorporates their fractions. The
slice-only project ratio in section 5 and Q-03 below is superseded and awaits
revision; R-01 also still requires a contract correction. The
draft-1 field specification below is retained unchanged for that discussion;
earlier blanket pending-approval wording is superseded by this dated update.

Date: 2026-09-06. Revision: draft 1. Author: CC (Sofie).
Status: proposed for coordinating contributor/operator review; no schema,
validator, renderer, migration, or consumer acceptance is implemented here.

Authority: [project plan](../../../project-plan.md), [slice plan](../slice-plan.md),
[seed brief](design-brief.md), and [source reconnaissance](source-reconnaissance.md).
[Contract cases](contract-cases.md) make the rules below falsifiable.
[Verification record](verification-record.md) records the inspected revisions,
working-tree qualifications, author checks, and their limits.

## 1. Decision boundary

The following decisions are already accepted and are preserved, not reopened:

| Decision | Contract consequence |
| --- | --- |
| Saga is every project in one repository | Collection document kind is `collection`; page heading is “Saga View”; files are `status.json`, `status.html`, `schemas/status.schema.json`. No `saga` key or saga plan/ledger/closure family. |
| Lower scales retain their identities | `project-status.*` and `arc-status.*`; project IDs are independent of release metadata; arc IDs are opaque, including decimal suffixes. |
| Consumers own coherent toolkit snapshots | Schema files, scripts, templates, dependency declarations and provenance move together through explicit adoption/upgrade. No installed-skill runtime lookup. |
| Status is a view of planning/evidence | Authored reports, mechanical derivation, evidence strength and acceptance remain distinguishable. Schema validity never establishes world truth. |
| Preserve useful Rootstock views | Saga overview, Frontier, Instrument, Spine, arc detail, gates, evidence indicators, themes and navigation survive with truthful field sources. |
| Lykn is the first consumer | Six observed project shapes constrain the draft; adoption refreshes the census and incorporates UAT before project closure. |

Everything else below is a **recommended proposal**, including field spellings,
enums, ownership rules, diagnostics and optional capability disposition. “Must”
and “error” describe how this candidate contract would behave if accepted; they
do not record operator approval. Section 11 lists decisions and alternatives.
The schema dialect, runtime, exact command interface, packaging and UAT protocol
remain Slice02 work. No design brief or parent plan was silently amended.

## 2. Documents, identity and ownership

A selected status tree can contain only a collection page, project pages without
a collection page, arc pages without their parent page, or a mixed tree. The
canonical paths, relative to the selected root, are:

| Kind | Input | Output | Entity |
| --- | --- | --- | --- |
| `collection` | `status.json` | `status.html` | Repository collection; children are projects |
| `project` | `<project-id>/project-status.json` | same directory, `project-status.html` | Project; children are arcs and/or direct slices |
| `arc` | `<project-id>/<arc-id>/arc-status.json` | same directory, `arc-status.html` | Arc; children are slices |

There is no slice status file: slices are inline records owned by their immediate
project or arc. A collection may inline a project with its child records if no
project page is adopted. Direct slices never require manufactured arcs.

IDs are nonempty, case-sensitive ASCII strings matching
`[A-Za-z0-9][A-Za-z0-9._-]*`, excluding `.` and `..`. This is an identity/path
safety rule, not a numeric parser. Identity keys are qualified by repository,
project and immediate ancestry: `example/project01-catalog/arc16.1-index` and
`example/project01-catalog/slice01-discovery` are distinct. Sibling IDs must be
unique even across different kinds. Decimal arc IDs retain their literal bytes.
Array order is editorial display order, never proof of dependency/chronology.

### Common document envelope

R = required; O = optional. Null is permitted only where explicitly stated.
Strings are plain text, nonempty unless a field explicitly permits an empty
array/object. Unknown keys are errors outside `extensions`.

| Field | Type / presence | Meaning and validation |
| --- | --- | --- |
| `$schema` | string, R | Document-relative path to the corresponding vendored schema, e.g. `../schemas/project-status.schema.json`. Must resolve inside this tree's `schemas/`; never fetched. |
| `format_version` | string, R | Candidate format version `1.0.0`; independent of skill metadata and source revision. All documents in one tree use the same supported version. |
| `kind` | enum above, R | Must agree with filename, path depth, schema and entity kind. |
| `repository` | object, R | `id` (stable ID, R), `name` (text, R), `url` (HTTPS URL, O). Same identity/name/URL throughout a tree. |
| `as_of` | timestamp or null, R | Time the author assessed this document's status inputs. Null means unknown, visibly so. No default to current time. |
| `sources` | Source[], R | Document-local reference registry; may be empty for explicitly unassessed records. IDs unique within this document. |
| `evidence` | Evidence[], R | Document-local claim registry; may be empty. IDs unique within this document. |
| `entity` | Entity, R | Own record for this document. Collection entity ID equals repository ID. |
| `extensions` | object, O | Namespaced keys, e.g. `example.org/notes`; JSON values retained. Cannot alter core semantics or inject HTML. Unsupported extension keys produce a visible diagnostic; never silently disappear. |

Timestamps are UTC strings `YYYY-MM-DDTHH:MM:SSZ` (calendar-valid, no fractional
seconds in draft 1). This document deliberately does not choose a JSON Schema
dialect. Dialect declaration belongs to schema files, not to status timestamps
or the instance's format-version string.

### Entity and child entries

| Field | Type / presence | Meaning and validation |
| --- | --- | --- |
| `id`, `kind`, `title` | strings, R | Kind is `collection`, `project`, `arc` or `slice`. Title is reader-facing; no inferred release number. |
| `parent` | EntityKey or null, R | Null for collection; repository key for project; project key for arc; immediate project/arc key for slice. A key does not require a parent page. |
| `description` | text, R | Purpose/capability; plain text, rendered without executing markup. |
| `source_refs` | source ID[], R | Exact local registry pointers supporting this record; empty means unassessed provenance and generates a warning. |
| `state` | State, R except collection | Lifecycle, delivery, closure and acceptance as defined in section 3. Forbidden on collection: there is no repository-wide completion judgment. |
| `children` | Children, R except slice | Registry of known immediate child units. Forbidden on slice. |
| `progress` | Progress, O, forbidden on slice | Slice-delivery counts; absent means no count assessment supplied, never zero. |
| `depends_on` | Dependency[], O | Absent means dependency assessment unknown; `[]` means explicitly none reported. Required for a computed Frontier eligibility result. |
| `related` | Target[], O | Nonblocking relationships. Reverse `blocks` is derived from local dependency edges; external outcomes use related links with a label, not inferred blockers. |
| `phase` | text, O | Authored grouping for project views; no order or completion implication. |
| `origin` | text, O | Retrospective wrapper, historical grouping, research seed, etc.; always visible with the record. |
| `planned_release` | text or null, O, project only | Absent: not supplied; null: explicitly no assigned release; text: reported target. Shared values do not merge projects. |
| `release_note` | text, O, project only | Qualification of release metadata. |
| `gates` | Gate[], O | Named current-scale checks; absent means unassessed; empty means explicitly no named gates recorded. |
| `findings` | Findings, O | Assessed findings collection, section 6. |
| `checks` | Check[], O | Scoped observations such as drift or reconciliation; no unconditional green defaults. |
| `next_actions` | Action[], O | Authored priorities with explanation; never labeled computed readiness. |
| `links` | Link[], O | Optional adjacent material, including lessons or a port/reconciliation ledger. |
| `metadata` | `{label: text, value: text}[]`, O | Display-only ancillary facts; cannot substitute for core counts/states/relationships. |

EntityKey has required `repository` (ID), `project` (ID or null), `arc` (ID or
null), `slice` (ID or null). A collection key has the last three null; project
has only project set; arc has project and arc set; slice has project and slice
set, optionally arc. A key cannot skip project. Keys use IDs, not paths.

Children has required `coverage` (`complete`, `partial`, `unknown`), `scope`
(text explaining the population at `as_of`), `source_refs` (source ID[]), and
`items` (ChildEntry[]). `complete` asserts a complete inventory of current
planned immediate units for that scope; it is not a claim that all future work
is planned. `partial` and `unknown` require a nonempty `note`; `note` is optional
otherwise. An empty array with unknown coverage does not mean no work exists.
Scope text cannot turn a filtered selection into “all projects.”

ChildEntry has required `id`, `kind`, `detail` (status-root-relative JSON path or
null). Exactly one mode applies:

- With non-null `detail`, it has no `record`. The referenced document owns all
  facts. Hydration reads its entity; identity, kind, parent and repository must
  match. Missing/invalid detail is an error, not optional detail.
- With `detail: null`, `record` is required and is a complete inline Entity.
  Entry ID/kind must equal record ID/kind. No page is promised or linked. This
  includes slices and summary-only projects/arcs. Inline records use the owning
  document's sources/evidence, including any nested inline descendants.

There is one authored Entity per qualified key across the tree. A detail entry
is a reference, not a second entity definition. Defining an inline record and
also a document for that entity is a duplicate error. If a parent page is
absent, a standalone child document remains valid; if the parent exists it must
list the child by detail reference. This prevents invisible orphan detail pages.
No parent snapshots duplicate titles, states or counts from detail documents.
The cost is that a referenced child document is needed to render its parent.

## 3. State, closure and acceptance

State has these required fields; collection entities omit State altogether.

| Field | Type / values | Meaning |
| --- | --- | --- |
| `lifecycle` | `planned`, `research`, `active`, `blocked`, `paused`, `closed`, `archived`, `unknown` | Reported working disposition. Archived describes retention, not successful delivery. |
| `delivery` | `not-started`, `in-progress`, `complete`, `unknown` | Author's capability-delivery assessment. `complete` requires an own-subject delivery claim of at least attested strength, but does not imply verification or acceptance. |
| `closure` | `unassessed`, `open`, `proposed`, `verified`, `deferred`, `not-applicable` | Current-scale ledger/composition disposition. |
| `acceptance` | `unassessed`, `pending`, `accepted`, `rejected`, `not-required` | Operator/domain acceptance judgment, independent of mechanical verification. |
| `reported_label` | text | Original source status wording, preserving distinctions not captured by enums. |
| `note` | text | Rationale, uncertainty, scope qualifications; required even when concise. |
| `evidence_refs` | evidence ID[] | Evidence for the state, qualified by each claim's subject and scope. |
| `criteria` | Criterion[] | Current-scale closure rows; may be empty while unassessed/open. |
| `criteria_coverage` | `complete`, `partial`, `unknown` | Completeness of current-scale closure requirements. |
| `deferral` | Deferral, conditional | Required exactly when closure is `deferred`. |

Criterion requires `id`, `text`, `disposition` (`open`, `done`, `deferred`,
`no-op`), and `evidence_refs`. `rationale` is required for deferred/no-op and
optional otherwise. `deferral` is required exactly for deferred criteria.
Criterion IDs are unique within their entity.

Deferral requires `reason`, `destination` (Target), `reentry` (text) and
`evidence_refs` (nonempty evidence ID[] documenting the decision). Deferring
work is not completion. Accepted exclusions can discharge a closure criterion,
but cannot count as delivered slices.

Rules:

1. `proposed` closure requires own-scale evidence and at least one criterion;
   it displays “proposed-done,” even with `delivery: complete`.
2. `verified` requires nonempty complete criteria, no open criterion, and
   reproduced/reconciled evidence for every done row at this entity's scale.
   Deferred/no-op rows require a decision claim at that scale with at least
   reproduced strength and checkable rationale; deferred rows also need their
   destination/re-entry. State evidence must include own-scale composition
   evidence (or slice verification for slices). Child evidence alone is invalid.
3. `accepted` requires an explicit operator/authorized reviewer acceptance
   claim for this entity. `not-required` requires a scoped decision claim;
   absence of a gate is not that decision. These claims have a named actor,
   pointer and assessment time; their minimum strength is `attested` because
   this is a reported judgment, not automatic independent reproduction.
4. `lifecycle: closed` requires `closure: verified` and acceptance `accepted`
   or `not-required`. Historical “closed” without accessible proof is preserved
   as `reported_label`, with lifecycle `archived` or `unknown`, never upgraded.
5. `delivery: complete` may coexist with acceptance pending/rejected or closure
   deferred. A project can be mechanically verified and await operator review.
   A closed unit may contain explicitly accepted deferred/no-op scope, so closed
   does not force every slice delivered. Conflicts must be explained in `note`.
6. No automatic mutation of State from children, gates, counts or rendering.
   A closed parent with an open child requires the parent's criteria/decision
   evidence to name that exclusion; otherwise consistency validation fails.

Evidence indicators are attached to named claims/criteria. No average or maximum
child evidence level becomes a parent evidence rating. A compact closure
indicator may show the weakest strength among the required own-scale claims,
with unknown/missing shown explicitly and labels available without color.

## 4. Sources, claims, and portable references

Source requires `id`, `kind`, `label`, `locator`. Optional `note` provides
qualification. Kinds and discriminated locator shapes are:

| Kind | Required locator fields | Meaning |
| --- | --- | --- |
| `planning` | `path` | POSIX path relative to the owning planning worktree root (parent of canonical `status/`); optional `fragment`. No absolute path or traversal. |
| `git` | `repository`, `revision`, `path` | Repository ID or HTTPS repository URL; immutable full commit ID; repo-relative path; optional `ref_hint` and `fragment`. Branch hint is not a revision. |
| `url` | `url` | HTTPS URL; optional `fragment`; no fetch needed for validation/render. |
| `snapshot` | `repository`, `base_revision`, `working_tree`, `observed_at`, `paths` | `working_tree` is `dirty` or `unknown`; `paths` is nonempty repo-relative path[]. Optional `digest` records an externally retained snapshot; absent digest means mutable/unpinned evidence. |

Git revision/base_revision strings must be full 40- or 64-character lowercase
hex commit IDs in this candidate format, never branch names. Snapshot
observed_at is a non-null timestamp. Repo-relative paths are nonempty normalized
POSIX paths without absolute prefixes, empty components, `.` or `..`.

Snapshot base revision does not claim edited bytes are committed. Hardware
measurement or operator-report evidence can point to a retained transcript
using any appropriate Source; its content never becomes an executable action.
Planning sources are portable within the consuming checkout. Git/URL sources
may refer to a release branch's pinned commit or another repository without
requiring that checkout on the renderer's host. Link accessibility is distinct
from evidence validity. A Git reference without a known HTTPS repository URL
remains a labeled repository/revision/path citation; do not invent a forge URL.
Source and evidence references used by state, gates, criteria, findings or checks
must match the owning entity subject; referenced claim scopes must support the
particular assertion. A link to child evidence alone cannot satisfy that rule. A missing local planning target is a warning with a
visible unavailable label; missing required status detail is an error.

Evidence fields (all required unless marked):

| Field | Type / validation |
| --- | --- |
| `id`, `label`, `claim` | IDs/text naming exactly what is supported. |
| `subject` | EntityKey; resolves to an entity in this tree. |
| `scope` | `source-observation`, `delivery`, `verification`, `composition`, `acceptance`, `decision`, `gate`, `finding`, `check`. |
| `kind` | `document-review`, `command-result`, `measurement`, `operator-report`, `review`, `integration`. Kind is not strength. |
| `strength` | `asserted`, `attested`, `reproduced`, `reconciled`, or null for unassessed. |
| `source_refs` | source ID[]; nonempty for any strength above asserted and for acceptance/decision claims. |
| `actor` | text; person/context that supplied the claim. |
| `observed_at` | timestamp or null; null explicitly unknown. |
| `review` | O; required for reproduced/reconciled: `actor`, `at` (timestamp), `method` (text), `source_refs` (nonempty source ID[]). Names independent reviewer/witness and reproduction route. |
| `reconciliation_refs` | O source ID[]; nonempty and required for reconciled, identifying the broader check. |
| `note` | O text; uncertainty, limits, conflicting reports, physical observation context. |

Reproduced/reconciled without a review is an error. The validator can check
that a declared independent review exists; it cannot prove actor independence
or truth. Dates are observations, not renderer freshness. `as_of` cannot
precede a non-null claim/review date referenced by that document. Conflicting
claims are preserved and explained; they do not automatically overwrite state.
All source/evidence IDs resolve within the owning document. Imported child
records retain their document context after hydration.

Target is exactly one of `{entity: EntityKey}` or `{source_ref: source ID}`.
Link requires `label`, `target` (Target), and `relation` (`planning`, `evidence`,
`lessons`, `port-ledger`, `related`). Relative generated HTML links are derived
from discovered detail documents, not stored in records. Source fragments are
text anchors, escaped during URL construction. Never accept `javascript:`,
`data:`, `file:`, shell commands as URLs, authored raw HTML, CSS classes or
pre-escaped text. Display text containing `<` or quotes remains literal text.
No validation/render step executes source contents, accesses hardware or needs
network access.

## 5. Counts, coverage and dependencies

Progress describes **slice delivery**, not effort, acceptance or verified
closure. It has required `mode` (`computed`, `reported`), `scope` (text), and
`coverage` (`complete`, `partial`, `unknown`). Reported mode additionally
requires `done`, `total` (each nonnegative integer or null), `source_refs`
(nonempty source ID[]), and `note` (text). Computed mode forbids those four
fields: values are derived and cannot drift as duplicated inputs.

Progress `scope` explains the population; it cannot override these counting
rules. Complete coverage always means all current descendant slices of this
entity. Partial coverage explicitly reports a subset and cannot be compared as
a complete roll-up.

The denominator is the number of planned leaf slices at `as_of`, including
retained deferred/no-op slices. The numerator counts slices with
`state.delivery == complete`, irrespective of acceptance; UI labels this
“slices reported delivered.” No-op/deferred disposition alone adds nothing to
the numerator. Unknown delivery is not silently treated as not delivered.

Computed mode requires complete children coverage along every included branch
and known delivery for every leaf slice; its own coverage must be `complete`.
Walk arcs plus direct slices exactly once; never add both an arc's total and its
expanded slices. A collection may compute slice delivery only if every project
qualifies. A research seed with a complete current inventory of zero slices
computes 0/0; show “no slices planned,” no percentage and no completed badge.

Reported mode is useful for archives or intentionally sparse detail. Partial
coverage counts a declared subset; unknown coverage means no assurance that
the reported population is exhaustive. When total is known, done must not
exceed it; if done or total is null there is no percentage. A known done count
with unknown total displays “N reported delivered; total unknown.” If both
numbers are known and total > 0, percentage is `100 * done / total`, rounded
to the nearest whole percent (half up) **for display only**, always with the
counts and coverage. Partial ratios say “of reported subset.” A displayed
rounded 100% never proves complete delivery or closure.

If a reported complete roll-up has complete, known descendant slice records,
compare the authored numbers against their sum; discrepancy is an error.
If descendants are incomplete, preserve reported counts with their source and
an “unreconciled with detail” warning. Even then, known delivered descendants
cannot exceed reported done, and known slice identities cannot exceed reported
total for the same scope. Reported subtree totals are not mixed with computed
leaf totals. Nonmatching scope requires an explicit separate display; it cannot
masquerade as a whole-project roll-up. In this draft there is one Progress per
entity: other metrics stay labeled metadata, never pooled.

Counts of projects/arcs by lifecycle, delivery, closure or acceptance may be
derived independently from a complete corresponding inventory. They must be
labeled by their actual predicate (“arcs mechanically verified,” for example).
No generic `landed`, `done`, `pct`, or “all clear” input is accepted. With partial
inventory, show known counts plus a coverage qualification, not an exhaustive
summary. Finding and gate counts have their own populations (section 6).

Dependency requires `target` (Target), `requires` (`delivered`, `verified`,
`accepted`), and `note` (text). Source targets additionally require `assessment`
(`satisfied`, `unsatisfied`, `unknown`) and `evidence_refs` (nonempty except
unknown). Local entity targets derive satisfaction from delivery complete,
closure verified, or acceptance accepted respectively; external assessments are
reported observations, visibly labeled. Duplicate edges, self-dependencies,
local dependency cycles and unresolved entity keys are errors. `related` edges
may cycle. An unmet dependency is valid blocked work, not a validation error.

Frontier eligibility is calculated only for lifecycle planned/research/active,
delivery not complete, explicit dependencies with all predicates satisfied.
Missing dependency assessment yields “readiness unknown”; unknown delivery also
yields unknown. Blocked/paused/closed/archived entities are not eligible.
This is **eligibility from declared data**, not proof of world-state readiness,
and never “refreshed on read.” The renderer may group editorial array order by
phase; it may not claim topological ordering unless Slice02 specifies and later
implementation actually provides that algorithm. Authored Action requires
`label`, `reason`, `target` (Target); it is shown separately from eligibility.

## 6. Named gates, findings and checks

Gate requires `id`, `label`, `state` (`pending`, `passed`, `failed`, `waived`,
`unknown`), and `evidence_refs`. Optional `note` is required for waived gates.
IDs are unique per entity. Passed/failed/waived require evidence for that entity
with scope gate or decision; passed/failed evidence must be at least attested.
A gate can be author-passed while closure remains proposed. Render one labeled
slot per item, with passed/failed/waived/pending/unknown visibly different.
Compute passed/total from the list; waived is separate, never a green pass.
An empty gate array has zero named checks, not “all gates passed.” Four and six
gates both work without clipping; no positional `gate_filled` is retained.

Findings has required `coverage` (`complete`, `partial`, `unknown`), `scope`
(text), and `items` (Finding[]). Finding requires `id`, `title`, `detail`,
`severity` (`serious`, `correctness-grade`, `polish`, `unclassified`),
`disposition` (`open`, `resolved`, `deferred`, `rejected`, `unassessed`), and
`evidence_refs`. Optional `rationale` is required for resolved/deferred/rejected;
`deferral` is required exactly for deferred. Resolved/rejected need decision or
finding evidence. Empty/absent findings cannot establish broad system health:
only an assessed complete empty set may say “no findings recorded in [scope].”
Finding IDs are unique per entity; all title/detail/severity/disposition text
must render, including long content. Counts are derived from the actual items
and shown with coverage. No template accepts alternate silent-loss field names.

Check requires `id`, `label`, `scope` (text), `result` (`pass`, `fail`, `unknown`),
`checked_at` (timestamp or null), and `evidence_refs`. Pass/fail requires a
non-null time and evidence with scope check. Unknown must not be rendered green.
“Drift checked” is a dated, scoped observation; no check object means unassessed.
A schema-validation result is explicitly about this dataset, never a whole
repository reconciliation claim. Check/gate IDs are unique within each list.

## 7. Discovery and validation outcomes

Discover every regular filename ending in `status.json` recursively within the
selected status root, including files not linked by a parent. Unknown names
(e.g. `slice-status.json`, `old-status.json`), wrong location/kind/version,
malformed JSON, duplicate object keys, unreadable files and duplicate IDs are
errors. Symlinked status files/directories are reported as unsupported errors,
not followed or silently skipped. Artifact/example files belong outside a
consumer's selected live tree. `lessons.json` is not a status input; extension
handling is explicit in section 10. Schema files end in `schema.json` and do
not collide with this discovery rule.

Then check envelopes, entity fields, local references, hierarchy/ownership,
dependencies/cycles, evidence prerequisites, dates and count invariants. A
selected-page render still validates the whole selected tree and hydrates its
dependencies; it cannot hide malformed sibling inputs. Validation never reads
Markdown as an executable instruction or decides whether a historical closure
actually occurred. Every error names file, JSON pointer or entity key, rule,
and repair direction. Stable diagnostic codes below are proposed fixture
labels, not an implemented CLI promise.

| Error family | Representative failure |
| --- | --- |
| `E-DOCUMENT` | Unsupported name/path/kind/schema/version; malformed JSON; duplicate object key; unreadable/symlinked status input |
| `E-FIELD` | Missing/unknown field; invalid type/null/enum/date |
| `E-IDENTITY` | Duplicate sibling/qualified entity ID; parent/key disagreement |
| `E-DETAIL` | Promised detail missing; inline/detail conflict; discovered child omitted by existing parent |
| `E-REFERENCE` | Dangling source/evidence/entity key; invalid path or URL |
| `E-CYCLE` | Local dependency or hierarchy cycle/self-edge |
| `E-EVIDENCE` | Unsupported closure/acceptance/gate/check or wrong subject/scale evidence |
| `E-PROGRESS` | Impossible numbers, false computed coverage, complete same-scope roll-up mismatch |

Errors fail validation and prevent rendering success. Warnings remain visible
in diagnostics and affected views: `W-COVERAGE`, `W-UNASSESSED`,
`W-UNRECONCILED`, `W-SOURCE-UNAVAILABLE`, `W-MUTABLE-SOURCE`, `W-EXTENSION`.
Warnings cannot waive any error. Exact command status codes, output channels,
freshness hashes, schema resolver and deterministic output protocol are Slice02.

## 8. Rootstock extraction map

Source provenance and reproducible read routes are in the verification record.
Only field vocabulary/behavior is retained here; no private payload, example
text, branch narrative or project data is copied. This mapping covers the union
of observed keys and the template-only expectations, including adjacent pages.

| Trial fields / behavior | Candidate disposition |
| --- | --- |
| `initiative.name/tagline/intro` | `repository.name`, collection title/description; tagline as optional metadata. Title includes Saga View. |
| `streams[].name/cap/status/href` | Project child identity/description/state and resolved detail reference. No hard-coded stream count. |
| `streams[].badge/branch/meta[].k/v` | Reported label, qualified source ref/ref_hint, optional metadata label/value. Private branch workflow prose retired. |
| Hub `summary.streams/shipped/restructure` | Derived project counts with named predicates; descriptive prose in collection description. No invented shipped count. |
| Hub `summary.queued/isolated`, `lane.ledger/buckets/groups/drain_note` | Domain-specific port lane; proposed optional external link, section 10. No generic closed-work meaning. |
| Lane bucket `cls/count/label`; group `count/desc/empty_msg/label/status/rows`; row `disp/disp_cls/dst/row/src/what` | Inventory retained as adjacent capability, not required core schema. Generic findings/links may refer to its decisions without importing row payloads or CSS. |
| `project.name/number/vision`, `arc.id/name/capability/number_note/origin` | Entity title/id/description/origin. Number is identity text or display metadata, never release/ordering logic. |
| `arcs[]` and `chunks[]` | Child entries; chunks that are actual slices become inline slice entities. Other chunk meanings require author classification, not automatic conversion. |
| Arc/chunk `status/status_label/item_cls` | Typed State plus original reported label. Drop item CSS class. |
| `arcs[].phase`, `phases[].key/title` | Entity phase label; renderer groups explicit labels in first-appearance order. Preserve phase descriptions in parent metadata if needed. |
| `arcs[].deps` | Typed dependencies; a prose string must be assessed, not parsed into guessed edges. |
| `arcs[].href`, `hub_ref/project_ref.href/name` | Detail reference and EntityKey; navigation/title derived from actual documents. Absent parent page remains supported. |
| `arcs[].close_note`, `chunks[].note` | State note and scoped closure criteria/evidence. |
| `arcs[].done/total/pct`, `summary.slices_done/slices_total`, `progress.done/total/pct` | Progress modes/coverage; derive pct; detect or qualify summary disagreement. |
| `summary.arcs_landed/arcs_total` | Derived named lifecycle/delivery/closure count, not ambiguous landed. |
| `progress.batch/remaining` | Description/next_actions/metadata; numeric remaining only when known total and done. |
| `arcs[].evidence`, `chunks[].evidence/evidence_label` | Named evidence strength + pointers. Integer pip level alone cannot establish reproduced evidence. |
| `gate_filled/gates_filled` | Named gates; array length supplies denominator. No assumed four/six stage progression. |
| `close.items[].label/done`, `close.note` | Criteria text/disposition/evidence plus State note. A Boolean true alone is not verified closure. |
| Findings `id/text/title/detail/label/severity/disp/disp_cls` | Single required title/detail/disposition contract. Preserve meaningful text; classify severity explicitly; strip styling. Missing/ambiguous mappings require author correction. |
| `summary.active/active_detail/blocked` | Derived lifecycle counts plus next_actions; unknown/partial inventory qualified. |
| `summary.drift/drift_detail/integrity_findings/last_checked` | Named dated checks and scoped findings; never unconditional green cards. |
| `ready[].id/name/why` | Authored next_actions or separately calculated declared-data eligibility, not unearned “topological sort.” |
| `lessons_ref`, `summary.lessons_count` | Optional lessons link; no core lesson count without a defined imported lesson collection. |
| `meta[].k/v`, `streams[].meta[].k/v` | Plain metadata label/value. Core semantic facts use typed fields. |
| `generated`, `css_href` | `as_of` for assessment only when source meaning warrants it; renderer provenance handled separately. CSS ownership in toolkit, not JSON. Never invent dates. |
| Lessons `project/project_ref`, `subtitle/through`, `lessons[].num/title/category/body`, `wins[].tag/text` | Adjacent lessons capability inventoried; optional link proposal below preserves access, not a promise to extract its template in core. |
| Hard-coded page manifest and silent missing-input skip | Full tree discovery, promised-detail errors, explicit absent-detail records. |
| Disabled escaping/default undefined fields, source-specific titles/theme key/fonts | Escaped text, missing-field failures, repository title, local theme/template policy; offline font behavior specified in Slice02. |

Additional live inspection found authored slice totals disagreeing with arc sums
in all three inspected project documents, not only the example in the seed.
This establishes ambiguity, not the correct count. The draft requires either
matching complete totals or explicit sparse/unknown coverage and provenance.

## 9. View-to-field contract

| View / element | Required source and behavior |
| --- | --- |
| Saga overview | Repository/collection title and description, ordered project entries, project State and optional release/progress. Always label partial collection coverage; no saga acceptance meter. |
| Frontier | Child identity/description, phase, lifecycle/delivery, dependency predicates, next_actions, scoped checks/findings. Distinguish authored priority, declared-data eligible, blocked and unknown. |
| Instrument | Same child records, Progress counts/coverage, named gates, own-scale evidence and acceptance. No four-gate clipping or default green health. |
| Spine | Every child row in editorial order, literal ID/origin, dependencies, status and available detail link; direct slices appear alongside arcs with kind labels. No rows silently dropped for phase absence. |
| Arc detail | Capability, parent navigation when available, ordered slices, own and slice gates/evidence, full findings title/detail/severity/disposition, criteria, notes and next actions. |
| Evidence indicators | Semantic strength plus accessible label, pointer, subject, observation/review date. Neutral evidence styling distinct from lifecycle color. |
| Gate display | Exactly one named marker per gate; unknown, failure and waiver differ from pass. |
| Release and archival annotations | Null target says no release assigned; absent target says not supplied; origin/reported label/coverage always reachable and never replaced by a percent. |
| Navigation/themes | Discovered relative HTML links only for pages that exist; source/adjacent links labeled separately; local shared templates own light/dark styling. |
| Freshness | Separate status assessment/evidence time from toolkit/render provenance; no “checked today” implied by generating HTML. |

Missing required display data fails validation. Optional absent content is
labeled unassessed or omitted according to its field meaning, not invented.
Static usable content, narrow-screen/dense/long-text behavior, accessible
labels, offline fonts and theme interaction remain renderer/UAT requirements
for Slice02 and later implementation. No browser acceptance occurred here.

## 10. Evolution, snapshots and adjacent capabilities

Propose one format version for shared definitions and the three schemas, with
major/minor/patch compatibility rules separate from all skill versions. A
consumer accepts only versions listed by its pinned toolkit, never guesses
compatibility from a major number. A newer optional-field addition increments
minor and may be rejected by an older strict reader; an incompatible meaning,
required field, enum interpretation or hierarchy change increments major.
Corrections that change no accepted data or meaning increment patch. Mixed
versions in one tree are rejected until an explicit all-document migration.

Each copied toolkit needs source repository/revision, copy date, file hashes,
dependency pins, supported format versions and documented local modifications.
The exact manifest filename/shape is Slice02, not an extra field in every status
record or a second skill-version authority. The validator resolves shared
schemas locally from this coherent copy. Changing the installed skill cannot
change an old consumer's schema, dependencies, renderer or output.

Upgrade owner is the consumer maintainer: preserve old snapshot; inspect local
changes; review schema/data migration; migrate every affected document; validate,
render and inspect output; run acceptance tests; record provenance and explicitly
accept. Unsupported input fails with a migration diagnostic; no automatic fetch,
implicit data rewrite, or silent fallback. A rollback restores toolkit **and**
compatible data/generated outputs. Private imports require a reviewed mapping;
no guessed evidence levels or status upgrades.

**Port lane proposal (Q-05):** core supports a typed link to a separately owned
port/reconciliation ledger. Do not extract its special buckets/branch operations
as mandatory Saga fields. Alternative: a separately versioned optional extension
schema/template with explicit fixtures and UAT; this adds toolkit scope and must
be accepted/planned before claiming the original port view is delivered.

**Lessons proposal (Q-05):** retain a typed adjacent lessons link; standalone
lesson authoring/rendering is not required core status behavior. Alternative:
extract the lessons template/data contract as an optional module with independent
content and count validation. The source capability is inventoried above, not
silently discarded. Arc01 must record acceptance or amend scope for either
module; these proposals are not approved deferrals.

## 11. Review decisions and Slice02 handoff

| ID | Recommended choice | Alternative / tradeoff | Review boundary |
| --- | --- | --- | --- |
| Q-01 | Detail references or inline records, exactly one owner | Duplicated parent snapshots render alone but need freshness/equality rules for every summary field. References prevent contradictions but require referenced data when rendering a parent. | Coordinating contributor/operator accepts ownership before schema implementation. |
| Q-02 | Typed State axes and strict evidence prerequisites for verified/closed | Free-form lifecycle only is easier to import but cannot distinguish mechanical success, history and operator acceptance reliably. Preserve original wording alongside typed values. | Accept vocabulary and historical closed-label treatment; do not re-adjudicate Lykn. |
| Q-03 | Slice delivery as the only built-in progress ratio; coverage and zero/unknown rules above | Weighted effort, ledger-row percentages or mixed arc/slice counts require additional denominators and author policy. Separate metrics may be a later accepted extension. | Accept count meaning and treatment of deferred/no-op slices. |
| Q-04 | Closed fields, uniform format version, local schema resolution; unknown extensions visible | Permissive keys ease imports but reproduce findings loss. Multiple format versions per tree increase migration complexity. | Accept compatibility policy here; Slice02 chooses dialect/runtime/resolver and provenance manifest. |
| Q-05 | Port lane and lessons as optional links in core | Optional full modules preserve additional views but need schema, rendering, packaging and UAT scope. | Arc01 disposition required; no silent removal/deferral or source copy. |
| Q-06 | Declared-data Frontier eligibility, explicit dependency predicates | Authored-only next actions avoid computation but lose useful frontier calculation; real source reconciliation is a separate, much larger feature. | Accept eligibility semantics; Slice02 defines actual algorithm/checks and truthful labels. |

Slice02 also specifies exact CLI diagnostics/freshness behavior, semantic schema
constraints vs cross-document checks, finite dependency/runtime policy, manifest
and upgrade workflow, package/source impact map, executable conversion of the
case matrix, complete view contracts and Lykn UAT intake/retest. These are the
already planned Slice02 responsibilities, not waived acceptance criteria here.

The reviewer can accept, amend or reject Q-01 through Q-06 against the worked
cases. Record the decision before implementing the toolkit. This draft contains
no commitment on their behalf and does not open the next slice.
