---
concept: "Sentence Spacing"
slug: "sentence-spacing"
category: "typography"
subcategory: "type-composition"
tier: "foundational"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Type Composition"
chapter_number: null
pdf_page: null
section: "One Space Between Sentences"
extraction_confidence: "high"
aliases:
  - "sentence space"
  - "one space rule"
  - "inter-sentence spacing"
prerequisites:
  - "typewriter-habits"
extends: []
related:
  - "curly-quotes"
  - "hyphens-and-dashes"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Sentence spacing concerns the spaces separating sentences. Butterick recommends one space for his prose typesetting convention; this is contextual editorial guidance, not the definition of all sentence spacing or a universal readability law.

# Core Definition

Butterick recommends: “Always put exactly one space between sentences.” He reports Bringhurst's “Use a single word space between sentences” (The Elements of Typographic Style, 4th ed., p. 29), Felici's statement that separating sentences with two word spaces “has no place in typesetting” (The Complete Manual of Typography, p. 80), and Chicago's advice to leave “a single character space, not two spaces” (16th ed., rule 2.9). These are quotations reported by the prepared page, not independently checked originals or proof of universal consensus. His argument that extra spaces can disturb page texture is not an empirical result established here.

The prepared page acknowledges disputed origins for double spacing, permits two spaces in monospaced/typewriter-style text, and advises accepting a workplace requirement when resisting would endanger employment. Its broad phrase about spacing after punctuation concerns his prose convention: do not apply it to decimal points, URLs, code or languages with other conventions.

# Prerequisites

- **Typewriter Habits** — Checklist item #2 supplies the source's editorial context; it does not settle the disputed history of sentence spacing.

# Key Properties

1. **Source recommendation**: Use one space between prose sentences when adopting Butterick's convention.
2. **Reported authorities**: The page cites Bringhurst's single-word-space advice, Felici's objection to typewriter-style double spacing, and Chicago's advice for sentences and colons. Their originals were not independently checked here.
3. **Convention can change**: Butterick acknowledges earlier spacing practices differed; his insistence is a position about the practice he recommends.
4. **Texture argument**: Extra spaces and possible white-space rivers are his visual explanation, not a newly observed rendering or controlled readability finding.
5. **Exceptions**: The source tolerates two spaces in monospaced text and separately yields to the described workplace requirement. Respect actual house style and protected data.
6. **Display differs from storage**: CSS may collapse or preserve spaces for rendering without rewriting underlying document data. Stored space counts alone do not establish a visible gap.

# Construction / Recognition

## To Construct/Create:
1. Identify prose sentence boundaries, language and the adopting editorial rule. If using this convention, type one space between sentences; punctuation inside `3.14`, URLs or code has a different role.
2. For existing text, constrain edits to intended prose and inspect them. Do not bulk-collapse spaces in preformatted material, quoted data, code or deliberate alignment.
3. For web output, check the effective `white-space` behavior. `normal`, `nowrap` and `pre-line` collapse consecutive spaces; `pre`, `pre-wrap` and `break-spaces` preserve them with different wrapping/end-of-line rules. These are rendering rules, not source-text replacement.

## To Identify/Recognise:
1. Inspect stored text and the rendered paragraph separately. Two stored U+0020 spaces between words can collapse under `white-space: normal` and be preserved under `pre-wrap`; this does not promise a fixed physical gap.
2. Judge the actual page texture in its font, layout and language. Do not infer visible rivers or readability effects just from character counts.

# Context & Application

- **Typical contexts**: Edited prose where Butterick's single-space convention is adopted.
- **Common applications**: Sentence boundaries and applicable prose punctuation, subject to language, house style and data preservation.
- **Historical note**: Butterick explicitly acknowledges competing accounts of the two-space habit's origins. This review does not settle that history or research competing readability claims.

# Examples

**Example 1** (one-space-between-sentences): The prepared page presents the same paragraph with one space, two spaces and a monospaced variant. Butterick describes the extra gaps as disrupting balance; this is his illustration, not a rendering observation reproduced in this card.

**Example 2** (one-space-between-sentences): Butterick invites skeptical readers to inspect books, newspapers and magazines and argues for professional custom. That invitation is not a survey proving all publications use one space. For a technical contrast, `A.  B.` stores two spaces after the period; CSS can collapse them for display or preserve them without changing those stored characters.

# Relationships

## Builds Upon
- **Typewriter Habits** — Item #2 supplies the source's single-space recommendation and checklist context, while the sentence-spacing page retains history and usage exceptions.

## Related
- **Curly Quotes** — Checklist item #1 is another prose-composition choice; both require protecting literal code/data.
- **Hyphens and Dashes** — Checklist item #3 similarly distinguishes intended prose punctuation from literal character sequences.

# Common Errors

- **Error**: Turning the one-space recommendation into a global space-removal operation or a claim that all professionals always agree.
  **Correction**: Apply the chosen prose convention within its language and house style; retain exceptions and protected text, and distinguish Butterick's reported authority from independent verification.

# Common Confusions

- **Confusion**: A source's single-space preference proves better readability, or two stored spaces guarantee a visibly doubled gap.
  **Clarification**: This page supplies editorial advice and an illustration, not general empirical proof. CSS whitespace processing and actual font/layout determine display; neither rewrites stored data.

# Source Reference

"One Space Between Sentences" page. "Type Composition" chapter.

# Verification Notes

- Available source: complete prepared one-space-between-sentences.md, including reported authorities, disputed origins, monospaced and workplace exceptions. Original editions/capture fidelity and independently checked authority quotations remain unresolved under P10-11.
- Technical distinction: [CSS Text Level 3, §3 and §4 opening](https://www.w3.org/TR/css-text-3/#white-space-property) separates collapse/preservation for rendering from underlying document data. No browser, visual comparison, cognitive study or conformance test was run.
- Historical extraction confidence stays unchanged and does not establish universal custom or readability benefit.
- Three local relationships retain their checklist/literal-text premises. CQ1 membership stays recorded, but sentence spacing alone does not define visual hierarchy or all its properties.
