---
concept: "Musical Interval ↔ Typographic Ratio (Rosetta Stone)"
slug: "musical-interval-typographic-ratio"
category: "design-principles"
subcategory: "cross-domain-mapping"
tier: "advanced"
layer: "1-principles"
source: "More Meaningful Typography"
source_slug: "posts"
authors: "Tim Brown"
chapter: "Modular scales and how they apply to web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases:
  -
    - "harmonic ratios in typography"
    - "musical ratios for type"
    - "interval-based scale ratios"
prerequisites:
  - "scale-ratio"
  - "modular-scale"
  - "golden-ratio"
extends:
  - "scale-ratio"
  - "ratio-selection-criteria"
related:
  - "modular-scale-construction"
  - "typographic-rhythm-modular-scale"
contrasts_with: []
answers_questions:
  - "What is the mathematical relationship between musical intervals and typographic scale ratios?"
  - "Why must visual scales be geometric (multiplicative) rather than arithmetic (additive)?"
  - "How do you select an appropriate scale ratio for a given design context?"
rosetta_stone:
  -
    domain: "music"
    concept: "A chosen positive frequency ratio reused as a type-size multiplier"
    rating: "rigorous"
    note: "If a chosen frequency pair has ratio r and a type-size step is defined using that same r, the numerical factor is identical. For example, 300/200 = 24/16 = 3/2. This conditional arithmetic does not establish a tuning-system identity, an interval-name table, consonance, or visual harmony; those claims need separate evidence."
  -
    domain: "mathematics"
    concept: "One positive factor reused across quantities; rationality is a separate property"
    rating: "rigorous"
    note: "For declared positive bases and r>0, sequences a*r^n and b*r^n share the same adjacent factor. This does not imply that every musical scale is geometric or that every interval ratio is a small-integer fraction. Exact 4/3 differs from decimal 1.333=1333/1000; exact irrational φ differs from rational decimal 1.618=809/500. Brown’s inspected article does not enumerate the legacy interval table."
css_implementation:
  -
    property: "font-size (via scale ratio)"
    example: "/* Independent numeric illustration; base 16px, unrounded generation, two-place display. No type-role default or verified musical label. */ /* Exact r=4/3 */ .r43-step0 { font-size: 16.00px; } .r43-step1 { font-size: 21.33px; } .r43-step2 { font-size: 28.44px; } /* Decimal r=1.333 */ .r1333-step0 { font-size: 16.00px; } .r1333-step1 { font-size: 21.33px; } .r1333-step2 { font-size: 28.43px; } /* Exact r=3/2 */ .r32-step0 { font-size: 16.00px; } .r32-step1 { font-size: 24.00px; } .r32-step2 { font-size: 36.00px; }"
    support: "baseline"
---
# Quick Definition

A designer may reuse a chosen positive frequency ratio `r` as a type-size multiplier. The number is the same only when both choices declare that same factor; this conditional arithmetic does not make music and typography one system or establish consonance or visual harmony.

# Core Definition

Brown's prepared article opens by saying that meaningful ratios rooted in “geometry, music, nature, and history” can be expressed as modular scales (lines 109–112). Later Brown quotes Bringhurst: “A modular scale, like a musical scale, is a prearranged set of harmonious proportions” (lines 133–140). Brown then describes generating values from a ratio and a starting number and combining strands (lines 142–156). These passages establish an invocation, an attributed comparison and a construction procedure. They do not enumerate an interval-name/value table or verify tuning, consonance, a complete ratio menu, or a perceptual effect.

If a selected pair of frequencies has ratio `r`, and a type-size step is also defined with `r`, the numerical factor is identical. For example, `300/200 = 24/16 = 3/2`. This identity is an equation between declared quantities; it does not transfer a musical judgment to type.

For positive bases `a` and `b`, a declared common factor `r>0` generates strands `a*r^n` and `b*r^n`. Each strand has adjacent indexed quotient `r` by construction. This does not imply that every musical scale is geometric, every musical frequency ratio is rational or a small-integer fraction, or that type sizes must follow music. A geometric strand is one available model; independent values such as `10, 20, 30` have equal additive gaps of `10` and unequal adjacent ratios `2` and `1.5`.

The former card's named examples are retained below as legacy associations. Their numeric fractions and decimal arithmetic are checked here; interval names, tuning systems and typographic applications are unassessed. Keeping a label as historical card content does not certify it, and lack of inspection does not show that it is false.

# Prerequisites

- **Scale ratio** — A declared multiplier can generate one typographic strand; no musical origin is required.
- **Modular scale** — The card concerns an optional ratio-generated construction, not a rule that every visual scale use one.
- **Golden ratio** — The earlier card contrasted φ with musical ratios. This review distinguishes exact irrational φ from rational decimal `1.618`; irrationality alone does not establish musical exclusion, consonance or beauty.

These are retained navigation relationships. The seven field occurrences and their local direction, rationale and unresolved edge support are itemized in the batch record; a valid endpoint does not by itself verify an edge.

# Key Properties

