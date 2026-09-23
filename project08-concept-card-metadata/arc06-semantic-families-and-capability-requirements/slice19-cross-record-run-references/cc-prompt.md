# Project08 Arc06 Slice19: Cross-Record Run References

Work in the canonical planning checkout:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`.
The source checkout is `/Users/oubiwann/lab/billosys/ai-engineering`.

## Assignment And Authority

Produce an evidence-only semantic packet for **exactly 19 Set C pairs**. This
slice asks what `run_refs` means in each observed record kind, what each
element identifies, and which targets can actually be resolved. It does not
design or implement the future schema.

The Operator selected the Three-Contributor Workflow (CDC + CRC + CC) and
Expedited Mode. CDC's preserved `cdc-directive02.md` approves exact Set C as
Slice19 after Slice18 acceptance and fresh readiness. CRC has independently
accepted Slice18 and opened this assignment. You are CC. Your output is
proposed-done until CRC independently reviews it; CDC retains arc/project
composition and design-change authority.

Binding baseline at prompt authoring:

- source: `a5861c4b8e93af932d18cb571415cc570c758240`, clean;
- pre-opening planning: `5e6310b8`, clean;
- Set authority: `dee3052c88e0fd9361e74200fd1eea26ade76435`;
- Slice18 final candidate: `981ef9ff29ef390e186ae782555d0fcb4d9276ed`;
- Slice18 recipe: `2ab6679718326fc76ecf2e10d3678f385f086eb0`;
- frozen inventory SHA-256:
  `afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.

Recheck current heads and dirty state before work. Source movement is allowed
only when every relevant pinned input remains byte-identical or the difference
is explicitly reconciled. Stop on material drift; do not silently repin.

## Binding Scope

The exact assigned pairs are:

~~~json
[
  ["run_refs","claim"],
  ["run_refs","competency-question"],
  ["run_refs","concept-card"],
  ["run_refs","memory-admission"],
  ["run_refs","preservation-decision"],
  ["run_refs","reconciliation-result"],
  ["run_refs","relationship-edge"],
  ["run_refs","source-locator"],
  ["run_refs","source-support"],
  ["run_refs","validation-result"],
  ["run_refs","verification-result"],
  ["run_refs[]","concept-card"],
  ["run_refs[]","source-support"],
  ["run_refs[].id","concept-card"],
  ["run_refs[].id","source-support"],
  ["run_refs[].path","concept-card"],
  ["run_refs[].path","source-support"],
  ["run_refs[].revision","concept-card"],
  ["run_refs[].revision","source-support"]
]
~~~

Opening accounting is 555 full / 260 independently accepted / 295 remaining /
19 assigned / 276 outside. Assignment is not acceptance. Do not add a prefix-
matched field, infer an omitted child for the other nine kinds, or absorb any
Slice20/21 or 248-pair later-family member.

## Required Reading And Execution Preflight

Record a categorized intake/readback in `artifacts/semantic-evidence.md` before
dependent drafting. A filename without a bounded section means read the entire
file. Recover any truncated read with contiguous reads and record the recovery.

### Required-full

Read these complete:

1. this prompt, `slice-plan.md`, and `ledger.md`;
2. `../cdc-directive02.md` and `../crc-escalation02.md`;
3. `project08-concept-card-metadata/AGENTS.md`;
4. all eleven source templates at source `a5861c4b`:
   `claim.md`, `competency-question.md`, `concept-card.md`,
   `memory-admission.md`, `preservation-decision.md`,
   `reconciliation-result.md`, `relationship-edge.md`, `source-locator.md`,
   `source-support.md`, `validation-result.md`, `verification-result.md`;
5. `knowledge/concept-cards/examples/rich-profile-card.md`;
6. Slice18 `artifacts/handoff.md` and `crc-verification.md`;
7. Slice03 `artifacts/evidence-replay-contract.md` and
   `artifacts/worked-replay.md`;
8. both preserved baseline README files under Arc01 Slice01
   `artifacts/baseline-snapshots/`;
9. the Arc07 pilot extraction run at planning `5e6310b8`:
   `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/`
   `slice02-pilot-markdown-preparation-and-card-extraction/artifacts/`
   `extraction-run.md`.

Read representative populated records completely, not only frontmatter:

