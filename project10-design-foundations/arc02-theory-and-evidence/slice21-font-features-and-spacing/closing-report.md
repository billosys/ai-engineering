# Slice21 CC return — proposed results

**Assignment:** `cc-prompt.md`, Slice21 Font Features and Spacing. Returned for
CDC Sofie's review via the Operator relay. **This is a proposed-done report;
the four ledger statuses remain `open` pending independent review.**

## Revisions and commit scope

- Source baseline: `52bfa46332592106f9301226571d6f441df8ce2d`.
- Source commit: `dba03b611572eadb15525e814282dde67d65a9bd` on `main`, with both
  required coauthor trailers. Exact nine paths:
  - `knowledge/design/concept-cards/practical-typography/opentype-features.md`
  - `knowledge/design/concept-cards/practical-typography/kerning.md`
  - `knowledge/design/concept-cards/practical-typography/letterspacing.md`
  - `knowledge/design/concept-cards/practical-typography/ligatures.md`
  - `knowledge/design/concept-cards/practical-typography/alternate-figures.md`
  - `knowledge/design/concept-cards/practical-typography/optical-vs-metric-spacing.md`
  - `knowledge/design/guides/type.md` (only “Check candidates and fallbacks”)
  - `knowledge/design/SKILL.md` (metadata version only)
  - `knowledge/design/version-history.md` (additive 1.0.18 entry)
- Planning baseline: `e9876d8a08740694d40f66db6f0a79faf31340ee`. Planning commit
  is pending until this report is committed; it will contain only
  `artifacts/batch-record.md`, this report, and ledger Evidence/Notes cells.
- Source tree is otherwise clean; the pre-existing untracked `knowledge/lfe/`
  remains untouched. No push or publication occurred.

## Row walk

Opening rows: 4. All 4 are accounted for below. Each proposed result is CC-
attested only; CDC must inspect/reproduce the evidence before changing a status.

