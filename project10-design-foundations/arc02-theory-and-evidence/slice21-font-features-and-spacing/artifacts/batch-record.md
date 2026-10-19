# Slice21 batch record

Intake and execution evidence for `cc-prompt.md`, returned to CDC Sofie via the
Operator relay. This is CC evidence, not independent acceptance. Four ledger
criteria and statuses remain unchanged.

## Pins, scope and preflight

- Planning: branch `planning`, HEAD `e9876d8a08740694d40f66db6f0a79faf31340ee`,
  17 ahead of `origin/planning`; clean before this record. Prompt was added
  after predecessor `cd32d81b3cec2542a0a7acf10ad76d5129f6fa75`.
- Source: branch `main`, HEAD
  `52bfa46332592106f9301226571d6f441df8ce2d`, tracked tree clean; unrelated
  untracked `knowledge/lfe/` is preserved.
- Authority: source writes are limited to the six named card bodies, only
  “Check candidates and fallbacks” in `knowledge/design/guides/type.md`,
  `knowledge/design/SKILL.md` metadata version, and additive
  `knowledge/design/version-history.md` entry. Planning writes are limited to
  this artifact, `closing-report.md`, and Evidence/Notes cells of this ledger.
  No status, criteria, prompt, plan, CDC record, registry, tooling, publication,
  push, closure or successor is authorized.
- The initial index locator used the nonexistent historical path
  `slice01-schema-and-field-inventory`; corrected to the prompt's pinned
  `project10-design-foundations/arc01-portable-contract/slice01-scope-and-portability-contract/artifacts/card-source-index.jsonl`.
  A prior query attempt also used `Path.removeprefix` and failed on the local
  Python version; the query was rerun using `Path.relative_to`. Neither failed
  attempt changed files or supplied evidence.

## Required reading coverage

Read from planning HEAD above and source HEAD above unless noted. Full reads
were delivered in bounded tool outputs; these receipts describe coverage, not
independent comprehension or semantic acceptance.

| Required item | Loaded extent |
|---|---|
| Planning `AGENTS.md` (operator supplied); source `AGENTS.md` | Full; source authority and source/planning separation checked. |
| `knowledge/collaboration-framework/SKILL.md`; `knowledge/project-management/SKILL.md` and `guides/README.md` | Full. Project Management wayfinder loaded before focused guidance. |
| Project10 `project-plan.md`; Arc02 `arc-plan.md` | Complete active body through the Version History boundary; parent ledger criterion rows in full. |
| Slice21 `cc-prompt.md`, `slice-plan.md`, `ledger.md` | Full; all four criteria/statuses open and unchanged. |
| PM `guides/03-planning-top-down.md` | Planning authority through Agree investigations; per-slice open set through implementation-ready assignment; iteration handoff applicable constraints checked. |
| Engineering-methods `guides/07-implementation-prompt-authoring.md` | Full Required reading and CC intake section, including recovery, coverage record and contract-readback rules. |
| Work-verification `guides/01-ledger-discipline.md`; testing `guides/03-validation-gates.md` | Full guides. |
| `knowledge/design/SKILL.md`, `guides/type.md`, `version-history.md`; Concept Cards `SKILL.md` | Full. |
| Concept Cards `guides/05-evidence-lifecycle.md` | Assess Evidence Grade through Record Evidence Gaps; Keep Rich Prose Attached To Its Warrant. |
| Concept Cards `guides/06-graph-cq.md` | Select Relationship Identity through Rich-Body Relationship And CQ Boundaries. |
| Six source cards | Full reads: `opentype-features.md` 111 lines/4,276 bytes; `kerning.md` 115/4,330; `letterspacing.md` 119/4,515; `ligatures.md` 103/3,716; `alternate-figures.md` 114/4,607; `optical-vs-metric-spacing.md` 116/5,910. Total 678 lines/27,354 bytes. |
| Six prepared Butterick pages | Full reads: `opentype-features.md` 92 lines/4,824 bytes; `kerning.md` 96/3,150; `letterspacing.md` 106/4,662; `ligatures.md` 104/4,701; `alternate-figures.md` 172/8,804; `metrics-vs-optical-spacing.md` 112/6,896. Total 682 lines/33,037 bytes. |
| Five endpoint cards | Complete Core Definition, Prerequisites and Relationships sections of `font.md`, `small-caps.md`, `all-caps.md`, `body-text.md`, `typographic-color.md`; no whole-endpoint acceptance. An initial BSD `head -n -1` extraction failed; Ruby section extraction then delivered all requested complete sections. |
| Primary definitions | CSS Fonts Module Level 4 Working Draft dated 2026-10-16 §§6.3, 6.4, 6.7, 6.12 and 7; CSS Text Module Level 3 §7.2 including cursive/script qualifications in §7.2.1; Adobe InDesign “About kerning and tracking,” types of kerning through measurement. Opened the definition prose/tables and skipped linked test listings as instructed. |
| Reference-only | Slice20 closing/CDC records and P10-11 source-input-actions used only for prior-result limits and provenance; no prior acceptance copied. |

