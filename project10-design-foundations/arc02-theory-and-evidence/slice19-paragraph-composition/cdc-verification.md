# Slice19 CDC verification

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