- all four Arc07 Slice02 candidate cards and four source-support records;
- `knowledge/concept-cards/examples/rich-profile-card.md`;
- at least one byte-preserved rich-rerun and one teaching-rerun card whose
  `run_refs` points to the sibling README.

The required-data whole-population projection below covers every other card;
these full reads supply body/context evidence without requiring 31 repeated
teaching bodies.

### Required-section

Read the complete named sections and their definitions at source `a5861c4b`:

- `knowledge/concept-cards/SKILL.md`: record templates, representative examples,
  and the record/operation boundaries surrounding them;
- `guides/01-load-contract.md`: construct boundaries and false upgrades;
- `guides/02-operator-workflow.md`: scope, provenance and lifecycle handoff;
- `guides/03-extraction.md`: establish run provenance, output provenance and
  locator/support separation;
- `guides/04-re-extraction-preservation.md`: inventory/run identity and
  preservation handoff;
- `guides/05-evidence-lifecycle.md`: assertion support versus run history;
- `guides/06-graph-cq.md`: relationship/CQ provenance and warrant boundaries;
- `guides/07-reconciliation.md`, `08-validation-verification.md`, and
  `09-memory-admission.md`: result/decision actors, targets, evidence, scope,
  outcome and authority boundaries;
- `references/record-field-groups.md`,
  `references/semantic-audit-boundaries.md`, and
  `references/structural-validation-candidates.md`: reference shape and what
  path/target checks cannot prove;
- Project08 `project-plan.md`: Current Direction, Schema And Specification
  Discussion Gate, Arc Roadmap and Definition Of Done;
- Arc06 `arc-plan.md`: Current Review, Family Method, Slice Roadmap and Scope.

### Required-data

At the opening planning commit, query the complete frozen inventory and retain
commands, exits, denominators, exclusions and complete outputs (or lossless
partitions) for:

1. exact Set C derivation from escalation block index 2;
2. inclusion in the 295 remaining pairs, disjointness from 260 accepted,
   19 unique assigned and 276 outside;
3. all parsed records of the eleven assigned kinds, grouped by kind with total,
   root absent/present, and present value shape;
4. a record-level projection of path, kind, `run_refs` state and complete value;
5. every concept-card/source-support element and each `id`, `path`, `revision`
   child, preserving missing/non-object/wrong-type states;
6. the three YAML errors and fifteen no-opening-frontmatter records as
   exclusions, not absent fields;
7. the 2,054 Complete Musician/Erlang records and root-presence count for
   `run_refs`;
8. all four unique populated reference tuples and their source-record counts.

Expected baseline observations are tests to reproduce, not conclusions to
force: 49 parsed selected records across eleven kinds; populated references
only in concept-card and source-support; four unique tuples; three YAML errors;
fifteen no-frontmatter rows; and zero historical `run_refs` roots. Report any
discrepancy and stop if it changes scope or evidence sufficiency.

### Conditional And Reference-only

- **Conditional:** load prior semantic-family packets only when reusing a
  specific accepted interpretation; cite exact member/applicability and retain
  its limits. Similar field spelling is not enough.
- **Conditional:** inspect additional preserved rerun cards when the whole-set
  projection exposes a shape/value not represented by required full witnesses.
- **Reference-only:** historical v3.2 prompts may explain older process intent,
  but they are not current `run_refs` authority and are not required unless a
  current claim depends on them.

## Engineering Decisions

These decisions are binding for this evidence assignment:

1. A root `run_refs` membership is interpreted in its containing record kind.
   The same spelling does not establish identical purpose, requiredness or
   lifecycle authority across user-authored, trace, result and decision records.
2. Root state, sequence state, element shape and child state are separate.
   Preserve absent, empty sequence, populated sequence, non-object element,
   missing child, null and wrong-type values.
3. Resolve a recorded path relative to the containing record's directory in
   its authoritative evidence tree. For preserved workbench cards, use the
   matching baseline-snapshot tree, not mutable ignored workbench bytes.
4. Path resolution and target identity resolution are separate predicates.
   An existing README without frontmatter is not an extraction-run identity
   match. A missing path is not successful no-match of an inspected target.
5. Exact identity requires target `record_type: extraction-run`, matching id
   and matching revision. The current references do not carry `record_type`, so
   target kind comes only from an inspected target declaration, never the field
   name or filename.