Primary URL readback: [CSS Fonts Module Level 4](https://www.w3.org/TR/2026/WD-css-fonts-4-20261016/) is a Working Draft; §§6.3/6.4 specify kerning and ligature controls/defaults, §6.7 separates numeric figure and spacing values, §6.12 recommends high-level controls over low-level feature settings, and §7 describes defaults/precedence. [CSS Text Module Level 3 §7.2](https://www.w3.org/TR/css-text-3/#letter-spacing-property) defines tracking as additional spacing alongside kerning and specifies typographic-unit and script-sensitive behavior. [Adobe's InDesign guidance](https://helpx.adobe.com/indesign/desktop/format-and-style-text/tabs-indents-and-spacing/about-kerning-and-tracking.html) defines metrics and optical kerning and identifies conditional contexts where optical adjustment can help. The draft and product-specific page do not establish behavior in an untested browser, font, app or assistive technology.

## Contract readback

The intended delivery is corrected, useful teaching on six cards plus a
coherent feature/spacing method in the existing packaged type guide and the
owning skill's 1.0.18 history. Preserve all six heading sequences and literal
Source References; change exactly seven existing CSS metadata scalars and no
other metadata. The six full bodies and prepared pages are required because
examples, errors, verification notes and repeated statements can contradict a
corrected definition. Attribute Butterick's advice and source-era software
support; distinguish source report, current technical warrant, editorial
synthesis and observed behavior.

OpenType support requires a suitable font and shaping/application support, but
required script shaping is distinct from optional Latin refinements; common
ligatures normally default on. Kerning data, a CSS request and the shaped
result are separate; `font-kerning: normal` requests metric kerning without
promising equal gaps or visible change. Tracking is additive and contextual,
not pair kerning or universal per-codepoint insertion; preserve Butterick's
5–12% caps advice as attributed judgment with his small-text and display-size
lowercase exceptions. Ligature automation and manually substituted Unicode
text have different effects; required script shaping cannot be generalized
from the Latin `fi` illustration. Figure height/form and advance width are
independent choices; equal advances do not align values with different digit
counts or decimals. “Optical” versus “metrics” in the source is an InDesign
comparison; Adobe's conditional use cases warrant a qualified comparison, not
a CSS mapping or an empirical claim.

The typed relationship inventory and each rich-body relationship statement
are distinct evidence objects: record target identity, field/index, direction
or symmetric contrast basis, premise and disposition for each occurrence.
Resolved paths or matching counts alone do not warrant an edge. For each of
the nine CQ memberships, preserve the exact question and map the actual answer
components, useful contribution and genuine gaps; do not infer anatomy answers
from a kerning/ligature mention or infer a spacing-system answer from tracking.
Do not invent content or remove deficient memberships. This bounded local
review does not close whole-domain edge/CQ composition, source fidelity,
endpoint semantics, actual rendering/accessibility, the corpus, hosted views,
release or Operator gates.

The accepted index and exact baseline projection below govern preservation.
Check all 233 identities, seven scalar exceptions, 227 unchanged cards, all
161 tracked design source files, six frozen heading/citation sequences, guide
boundary, path/fragment integrity, LF/EOF and package bytes. Run native gates
sequentially in the prompt's order, with a separate fresh `make design` and
byte-compare all eight packaged Markdown members to the committed source.
Report exact commands, warnings, failures/recovery and unrun limitations. The
two worktrees require separate allowlisted commits with required coauthor
trailers. Return proposed outcomes only; CDC independently reviews them and
the ledger remains open.

The easily missed constraints are that (1) default-active common ligatures and
required script shaping refute a blanket explicit-enable/off rule, (2) CSS
feature requests cannot establish glyph availability or rendering, (3) the
nine CQ memberships and 25 body statements cannot be “fixed” by editing the
27 typed relations, and (4) commit/package success cannot be described as
semantic acceptance or publication.

## Pinned data queries and baseline projection

Accepted source index: planning commit
`9cc203380aede19231b7c5119f0b43d9fe3d0e78`, path
`project10-design-foundations/arc01-portable-contract/slice01-scope-and-portability-contract/artifacts/card-source-index.jsonl`.
The full JSONL was parsed: 233 rows, 233 unique paths; all six requested paths
occur exactly once. The six-card query read each current raw YAML front matter
through Ruby Psych and the entire `# Relationships` section. The current
projection contains 27 typed header tuples: 8 `prerequisites`, 17 `related`,
2 `contrasts_with`, 0 `extends`.

| Card | prerequisites | related | contrasts_with | CQ memberships |
|---|---|---|---|---|
| `opentype-features` | 0 font | 0 small-caps; 1 ligatures; 2 alternate-figures; 3 kerning | — | CQ1 |
| `kerning` | 0 font | 0 letterspacing; 1 optical-vs-metric-spacing; 2 opentype-features | 0 letterspacing | CQ5, CQ12 |
| `letterspacing` | 0 font | 0 kerning; 1 all-caps; 2 small-caps | 0 kerning | CQ11, CQ12 |
| `ligatures` | 0 font | 0 opentype-features; 1 kerning | — | CQ5 |
| `alternate-figures` | 0 font; 1 opentype-features | 0 all-caps; 1 body-text | — | CQ5 |
| `optical-vs-metric-spacing` | 0 kerning; 1 font | 0 letterspacing; 1 typographic-color; 2 body-text | — | CQ5, CQ12 |

Full CQ texts and occurrence mapping (membership total 9):

| CQ | Exact question | Members |
|---|---|---|
| CQ1 | What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it? | `opentype-features` (1) |
| CQ5 | What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)? | `kerning`, `ligatures`, `alternate-figures`, `optical-vs-metric-spacing` (4) |
| CQ11 | What distinguishes a spacing system from arbitrary padding values — what problem does constraint solve? | `letterspacing` (1) |
| CQ12 | How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient? | `kerning`, `letterspacing`, `optical-vs-metric-spacing` (3) |

