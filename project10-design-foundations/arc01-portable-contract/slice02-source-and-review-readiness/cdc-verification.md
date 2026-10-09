# Slice02 CDC verification

Reviewer: Sofie (CDC), separate from CC; Two-Contributor Workflow, 2026-10-09.
Candidate: `db48d8631b28ef1817dcd8c645b5a0f1e44293fb`; assignment:
`d12d32df74d9c1931d51804951dd53c04b892dda`, `cc-prompt.md`.
SOURCE: `dffa504e851b03b8e4746f1941068e4cc850b612`; accepted Slice01:
`9cc20338`, closure `1944d1ed`; shared audit: `795ac75b`.

## Current verdict

**Iteration04 accepted for local criteria; eight of nine rows done, Slice02 open.**
Candidate `759ce2dd116a4cfe03b72d43fd2791f48486251c`, direct child of issue
`83db00fed56a8528dfa151d9bef755b9873c6a04`, resolves the remaining prepared
join/role, receipt and checker findings. CDC independently accepts S02-01/02/04/
07/09; S02-03/05/06 retain their earlier acceptance. S02-08 alone remains open,
input-blocked by original editions/page bases and immutable web capture/lineage/
fidelity evidence. No Slice03, original fidelity or full semantic acceptance.
[Iteration04 review](#iteration04-independent-review--2026-10-09) is the current
verdict; prior reviews and issued prompts remain historical. No further local
correction is assigned. Source-input intake precedes any separately authorized
preparation assignment; Expedited Mode remains enabled within that gate.

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


## Iteration02 independent review — 2026-10-09

Reviewer: Sofie (CDC), separate from CC. Candidate `bf02e9709371a1ce0306f8f52d3d2a09c75dc7e9`;
assignment `496c810ad251afc3b0f670420028884a9e1cc945`. SOURCE remains
`dffa504e851b03b8e4746f1941068e4cc850b612`; accepted Slice01 and audit pins unchanged.
This is independent bounded review, not independent reading of all four articles
or any 233-card semantic acceptance. Prior reviews above remain historical.

### Reproduced results and limits

- Commit/path review: exactly seven authorized planning files, both required
  trailers; `git diff 496c810 bf02e970 --check` passes. SOURCE remains clean for
  tracked files; unrelated `knowledge/lfe/` and `project12-chcd-protocol/` remain.
- Strict parsing of every actual JSONL line: 233 unique sorted paths exactly
  equal the accepted index; every hash/literal identity/locator/reference/status
  copy matches. Exact full-path caveat membership passes for all 233 cards.
- Map delta against `496c810` is only separate line-30 targets on the two Brown
  opening cards. All previous targets/raw assertions remain unchanged.
- All 142 local target instances have correct pinned hashes and inclusive bounds:
  37 complete Butterick documents/observed titles, 101 physical heading boundaries
  (including quoted headings), four exact Brown paragraph targets. Physical
  existence/boundaries do not establish the intended cited section; see F03.
- All 46 current table paths, literal pairs, exact raw references and target
  path/hash/span associations reconcile to JSONL. Their contexts reduce to five
  distinct bodies used 12, 13, 11, 2 and 8 times. Full distinct text and all
  reference/target projections were delivered; only the Brown pair has additional
  paragraph-specific language. The generic per-article observations are useful
  shared qualifications but not conclusions for every cited passage.
- Replayed the exact two fenced Python blocks from committed execution notes.
  The first returned all eight recorded PASS lines. Its predicates do not check
  intended parents/clause coverage, and its sorted-only map assertion does not
  itself prove uniqueness; CDC's stronger checks above do. The second exited 1:
  `AssertionError` with the notes path, regex fragment `[^"\\\']+`, and
  disposition `missing` (execution-notes published checker, line 26).
  The regex inside its own fenced code was treated as a Markdown link. This is
  a replay defect, not evidence of an actual broken prose link. Independently
  skipping fenced/inline code finds 20 real local links, two fragments, all valid;
  all seven files pass EOF/no-CRLF. Do not relabel that substituted check as a
  successful replay of CC's published helper.
- The primary block rechecks exact equality of all 16 DES table rows. The method
  is unchanged. The 161-row source inventory and prior Butterick structural
  evidence are retained at earlier review scope: their inputs are unchanged,
  so no fresh inventory or whole-page reading is claimed.
- Guide extents 37–97 (output contract) and 106–186 (concept-card verification)
  cover the named sections completely. Precise receipts and executable raw-copy
  checks improve F05. Historical failed-slurp input remains explicitly unavailable;
  no retrospective transcript is invented. Reading receipts remain CC evidence.

### Remaining findings

**F01 — Partial contextual handoff (serious; S02-04/09).** The table mostly repeats
one paragraph per article for materially different cited sections. For example,
colour-contrast's 397–430 target receives the same HSL-history paragraph as colour
mixing's 41–74; the row does not record its own contrast/tools context. Oklab's
matrix/whitepoint/XYZ rows likewise share dataset caveats without a conclusion on
their particular clauses. Iteration02 explicitly required specific inspected
conclusions. Keep complete-file receipts and shared qualifications; add traceable
clause-specific results, sharing identical clause results across full card paths.
This is not a request to perform correctness review or re-read every file.

**F03 — Matching headings omit intended hierarchy and complete clauses
(correctness-grade; S02-03/04).** `chroma-vs-saturation.md` and `hsl.md` explicitly
cite HSL under “Color spaces for color picking”, whose parent span is 104–298.
Their 943–1136 HSL target is under “Source Code” (772–EOF), describing conversion
to Okhsl (945). `hsv.md` similarly includes 840–942 under Source Code, describing
Okhsv (842), as well as its intended 112–142 theory section. These are valid
physical boundaries but false matches for the qualified theory citations. Remove
those matches or explicitly distinguish supplemental context, preserving history.

Brown's `typographic-rhythm-modular-scale.md` raw reference explicitly includes
Conclusion, but no 352–357/section6 target or unresolved disposition exists. Its
“tools—not dogma” qualification is at 356. `natural-colour-system.md` explicitly
cites the comparison table, but only 53–84 is mapped; the actual Summary/table/
subjective framing/footnotes are 278–298. Check all 46 references clause by clause,
including unquoted prose locators, rather than treating these examples as the
whole defect population. Oklab's HSV gamut limitation at 397 already belongs to
the gamut card's 329–409 target; it needs a specific contextual conclusion, not
an invented missing-span finding. Prior F03 replay established only named
corrections and physical structure; this current intended-content review narrows
any broader interpretation of “navigation resolved”.

**F05 — Committed checker replay incomplete (serious; S02-07/09).** Retain the
successful first-block replay and exact failed second-block receipt. Repair link
extraction to distinguish code from prose, exercise a real missing-link negative
control, and replay after all notes/code are present and from committed bytes.
Keep PASS wording aligned to actual predicates. The current helper does not
establish the required intended-parent or complete-clause/context checks.

F02's caveat correction and F04's DES allocation remain reproduced within their
actual scopes. None of these findings requires original acquisition to repair.
Original editions/captures/lineage/fidelity remain a separate S02-08 input block.

### Ledger walk and next handoff

All nine statuses remain open; no row criterion is weakened or deferred.
S02-01 has precise intake receipts but unresolved contextual/check claims;
S02-02 retains identity limits, with the current local-navigation claim too broad;
S02-03 raw-copy population passes but intended typed mappings need repair;
S02-04 lacks complete clause-specific contextual results;
S02-05's current “resolved locators” action needs reconciliation to these defects;
S02-06's unchanged method/DES evidence remains scoped, without a whole-slice
acceptance decision; S02-07 preservation/actual links pass but the published
committed helper fails; S02-08 lacks originals/captures/fidelity;
S02-09 partial accounting is candid, but overstates completion of contextual
mapping/check replay. Correct local evidence in iteration03; retain all remaining
original-input and independent gates. No Slice03 opening under Expedited Mode
until full acceptance. Arc sequence and full-corpus/five-dimension scope unchanged.

### Recoverable reviewer check

The following inline Python was independently run from PLANNING (exit 0). It
adds uniqueness/full-path membership, physical-boundary and table joins to CC's
first-block replay, and explicitly uses a different fence-aware link check.
No maintained validator or source change is introduced.

```python
from pathlib import Path
import json, re, hashlib, collections, subprocess, urllib.parse
P=Path('/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning')
S=Path('/Users/oubiwann/lab/billosys/ai-engineering')
L=P/'project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness'
def strict(p):
 rows=[]
 for n,line in enumerate(p.read_text().splitlines(),1):
  assert line.strip(),(p,n,'blank')
  x=json.loads(line); assert isinstance(x,dict),(p,n,'non-object'); rows.append(x)
 return rows
m=strict(L/'artifacts/locator-map.jsonl')
i=strict(L.parent/'slice01-scope-and-portability-contract/artifacts/card-source-index.jsonl')
I={x['path']:x for x in i}
assert len(m)==len(i)==len(I)==233
assert [x['card_path'] for x in m]==sorted(I)
for x in m:
 y=I[x['card_path']]; assert x['card_sha256']==y['sha256']
 assert x['primary_source_raw']=={k:y['source_fields_raw'][k] for k in ('source','authors')}
 a=x['asserted_locators_raw']
 assert all(a[k]==y['source_fields_raw'][k] for k in ('chapter','pdf_page','section'))
 assert all(a[k]==y[k] for k in ('source_reference_raw','source_reference_status'))
 group=x['card_path'].split('/')[3]
 prefix={'art-and-visual-perception':'ARN','munsell-colour-system':'CLE','the-new-typography':'TSCH'}.get(group)
 expected={f'C-{prefix}-ORIGINAL-EDITION',f'C-{prefix}-PAGE-BASIS','C-BOOK-FIDELITY'} if prefix else ({'C-BUTTERICK-CAPTURE-IDENTITY','C-BUTTERICK-CAPTURE-FIDELITY'} if group=='practical-typography' else {'C-WEB-CAPTURE-IDENTITY','C-WEB-CAPTURE-FIDELITY'})
 assert set(x['caveat_ids'])==expected,(x['card_path'],'caveats')
print('PASS 233 unique sorted exact raw copies; full-path caveat membership')
oldrows=[json.loads(s) for s in subprocess.check_output(['git','show','496c810:project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness/artifacts/locator-map.jsonl'],cwd=P,text=True).splitlines()]
changed=[]
for x,y in zip(m,oldrows):
 if x!=y:
  t=x['prepared_targets'][0]; assert t['locator_value']['line_start']==t['locator_value']['line_end']==30
  z=dict(x); z['prepared_targets']=x['prepared_targets'][1:]; assert z==y
  changed.append(x['card_path'])
assert changed==['knowledge/design/concept-cards/posts/golden-ratio.md','knowledge/design/concept-cards/posts/musical-interval-typographic-ratio.md']
print('PASS map delta only two Brown line-30 targets; all other row bytes/values retained')
def heading(s): return re.match(r'^(#{1,6})\s+(.*)',re.sub(r'^(?:>\s*)+','',s))
counts=collections.Counter()
for x in m:
 for t in x['prepared_targets']:
  b=(S/t['path_or_uri']).read_bytes(); lines=b.decode().splitlines(); v=t['locator_value']
  assert hashlib.sha256(b).hexdigest()==t['snapshot_sha256']
  start,end=v['line_start'],v['line_end']; assert 1<=start<=end<=len(lines)
  if t['locator_kind']=='local-markdown-document':
   counts['documents']+=1; assert start==1 and end==len(lines)
   assert v['page_title']==re.search(r'^title: "(.*)"$',b.decode(),re.M)[1]
  elif 'paragraph_role' in v:
   counts['paragraphs']+=1; assert start==end and start in (30,109)
   assert lines[start-1].startswith('We have all heard of the golden mean' if start==30 else 'This and other meaningful ratios')
  else:
   counts['headings']+=1; h=heading(lines[start-1]); assert h and v['heading'] in h[2]
   assert len(h[1])==v['heading_level']
   boundary=next((n for n in range(start,len(lines)) if (a:=heading(lines[n])) and len(a[1])<=len(h[1])),len(lines))
   assert end==boundary,(x['card_path'],v)
assert counts=={'documents':37,'paragraphs':4,'headings':101}
print('PASS 142 target hashes/bounds: 37 documents, 101 heading boundaries, 4 Brown paragraphs')
posts={x['card_path']:x for x in m if '/posts/' in x['card_path']}
notes=(L/'artifacts/execution-notes.md').read_text()
section=notes.split('### 46-card complete association and contextual result\n')[1].split('Accounting after')[0]
records=[s.strip()[2:-2].split(' | ') for s in section.splitlines() if s.startswith('| `knowledge/design/concept-cards/posts/')]
assert len(records)==len(posts)==46 and {a[0].strip('`') for a in records}==set(posts)
contexts=collections.Counter()
for a in records:
 x=posts[a[0].strip('`')]; pair=x['primary_source_raw']
 assert json.loads(a[1].strip('`'))==[pair['source'],pair['authors']]
 assert json.loads(a[2].strip('`'))==x['asserted_locators_raw']['source_reference_raw']
 targets=a[3].split('<br>'); assert len(targets)==len(x['prepared_targets'])
 for text,t in zip(targets,x['prepared_targets']):
  v=t['locator_value']; assert f"`{t['path_or_uri']}`" in text and f"`{t['snapshot_sha256']}`" in text
  assert f"{v['line_start']}–{v['line_end']}" in text
 contexts[a[4]]+=1
assert sorted(contexts.values())==[2,8,11,12,13]
print('PASS 46 table identity/reference/target associations; ONLY 5 distinct context bodies:',sorted(contexts.values()))
changed_paths=subprocess.check_output(['git','diff-tree','--no-commit-id','--name-only','-r','bf02e970'],cwd=P,text=True).splitlines()
assert len(changed_paths)==7
links=fragments=0
for name in changed_paths:
 p=P/name; b=p.read_bytes(); assert b.endswith(b'\n') and b'\r\n' not in b
 if p.suffix!='.md': continue
 text=re.sub(r'^```[^\n]*\n.*?^```\s*$', '',p.read_text(),flags=re.M|re.S)
 text=re.sub(r'`[^`\n]*`','',text)
 for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
  dest=dest.strip().split()[0].strip('<>')
  if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',dest) or dest.startswith('//'): continue
  path,sep,frag=dest.partition('#'); target=(p.parent/urllib.parse.unquote(path)).resolve() if path else p
  assert target.is_file(),(name,dest); links+=1
  if sep and frag:
   fragments+=1; content=target.read_text(); slugs=set()
   for h in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',content,re.M):
    h=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',h).strip().lower()
    slugs.add(re.sub(r'[^\w-]','',re.sub(r'\s+','-',h)))
   ids=set(re.findall(r'\bid=["\']([^"\']+)',content))
   assert urllib.parse.unquote(frag) in slugs|ids,(name,dest)
print('PASS 7 newlines; actual prose local links/fragments:',links,fragments)
```

Reviewer handoff self-check: exactly six reviewer paths; all protected CC
supporting artifacts/method/closing report and issued prompts are byte-identical
to `bf02e970`; all nine ledger criterion/status rows are unchanged/open. Six
files pass newlines; 34 actual local links and six fragments resolve. The embedded
reviewer block replays from this record with exit 0. `git diff --check` passes.
Initial aggregate output was truncated; bounded data/context projections recovered
the affected review coverage. A guide read attempted from PLANNING failed because
that source path does not exist there; the complete requested SOURCE section was
then delivered. Neither failure was counted as successful reading. Original
fidelity, media/browser/accessibility and package/semantic checks remain unrun.
These are planning-author self-checks, not independent acceptance of this prompt.
Committed-tree scope/whitespace verification follows the explicit-file commit.


## Iteration03 independent review — 2026-10-09

Sofie (CDC), separate from CC, Two-Contributor Workflow. Candidate
`80813b2e2b1ebd6b3bc714e9a4b86478b21cf6ae`, assignment `96137b1f`; SOURCE
`dffa504e851b03b8e4746f1941068e4cc850b612`. Accepted Slice01/audit pins retained.

### Reproduced and retained evidence

The candidate has exactly seven authorized files and both trailers. Its map
changes five rows: remove HSL code 943–1136 twice and HSV code 840–942 once;
add NCS Summary 278–298 and Brown Conclusion 352–357. The five appended mapping
notes explain those changes. Raw/card/source identity fields and caveats are
unchanged. The original captures/page bases remain unresolved.

The exact committed inline checker executes with exit 0 and all eight published
PASS lines, including 233 unique raw copies/eight pairs, full-path caveats,
104 post/141 total hashes/bounds, hierarchy, known omission/clipping witnesses,
83 literal parsed parts across 46 references, DES equality, 26 local links/three
fragments and seven EOF/no-CRLF files. PASS wording about exact joins/roles exceeds
those predicates; see the failure witness below. Its HEAD-based file selection is
applicable to this candidate at this run, not arbitrary later reviewer commits.

A stronger independent join check matches all 44 unique unit path/hash/span
identities to the actual map and every reverse full-card membership. All 44
observations and all 83 clause joins were delivered/inspected. Per-clause intended
article checking finds one cross-source mismatch (secondary hsl.md, U05). This
is substantially improved F01 evidence; full article reading remains CC attestation.
No original comparison or all-card correctness/support review is claimed.

Unchanged 161-file source inventory, earlier Butterick physical/identity checks,
raw baseline and F02/F04 evidence are retained at their earlier records/revisions:
accepted inputs, inventory/method and source bytes are unchanged; the five map
changes do not affect them. This is retention, not a fresh full inventory or
Butterick read. Current actions and complete method were inspected against the
project contract. Method's exact 16 DES rows compare equal to accepted Slice01.

### Remaining findings and contrary checks

**F03 — Secondary HSL join (correctness-grade; S02-02/04).** In the notes' hsl.md
row, the raw CSS-Tricks “HSL Values” clause joins U05 and U32. U05 is Ottosson
HSL theory (143–178); only U32 is CSS-Tricks HSL Values (97–125). The primary
clause's U05/U06 join is correct and the JSONL map itself correctly separates the
secondary citation. Repair the clause join, preserving the accepted map.

**F01 — Shared-unit role (serious; S02-02/04).** U32 calls the CSS-Tricks unit
secondary, but its reverse membership includes hsl-css-syntax.md, whose primary
pair is Drasner. Use a source-neutral unit observation and primary/secondary roles
at each card/clause join. Article source statements remain unverified domain claims.

**F05 — Exact join validation (serious; S02-07/09).** The checker verifies clause
strings/counts and global unit-ID existence, not every claimed clause-to-map/
source relation. In memory only, replacing the secondary HSL join's U32 with
unrelated Brown Conclusion U43 still returns all eight PASS lines from the exact
published checker. The contrary input passes despite being an ineligible source
unit for that card/clause. No file was changed. The added independent check
rejects the actual U05 cross-source assignment. Validate eligibility and intended
source/section/role for every join and run bad cases through the same predicate.
The repaired prose-link checker itself now reproduces; retain that success.

**F05 — Source guide receipts (serious; S02-01/09).** Notes report SOURCE guide
lengths 87/109/220; direct pinned-blob and current-file comparisons establish
94/108/231 for locator/output/verification guides. Exact installed counterparts
match those SOURCE hashes too. Therefore those counts cannot stand as exact
SOURCE coverage receipts. Preserve history, recover actual earlier read path/range
if possible, otherwise label unknown; record fresh bounded reads/readback at the
actual pinned paths. The issued iteration03 prompt requests knowledge/...;
notes incorrectly attribute a request for docs/... to that prompt. The failed
path attempt is execution history, not evidence that the issued route was stale.
Hashes: locator `6d69bd5ff0445af357b1ca39f442db40e25cbf348f7228f1be35484e8019e1ac`;
output `7f93c35e5db153568793002b1199ea8ae3cb61d8fa2ca5e2a15fca4bd2fbbe15`;
verification `095c897f934f753ba5aa1f5b7f40d22a5134f52eb8b71545e9186de4deb396d3`.

### Ledger acceptance and remaining work

| Row | CDC disposition at 80813b2e | Scope and reason |
|---|---|---|
| S02-01 | open | Guide receipts contradict actual SOURCE extents; fresh truthful intake required |
| S02-02 | open | Primary identities/limits retained, but secondary clause/role evidence needs correction |
| S02-03 | done — reproduced | All 233 raw copies and corrected typed map/caveats account for the baseline; no original-fidelity claim |
| S02-04 | open | Unit-specific context improved; secondary join/role remain inaccurate |
| S02-05 | done — reproduced | Every required book/capture/lineage/locator/conversion/media gap has a concrete input, owner, allowed action and falsifiable re-entry; actual acquisition is S02-08 |
| S02-06 | done — reproduced | Complete procedure covers every claim/five dimensions, relationship/CQ components, revisions/corrections, repeated eight live files and all DES findings; examples stay illustrative |
| S02-07 | open | Preservation/actual links/replay pass; published exact-join validation misses the contrary witness |
| S02-08 | open — input-blocked | Missing originals for 150 book-backed cards and immutable captures/lineage/fidelity for 83 web-backed cards |
| S02-09 | open | Partial reporting preserves original gates but overstates joins/receipts/check scope |

These acceptances meet the written bounded criteria; they do not require or claim
later semantic execution. The remaining defects are planning evidence repairs in
iteration04, without redoing whole-file reads or accepted map/actions/method work.
No weakening, deferral, source acquisition or Slice03 opening. Expedited Mode
continues within remaining gates and the five-refinement budget.

### Recoverable stronger reviewer check

The following was executed from PLANNING, alongside exact committed-checker replay.
It prints an expected finding rather than falsely returning a whole-packet pass.
The first draft assumed only target fields could change and failed on authorized
mapping-note additions; the corrected version separately inspected those notes
and retains all other-field equality. Truncated/grouped displays and mistaken
PLANNING-relative source reads were recovered with bounded SOURCE/data projections;
failed delivery was not counted as reading. No CC artifact was edited by CDC.

```python
from pathlib import Path
import json,re,subprocess,hashlib,collections
P=Path('/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning')
S=Path('/Users/oubiwann/lab/billosys/ai-engineering')
L=P/'project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness'
rows=[json.loads(s) for s in (L/'artifacts/locator-map.jsonl').read_text().splitlines()]
old=[json.loads(s) for s in subprocess.check_output(['git','show','96137b1f:'+str((L/'artifacts/locator-map.jsonl').relative_to(P))],cwd=P,text=True).splitlines()]
changes=[]
for a,b in zip(rows,old):
 if a==b:continue
 aa=dict(a);bb=dict(b);aa.pop('prepared_targets');bb.pop('prepared_targets');aa.pop('mapping_notes');bb.pop('mapping_notes');assert aa==bb
 before={json.dumps(x,sort_keys=True) for x in b['prepared_targets']};after={json.dumps(x,sort_keys=True) for x in a['prepared_targets']}
 changes.append((a['card_path'],[(json.loads(t)['locator_value']['line_start'],json.loads(t)['locator_value']['line_end']) for t in after-before],[(json.loads(t)['locator_value']['line_start'],json.loads(t)['locator_value']['line_end']) for t in before-after]))
assert len(changes)==5
print('Exact map delta (card, additions, removals):',changes)
notes=(L/'artifacts/execution-notes.md').read_text()
us=notes.split('### Iteration03 unique source-unit inspection results (CC evidence)\n')[1].split('### Iteration03 exact clause-to-unit')[0]
units={}
for line in us.splitlines():
 if not re.match(r'^\| U\d{2} \|',line):continue
 a=line.split(' | ');uid=a[0].removeprefix('| ');path=a[1].strip('`');sha=a[2].strip('`');span=re.match(r'(\d+)–(\d+);',a[3]);start,end=map(int,span.groups())
 assert uid not in units;assert hashlib.sha256((S/path).read_bytes()).hexdigest()==sha
 units[uid]=(path,start,end)
 cardpaths=re.findall(r'`(knowledge/design/concept-cards/posts/[^`]+)`',a[-1])
 actual={x['card_path'] for x in rows if any((t['path_or_uri'],t['locator_value']['line_start'],t['locator_value']['line_end'])==(path,start,end) for t in x['prepared_targets'])}
 assert set(cardpaths)==actual,(uid,cardpaths,actual)
keys={(t['path_or_uri'],t['locator_value']['line_start'],t['locator_value']['line_end']) for x in rows if '/posts/' in x['card_path'] for t in x['prepared_targets']}
assert len(units)==len(set(units.values()))==44 and set(units.values())==keys
print('PASS 44 unique unit path/hash/span identities and every reverse full-card association')
cs=notes.split('### Iteration03 exact clause-to-unit joins for the 46 post references\n')[1].split('### Iteration03 complete retained validation')[0]
clause_count=0;wrong=[]
for line in cs.splitlines():
 if not line.startswith('| `knowledge/design/concept-cards/posts/'):continue
 a=line.split(' | ');card=a[0].removeprefix('| ').strip('`');row=next(x for x in rows if x['card_path']==card)
 primary=next(t['path_or_uri'] for t in row['prepared_targets'] if not t['locator_value'].get('citation_role'))
 for part in a[1].split('<br>'):
  clause,tail=part.rsplit(' => ',1);ids=re.findall(r'\bU\d{2}\b',tail);assert ids
  clause_count+=1
  for uid in ids:
   assert uid in units and units[uid] in {(t['path_or_uri'],t['locator_value']['line_start'],t['locator_value']['line_end']) for t in row['prepared_targets']}
   expected='knowledge/design/sources/md/posts/working-with-colours.md' if 'Working With Colors Guide' in clause else primary
   if units[uid][0]!=expected:wrong.append((card,clause,uid,units[uid][0],expected))
assert clause_count==83
assert len(wrong)==1 and wrong[0][2]=='U05'
print('FAIL intended per-clause source identity:',wrong)
# The candidate checker merely checks unit-ID existence; replacing a valid unit
# with any other known ID preserves its generic membership/count checks.
hsl_line=next(s for s in cs.splitlines() if s.startswith('| `knowledge/design/concept-cards/posts/hsl.md`'))
forged=hsl_line.replace('=> U05, U32 (secondary','=> U05, U43 (secondary')
assert forged.count('=> U')==hsl_line.count('=> U') and set(re.findall(r'\bU\d{2}\b',forged))<=set(units)
print('Negative witness: unrelated U43 passes the published count/unit-ID membership predicates')
for name in ['knowledge/document-extraction/guides/09-locator-model.md','knowledge/document-extraction/guides/03-output-contract.md','knowledge/concept-cards/guides/08-validation-verification.md']:
 b=(S/name).read_bytes();assert b==subprocess.check_output(['git','show','dffa504e:'+name],cwd=S)
 print('Pinned SOURCE guide:',name,len(b.decode().splitlines()),hashlib.sha256(b).hexdigest())
```

The complete contrary-check replay below returned all eight PASS lines after
substitution (no disk changes); the Path method was restored in finally:

```python
from pathlib import Path
import subprocess, re, contextlib, io
name='project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness/artifacts/execution-notes.md'
text=subprocess.check_output(['git','show','80813b2e:'+name],text=True)
code=re.search(r'```python\n(.*?)\n```',text.split('### Iteration03 complete retained validation and prose-link checker\n')[1],re.S)[1]
forged=text.replace('=> U05, U32 (secondary cited article; distinct from primary pair)',
                    '=> U05, U43 (secondary cited article; distinct from primary pair)')
assert forged!=text
original=Path.read_text
try:
    def read(path,*args,**kwargs):
        if path.resolve()==(Path.cwd()/name).resolve(): return forged
        return original(path,*args,**kwargs)
    Path.read_text=read
    output=io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(compile(code,'80813b2e-checker:in-memory-U43-substitution','exec'),{})
    assert len(output.getvalue().splitlines())==8
    print('Published checker accepted unrelated U43; all eight PASS lines remain green')
finally:
    Path.read_text=original
```

The contrary checker is intentionally candidate-dependent (HEAD was 80813b2e,
clean tracked tree at execution); later reviewer files change its allowlist
selection. Replay that exact historical experiment in its candidate checkout,
not against unrelated HEAD edits. The stronger review block above remains scoped
to candidate map/notes; revised joins will require affected checks at their new
revision. No new acceptance is inferred from running a historical block later.

Reviewer handoff self-check: six reviewer paths; protected CC supporting artifacts,
method/input actions/map/closing report and issued prompts remain byte-identical
to 80813b2e. All nine criteria/verifiers/significance/origins are unchanged;
S02-03/05/06 alone changed to done, six remain open. Six EOF/no-CRLF files,
40 local links and ten fragments resolve; the stronger reviewer block replays
with its expected single finding. `git diff --check` passes. These are author
self-checks of reviewer/planning records, not independent acceptance of this
new prompt. Committed-tree exact scope and whitespace checks follow the commit.

## Iteration04 independent review — 2026-10-09

Reviewer Sofie (CDC), separate from CC; Two-Contributor Workflow. Candidate
`759ce2dd116a4cfe03b72d43fd2791f48486251c`; issue
`83db00fed56a8528dfa151d9bef755b9873c6a04`, preserved
[iteration04 prompt](cc-prompt-iteration04.md). SOURCE remains
`dffa504e851b03b8e4746f1941068e4cc850b612`; Slice01/audit pins unchanged.

### Reproduced results and evidence retention

The final candidate is a direct child of the exact issuing commit, with exactly
five authorized paths and both required trailers. Protected map, actions, method,
plans, prompts, CDC history, Slice01 and audit bytes are unchanged. SOURCE has no
tracked changes; its `knowledge/lfe/` and planning `project12-chcd-protocol/`
remain the unrelated untracked entries. Candidate `git diff --check` passes.

CDC extracted the exact 293-line checker from **759ce2dd committed bytes**,
inspected it, and ran it before reviewer changes: exit 0, all nine PASS lines.
This reproduces 233 raw copies/eight pairs/caveats, 104 post/141 total targets,
hashes/inclusive bounds, intended theory hierarchy and specified omission/clipping
controls, all 83 joins, DES equality, 28 prose links/six fragments and five EOF/
no-CRLF files. The retained intermediate `33e18a19` receipt is accurately identified;
this fresh final-candidate replay supplies the final object-specific evidence.
The unmodified checker uses HEAD only under its explicit issue/direct-child guard;
it should not be run unchanged against a subsequent CDC commit. The pinned
reviewer replay below preserves candidate scope after that commit.

A separate article-identity check covers every one of the 83 clauses. Every one
of the 44 unique unit IDs retains its previously independently inspected exact
path/hash/span/heading tuple; the complete unique tuple set and every reverse
full-card membership match the map. The independent check additionally compares
unit heading labels to mapped heading metadata. All 43 unchanged observations
retain earlier applicability; U32 alone changes to a source-neutral observation.
All 46 clause rows now identify their primary/secondary/supplemental role. The
hsl.md primary clause remains U05/U06 and its distinct CSS-Tricks clause is U32
alone; Drasner's primary HSL clause remains U32/U18. Explicit expectations were
checked against the literal clauses and retained unit identities, rather than
accepted merely because the code copies those IDs.

The exact full published checker rejects three **in-memory table mutations**:
adding eligible-but-wrong-source U05 to secondary HSL, replacing U32 with globally
known but ineligible U43, and labeling Drasner's primary clause secondary. No
file was changed by these controls. The inline same-predicate controls also pass.
These tests establish navigation and recorded join/role integrity, not semantic
support or original fidelity. The independent extra heading comparison does not
imply that the CC predicate separately compares every displayed heading label.

Fresh guide receipts reconcile pinned/source/installed bytes at 94/108/231 lines
and the three published SHA-256 values. Required fresh scopes are recorded as
locator 1–94, output 55–97 and verification 143–186, with a coherent contract
readback. Historical 87/109/220 extents, the incorrect docs/... prompt attribution,
and unavailable earlier exact ranges remain visible; no earlier complete read is
invented. CC's reading is attested; CDC reproduces input identity, required query
coverage and the receipt/readback reconciliation, not the mental act of reading.

Earlier 161-file inventory, Butterick title/URL/body-boundary and 37 complete-read
records, whole-article receipts, F02/F04, and accepted map/actions/method evidence
retain their earlier scopes and revisions: their inputs are unchanged. CDC did
not repeat four whole-article or 37 Butterick reads this pass. Earlier intake and
failure-history blocks are byte-preserved; correcting the current joins/checker
does not turn their older green results into stronger historical predicates.

### Findings, ledger walk and bubble-up

F01/F03/F05 are resolved within their local evidence criteria; earlier F02/F04
remain resolved. S02-08's required inputs are still absent. The current closing
addendum correctly walks all nine rows as three accepted/six open at CC handoff;
CDC's five new acceptances below supersede that handoff, without editing it.
Six produced supporting artifacts remain under artifacts/; author reconnaissance
is immutable input, and every issued prompt remains in the slice root.

| Row | CDC disposition at 759ce2dd | Evidence and limit |
|---|---|---|
| S02-01 | done — reconciled | Exact pins/authority/readback, fresh truthful guide receipts and complete structured query coverage; old unverifiable read ranges remain historical, not accepted as complete reads |
| S02-02 | done — reconciled | All eight raw identities/populations, explicit original/prepared limits and corrected secondary/supplemental joins; missing originals are disclosed, not verified |
| S02-03 | done — retained/reproduced | Earlier accepted map unchanged; 233 raw copies, caveats and current typed targets replay |
| S02-04 | done — reconciled | 37 Butterick records retained plus all 46 post paths/83 clause joins/44 units reproduced against context identities and attributed inspection records; prepared navigation only |
| S02-05 | done — retained | Input/owner/action/authorization/re-entry register unchanged and applicable; acquisition remains unperformed |
| S02-06 | done — retained/reproduced | Five-dimension claim method unchanged and applicable; all 16 DES rows replay; semantic execution remains downstream |
| S02-07 | done — reproduced | Exact five-path commit/protected inputs, final committed checker, stronger joins/headings, full contrary controls, links, newlines and diff check |
| S02-08 | open — input-blocked | No exact originals for 150 book-backed cards or immutable capture/lineage/fidelity evidence for 83 web-backed cards |
| S02-09 | done — reconciled | Complete nine-row walk, actual five-file change set and existing artifact inventory, preserved failures/limits and truthful blocked arc handoff |

Scope-as-specified versus delivery: the local identity/navigation/method packet
is accepted; the required original-source readiness part of Slice02 is not yet
delivered. No deferral, denominator reduction, quarantine substitution or weaker
gate is adopted. Arc01 A01-02 and composition remain open. The anticipated input
gate needs no structural arc or sequencing amendment. Parent and slice plans
receive status/history updates only. No Slice03 opening while S02-08 is open.

Next owner: Operator provides/selects exact Arnheim, Cleland and Tschichold
original files/editions (and translation where applicable), with printed/physical
page bases; identifies existing Butterick/four-article captures and conversion
records or selects fresh capture preparation. CDC then defines exact input and
output allowlists, version/capture and fidelity procedure before a separate CC
assignment. Public URLs or bibliographic entries alone cannot close S02-08.
No capture, purchase, conversion or private search is authorized by this review.
No fifth refinement is spent merely repeating blocked input requests. Full
233-card/five-dimension semantic review, original comparison, media/datasets and
package/browser/accessibility checks remain unrun here and binding downstream.

### Recoverable candidate-pinned reviewer replay

Run with Python 3 from any directory on this host. It reads the exact planning
candidate through Git objects, pins the CC checker's historical file-selection
scope, and runs valid and bad inputs through the full published checker. Source
and installed guidance are checked against their named pinned bytes; changing
those inputs intentionally invalidates this replay. This is inline review evidence,
not maintained validator software. Exit 0; exact output follows the code.

```python
from pathlib import Path
import subprocess,json,re,hashlib,contextlib,io
P=Path('/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning')
S=P.parent.parent
L=P/'project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness'
C='759ce2dd116a4cfe03b72d43fd2791f48486251c'
ISSUE='83db00fed56a8528dfa151d9bef755b9873c6a04'
def blob(pin,path):return subprocess.check_output(['git','show',pin+':'+str(path.relative_to(P))],cwd=P,text=True)
b=blob(C,L/'artifacts/execution-notes.md');old=blob(ISSUE,L/'artifacts/execution-notes.md')
m=[json.loads(x) for x in blob(C,L/'artifacts/locator-map.jsonl').splitlines()]
posts=[x for x in m if '/posts/' in x['card_path']]
def unitrows(n):return [x for x in n.split('### Iteration03 unique source-unit inspection results (CC evidence)\n')[1].split('### Iteration03 exact clause-to-unit')[0].splitlines() if re.match(r'^\| U\d{2} \|',x)]
assert [x.split(' | ')[:4] for x in unitrows(b)]==[x.split(' | ')[:4] for x in unitrows(old)]
units={}
for x in unitrows(b):
 a=x.split(' | '); uid=a[0].removeprefix('| ');path=a[1].strip('`'); start,end,heading=re.match(r'(\d+)–(\d+); (.*)',a[3]).groups()
 units[uid]=(path,int(start),int(end))
 matches=[t for r in posts for t in r['prepared_targets'] if (t['path_or_uri'],str(t['locator_value']['line_start']),str(t['locator_value']['line_end']))==(path,start,end)]
 assert matches
 if 'heading' in matches[0]['locator_value']:assert heading==matches[0]['locator_value']['heading']
 actual={r['card_path'] for r in posts if any((t['path_or_uri'],t['locator_value']['line_start'],t['locator_value']['line_end'])==units[uid] for t in r['prepared_targets'])}
 assert actual==set(re.findall(r'`(knowledge/design/concept-cards/posts/[^`]+)`',a[-1]))
keys={(t['path_or_uri'],t['locator_value']['line_start'],t['locator_value']['line_end']) for r in posts for t in r['prepared_targets']}
assert len(units)==len(set(units.values()))==44 and set(units.values())==keys
print('PASS 44 exact predecessor unit identities, headings and reverse memberships')
section=b.split('### Iteration03 exact clause-to-unit joins for the 46 post references\n')[1].split('### Iteration03 complete retained validation')[0]
count=0
for line in section.splitlines():
 if not line.startswith('| `knowledge/design/concept-cards/posts/'):continue
 a=line.split(' | ');card=a[0].removeprefix('| ').strip('`');row=next(r for r in posts if r['card_path']==card)
 primary=next(t['path_or_uri'] for t in row['prepared_targets'] if not t['locator_value'].get('citation_role'))
 for part in a[1].split('<br>'):
  clause,tail=part.rsplit(' => ',1);ids=re.findall(r'\bU\d{2}\b',tail);assert ids
  expected='knowledge/design/sources/md/posts/working-with-colours.md' if 'Working With Colors Guide' in clause else primary
  assert all(units[u][0]==expected for u in ids),(card,clause,ids)
  count+=1
assert count==83
print('PASS all 83 intended article joins')
code=b.split('### Iteration03 complete retained validation and prose-link checker',1)[1].split('```python\n',1)[1].split('\n```',1)[0]
# Pin the historical Git scope explicitly; use committed bytes for every planning read.
code=code.replace("current=run(['git','rev-parse','HEAD'])","current='"+C+"'")
hsl=next(x for x in section.splitlines() if x.startswith('| `knowledge/design/concept-cards/posts/hsl.md`'))
dr=next(x for x in section.splitlines() if x.startswith('| `knowledge/design/concept-cards/posts/hsl-css-syntax.md`'))
orig=Path.read_text
for label,line,repl in [('valid',None,None),('wrong-source U05',hsl,hsl.replace('=> U32 (secondary','=> U05, U32 (secondary')),('ineligible U43',hsl,hsl.replace('=> U32 (secondary','=> U43 (secondary')),('wrong role',dr,dr.replace('(primary;','(secondary;'))]:
 changed=b if line is None else b.replace(line,repl)
 def read(self,*args,**kwargs):
  if self==L/'artifacts/execution-notes.md':return changed
  if self.is_relative_to(P):return blob(C,self)
  return orig(self,*args,**kwargs)
 Path.read_text=read
 try:
  try:
   with contextlib.redirect_stdout(io.StringIO()):exec(compile(code,'committed-check','exec'),{})
  except AssertionError:
   assert label!='valid';print('PASS full checker rejects',label)
  else:
   assert label=='valid';print('PASS candidate-pinned full checker: all nine checks')
 finally:Path.read_text=orig
for f in ['knowledge/document-extraction/guides/09-locator-model.md','knowledge/document-extraction/guides/03-output-contract.md','knowledge/concept-cards/guides/08-validation-verification.md']:
 data=(S/f).read_bytes();pinned=subprocess.check_output(['git','show','dffa504e:'+f],cwd=S)
 installed=Path('/Users/oubiwann/Library/Application Support/ChatGPT-Profiles/personal/codex-home/skills')/f.removeprefix('knowledge/')
 assert data==pinned==installed.read_bytes()
 print('PASS source/pinned/installed guide',len(data.decode().splitlines()),hashlib.sha256(data).hexdigest())
assert subprocess.check_output(['git','diff',ISSUE,C,'--check'],cwd=P,text=True)==''
print('PASS candidate diff check')
```

```text
PASS 44 exact predecessor unit identities, headings and reverse memberships
PASS all 83 intended article joins
PASS candidate-pinned full checker: all nine checks
PASS full checker rejects wrong-source U05
PASS full checker rejects ineligible U43
PASS full checker rejects wrong role
PASS source/pinned/installed guide 94 6d69bd5ff0445af357b1ca39f442db40e25cbf348f7228f1be35484e8019e1ac
PASS source/pinned/installed guide 108 7f93c35e5db153568793002b1199ea8ae3cb61d8fa2ca5e2a15fca4bd2fbbe15
PASS source/pinned/installed guide 231 095c897f934f753ba5aa1f5b7f40d22a5134f52eb8b71545e9186de4deb396d3
PASS candidate diff check
```

Reviewer execution limits: one broad diff output was truncated; all changed
checker code was read in bounded chunks and other changes were inspected or
compared through complete committed projections. A refresh command initially
requested nonexistent `04-closing-bottom-up.md`; `rg --files` resolved the live
`04-closing-slices.md`, which was then read. Neither failed attempt is evidence
of complete reading or a dangling issued prompt. No unresolved validation failure.

### Reviewer packet validation

The five reviewer paths are project-plan.md, Arc01 arc-plan.md, Slice02
slice-plan.md, ledger.md and this CDC record. All nine criterion/verify/significance/
origin fields remain identical to the candidate; previously accepted S02-03/05/06
rows remain byte-identical. Eight rows are done and S02-08 remains open.
All prior CDC review text is preserved, apart from the expressly replaced current
verdict. A reviewer QA assertion initially expected the wrong number of trailing
newlines at the historical/appended boundary and stopped before creating its
replay file; comparing the unchanged historical text independently of boundary
blank lines repaired that helper. The durable checker was then extracted from
this record and reproduced with exit 0 and every result above. Five reviewer
files have 40 resolving local links/17 fragments, final newlines and no CRLF;
Git diff check passes. No package or source metadata changed, so package Make
gates do not apply to this planning-only review.
