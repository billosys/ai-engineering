# Project08 Arc06 Slice16: Supporting-Record Actor Mode And Role

You are CC in the Operator-selected Three-Contributor Workflow and Expedited
Mode. Execute the initial Slice16 assignment from the canonical planning
worktree and return a committed **proposed-done** evidence packet to CRC through
the Operator. This prompt's project-relative path is
`arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/cc-prompt.md`.
This is evidence-only semantic inventory, not source implementation, schema
adoption, runtime work or memory admission.

## Binding Contract And Opening State

Arc06 `cdc-directive01.md` approves exactly twelve field-path/kind pairs:
`actor.mode` and `actor.role` in memory-admission, preservation-decision,
relationship-edge, source-locator, source-support and validation-result.
The full ordered list is in this slice's `slice-plan.md`; derive the actual
set from that block, not from an improvised list. Slice15's eight other-kind
pairs were independently accepted at planning `a97ab97b` and must not be
reaccepted, reassigned or assumed equivalent. Opening live coverage is
555 full / 208 accepted / 347 remaining / twelve assigned / 335 outside.
Source baseline is `ce3f77103eff5e07b3533a03c65f158684fc1039`; frozen
inventory SHA-256 is `afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.
CRC's pre-opening recount in `slice-plan.md` is an oracle to challenge with
native inputs, not CC evidence. No source skill, record template, schema,
parser/helper, graph/runtime, package, workbench corpus or frozen inventory
edit is authorized. P-15 and all UAT/operator gates remain open. Slice17's
larger provenance work needs a separate CDC sizing decision.

**Binding semantic boundary:** preserve exact parent-absent, object/child-null,
and populated-string states by record kind, family and revision. `actor.mode`
is not `worker_scope.mode`; `actor.role` is not a CQ role, relationship
`endpoint_roles`, `validator_identity`, source author, admission
`decision_authority_ref`, or Operator acceptance. A repeated pilot label is
an observation, not a global vocabulary or authority equivalence. Distinguish
support-record actor from supported claim/card actors. Where only a template
slot exists, state the uncertainty; do not invent a populated record policy.

## Required Reading And CC Intake

Read in this order, with source root the main checkout and planning root
`.worktrees/planning`. `required-full` means the entire document, including
tables and code. Use bounded reads; recover any truncated range. The actual
checkout state wins over a historical commit label only after drift is
explicitly reconciled with CRC.

| Class | Exact material and extent | Why / when |
| --- | --- | --- |
| Required-full | This `cc-prompt.md`, this slice's `slice-plan.md` and `ledger.md`; Arc06 `cdc-directive01.md` | Current assignment, exact pair list, six rows and approved ownership; load before any edit. |
| Required-section | Project `project-plan.md`: `Current Direction: Semantic Families And Capabilities`, `Contributor Workflow`, P-15/schema gate and current roadmap; Arc06 `arc-plan.md`: `Current Review`, `Design Handoff History`, slice breakdown, `Version History`; project and arc ledgers: P-1/P-4/P-6/P-15 and A6-1/A6-3/A6-6/A6-7 | Parent authority, outside owners and non-adoption gates; load before deriving meanings. |
| Required-full | Project `artifacts/semantic-coverage-current.json`; Arc01 Slice01 `artifacts/frontmatter-inventory.json` as structured query input; Slice15 `artifacts/semantic-membership.json`, `artifacts/semantic-evidence.md`, `artifacts/handoff.md`, `crc-verification.md` | Exact live/frozen state and independently accepted comparison; query the large JSON without eliding required selected records, not by printing the entire inventory. |
| Required-full | Source templates `knowledge/concept-cards/templates/memory-admission.md`, `preservation-decision.md`, `relationship-edge.md`, `source-locator.md`, `source-support.md`, `validation-result.md`; source examples `knowledge/concept-cards/examples/memory-admission.md` and `relationship-edge.md`; planning Arc07 Slice02 `artifacts/candidate-cards/support-emergent-explanation.md`, `support-memory-consolidation.md`, `support-model-data-constraints.md`, `support-pattern-separation.md` under `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/` | Six reserved slots, two absent-parent witnesses and four populated supports; read bodies to distinguish what each actor can and cannot mean. |
| Required-section | Source `knowledge/concept-cards/references/record-field-groups.md` entire table and conventions; `guides/02-operator-workflow.md` sections `Record Scope Before Deriving Content`, `Maintain The Construct Boundaries`, `Keep Results Separate`; `guides/03-extraction.md` sections `Establish The Extraction Run`, `Capture Locators, Spans And Source Support`; `guides/04-re-extraction-preservation.md` section `Record Preservation Decisions`; `guides/05-evidence-lifecycle.md` sections `Identify The Subject And Its Evidence`, `Maintain Separate Lifecycle Records`; `guides/06-graph-cq.md` sections `Identify Endpoints And Meaning`, `Establish A Competency Question`; `guides/08-validation-verification.md` sections `Record Review Actors And Evidence Provenance`, `Perform Structural Validation`; `guides/09-memory-admission.md` sections `Establish The Admission Scope`, `Evaluate The Gate` | Applies kind-specific source guidance; load before writing member/shared meanings. |
| Required-section | Source `knowledge/testing/guides/01-testing-discipline.md` sections `Test Behavior And Contracts`, `Failure Triage`; `knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md` sections `Required reading and CC intake`, `Review readiness before issuing`; `knowledge/work-verification/guides/03-row-closure.md` reviewer/row protocol | Native negative tests, complete intake/readback, proposed-done row walk. |
| Conditional | Slice15 `artifacts/validation-evidence.md` complete `Literal route` and wrapper, triggered if reusing its replay/hashing/range mechanics; record whether reused | Reuse mechanics without copying Slice15 counts, endpoints, set or meanings. |

In `artifacts/validation-evidence.md`, record the actual source/planning HEADs,
status, required items and fully loaded extents, conditional trigger, and a
short source-cited readback connecting S16-1..S16-6 to the six record kinds,
native observations, controls, and no-schema/no-admission fence. File
existence, hashes or a prior session's read claim do not establish loading.
Stop and report a material missing/changed input before dependent work.

## Evidence Design And Recommended Sequence

The following is a worked route, not a substitute for checking the native
inputs. Local Bash/jq names may differ if the same observable contract holds.
Use the existing six-file Slice15 packet as a *mechanical* pattern, not a
semantic template. No Ruby, Python, Fennel or new helper/parser is authorized.

1. **Pin the exact assignment.** Extract the JSON list in `slice-plan.md`;
   compare it to `coverage.next_slice_pairs`, verify twelve unique pairs,
   subset of the 347 remaining, disjoint from 208 accepted, and full union
   equal to the frozen 555. Reject extra/missing pairs. Do not treat all 335
   outside pairs as Slice17's assignment.
2. **Derive the native census.** Query only parsed object-valued inventory
   records of the six selected kinds. Expected denominator: 12 records =
   memory-admission 2, preservation 1, edge 2, locator 1, support 5,
   validation 1. For each child field: two absent actor parents (synthetic
   admission and edge), six template actor objects with null children, four
   Arc07 pilot support objects with `id=codex-cc`, `mode=agent-direct`,
   `role=extractor`. Confirm the four support paths and exact values directly.
   Separately derive all three YAML::XS error paths, 15 no-frontmatter records
   and 2,054 parsed untyped legacy mappings with absent actor parents.
3. **Interpret each pair.** Create twelve registry memberships and twelve
   field/kind meanings. For every member include definition, applicability,
   observed state, evidence IDs, exceptions, reader/extractor/query/migration
   consequences and unresolved questions. One shared rule may describe
   a genuine cross-kind pattern only with explicit applicable kinds, member
   roles and exceptions. Do not generalize support `extractor` to admission,
   preservation, edge, locator or validation actors. Compare Slice15's card
   observation and its unresolved mode/role questions explicitly.
4. **Register evidence in two layers.** Each member cites concrete native
   template/example/pilot witnesses and governing source guidance, with
   root, path, read mode, authority commit, SHA-256, role and source range.
   The shared semantic report explains why each record-local distinction
   matters and where evidence is silent. Hashes and ranges establish
   retrievability, not semantic warrant. Use snapshots for committed inputs,
   explicit `live` only for ignored workbench if any is actually needed.
5. **Build the literal replay before claiming done.** Derive census and
   exclusion sets from the frozen inventory; compare them to authored
   registry values. Validate exact membership/meaning/evidence references,
   every registered hash and numeric range at its authority, current relevant
   source bytes, protected planning files, six-file changed-path fence and
   whitespace. The precommit route may read the working registry; committed
   mode must load registry from `CC_COMMIT` and execute recipe bytes extracted
   from `REPLAY_COMMIT`. Fail closed on absent/invalid endpoints. Keep
   source-wide unrelated HEAD movement separate from relevant-byte drift.
6. **Write handoff and closeout.** `artifacts/handoff.md` compares the four
   Slice15 kinds with these six, states per-kind unknowns, and returns Slice17
   run/preparation/method/shared-reference/CQ questions to CDC sizing. Walk
   S16-1..S16-6 in `closing-report.md`; inventory artifacts and bubble up to
   Arc06 with specified-versus-delivered scope. Do not write a CRC verdict.

Representative structured query shape, to be adapted and exercised against
the actual frozen inventory (not pre-tested drop-in code):

~~~bash
kinds='["memory-admission","preservation-decision","relationship-edge","source-locator","source-support","validation-result"]'
jq --argjson kinds "$kinds" '
  [.records[] | select(.frontmatter == true and (.values|type)=="object")
    | select(.record_kind as $k | $kinds|index($k))
    | {path,kind:.record_kind,actor_state:(
        if (.values|has("actor")|not) then "parent-absent"
        elif .values.actor==null then "parent-null"
        elif (.values.actor|type)!="object" then "unexpected"
        else "object" end),actor:(.values.actor // null)}]
' "$inventory"
~~~

The sketch's `actor` projection is **not** the state oracle: JSON `// null`
collapses absent and null there, so compute and compare child presence/type
separately before counting. For positive controls, read actual pilot support
`actor` from the inventory by exact path and compare to an independent literal
expected object with `jq -n -e --argjson actual ... --argjson expected ...`.
Mutate the observed object's mode to `human-assisted`, role to `validator`,
swap them, and show the **same** comparison rejects each. Select an absent
synthetic actor parent with `has("actor")|not`; mutate that record to
`actor: null` and show the same absence predicate rejects it. Reject an
attempt to treat a populated support actor as the actor of its `subject_ref`.
Run a real absent-path lookup returning `[]`/0 and a real missing inventory
path returning nonzero; do not use an invented wrapper error as a substitute.