All 25 predecessor body relation occurrences follow. Location is line offset
inside the card's `# Relationships` section; exact text is preserved for the
later occurrence-by-occurrence disposition.

| # | Card / subsection | Exact existing body statement |
|---:|---|---|
| 1 | `opentype-features` / Builds Upon | **Font** — OpenType features are part of font files. |
| 2 | `opentype-features` / Related | **Small Caps** — Accessed via `smcp` OpenType feature. |
| 3 | `opentype-features` / Related | **Ligatures** — Accessed via `liga` OpenType feature. |
| 4 | `opentype-features` / Related | **Alternate Figures** — Accessed via OpenType figure features. |
| 5 | `opentype-features` / Related | **Kerning** — Accessed via `kern` OpenType feature. |
| 6 | `kerning` / Builds Upon | **Font** — Kerning data is part of the font file. |
| 7 | `kerning` / Contrasts With | **Letterspacing** — Letterspacing affects all pairs uniformly; kerning adjusts specific pairs. |
| 8 | `kerning` / Related | **Optical vs. Metric Spacing** — InDesign's "optical" spacing overrides font kerning data. |
| 9 | `kerning` / Related | **OpenType Features** — Kerning is activated as an OpenType feature (`kern`). |
| 10 | `letterspacing` / Builds Upon | **Font** — Letterspacing modifies the font's default spacing. |
| 11 | `letterspacing` / Contrasts With | **Kerning** — Kerning adjusts specific pairs; letterspacing adjusts all pairs. |
| 12 | `letterspacing` / Related | **All Caps** — Always letterspace caps. |
| 13 | `letterspacing` / Related | **Small Caps** — Always letterspace small caps. |
| 14 | `ligatures` / Builds Upon | **Font** — Ligatures are font-specific features. |
| 15 | `ligatures` / Related | **OpenType Features** — Ligatures are accessed as OpenType features. |
| 16 | `ligatures` / Related | **Kerning** — Both address letter spacing issues. |
| 17 | `alternate-figures` / Builds Upon | **Font** — Alternate figures are font-specific. |
| 18 | `alternate-figures` / Builds Upon | **OpenType Features** — Accessed as OpenType features. |
| 19 | `alternate-figures` / Related | **All Caps** — Lining figures are mandatory with caps. |
| 20 | `alternate-figures` / Related | **Body Text** — Oldstyle proportional figures suit body text. |
| 21 | `optical-vs-metric-spacing` / Builds Upon | **Kerning** — Metrics preserves kerning pair data; optical replaces it. |
| 22 | `optical-vs-metric-spacing` / Builds Upon | **Font** — The entire argument rests on respecting font-internal spacing data. |
| 23 | `optical-vs-metric-spacing` / Related | **Letterspacing** — Both concern inter-character spacing, but letterspacing is additive while optical is a wholesale replacement. |
| 24 | `optical-vs-metric-spacing` / Related | **Typographic Color** — The goal of good spacing is even color; optical spacing disrupts it. |
| 25 | `optical-vs-metric-spacing` / Related | **Body Text** — Spacing errors accumulate most visibly at body text sizes. |

The body statements above were paired by their actual source headings and
identity, not inferred from the front-matter lists. The card/final-text
disposition, support, scope and relation rationale are recorded below after
the complete revised bodies were read back.

### Typed relation disposition: 27 distinct header occurrences

Prerequisites are recorded as target → card; `related` and
`contrasts_with` are symmetric associations/comparisons, with the stated basis.
The table preserves each card/field/list-index/target identity. “Supported” here
means the bounded local explanation gives a plausible, scoped premise; it is
not an independent edge record, whole-endpoint review or semantic acceptance.

