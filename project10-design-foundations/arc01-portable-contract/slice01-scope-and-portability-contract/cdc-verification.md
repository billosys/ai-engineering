# Slice01 CDC verification

Reviewer: Sofie (CDC), 2026-10-09, separate from CC's execution context.
Workflow: Two-Contributor. Reviewed CC commit
`0e0c1d0a6b9f451a9328036b0af035e5405cafa8`, against initial assignment
`3e5fc9b089c95c5ab97aa25917644a7d83895f28`, source
`dffa504e851b03b8e4746f1941068e4cc850b612`, and Project09 audit
`795ac75b7d02536e0e95252457ac3282cd17d8d8`.

## Current verdict

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
