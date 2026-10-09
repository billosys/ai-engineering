# Slice02 CDC verification

Reviewer: Sofie (CDC), separate from CC; Two-Contributor Workflow, 2026-10-09.
Candidate: `db48d8631b28ef1817dcd8c645b5a0f1e44293fb`; assignment:
`d12d32df74d9c1931d51804951dd53c04b892dda`, `cc-prompt.md`.
SOURCE: `dffa504e851b03b8e4746f1941068e4cc850b612`; accepted Slice01:
`9cc20338`, closure `1944d1ed`; shared audit: `795ac75b`.

## Current verdict

**Partial packet reviewed; Slice02 remains open.** CC did not propose completion.
S02-08 is genuinely input-blocked; S02-04 also contains unfinished accessible
work. All nine rows remain open. No Slice03 advance, original-source acceptance,
semantic acceptance or changed project scope follows from this review.
The next assignment is [iteration01](cc-prompt-iteration01.md).

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
