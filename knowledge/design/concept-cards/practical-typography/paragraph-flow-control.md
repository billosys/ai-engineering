---
concept: "Paragraph Flow Control"
slug: "paragraph-flow-control"
category: "typography"
subcategory: "type-composition"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Widow and Orphan Control"
extraction_confidence: "high"
aliases:
  - "widow and orphan control"
  - "straggler control"
  - "page break management"
prerequisites:
  - "body-text"
extends: []
related:
  - "line-spacing"
  - "headings"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Widows and orphans describe paragraph lines isolated across a fragmentation boundary such as a page or column. Butterick recommends using controls pragmatically and weighs their blank-space cost; a short final line in continuous scrolling is a different issue.

# Core Definition

Butterick defines: "When only the last line of the paragraph appears at the top of the second page, that line is called a widow. When only the first line of the paragraph appears at the bottom of the first page, that line is called an orphan."

His stance is pragmatic: "Do you need widow and orphan control? Try it. See how it looks." He approaches it like ligatures — "I only use it if widows and orphans are causing a visible problem. Otherwise, I find that the blank lines at the bottom of the page are more annoying."

Butterick considers widows more distracting because of their possible shortness; this is a source judgment. CSS widows and orphans apply to fragmentation and are separate controls.

# Prerequisites

- **Body Text** — Widow/orphan control manages body text flow across pages.

# Key Properties

1. **Widows**: Lines treated at the start of the next fragment under applicable pagination rules.
2. **Orphans**: Lines treated at the end of the preceding fragment under applicable pagination rules.
3. **Separate CSS controls**: CSS defines `widows` and `orphans` separately. Butterick’s all-or-nothing statement describes the word-processor controls he discusses, not all layout systems.
4. **Trade-off**: Preventing isolated lines can leave additional blank space; inspect the trade-off in the output.
5. **Optional**: Use only if the problems are visually distracting.
6. **Source judgment**: Butterick finds widows more distracting because they may be short; this is not a universal preference.
7. **Web documents can fragment**: Print and paged/column web output can have widows and orphans; continuous-scroll last lines are a different visual condition.

# Construction / Recognition

## To Construct/Create:
1. Word and Pages menu paths are source-era examples and may vary by version.
2. CSS has separate `widows` and `orphans` properties for fragmentation contexts.
3. Evaluate whether the cure (blank lines) is worse than the disease.
4. Fix individual widows with judicious editing rather than global settings.

## To Identify/Recognise:
1. In page/column fragmentation, a widow concerns lines at the start of the next fragment; an orphan concerns lines at the end of the previous fragment. CSS properties address these conditions separately.

# Examples

**Example 1** (widow-and-orphan-control): Butterick's pragmatic approach — "Try it. See how it looks."

# Relationships

## Builds Upon
- **Body Text** — A body text page-flow concern.

## Related
- **Line Spacing** — Changes to measure, type or line spacing can affect where fragmentation occurs; verify the page/column output.
- **Headings** — Keep-with-next prevents headings from orphaning.

# Common Errors

- **Error**: Always enabling widow and orphan control without evaluating the result.
  **Correction**: Check whether the blank lines at page bottoms are more or less distracting than the widows and orphans themselves.

# Common Confusions

- **Confusion**: Widows and orphans are equally problematic.
  **Clarification**: Butterick considers widows more distracting because they may be short; CSS treats widows and orphans as separate controls in fragmentation.

# Source Reference

"Widow and Orphan Control" page. "Page Layout" chapter.

# Verification Notes

- Claim review: source advice is attributed and scoped; the technical corrections in this assigned card are summarized in the changed teaching above.
- Source basis: the prepared Practical Typography page named in Source Reference was read. Extraction confidence is provenance, not a current technical proof.
- Technical review: relevant CSS behavior was checked against the cited primary specifications. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS Fragmentation [widows and orphans §3.3](https://www.w3.org/TR/css-break-3/#widows-orphans).
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open.
- Relationship and competency-question contribution is reconciled in Slice19 batch record; this does not establish whole-card endpoint review or full-corpus closure.
