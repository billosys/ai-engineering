# Slice19 CDC verification

Current review: [Iteration01](#iteration01-independent-review--2026-10-17);
S19-01/02 open, S19-03/04 done at their recorded checked scope. Iteration02 active.
The initial review below is preserved as history.

2026-10-17. CDC Sofie independently reviewed the initial CC return under the
Two-Contributor Workflow and Expedited Mode. **Partial acceptance: S19-03/04
done at the checked candidate; S19-01/02 open. Slice19 remains active.**

## Inputs and review

- Issued initial prompt: `cc-prompt.md` at planning
  `4c1861e3243fadb09edec7e201329d92a402c37c`.
- CC source candidate C: `096fb4b38b5eb2bacd0150347e732462ae85dd19`, direct
  child of assigned `7068045aacd6cb75b856786a1de070791f21c2a8`.
- CC planning return H: `4c0806936bf0513a27e02633050e878ce318df01`, direct
  child of the issue. Exactly the batch, closing report and ledger changed.
- Project1.73 active body, then Arc02 1.56 active body, slice plan and ledgers
  govern. CDC read all eleven complete card bodies, revised guide, complete
  308-line batch and closing report; inspected deltas, raw/typed headers and
  protected source projections. Initial source-preparation and endpoint reads
  remain applicable to unchanged inputs; endpoint whole-card acceptance is not
  inferred. Current primary CSS Inline §5.1, OpenType em-square section and
  WCAG2.2 SC1.4.12 were checked again for the findings below.

## Reproduced checks

- Source: exact fourteen authorized paths and assigned parent; planning: exact
  three outputs and assigned parent. Both have the required separate Codex and
  Billo AI trailers. Commit diff/whitespace checks pass; planning criteria and
  statuses were unchanged by CC.
- Accepted index at planning9cc20338 and current/source-base rosters agree on
  all233 paths. Raw headers match after exactly the six literal permitted
  scalar replacements; parsed typed headers agree under those same exceptions.
  All eleven heading sequences and literal Source References match the base;
  222 other cards,161 source files, five other guides, Makefile and metadata
  helper are unchanged. Changed Markdown is LF with terminal newlines.
- Changed source plus five slice records:19 files,44 local links and11 fragment
  references resolve. This is local navigation checking, not hosted rendering.
- Independently calculated nominal12pt=16CSSpx;12pt×1.35=16.2pt=21.6CSSpx;
  synthetic1150/1000=1.15em; unitless parent20/child12 at1.5 gives30/18;
  parent-declared150% inherits30/30; eligible/noncollapsing positive6px margins
  give6/12. Old responsive expression gives16/20px at320/1280px widths and
  40vw gives128/512px. Synthetic65×8/4/16 advances give520/260/1040px.
  These are arithmetic/source distinctions, not rendered-font/engine tests.
- Fresh sequential `make help`, `make check-skills`,
  `make check-skill-versions`, `make check-package-paths`, and separate
  `make design` all exit0. Version gate:25 source skills/25 packages/zero
  errors. Path gate:25 ZIPs/402 Markdown files/zero hard failures;596 warnings
  at594 locations, three exceptions and798 skipped external URLs retained.
  Description check passes the hard limit with19 soft-target notices.
- Fresh design ZIP:8/8 Markdown members equal committed C bytes. SHA-256:
  `b5354ba6fbf0470a3aeed76ad58330821e7f67d17fe876a12b297de012d0cb9d`.
  Version/history gate checks the whole owned source/package contract. Skill
  metadata is1.0.16 with its additive history entry. Passing packaging does not
  establish the disputed teaching or semantic evidence.

Reproduction used native Make targets, direct Git/blob comparisons, Ruby YAML
parsing and direct arithmetic. Temporary read-only comparison scripts/logs in
`/private/tmp/p10-s19-cdc-*` are incidental execution aids, not new project
artifacts or product validators. One early log-tail probe preceded log creation;
that inspection found no log yet, rather than a failed gate. All five gates
subsequently completed. No source edits, pushes or publication by CDC.

## Findings requiring Iteration01

### F01 — Incorrect reference values in the packaged type method

At C, `knowledge/design/guides/type.md:98–108` says percentages compute from
“the parent value” and gives “1.5 times line height,2 times following-paragraph
spacing.” A `line-height` percentage uses the computed font size of the element
where specified; its computed length then inherits. The parent-declared example
is correct only under its implicit declaration/inheritance setup. Explicit150%
on the12px child instead yields18px. See [CSS Inline §5.1](https://www.w3.org/TR/css-inline-3/#propdef-line-height).

[WCAG2.2 SC1.4.12](https://www.w3.org/TR/WCAG22/#text-spacing) bases all four
spacing amounts on **font size**: at least1.5× for line height,2× for following-
paragraph spacing,.12× for letters and.16× for words. At font20px, authored
line-height27px and paragraph gap15px, the first two specified override values
are30px/40px, not40.5px/30px. Preserve AA override versus authored-default and
AAA distinctions. The initial CDC prompt itself used ambiguous shorthand for
the WCAG multipliers; CDC owns and explicitly corrects that instruction here.
No conformance testing is added. S19-02 remains open.

### F02 — Contradictory repeated claims in two cards

At C, `point-size.md:48` still says digital fonts are drawn inside an em
rectangle; `em-unit.md` correctly explains that glyphs can extend outside its
coordinate grid. `point-size.md:107–108` still labels doubling heading size an
error and commands subtler increments. Attribute Butterick's emphasis advice
and allow hierarchy/task-driven sizes; nominal size is a scale reference, not
an outline bound. [OpenType em square](https://learn.microsoft.com/en-us/typography/opentype/spec/ttch01#funits-and-the-em-square)
supports the digital distinction.

At C, `hyphenation.md:95–96` asks whether auto always works but answers a
different question about left alignment/headings. Its recognition line71,
heading relationship line86 and error line90 also retain unqualified
recommendations, despite scoped Core/Properties teaching. Make the clarification
answer known-language/resource dependence; treat rivers as a possible result
and heading/justification choices as contextual source advice. Preserve useful
source examples, distinctions and actual-output checks. S19-01/02 remain open.

### F03 — Inventories do not establish every final relationship disposition

The batch's49 raw header tuples and47 predecessor body statements are useful
and correctly separated. The47-row table has no final statement/disposition
column; a paragraph listing selected changes leaves the remainder implicit.
The header summary lists broad co-control topics without recoverably connecting
every tuple/type/direction to its supporting premise. In particular, record
`prerequisites` as endpoint→listing card; a learning aid is not a demonstrated
universal prerequisite or a source assertion just because two concepts occur.

Complete the existing tables/groups, without a new registry: identify the final
retained/reworded/removed premise for each predecessor body statement, and map
each exact header tuple once to an explicit scoped warrant. Shared groups are
fine when members and the actual common premise are clear. An appropriate
example is point-size supporting em-unit's nominal-size definition, while
allowing digital glyphs outside the grid; this does not warrant maximum bounds.
Keep endpoint limits, current body versus header namespaces and exact inputs
visible. The CQ table's16 occurrences/six texts with partial contributions and
missing components are useful; no new CQ inventory is requested. S19-02 open.

## Row dispositions and next action

| Row | CDC disposition | Evidence / limit |
|---|---|---|
| S19-01 | open | Useful corrections and eleven five-dimension summaries; F02 prevents complete final-body acceptance. |
| S19-02 | open | F01/F02/F03; CQ partial-answer boundaries are retained, not full answerability. |
| S19-03 | done | Independently reproduced exact-path, roster, six-scalar, raw/typed header, citation/heading and protected-byte checks at C. |
| S19-04 | done | Independently reproduced owning version/history, native/package gates,8/8 integration and scoped return at C/H; teaching correctness remains S19-01/02. |

[Iteration01](cc-prompt-iteration01.md) is the active CC implementation handoff.
Source changes are narrowed to the two card bodies and type-guide paragraphs;
retain this candidate's other accepted material. Fresh affected preservation
and package checks apply to the return; do not relabel C's acceptance as checking
future bytes. Keep current1.0.16 for this unfinished correction group.

No parent-plan change or successor is warranted by these local findings.
P10-11 fidelity, corpus/live/global composition, hosted final-revision rendering,
actual browser/AT behavior and release gates remain with their existing owners.
Neither Slice19 nor Arc02 closes here.

## Iteration01 independent review — 2026-10-17

**Current verdict: F01/F02 resolved; F03's current memberships, directions and
premises reproduced, with two predecessor-transcription errors remaining.
Slice19 stays open for the narrowly bounded F04/F05 correction below.**

Source C1=`0428cbfd6adedfa83305086d3b5ea4e54cfe2a5a`, direct child of C096fb4b3;
planning H1=`cfb084c27e9315de029732e5d456e8eaa3a7a9cc`, direct child of issue
ca97cd41. CDC reviewed the three source deltas, both complete changed card
bodies, the guide correction and the entire Iteration01 batch/report addenda.
The initial unchanged source/guide review remains applicable by byte comparison.

### Reproduced Iteration01 evidence

- Exact source3/planning3 path sets, both parent pins/trailers, no whitespace
  failures. CC changed only ledger Evidence/Notes. Issued prompt and CDC record
  remain byte-identical. Planning clean; SOURCE only unrelated `knowledge/lfe/`.
- All233 paths/headers match C; raw identity establishes unchanged typed values
  as well.231 other cards and all eleven heading sequences/literal citations
  are unchanged; exact whole-tree scope also preserves all161 sources, five
  other guides, owning SKILL/history, helper, Make/schema/package lists.
- F01 now correctly distinguishes parent-declared/inherited150% from a child
  explicitly declaring150%. Independent20/12px calculations give30/30 versus
  child18; unitless1.5 gives30/18. WCAG values at font20px give30/40/2.4/3.2px
  and reject authored-value40.5/30. F02's grid/bounds, heading choice and
  language/resource/rivers statements are correct and consistent in both
  complete changed bodies. Useful examples and the scoped guide CSS survive.
- All49 header tuples match typed source identities once, with correct
  prerequisite endpoint→listing orientation and symmetric related/contrast
  readings. CDC assessed their local learning/association premises and limits;
  this does not accept complete external cards or universal dependencies.
  All47 current body statements join literally to the47 final table cells;
  final/predecessor endpoint sets match, with no additions or removals.
  Only45/47 predecessor statements match literal original7068045a bytes:
  the two mismatches are F05 below. The direct comparison stopped at the first
  mismatch; a diagnostic pass compared the whole population and found exactly
  these two, with all current cells matching. This is a finding, not a passing
  exact-predecessor claim. CQ16/six-text contributions remain partial and
  unchanged; affected point-size and hyphenation teaching preserves those limits.
- Changed source and three returned records:6 files,18 local links/12 fragments
  resolved, LF/EOF passed. Fresh sequential `make help`, `make check-skills`,
  `make check-skill-versions`, `make check-package-paths`, separate `make design`
  all exit0.25 source skills/25 packages/zero version errors;25 ZIPs/402 Markdown
  files/zero hard failures;596 warnings at594 locations,3 exceptions,798 external
  URLs skipped. All8 design Markdown members equal committed C1. ZIP SHA-256
  `94273e08587c3afe8d37477da4180c5e0856c45a2e469e9674a9c721d49c36d4`.
  Native/version/package success does not establish semantic or hosted behavior.

### F04 — Two frozen CSS examples contradict the corrected teaching

Both existing `css_implementation[0].example` scalars at C1 line33:
- `justified-text.md` still says “always pair with hyphenation,” contradicting
  its corrected contextual source recommendation and conditional behavior.
- `hyphenation.md` still says `lang` is required on `html`, contradicting its
  corrected element/ancestor explanation. [CSS Text §1.3/§5.3](https://www.w3.org/TR/css-text-3/#hyphenation)
  requires known content language and an appropriate resource, without that
  exclusive HTML-element placement rule.

These were frozen by CDC's six-scalar initial design and Iteration01 boundary;
CC obeyed that boundary. CDC owns the omission. It prevents full self-consistency
under S19-01 and is repaired within the same two existing cards/fields, with no
new schema/data/capability. The current slice plan and Iteration02 explicitly
amend the permitted total from six to eight scalars and S19-03's matching count.
No silent contract rewrite or blanket permission to modify metadata: exactly
the two replacement values in Iteration02 are authorized. Other headers and all
current bodies remain frozen. The whole-project semantic requirement is unchanged.

### F05 — Two predecessor rows are paraphrases, not verbatim input

In H1's “F03 — disposition of all47 predecessor body statements” table,
`line-spacing`→`Body Text` and `line-length`→`Body Text` have predecessor cells
“one of the four primary body text controls.” Original7068045a actually says:

- `Line spacing is one of body text's four primary controls.`
- `Line length is one of body text's four primary controls.`

Their final body statements already match these originals. Repair the two
predecessor cells and classify them retained-with-supported-limit, not reworded;
keep their valid current cells and scope limits. Preserve the original earlier
inventory as historical and identify the correction. The other45 predecessor
and47 current cells, all49 tuple identities and the CQ table need no new repair.

### Row walk, retention and handoff

| Row | Current CDC disposition | Limit / required next proof |
|---|---|---|
| S19-01 | open | Body/guide repairs accepted at C1; F04 must align two existing CSS metadata examples. |
| S19-02 | open | Local current premises/directions and CQ limits accepted at C1/H1; F05 prevents exact predecessor-map acceptance. |
| S19-03 | done at C1 | All233 raw headers unchanged from accepted C; preservation outside the now-eight named exception slots is independently reproduced. Iteration02 must verify only its two exact replacements and all protected bytes at the returned revision. |
| S19-04 | done at C1/H1 | Fresh independent native/version/package and return checks above; body/header-only follow-up changes no packaged input or version. Retain only after checking those inputs remain byte-equal. |

[Iteration02](cc-prompt-iteration02.md) is the current CC assignment. It needs two
literal metadata-scalar replacements and two exact predecessor-row repairs,
not another semantic audit or build system. Preserve original-fidelity, final
hosted rendering, corpus/live/global, actual browser/AT and release owners.
Slice19 remains active; no successor is opened. No source edits, push or
publication were performed by CDC. Arc's parent criteria/statuses are unchanged;
its routine wording now leaves exact metadata bounds in the slice's one home.