| ID | Card / field[index] → target | Relation reading and local warrant in final body |
|---|---|---|
| T01 | `opentype-features` / prerequisites[0] → `font` | Font resource → feature use; the target must supply relevant glyphs/features, and the app must shape them. Necessary context, not sufficient by itself. |
| T02 | `kerning` / prerequisites[0] → `font` | Font resource → kerning; a resource may provide pair data, while shaping also depends on text/stack. |
| T03 | `letterspacing` / prerequisites[0] → `font` | Font resource → tracking decision; final text is shaped with its own spacing before added tracking is judged. |
| T04 | `ligatures` / prerequisites[0] → `font` | Font resource → optional ligature; required script shaping remains an additional distinct condition. |
| T05 | `alternate-figures` / prerequisites[0] → `font` | Font resource → numeral forms/advances; the final card makes font and application support explicit. |
| T06 | `alternate-figures` / prerequisites[1] → `opentype-features` | OpenType features → alternate figure access; source page and CSS numeric controls support this as one possible route, with availability conditional. |
| T07 | `optical-vs-metric-spacing` / prerequisites[0] → `kerning` | Kerning concept → InDesign spacing comparison; the revised body limits the comparison to font pair data/alternative adjustment, not a general prerequisite for every optical workflow. |
| T08 | `optical-vs-metric-spacing` / prerequisites[1] → `font` | Font metrics/shapes → spacing comparison; Adobe definitions and source discussion support relevance, not quality or price claims. |
| T09 | `opentype-features` / related[0] ↔ `small-caps` | `smcp` is one possible small-cap feature; both bodies condition use on font and target shaping support. |
| T10 | `opentype-features` / related[1] ↔ `ligatures` | Feature classes include ligatures; common optional forms remain distinct from required script shaping. |
| T11 | `opentype-features` / related[2] ↔ `alternate-figures` | Figure forms/widths are optional feature choices; CSS Fonts §6.7 separates form and spacing groups. |
| T12 | `opentype-features` / related[3] ↔ `kerning` | Kerning is a spacing feature; CSS Fonts §6.3 provides a high-level metric-kerning property. |
| T13 | `kerning` / related[0] ↔ `letterspacing` | Pair/context adjustment compared with additive tracking; CSS Text §7.2 says tracking is in addition to kerning. |
| T14 | `kerning` / related[1] ↔ `optical-vs-metric-spacing` | InDesign comparison concerns font pair data versus shape-based adjustment; supported by Butterick's scoped discussion and Adobe's definitions. |
| T15 | `kerning` / related[2] ↔ `opentype-features` | `kern` route versus high-level control; CSS Fonts §6.12 recommends `font-kerning` for ordinary kerning requests. |
| T16 | `letterspacing` / related[0] ↔ `kerning` | Symmetric association recorded at letterspacing's own list index, separate from kerning's occurrence; pair adjustment versus tracking is supported by source and CSS Text. |
| T17 | `letterspacing` / related[1] ↔ `all-caps` | Caps can be considered for tracking; 5–12% is attributed advice, not a mandatory edge rule. |
| T18 | `letterspacing` / related[2] ↔ `small-caps` | Small caps can be considered for tracking; actual glyph design/text governs, no fixed amount. |
| T19 | `ligatures` / related[0] ↔ `opentype-features` | Ligatures are one feature class; optional Latin forms and script-required shaping are separated. |
| T20 | `ligatures` / related[1] ↔ `kerning` | Both affect adjacent glyph appearance, by substitution versus spacing adjustment; a qualified editorial association. |
| T21 | `alternate-figures` / related[0] ↔ `all-caps` | Lining may suit caps, but source preference is optional and lining may fall below cap height. |
| T22 | `alternate-figures` / related[1] ↔ `body-text` | Proportional oldstyle is one possible body-text choice; source preference is contextual, not universal. |
| T23 | `optical-vs-metric-spacing` / related[0] ↔ `letterspacing` | Tracking addition versus kerning adjustment; explicitly qualified by application and script, and not described as CSS optical equivalence. |
| T24 | `optical-vs-metric-spacing` / related[1] ↔ `typographic-color` | Spacing can affect text texture, but “even color” is not asserted as a universal result. This is a bounded editorial association. |
| T25 | `optical-vs-metric-spacing` / related[2] ↔ `body-text` | Butterick's accumulation claim is attributed as his argument; no empirical body-text effect is claimed. |
| T26 | `kerning` / contrasts_with[0] ↔ `letterspacing` | Symmetric contrast: pair/context kerning versus tracking across typographic units; CSS Text and both card explanations support the distinction. |
| T27 | `letterspacing` / contrasts_with[0] ↔ `kerning` | Same symmetric comparison recorded independently at this card's own field/index; not counted as a second independent warrant. |

T01–T27 enumerate all actual nonempty tuples: 8 prerequisites + 17 related + 2
contrasts. There is no `extends` entry. Edge direction for prerequisites is
not inferred from the symmetric related/contrast fields. Reciprocal related or
contrast list occurrences retain their separate card-local identities but do
not count as independent corroboration.

### Body relation occurrence disposition: 25 separate statements

These are not the typed tuple projection above. The old statement at left is
traced to the revised card-specific relationship text at right; each change
retains a useful premise while correcting scope, modality or unsupported
generality.

