---
concept: "DIN Paper Formats"
slug: "din-paper-formats"
category: "design-systems"
subcategory: "format-standards"
tier: "intermediate"
layer: "3-implementation"
source: "The New Typography"
source_slug: "the-new-typography"
authors: "Jan Tschichold"
chapter: "New Typography and Standardization"
chapter_number: 14
pdf_page: 134
section: null
extraction_confidence: "high"
aliases:
  - "DIN 476"
  - "A-series paper sizes"
  - "ISO 216"
prerequisites:
  - "standardization-in-design"
extends: []
related:
  - "the-new-typography"
contrasts_with: []
answers_questions: []
rosetta_stone:
  -
    domain: "mathematics"
    concept: "1:√2 ratio"
    rating: "rigorous"
    note: "Ideal 1:√2 rectangles preserve their aspect ratio when the long dimension is halved and the half is rotated. This exact mathematical construction does not make the listed integer-millimetre nominal formats exact copies of that ratio."
css_implementation:
  -
    property: "@page size"
    example: "@page { size: A4; } /* 210mm × 297mm */"
    support: "baseline"
---

# Quick Definition

The card records Tschichold’s advocacy of DIN 476 and its ideal 1:√2 construction: ideal A0 has area 1m² and successive halving generates A1 through A7. Nominal integer-millimetre dimensions approximate that geometry; the recorded "good page proportions" are a design judgment, not universal superiority.

# Core Definition

This section preserves the card’s recorded account of Tschichold’s historical programme; quotations, attributions and page claims have not been checked against the unavailable represented edition. Its polemics are not universal contemporary rules.

The card reports Tschichold advocating the DIN system broadly across printing: "For business letterheads the most suitable format is A4 (210 × 297 mm), a practical and pleasant size."

The recorded ideal mathematical basis is 1:√2 (approximately 1:1.41), expressed as "every page size should be in the proportions of 1:√2" — a principle first proposed by Lichtenberg in 1796 and given "partial recognition" during the French Revolution. The exact preservation property applies to ideal rectangles, not every listed nominal dimension. The Lichtenberg/date/origin narrative is retained as reported history, unverified here.

The card lists nominal A0 (841 × 1189mm) through A7, with a reported B-series alternative. Its poster (DIN A0-A3), letterhead (A4), postcard (A5/A6) and visiting-card examples describe the programme, not mandatory formats for all printed matter.

# Prerequisites

- **Standardization in Design** — DIN formats are the primary concrete implementation of the standardization principle.

# Key Properties

The historical preferences below describe the programme; current use depends on content, audience, language/script, output, constraints and supplied identity.

1. **Ideal 1:√2 proportion**: Halving the long dimension and rotating preserves the ideal aspect ratio; nominal millimetre sizes approximate it.
2. **Ideal versus nominal A0**: Ideal sides are S = 2^(-1/4)m and L = 2^(1/4)m, with area 1m². Nominal 841 × 1189mm has area 0.999949m² and ratio 1189/841 ≈ 1.4137931034, not exactly √2.
3. **Successive ideal halving**: The construction motivates A0–A7. Integer nominal dimensions need separate treatment: 297/2 = 148.5mm, whereas nominal A5 has short side 148mm.
4. **Nominal A4**: 210 × 297mm is the recorded business-correspondence example; selection depends on production and use.
5. **Bounded applicability**: ISO 216:2007’s official abstract covers administrative, commercial and technical paper and certain printed matter, not necessarily books, posters or newspapers. This is an abstract-level check, not a full-standard or tolerance claim.
6. **Compatibility**: Standard formats can help filing, supply and production where the actual workflow uses them; no blanket geographic adoption claim is established here.

# Construction / Recognition

## To Construct/Create:
1. For the mathematical model, start from ideal A0 with the sides above, then halve its long dimension and rotate.
2. For production, choose the required nominal format and verify the actual supplier/output constraints; do not derive a nominal table by exact arithmetic alone.
3. A4 (210 × 297mm), A5 (148 × 210mm) and A3 (297 × 420mm) remain the listed examples.
4. `@page { size: A4; }` requests an A4 page box in CSS; it does not guarantee printer hardware output.

## To Identify/Recognise:
1. Standard sizes: A4 (210 × 297mm), A5 (148 × 210mm), A3 (297 × 420mm).
2. An approximate aspect ratio alone does not establish standard conformance; identify nominal dimensions and the applicable production specification.

# Context & Application

- **Typical contexts**: Paper/document workflows that benefit from the specified formats; neither a screen page width nor every printed object must follow them.
- **Common applications**: A4 documents, A5 booklets, A3 posters, A6 postcards.
- **Historical note (reported, unverified here)**: DIN 476 was adopted in Germany in the early 1920s and became ISO 216 in 1975. It is now the international standard everywhere except the US, Canada, and a few other countries that retain letter/legal sizes.

## Cross-Domain Connections

**Mathematics → RIGOROUS within the ideal model**: Let L > S be long and short sides. After cutting L in half and rotating, preservation requires L/S = S/(L/2), hence L² = 2S² and L/S = √2. This is the unique positive ratio with that property. Ideal A0 has S·L = 2^(-1/4)·2^(1/4) = 1m². Integer-millimetre nominal sizes are approximations, so the proof does not make them exactly self-similar.

# Examples

These are retained reported examples and quoted wording, not newly verified figure, authorship, priority or page evidence.

**Example 1** (p. 96): The poster sizes: "2 sheet 84 × 120 cm, 1 sheet 60 × 84 cm, Half sheet 42 × 60 cm, Quarter sheet 30 × 42 cm. These sizes represent DIN sizes A0, A1, A2, and A3 rounded to cm."

**Example 2** (p. 110): Letterhead format: "A4 (210 × 297 mm), a practical and pleasant size" — with reported comparisons to old quarto, folio and filing systems; those physical comparisons remain unverified here.

# Relationships

## Builds Upon
- **Standardization in Design** — DIN formats are the concrete application of the standardization principle.

## Related
- **The New Typography** — DIN formats are part of the movement's practical programme.

# Common Errors

- **Error**: Ignoring actual production, storage and content requirements when choosing a format.
  **Correction**: The recorded polemic says "It is usually a sign of incompetence when a non-standard format is insisted on 'for artistic reasons.'" Contemporary custom formats can be justified by content, identity or production; compare trade-offs rather than diagnosing incompetence.

# Common Confusions

- **Confusion**: Standard formats necessarily prevent expression, or guarantee better design.
  **Clarification**: Tschichold praises "good page proportions" and says "the artistic possibilities of standard formats... are unlimited." These are reported aesthetic claims; standards can support a workflow without determining its composition.

# Source Reference

"New Typography and Standardization" (pp. 93-100). DIN 476 specification reproduced on pp. 97-98.

# Verification Notes

Current scoped review: contemporary correctness/scope, local consistency and the exact relationship/CQ occurrences are assessed in Slice26’s batch record. The unavailable edition, translation and page basis leave source fidelity, quotations, figures and historical dates/priority unassessed/input-blocked. No new original read, empirical readability result, browser/AT check or full-standard inspection is claimed.

The following notes are preserved historical extraction assertions, including their old confidence, OCR and uncertainty wording. They are not newly verified results:

- Definition source: Direct quotes and specifications from Ch. 14.
- Confidence rationale: High — concrete standard with precise measurements and mathematical basis.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. Mathematics parallel (1:√2 ratio) noted as RIGOROUS.
- OCR issues: German specification text partially garbled; measurements verified from standard.