6. A run reference links provenance. It does not transfer actor, source scope,
   method, support, evidence grade, validation, verification, reconciliation,
   preservation, admission, runtime state or contributor authority.
7. Record observed contradictions and underspecification as bounded findings
   with a named owner. Do not repair source or choose a future schema here.

The target matrix to reproduce is:

| Reference tuple | Address result | Identity result |
| --- | --- | --- |
| Arc07 pilot | relative path resolves to frontmatter record | exact extraction-run id/revision match |
| Rich rerun | relative path resolves to preserved README | no declared target identity/revision; path-only |
| Teaching rerun | relative path resolves to preserved README | no declared target identity/revision; path-only |
| Synthetic field guide | relative target path absent | missing target; no identity comparison |

This table is an independently derived baseline oracle. If actual pinned bytes
disagree, report the discrepancy rather than editing evidence to fit it.

## Required Outputs

Create exactly these six files and no others:

~~~text
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/semantic-membership.json
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/semantic-evidence.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/validation-evidence.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/artifacts/handoff.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice19-cross-record-run-references/closing-report.md
~~~

Do not create `crc-verification.md`. Do not edit the prompt, plan, parent plans,
coverage register, source checkout, prior packets or baseline snapshots.

### `semantic-membership.json`

Follow the established Slice18 structure. Include:

- artifact kind and `cc-proposed-done` status;
- exact assignment and opening counts;
- exactly 19 unique membership objects and unique meaning IDs;
- for each member: field path, record kind, effective meaning, applicability,
  observed states, evidence IDs, exceptions, reader/extractor/query/migration
  consequences, owner-tagged unresolved questions and bounded disposition;
- an evidence registry binding every input to root, path, read mode, authority
  commit, SHA-256, role, member scope, validated source range, interpretation
  and limit.

Do not use a generic shared definition in place of kind-specific meaning. It is
valid for a template-only kind to conclude only that the field is an empty
provenance attachment surface whose precise use/requiredness is unresolved.

### `semantic-evidence.md`

Include:

- categorized required-reading readback and any truncation recovery;
- exact coverage and exclusion census;
- complete eleven-kind census and record-level root projection;
- complete populated element/child projection for concept-card/source-support;
- four-tuple frequency and target-outcome matrix;
- documented rule, observed value, author inference, conflict/unknown and
  unresolved-owner sections kept visibly separate;
- kind-specific operational consequences and historical comparison;
- explicit limits on target resolution, run provenance and authority.

### `validation-evidence.md`

Provide one literal Bash route and a separate committed-endpoint wrapper.
The route must read contribution bytes from `CC_COMMIT`, recipe bytes from
`REPLAY_COMMIT`, and authoritative evidence from each registry row. Reuse the
Slice18 pattern only after checking every predicate against this slice.

A suitable state projection has this binding behavior (names are illustrative):

~~~jq
def leaf:
  if . == null then {state:"null", value:null}
  elif type == "array" and length == 0 then {state:"empty-sequence", value:[]}
  elif type == "array" then {state:"populated-sequence", value:.}
  else {state:("populated-" + type), value:.}
  end;

# root: absent or leaf(value)
# root[]: parent absent, unexpected non-array, empty or populated sequence
# root[].child: preserve every index; non-object elements and absent children
# are explicit states, never flattened into one invented value.
~~~

Target resolution must use two independent checks:

~~~text
address_result = resolve reference.path against containing record authority/base
identity_result = only if target bytes declare frontmatter:
  target.record_type == "extraction-run"
  and target.id == reference.id
  and target.revision == reference.revision
~~~

For the Arc07 target, use its planning-authority path without pretending the
inventory's `.worktrees/planning/` prefix is a Git tree path. For reruns, bind
the preserved baseline card and README hashes and resolve inside that copied
tree. For the source example, bind the source commit and prove the referenced
relative path is absent at that authority. Do not use mutable filesystem
existence as the only oracle.

The committed wrapper must:

1. require nonempty `CC_COMMIT` and `REPLAY_COMMIT`;
2. validate both as commits;
3. extract exactly one nonempty literal route from the declared recipe bytes;
4. run `bash -n` before execution;
5. execute with explicit endpoints;
6. fail closed for missing/stale/foreign endpoints or missing route.

### `handoff.md`, ledger and closing report

