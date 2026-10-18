---
concept: "Alternate Figures"
slug: "alternate-figures"
category: "typography"
subcategory: "type-elements"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Alternate Figures"
extraction_confidence: "high"
aliases:
  - "alternate numerals"
  - "figure styles"
prerequisites:
  - "font"
  - "opentype-features"
extends: []
related:
  - "all-caps"
  - "body-text"
contrasts_with: []
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
rosetta_stone: []
css_implementation:
  -
    property: "font-variant-numeric"
    example: ".body { font-variant-numeric: oldstyle-nums proportional-nums; } .table { font-variant-numeric: lining-nums tabular-nums; }"
    support: "baseline"
---

# Quick Definition

Alternate figures offer different numeral forms and advances. Figure height/form (lining or oldstyle) and width (tabular or proportional) are separate choices; suitability depends on font support, text and alignment need.

# Core Definition

Butterick describes figures as forms that do not come from the uppercase and lowercase alphabets, and says type designers may supply alternates for different contexts. He cautions that not every font supplies every set and that the default figures are intended to work across contexts. Preserve that as useful source advice rather than a guarantee that a default always suits a particular design.

Lining figures often align near cap height, but Butterick notes some are between lowercase and cap height. Oldstyle figures use ascenders and descenders and may suit lowercase text; he does not say they are inherently better. His `TOP 40 IN 1987` example contrasts oldstyle figures in caps with lining figures. Separately, tabular digits share a fixed advance, while proportional figures vary in width. The four combinations are lining-proportional, lining-tabular, oldstyle-proportional and oldstyle-tabular.

A line of zeroes above ones can reveal whether those two digit forms have equal advances in that font. It cannot establish equal widths for every digit, nor does tabular width alone align decimal points or values with different digit counts; those need suitable layout and formatting.

# Prerequisites

- **Font** — Available numeral forms and widths depend on the supplied font and shaping application.
- **OpenType Features** — Alternate figures may be exposed as font features; inspect actual support.

# Key Properties

1. **Independent axes**: lining/oldstyle concerns figure form and height; tabular/proportional concerns advance width. These are not variable-font axes.
2. **Four combinations**: a font may offer any subset of the four form/width combinations.
3. **Optionality**: the prepared source says defaults are generally useful and alternates are not present in every font.
4. **Context**: lining can fit caps; oldstyle may integrate with lowercase; proportional figures may suit prose; tabular advances can help columns.
5. **Alignment limits**: equal digit advances aid column alignment but do not perform decimal alignment or compensate for different value lengths by themselves.

# Construction / Recognition

## To Construct/Create:
1. Identify whether the task needs a figure form, common digit advances, or both; choose each axis separately.
2. Check the actual font and target application's available controls. Use a high-level numeric property such as `font-variant-numeric` when supported.
3. For columns, request tabular figures if available and also use a layout that aligns values or decimal separators.
4. Compare a zero/one sample only as a limited width clue; inspect other digits and representative values.

## To Identify/Recognise:
1. Lining figures often sit near cap height; some do not. Oldstyle figures may ascend or descend relative to the baseline.
2. Compare `00000000000` with `11111111111` to check those two advances only.
3. Compare actual column values and decimal positions; equal digit widths alone do not establish complete alignment.

# Examples

**Example 1** (alternate-figures): Butterick's `TOP 40 IN 1987` comparison uses oldstyle figures as the source's poor-fit example with caps and lining figures as its preferred fit. He also notes lining figures may fall between lowercase and cap height.

**Example 2** (alternate-figures): Butterick contrasts proportional and tabular currency columns. Tabular advances help the digits occupy consistent widths, while layout still determines alignment of separators and values of different lengths.

**Example 3** (alternate-figures): The zero-over-one test compares equal-length runs of two digits. It indicates whether zero and one have equal advances, not whether all digits do.

# Relationships

## Builds Upon
- **Font** — The font and shaping application determine which forms and widths are available.
- **OpenType Features** — Alternate figure features can expose these choices; availability is font-specific.

## Related
- **All Caps** — Lining forms may suit caps, but the source's preference is not a mandatory rule and some lining figures sit below cap height.
- **Body Text** — Proportional oldstyle figures are one possible body-text treatment; use actual content and context.

# Common Errors

- **Error**: Treating lining figures as always cap-height, oldstyle as mandatory for prose, or tabular figures as sufficient for every alignment problem.
  **Correction**: Inspect the actual font, keep the two axes independent, and use layout for decimal or unequal-length alignment.

# Common Confusions

- **Confusion**: If zero and one have equal widths, all digits and all number strings align.
  **Clarification**: That sample tests only those two advances. Check the other digits, separators and representative values, then align them with layout.

# Source Reference

"Alternate Figures" page. "Text Formatting" chapter.

# Verification Notes

- The four combinations, `TOP 40 IN 1987`, currency columns and zero/one probe come from Butterick's prepared page; preferences are attributed rather than universalized.
- CSS Fonts Working Draft separates numeric figure and spacing values; no font feature or column rendering was tested.
- The font/OpenType and caps/body-text relations are locally qualified; CQ5 anatomy is not answered by numeral examples and remains a real gap.