| Body ID | Existing statement | Final disposition |
|---|---|---|
| B01 | OpenType features are part of font files. | Retained as “may contain layout features”; added application/text conditions. |
| B02 | Small Caps accessed via `smcp`. | Retained as one possible feature, conditioned on font and target shaping. |
| B03 | Ligatures accessed via `liga`. | Reframed by feature class; optional common forms separated from required shaping. |
| B04 | Alternate figures accessed via OpenType figure features. | Retained as optional forms/widths and tied to actual support. |
| B05 | Kerning accessed via `kern`. | Retained as one route; high-level `font-kerning` preferred for ordinary requests. |
| B06 | Kerning data is part of font file. | Qualified to “may include”; presence does not determine final shaped spacing. |
| B07 | Letterspacing affects all pairs uniformly; kerning adjusts specific pairs. | Corrected to typographic character units and contextual glyph adjustment; tracking additive. |
| B08 | InDesign Optical overrides font kerning data. | Kept within InDesign source context; Adobe definitions and its use cases added, no universal claim. |
| B09 | Kerning is activated as `kern`. | Kept as a feature route but scoped against the higher-level CSS property. |
| B10 | Letterspacing modifies font's default spacing. | Kept as additional tracking evaluated with the font's shaping result. |
| B11 | Kerning adjusts pairs; letterspacing adjusts all pairs. | Refined to contextual kerning versus added spacing over typographic units. |
| B12 | Always letterspace caps. | Changed from directive to attributed 5–12% contextual advice with judgment. |
| B13 | Always letterspace small caps. | Changed from directive to contextual option; no fixed amount. |
| B14 | Ligatures are font-specific features. | Retained for optional forms; added shaping system/text dependency and required-script distinction. |
| B15 | Ligatures are accessed as OpenType features. | Retained as a feature class, with defaults and required/optional distinction. |
| B16 | Ligatures and kerning both address letter-spacing issues. | Narrowed to adjacent-glyph appearance, substitution versus spacing adjustment. |
| B17 | Alternate figures are font-specific. | Retained with shaping-application support. |
| B18 | Alternate figures are OpenType features. | Retained as one access route; availability remains font-specific. |
| B19 | Lining figures are mandatory with caps. | Qualified: lining may suit caps, source preference not universal, and cap-height exception retained. |
| B20 | Oldstyle proportional figures suit body text. | Retained as one possible treatment, contextual rather than prescriptive. |
| B21 | Metrics preserves pairs; optical replaces them. | Limited to source's InDesign account; Adobe's definitions clarify the methods and contextual uses. |
| B22 | Optical/metrics argument rests on font internals. | Retained with font data and glyph shapes as inputs; price/format do not establish suitability. |
| B23 | Tracking is additive while optical is a wholesale replacement. | Qualified: tracking adds spacing; optical/metrics comparison remains InDesign-specific and app-dependent. |
| B24 | Good spacing aims at even color; Optical disrupts it. | Recast as a possible texture relation; no universal outcome claim. |
| B25 | Spacing errors accumulate most visibly at body sizes. | Retained only as Butterick's attributed argument, not a tested effect. |

The original full line, target identity and subsection for each B row are in the
baseline table above; the final target is the corresponding card's
`# Relationships` subsection, preserving the same heading and occurrence
order. No header tuple was added, deleted or silently used as a substitute for
one of these 25 prose occurrences.

### Five-dimension outcome by card (CC assessment)

| Card | Available source fidelity | Technical correctness | Scope | Internal/cross-card consistency | Local edge/CQ coverage |
|---|---|---|---|---|---|
| `opentype-features` | Prepared page distinctions retained; application support claims labeled source-era. Original capture remains unavailable under P10-11. | CSS high-level versus low-level control, required script features and optional refinements distinguished against the W3C draft. | No current support survey or named-font result. | Does not say every feature is explicit or every font equivalent; agrees with ligature/figure/kerning cards. | Font prerequisite and four local relations qualified. CQ1 gets feature/form contribution, not a complete hierarchy answer. |
| `kerning` | Pair examples and “Always use” advice retained with attribution; stale UI not repeated as current. | `auto/normal/none`, proportional glyphs, absent data, tracking interaction and high-level control reflect CSS Fonts. | No current default, actual pair output or browser assertion. | Visible gap is not treated as proof; tracking additive; optical comparison scoped to InDesign. | Font, letterspacing contrast and optical/OpenType associations stated; CQ5/CQ12 contributions remain partial. |
| `letterspacing` | 5–12% advice, under-9pt and large-headline exceptions, and disputed Goudy anecdote preserved. | CSS Text typographic-unit, bidi/script behavior and tracking/kerning distinction incorporated; example arithmetic is illustrative. | No mandatory range, comfort claim or Unicode-codepoint guarantee. | Agrees with kerning distinction, caps/small-caps context and guide method. | Font/caps/small-caps and kerning relations qualified. CQ11 is not answered by a tracking example; CQ12 only gets spacing contribution. |
| `ligatures` | `fi`, omitted font names, `gy` separation, manual substitution concerns and stylistic preference retained with attribution. | Common-default and script-required behavior separated from optional Latin controls; no universal toggle claim. | No font specimen, browser, search or AT outcome claim. | Compatible with OpenType feature card and kerning substitution/spacing distinction. | Font/OpenType/kerning associations qualified. CQ5 anatomy remains unanswered. |
| `alternate-figures` | Independent choices, all four combinations, TOP 40, currency columns and zero/one sample retained; lining-height exception and optionality restored. | Numeric form versus width groups reflected in CSS Fonts; layout needed for decimal/unequal-length alignment. | Does not claim every font supports four combinations or turn figure options into variable axes. | Consistent with OpenType and guide's tabular-number request. | Font/OpenType prerequisite and caps/body-text associations qualified. CQ5 is not answered by numeral examples. |
| `optical-vs-metric-spacing` | `nu/un`, `un/no`, `nt/it` and Butterick's view remain attributed; no names/behavior invented. | Adobe's metrics/optical definitions and conditional contexts qualified; InDesign menu kept separate from CSS `font-kerning` and `opsz`. | No current algorithm, legal, price, app-default or rendered comparison claim. | Compatible with kerning, tracking and typographic-color claims; no universal superiority. | Kerning/font prerequisite and letterspacing/color/body-text relations bounded. CQ5/CQ12 support is partial; neither question fully answered here. |

