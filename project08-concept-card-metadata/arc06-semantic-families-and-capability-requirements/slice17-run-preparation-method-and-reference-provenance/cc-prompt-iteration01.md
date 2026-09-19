# Slice17 Iteration01: Complete Controls And Preserve Endpoint Replay

You are CC in the Project08 Three-Contributor Workflow with Expedited Mode.
Execute this preserved corrective assignment and return a committed
**proposed-done** repair to CRC through the Operator. Project-relative path:
`arc06-semantic-families-and-capability-requirements/slice17-run-preparation-method-and-reference-provenance/cc-prompt-iteration01.md`.
The predecessor `cc-prompt.md` remains preserved and binding except where this
prompt narrows the repair. This is replay/report correction, not semantic
redesign, source implementation or a new slice.

## Baseline, Accepted Work, And Remaining Rows

CRC reviewed clean planning `89d1b452b26235d16508c245f9bb13d6dd616079`
and source `ce3f77103eff5e07b3533a03c65f158684fc1039`.
Independent execution of recipe `f82af9b7` against registry `97a75091` passed.
CRC accepts for preservation, but not final slice closure, the exact eighteen
meanings, 39-row evidence registry, full native matrix, semantic report,
handoff, positive no-match/tool-error results and all controls already present.

`crc-verification.md` records three findings. R1 affects S17-1/S17-3/S17-5:
four required discriminators were omitted. R2 affects S17-6: the reported
endpoint wrapper is not preserved and its status-2 claim is not reproducible.
R3 affects S17-3: one sentence says two YAML-error files while naming three.
S17-2, S17-4 and S17-7 have no finding. Preserve 555/220/335/18/317, all
existing checks and the unopened Slice18-21/248-pair owners. No pair moves to
accepted during CC repair.

## Required Reading And Intake

Read in order with bounded, complete output. Recover truncation and record the
loaded extent, current revisions and concise contract readback in the existing
`artifacts/validation-evidence.md`; carry the pointer into `closing-report.md`.

| Class | Exact material and state | Purpose |
| --- | --- | --- |
| Required-full | This prompt; `crc-verification.md`; current `slice-plan.md` and `ledger.md`; initial `cc-prompt.md`; complete `artifacts/validation-evidence.md`; `closing-report.md`, all at current planning HEAD | Exact R1-R3 contract, preserved initial controls and reporting surfaces; load before editing |
| Required-full | `artifacts/semantic-membership.json`, `artifacts/semantic-evidence.md`, `artifacts/handoff.md` at registry endpoint `97a75091` | Read-only semantic baseline; ensure repair does not change accepted-for-preservation meanings |
| Required-section | `project-plan.md`: `Current Direction`, `Contributor Workflow`, `Schema And Specification Discussion Gate`; `arc-plan.md`: `Current Review`, `Operating Method`, `Slice Roadmap`; `cdc-directive02.md`: `Decisions And Authority`, `Exact Ownership And Order`, `CRC Readiness Issuance And Review`, `Holds And Return` | Retain scope, role and no-normative-adoption boundaries |
| Required-section | Source `knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md`: `The author responsibility and decision authority`, `Design the tests and their oracles`, `Required reading and CC intake`, `Corrective iterations`; source `knowledge/testing/guides/01-testing-discipline.md`: behavioral-contract and failure-triage sections; `knowledge/work-verification/guides/03-row-closure.md`: final statuses and CC protocol | Apply same-predicate controls and truthful row closure |
| Required-data | Current coverage exact counts/set; frozen inventory's three extraction-run records, three YAML errors, fifteen no-frontmatter records and 2,054 historical rows; current registry's exact 18 memberships/39 unique evidence IDs; current route's existing control names/statuses | Reproduce complete bounded projections and preserve denominators; record commands, exits and complete selected output |

Conditional: if a repair would change `semantic-membership.json`,
`semantic-evidence.md` or `handoff.md`, stop and return to CRC unless a newly
discovered factual contradiction makes that unavoidable. Those files are not
authorized for ordinary Iteration01 edits. Slice18-21 are reference-only and
must remain unopened.

Your readback must connect each R1-R3 defect to its production predicate,
observable correction and ledger row. The easily missed constraint is that an
inner route which merely checks that `REPLAY_COMMIT` exists cannot prove its own
bytes were extracted from that commit; the preserved outer wrapper must perform
that extraction before execution.

## Binding Repair Design

### R1: Add The Four Missing Controls

Keep all existing positives and controls. Add these exact cases using the same
production predicates as valid candidates; do not introduce weaker control-only
comparators.

1. **Null-to-absent:** clone `actual_matrix`, replace template
   `finished_at: {state:"null",value:null}` with
   `{state:"absent",value:null}`, and require `check_matrix` to reject status 1.
   This is separate from the existing empty-list-to-absent control.
2. **Accepted/outside membership addition:** clone the valid registry and append
   a structurally complete membership cloned from an existing object, but set
   `[field_path,record_kind]` to an already accepted or outside pair such as
   `["actor","claim"]` and give it a unique `meaning_id`. Require the existing
   `check_registry` exact-set predicate to reject status 1. Avoid an accidental
   rejection solely from a duplicate meaning ID or missing required key.
3. **Other-target path:** clone `actual_matrix`, change the trace
   `input_source_ref.path.value` to the declared prepared target
   `document-extraction/prepared/synthetic-method-note-002.md` (or perform the
   exact inverse), and require `check_matrix` to reject status 1. Preserve the
   existing arbitrary wrong-path control too.