## Test Oracles And Required Gates

| Row | Positive result | Required negative or limitation |
| --- | --- | --- |
| S16-1 | Exact twelve, 208/347/12/335, no accepted overlap, 555 unique union | Extra pair, duplicate or Slice15 double count rejects. |
| S16-2 | 12 by 2/1/2/1/5/1, parent 2 absent/6 null/4 populated; exact errors 3, no-frontmatter 15, legacy 2,054 | Wrong three-path YAML exclusion rejects; malformed is not an absent actor. |
| S16-3 | Twelve evidence-backed meanings with kind-specific consequences and explicit Slice15 comparison | Decision authority, endpoint role, validator or source author cannot silently become actor role. |
| S16-4 | Native support positive; wrong mode, wrong role, child swap, absence-as-null and support-to-claim propagation reject; no-match `[]`/0 versus missing input nonzero | Controls use the same predicates as valid checks; expected value is not recycled as observation. |
| S16-5 | Valid pinned route passes all registered hashes/ranges, exact six-file scope, source/protected planning state and whitespace | One wrong hash, wrong YAML path, dangling evidence, invalid membership, out-of-bounds/reversed range and missing/foreign recipe endpoint reject; report actual statuses. |
| S16-6 | Handoff retains Slice17 sizing, other family owners, P-15 and UAT | No schema, actor enum, runtime, admission or next-slice acceptance claim. |

