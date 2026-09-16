# CDC Verification: Arc06 Slice03

Date: 2026-09-15. Verdict: closed with attributed minor CDC replay corrections.
CC endpoint: `b1043afe6b62c019fbcd29dd01c927ea7f9572ac`.
Opening planning endpoint: `ba2dbfd0a30ca4b0fad406d796efc7f54c76e5b6`.
Source: `e763c661592ff1097a94bb470db9cf924524579d`, unchanged and clean.

## Review And Attribution

CDC read the project/arc/slice contract, five-row ledger, three artifacts and
CC closing report, inspected the exact five-file contribution and required
trailers, then executed the recipe extracted from the CC commit. It passed.
Native expected/observed objects were inspected, not inferred from that exit
status. Five opening rows, five CC dispositions, five final CDC dispositions.

The original recipe had three bounded operational shortcomings:

1. Its wrong-digest control compared Markdown bytes to the literal label
   `wrong-digest`. CDC changed it to compute the actual SHA-256 and compare
   against an incorrect 64-digit hash with the positive case's equality
   operation. The original test did not exercise digest verification.
2. Its outer pipeline could run an empty shell successfully after a Git error.
   CDC added fail-closed extraction and a nonempty-block check, separating
   the inspected CC endpoint from the selected replay revision.
3. Its live-status check permanently required zero next-slice assignments.
   CDC retained those exact opening values against the explicit opening
   snapshot and checks live counts against their arrays and accounting
   invariants. Later assignments no longer invalidate historical evidence.

CDC also corrected the prose's `jq -S` description to the actual structural
value comparison. These are attributed replay/documentation completions under
the project/arc operating rule, not independently reviewed CDC-authored
semantic conclusions. No native expected identity, meaning, membership
acceptance, requiredness or authority claim changed. Original CC artifacts
remain inspectable at b1043afe; the CC closing report is not rewritten.

## Reproduction

The original committed block passed with CC_COMMIT=b1043afe. The corrected
block passed in both CC_PRECOMMIT=1 and committed-endpoint modes before CDC
closure/new-slice files were added. Thus the precommit test inspected exactly
the original five changed files, with the corrected replay among them, not
the later expanded CDC contribution.

Tools observed: Bash 5.3.9, jq 1.6, ripgrep 15.2.0; Git, shasum, awk and
standard shell tools read local inputs. No source/package/install, extraction,
parser or helper implementation was needed.

| Check | Observed result and limit |
| --- | --- |
| Historical plan/ledger/coverage | All three published hashes match Git bytes at 753bacb0 |
| Historical versus live | All three live hashes differ; historical bytes still reproduce |
| Frozen inventory | Published afc1985f... digest matches |
| Legacy native lookups | Actual Accent Types and Behaviour arrays equal independently authored expectations |
| Reordered keys | Structural comparison passes |
| CQ tuple and parent states | Expected id/path/revision 1; missing answer_criteria, null memory_admission_ref, empty preservation_refs retained |
| Wrong digest | Corrected actual hash comparator rejects with status 1 |
| Invalid Git path | Status 128, empty stdout and nonempty stderr |
| Wrong question | Actual empty result from successful command, not a tool error |
| Wrong CQ ID/revision | Native tuple rejects each expectation with comparison status 1 |
| Missing inventory | jq status 2, empty stdout and nonempty stderr |
| Wrapper probes | Missing Git path rejects with 128; document without a replay block rejects with 1 |
| Scope | Exactly five original CC files; required trailers; source and protected history unchanged |

For corrected replay use the wrapper in worked-replay.md, pinning
REPLAY_COMMIT to this CDC commit and keeping CC_COMMIT=b1043afe. Before the
CDC commit exists, extracting the corrected working-tree fenced block with
that CC_COMMIT is an explicitly live recipe test, not a claim that the
corrected code exists at the CC endpoint.

The original endpoint diff preserves Arc01, both coverage registers and all
accepted Slice01/02/12 packets. CDC's later current-register change assigns
eight pairs only; accepted/remaining arrays, accepted additions and the
frozen transition stay unchanged.

After opening Slice13, the corrected live recipe passed again with
CC_COMMIT=b1043afe: historical opening counts remain 180/375/0 and live counts
are 180/375/8 (367 outside). The plan-derived exact eight-pair assignment,
unchanged accepted/remaining arrays and accepted additions, protected-path
diff, new prompt shell syntax and whitespace checks all passed. This is a
later status observation, not new semantic acceptance.

## Row Walk

- S3-1 done: roots, identity, revision, original/copy lineage, roles,
  expected/observed and interpretation are explicitly distinct.
- S3-2 done: pinned Git bytes reproduce; corrected digest and Git-input
  controls reject by different mechanisms.
- S3-3 done: native JSON observations and all requested controls reproduce;
  no lookup is promoted to answer adequacy.
- S3-4 done: literal route, original exact scope, precommit/committed modes
  and fail-closed entrypoint checked; CDC corrections attributed above.
- S3-5 done: all eight proposed next pairs exist in the remaining register;
  provenance and cross-owner obligations survive in the revised roadmap.

## Bubble-Up And What Worked

All three artifacts and the closing report are in their declared homes.
There are no missing deliverables or newly accepted semantic pairs. The
bounded two-case packet kept observations and limits readable; native query
controls needed no semantic repair. This is not a causal model comparison.

The arc plan changes before advancement: the handoff's proposed first unit
opens as canonical Slice13, actor and actor.id across claim, competency-question,
concept-card and extraction-run. No lettered batch hierarchy is introduced.
Slice14 inherits the remaining original provenance/shared-reference work,
subject to sizing/splitting before execution. Arc06 retains all 367 unassigned
pairs, including non-provenance families. Counts remain 180 accepted / 375
remaining; eight assigned, zero newly accepted. P-15, source implementation,
real extraction/UAT and operator acceptance stay open.
