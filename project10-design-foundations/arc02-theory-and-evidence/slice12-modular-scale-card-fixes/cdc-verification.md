# Slice12 — CDC independent review

## Initial return review — 2026-10-14

Reviewer: CDC Sofie, separate from CC implementation; Two-Contributor Workflow.
Operator relayed CC's return. Reviewed the initial [assignment](cc-prompt.md) at
issue `ff87331d4d8b2858203ba4fb98fe7d3100e8df49`, source candidate
`fd876e7ca906ef350a051ad2c17196064fe43147` (parent
`fce72353178c4cb8e742268e7715d70050ebc397`) and planning return
`0631c98ac118e918fed8f68a5b333685f765e24e` (direct child of issue).
Source implementation was not changed by CDC. CC's records remain proposed
evidence, not copied acceptance. Current verdict: **Slice12 stays open**;
S12-04 is independently done for this candidate's integration/check scope;
S12-01/02/03 need the [Iteration01 assignment](cc-prompt-iteration01.md).

## Reproduced evidence

- Inspected all three complete revised cards, their original teaching headings
  and bibliography, the source diff, version/history diff, initial contract,
  ledger and full return records. Read Brown's pinned prepared identity lines
  1–30 and article 109–356, including CSS, contrary improvisation, font failure
  and conclusion. Prepared SHA-256 is
  `6b63c1ca5bf9d2d92ebb0f8cda8bf05ecd2fffdabf3d068e496b42c2794f33b9`.
  This reproduces a prepared-source comparison, not historical fidelity.
- Independently extracted the six prescribed replacements from the **issued
  prompt blob**, parsed old/new YAML with duplicate-key rejection and recursive
  type/key/list-order comparison. Exactly those six scalar values differ;
  references and ordered teaching headings match. Relations, original CQs,
  identities, nested aliases and confidence remain unchanged.
- Git tree/object comparison: same 233 paths, exactly three changed cards and
  230 equal blobs; all 161 source files and the guide tree are exact. Source
  commit contains exactly the five authorized paths, planning return exactly
  three; parents, separate co-author trailers and both commit whitespace checks
  pass. Main retains only the pre-existing untracked `knowledge/lfe/`.
- Fraction `809/500`, exact base/exponent calculation, Decimal precision 50,
  half-even three-place rounding reproduce **two seven-value sequences**:
  base10 `2.361,3.820,6.180,10.000,16.180,26.179,42.358`;
  base18 `4.249,6.876,11.125,18.000,29.124,47.123,76.244`.
  Source-reported `3.819/2.360` remain distinctly attributed. The bases10/15,
  ratio2 merge gives adjacent `3/2,4/3,3/2,4/3,3/2`; bases10/20 give a geometric
  duplicate-free merge. Neither blanket merge claim is true.
- Current/corrected whole/header/body hashes and lengths reproduce the batch
  table using bytes through the closing delimiter's LF for the header. Current
  body counts are 11454,10673,8258 bytes respectively. Historical bridge has a
  different accepted offset convention; that must remain separately named.
- All required Make gates executed independently: help, skill descriptions,
  version contract, package paths, then a separate fresh design build. Passed:
  24 source skills/24 packages, zero version errors; package paths zero hard
  failures, 596 warnings, three exceptions and 681 external URLs skipped.
  The 18 soft description notices remain. Fresh archive's eight Markdown
  members equal candidate source; cards are not members. Fresh SHA-256
  `e3956535141997ddcce73ee0d6e69e9c9e044945f047456b9a976fc36d154069`
  differs from CC's build identity because archive timestamps are regenerated;
  member equality is the reproduced content check. No browser, hosted,
  installation, push, publication or original-fidelity check was performed.

Temporary one-off review helpers are not deliverables. A Ruby ternary spacing
syntax error was repaired before the successful metadata check. An initial
descending-ratio witness mixed floats with Fraction; it was rerun with exact
Fractions and passed. A guessed concept-cards guide filename failed; the actual
skill route `guides/06-graph-cq.md` was loaded. An early log inspection preceded
build completion; the running process was subsequently awaited and final logs
and archive inspected. None of these failed attempts count as passed evidence.

## Findings

### F01 — Remaining teaching contradictions and unstated ratio conditions