These are CC's proposed results. Available prepared-page fidelity is not a
source-capture audit, and technical/specification cross-checking is not a
rendered behavior test or independent review.

### CQ answer-component attempts

| CQ and required answer components | Cohort contribution and mapped members | Attempt / actual gap |
|---|---|---|
| CQ1: define visual hierarchy; explain how size, colour, contrast, weight and spacing establish it. | `opentype-features` supplies optional feature/form variation and spacing-related controls; `kerning` and `letterspacing` explain local spacing. Slice20 supplies broader conceptual hierarchy material. | Partial contribution only: this cohort explains selected type-feature and spacing choices, but does not define hierarchy or compose all five properties. No target specimen is required for a general explanation; a specimen would be needed only for a claim about its actual rendering. |
| CQ5: explain baseline, x-height, cap height, ascender, descender and counter. | `kerning`, `ligatures`, `alternate-figures`, `optical-vs-metric-spacing` list the CQ. Alternate figures mentions cap height and baseline in numeral context. | Not answerable from these members: none defines the requested anatomy set, and isolated height references do not supply the missing distinctions. Preserve all four memberships as a gap. |
| CQ11: distinguish a spacing system from arbitrary padding and explain what constraint solves. | `letterspacing` contributes one contextual tracking measurement and warns against treating it as universal. | Not answerable: a type-specific tracking example does not define a spacing system, arbitrary padding, or the role of constraints. Keep the question unresolved; do not manufacture a system explanation here. |
| CQ12: explain how font weight, colour and spacing work with size to make hierarchy and why size alone is insufficient. | `kerning`, `letterspacing`, `optical-vs-metric-spacing` contribute local spacing distinctions and possible text texture; Slice20 provides prior conceptual support. | Partial contribution only: the cohort does not integrate weight, literal colour, spacing and size into an answer to why size alone is insufficient. Existing Slice20 conceptual material remains the broader support; no specimen is needed to explain the general concept, but actual output claims require one. |

No memberships or CQ wording changed. This is a cohort contribution/gap
assessment, not whole-corpus CQ closure, coverage validation, retrieval
evidence, or semantic admission.

## Validation and package results

### Preservation and focused checks

- Accepted index at `9cc203380aede19231b7c5119f0b43d9fe3d0e78`: 233 rows / 233
  unique paths; current card roster exactly matches all 233.
- Raw frontmatter check substituted only the seven prompt literals and compared
  the rest of each frontmatter block byte-for-byte. Ruby Psych typed projection
  found exactly seven changed scalar leaves, with map key order preserved and
  all other fields/lists unchanged.
- All 227 cards outside the six assigned paths compare byte-for-byte with
  `main` baseline `52bfa46332592106f9301226571d6f441df8ce2d`. Source commit
  changes only the nine allowlisted paths. All six card heading sequences and
  literal `Source Reference` sections are unchanged.
- `git ls-files knowledge/design/sources`: 161 tracked files; zero source paths
  changed. `knowledge/design/guides/` diff contains only `type.md`; insertion
  is within “Check candidates and fallbacks”.
- One-off local Markdown path/fragment check across the changed guide and six
  cards: 2 local links checked, 0 failures. The cards have no Markdown links.
- Exact source allowlist: 9/9 paths. LF and terminal newline: 9/9. `git diff
  --check`: pass.
- The only metadata version scalar changed in the entrypoint is
  `1.0.17` → `1.0.18`; history addition is a new 1.0.18 entry. Existing history,
  including the earlier 1.0.14 block, remains in place.

### Native gate sequence and outputs

Commands were run serially from `/Users/oubiwann/lab/billosys/ai-engineering`:

| Order | Command | Result |
|---:|---|---|
| 1 | `make help` | Pass; repository target surface inspected. |
| 2 | `make check-skills` | Pass: 25 skills; all descriptions within hard limit. Output reports 19 descriptions above the 300-character editorial target; no description change was made. |
| 3 | `make check-skill-versions` | Pass: version contract, 25 source skills, 25 generated packages, 0 errors. The command also generated the package set. |
| 4 | `make check-package-paths` | Pass: 25 ZIPs, 402 Markdown files scanned, 0 hard failures, 596 warnings (594 unique warning locations), 3 explicit exceptions, 798 external URLs skipped. Warning categories: 170 repo-only/provenance, 154 parser false positive, 124 bundled-reference, 97 sibling-skill-reference, 28 example-project path, 23 source-clone-reference. |
| 5 | fresh `make design` | Pass after deleting only the generated visual-design-system ZIP and rebuilding from committed source. The design description is 360 characters, one above the editorial target; the hard skill-description gate passed. |

Fresh `target/skills/visual-design-system.zip` SHA-256:
`fb0398777dd4af9108c2ff8b1fe1fd226109f9244750397282837c60536a5f96`.
All eight Markdown members were extracted and compared byte-for-byte with
`git show HEAD:<corresponding knowledge/design path>`; all eight matched:

