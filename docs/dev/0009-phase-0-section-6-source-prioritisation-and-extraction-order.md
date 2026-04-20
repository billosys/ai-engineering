# Phase 0 - Section 6 - Source Prioritisation and Extraction Order

## 6. Source Prioritisation and Extraction Order

### 6.1 Extraction Waves

Sources are organised into waves by strategic value. Each wave should be fully extracted, validated, and ingested into the graph DB before the next wave begins.

**Source assessment protocol.** For any source not listed below, perform a source assessment (see extraction prompt template, Phase 0.5) before beginning extraction. Document: OCR quality, prose style, structural features, key chapters, estimated card count, and recommended agent architecture. Save assessment notes in the post-mortem.

#### Wave 1 — Immediate Practical Impact (Free + Critical Paid)

These sources provide the fastest path to usable knowledge for the target user.

| Priority | Source | Category Coverage | Est. Cards | Acquisition |
|----------|--------|-------------------|------------|-------------|
| 1 | **Refactoring UI** (Wathan & Schoger) | `colour-theory`, `typography`, `layout-composition`, `design-principles` | 80-120 | PDF, $79-149 |
| 2 | **Laws of UX** (Yablonski, lawsofux.com) | `visual-perception`, `interaction-design`, `design-principles` | 30-40 | Free website |
| 3 | **The Vignelli Canon** (Vignelli, free PDF) | `design-principles`, `typography`, `layout-composition`, `visual-identity` | 25-35 | Free PDF |
| 4 | **Atomic Design** (Frost, free online) | `design-systems` | 20-30 | Free website |
| 5 | **Practical Typography** (Butterick, free) | `typography` | 30-40 | Free web book |
| 6 | **Utopia blog + calculators** | `typography`, `layout-composition`, `design-systems` | 15-25 | Free website |
| 7 | **ModernCSS.dev** (Eckles) | `layout-composition`, `accessibility` | 20-30 | Free website |

**Wave 1 estimated total: 220-320 concept cards**

#### Wave 2 — Deep Foundations

These provide the perceptual science, mathematical rigour, and canonical design theory.

| Priority | Source | Category Coverage | Est. Cards | Acquisition |
|----------|--------|-------------------|------------|-------------|
| 8 | **Interaction of Color** (Albers) | `colour-theory`, `visual-perception` | 40-60 | Print, ~$25 |
| 9 | **Elements of Typographic Style** (Bringhurst) | `typography`, `layout-composition` | 60-80 | Print, ~$25 |
| 10 | **Design of Everyday Things** (Norman) | `interaction-design`, `visual-perception` | 40-50 | Ebook, ~$15 |
| 11 | **Thinking with Type** (Lupton, 3rd ed 2024) | `typography`, `layout-composition` | 40-50 | Print, ~$25 |
| 12 | **Grid Systems in Graphic Design** (Müller-Brockmann) | `layout-composition` | 30-40 | Print, ~$50 |

**Wave 2 estimated total: 210-280 concept cards**

#### Wave 3 — Advanced & Supplementary

| Priority | Source | Category Coverage | Est. Cards | Acquisition |
|----------|--------|-------------------|------------|-------------|
| 13 | **Elements of Color** (Itten, condensed) | `colour-theory` | 20-30 | Print, ~$30 |
| 14 | **Don't Make Me Think** (Krug) | `interaction-design`, `information-architecture` | 20-25 | Print/ebook, ~$20 |
| 15 | **Every Layout** (Pickering & Bell) | `layout-composition`, `design-systems` | 20-30 | Paid website, ~$70 |
| 16 | **Art and Visual Perception** (Arnheim) | `visual-perception`, `visual-elements` | 40-60 | Print, ~$25 |
| 17 | **Information Visualization** (Ware, 4th ed) | `visual-perception`, `data-visualisation` | 50-70 | Print, ~$60 |

**Wave 3 estimated total: 150-215 concept cards**

#### Wave 4 — Living Sources (Ongoing Extraction)

These are continuously updated resources that should be revisited periodically.

