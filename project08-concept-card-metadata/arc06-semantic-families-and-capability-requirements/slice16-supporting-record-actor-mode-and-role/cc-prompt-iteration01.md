# Slice16 Iteration01: Bind Evidence Authorities And Range Coverage

You are CC in the Project08 Three-Contributor Workflow with Expedited Mode.
Execute this preserved follow-up assignment and return a committed
**proposed-done** repair to CRC through the Operator. Project-relative path:
`arc06-semantic-families-and-capability-requirements/slice16-supporting-record-actor-mode-and-role/cc-prompt-iteration01.md`.
The predecessor is this slice's issued `cc-prompt.md`; do not edit it. This is
evidence-route and reporting repair, not source implementation or semantic
redesign.

## Baseline And Remaining Rows

CRC reviewed the packet at clean planning `974dd26a` and source `ce3f7710`.
The pinned wrapper with `CC_COMMIT=2953953d` and `REPLAY_COMMIT=974dd26a`
passed; the twelve field/kind meanings, 12-record census and six-file scope
have no finding. CRC's `crc-verification.md` records three unresolved issues:
R1 and R2 on S16-5 (declared authority and all-range validation), and R3 on
S16-4 (raw no-match output). Preserve 555/208/347/12/335, the accepted
Slice15 eight, all 45 evidence rows, the three YAML/15 no-frontmatter and
2,054 legacy distinctions, every existing positive/negative control, and the
source/plan protection fence. No pair moves to accepted in this pass. Slice17
remains CDC-held; P-15 and UAT remain open.

## Required Reading And Intake

Read in order, using bounded complete output:

| Class | Exact material | Why |
| --- | --- | --- |
| Required-full | This prompt; this slice's `slice-plan.md`, `ledger.md`, `crc-verification.md`, `artifacts/validation-evidence.md` including the entire literal route, `artifacts/semantic-membership.json`, and `closing-report.md` | Current assignment, three defects and exact replay/registry surface; load before editing. |
| Required-section | Initial `cc-prompt.md`: `Binding Contract And Opening State`, `Evidence Design And Recommended Sequence`, `Test Oracles And Required Gates`, `Scope, Stop Conditions And Return`; project `project-plan.md` `Current Direction` and `Contributor Workflow`; Arc06 `arc-plan.md` `Current Review` and Slice15-17 breakdown | Retain initial behavioral/authority fences without treating this as a new slice. |
| Required-full | Arc06 `cdc-directive01.md` | Exact twelve-pair boundary, held Slice17, no source/schema authority. |
| Required-data | Project `artifacts/semantic-coverage-current.json`, exact `counts`, accepted/remaining/next-set queries; Arc01 Slice01 `artifacts/frontmatter-inventory.json`, twelve selected actor states plus three parse-error paths, fifteen no-frontmatter and 2,054 legacy rows | Reproduce the relevant denominator/projection without dumping the full inventory; record commands, exits and full selected results. |
| Required-section | Source `knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md` sections `Required reading and CC intake`, `Corrective iterations`; source `knowledge/testing/guides/01-testing-discipline.md` sections `Test Behavior And Contracts`, `Failure Triage`; source `knowledge/work-verification/guides/03-row-closure.md` sections `Final Statuses`, `Working Protocol For CC` | Intake, negative-oracle design and truthful row walk. |

Record actual source/planning revisions and status, loaded extents and data-query
results in the existing `artifacts/validation-evidence.md`. Recover truncated
required output. Provide a concise source-cited readback connecting R1-R3 to
S16-4/S16-5, the exact files to repair, and expected failure outcomes. If a
registered input or source baseline changed materially, stop and report it to
CRC before dependent edits. This prompt does not waive the initial assignment.

## Focused Repair Recipe