1. `visual-design-system/SKILL.md` — 8,951 bytes
2. `visual-design-system/guides/breaking-the-layout-monoculture.md` — 21,764
3. `visual-design-system/guides/colour.md` — 5,754
4. `visual-design-system/guides/design.md` — 10,977
5. `visual-design-system/guides/foundations-of-design.md` — 30,952
6. `visual-design-system/guides/layout.md` — 35,986
7. `visual-design-system/guides/type.md` — 8,216
8. `visual-design-system/version-history.md` — 6,472

Source commit `dba03b611572eadb15525e814282dde67d65a9bd` has message
“Correct typography feature and spacing guidance” and both trailers:
`Co-authored-by: Codex <noreply@openai.com>` and
`Co-authored-by: Billo AI <ai-engineering@billo.systems>`. Its exact nine paths
are recorded in the closing report. At return, `main` is six commits ahead of
`origin/main`; the pre-existing untracked `knowledge/lfe/` is untouched. No
push/publication occurred.

### Failed attempts and recovery record

- A first historical index path lookup targeted `slice01-schema-and-field-inventory`;
  no such path exists. It was corrected to the named Slice01 scope-and-portability
  artifact. A first earlier Python query used unavailable `Path.removeprefix`;
  it was rerun with `Path.relative_to`.
- An initial endpoint-section shell extraction used GNU `head -n -1`, unsupported
  by this macOS `head`; Ruby then extracted and delivered the complete three
  requested sections from all five endpoints.
- An early relationship-section query continued through following error,
  confusion and verification bullets (73 lines); it was corrected to isolate
  the concept relationship statements, yielding the required 25. The full
  exact baseline statements are preserved above.
- The first whole-card byte comparison used Ruby text-mode output and falsely
  reported a mismatch; rerunning `git show` in binary mode yielded exact byte
  equality for all 227 non-assigned cards.
- Package checker warnings are the only warnings in the native gates; there
  were no hard failures. Gate output was summarized here; the detailed warning
  rows were not expanded because the command reports 0 hard failures and the
  prompt does not require rerunning with `--show-warnings`.

All recoveries completed without changing scope or modifying protected paths.
These checks establish the bounded source/package state only. They do not
establish original-capture fidelity, endpoint acceptance, browser or font
behavior, accessibility, hosted rendering, corpus closure, release or
publication.

## Iteration01 F01 repair — intake before source edit, 2026-10-18

CC context `/root/s21_cc` acknowledges `cc-prompt-iteration01.md`, issued at
planning `ad8ebdd7a38beb83bdf245c9c2d71411df2eee0d`. SOURCE is the clean dedicated
`codex/project10-arc02-autonomous` checkout at
`d19de06d1e79e22dac0b67b5bf2e527c048a1f73`; PLANNING is clean at the issuing
commit. The preserved initial report/recipe and accepted independent results
remain historical evidence; this pass changes no acceptance contract.

Text intake delivered before the dependent source edit:

- Current SOURCE `AGENTS.md`1–238; repository collaboration-framework
  `SKILL.md`1–567 (bounded1–210,211–400,401–567 with the elided330–365 recovered);
  PM `SKILL.md`1–85 then wayfinder1–219, all complete. The installed composer
  was also read, but differs in relative package routes; repository text governs.
- PLANNING Project10 active body1–286, then Arc02 active body1–157; complete
  Slice21 plan1–113, ledger1–10, Iteration01 prompt1–70, independent review1–229
  and pre-existing closing report1–88. Initial prompt authority/scope/gates1–63
  and155–end plus recipe6 (102–109) were loaded; an elided initial scope read
  was recovered in a separate1–63 read. Batch optical five-dimension row and
  validation/limits263–375 were delivered completely.
- Complete current optical card1–113 and complete prepared metrics-vs-optical
  source1–112, including the three illustration descriptions32–38.
- Design `SKILL.md` brief/context/routes/principles24–82; Concept Cards guide05
  “Keep Rich Prose Attached To Its Warrant”130–158; work-verification guide05
  “Evidence During Correction Review”80–106; engineering-methods guide07 CC
  intake297–398; PM iteration naming277–end and handoff202–256. Also loaded
  methodology role/shared/two-contributor26–153 and Autonomous326–461, full
  ledger-discipline guide and row-closure guide. Truncated tool output was
  recovered in bounded reads; no prior context's reading is claimed here.

Required-data query coverage, distinct from semantic reading: Python pathlib/
subprocess queries read the full accepted index at planning9cc20338 and all
current tracked design objects, then compared the sorted entire roster. Result:
233 index rows/233 unique current card paths;233 raw headers;402 tracked design
objects, including161 source files and6 guides;7080 tracked repository paths.
Baseline tracked status is clean. A temporary `/private/tmp/s21-iteration01-state.json`
records the exact pre-edit roster/raw headers/design digests for the post-edit
whole-population checks; it is not a maintained checker or durable artifact.
No sampling or new whole-card semantic acceptance is inferred from these queries.

