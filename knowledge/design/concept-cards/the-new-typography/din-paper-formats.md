---
# === CORE IDENTIFICATION ===
concept: DIN Paper Formats
slug: din-paper-formats

# === CLASSIFICATION ===
category: design-systems
subcategory: format-standards
tier: intermediate
layer: 3-implementation

# === PROVENANCE ===
source: "The New Typography"
source_slug: the-new-typography
authors: "Jan Tschichold"
chapter: "New Typography and Standardization"
chapter_number: 14
pdf_page: 134
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "DIN 476"
  - "A-series paper sizes"
  - "ISO 216"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - standardization-in-design
extends: []
related:
  - the-new-typography
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "1:√2 ratio"
    rating: rigorous
    note: "DIN paper formats use the ratio 1:√2, which ensures that halving a sheet preserves the aspect ratio — a mathematical invariant that makes the system internally consistent."

css_implementation:
  - property: "@page size"
    example: "@page { size: A4; } /* 210mm × 297mm */"
    support: baseline
---

# Quick Definition

The DIN 476 paper standard defines a system of paper sizes based on the 1:√2 proportion, where each size is exactly half the next larger size — starting from A0 (1m²) and producing A1 through A7 by successive halving, giving "good page proportions" with comprehensive economic advantages.

# Core Definition

Tschichold advocates the DIN system as the format standard for all printing: "For business letterheads the most suitable format is A4 (210 × 297 mm), a practical and pleasant size."

The mathematical basis: every page is in the proportion 1:√2 (1:1.41), meaning that "every page size should be in the proportions of 1:√2" — a principle first proposed by Lichtenberg in 1796 and given "partial recognition" during the French Revolution. The key property: successive halving preserves the aspect ratio.

The system is comprehensive: A0 (841 × 1189mm) through A7, with the B-series for cases where A-formats are unsuitable. Poster sizes (DIN A0-A3), letterheads (A4), postcards (A5/A6), and visiting cards all fit within the system.

# Prerequisites

- **Standardization in Design** — DIN formats are the primary concrete implementation of the standardization principle.

# Key Properties

1. **1:√2 proportion**: Halving preserves the aspect ratio — the defining mathematical property.
2. **A0 = 1m²**: The system starts from a sheet of exactly one square metre.
3. **Successive halving**: A1 = A0 halved, A2 = A1 halved, etc.
4. **Main format A4**: 210 × 297mm — the standard for business correspondence and most documents.
5. **Comprehensive**: Covers all printing from posters (A0-A1) to visiting cards (A7).
6. **International adoption**: Used across Europe and becoming international, except North America.

# Construction / Recognition

## To Construct/Create:
1. Start from A0 (841 × 1189mm, area = 1m²).
2. Halve the long dimension to get the next smaller size.
3. Each size maintains the 1:√2 ratio.
4. Choose the appropriate size for the application.

## To Identify/Recognise:
1. Standard sizes: A4 (210 × 297mm), A5 (148 × 210mm), A3 (297 × 420mm).
2. The aspect ratio 1:1.414 is the signature of DIN/ISO paper.

# Context & Application

- **Typical contexts**: All paper-based design, digital document design, print production.
- **Common applications**: A4 documents, A5 booklets, A3 posters, A6 postcards.
- **Historical note**: DIN 476 was adopted in Germany in the early 1920s and became ISO 216 in 1975. It is now the international standard everywhere except the US, Canada, and a few other countries that retain letter/legal sizes.

## Cross-Domain Connections

**Mathematics → RIGOROUS**: The 1:√2 ratio is mathematically invariant under halving — if you cut a 1:√2 rectangle in half along its long side, each half is also 1:√2. This is the unique ratio with this property (proof: if a/b = b/(a/2), then a² = 2b², so a/b = √2). This makes the system self-similar at every scale.

# Examples

**Example 1** (p. 96): The poster sizes: "2 sheet 84 × 120 cm, 1 sheet 60 × 84 cm, Half sheet 42 × 60 cm, Quarter sheet 30 × 42 cm. These sizes represent DIN sizes A0, A1, A2, and A3 rounded to cm."

**Example 2** (p. 110): Letterhead format: "A4 (210 × 297 mm), a practical and pleasant size" — deeper than old quarto, same width as folio, fits existing filing systems.

# Relationships

## Builds Upon
- **Standardization in Design** — DIN formats are the concrete application of the standardization principle.

## Related
- **The New Typography** — DIN formats are part of the movement's practical programme.

# Common Errors

- **Error**: Choosing custom paper sizes for aesthetic reasons.
  **Correction**: "It is usually a sign of incompetence when a non-standard format is insisted on 'for artistic reasons.'"

# Common Confusions

- **Confusion**: Standard formats limit design possibilities.
  **Clarification**: The 1:√2 proportion gives "good page proportions" and "the artistic possibilities of standard formats... are unlimited."

# Source Reference

"New Typography and Standardization" (pp. 93-100). DIN 476 specification reproduced on pp. 97-98.

# Verification Notes

- Definition source: Direct quotes and specifications from Ch. 14.
- Confidence rationale: High — concrete standard with precise measurements and mathematical basis.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. Mathematics parallel (1:√2 ratio) noted as RIGOROUS.
- OCR issues: German specification text partially garbled; measurements verified from standard.
