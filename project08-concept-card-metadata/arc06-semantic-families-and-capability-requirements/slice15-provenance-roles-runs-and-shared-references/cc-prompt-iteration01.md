# Slice15 Iteration01: Complete Negative Evidence Controls

You are CC in the Project08 Three-Contributor Workflow with Expedited Mode.
Execute this preserved follow-up assignment and return the committed packet
to CRC through the Operator. Project-relative path:
`arc06-semantic-families-and-capability-requirements/slice15-provenance-roles-runs-and-shared-references/cc-prompt-iteration01.md`.
The preceding assignment is `cc-prompt.md`; do not edit it. This is evidence
repair, not source implementation or semantic/schema redesign.

## Contract And Baseline

CRC independently replayed the committed initial packet (`CC_COMMIT=678a8c76`,
`REPLAY_COMMIT=89568110`) at planning HEAD `178f1e6e` and source HEAD
`76a69fd9c295e78f23faa651746c2e36646e0ebd`. The valid route exited 0 and
the native eight-pair meanings were bounded. CRC found three gaps in
`crc-verification.md`: missing wrong-hash mutation (R1), claimed but unrun
wrong YAML-exclusion mutation (R2), and wording that overstates a missing-path
endpoint test as a valid stale-recipe test (R3). Preserve the 37/2,054 census,
39 evidence hashes/ranges, current eight-pair assignment, source drift guard,
all existing controls, and the 200/355/8/347 opening coverage. The frozen
transition, accepted Slice13/14 packets, skills, schema, runtime, package,
memory and UAT remain untouched. No pair moves to accepted in this pass.

## Required Reading And Intake

Read completely, in order, from the canonical planning checkout: this prompt;
`slice-plan.md`; `ledger.md`; `crc-verification.md`; the initial `cc-prompt.md`
(especially Test Oracles and Scope); `artifacts/validation-evidence.md` (all
of the literal route); `artifacts/semantic-membership.json`; and
`closing-report.md`. Read the current `project-plan.md` sections on workflow,
coverage and gates, `arc-plan.md` sections on Slice15/16/17 and authority, and
`../cdc-directive01.md` fully for the approved eight/twelve split. Read the
source `knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md`
sections `Required reading and CC intake` and `Corrective iterations`, and
`knowledge/testing/guides/01-testing-discipline.md` sections on behavioral
oracles and failure triage. The source is the main ai-engineering checkout at
the source HEAD above; planning is the canonical `.worktrees/planning` checkout.

Before editing, record the actual current source/planning revisions, clean or
dirty state, each required item's fully loaded extent, and a concise readback
in the existing `artifacts/validation-evidence.md`. If output is truncated,
recover the omitted ranges. Read the CC closing report's actual statuses as
historical claims, not as authority to skip a control. If source or planning
has drifted materially, stop and report the specific difference to CRC.

## Repair Recipe

1. In `artifacts/validation-evidence.md`, factor the current positive
   `hash_evidence` comparison into a candidate-registry predicate, or use an
   equivalent direct call that exercises **the same** hash comparison for
   valid and corrupted registries. The candidate must be valid JSON, and the
   mutation must change exactly one `.evidence[].sha256` while the registered
   input bytes remain unchanged. For example, clone the registry through jq,
   alter the `projectLedger` hash to a 64-character wrong hex value, and feed
   that candidate to the verifier. Binding result: valid registry passes all
   39 rows; corrupted candidate rejects with nonzero status. Do not mutate a
   source/planning file to simulate a hash mismatch. Recommended shape:

   ~~~bash
   # Sketch, not pre-tested drop-in code: adapt the existing hash dispatcher.
   check_hashes() {
     local candidate=$1 row expected actual
     while IFS= read -r row; do
       # Resolve root/read_mode/authority/path exactly as the existing route.
       # Compare actual pinned bytes to the hash on this candidate row.
       [[ "$actual" == "$expected" ]] || return 1
     done < <(jq -c '.evidence[]' <<< "$candidate")
   }
   valid=$(jq -c . "$registry")
   check_hashes "$valid" || fail "registered hash mismatch"
   wrong=$(jq -c '(.evidence[]|select(.evidence_id=="projectLedger")|.sha256)="0000000000000000000000000000000000000000000000000000000000000000"' <<< "$valid")
   if check_hashes "$wrong"; then fail "wrong hash accepted"; fi
   ~~~

   Keep the existing snapshot/live dispatch, current-source byte check, all
   39 positive rows and exact authority commits. Avoid a second, weaker
   predicate used only by the control. Record the wrong-hash exit status.

2. Reuse the route's exact YAML-exclusion set comparison as a function over
   the candidate registry. Positive input must match the three frozen
   YAML::XS error paths, not just count 3. Clone the authored registry and
   replace one exclusion path with a plausible but nonexistent pathname,
   keeping list length at three. The candidate must reject with status 1;
   the valid registry must pass. Preserve the distinction between three parse
   errors, 15 no-frontmatter files and 37 parsed selected mappings. Do not
   edit the frozen inventory. This is the same-predicate test that the initial
   prose claimed but did not run.

3. Correct `closing-report.md` and `artifacts/semantic-evidence.md` so their
   control lists and endpoint descriptions match **observed** runs. The older
   `8e6b6770`/opening `4db8d882` recipe-path checks returned status 2 because
   Slice15's recipe file was absent, not because a present valid stale recipe
   was semantically rejected. Record this limitation explicitly. Do not
   invent a previous valid Slice15 recipe or silently recast status 2 as a
   stronger test. Update the validation record with the new precommit and
   committed outcomes, any failures, and the actual changed endpoints.

4. Reconcile `ledger.md` S15-2 and S15-5 and `artifacts/handoff.md` only as
   needed for accurate proposed-done attestation. Preserve the other four
   row claims and all substantive semantic meanings unless evidence forces
   a specific correction. If a new design or scope decision becomes necessary,
   stop and return it to CRC; CRC escalates to CDC and the Operator.

## Verification And Return

Run the complete literal route with valid data, then both new mutations and
all existing controls. Re-run the precommit mode, the committed CC/recipe
wrapper with separately pinned endpoints, `jq empty` on the registry,
`git diff --check`, `git diff --cached --check`, exact six-path scope and
source/planning status. Report actual exit statuses, including failed or
unrun attempts; a status-0 wrapper alone does not prove semantic acceptance.
The replay must execute bytes extracted from the named `REPLAY_COMMIT`, not
from the live file. A missing recipe path must fail closed. If a valid older
recipe does not exist, say so; do not demand a fictitious stale-valid case.

CC may edit only the six original output paths: `artifacts/semantic-membership.json`,
`artifacts/semantic-evidence.md`, `artifacts/validation-evidence.md`,
`artifacts/handoff.md`, `ledger.md`, and `closing-report.md`. Preserve this
prompt, the initial prompt and `crc-verification.md` as read-only. The route
repair should normally touch validation evidence, semantic evidence and
closing report, with ledger/handoff only if their claims need adjustment.
Inspect staged, unstaged and named-new paths. Use explicit file names in both
`git add --` and `git commit --only --`; do not commit directories, globs or
unrelated work. Include the required trailers:

~~~text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
~~~

Return the exact CC contribution and separate recipe commits, six-path diff,
full replay results, R1-R3 disposition, row walk and remaining limitations to
CRC through the Operator. The packet remains CC proposed-done until CRC
independently reviews it; Slice16 cannot open before that review.