1. **Bind each evidence row to its authority.** In the literal route's
   `check_hashes` and range checker, read `.authority_commit` from each row.
   The 45 current snapshot rows are pinned at planning opening
   `3b7790f88cd30fa6c4988a6950b4989ae1933b7d` or source opening
   `ce3f77103eff5e07b3533a03c65f158684fc1039` according to `.root`.
   Require that root/commit pairing for this packet, then resolve the path
   through that **declared** commit. Do not merely compare candidate hashes
   to an unmutated registry while reading the fixed opening commit. Preserve
   source cleanliness and relevant-byte drift checks without requiring the
   global current source HEAD to remain equal to opening HEAD. A future
   mixed-authority pattern would require explicit registration and review;
   it is not silently authorized here.

   Recommended Bash shape (design sketch, not pre-executed drop-in code):

   ~~~bash
   resolve_snapshot() {
     local row=$1 evidence_root path commit expected repo
     evidence_root=$(jq -r '.root' <<< "$row")
     path=$(jq -r '.path' <<< "$row")
     commit=$(jq -r '.authority_commit' <<< "$row")
     case "$evidence_root" in
       planning) expected=$opening_planning; repo=$root ;;
       source) expected=$opening_source; repo=$source ;;
       *) return 1 ;;
     esac
     [[ "$commit" == "$expected" ]] || return 1
     git -C "$repo" show "$commit:$path"
   }
   ~~~

   The sketch illustrates binding the declared revision, not a prescribed
   helper signature. Preserve the route's existing root/read-mode dispatch;
   the sketch covers snapshot rows only. Bash/Git/jq/shasum only; no new
   helper file or parser. Positive
   result: all 45 registered hashes and locations at their declared commits.
   Negative result: mutate exactly one `authority_commit` to a nonexistent or
   wrong existing revision; the same production check must reject status 1
   without modifying registered bytes. Record which row was changed.

2. **Check every range.** Current registry has 42 numeric `lines a-b` rows,
   two `JSON document` rows (`currentCoverage`, `transitionCoverage`), and
   one `JSON document; selected values and YAML-error records` row
   (`inventory`). The route must visit all 45 and require each exact descriptor
   only for its named JSON evidence ID. Numeric spans must be well formed,
   positive, ordered, and within the line count of the row's declared
   authority bytes; reject unsupported roots/read modes. A `not-a-range`
   mutation on a numeric row, or a JSON descriptor on a Markdown row, must
   reject status 1. Retain out-of-bounds and reversed-range controls. An
   empty projection over selected numeric rows is not an all-row check.

3. **Return the promised no-match value.** Use the real inventory query to
   capture the selected actor array itself. The absent path must yield literal
   `[]` and status 0; a missing inventory file must yield nonzero (observed
   status 2). Record both independently. An optional `{count,actors}` summary
   may supplement but must not replace the raw result. Update
   `artifacts/validation-evidence.md` and `closing-report.md` accordingly.

4. **Reconcile CC attestation.** Re-run the full route in precommit and pinned
   committed modes. Record the exact CC registry endpoint and separate recipe
   endpoint; the recipe executed must come from `REPLAY_COMMIT`, not the live
   Markdown. Record exploratory failures, all mutation statuses and any unrun
   checks. Adjust `artifacts/semantic-evidence.md`, `artifacts/handoff.md` or
   `ledger.md` only if factual claims need correction. Do not change the
   twelve member meanings merely to satisfy a mechanical test.

## Acceptance And Return

R1 passes when a changed declared authority is rejected while all 45 valid
hashes and ranges still pass at their registered revisions. R2 passes when
all 45 range fields are classified and an unknown or misplaced descriptor
fails alongside out-of-bounds/reversed spans. R3 passes when the real
no-match returns `[]`/0 and missing input remains a distinct error. Recheck
the exact twelve-pair set, 12/2/6/4 and 2,054/3/15 denominators, all prior
negative controls, registry references, source/protected planning paths,
`jq empty`, `git diff --check`, `git diff --cached --check` and both worktree
statuses. A status-0 wrapper is structural evidence, not semantic acceptance.

CC may edit only the six original Slice16 output paths:
`artifacts/semantic-membership.json`, `artifacts/semantic-evidence.md`,
`artifacts/validation-evidence.md`, `artifacts/handoff.md`, `ledger.md`, and
`closing-report.md`. The route/report repair should normally touch the last
two evidence/report surfaces, with ledger/handoff only if needed. Preserve
this prompt, initial prompt, plans, directive, CRC record, coverage, inventory,
Slice15 packet, and source checkout. If repair would change scope, schema,
authority policy or owner, stop and return to CRC for CDC escalation.

Inspect staged, unstaged and named-new paths. Use explicit full file names
in `git add --` and `git commit --only --`, never a directory/glob/broad add
or `-a`; preserve unrelated work. Include required trailers:

~~~text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
~~~

Return this iteration path, exact contribution/recipe commits and changed
files, intake/readback pointer, R1-R3 disposition, full replay output/status,
failed or unrun attempts, six-row closeout and remaining limits through the
Operator to CRC. CRC alone independently accepts this slice; CDC arc
composition and Operator gates remain separate.