1. **Conditional numerical reuse**: If a chosen frequency pair and a chosen type-size step use the same `r`, the factor is numerically identical. The domains and any judgments about them remain separate.
2. **Declared construction**: A strand `a*r^n` is geometric under its declared positive base and ratio. This is a property of that construction, not a universal property of music or visual scales.
3. **Exact and decimal values differ**: `4/3` is not `1.333`, which equals `1333/1000`; the difference is `1/3000`. For base `16`, exact `4/3` gives `16`, `64/3`, `256/9`, displayed `16.00`, `21.33`, `28.44` at two-place half-even rounding. Decimal `1.333` gives `16`, `21.328`, `28.430224`, displayed `16.00`, `21.33`, `28.43`. The first rounded step hides the different models; the second distinguishes them.
4. **Compute from the unrounded base**: Do not feed a displayed rounded step into the next multiplication. Exact `3/2` from `16` yields `16`, `24`, `36`.
5. **φ and its decimal approximation differ**: Exact `φ=(1+√5)/2` is irrational; decimal `1.618=809/500` is rational. This arithmetic distinction does not decide whether an interval is used or consonant, or whether a type scale is pleasing.
6. **No prescribed ratio menu or role**: Brown's prepared article does not supply the interval table represented by the card's earlier labels. The calculations below are independent numeric illustrations, not type-role defaults or verified musical labels.

# Construction / Recognition

## To Construct/Create:
1. State the design context and fixed inputs. A musical or historical association is optional.
2. If using a geometric strand, declare its positive base and ratio.
3. Generate each term from the unrounded base; document the precision and display-rounding rule.
4. Inspect the actual type, content and layout. Keep permitted fixed, additive or optical exceptions where they serve the project.
5. If reusing a frequency ratio, state the selected pair and independently chosen type multiplier so the conditional equality is explicit. Do not infer a default from a musical label.

## To Identify/Recognise:
1. Check which exact or decimal factor is declared and whether each displayed value was computed from the unrounded base.
2. Keep a source's report, an independently derived calculation and a legacy domain label distinct.
3. Treat named interval/value associations, tuning assumptions and perceptual claims as unresolved unless their own evidence is inspected.

# Context & Application

- **Typical contexts**: Explaining a deliberately shared numerical factor, or documenting an optional ratio-generated type scale.
- **Common applications**: State the context, base and ratio; calculate unrounded values; document precision; inspect actual type and retain justified exceptions. Independent selection can also fit content or fixed inputs.
- **Historical/stylistic notes**: Brown invokes music and quotes Bringhurst's comparison. His prepared article does not confer “classic,” “bold,” “editorial,” or other style character on the legacy interval labels. This card does not inspect the cited book, talk or calculator contents.

## Cross-Domain Connections

**Music → conditional arithmetic**: A selected frequency pair and a separately chosen type step share the numerical factor when both are defined by the same `r`. Example: `300/200 = 24/16 = 3/2`. This does not verify an interval-name table, tuning-system identity, consonance or visual harmony.

**Mathematics → declared model**: For positive `a`, `b` and `r`, strands `a*r^n` and `b*r^n` share adjacent factor `r`; that follows from their construction. Exact and decimal inputs can produce different later results even where rounded first steps coincide. Rigor in the two retained metadata mappings applies only to this explicitly declared arithmetic, not to the music domain or every source claim.

# Examples