Contract readback: initial recipe6 and reviewer F01 require the missing
round/flat comparison itself, not just pair names. Prepared source32–38 supplies
the direction (`u` left), shape (`o` round versus `n` flat) and gap/darkness
contrast (`nt`/`it` versus `ti`). Restore only Example1 with the issued paragraph;
keep it Butterick's description of the illustration, preserving Adobe's
conditional comparison and the no-independent-rendering qualification. Direct
paragraph reversal must recover the exact pinned blob, proving every other card
byte unchanged. Compare all233 headers,232 other complete cards,161 sources,
all6 guides,owner/history and all other tracked inputs. The card is unbundled:
unchanged package/checker inputs permit retention of the independently rerun
d19de06d evidence; no fresh native/browser/font/AT/hosted/fidelity result is
claimed. Four row states stay open/done/done/done. CC supplies attestation only;
`/root/s21_review` independently verifies and CDC controls acceptance/closure.

## Iteration01 repair results

Source commit `bca347f580132b0313a9bbb29d77c980a995b8f9`, parent
`d19de06d1e79e22dac0b67b5bf2e527c048a1f73`, changes only
`knowledge/design/concept-cards/practical-typography/optical-vs-metric-spacing.md`
Example1. The paragraph now retains the leftward `u` shift, metrics-balanced
`un`/`no` gaps versus optical round `o`/flat `n` proximity, and darker `nt`/`it`
versus `ti`. A post-edit full-card read against complete prepared source32–38
confirms the direction, shape and gap explanation and its illustration
attribution. Adobe's conditional contexts and every other card byte survive.

This supersedes the initial optical-card available-source/teaching assessment
above for the current revision: the first return retained pair names but
omitted the round/flat explanation, as independent F01 correctly found.

| Optical card dimension | Current CC-attested result |
|---|---|
| Available-source fidelity/teaching | The three concrete illustration explanations are now retained against prepared source32–38. P10-11 original-capture/conversion fidelity remains blocked. |
| Technical correctness | The change reports Butterick's illustrated spacing/darkness contrasts; it adds no independent measurement or algorithm claim. Existing qualified metrics/optical and CSS/opsz distinctions remain byte-identical. |
| Scope | Explicit illustration attribution and no-independent-rendering limit remain; no universal optical result is asserted. |
| Internal/cross-card consistency | The concrete example now explains the comparison named in Core Definition/Key Properties; every other card/guide and Adobe qualification is unchanged. |
| Local edges/CQs | Complete Relationships and all raw metadata are unchanged. The restored example supports the same bounded spacing/texture premise; no anatomy answer or broader hierarchy coverage is invented. Retain the independent27/25/9 local result with its existing CQ gaps. |

Fresh direct checks (Python pathlib/subprocess/hashlib/zipfile plus Git, all
exit0):

- Replace only the revised Example1 paragraph with its pinned predecessor:
  exact original bytes and Git blob `9be7f3a329045a23c6b57c8f2537e6f44f3da498`
  recovered. Revised blob is `26d01b1bea0b953bc85aa78e08143eee3b7b0a3d`.
  This also proves frozen heading/citation/metadata/relationship sections.
- Entire current233-card roster equals the accepted233 index paths; all233
  raw headers and232 other complete cards equal the pre-editd19de06d objects.
  All161 sources (including conversion report),6 guides,owner/history and401
  other tracked design objects equal their pre-edit bytes.
- `git diff --name-only d19de06d` returns exactly the one allowed card; the
  complete7080 tracked-path set is unchanged and7079 other tracked source
  paths, including Make/package/checker inputs, have no delta. No maintained
  checker or extra negative suite was added.
- LF/terminal newline pass; revised card has0 local Markdown links.
  `git diff --check` passes. Planning return scope, Evidence/Notes-only ledger
  mutation and local links/fragments are checked before its separate commit.
- Read the existing generated design ZIP without rebuilding: all8 Markdown
  members equal both current andd19de06d committed inputs. Existing ZIP SHA256
  remains `a84faa792bddef0f920d4623b6fca604f81b328513c12b2f0693e4375a83f068`.

Retained independent evidence: `../cdc-verification.md`, “Preservation, scope
and package reproduction,” actual reviewer `/root/s21_review`,2026-10-18 at
d19de06d. The paragraph is outside the8-member package; all package/checker
inputs and the acceptance criteria are identical. No finding undermines those
methods, and this issued correction requires retention rather than a fresh
build. Retain its successful native/version/package gates,25 source/package
versions/0 errors and8/8 package comparison, including the default-interpreter
PyYAML failure/retry and606 warnings/605 locations. These are retained results,
not fresh execution. Owning1.0.18/history remain unchanged.

Commit recovery: the first source commit message separated the two coauthors
with a blank paragraph, so Git parsed only the last as a trailer. Its message-
only correction first hit `index.lock: Operation not permitted`; the identical
escalated amendment succeeded. Final commit above has both trailers recognized
by Git. No source content changed during that recovery.
The planning commit's first attempt also hit the metadata sandbox
(`index.lock`); this denied attempt supplies no commit evidence.

Four dispositions remain S21-01 open/proposed repair, S21-02 done/retained local
review, S21-03 done/retained plus fresh preservation, S21-04 done/retained native
and package evidence. Independent reviewer acceptance of this revision is
pending. No original-capture/full-corpus/global/behavior/hosted/release outcome,
new native run, push, merge, publication, closure or successor is claimed.
The sole durable supporting artifact remains this batch record. The bounded
repair changes no arc dependency, scope, criterion or higher gate.
