# Slice20 CC batch record

## Assignment and baselines

- Issuing planning commit: `7acd1465127d5b6236c61a06e30545f7c746a1e1` (parent `ea1e8392abda378f1deaac9e1a64b8b2bfb9ef19`, the Slice19 closing revision).
- Source baseline: `3c31bc11e8513ddce10fd6a9c9227e82abd51092` on `main`, matching the issued pin. Planning checkout is `planning`; it was clean at intake. Main tracked files were clean; the pre-existing untracked `knowledge/lfe/` was preserved.
- The issued prompt authorizes nine typography cards, `knowledge/design/guides/type.md`, `knowledge/design/SKILL.md`, and `knowledge/design/version-history.md` only (12 source paths maximum); planning writes are this record, `closing-report.md`, and Evidence/Notes cells in the ledger. It explicitly forbids push, publication, closure, or successor work.

## Required reading and actual coverage

- Read current main `AGENTS.md` and the complete installed collaboration-framework skill; loaded its posture/rights/methodology guidance as applicable. Read project-management SKILL and Guides README, PM guide03 usable-increment and complete-assignment sections, engineering-methods guide07 required-reading/intake section, work-verification guide01 ledger discipline and guide05 independent verification/retention, and testing guide03 proportionate proof/native-package gates.
- Read Project10 plan active body through line 243, Arc02 active body through line 145, both parent ledger criterion/status rows, complete Slice20 plan, ledger, and this prompt. Slice19 history is reference-only; its accepted paragraph method is preserved.
- Read the complete design `SKILL.md`, current `guides/type.md`, `version-history.md`, Concept Cards SKILL and guides05/06. Read all nine assigned cards and all nine complete prepared pages under `knowledge/design/sources/md/practical-typography/` (972 lines total): `what-is-typography.md`, `what-is-good-typography.md`, `font-basics.md`, `mixing-fonts.md`, `headings.md`, `bold-or-italic.md`, `all-caps.md`, `small-caps.md`, and `color.md`.
- Read Core, Prerequisites, and Relationships for the eight named external endpoints: `body-text`, `kerning`, `letterspacing`, `line-spacing`, `opentype-features`, `page-layout-maxims`, `point-size`, and `typewriter-habits`. This is section coverage, not acceptance of whole endpoint cards. Broader tracking/kerning mandates remain unreviewed and later-owned by Arc02.
- Read the primary source passages used for current technical distinctions: CSS Text 3 §2.1; CSS Fonts 4 draft §§2.8 and 6.6; OpenType variations overview; TrueType instruction-set introduction; HTML headings and `em`/`strong` definitions; WCAG 2.2 SC1.4.1. No browser-support survey, legal review, price survey, cognitive-research survey, source acquisition, or new empirical inquiry was performed.

## Source-cited contract readback

The prompt's operational contract is to preserve task-led typography, multiple valid solutions, supplied assets, and the distinction between textual meaning and visual presentation while correcting overgeneralized source-era advice. Butterick's preferences and anecdotes remain attributed rather than universal evidence. The nine cards must each end with five actual outcome dimensions and claim-specific support/limits; metadata, relationship sections, examples, and verification notes must agree. Header tuples and body relationships are separate constructs even though each count is 44. The type guide change is confined to “Assign roles and hierarchy”; owning skill metadata moves only from 1.0.16 to 1.0.17 with additive history. The only permitted metadata changes are the three exact existing CSS scalars in the prompt. The accepted paragraph method and all other protected source/corpus material remain frozen.