At source `fd876e7c`, `scale-ratio.md:111` still says “no scale exists without
it,” contrary to its own false-premise CQ answer and the contextual live guide.
The batch's relationship row incorrectly says that body already excludes this
universal. Its recognition step at line83 divides larger by smaller although
its general formula is not restricted to ascending strands: the indexed sequence
10,5,2.5 has ratio1/2 but this test reports2. Step-spacing line72 also requires
an ascending-ratio condition. The cards' authored formulas need explicit positive
base/ratio domains (zero ratio cannot support negative exponents).

The ratio card's required culture/history selection step (line77) is still
stronger than Brown's contextual example; its Related labels present1.618 and
1.333 without approximation qualifications. The construction card's historical
note at line101 states an inversion of conventional workflow as a general fact
rather than Brown's historical position. These are substantive repeated-scope
issues within the assigned full-body correction, not requests for a new theory
investigation. Repair these clauses and their affected evidence/CQ/edge joins;
keep correct examples, preserved questions, mappings and unresolved endpoints.

### F02 — Source-support joins target unrelated lines

The teaching-section table claims two-strand evidence at146–148, scale uses
151–152 and typeface-first evidence at153–155. Actual pinned text at those
reported locations is the ascending/descending arithmetic list. Correct source
joins are two-strand alternatives **156**, applications **166**, typeface-first
**168–170**; source lists144–154; construction/example174–188; workflow contrast
338–350. Other larger enclosing ranges may remain where coverage is accurate.
The correct hash and broad section span do not repair a false clause locator.
Re-read and correct the asserted joins, preserving the initial receipt as history.

### F03 — Historical bridge conflates source and planning revisions

`git show c4cc7427:<Arc06 Slice02 batch-results path>` fails: this is a main
source commit, not the planning artifact revision. The accepted bridge is at
planning **`5020db5296d58e4c43988494b9ca806423f60309`**, SHA-256
`8121246fe4d4010942ca48fc30779156b5a09841868e8e33fd7b9a5487c41d01`,
byte-equal to the bridge inherited by the present planning candidate. Source
`c4cc74279ac845003b0c80f55907981241c58a99` remains the normalized source
revision inside that bridge. Exact row mapping: construction158, modular159,
ratio174. Structured `sentinel_deltas.current_to_final` reports respectively
one (`contrasts_with`), three (`prerequisites/extends/contrasts_with`), and three
normalizations. Thus all three headers were normalized; bodies were preserved
at that phase. The batch's “only” statement hides the other headers' changes.
Correct the reference and accounting while retaining historical raw/current/
normalized/Unicode identities and the two body-offset conventions.

Incidental receipt errors can be corrected in the same return, without extra
criteria: batch preparation-parent hash lacks its final `5`; “six displayed
sequences” should name the actual two seven-value sequences and distinct merge
witnesses. These do not independently justify another iteration.

## Four-row accounting and bubble-up

| Row | CDC disposition | Evidence / remaining work |
|---|---|---|
| S12-01 | open | Complete cards were read, but F01's missed clauses and F02's false support joins undermine the claimed coverage/consistency outcomes. |
| S12-02 | open | Main arithmetic and six leaves pass; F01 leaves repeated scope and ratio-direction defects in teaching. |
| S12-03 | open | Current preservation, exact six leaves and current hashes pass; F03's historical revision/normalization account is inaccurate. |
| S12-04 | done | Reproduced current candidate integration, owning version/history, exact commit scopes, required gates and fresh eight-member equality; unbundled/hosted/fidelity/release limits are honest. Affected integration checks must be fresh for the refinement. |

Four opening rows retained: one done, three open, no deferrals or no-ops.
One supporting artifact, `artifacts/batch-record.md`, matches actual output.
Source corrections are usable but this slice has not met its complete contract.
The next assignment is a correction inside Slice12, not a new evidence-only
slice. Parent scope and all thirteen/ten criteria are unchanged. Original-fidelity
inputs, 230 other card reviews, missing/external endpoint warrant, full live/global
review, actual accessibility behavior and affected final hosted/package/release
proof remain with their existing owners. No Slice13 or arc closure follows.

Planning handoff checks pass across six changed/new files: 53 local links and
four fragments resolve, LF/EOF and whitespace checks pass. The four criterion
texts/verification contracts are unchanged; only S12-04 becomes done. Original
prompt, CC batch/closing report and both parent ledgers are byte-exact to the
reviewed planning return. Source remains atfd876e7c with no tracked CDC edits.


## Iteration01 independent review — 2026-10-14

