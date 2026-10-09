# Slice01 CDC verification

Reviewer: Sofie (CDC), 2026-10-09, separate from CC's execution context.
Workflow: Two-Contributor. Reviewed CC commit
`0e0c1d0a6b9f451a9328036b0af035e5405cafa8`, against initial assignment
`3e5fc9b089c95c5ab97aa25917644a7d83895f28`, source
`dffa504e851b03b8e4746f1941068e4cc850b612`, and Project09 audit
`795ac75b7d02536e0e95252457ac3282cd17d8d8`.

## Current verdict — iteration01 review, 2026-10-09

**Changes requested; Slice01 remains open.** Reviewed CC correction commit
`7000ff4df723dcf00728d1507ad63a118566651e` against issued iteration01 at
`fa0b2ad43527b8a1973c4848f291b82051aebc4c`. The two initial findings are
corrected. Fresh replay found one candidate-table transcription error and three
heading-fragment mismatches. [Iteration02](cc-prompt-iteration02.md) limits the
remaining correction to execution notes, closing report and ledger. All seven
rows remain open; no source acquisition or semantic review is added to Slice01.

## Initial verdict — initial CC review, 2026-10-09

**Changes requested; Slice01 remains open.** Two bounded evidence corrections
are required under [iteration01](cc-prompt-iteration01.md). No ledger row is
closed by this review. The inventory, contract proposal and finding allocation
substantially satisfy the assignment; this verdict does not require source
acquisition, a corpus rewrite, or semantic acceptance in Slice01.

## Findings

### CDC-S01-01 — Source membership predicate does not select its population

