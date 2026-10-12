# Arc02 Slice08 CC proposed return

This is the CC return for independent CDC review, not acceptance or slice
closure. The assignment was issued by the commit opening this slice on
planning. Source baseline: `52f0b5208b538d9e1e351e22aa3e2c88e620014f`.

## Delivered source

The current source commit on `main` is
`d644db46913823eed957bb16a48d062e1a7dd71f`, tree
`a36e2923995395216982967ab2ccad7babbf4f5d`, parent
`41ebca1844de1e80cc7145e0e2d6ccc21c2864eb`. A `git pull --rebase` replayed
the initial source commit onto updated main history. The four assigned source
files at the replayed parent are byte-identical to their images at assigned
source pin `52f0b520`; the current commit still changes exactly:

- `knowledge/design/SKILL.md` — metadata version 1.0.2→1.0.3 only.
- `knowledge/design/version-history.md` — matching neutral entry, earlier
  entries retained.
- `knowledge/design/guides/design.md` — ACT-10/11/16 and specified neighbors.
- `knowledge/design/guides/foundations-of-design.md` — ACT-18/19/20/21.

The specified replacements distinguish DTCG interchange/value types from
optional token architecture and project-defined semantic names, qualify
cross-system comparisons, permit useful two-layer and local-value choices, and
limit propagation claims to consumers whose references resolve through a
changed value. The complete changed contexts and all 21 action dispositions
are in the [batch record](artifacts/batch-record.md).

## Row-by-row proposed disposition

The ledger retains all four rows as `open` for CDC review.

| Row | CC proposal | Evidence and limit |
|---|---|---|
| S08-01 | Proposed satisfied at the assigned seven-action source scope. | Seven replacements are present once each in their contexts, with bounded primary-source wording and optional architecture choices. CDC must reproduce the source review. |
| S08-02 | Proposed satisfied at the assigned 21-action and preservation scope. | The seven matches were corrected; the fourteen superseded actions were reconciled semantically. Protected colour teaching and all three entrypoint CSS examples were compared to source before the edit. CDC review remains due. |
| S08-03 | Proposed satisfied for committed source and fresh package checks. | Four source paths, metadata/history, trailers, required Make gates and eight archive-member byte matches are recorded below. The planning output commit is limited to the three authorized files and will carry both required trailers. CDC reproduction remains due. |
| S08-04 | Proposed satisfied for the specified analytic cases and accounting. | Two-layer, local-value, direct/transitive dependency and retained `button=new`, `badge=new`, `fixed=old` witness were reviewed against delivered prose. These are analytic checks, not fresh-context, browser, export or runtime evidence. |

## Gates and package identity

`make help`, `make check-skills`, `make check-skill-versions`,
`make check-package-paths`, fresh `make design`, and source/planning
`git diff --check` passed. The skill check reports 18 descriptions above its
300-character soft editorial target; `visual-design-system` is 360 characters.
The version check reports 24 source skills, 24 packages and zero errors. The
final post-rebase package-path check reports 24 ZIPs, 388 Markdown files, zero
hard failures, 596 warnings at 594 unique locations, three explicit exceptions
and 681 skipped external URLs. The pre-rebase run had 593 warnings at 592
locations. Detailed warning rows are hidden by default.

Fresh `make design` produced `target/skills/visual-design-system.zip`. All
eight actual Markdown members were individually compared byte-for-byte with
the committed source and match. Package SHA-256:
`5e2ac28a0100be3f74f4bbaebb9d53bc04581e11bdd97b2222e57aa6c759902c`.
The source commit contains the four listed paths only, with separate required
Codex and Billo AI trailers. The three planning outputs in this return are
committed together with the same trailers; no receipt-only follow-up is used.

The first version-gate attempt was blocked when sandbox policy denied creation
of its temporary `build/` directory; the approved retry passed. An overly broad
first package-member comparison included source/card Markdown not shipped in
the archive; the corrected comparison used all eight actual archive members
and passed. An initial ACT-16 exact-match candidate also included the preceding
paragraph and matched zero times; no target edit occurred until it was narrowed
to the complete specified final paragraph. The source commit was then replayed
by the observed main-history rebase; its four parent file images match the
assigned pin, and the required package gates were rerun on the rebased tree.
These recoveries and the successful checks are itemized in the batch record.