Current verdict: **three done, S12-02 open**. Reviewed source
`a05550386eefe021140a55e110a1868dd978f893`, direct child of initial source
`fd876e7ca906ef350a051ad2c17196064fe43147`, and planning return
`f142e9172a1b7d90f3c99f6681214183bd5d9a8c`, direct child of issuing
`cdf0dc0158593e6c62e3295bb59950ac629b63e7`. Assignment:
[Iteration01](cc-prompt-iteration01.md). CDC authored no source repair.

The scoped three-card source diff and three-output planning diff, actual
parents, trailers and both commit whitespace checks pass. All three metadata
prefixes are byte-exact tofd876e7c; all233 paths remain, exactly three changed
and230 unchanged. Original bibliography and teaching sections survive. Source,
guide, owning entrypoint/history and Makefile objects are unchanged. Retain the
initial independent complete-card/source/math checks where this delta cannot
alter them; inspect the changed clauses and their evidence freshly. The entire
ratio card was read again, including the remaining Related label below.

F01's positive-domain, indexed-direction, exact-versus-rounded, contextual
selection, scope and historical-workflow changes pass. Fresh exact Fraction
witnesses reproduce indexed ratios1/2,2 and1; source output6.180/3.819/2.360
and independent47.123/11.125 remain distinct. F02 corrected locators156,166,
168–170,144–154,174–188 and338–350 match inspected pinned source passages;
initial wrong joins remain expressly superseded. F03 now identifies the actual
planning artifact5020db52 (SHA8121246fe4d4010942ca48fc30779156b5a09841868e8e33fd7b9a5487c41d01)
and normalized sourcec4cc7427. Independently selected rows158/159/174 reproduce
one/three/three sentinel changes and exact historical body equality/hashes at
the stated LF-inclusive offsets. Current whole/header/body hashes and counts
match the refinement table. The initial suffix/count mistakes are superseded.

Retain S12-04's independent Make checks atfd876e7c: every relevant source/
package input is unchanged by this body-only diff. Independently inspected the
present ZIP: all eight Markdown members equal current source, and no cards
are members. CC additionally attests fresh gates; this record does not relabel
those executions as CDC runs. The previously reproduced two seven-value numeric
sequences and merge controls remain valid; their model and examples are intact.
No new original fidelity, hosted, browser/AT, installation or publication check.

### F04 — One prescribed Related label was not repaired

At current `scale-ratio.md:115`, the old label remains:
“Golden ratio — One specific, historically prominent scale ratio (1.618).”
Iteration01 repair2 explicitly required the Related labels to identify1.618
as an approximation toφ. The card's surrounding definitions now qualify this
correctly, so this is a missed local repair rather than an overturned numerical
analysis. Replace only that one sentence using
[Iteration02](cc-prompt-iteration02.md); retain all other accepted changes.
No broad research or package replay is needed for this unbundled one-line fix.
The initial explicit replacement/list check missed this clause; the new prompt
supplies the literal old/new line and requires whole-file reverse comparison.

Incidental wording in the batch's preservation paragraph calls the six prior
metadata changes “empty-list” corrections. They are the six **semantic scalar**
changes from the initial prompt; the seven Arc06 sentinel changes are a separate
historical transformation. This distinction is reproduced above and can be
clarified in the same return; it does not create another criterion or blocker.

| Row | Current CDC disposition | Independent result |
|---|---|---|
| S12-01 | done | Complete available-evidence three-card review and corrected five-dimension/support/edge/CQ accounting; remaining F04 explicitly identified, not hidden. Original fidelity/empirical/endpoint gaps remain open at parent owners. |
| S12-02 | open | All other corrections pass; F04's required local approximation label remains unchanged. |
| S12-03 | done | Exact prefixes, unaffected corpus/source/live payloads, actual historical bridge/sentinels and corrected revision-aware hashes reproduce. |
| S12-04 | done | Retained independent integration/gates with exact input applicability; fresh ZIP member comparison. Cards remain unbundled and unhosted here. |

Four criteria retained, three done/one open; no deferrals or no-ops. One existing
supporting artifact remains. Slice12/Arc02/Project10 stay open; broader corpus,
original fidelity, global consistency, actual behavior and final-revision hosted/
release obligations are not accepted. Current assignment is Iteration02 for the
one missed line, with the same three planning return homes. Parent dispositions
and issued prompts remain unchanged; no Slice13 is opened before Slice12 closes.
