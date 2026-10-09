# Slice02 CDC verification

Reviewer: Sofie (CDC), separate from CC; Two-Contributor Workflow, 2026-10-09.
Candidate: `db48d8631b28ef1817dcd8c645b5a0f1e44293fb`; assignment:
`d12d32df74d9c1931d51804951dd53c04b892dda`, `cc-prompt.md`.
SOURCE: `dffa504e851b03b8e4746f1941068e4cc850b612`; accepted Slice01:
`9cc20338`, closure `1944d1ed`; shared audit: `795ac75b`.

## Current verdict

**Iteration01 partial packet reviewed; Slice02 remains open.** Current candidate
`1c0c8acf89d5f8abba61399ac1b1d394b60c74a3` executes the iteration issued at
`5a8eaccdc9902b42150afac87c0f37aba5dc2381`. F02/F03/F04 corrections are
independently reproduced. The 37 Butterick complete-read records are present
and structurally reconciled, with reading attributed to CC. F05's complete
executable checks and precise guide/input extents remain incomplete. The next
assignment is [iteration02](cc-prompt-iteration02.md), covering the 46 post cards
and that evidence gap. All nine rows remain open; original readiness remains
blocked. No Slice03 or full semantic/source-fidelity acceptance.

The following initial verdict and review remain historical at `db48d863`.
CC did not propose completion.
S02-08 is genuinely input-blocked; S02-04 also contains unfinished accessible
work. All nine rows remain open. No Slice03 advance, original-source acceptance,
semantic acceptance or changed project scope follows from this review.
The then-issued assignment was [iteration01](cc-prompt-iteration01.md).

## Independently reproduced checks

- `git show --format=full --stat db48d863` and `git diff-tree --no-commit-id
  --name-only -r db48d863`: exactly the eight CC-allowlisted paths, both required
  coauthor trailers. `git diff d12d32df db48d863 --check`: no findings.
- Parsed all 233 JSONL objects and the accepted index; path set/order/uniqueness,
  hashes and literal source/author/chapter/page/section/reference/status copies
  match. This validates copies, not original support or locator completeness.
- Reopened all 138 prepared target instances: hashes match; all inclusive spans
  fit their pinned files. All 101 article-section boundaries match the next
  same-or-higher heading when quoted headings are recognized. Thirty-seven
  Butterick paths/full-file extents resolve. Nine stored page titles differ from
  observed frontmatter spelling; see F03.
- Parsed all 161 source-register inventory rows and compared full path sets,
  sizes and SHA-256 against SOURCE: exact equality. Seventeen local Markdown
  file links resolve. SOURCE remains at its pin with no tracked design changes.
  Diff from the issued opening leaves Slice01, Project09, initial prompt,
  slice plan and author reconnaissance unchanged. Unrelated untracked source
  and planning paths remain present.
- Inspected the full prose reports/method/actions/ledger and closing report,
  all group/target/caveat projections, complete prepared `headings.md`, Brown
  opening and further-reading context, conversion report and accepted DES map.
  This was not a full read of all 83 prepared passages or semantic review.

Core replay shape, from PLANNING (temporary inline checks, no new validator):

```python
from pathlib import Path
import json, hashlib, re
S = Path('/Users/oubiwann/lab/billosys/ai-engineering')
L = Path('project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness')
B = L.parent / 'slice01-scope-and-portability-contract/artifacts/card-source-index.jsonl'
index = {r['path']: r for r in map(json.loads, B.read_text().splitlines())}
rows = list(map(json.loads, (L/'artifacts/locator-map.jsonl').read_text().splitlines()))
assert len(rows) == len(index) == 233
assert [r['card_path'] for r in rows] == sorted(index)
def heading(line):
    return re.match(r'^(#{1,6})\s+(.*)', re.sub(r'^(?:>\s*)+', '', line))
for r in rows:
    b = index[r['card_path']]
    assert r['card_sha256'] == b['sha256']
    assert r['primary_source_raw'] == {k:b['source_fields_raw'][k] for k in ('source','authors')}
    expected = {k:b['source_fields_raw'][k] for k in ('chapter','pdf_page','section')}
    expected.update({k:b[k] for k in ('source_reference_raw','source_reference_status')})
    assert r['asserted_locators_raw'] == expected
    for t in r['prepared_targets']:
        data = (S/t['path_or_uri']).read_bytes()
        assert hashlib.sha256(data).hexdigest() == t['snapshot_sha256']
        lines = data.decode().splitlines(); v = t['locator_value']
        assert 1 <= v['line_start'] <= v['line_end'] <= len(lines)
        if t['locator_kind'] == 'local-markdown-lines':
            h = heading(lines[v['line_start']-1])
            assert h and v['heading'] in h[2]
            end = next((i for i in range(v['line_start'],len(lines))
                        if (n:=heading(lines[i])) and len(n[1]) <= len(h[1])),len(lines))
            assert end == v['line_end']
```

