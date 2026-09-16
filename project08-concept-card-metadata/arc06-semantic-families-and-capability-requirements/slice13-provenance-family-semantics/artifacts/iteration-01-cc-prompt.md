# CC: Slice13 Iteration 01, Bounded Evidence Repair

Use a NEW CC session in
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning.

Read project08-concept-card-metadata/AGENTS.md, project/arc plans and ledgers,
this slice's slice-plan.md, ledger.md and cdc-verification.md. Use the current
collaboration-framework/project-management/work-verification guidance. Read the
corrected Slice03 replay and its CDC attribution for the relevant mechanics.
Then read the six submitted Slice13 files at 78be7fab and the specific source
sections implicated by R4. Do not reload every past iteration or redo all
semantic work; retain the verified scope/handoff and supported interpretations.

Source /Users/oubiwann/lab/billosys/ai-engineering stays read-only.
This is the same eight-pair slice, not Slice14 or a new schema. Coverage remains
180 accepted / 375 remaining / eight assigned / 367 outside. P-15 stays open.

## Repair R1-R4

**R1: Validate the actual authored packet.** The original route can pass with
a fabricated member path and dangling member/shared evidence IDs. Derive the
expected eight pairs from the pinned plan, compare the actual memberships and
scope, enforce uniqueness/inclusion/disjointness and resolve meaning IDs and
both evidence-ID layers. Compare the authored census to native results.
Check declared baseline mappings against registered manifest entries and native
bytes, not just a hard-coded cmp. Use the same predicates against separate
temporary invalid-pair and dangling-reference variants: they must reject for
the intended reason. Do not change accepted evidence to make a test pass.

**R2: Reproduce the claimed snapshot.** Provide a literal fail-closed route
wrapper, with recipe revision separate from CC contribution endpoint.
Committed mode must load its registry from that endpoint, not a later working
tree. Precommit may read the live candidate registry explicitly. Pin assignment/
plan/coverage authority to the relevant opening snapshot; report current live
status separately. Do not require the current register to retain obsolete
assignment bytes after authorized CDC advancement. Keep source/frozen input
drift checks. Correct protected arc paths to include the project prefix.

Record three separate boundaries:
- Original contribution: 609f2f55 to 78be7fab, exactly six CC files.
- This repair: fresh repair opening HEAD to new CC endpoint, the authorized
  subset of the same six files, excluding intervening CDC plans/review/prompt.
- Current state: source/prior-input preservation and live status, not a
  substitute for either fixed-history comparison.

Test precommit and committed modes at their actual endpoints. Do not silently
substitute the repair opening for original provenance. Derive evidence-count
output from the validated registry rather than preserving a stale hard-coded
40 when registration changes.

**R3: No swallowed search errors.** The existing raw actor search uses
`|| true`, so a missing input is reported as no actor field. Capture and
distinguish real match/no-match/error statuses and stdout/stderr; exercise a
real error at that operation. Or remove this redundant raw search explicitly,
retaining hash-bound native field-state proof and the actual jq missing-input
control. A separate successful missing-inventory control does not justify a
different operation hiding errors.

**R4: Complete the bounded comparison and citations.** Add the required legacy
untyped census for actor and nested actor.id (state parent absence explicitly).
CDC observed 2,054 parsed legacy mappings with zero actor parents; reproduce,
do not simply copy the reviewer result. This is not a claim that legacy
provenance never existed. Assert the selected 37-record family/state/label
breakdown and named parse exclusions against native data, and reconcile every
authored census cell. Avoid child lookup states becoming semantic inapplicability.

Correct the field-group citation: that table explicitly lists actor for the
run, while the four templates establish the four selected mapping placements.
Register project08-concept-card-metadata/AGENTS.md separately from the planning
root AGENTS.md and retain their different roles. Add precise section/range
references for the changed evidence interpretations. Reconcile registry,
semantic report, handoff and closeout without weakening existing caveats.

## Verification And Stop Conditions

Preserve all original acceptance criteria and six ledger rows. S13-1/S13-6 are
CDC-verified; do not reset them. Rows S13-2 through S13-5 may become CC-attested
proposed-done with explicit R1-R4 evidence, not independently closed.

Reproduce the positive replay, each relevant negative control, registered hashes,
member/shared references, native census, preservation, whitespace and explicit
scope. Preserve failed attempts and limitations. Temporary mutation data belongs
under /private/tmp and must not replace native or tracked evidence. Remove only
your temporary files. No new helper/parser/framework, Ruby, Python, source,
package/install, extraction, schema/runtime/graph/memory change, task dispatch
or model-setting change. Stop with a sizing proposal if repair grows beyond
the bounded findings. No next-slice execution or coverage update.

Only these files may change:
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/semantic-membership.json
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/semantic-evidence.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/validation-evidence.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/handoff.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/ledger.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/closing-report.md

Do not edit plans, CDC report, this prompt, original cc-prompt.md, coverage,
prior slices or source. Preserve unrelated work/index entries. Read each
finding to closure, but do not manufacture facts or future requiredness.

## Explicit Commit

Use exact filenames, inspect the staged diff, and commit only changed files
from the authorized list. The literal full list is safe here when all exist;
do not substitute a directory or broad glob.

~~~bash
git add -- \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/semantic-membership.json \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/semantic-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/validation-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/handoff.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/ledger.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/closing-report.md
git diff --cached --name-only
git diff --cached --check
git commit --only \
  -m "plan(project08): repair actor identity evidence replay" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" -- \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/semantic-membership.json \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/semantic-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/validation-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/artifacts/handoff.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/ledger.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice13-provenance-family-semantics/closing-report.md
~~~

Run the committed replay with the real endpoint. Return the commit, each
finding's disposition, actual controls and remaining limits. Status remains
CC proposed-done pending independent CDC review; do not create a CDC verdict
or open Slice14.
