# CC Assignment: Verify Registered Evidence Ranges (Iteration 03)

Project: `project08-concept-card-metadata`.
Arc: `arc06-semantic-families-and-capability-requirements`.
Slice: `slice14-provenance-context-and-reference-semantics`.
This prompt: `cc-prompt-iteration03.md`.
Predecessor: preserved, executed `cc-prompt-iteration02.md` (contribution
`ee80f9149a8badaa998ef65e5b8e17239164cb5f`, separate replay recipe
`3372da88c5ed2d9d070a89974473532ff0f29e4a`). This is the second
requested corrective pass; iteration01 was a routing replacement. CC returns
the packet to the independent CRC through the Operator. CDC owns design and
arc/project composition. Expedited Mode remains in force.

This is **evidence-only repair**, not source implementation. Keep exactly the
same twelve actor/actor.id pairs, six ledger rows and six-file CC output fence.
CRC independently reproduced the iteration02 R1-R4 repairs. The only open
finding is R5 under S14-5: four `source_range` values in the evidence register
cite lines past the ends of their pinned files, and the replay does not check
registered reading ranges. No semantic pair is accepted until independent
review of this correction. No schema, source skill, runtime, package,
extraction, memory or Slice15 work is authorized.

## Baseline And Required Reading

Canonical planning root:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`.
Read-only source root: `/Users/oubiwann/lab/billosys/ai-engineering`.
At authoring, planning HEAD was `eab5e69c02afc1cce0cb983d8ba26f893a0902c0`
and source HEAD was `76a69fd9c295e78f23faa651746c2e36646e0ebd`;
both were clean. The four bad ranges were checked against each row's declared
authority commit, not against a guessed mutable copy. Recheck actual HEADs
and dirty state at intake. Your opening planning authority is the clean commit
containing this assignment, not the author's earlier HEAD. A source HEAD
advance alone is not drift; compare registered bytes and relevant paths.

Paths in the table are relative to the named root. `slice/` means the exact
planning directory
`project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice14-provenance-context-and-reference-semantics/`.
Read in order before dependent edits. A bare historical prompt is not current
authority.

| Order | Root and path | Scope | Why / before |
| --- | --- | --- | --- |
| 1 | Source `AGENTS.md`; Planning `project08-concept-card-metadata/AGENTS.md` | Required-full | Standing branch, commit, role and project fences; before any edit. |
| 2 | Planning `slice/cc-prompt-iteration03.md`, `slice/slice-plan.md`, `slice/ledger.md`, `slice/crc-verification.md` | Required-full, each file | Current assignment, unchanged six-row contract and chronological CRC R5; before design or edit. |
| 3 | Planning `slice/artifacts/semantic-membership.json`, `slice/artifacts/validation-evidence.md`, `slice/closing-report.md` | Required-full, each file | Existing 42-row register, literal executable replay and CC attestation; before changing either artifact. |
| 4 | Planning `project08-concept-card-metadata/project-plan.md` sections `Schema And Specification Discussion Gate`, `Current Direction: Semantic Families And Capabilities`, `Contributor Workflow`, `Design Handoff History`; `project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/arc-plan.md` sections `Current Review`, `Starting Evidence And Coverage`, `Operating Method`, `Slice Roadmap`, `Deliverables And Acceptance` | Required-section, complete named sections and necessary definitions | P-15, CRC authority, accepted/outside work; before finalizing the repair. |
| 5 | Source `knowledge/collaboration-framework/SKILL.md`, `knowledge/concept-cards/SKILL.md`; Source `knowledge/project-management/guides/README.md` | Required-full, each file | Workflow/Expedited and domain boundaries; before implementation. |
| 6 | Source `knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md` section `Required reading and CC intake`; Source `knowledge/concept-cards/guides/08-validation-verification.md` sections `Define The Review Before Checking`, `Perform Structural Validation`, `Make Each Result Recoverable`; Source `knowledge/testing/guides/01-testing-discipline.md` sections `Test Behavior And Contracts`, `Failure Triage` | Required-section, complete named sections and definitions | Intake, source-bound structural checks and meaningful negative controls; before implementation. |
| 7 | Planning `slice/artifacts/semantic-evidence.md`, `slice/artifacts/handoff.md` | Required-section: `Opening state and exact boundary`, `Iteration02 corrections`, `Native census`, `Outside work and next unit` as applicable to the named file | Ensure range repair does not alter semantic conclusions or downstream ownership; before report. |
| 8 | Planning `slice/cc-prompt-iteration02.md` and older prompts | Reference-only historical assignments | Preserve them unchanged; consult only if a conflict is suspected. |

Governing repository instructions may require additional full reads; this
manifest does not narrow them. Load each required extent with bounded tool
output; recover every truncated portion, including file ends. Record actual
loaded paths, commit/state and ranges or gaps in a compact `Iteration03 intake`
section of the existing `artifacts/validation-evidence.md`. Add a brief
source-cited contract readback connecting S14-5, the register/route edits,
failure behavior and unchanged acceptance boundaries. Carry its pointer into
`closing-report.md`. Receipt or hash alone is not comprehension or acceptance.
If a required input is unavailable or conflicts with this assignment, stop
the affected edit and report the exact conflict to CRC through the Operator.

## Inspected Baseline And Binding Decisions

At `ee80f914`, `artifacts/semantic-membership.json` has 42 evidence entries.
Each has root, path, hash, read mode, authority, role and `source_range`.
`artifacts/validation-evidence.md` already resolves all 42 bytes/hashes and
replays the native census, but never reads `source_range`. The source skill's
validation guide separates structural evidence integrity from semantic
warrant; this repair checks registered locations, not actor meaning or source
truth. Testing guidance calls for a negative control that rejects a plausible
wrong register, not merely a parser exit.

| Guidance applied by CRC | Decision here | Proof CC must return |
| --- | --- | --- |
| `knowledge/concept-cards/guides/08-validation-verification.md`, `Perform Structural Validation` and `Make Each Result Recoverable` | Check exact evidence location at its declared revision; do not claim semantic verification from a passing hash/range check. | All 42 rows resolve, four corrected spans exist, claim remains structural only. |
| `knowledge/testing/guides/01-testing-discipline.md`, `Test Behavior And Contracts` | Exercise the same production range predicate with out-of-bounds and reversed-span mutations. | Both mutations fail while a valid multi-span and existing JSON descriptor pass. |
| `knowledge/work-verification/guides/05-independent-verification.md`, `The Separation Rule` | CC records proposed-done; CRC independently replays before acceptance. | Closing report and ledger retain the reviewer gate. |

**Binding:** resolve a line range against the *same declared root, read mode,
path and authority revision* used for its evidence hash. Do not use current
working-tree length for a snapshot. Treat `JSON document` range descriptions
as non-line descriptors; keep their existing hash/path checks. For line ranges,
require well-formed positive inclusive spans, start <= end, and every end <=
the resolved file's actual line count. Missing file/commit, invalid range or
out-of-bounds range fails the replay. No silent truncation or substitution.

**Binding:** preserve iteration02's R1-R4 repairs, both evidence-reference
layers, all 42 hashes, exact twelve-pair/188-367-12-355 accounting,
2,054-record legacy denominator, three YAML errors versus 15 no-frontmatter
records, diagnostics, negative controls, separate recipe endpoint and
unrelated-source-HEAD tolerance. Do not edit the old prompt or frozen inputs.

**Recommended:** add a `check_registered_ranges "$registry"` function to the
existing literal route, near `hash_evidence`, and call it in precommit and
committed modes. Keep the checker in `validation-evidence.md`; no new helper
file, parser, schema or dependency. Private function names are local
discretion; accepted range syntax and failure behavior are not.

Four currently false registrations, measured at their declared revisions:

| Evidence ID | Current `source_range` | Pinned file length | Valid correction |
| --- | --- | ---: | --- |
| `projectLedger` | `lines 1-45` | 43 | `lines 1-43` |
| `slicePlan` | `lines 17-225` | 223 | `lines 1-223` (entire opening plan) |
| `assignmentPrompt` | `lines 1-236` | 72 | `lines 1-72` (entire executed prompt) |
| `slice03ReplayContract` | `lines 1-100` | 93 | `lines 1-93` |

These are the only out-of-bounds numeric rows found in the author's 42-row
scan; rederive all 42 rather than trusting that assertion. When moving the
opening authority to the commit containing iteration03, remeasure the new
`slicePlan` and `assignmentPrompt` from that commit. Register the actual
iteration03 prompt and its actual hash/range; protect it in the replay's
read-only path set. Do not reuse the 223/72 lengths if those files changed.

## Implementation Spine And Code Shape

1. **Registry, `artifacts/semantic-membership.json`:** inspect all 42
   `source_range` entries and resolve each against its own evidence row.
   Correct the four known false ranges and update the opening assignment
   references (`slicePlan`, `sliceLedger`, `assignmentPrompt`) to the actual
   iteration03 opening commit where appropriate. Preserve IDs, member/shared
   links, native census and semantic meanings. Result: every cited line exists
   in the registered bytes, with unchanged evidence scope.
2. **Route, `artifacts/validation-evidence.md`:** add range validation after
   JSON/reference and hash resolution. Use the same root/mode/authority/path
   dispatch as `hash_evidence`; for snapshots, count lines from `git show
   "$authority:$path"`, for live entries from the declared file path. A
   failed `git show`, read or parse must propagate nonzero. Accept existing
   `JSON document` descriptions without inventing line numbers. Do not turn
   this check into a current-HEAD lock.
3. **Negative control:** clone the parsed registry in memory, mutate one
   otherwise valid row's `source_range` to `lines 1-999999`, and run the *same*
   range predicate used in the positive path. It must fail nonzero. Also
   exercise an inverted span such as `lines 15-10`; a mere maximum-line check
   would wrongly accept it. Keep the existing wrong-exclusion, wrong-actor,
   member/reference, no-match/error and missing-recipe controls intact.
4. **Attestation:** record actual commands/results and any failed attempts in
   `validation-evidence.md`; update the existing `ledger.md` and
   `closing-report.md` for iteration03. Touch `semantic-evidence.md` or
   `handoff.md` only if a statement becomes stale. Do not claim CRC acceptance.

The following is an **illustrative Bash/jq integration sketch**, not tested
drop-in code. Its jq span predicate *was* independently exercised by CRC with
`n=72`: `lines 1-72` and `lines 1-10, 20-30` returned true/status 0;
`lines 1-236` and `lines 15-10` returned false/status 1. CC must wire the
file-resolution branch into the existing route and test the integrated code.

~~~bash
check_line_range() {
  local row=$1 range n evidence_root mode authority path
  range=$(jq -r '.source_range' <<< "$row") || return 1
  case "$range" in
    "JSON document"|"JSON document; selected values and YAML-error records") return 0 ;;
    "lines "*) ;;
    *) return 1 ;;
  esac
  evidence_root=$(jq -r '.root' <<< "$row") || return 1
  mode=$(jq -r '.read_mode' <<< "$row") || return 1
  authority=$(jq -r '.authority_commit // empty' <<< "$row") || return 1
  path=$(jq -r '.path' <<< "$row") || return 1
  case "$evidence_root:$mode" in
    planning:snapshot) n=$(git -C "$root" show "$authority:$path" | awk 'END {print NR}') || return 1 ;;
    source:snapshot) n=$(git -C "$source" show "$authority:$path" | awk 'END {print NR}') || return 1 ;;
    planning:live) n=$(awk 'END {print NR}' "$root/$path") || return 1 ;;
    source:live) n=$(awk 'END {print NR}' "$source/$path") || return 1 ;;
    *) return 1 ;;
  esac
  jq -ne --arg r "$range" --argjson n "$n" '
    if ($r | test("^lines [1-9][0-9]*-[1-9][0-9]*(, [1-9][0-9]*-[1-9][0-9]*)*$")) then
      ([ $r | scan("[0-9]+-[0-9]+") | split("-") | map(tonumber) ]
       | all(.[]; .[0] <= .[1] and .[1] <= $n))
    else false end
  ' >/dev/null
}

[[ $(jq '.evidence | length' "$registry") == 42 ]] || fail "evidence denominator changed"
while IFS= read -r row; do
  check_line_range "$row" || fail "invalid source_range: $(jq -r '.evidence_id' <<< "$row")"
done < <(jq -c '.evidence[]' "$registry")
~~~

The sketch assumes the literal route's existing `set -euo pipefail`, `root`
and `source` bindings. Ensure failures propagate through the real call site;
do not hide a failed input read in a process substitution or turn a malformed
range into an empty success. The existing JSON descriptions are the two
literal forms shown; a new notation needs CRC/CDC disposition. An equivalent
local implementation is acceptable
only with the same behavior and explicit explanation in the return packet.

## Test Oracles And Required Gates

| Criterion | Setup and action | Expected observation | Rejects |
| --- | --- | --- | --- |
| S14-5 range integrity | Resolve each of 42 registered inputs at its declared snapshot/live state; run same predicate on all line spans | Every registered span is in-bounds after correction; the four previously false rows resolve to their actual pinned files | Hash-only validation and copied stale line counts |
| S14-5 negative control | Mutate a valid line range to `lines 1-999999`; rerun the production range predicate | Nonzero rejection with identified evidence ID | A checker that ignores `source_range` |
| S14-5 boundary control | Mutate a range to `lines 15-10` | Nonzero rejection | End-only checks accepting reversed spans |
| S14-5 non-line continuity | Keep `JSON document` descriptions and re-run all evidence hashes | Descriptions remain accepted; files still resolve and hash | Accidental rejection or bypass of JSON evidence |
| S14-1/S14-4 continuity | Re-run the full existing literal route on the corrected packet | Twelve exact pairs; 188/367/12/355; 12 native and 2,054 legacy mappings; all earlier diagnostics and controls retain their statuses | Regression while adding range checks |
| S14-2/S14-3 continuity | Recheck support census and YAML exclusions | Four populated support actors, one template/null; three YAML errors distinct from 15 no-frontmatter | Semantic/count regression |
| S14-6 continuity | Read handoff and project gate | Slice15 and P-15 remain open; no source, schema or runtime action | Silent downstream scope loss |

From the canonical planning cwd, run the complete precommit route with
`CC_PRECOMMIT=1` while the explicitly named allowed files are staged. Then
commit the exact changed files with both required trailers and run the
published committed wrapper with `CC_COMMIT=<new contribution>` and a separate
explicit `REPLAY_COMMIT=<recipe revision>`. Reproduce missing/stale recipe
rejection and the new range controls. Run `jq empty` on the registry,
`git diff --cached --check`, `git diff --check`, and inspect both worktree
statuses. Record commands and status/output, including failed/unrun attempts.
No source/package Make gate substitutes for this planning-only replay.

## Scope, Stop Conditions And Return

Permitted CC output paths, all under `slice/`, are only:

- `artifacts/semantic-membership.json`
- `artifacts/semantic-evidence.md`
- `artifacts/validation-evidence.md`
- `artifacts/handoff.md`
- `ledger.md`
- `closing-report.md`

Plans, issued prompts, `crc-verification.md`, coverage, frozen inventory,
earlier packets and all source files are read-only. Do not add a helper,
parser, Ruby/Python script, schema or new artifact. Exact changes should
normally be registry, validation, ledger and closing report; the other two
remain allowed only if continuity requires them. Check staged, unstaged and
named-new union against the six paths. Use explicit filenames in `git add --`
and `git commit --only --`; never use a directory pathspec or broad add.
Include both trailers:

~~~text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
~~~

If a registered path or authority revision is missing, an evidence meaning
changes, a new range notation needs policy, or this repair cannot fit with
review headroom, stop affected work and return an exact blocker to CRC through
the Operator. CRC escalates design/scope changes to CDC; CC does not choose a
new contract. Otherwise execute under existing authority. Report the actual
opening and final commits, files changed, per-row evidence, precommit and
committed statuses, failed/unrun attempts, intake/readback pointer, any
deviation from the recommended sketch and remaining limitations. The CC
closing report stays proposed-done pending independent CRC verification.