Other checks used direct inventory table parsing and full-path group/caveat
counts. Their results above are CDC reproduction, not CC attestation. Initial
CDC heading detection omitted `>` prefixes and reported three false failures;
corrected parsing produced zero mismatches across 101 spans. A strict Butterick
title assertion stopped the first combined helper; a separate full enumeration
then found all nine spelling differences. One source-card read used PLANNING
instead of SOURCE and failed; the SOURCE read was recovered. These helper errors
do not become green checks by command exit alone.

Public metadata spot checks on 2026-10-09: [UC Press Arnheim](https://www.ucpress.edu/books/art-and-visual-perception-second-edition/epub-pdf)
identifies a second edition; [Huntington Cleland](https://www.huntington.org/collections/lib-710228)
identifies a 1937 catalog item. Neither identifies the actual cards' originals.
The issued [Tschichold publisher URL](https://www.ucpress.edu/book/9780520250123/the-new-typography)
returned only site chrome/loading through the web reader, so its edition details
were not reproduced. Other CC web observations remain attested; no files were
downloaded or source captures made.

## Findings and repair boundary

| ID | Affected rows | Finding and concrete witness |
|---|---|---|
| F01 | S02-01/04/07/09 | CC admits not reading all cited prose/context. Locator notes nevertheless say every Butterick complete page was inspected. Complete accessible passage reads and scoped receipts are required; hashes/headings are insufficient. |
| F02 | S02-02/03/05/08 | Caveat references and actions disagree. All 19 Cleland rows use `C-BOOK-ORIGINAL-ABSENT`, absent from the action table's IDs; its named Cleland edition/page IDs occur in no locator rows. One Cleland `munsell-colour-system/munsell-colour-system.md` row also incorrectly inherits web-capture caveats despite no web target. All 37 Butterick rows carry title-unresolved caveats despite reported resolution, and lack the named capture/fidelity caveats required for their empty originals. Use full card paths/raw pairs, never a shared basename, for applicability. |
| F03 | S02-02/03/04/07 | Golden Ratio literally cites the opening paragraph, but its targets start at lines 133, 172 and 358; the opening is neither mapped nor explicitly explained as unresolved. HSL notes say the secondary locator is unresolved and separately mapped in the same current row. Nine Butterick `page_title` values contain citation spelling rather than literal observed frontmatter, without recording normalization (e.g. `First-Line Indents` versus `First Line Indents`). Preserve asserted and observed values separately. |
| F04 | S02-06/09 | Method allocation omits DES-014/015/016 and places DES-009 in an Arc03 group although its primary owner is Arc02. Reconcile all 16 primary owners/cross-references against Slice01 contract §5 without changing that accepted map. |
| F05 | S02-01/07/09 | Intake says method guides were consulted without precise complete extents; most target/validation queries are described but not executable. Closing S02-03 says final comparison remains required while execution notes say it passed; readiness total omits the two secondary spans. Preserve prior issued evidence and add a precise current readback/query/result record and consistent scoped totals. |

## Row accounting and bubble-up

S02-01: partial intake, F01/F05. S02-02: reproduced populations/inventory,
unreconciled provenance/caveats, F02/F03. S02-03: reproduced raw copies/spans,
unfinished mapping and caveat accounting, F02/F03. S02-04: incomplete full
passage reads, F01/F03. S02-05: useful proposed inputs; caveat applicability
needs repair, F02. S02-06: useful five-dimension procedure; F04 remains.
S02-07: reproduced scope/preservation and selected integrity checks; affected
target/report checks remain. S02-08: external originals/capture/fidelity gate
unresolved. S02-09: honest partial return, but F01/F04/F05 prevent acceptance.
No row is closed or deferred by this review.

Assigned piece delivered: all expected artifacts, complete raw population and
useful navigation scaffolding; unavailable evidence is disclosed. Work still
owed: report/map corrections and complete prepared passage/context inspection.
Operator/source owner supplies exact originals/captures; CDC scopes any source
preparation after concrete inputs. Iteration01 bounds accessible reading to 37
Butterick pages and specific correction witnesses; all 46 post cards remain
required later in this same slice. This execution batching changes no acceptance
criterion, denominator, source authority or arc sequence. Arc/project remain open.

No browser/accessibility, package, original fidelity, full claim verification or
relationship/CQ corpus acceptance was run. CDC reproduction of structural checks
does not accept CC's unfinished semantic/context work.

Reviewer-record self-check before commit: the embedded replay above executes
successfully from PLANNING; six reviewer-owned files contain 31 resolving local
links and two resolving fragments. All nine ledger criterion/verification/
significance/origin/status fields remain identical to `db48d863`, with every row
open. Six CC artifacts and its closing report remain byte-unchanged; initial
prompt, author input, accepted Slice01 and Project09 remain protected. SOURCE
still has only its pre-existing untracked `knowledge/lfe/`; planning retains
unrelated `project12-chcd-protocol/`. Whitespace check passes. These are checks
of this review/handoff record, not independent acceptance of author planning.

## Iteration01 independent review — 2026-10-09

### Reproduced results and retained evidence

Candidate `1c0c8acf89d5f8abba61399ac1b1d394b60c74a3`, assignment `5a8eaccd`.
Inspected the exact eight-path delta, required trailers and unchanged nine-row
contract. `git diff 5a8eaccd 1c0c8acf --check` passes. SOURCE remains at `dffa504e`;
accepted Slice01, audit, parent plans, slice plan, issued prompts and prior CDC
record were unchanged by CC. Unrelated untracked paths remain untouched.

Fresh direct checks parsed **every line** of the current JSONL with `json.loads`:
233 sorted unique rows; all card hashes and raw source/author/chapter/page/section/
reference/status copies match the accepted index. No non-JSON trailing record
exists in this committed map. A filtered `rg` projection alone would not establish
that file-integrity property.

All 140 target instances have correct local SHA-256 and valid inclusive spans:
37 Butterick full-file targets, 101 article heading targets and two unheaded
Brown opening targets. The 101 heading ranges end at the next same-or-higher
heading with `>` prefixes recognized. Both Brown paragraph targets are line 109,
with the actual wrapper end/start at 107/111; no heading is fabricated. Literal
observed Butterick titles now match frontmatter. All 233 active caveat sets match
their full-path primary collections: Arnheim 112, Cleland 19, Tschichold 19,
shared book fidelity 150, Butterick capture/fidelity 37, post capture/fidelity 46.
The old `db48d863` caveat and omitted-opening records fail these controls.

All 37 read-table card/page associations, SHA-256, observed titles, URLs and
EOF extents reconcile with their source files and current map. The table and
context notes attest CC's complete reads; checks of identity/range cannot prove
attention or comprehension. CDC retains its own earlier full `headings.md`
inspection and freshly inspected Brown opening, CSS HSL, Oklab data qualification
and Okhsv opening witnesses. No new whole-page semantic verdict is asserted.

The method's 16 DES rows equal the complete accepted Slice01 §5 table, including
owners, cross-references, outcomes and checks. Seventeen local Markdown file
links resolve; outputs have final newlines. Prior 161-file inventory reproduction
is retained at `db48d863`: the inventory rows and pinned SOURCE bytes are unchanged
and no finding undermines that check. This retention is not a fresh inventory run.

The existing core replay needs a branch for the two new unheaded targets:
when `paragraph_role` is present, check exact one-line span/text and recorded
wrapper boundaries, rather than asserting a heading. The historical code remains
scoped to `db48d863`; it is not evidence of a current failure or a universal parser.

### Finding dispositions and remaining work

- F01: the 37-page batch is delivered as CC-attested complete reading with
  independently checked identity/coverage. All 46 post-card passage reads remain.
- F02: corrected caveat membership/definitions independently reproduced.
- F03: opening/HSL/observed-title corrections independently reproduced; prepared
  navigation only. Source identity/fidelity remain blocked.
- F04: complete DES allocation independently reproduced.
- F05: partial. Execution notes still describe most comparisons without complete
  executable commands/code and dependencies. Iteration intake lacks per-guide
  delivered extents from the required manifest. The failed “non-JSON trailing
  line” receipt does not name its exact input/command; current strict parsing
  succeeds. Preserve that failure and clarify its scope instead of filtering
  unknown records away or inventing historical receipts.

S02-01 remains open for precise current intake/readback; S02-02/03/05 have useful
reproduced accounting but incomplete source/context handoff; S02-04 awaits 46
post cards; S02-06's method allocation is corrected without semantic execution;
S02-07's affected structural checks pass, with evidence-log completion pending;
S02-08 remains input-blocked; S02-09 preserves partial status and pending work.
No criterion is weakened and no row is closed or deferred.

### Bubble-up and author reconnaissance for iteration02

The remaining local mapping work concerns four prepared articles, 46 primary
cards and 103 target instances (101 primary, two secondary). Overlapping target
spans merge to approximately 206,049 characters; all four files together contain
251,261 characters. Read each full prepared article once with complete bounded
delivery, then associate each card/reference/target to its inspected passage and
context. This preserves unheaded text and qualifications outside mapped headings
without repeating the same prose per card. It does not inspect originals or
perform all 233 claim reviews.

Direct witnesses informed the assignment: Brown line 109 uses an antecedent-
dependent opening; CSS-Tricks HSL 97–125 contains a historical attribution plus
code/figures; Oklab 251–255 qualifies its chart-data comparison; Okhsv 1–22 points
to an interactive companion. Record missing context/media/dynamic evidence as
scoped limitations, without rewriting source or deciding domain truth from a
navigation pass. Document-extraction's structure/locator contracts require this
context; concept-cards distinguishes source text from warranted claims.

Preparation/fidelity mutations need a separate concrete assignment once exact
book editions/capture inputs and destinations are identified. No such mutation
is authorized by iteration02, and unavailable inputs cannot advance Slice03.
The full corpus/five dimensions, C&B removal decision and release gates remain.

Current target replay, run from PLANNING; complements the raw-copy and table
checks above without changing the historical replay:

```python
from pathlib import Path
import json, re, hashlib
S = Path('/Users/oubiwann/lab/billosys/ai-engineering')
L = Path('project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness')
rows = list(map(json.loads, (L/'artifacts/locator-map.jsonl').read_text().splitlines()))
def heading(line):
    return re.match(r'^(#{1,6})\s+(.*)', re.sub(r'^(?:>\s*)+', '', line))
counts = [0, 0, 0]
for r in rows:
    for t in r['prepared_targets']:
        data = (S/t['path_or_uri']).read_bytes(); lines = data.decode().splitlines()
        v = t['locator_value']
        assert hashlib.sha256(data).hexdigest() == t['snapshot_sha256']
        assert 1 <= v['line_start'] <= v['line_end'] <= len(lines)
        if t['locator_kind'] == 'local-markdown-document':
            counts[0] += 1
            assert v['line_start'] == 1 and v['line_end'] == len(lines)
            assert v['page_title'] == re.search(r'^title: "(.*)"$', data.decode(), re.M)[1]
        elif 'paragraph_role' in v:
            counts[2] += 1
            assert v['line_start'] == v['line_end'] == 109
            assert lines[108].startswith('This and other meaningful ratios')
            assert not heading(lines[108])
            assert lines[106] == '</div>' and lines[110].startswith('<div class="illustration')
        else:
            counts[1] += 1; h = heading(lines[v['line_start']-1])
            assert h and v['heading'] in h[2]
            end = next((i for i in range(v['line_start'], len(lines))
                        if (n:=heading(lines[i])) and len(n[1]) <= len(h[1])), len(lines))
            assert end == v['line_end']
assert counts == [37, 101, 2]
```

Review/handoff self-check: six reviewer files, 33 local links and four fragments
resolve; nine criterion/verification/significance/origin/status rows remain
unchanged/open; CC outputs and both prior prompts are unchanged. An attempted
record patch used a non-matching context and made no edit; the corrected append
is validated separately. The committed-tree scope/whitespace check is required
after the review commit; these author checks are not independent plan acceptance.