**Example 1 (Brown's prepared-source examples):** The opening says: “This and other meaningful ratios rooted in geometry, music, nature, and history can be expressed as modular scales and put to work on the web” (lines 109–112). Later Brown quotes Bringhurst: “A modular scale, like a musical scale, is a prearranged set of harmonious proportions” (lines 133–140). These are source statements, not a complete interval table or independent proof of shared systems or perceptual results.

**Example 2 (numeric reuse):** `300/200 = 24/16 = 3/2`. Both fractions reduce to `3/2`. This illustrates conditional factor reuse only.

**Example 3 (retained legacy associations, labels unassessed):** The prior card listed octave `2:1 = 2`, major second `9:8 = 1.125`, minor third `6:5 = 1.2`, major third `5:4 = 1.25`, perfect fourth `4:3 ≈ 1.333`, and perfect fifth `3:2 = 1.5`. Their fraction/decimal arithmetic is shown; this review does not assess interval names, tuning context, or mapping to typographic applications. Exact `4/3` is approximately `1.333333…`, not decimal `1.333`.

**Example 4 (independent scale arithmetic):** With base `16`, exact `r=4/3` yields `16`, `64/3`, `256/9`; two-place half-even display is `16.00`, `21.33`, `28.44`. With decimal `r=1.333=1333/1000`, it yields `16`, `21.328`, `28.430224`; display is `16.00`, `21.33`, `28.43`. Generate each term from `16`, not from rounded `21.33`.

**Example 5 (exact and decimal φ):** Exact `φ=(1+√5)/2` is irrational, whereas decimal `1.618=809/500` is rational. Exactness alone says nothing about musical exclusion, consonance or aesthetic result.

**Example 6 (contrary construction):** `10, 20, 30` has equal additive gaps `10` and adjacent ratios `2` then `1.5`. It refutes a claim that every visual scale must have a constant ratio. It does not establish that this sequence suits any particular typography.

# Relationships

## Builds Upon
- **Scale ratio** — Editorial prerequisite: understanding a declared multiplier helps explain the optional type strand. A musical origin is not necessary.
- **Modular scale** — Editorial prerequisite: this card explains one possible ratio-generated strand, while additive and independent choices remain possible.
- **Golden ratio** — Editorial comparison: it clarifies exact φ versus decimal `1.618`; it does not show that φ is excluded from music or visually beneficial.

## Enables
- **Scale ratio** — This card supplies a conditional cross-domain example; whether it elaborates the endpoint concept remains an editorial edge assessment.
- **Ratio selection criteria** — It offers one optional consideration, not a required selection rule or supported interval menu.

## Related
- **Modular scale construction** — The ratio example can be used in a declared construction; this does not establish a musical source table.
- **Typographic rhythm via modular scale** — Brown's quotation is an analogy; this review does not establish rhythmic equivalence or perceptual benefit.

## Contrasts With
- **Arbitrary ratio selection** — Earlier body prose framed this as a contrast, but no `contrasts_with` metadata edge is recorded. This review does not treat a convenient or independently chosen ratio as invalid.

# Common Errors

- **Error**: Treating the analogy as proof that musical and typographic scales are the same system.
  **Correction**: Only the numerical factor is shared when both choices explicitly use the same `r`; source attribution, domain truth and perceptual claims have separate warrants.

- **Error**: Treating every visual scale as necessarily geometric.
  **Correction**: A geometric strand is optional. Additive `10, 20, 30` has equal gaps and unequal adjacent ratios; neither construction alone proves typographic suitability.

- **Error**: Treating `4/3` and decimal `1.333` as identical, or generating a later step from a rounded display.
  **Correction**: `4/3` differs from `1333/1000` by `1/3000`; compute each term from the unrounded base and round only for display.

- **Error**: Treating the old interval-name menu or style adjectives as verified by Brown's article.
  **Correction**: Retain those names and values as legacy associations with unassessed interval/tuning/application labels. Brown invokes music and quotes an analogy but does not enumerate the table. Its absence from this article does not establish a label is false.

- **Error**: Treating irrationality of exact φ as evidence of musical exclusion, consonance or beauty.
  **Correction**: Irrationality distinguishes φ from every rational number; the music and perceptual questions need separate evidence.

# Common Confusions

- **Confusion**: A shared factor means the physical quantities or their domain judgments are equivalent.
  **Clarification**: The factor is numerically equal under the stated condition. Frequency and type size remain different quantities.

- **Confusion**: A geometric strand is required for every visual scale.
  **Clarification**: The original question is answered directly: it is not required. Additive or independent values are possible; evaluate the actual design separately.

- **Confusion**: A first rounded display proves two input models are identical.
  **Clarification**: Exact `4/3` and decimal `1.333` both display `21.33` at the first step from base `16`, but their second-step displays differ (`28.44` versus `28.43`).

- **Confusion**: A rigorous mapping rating verifies the entire music mapping.
  **Clarification**: The retained ratings apply only to explicitly declared arithmetic. They do not verify the music domain, the legacy interval table, Brown's full account or every claim in this card.

# Source Reference

Opening paragraph; "Modular scales and how they apply to web design" (Bringhurst quote); "Further Reading" (reference to "More Perfect Typography" talk) — More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- **Historical extraction record**: Extraction confidence remains `medium`, and the earlier OCR observation remains “None significant.” These are preserved observations about the prior extraction act, not current source-fidelity or semantic acceptance.
- **Superseded claims**: The earlier “partially verified” cross-reference, interval-table attribution, broad music/typography identity, perceptual parallel, geometric-sequence equivalence, φ exception and style prescriptions describe the former card. They are not current verified facts. Legacy interval names and values remain visible as unassessed associations; their arithmetic is checked independently.
- **Current bounded review**: Prepared Brown lines 109–112 invoke music; 133–140 quote Bringhurst's comparison; 142–156 describe ratio generation and merging. These support those attributed observations and the procedure, not an interval-name/value table, complete menu, tuning claim or perceptual benefit. Original capture identity/fidelity remains unresolved under P10-11.
- **Technical result**: Exact rational arithmetic distinguishes `4/3` from `1.333=1333/1000` (difference `1/3000`), and exact irrational φ from decimal `1.618=809/500`. Two-place half-even values are derived from the unrounded base. The `rigorous` mapping ratings are preserved but scoped to explicitly declared arithmetic only; they do not grade the music domain or all source claims.
- **Relationships and questions**: The header's seven relation occurrences and three questions remain unchanged. The batch record itemizes each occurrence and question with endpoints, direction, inspected components, source/math mapping and unresolved limits. Resolved slugs and partial endpoint sections do not establish edge support or complete answerability.
- **Limits**: No interval-name verification, new music/tuning inquiry, empirical harmony test, complete endpoint/global review, browser/accessibility claim or original-source acceptance was performed. CDC independent review remains pending.