4. **Missing inventory input or invalid authority:** execute the native inventory
   projection against a path that does not exist, or attempt to load the
   inventory from an invalid Git revision. Capture command status/stdout/stderr;
   require nonzero with error evidence and keep it distinct from both successful
   target no-match results. Do not substitute the existing missing synthetic
   target, which exercises a different input/operation.

Print and record four new named statuses. Update the control inventory and all
“all controls” claims so they enumerate the actual complete set. Do not change
the independently authored positive matrix or derive expected values from the
mutated candidates.

### R2: Preserve The Actual Endpoint Wrapper

Add a second literal Bash block or clearly delimited shell section in
`artifacts/validation-evidence.md` that is the exact wrapper used for committed
execution. It must:

1. accept explicit `CC_COMMIT` and `REPLAY_COMMIT`;
2. validate both as commits;
3. load `artifacts/validation-evidence.md` from the declared `REPLAY_COMMIT`;
4. extract exactly one nonempty `~~~bash` literal-route block into a temporary
   file, rejecting a missing file, zero/multiple blocks or malformed close;
5. run `bash -n` on the extracted route;
6. execute that extracted file with the same declared endpoint variables; and
7. preserve the route's stdout and actual exit status.

Recommended behavior sketch, not pre-tested drop-in code:

~~~bash
run_endpoint() {
  local cc=$1 recipe=$2 doc script starts
  doc=$(mktemp); script=$(mktemp)
  git cat-file -e "$cc^{commit}" || return 2
  git cat-file -e "$recipe^{commit}" || return 2
  git show "$recipe:$validation_rel" > "$doc" 2>/dev/null || return 2
  starts=$(grep -c '^~~~bash$' "$doc" || true)
  [[ "$starts" == 1 ]] || return 2
  awk '/^~~~bash$/{p=1;next} p&&/^~~~$/{exit} p' "$doc" > "$script"
  [[ -s "$script" ]] || return 2
  bash -n "$script" || return 2
  CC_COMMIT=$cc REPLAY_COMMIT=$recipe bash "$script"
}
~~~

The wrapper may use safer temporary cleanup and stricter close detection, but
its observable contract is binding. Execute the valid CC contribution against
a **separate new recipe endpoint** and require status 0. Execute the wrapper
with the opening planning commit and foreign source commit as recipe endpoints;
both must fail closed before the inner route. If the wrapper explicitly maps
those extraction failures to 2, record 2 and the literal wrapper proving it.
Otherwise record the actual nonzero statuses and remove the unsupported status-2
claim. Also test an absent/nonexistent commit ID if practical and record it.

The inner route may still check endpoint existence defensively, but that check
does not replace the outer extraction. The recipe executed during acceptance
must be bytes from the reported recipe endpoint, never the live working file.

### R3: Correct The Census Sentence

In `artifacts/validation-evidence.md`, replace the contradictory “the three
YAML-error paths are the two ... files” wording with “the three ... files.”
Preserve the exact three paths, count and distinction from fifteen
no-frontmatter records. Reconcile the closing report if it repeats or implies
the wrong count.

## Required Files, Validation, And Return

CC may edit exactly these three existing Slice17 output paths:

~~~text
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice17-run-preparation-method-and-reference-provenance/artifacts/validation-evidence.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice17-run-preparation-method-and-reference-provenance/ledger.md
project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice17-run-preparation-method-and-reference-provenance/closing-report.md
~~~

All prompts, plans, CRC record, registry, semantic evidence, handoff, parent
plans/ledgers, coverage, inventory, source and future slices are read-only.
Stop and return if the repair needs another path, changes a meaning, changes
counts/ownership, or exposes a contradiction requiring CDC design authority.

Run `jq empty` on the unchanged registry, the complete repaired route in
precommit mode, the preserved wrapper against contribution/separate-recipe
endpoints, every old and new control, `git diff --check`,
`git diff --cached --check`, exact three-file staged/unstaged/untracked union,
and both worktree statuses. Required results:

- positive replay status 0 with unchanged 18/39, 3 x 18, 3/15/2,054 and target
  observations;
- every old control still rejects with its recorded status;
- four new R1 controls reject/fail distinctly as specified;
- valid separate recipe execution passes from preserved endpoint bytes;
- missing/opening/foreign recipe endpoints fail closed with truthfully recorded
  statuses; and
- the census wording consistently says three YAML-error files.

Update S17-1/S17-3/S17-5/S17-6 to CC proposed-done only after these pass;
retain S17-2/S17-4/S17-7 without re-attesting new semantic work. CC does not
write or alter `crc-verification.md` and does not accept the slice.

Commit only the three explicit files with `git add --` and
`git commit --only --`, never a directory/glob/broad add or `-a`. Include:

~~~text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
~~~

Return this iteration path; exact source/opening/contribution/recipe/final
commits; three changed files; intake/readback pointer; R1-R3 disposition; old
and new control statuses; wrapper extraction/execution statuses; failed or
unrun attempts; seven-row closeout; and remaining limits. CRC will independently
extract the wrapper and recipe and decides Slice17 acceptance. CDC arc
composition, P-15, UAT and Operator acceptance remain separate.

## CRC Author Readiness

This correction is source-grounded in the initial prompt, current route and
independent replay. It is design-complete at the mechanical boundary: four
named controls, one outer endpoint contract and one wording fix. It is
executable with existing Bash/jq/Git/hash tools, falsifiable by the exact
mutations and endpoint failures above, and bounded to three files with semantic
artifacts preserved. This is CRC author self-review, not CC completion or
independent acceptance.
