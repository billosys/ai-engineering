---
concept: "Asymmetric Typography"
slug: "asymmetric-typography"
category: "layout-composition"
subcategory: "layout-principles"
tier: "foundational"
layer: "1-principles"
source: "The New Typography"
source_slug: "the-new-typography"
authors: "Jan Tschichold"
chapter: "The Principles of the New Typography"
chapter_number: 12
pdf_page: 102
section: null
extraction_confidence: "high"
aliases:
  - "asymmetric layout"
  - "non-axial composition"
  - "asymmetric page composition"
prerequisites:
  - "functional-typography"
extends: []
related:
  - "the-new-typography"
  - "active-white-space"
  - "typographic-contrast"
  - "reading-order"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone: []
css_implementation:
  -
    property: "text-align"
    example: "body { text-align: start; } /* Logical line alignment; page composition needs separate choices. */"
    support: "baseline"
---

# Quick Definition

Asymmetric typography organizes a composition without making a shared central axis its governing structure; Tschichold advocates it as a response to content hierarchy and reading — "Asymmetry is the rhythmic expression of functional design."

# Core Definition

This section preserves the card’s recorded account of Tschichold’s historical programme; quotations, attributions and page claims have not been checked against the unavailable represented edition. Its polemics are not universal contemporary rules.

Tschichold's argument against centred layout is both practical and philosophical: "We believe it is wrong to arrange a text as if there were some focal point in the centre of a line which would justify such an arrangement. Such points of course do not exist, because we read by starting at one side."

The central axis of old typography is criticised as artificial: "The central axis runs through the whole like an artificial, invisible backbone: its raison d'être is today as pretentious as the tall white collars of Victorian gentlemen." In centred composition, "the contents are subordinated to 'beautiful line arrangement.' The whole is a 'form' which is predetermined and therefore must be inorganic."

By contrast: "Working through a text according to these principles will usually result in a rhythm different from that of former symmetrical typography. Asymmetry is the rhythmic expression of functional design. In addition to being more logical, asymmetry has the advantage that its complete appearance is far more optically effective than symmetry."

# Prerequisites

- **Functional Typography** — Content-led hierarchy supports understanding the historical argument for asymmetry; function can also justify a centered composition.

# Key Properties

The historical preferences below describe the programme; current use depends on content, audience, language/script, output, constraints and supplied identity.

1. **Non-axial organization**: The page is not governed by one central axis. Centered subcomponents can coexist within it; asymmetry is not a synonym for flush-left/ragged-right text.
2. **Script-aware reading**: Content structure and writing mode inform placement. Left-to-right describes relevant scripts, not a universal category of European readers.
3. **Rhythmic option**: Varied line lengths and groupings can create deliberate rhythm; asymmetry alone does not make it natural or effective.
4. **Attributed preference**: Tschichold calls asymmetric composition "far more optically effective than symmetry." This is not a comparative readability result for every task.
5. **Unlimited variation**: "The principle of asymmetry gives unlimited scope for variation."
6. **Expresses modern life**: "The liveliness of asymmetry is also an expression of our own movement and that of modern life."
7. **Order within asymmetry**: "A striving for order can, and must, also be expressed in asymmetrical form."

# Construction / Recognition

## To Construct/Create:
1. Read the text and identify its logical structure and hierarchy.
2. Arrange elements according to their communicative importance, not a centred axis.
3. Choose text alignment for the script and content. CSS `text-align: start` optionally aligns lines to the logical start; it does not generate an asymmetric page.
4. Create rhythm through contrast in type sizes, weights, and spatial groupings.
5. Maintain order: asymmetry must not degenerate into chaos.

## To Identify/Recognise:
1. Centred typography: all lines balanced around an invisible vertical axis; rigid, symmetrical appearance.
2. Asymmetric typography: non-axial spatial grouping, which may use varied margins, dynamic placement or active space. Preserve meaningful source/reading/focus order independently.

# Context & Application

- **Typical contexts**: Posters, editorial layouts or interfaces where a non-axial composition suits the content and supplied identity.
- **Common applications**: Dynamic heading placement and non-axial groups; left-aligned body text alone does not identify asymmetry.
- **Historical note (reported, unverified here)**: Asymmetric typography became the dominant paradigm of 20th-century graphic design. It is now so standard that centred text is the marked/unusual choice in most contexts.

# Examples

These are retained reported examples and quoted wording, not newly verified figure, authorship, priority or page evidence.

**Example 1** (p. 70): The centred letterhead "Das politische Buch" — "Centred layout using lightweight sanserif has no visual effectiveness and reaches a 'typographic low' for today."

**Example 2** (p. 70): Tschichold's redesign contrasting an old centred poster with an asymmetric version using the same type — "The effect is gained chiefly by contrasts in type sizes and the use of space."

# Relationships

## Builds Upon
- **Functional Typography** — Functional purpose supplies a premise for the programme’s compositional choice, not a logical necessity that every functional design be asymmetric.

## Related
- **The New Typography** — Asymmetry is the movement's signature compositional approach.
- **Active White Space** — Non-axial grouping can make open areas significant; active space also works in centered compositions.
- **Typographic Contrast** — Contrast in type sizes drives asymmetric rhythm.
- **Reading Order** — Spatial emphasis can suggest entry points; continuous text direction and meaningful programmatic/focus sequence need their own checks.

# Common Errors

- **Error**: Using asymmetric elements (bold rules, circles) as decoration while retaining centred structure.
  **Correction**: Asymmetry must be structural, driven by content hierarchy, not a visual style applied to old forms.

# Common Confusions

- **Confusion**: Asymmetry means disorder or randomness.
  **Clarification**: "A striving for order can, and must, also be expressed in asymmetrical form. It is the only way to make a better, more natural order possible."

# Source Reference

"The Principles of the New Typography" (pp. 68-72).

# Verification Notes

Current scoped review: contemporary correctness/scope, local consistency and the exact relationship/CQ occurrences are assessed in Slice26’s batch record. The unavailable edition, translation and page basis leave source fidelity, quotations, figures and historical dates/priority unassessed/input-blocked. No new original read, empirical readability result, browser/AT check or full-standard inspection is claimed.

The following notes are preserved historical extraction assertions, including their old confidence, OCR and uncertainty wording. They are not newly verified results:

- Definition source: Direct quotes from pp. 68-72 of Ch. 12.
- Confidence rationale: High — Tschichold's argument is extended and explicit with clear before/after examples.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: Minor broken spacing. Reconstructed from context.