| Source | Category Coverage | Notes |
|--------|-------------------|-------|
| Material Design 3 documentation | `design-systems`, all visual categories | Living reference implementation |
| Apple Human Interface Guidelines | `interaction-design`, `design-systems` | Platform-specific but principle-rich |
| IBM Carbon documentation | `design-systems`, `accessibility` | Strong accessibility focus |
| Shopify Polaris documentation | `design-systems`, `design-principles` | Strong governance documentation |
| GitHub Primer documentation | `design-systems` | Strong token architecture |
| W3C DTCG specification | `design-systems` | The emerging standard for design tokens |
| Josh Comeau's blog | `layout-composition`, `motion-design` | Deep CSS mental models |
| Nielsen Norman Group articles | `interaction-design`, `information-architecture` | Evidence-based UX research |
| Google Fonts Knowledge | `typography` | Variable fonts, optical sizing |

### 6.2 Source-Specific Extraction Notes

**Refactoring UI** — This is the single most important source for Wave 1. It is written for the target user (developer who needs to design). Extract every tactical pattern as a concept card. Pay special attention to the "before/after" examples — each one illustrates a principle violation and its correction, which maps directly to diagnostic competency questions. The book doesn't use formal terminology consistently, so concept cards should add the canonical design vocabulary as `aliases` (e.g., if the book says "make some things big and some things small" without using the term "visual hierarchy," the card should use `visual-hierarchy` as the concept name with the book's phrasing as context). This is a prescription-heavy source (see Section 9.2, item 11): most concepts are defined through tactical rules and before/after demonstrations rather than formal definitions. Synthesise Core Definitions from the book's prescriptions and their stated rationale.

**Laws of UX** — Near-perfect concept card source. Each law is already atomic, has a psychological foundation, and includes practical applications. The main extraction work is adding `prerequisites`, `related`, and `contrasts_with` relationships that the website doesn't make explicit, and connecting each law to the mathematical formulation where one exists (Fitts's, Hick's, Stevens's, Weber's).

**Albers, *Interaction of Color*** — Structured as sequential exercises, not as a reference. The extraction challenge is that Albers teaches through *demonstration*, not definition. Concept cards will need to synthesise definitions from his exercises. Set `extraction_confidence: medium` for most cards and note "Synthesised from Albers's exercise on pp. X-Y" in verification notes.

**Bringhurst** — Extremely rich but print-focused. Extract the principles and proportional systems; flag any concept that is specifically about print composition and note its web equivalent (or lack thereof) in Context & Application.

**Every Layout** — The 13 layout primitives map directly to concept cards. The philosophy ("composition over inheritance") maps to a design-principles card. Each primitive has clear prerequisites, construction steps, and use cases. This source is unusually well-suited to our card format.

**Munsell Color System** (Cleland, *A Practical Description of the Munsell Color System*) — ~20 pages, 19 cards. OCR quality: poor in Chapter 8 (Balance), with repeated text blocks around worked examples. Prose style: 1920s discursive narrative; definitions embedded in flowing text with no section headings or bullet lists. Extraction requires careful close-reading. Key chapters: 4-9 (Hue, Value, Chroma, Complementary Colours, Balance). Architecture: serial extraction (under 25 cards). Categories: primarily `colour-theory` with some `visual-perception`. Tiers: primarily foundational.

**Practical Typography** (Butterick, practicaltypography.com) — 156 source files, 37 cards extracted. Prose style: prescriptive and opinionated. Butterick defines by rule ("do this, don't do that") rather than formal definition; every Core Definition required synthesis from his prescriptions and rationale (see Section 9.2, item 11). The source is naturally card-shaped — each web page covers one focused topic. Categories: primarily `typography` (81%), with `layout-composition` (16%) and `design-principles` (3%). Tiers: mostly foundational and intermediate; only 1 advanced card, which correctly reflects the general-audience level. No Rosetta Stone mappings. Architecture: serial extraction (37 cards). The HTML-to-Markdown conversion was clean; no OCR issues.