The technical sources support bounded distinctions: CSS text transformation is language-sensitive presentation and does not rewrite underlying text ([CSS Text 3 §2.1](https://www.w3.org/TR/css-text-3/#text-transform)); CSS Fonts 4 describes small-cap feature requests and synthesis controls, but that draft is not a browser survey ([§6.6](https://www.w3.org/TR/2026/WD-css-fonts-4-20261016/#propdef-font-variant-caps), [§2.8](https://www.w3.org/TR/2026/WD-css-fonts-4-20261016/#propdef-font-synthesis)); variable-font resources can carry multiple instances ([OpenType variations](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview)), and TrueType fonts may contain instruction streams ([instruction set](https://learn.microsoft.com/en-us/typography/opentype/spec/tt_instructions)). HTML heading levels express document structure; `em` marks stress and `strong` importance/seriousness/urgency ([HTML headings](https://html.spec.whatwg.org/multipage/sections.html#the-h1,-h2,-h3,-h4,-h5,-and-h6-elements), [`em`/`strong`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-em-element)). WCAG says color must not be the sole visual means of conveying information ([SC1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)). None of these sources establishes the appearance, support, contrast, legibility, or accessibility of an adopting project's actual output.

## Required data queries and reconciliation

- Accepted index: planning revision `9cc20338`, `project10-design-foundations/arc01-portable-contract/slice01-scope-and-portability-contract/artifacts/card-source-index.jsonl`. Its 233 project card paths matched the 233 current card paths at source C1 exactly; sorted full-path comparison had no discrepancy.
- Source-C1 cohort query: 44 typed header tuples (14 prerequisites, 30 related, no `extends` or `contrasts_with`); 44 body relationship statements; 17 `answers_questions` occurrences across five distinct exact texts. The body relationship count was rerun with a concise AWK query after one earlier output was truncated; accepted result is 44.
- Exact CQ texts and occurrence counts: visual hierarchy (6); serif/sans choices with historical/functional reasons (1); web-app pairing (2); hierarchy through size/weight/color/spacing (6); the 14px body / 16px heading / 14px subheading hero case (2). Total: 17. Query membership counts are navigation evidence only.
- Query recovery log: initial structured-object query failed nine times because YAML keys were unquoted; corrected query used quoted JSON keys and completed. A subsequent frequency query using unsupported `add` failed nine times; replaced with a supported explicit frequency query, which returned the counts above. An earlier broad endpoint extraction was truncated; exact Core/Prerequisites/Relationships section extraction was rerun and fully inspected. The first body-relationship count output was truncated and was rerun as the concise AWK query above. No failed/truncated result is treated as evidence.
- Meaningful source limits identified before editing: the serif/sans CQ has no adequate history/function evidence in the assigned content; the web-app pairing CQ lacks an actual app, strings, face inventory, fallback, and target output; the hero CQ lacks a rendered hero to diagnose. These remain bounded/partial rather than inferred from card names or counts. Other CQ answer components will be mapped question by question in the completed batch record.

## Validation sequence and no-claim boundary

`make help` was run first in the main checkout and its normal target list was returned. Required post-edit commands are sequential: `make check-skills`, `make check-skill-versions`, `make check-package-paths`, then a separate fresh `make design`; inspect the generated archive and compare all eight Markdown members byte-for-byte with committed source, and inspect the complete version/history contract. No concurrent builds. No new fixtures, browser benchmark, actual browser/AT/font-failure, hosted rendering, source-fidelity, full-corpus, project closure, release, or publication claim is authorized.

## Header tuple reconciliation (C1 identity frozen)

All 44 typed header tuples are unchanged. `prerequisites` are directed from the named prerequisite to the current card; `related` is a symmetric association, not a directed prerequisite. No `extends` or `contrasts_with` tuples occur. The premise below is the bounded connection supported by the revised local teaching; it does not attest the whole endpoint card.

| Exact tuple | Type and direction | Local premise / limit |
|---|---|---|
| `good-typography.prerequisites[0]=typography` | prerequisite: typography → good-typography | Distinguishing text content from visual treatment identifies what is evaluated. |
| `font.prerequisites[0]=body-text` | prerequisite: body-text → font | Font is one rendering input among controls; no acquisition route follows. |
| `font-pairing.prerequisites[0]=font` | prerequisite: font → font-pairing | Compare actual resources/styles; labels do not establish suitability. |
| `font-pairing.prerequisites[1]=body-text` | prerequisite: body-text → font-pairing | Body text can be one role in a comparison; it need not be every design's primary content. |
| `headings.prerequisites[0]=body-text` | prerequisite: body-text → headings | Visual treatment is seen against surrounding text; this does not define semantic outline. |
| `headings.prerequisites[1]=typographic-emphasis` | prerequisite: typographic-emphasis → headings | Weight/size may contribute to a heading's visual style. |
| `headings.prerequisites[2]=point-size` | prerequisite: point-size → headings | Size can distinguish headings; no fixed increment is warranted. |
| `typographic-emphasis.prerequisites[0]=body-text` | prerequisite: body-text → typographic-emphasis | Surrounding text supplies a visual baseline. |
| `typographic-emphasis.prerequisites[1]=font` | prerequisite: font → typographic-emphasis | Available styles and actual output inform visual treatment. |
| `all-caps.prerequisites[0]=typographic-emphasis` | prerequisite: typographic-emphasis → all-caps | Uppercase is one optional emphasis treatment. |
| `small-caps.prerequisites[0]=typographic-emphasis` | prerequisite: typographic-emphasis → small-caps | Small caps is one optional treatment, not inherently refined or required. |
| `small-caps.prerequisites[1]=font` | prerequisite: font → small-caps | Actual feature/glyph coverage determines whether genuine forms can be used; paid status is irrelevant. |
| `typographic-color.prerequisites[0]=body-text` | prerequisite: body-text → typographic-color | Density can be considered in a text block; no foreground colour is prescribed. |
| `typographic-color.prerequisites[1]=typographic-emphasis` | prerequisite: typographic-emphasis → typographic-color | Weight/style may affect density; not semantics or attention by itself. |
| `typography.related[0]=good-typography` | related, symmetric | Visual treatment can be evaluated against goals; relatedness does not itself define a quality rule. |
| `typography.related[1]=body-text` | related, symmetric | Typography applies controls to body text, without making it universally primary. |
| `typography.related[2]=typewriter-habits` | related, symmetric | Prepared source discusses typewriter defaults; endpoint-wide claims were not reviewed. |
| `good-typography.related[0]=body-text` | related, symmetric | Source recommends body text first for prose-dominated work; not a universal priority. |
| `good-typography.related[1]=page-layout-maxims` | related, symmetric | Layout principles can serve text goals; endpoint's full maxim set is not accepted here. |
| `font.related[0]=point-size` | related, symmetric | Apparent size/metrics interact with a resource; endpoint-wide claims are not accepted by this edge. |
| `font.related[1]=kerning` | related, symmetric | A resource may provide kerning data; shaping depends on resource and renderer; endpoint-wide claims unreviewed. |
| `font.related[2]=opentype-features` | related, symmetric | A resource may expose features; availability/behavior needs actual inspection. |
| `font.related[3]=font-pairing` | related, symmetric | Available resources can be compared by role when an additional face solves a need. |
| `font-pairing.related[0]=headings` | related, symmetric | A heading role may motivate a face; structure is separate from font choice. |
| `font-pairing.related[1]=typographic-emphasis` | related, symmetric | Available styles may meet emphasis needs without another family; inspect output. |
| `headings.related[0]=all-caps` | related, symmetric | Caps are one possible treatment; source advice against them is contextual. |
| `headings.related[1]=typographic-color` | related, symmetric | Colour may contribute to hierarchy; inspect complete foreground/background pairs. |
| `headings.related[2]=line-spacing` | related, symmetric | Space may distinguish a heading; “best” is context-dependent and endpoint-wide claims unaccepted. |
| `typographic-emphasis.related[0]=all-caps` | related, symmetric | Another optional short-text treatment; evaluate language and output. |
| `typographic-emphasis.related[1]=small-caps` | related, symmetric | Optional if the feature exists; synthesis/fallback matter. |
| `typographic-emphasis.related[2]=headings` | related, symmetric | Emphasis may affect appearance; structure determines heading semantics. |
| `typographic-emphasis.related[3]=typographic-color` | related, symmetric | Weight may affect text-block density; literal colour/contrast is separate. |
| `all-caps.related[0]=small-caps` | related, symmetric | Distinct treatments; neither is universally superior. |
| `all-caps.related[1]=letterspacing` | related, symmetric | Tracking can be adjusted for string/font; endpoint mandates remain unreviewed. |
| `all-caps.related[2]=kerning` | related, symmetric | Kerning may affect a rendering; endpoint mandates remain unreviewed. |
| `all-caps.related[3]=headings` | related, symmetric | Caps may appear in headings; Butterick's preference is not a ban. |
| `small-caps.related[0]=all-caps` | related, symmetric | Distinct uppercase treatments; suitability depends on text/output. |
| `small-caps.related[1]=letterspacing` | related, symmetric | Tracking may help a particular result; no fixed value is set. |
| `small-caps.related[2]=kerning` | related, symmetric | Shaping can matter; no endpoint-wide mandate is accepted. |
| `small-caps.related[3]=opentype-features` | related, symmetric | `smcp` is relevant; check actual font/application support. |
| `small-caps.related[4]=typographic-color` | related, symmetric | Compare stroke weight/density; density is not literal contrast. |
| `typographic-color.related[0]=font` | related, symmetric | Resources may render with different density at equal settings; inspect output. |
| `typographic-color.related[1]=point-size` | related, symmetric | Size may affect density, not establish pair contrast. |
| `typographic-color.related[2]=small-caps` | related, symmetric | Compare forms/weight; density differences are not contrast ratios. |

## Predecessor body relationship dispositions

All 44 C1 relationship statements were matched by card, section type, and target to the final card. All 44 target identities and section types remain; all statements were reworded to qualify unsupported universals or state a limited local premise. None was removed and no new relationship identity was added. The exact C1 statement is quoted below; the final premise is the corresponding statement in that card's `# Relationships` section. Header identity does not stand in for body wording.

| Card / type / target | Exact C1 body statement | Final disposition |
|---|---|---|
| typography / Enables / Good Typography | “Understanding what typography is precedes understanding what makes it good.” | Reworded: visual-treatment distinction makes contextual evaluation possible. |
| typography / Enables / Body Text | “Body text is the most important element that typography governs.” | Reworded: typography applies visual controls to body text; not universally most important. |
| typography / Related / Typewriter Habits | “Bad typographic defaults inherited from the typewriter era.” | Reworded: prepared source discusses defaults; endpoint-wide claims outside review. |
| good-typography / Builds Upon / Typography | “Good typography is the quality dimension of the general concept.” | Reworded: evaluate visual treatment against text/context. |
| good-typography / Enables / Page Layout Maxims | “Maxims operationalise the principle that typography must serve the text.” | Reworded: layout principles can serve goals; endpoint not fully reviewed. |
| good-typography / Related / Body Text | “Start every project by making the body text look good” is a direct application of the utilitarian principle. | Reworded: source advice is useful in prose-dominated work, not universal order. |
| font / Builds Upon / Body Text | “Font is one of body text's four primary controls.” | Reworded: one input among controls; content/rendering also matter. |
| font / Enables / Font Pairing | “Selecting and combining fonts effectively.” | Reworded: compare available resources when another face solves a need. |
| font / Enables / Kerning | “Font files contain kerning data that affects letter spacing.” | Reworded: a resource may provide data; rendering-stack behavior varies; endpoint claims unreviewed. |
| font / Enables / OpenType Features | “Professional fonts include OpenType features like ligatures.” | Reworded: resources may expose features; check actual support. |
| font / Related / Point Size | “Fonts render differently at the same point size due to em sizing.” | Reworded: metrics interact; endpoint-wide claims not accepted by this edge. |
| font-pairing / Builds Upon / Font | “Pairing requires understanding of individual fonts.” | Reworded: compare actual resources/styles; no paid-font rule. |
| font-pairing / Builds Upon / Body Text | “Pairing decisions start with the body text font.” | Reworded: body text is one possible role, not universal primary content. |
| font-pairing / Related / Headings | “The most common reason for a second font.” | Reworded: heading role may motivate another face; structure remains separate. |
| font-pairing / Related / Typographic Emphasis | “Single-font emphasis often eliminates the need for pairing.” | Reworded: available styles may meet need; inspect actual appearance. |
| headings / Builds Upon / Body Text | “Headings exist relative to the body text.” | Reworded: visual comparison only; semantic outline is separate. |
| headings / Builds Upon / Typographic Emphasis | “Headings use bold and size variation.” | Reworded: weight/size can contribute when appropriate. |
| headings / Builds Upon / Point Size | “Size differentiation creates heading hierarchy.” | Reworded: size can distinguish; no fixed increment. |
| headings / Related / All Caps | “Butterick advises against caps in headings.” | Reworded: contextual preference, not ban. |
| headings / Related / Typographic Color | “Bold headings create color contrast.” | Reworded: colour may contribute; evaluate complete pair. |
| headings / Related / Line Spacing | “Space above and below is the best heading emphasis.” | Reworded: spacing can distinguish; “best” and endpoint-wide claim unaccepted. |
| typographic-emphasis / Builds Upon / Body Text | “Emphasis contrasts with the body text baseline.” | Reworded: surrounding text establishes visual baseline. |
| typographic-emphasis / Builds Upon / Font | “Serif vs. sans serif determines the approach.” | Reworded: actual available styles/output inform treatment; labels do not determine it. |
| typographic-emphasis / Related / All Caps | “Another emphasis option for short text.” | Reworded: optional; evaluate language/output. |
| typographic-emphasis / Related / Small Caps | “A subtler emphasis alternative.” | Reworded: optional if feature exists; account for synthesis/fallback. |
| typographic-emphasis / Related / Headings | “Heading hierarchy uses emphasis tools.” | Reworded: visual contribution does not determine semantic structure. |
| typographic-emphasis / Related / Typographic Color | “Bold creates darker color on the page.” | Reworded: weight may affect density; literal colour/contrast separate. |
| all-caps / Builds Upon / Typographic Emphasis | “All caps is an emphasis option alongside bold/italic.” | Reworded: optional treatment, not a universal substitute or mandate. |
| all-caps / Related / Small Caps | “A more refined alternative to all caps.” | Reworded: distinct; not universally superior. |
| all-caps / Related / Letterspacing | “Mandatory companion to all caps.” | Reworded: may be adjusted; endpoint mandate unreviewed. |
| all-caps / Related / Kerning | “Must be active when using caps.” | Reworded: may affect output; endpoint mandate unreviewed. |
| all-caps / Related / Headings | “Caps are sometimes used in headings (but Butterick advises against it).” | Reworded: contextual source preference, not ban. |
| small-caps / Builds Upon / Typographic Emphasis | “Small caps are a refined emphasis tool.” | Reworded: one option, not inherently refined/required. |
| small-caps / Builds Upon / Font | “Only professional fonts include real small caps.” | Reworded: actual feature/glyph coverage matters; paid status irrelevant. |
| small-caps / Related / All Caps | “Small caps follow the same spacing rules.” | Reworded: treatments are distinct; inspect actual text/output. |
| small-caps / Related / Letterspacing | “Mandatory with small caps.” | Reworded: tracking may help; no fixed value. |
| small-caps / Related / Kerning | “Must be active.” | Reworded: shaping may matter; no universal mandate. |
| small-caps / Related / OpenType Features | “Small caps are accessed as the `smcp` feature.” | Reworded: relevant feature; inspect font/application support. |
| small-caps / Related / Typographic Color | “The key difference between real and fake small caps is color consistency.” | Reworded: compare density/weight; not literal contrast. |
| typographic-color / Builds Upon / Body Text | “Typographic color is primarily a body text concern.” | Reworded: density can be assessed in a block; no foreground prescription. |
| typographic-color / Builds Upon / Typographic Emphasis | “Bold/italic differ in the color they produce.” | Reworded: weight/style may affect density, not meaning/attention alone. |
| typographic-color / Related / Font | “Different fonts produce different typographic color at the same settings.” | Reworded: resources may render differently; inspect actual output. |
| typographic-color / Related / Point Size | “Size affects the perceived intensity of color.” | Reworded: size may affect density, not pair contrast. |
| typographic-color / Related / Small Caps | “Real vs. fake small caps differ primarily in typographic color consistency.” | Reworded: compare forms/weight; density is not contrast ratio. |

## CQ answer-component map

All 17 memberships and the five complete strings below are preserved. The CQ lists are not answers by themselves; rhetorical questions in source prose were not counted as extra CQs.

| Exact question text | Occurrences | Bounded answer supported by assigned material | Missing / status |
|---|---|---|---|
| `CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?` | 6: typography, good-typography, headings, typographic-emphasis, all-caps, typographic-color | Hierarchy is contextual and task-led; distinguish text/appearance, choose structural levels, and compare size, weight, spacing, and colour in actual content. Keep density and literal colour separate and inspect the foreground/background pair. | Partial: no actual artifact, audience, string, or rendered hierarchy was supplied, so no property ranking or outcome is established. |
| `CQ 6: What distinguishes a serif typeface from a sans-serif, and what are the historical/functional reasons for each?` | 1: font | Do not infer actual performance or history from the serif/sans label; inspect supplied styles and text for the task. | Incomplete: assigned material does not substantiate the requested historical/functional account. No historical survey was commissioned. |
| `CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?` | 6: font-pairing, headings, typographic-emphasis, all-caps, small-caps, typographic-color | Size is one cue; weight, spacing, colour, face availability, semantic role, script/features, and surrounding text can also affect distinction. Compare the combined result and inspect the complete literal colour pair. | Partial: no assigned composition or rendered property comparison determines a best combination. No universal size/spacing/weight prescription follows. |
| `CQ 19: A landing page hero section uses a 14px body font, a 16px heading, and a 14px subheading. Why does it feel like nothing stands out?` | 2: headings, typographic-emphasis | A small size difference may be one candidate to inspect; consider content roles, weight, spacing, colour pair, actual face, and hierarchy together. Preserve semantic heading levels independent of CSS size. | Partial / diagnosis unavailable: no hero artifact, copy, viewport, font, background, or rendered evidence was provided. The numbers alone do not establish why it feels flat. |
| `CQ 26: How do you evaluate and select a typeface pairing for a web application? What properties should contrast, and what should harmonise?` | 2: font, font-pairing | Inventory supplied resources, assign roles, compare representative strings/styles, and check scripts, fallback, code, available axes, and actual output. Serif/sans, same-designer, and contrast/harmony are candidates, not rules. | Partial: no target app, content, face inventory, fallback, license, or output exists here; no concrete pairing can be recommended. |

## Nine card outcomes and support limits

Each card's `# Verification Notes` contains five explicit outcomes, source support, limitation, confidence scope, and preservation statement. Their outcomes are:

| Card | Five outcomes (condensed) | Specific support / limitation |
|---|---|---|
| typography | Text/rendering distinction; multiple visual controls; context/audience; expressive intent; highway example is not universal evidence. | Butterick directly defines typography; no independent rendering or legibility result. |
| good-typography | Purpose/audience; meaning support; context; multiple solutions; examples versus tests. | Source thesis is explicit; no audience study, design comparison, or legibility test. |
| font | Terminology; resource/axis inventory; actual coverage/features; supplied assets/license; no category/file-count rule. | OpenType variations support multiple instances; TrueType resources may include instructions. No project inventory/license/security/browser study. |
| font-pairing | Available resources; roles; actual text/styles; scripts/fallback/mixed runs; counts are contextual. | Source supports optional pairing and heuristics. No actual web app, strings, inventory, output, or license. |
| headings | Structure-derived level; visual distinction; multiple properties; contextual size/spacing; actual order/output. | HTML Standard headings/em/strong definitions and source advice. No browser pagination or AT output tested. |
| typographic-emphasis | Intended meaning; semantic markup; available styles; proportionate use; both meanings can apply. | HTML Standard definitions; no face inventory, page, accessibility tree, or AT behavior tested. |
| all-caps | Source text versus transform; language mapping; actual strings/scripts; actual spacing; attributed source claims. | CSS Text 3 §2.1; no cognitive/legal review, browser survey, or rendered comparison. |
| small-caps | Designed/scaled distinction; feature; font/script support; wider synthesis effects; fallback/output. | CSS Fonts 4 draft §§6.6/2.8; no supported/unsupported font or browser output tested. |
| typographic-color | Density/hue; density influences; contextual hierarchy; complete pair/state; no color-only meaning or comfort claim. | WCAG 2.2 SC1.4.1; no palette, pair, comfort, browser, or conformance test. |

## Focused cases (source-defined, not runs)

- One supplied family may serve adequate roles; multilingual coverage/fallback may call for more than three. Neither count proves quality. Same-designer and serif/sans pairings are comparison candidates.
- A hypothetical variable resource may expose multiple instances; this defeats a universal one-file-per-style claim without inventing an actual asset.
- If a face lacks small-cap forms, the feature declaration cannot prove genuine forms; disabling synthesis cannot create glyphs. A face with the feature is a separate conditional case. Neither case was run against an actual font.
- A heading's semantic level remains tied to structure when CSS size changes. A phrase can express both stress and importance; italic/bold appearance does not determine markup. A 12→24 size change is contextual, not intrinsically wrong.
- A gray foreground without its background establishes neither contrast nor comfort. Text density is not the WCAG foreground/background contrast ratio.

## Final preservation, build, and limitations

- Accepted index/current roster comparison: 233/233 exact paths. The 12 changed source paths are exactly the nine assigned cards, `knowledge/design/guides/type.md`, `knowledge/design/SKILL.md`, and `knowledge/design/version-history.md`; the pre-existing `knowledge/lfe/` untracked tree was left untouched. The 224 other cards, all 161 prepared/source files, five other guides, Make/helper/schema/package lists, all nine card heading sequences, and literal Source References were preserved. All assigned frontmatter was byte-identical to C1 except exactly the three named scalars; no new card field/provenance/confidence/source/identity was introduced.
- `make help`: completed at intake. `make check-skills`: pass, 25 skills; 19 descriptions over the 300-character editorial target were reported, with all descriptions within the hard limit. `make check-skill-versions`: pass, 25 source skills / 25 packages / 0 errors. `make check-package-paths`: pass, 25 ZIPs / 402 Markdown files / 0 hard failures; 596 warnings (594 unique locations), 3 explicit exceptions, 798 skipped external URLs. Warnings were retained; no detailed-warning rerun was requested by the prompt.
- Separate post-commit `make design`: pass, visual-design-system package contains 8 Markdown members. Byte comparison against committed source `2b0f5d2576f75e2e50bbb6b849671888d192ec47`: 8/8 identical (`SKILL.md`, `version-history.md`, and six guide files). Full 1.0.17 history contract inspected; older entries and the pre-existing top 1.0.14 record were left intact.
- `git diff --check`: pass. All nine frontmatters parsed with `yq`; raw ordered frontmatter comparison to C1 passed except the exact three scalars. The required Python YAML-library probe failed because PyYAML is not installed; raw-text/yq comparison was used instead. A first metadata update script asserted an unquoted version field; actual `SKILL.md` uses a quoted value, so that attempt stopped after earlier authorized edits. The corrected update succeeded. A separator error briefly duplicated the opening heading; a preservation audit caught it and it was corrected. A first attempt to add font-pairing teaching introduced a new heading; heading-sequence comparison caught and corrected it by moving the text into the existing Core section. All failures were recovered; final preservation checks passed.
- No actual browser, assistive technology, font with/without features, browser support, rendered design, contrast pair, cognitive experiment, legal question, original-source fidelity, exact-revision hosted page, full-corpus composition, release, or publication was tested or accepted. Preserve P10-11 source-fidelity ownership; remaining corpus/live/global-union review; actual browser/AT/font-failure work; P10-13, Arc04, A02-10 and exact-revision hosted/release owners.
- Source commit: `2b0f5d2576f75e2e50bbb6b849671888d192ec47` (parent is C1); required Codex and Billo AI trailers present. No push. Planning remains open for CDC review.
