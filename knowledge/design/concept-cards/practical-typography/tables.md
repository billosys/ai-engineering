---
concept: "Tables"
slug: "tables"
category: "layout-composition"
subcategory: "layout-patterns"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Tables"
extraction_confidence: "high"
aliases:
  - "data tables"
  - "layout tables"
prerequisites:
  - "body-text"
extends: []
related:
  - "rules-and-borders"
  - "typographic-grids"
contrasts_with: []
answers_questions:
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"
rosetta_stone: []
css_implementation:
  -
    property: "padding, border"
    example: "th, td { padding: 0.3em 0.5em; } /* illustrative cell padding; choose visible rules for the data */"
    support: "baseline"
---

# Quick Definition

A table organizes data by row and column relationships. Butterick's word-processor side-by-side layout advice must be separated from semantic HTML data tables; cell padding and borders are contextual formatting choices.

# Core Definition

Butterick recommends tables for grids of numbers and, in word processors, otherwise awkward side-by-side arrangements. On the web, [HTML `table`](https://html.spec.whatwg.org/multipage/tables.html#the-table-element) represents multidimensional tabular data and must not be used simply to arrange unrelated page content. CSS Grid/Flexbox can arrange semantic page content; they do not move table semantics into CSS or replace them for actual tabular data.

For the source's formatting examples he suggests starting without borders and adding useful ones, plus gently increasing internal cell space. His 0.03-inch starting value and 0.01-inch increments are reported word-processor advice, not verified current application defaults or mandatory web values. CSS `padding` is internal cell space; it is not a cell margin.

An HTML data table can have a `caption`, header cells (`th`) and appropriate `scope` or explicit header associations. Preserve the row/column meanings and help users interpret complex data. These structures support interpretation; they are not evidence of an assistive-technology test.

# Prerequisites

- **Body Text** — Text and number roles in cells provide context for typography; prose conventions do not define HTML table semantics.

# Key Properties

1. **Data relationships**: Rows/columns encode relationships rather than merely placing items next to one another.
2. **Optional border reduction**: Remove clutter only while retaining legible boundaries and associations.
3. **Internal space**: Choose cell padding for actual density and output; no single amount fits all tables.
4. **Source recipe**: 0.03″ plus 0.01″ increments describes Butterick's suggestion, not a current default.
5. **Unequal padding**: Different block/inline padding can suit the data and measure.
6. **Separate layout mechanism**: CSS Grid/Flexbox is suitable for visual page arrangement; HTML data semantics remain in the markup.

# Construction / Recognition

## To Construct/Create:
1. Decide whether the content has meaningful row/column relationships or is just side-by-side page content.
2. For a data table, use HTML table structure, meaningful row/column headers and a caption where useful; choose `scope` or explicit associations appropriate to complexity.
3. For unrelated visual layout, keep appropriate semantic content and use CSS Grid/Flexbox rather than an HTML layout table.
4. Adjust cell padding and borders together; preserve essential boundaries and interpretation.
5. Inspect actual enlargement, narrow-width handling, reading order and table navigation in the target output.

## To Identify/Recognise:
1. A cell's meaning depends on its row and column headers in tabular data.
2. A visual grid of unrelated content is not thereby a semantic table; appearance alone cannot establish the distinction.

# Examples

**Example 1** (tables): Butterick compares Athos/Porthos/Aramis against Priors?, Alibi? and Confession?: their Yes/No values are respectively Yes/No/Yes, No/Yes/Yes and No/No/No. The “Cluttered” and “Clean” versions repeat that data to illustrate his selective-border advice. The prepared Markdown does not preserve a reliable visual difference; the labels are his judgments, not measured readability here.

**Example 2** (tables): His Athos/Porthos/Aramis phone/cell/fax example repeats the same numbers in “Dense” and “Not” tables to argue for more internal space. The source suggests 0.03″ and gradual 0.01″ adjustments. This record reports the example without claiming current defaults or a rendered improvement. Its contact data are:

| Contact | Athos | Porthos | Aramis |
|---|---|---|---|
| Phone | (617) 555 1453 | (508) 555 3232 | (603) 555 8490 |
| Cell | (617) 555 3145 | (508) 555 2323 | (603) 555 8491 |
| Fax | (617) 555 5413 | (508) 555 4545 | (603) 555 8492 |

Concrete web choice: comparing each person's answers to the same three questions calls for a data table with people as column headers and questions as row headers. Placing an article beside its unrelated navigation calls for semantic article/navigation markup plus visual layout CSS. Giving both arrangements `display:grid` would not supply the data table's missing header relationships.

# Relationships

## Builds Upon
- **Body Text** — Cell text needs appropriate typography; its data relationships require an additional semantic decision.

## Related
- **Rules and Borders** — Border weight and placement can clarify or obscure data; assess actual boundaries rather than require removal.
- **Typographic Grids** — Table alignment forms a content-level grid, while semantic row/column associations distinguish it from arbitrary visual tracks.

# Common Errors

- **Error**: Replacing a semantic data table with unrelated elements styled as a grid, or using an HTML table only for page placement.
  **Correction**: Choose content semantics first; CSS layout is not a substitute for data relationships. Preserve headers and meaningful order.

# Common Confusions

- **Confusion**: All tables need every border, no borders, or a universal padding increase.
  **Clarification**: Compare the actual data, boundary needs and density. CSS padding supplies internal space; border reduction is an editorial option, not a semantic requirement.

# Source Reference

"Tables" page. "Page Layout" chapter.

# Verification Notes

- Available-source comparison: whole prepared tables.md, both Athos/Porthos/Aramis illustrations and padding recipe. Prepared tables retain data but not adequate style evidence; exact original capture/fidelity remains P10-11-blocked.
- Current support: HTML table/caption/th/scope definitions; current technical correction rejects the source's claim of moving semantic table markup into CSS. No browser-support/UI-default claim is inferred.
- Local outcome: one prerequisite and two related premises checked; CQ 7 receives a concrete content-grid case and its distinction from a general typographic grid, not whole-question/global acceptance.
- Historical confidence/metadata and earlier conversion/Rosetta observations remain extraction history rather than refreshed verification results.
- Unrun: actual rendering/enlargement/table navigation/AT, hosted output and full-corpus reconciliation.