Handoff records bounded findings, every unresolved owner, exact Slice20/21 and
248-pair remainder ownership, P-15, real extraction/UAT and Operator gates.
Walk all seven ledger rows with no silent drop. Inventory every supporting
artifact and compare scope-as-specified with scope-as-delivered. State failed,
blocked and unrun checks. CC may say proposed-done, never CRC/CDC accepted.

## Ordered Implementation Method

1. Recheck worktrees, authority commits and exact 19-pair set. Stop on material
   mismatch.
2. Complete and record required reading before semantic drafting.
3. Query the frozen inventory for the complete 49-record population and retain
   lossless outputs.
4. Build the root and element state projections independently of expected
   prose; compare them to the recorded matrix.
5. Inspect full templates and populated witnesses; write kind-specific meanings
   with evidence class and applicability labels.
6. Resolve the four unique target tuples against their correct authority/base;
   record address and identity results separately.
7. Register every cited input with authority/hash/range and verify all rows.
8. Implement the literal route and negative controls through the same positive
   predicates. Run precommit mode.
9. Write handoff, ledger walk and closing report; inspect exact path union and
   staged/unstaged state.
10. Commit only the six authorized files with explicit filenames. Add the
    distinct recipe endpoint only by another explicit-file commit if needed,
    then re-run the committed wrapper and record final endpoints/results in the
    authorized validation/close files.

## Diagnostics And Discriminating Oracles

The positive route must establish:

- exact 19-pair Set C and 260/295/19/276 opening accounting;
- 49 parsed selected records with exact per-kind denominators;
- exact root absent/empty/populated counts and all populated element values;
- three YAML errors and fifteen no-frontmatter exclusions;
- bounded 2,054-record historical root absence;
- four unique tuples with one exact identity match, two path-only/no-declared-
  identity outcomes and one missing target;
- all evidence hashes/ranges, protected inputs, exact six-file scope and clean
  worktrees.

Run these negative controls through the actual production predicates:

- change an empty template `run_refs` to absent and to null;
- change a populated array to a mapping and add a scalar array element;
- remove `id`, `path` and `revision` from separate populated elements;
- change child types (numeric id, list path, string revision);
- alter Arc07 id, revision and target kind independently;
- resolve Arc07 against a wrong containing-directory base;
- treat a README path as an identity match and require rejection;
- inject the expected id text into README body without frontmatter and require
  identity rejection;
- replace the missing synthetic target with an unrelated existing file and
  require identity rejection;
- collapse path-only, missing target and tool error into one result and require
  comparison failure;
- add one accepted or outside pair to the membership set;
- mutate one evidence authority, digest and range independently;
- query a nonexistent inventory path and invalid Git authority, preserving
  nonzero status and nonempty stderr separately from semantic no-match.

Do not hard-code a nonzero status unless the invoked tool contract guarantees
it; record actual statuses. A passing wrapper is structural evidence only.

Run at minimum: `jq empty`; full precommit route; same-endpoint and distinct-
endpoint committed replay; all controls; `git diff --check`;
`git diff --cached --check`; exact staged/unstaged/untracked path union; commit
trailer check; clean source/planning status. Source package gates are not a
substitute and are not required for this planning-only packet.

## Stop Conditions

Stop and return to CRC without reducing scope if:

- Set C, coverage, population or exclusion counts materially differ;
- an authoritative input is missing, altered or truncated without recovery;
- baseline snapshots cannot bind ignored workbench evidence durably;
- target outcomes cannot distinguish address, identity, no declaration,
  missing target and tool error;
- evidence contradicts accepted work or requires a normative policy;
- context pressure threatens complete reading, matrix construction or replay;
- any seventh path would need to change.

CRC escalates structural questions to CDC through the Operator. Do not continue
into Slice20.

## Commit And Return

Use explicit full filenames with `git add --` and `git commit --only --`. Never
use a directory, glob, `git add .`, `git commit -a`, or unrelated staged work.
Every assistant-authored commit includes exactly these trailers:

~~~text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
~~~

Return source/pre-opening/CC/recipe/final commits; exact six changed paths;
intake/readback pointer; set/population/exclusion/root-state counts; four target
outcomes; per-row attestation; precommit/committed exits and controls; every
failed or unrun check; deviations and unresolved questions; model/effort if
known, context recovery/compaction and correction categories. CRC verification,
CDC arc composition, P-15, UAT and Operator acceptance remain separate.