Run `jq empty` on the registry, full precommit and committed literal route,
`git diff --check`, `git diff --cached --check`, exact scoped diff and status
checks for both worktrees. Record any exploratory failures and all unrun
required checks. A passing wrapper is structural evidence only. This
planning-only slice does not require source package gates as a substitute.

## Scope, Stop Conditions And Return

CC may edit exactly these six Slice16 paths: `artifacts/semantic-membership.json`,
`artifacts/semantic-evidence.md`, `artifacts/validation-evidence.md`,
`artifacts/handoff.md`, `ledger.md`, and `closing-report.md`. The default
durable home is `artifacts/`; prompts, plans, directives, coverage, frozen
inventory, Slice15 records and source skills are read-only. Inspect the
staged/unstaged/named-new union. Stop and return to CRC if evidence changes
materially, the selected census differs, the route cannot distinguish a
real error, a member needs a new policy, or reading plus implementation
cannot fit with recovery headroom. CRC escalates structural questions to
CDC through the Operator; CC does not choose a different boundary.

Commit with explicit **file names** in `git add --` and `git commit --only --`,
never a directory/glob/broad add or `-a`. Preserve unrelated work. Include:

~~~text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
~~~

Return exact source/opening/CC/recipe commits, six-file changed-path list,
intake/readback pointer, census/member results, per-row attestation, precommit
and committed replay exit statuses, failed/unrun attempts and unresolved
questions. CRC independent verification and CDC arc composition remain
separate gates; do not write `crc-verification.md`.