## Artifact inventory and Arc02 bubble-up

One supporting artifact was produced: [the batch record](artifacts/batch-record.md).
The existing prompt, plan, ledger and CDC records are preserved. No other
artifact, checker framework, export harness or source file was added.

This source batch supplies corrected inputs to Arc02's token and live-content
review. It does not discharge complete eight-file/233-card/five-dimension
coverage, original-source fidelity, actual fresh-context behavior,
accessibility/browser behavior, GitHub rendering, or final package/release
composition. Material Design 3 and historical Polaris source passages remain
under CDC/Operator re-entry; the bounded live-page comparison does not establish
historical fidelity or export conformance. Existing A02-02/04–08, A02-09,
A02-10, Arc04, Arc06, P10-02/04–08 and P10-11–13 ownership remains unchanged.

No slice, arc or project closure is claimed. CDC review is pending; the next
assignment and parent composition gates remain governed by their existing
records.

## Iteration01 CC proposed return — 2026-10-12

This is the I1 return for independent CDC review. The missed F01 instruction is
now implemented: `design.md` Section I is headed `Comparing Design Systems`,
matching its bounded product/generation/token-category comparisons. Source
commit `1489e76730b759f01fb1e839a18b363d8296b610` has parent
`d644db46913823eed957bb16a48d062e1a7dd71f`, tree
`6058b581fb4d4c9c25599e07fca72e635bb4b392`, and changes exactly the one
authorized path by one line. Byte comparison confirms every other byte in that
file and every other tracked live source file is unchanged. No inbound old
fragment route exists. Metadata/history remain 1.0.3.

### Row-by-row proposal

The ledger preserves CDC's current states: S08-02/03 are `done`; S08-01/04 are
`open` pending CDC review. CC proposes:

| Row | I1 proposal | Evidence and limit |
|---|---|---|
| S08-01 | Proposed satisfied | All seven accepted source corrections remain; the previously missed heading now matches the required scope. CDC must review the composed source. |
| S08-02 | Retain CDC `done` | The exact substitution leaves the initial accepted 21-action reconciliation and protected teachings byte-applicable; the batch record preserves historical action pointers and names the current heading anchor. |
| S08-03 | Retain CDC `done` | Exact one-path source commit, fresh package-path check, fresh design archive and eight actual Markdown member byte matches are recorded. Archive SHA-256: `904a19186aab75f119c463bb5e26dce10594b81ef6d60c42bc713b2e0a63f074`. |
| S08-04 | Proposed satisfied | Corrected heading, four row outcomes, one-artifact inventory, analytic cases and unchanged Arc02 owners are accounted for. These are CC proposals, not slice acceptance. |

`make help` and fresh `make design` passed. `make check-package-paths` passed on
the authorized retry: 24 ZIPs, 388 Markdown files, zero hard failures, 596
warnings at 594 unique locations, three exceptions and 681 skipped external
URLs. Its first sandbox-denied generated-write attempt is retained as failed;
the successful retry and its actual exit are recorded in the batch record. All
eight actual packaged Markdown members match committed source bytes. The
unchanged skill-description check evidence is retained from CDC's initial
review because its source inputs did not change. `git diff --check` passed on
source and this planning return.
The first planning staging/commit attempt was blocked by sandbox denial on the
planning worktree's Git index lock; no files were staged. The bounded retry is
the single three-path planning return commit.

### Artifact inventory and scope diff

One supporting artifact exists: the existing
[batch record](artifacts/batch-record.md), now appended with I1 intake,
readback, preservation proof, actual checks, package/source identities and
current pointer. No new artifact or validation machinery was created. The
issued initial prompt, I1 prompt, slice plan, initial CDC review and original
source return are preserved. This I1 correction closes the F01 heading omission
only; it does not widen the four criteria or parent assignment. S08-01/04 are
proposed only, with CDC-owned statuses unchanged pending review.

Arc02 retains its full 233-card/eight-live/five-dimension review, original-source
fidelity and input readiness, global claim/relationship/CQ reconciliation,
fresh-context and actual browser/accessibility behavior, Arc06 metadata/rendering,
and Arc04 composition/package/release gates. Earlier type/spacing/tonal and
perception claims and the other recorded T/L/Arc02/Arc04 owners remain unchanged.
No slice, arc, project, installation or publication closure is claimed.