| Row | CC-proposed disposition | Evidence and caveats |
|---|---|---|
| S21-01 | Proposed done within the assigned correction scope. All six final bodies preserve their heading sequences and source-reference literals and carry concrete, qualified teaching. | [Batch five-dimension review](artifacts/batch-record.md#five-dimension-outcome-by-card-cc-assessment), source commit above. Prepared-page comparison does not establish original-source fidelity; no font/render/accessibility behavior was tested. |
| S21-02 | Proposed done for the bounded local relation/CQ review and guide integration, with the recorded answerability gaps preserved. All 27 typed occurrences and all 25 body statements are separately mapped. | [Typed relations](artifacts/batch-record.md#typed-relation-disposition-27-distinct-header-occurrences), [body statements](artifacts/batch-record.md#body-relation-occurrence-disposition-25-separate-statements), [CQ attempts](artifacts/batch-record.md#cq-answer-component-attempts). CQ5 and CQ11 remain unanswered by these members; CQ1 and CQ12 receive partial cohort contributions. No memberships were removed. Whole-domain composition remains open. |
| S21-03 | Proposed done for preservation checks. The current roster matches all 233 accepted index paths; exactly seven metadata scalars changed; all 227 other cards match pinned bytes; six heading/citation sequences are frozen; all 161 tracked source files are unchanged. | [Pinned data and validation record](artifacts/batch-record.md#pinned-data-queries-and-baseline-projection), exact checks detailed there. Original capture, endpoints, whole-corpus semantics and hosted views remain separate gates. |
| S21-04 | Proposed done for local version/package integration. Version 1.0.18 is present; the sequential native gates passed, followed by a fresh package build and 8/8 byte comparison. | [Gate results and package identity](artifacts/batch-record.md#validation-and-package-results). Package-path check reported zero hard failures and 596 warnings (594 unique locations; 3 explicit exceptions). The warnings were retained, not treated as hard failures. Package success is not release acceptance. |

## Validation and limits

`make help`, `make check-skills`, `make check-skill-versions`,
`make check-package-paths`, then a separate fresh `make design` all completed
successfully in that order. The version contract reported 25 source skills,
25 packages and 0 errors. The package-path gate scanned 25 zips and 402
Markdown files, with 0 hard failures, 596 warnings, 3 explicit exceptions and
798 skipped external URLs. `make check-skills` passed its description limit;
its output notes 19 descriptions above the 300-character editorial target.
The final design build reports the design description at 360 characters (one
above that editorial target); no description was changed in this assignment.

The fresh `target/skills/visual-design-system.zip` has SHA-256
`fb0398777dd4af9108c2ff8b1fe1fd226109f9244750397282837c60536a5f96`; each of
its eight Markdown members equals its corresponding committed source bytes.
Focused local-link/fragment checks passed for the two local Markdown links in
the changed guide; the six cards contain no local Markdown links. `git
diff --check`, exact path allowlist, LF/EOF and source-population checks passed.
The batch record retains earlier failed extraction/comparison attempts and
their corrections, not only the successful reruns.

No browser, assistive technology, target font, feature output, InDesign view or
hosted rendering was tested. No entire endpoint, corpus semantics, original
capture, release, push or publication is claimed. The ledger remains open for
CDC's independent review.

## Artifact inventory

- `artifacts/batch-record.md` — sole durable supporting artifact: intake,
  contract readback, exact relation/CQ projections, per-card review, validation
  outputs, recovery notes and scope limits.
- `closing-report.md` — this first-class slice return report, outside the
  supporting-artifact inventory.

## Bubble-up to Arc02

The slice delivered its assigned connected feature/spacing correction on main:
six cards now distinguish font data, feature requests, shaping and contextual
spacing; the existing packaged type method includes a scoped check; and the
fresh package matches committed source. This is the usable improvement checked
by the preservation and package evidence above. Slice21 exposed no new
dependency or scope correction requiring an Arc02 plan amendment: original
capture, broader CQ composition, and actual rendering remain with their
existing owners. CDC should confirm this conclusion during review.

Scope-as-specified versus scope-as-delivered: all nine authorized source paths
and all three authorized planning outputs are accounted for; no criteria,
statuses, plans, prompts, CDC records, registries, other guides or source
collections changed. The documented CQ gaps and validation warnings are
disclosed rather than silently dropped. No successor is opened by this return.

## Iteration01 return — 2026-10-18

Current assignment is preserved `cc-prompt-iteration01.md`, issued by planning
`ad8ebdd7a38beb83bdf245c9c2d71411df2eee0d`. This section supersedes the initial
report's current-state claims, while preserving that report as history.
Independent initial review accepted S21-02/03/04; S21-01 remains open pending
independent verification of this CC-attested F01 repair.

Source `bca347f580132b0313a9bbb29d77c980a995b8f9`, parent
`d19de06d1e79e22dac0b67b5bf2e527c048a1f73`, is on the dedicated
`codex/project10-arc02-autonomous` branch. Its sole path is
`knowledge/design/concept-cards/practical-typography/optical-vs-metric-spacing.md`;
only Example1 changed. It restores the attributed leftward/round-flat/darker-gap
explanation requested by F01. Both required coauthor trailers parse correctly.
Planning parent is `ad8ebdd7a38beb83bdf245c9c2d71411df2eee0d`; the return commit
is pending until this report is committed and contains only the existing
`artifacts/batch-record.md`, this report and ledger Evidence/Notes cells.
The direct contributor handoff carries its exact final hash; no receipt-only
follow-up commit is needed.

| Row | Current disposition / evidence |
|---|---|
| S21-01 | Remains open. F01 repair proposed complete against prepared source32–38; current full card reviewed. Independent acceptance pending. |
| S21-02 | Remains done at initial bounded scope. Unchanged relationships/CQs/guide preserve the independent local review and disclosed gaps; restored illustration supports the same spacing/texture premise. |
| S21-03 | Remains done. Fresh exact reversal/233 roster and raw-header/232 other-card/161 source/6 guide/other-input checks pass. |
| S21-04 | Remains done at local integration scope. Unbundled paragraph and unchanged package/checker inputs preserve the independent d19de06d native/package evidence; existing8/8 members still equal committed bytes. No new build. |

Detailed intake, current optical five-dimension assessment, checks, exact blob
identities, retained-evidence rationale and commit recovery are in the sole
supporting [batch record](artifacts/batch-record.md#iteration01-repair-results).
`git diff --check`, LF/EOF, exact allowed paths and local-link checks pass.
The unchanged ZIP retains the independent hash `a84faa792bddef0f920d4623b6fca604f81b328513c12b2f0693e4375a83f068`.

Scope-as-delivered equals this iteration's one source path/three planning
outputs. Main, issued prompts, reviewer record, criteria/statuses and all other
source/planning paths are untouched. No new dependency or plan change bubbles
up: CDC retains acceptance, closure and retrospective responsibility. Original
capture/fidelity, full corpus/live/global composition, actual browser/font/AT/
InDesign behavior, hosted rendering and release gates remain with their owners.
No push, merge, publication or successor was performed.