Criterion: S01-03, with a consequent reporting correction under S01-07.
Evidence: [source-readiness](artifacts/source-readiness.md#source-identity-groups),
lines 9–12 and its table. The advertised exact predicate compares raw index
values with display titles/authors. Raw values preserve YAML quote characters
and, for Ottosson, literal Unicode escapes. The table omits those quote
characters and renders an interpreted author name. Literal comparisons against
the displayed strings return zero matches for every group, rather than the
reported 112/19/19/37/12/10/13/11.

The underlying index and reported populations are correct. This is a
reproducibility defect in the report, not evidence of missing cards or incorrect
source availability. Add the eight lossless raw identity pairs and executable
membership expressions as specified in iteration01; preserve the index.

### CDC-S01-02 — Intake and exact-query receipts need completion

Criterion: S01-01 and the prompt's exact-query/results requirements, with a
consequent reporting correction under S01-07.
Evidence: [execution notes](artifacts/execution-notes.md), lines 22–24 identify
a 187-line required-full audit but record inspected ranges 1–98 and 99–186.
Line 187 contains the audit's acceptance and administrative-relocation limits.
The recorded extents do not establish a complete read. This is not a claim that
CC necessarily failed to read that line: resolve the receipt with a fresh actual
read, retaining the original observation rather than inventing past coverage.

The population section gives the exact tree command, but field/body extraction,
the second-pass comparison, and mapped-content searches are described as
algorithms rather than retained executable query text. The initial prompt
explicitly requires exact queries/results. Preserve those descriptions and add
the actual compact queries used on a corrective pass, including populations,
results and limitations. No maintained validator or transcript dump is needed.

## Independent evidence and row assessment

| Row | CDC observation | Disposition |
|---|---|---|
| S01-01 | Pins/readback are consistent; full-reading receipt and exact queries need the correction above | Open; CDC-S01-02 |
| S01-02 | Independently reconstructed all 402 manifest rows and all 233 index objects from source bytes; zero discrepancies | Reproduced pass; retained evidence, row stays open pending slice acceptance |
| S01-03 | Eight raw identity groups and counts reproduced; three missing book originals affect 150 cards; prepared holdings and caveats agree with designated tree | Open; CDC-S01-01 |
| S01-04 | Binding/proposed distinctions, ten profile inputs, seven principle dispositions and all five cases preserve portable scope and contextual craft | Review pass as a proposal; no teaching wording adopted here |
| S01-05 | All eight live files and DES-001–016 have accountable downstream treatment | Review pass; findings remain unclosed downstream |
| S01-06 | Exact seven-file CC allowlist, preserved source/audit bytes and initial prompt, valid local file targets, and clean whitespace check reproduced | Reproduced pass; unrelated work excluded |
| S01-07 | Row walk, limits, source owners and handoff are present; completion statements must reflect corrected receipts/predicates | Open pending corrective report and independent review |

The complete manifest comparison covered exact ordered paths, scopes, SHA-256,
byte sizes, pinned Git blobs and current working bytes. The independent index
reconstruction covered collection, hash, all eight literal field lists,
source-reference status and unchanged body spans through the next level-one
heading. Correct counts alone were not used as proof.

Raw source/author grouping reproduced Arnheim 112, Cleland 19, Tschichold 19,
Butterick 37, Drasner 12, Brown 10, and Ottosson's two articles 13 and 11.
The normalized-display comparison was a negative control: all eight populations
became zero. Local holdings comprise 160 prepared Markdown files and one
conversion report. Identifying passages/report support availability only;
original fidelity, edition/page mapping and all-card semantics remain unassessed.

Preservation checks used `git diff-tree` for CC's exact output paths and trailers,
`git show` for pinned input bytes, current Git statuses, and planning
`git diff --check` (exit 0). Source HEAD still equals the pin; pre-existing
untracked `knowledge/lfe/` remains. Planning now also has unrelated untracked
`project12-chcd-protocol/`; CC's clean-at-completion observation is historical.
No unrelated files were edited or staged. All resolved local Markdown file
targets were checked; CDC did not independently reproduce CC's heading-anchor
check in this initial pass.

The subsequent review/handoff integrity check resolved all 34 local links and
anchors in the six CDC-owned records, confirmed the six unmodified CC output
files still equal `0e0c1d0a`, confirmed the initial prompt equals its issued
commit, and counted all seven ledger rows still open. Only the ledger received
an added CDC status note; its criteria and row evidence were preserved.

One bounded read command used the source working directory for a planning-only
report path and exited 1; it was rerun from planning and succeeded. This did not
affect the successful population comparisons. No source/package build, browser,
assistive-technology, acquisition or semantic-corpus check was run by CDC.

## Correction boundary and next review

CC owns the three corrected reports plus ledger evidence notes. CDC has changed
only review/handoff records and current assignment pointers. Preserve the seven
original CC outputs in Git history and the issued initial prompt byte-for-byte.
Source acquisition and review-method readiness remain Slice02 work; Slice02
does not open until Slice01 acceptance. No project/arc scope change or new
Operator decision is required by these findings.

After CC returns iteration01, compare its exact diff and rerun affected
predicates, reading receipts and report consistency. Retain the reproduced
inventory/contract evidence only if their exact inputs and criteria remain
unchanged. Record the follow-up review here without erasing this verdict.

## Iteration01 independent replay — 2026-10-09

CDC replayed the four inspected Python blocks in execution notes together from
SOURCE, extracting complete fenced blocks with
`re.findall(r'^```python\n(.*?)^```$', notes, re.S | re.M)` and running the
concatenated text with `python3 -c`. Exit 0: the 402-file byte/hash/blob check,
233-card literal field/body check, raw membership and display negative control
passed. Four post searches returned all True; 37 Butterick candidate rows were
printed. Captured stdout SHA-256:
`167d3ac140eddfad74ccbfd63775be3575eac8f70fc7af10bf2bc36ce3de5974`.

Independent additional comparisons parsed the report's actual JSON and table
keys, checked each declared count, and counted one membership for every card:
eight groups, union 233, no duplicate/omitted membership. CDC-S01-01 is corrected.
The initial notes/report remain prefixes of their amended versions. The fresh
187-line audit receipt is explicit and consistent with the pinned file; complete
query text is now executable. CDC-S01-02's missing receipt/query-text defect is
corrected. Reading remains CC attestation supported by the coherent readback;
hashes and this replay do not establish attention or semantic understanding.

### CDC-S01-03 — One candidate set differs despite the correct count

The `headings` row of execution notes lists 23 candidate basenames including
`summary-of-key-rules`, but the recorded query yields 23 including
`text-formatting` instead. Direct source inspection confirms `headings` occurs
in `text-formatting.md` and does not occur in `summary-of-key-rules.md`.
CDC compared all 37 recorded candidate **sets**, not just counts: this is the
only mismatch; the other 36 sets agree. All 37 remain ambiguous, with 2–42
candidates; no validated locator follows. Correct the row and record the
transcription error. A correct denominator cannot repair an incorrect witness.
Affected evidence: S01-01/03/07 exact-query/results and handoff accuracy.

### CDC-S01-04 — Three section fragments do not match their headings

The two iteration01 headings contain a spaced em dash. Removing punctuation
and replacing each space with a hyphen yields
`iteration01-corrective-pass--2026-10-09` and
`iteration01-corrective-addendum--proposed-done`, while three links use single
hyphens. Two are in the ledger and one is in the closing report. The current
25-link/19-fragment population has zero missing files but three unmatched
fragments. This contradicts the claimed zero unresolved anchors.
The check follows [GitHub's section-link rules](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links)
and the [slugger implementation](https://github.com/Flet/github-slugger/blob/master/index.js),
which replaces each space without collapsing consecutive hyphens. Remove the
spaced em dashes from those two headings under iteration02's exact recipe;
the existing link fragments will then match. Affected evidence: S01-06/07.

### Preservation, evidence retention and complete row accounting

Exact diff from issued iteration01 to `7000ff4d`: the four authorized files,
both required trailers. Eight immutable slice files match the issued commit:
manifest, index, contract, reconnaissance, both issued prompts, slice plan and
initial CDC record. Both Project09 input files match `795ac75b`; the initial
notes and closing-report history were retained. Four changed files have final
newlines and no trailing whitespace. Commit-delta whitespace check passes.
Source remains at `dffa504e`; unrelated untracked source/planning directories
remain untouched.

| Row | Iteration01 CDC result | Current disposition |
|---|---|---|
| S01-01 | Fresh complete receipt and executable queries pass; one reported candidate witness differs | Open; CDC-S01-03 |
| S01-02 | Fresh documented population/index replay passes; prior stronger exact-order/scope evidence retained | Open pending final slice acceptance |
| S01-03 | Raw identities, declared/display counts and designated-tree gaps pass; one candidate-table cell needs correction | Open; CDC-S01-03 |
| S01-04 | Contract bytes and acceptance criteria unchanged; initial independent proposal/case review retained | Open pending final slice acceptance; no normative adoption |
| S01-05 | Map bytes, inputs and criteria unchanged; initial eight-file/all-16-finding review retained | Open pending final slice acceptance |
| S01-06 | Four-path scope, immutable inputs and whitespace pass; three fragments fail | Open; CDC-S01-04 |
| S01-07 | All seven rows and limits retained; current evidence/report must reflect the two remaining defects | Open; iteration02 |

Retained initial evidence keeps its original revision/date above. Exact input
comparisons establish its continuing applicability; no delta changes the
manifest/index, portable contract, map or their criteria. Live-state preservation
checks and affected queries were executed now. No package, browser, acquisition,
assistive-technology or semantic-corpus check was run.

Reviewer attempts: the first fenced-block extractor mistakenly stopped at a
triple-backtick string inside a Python regex and produced a SyntaxError; anchored
fence extraction resolved it and all four blocks passed. The first table check
failed on `headings`; a set comparison ruled out presentation-order differences
and confirmed the actual witness substitution. The fragment checker failed on
the three links above. One attempted GitHub documentation URL was unavailable;
the canonical section-link documentation and slugger source were accessible.
No final check failure is represented as a pass.

### Bubble-up to the arc

The packet delivers the inventory, availability assessment, proposed portability
contract and change map assigned to Slice01; the remaining defects are bounded
report integrity issues. All original rows/artifacts are present, with no scope
reduction or semantic-acceptance claim. The missing 150 book originals, Butterick
locator ambiguity and web-capture identity needs stay with planned Slice02;
principle/configuration adoption stays with Slice03. No structural arc-plan
amendment or new Operator decision is needed. Slice02 remains unopened pending
Slice01 acceptance. Update routine current-assignment pointers only.
