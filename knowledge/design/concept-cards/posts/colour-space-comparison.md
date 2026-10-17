---
concept: "Colour Space Comparison (Oklab vs CIELAB vs HSL)"
slug: "colour-space-comparison"
category: "colour-theory"
subcategory: "perceptual colour models"
tier: "advanced"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "What about existing models?"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases: []
prerequisites:
  - "perceptual-uniformity"
  - "oklab"
  - "colour-space"
  - "chroma-perceptual"
  - "lightness-perceptual"
extends:
  - "perceptual-uniformity"
related:
  - "colour-interpolation-perceptual"
  - "gamut-srgb"
contrasts_with: []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
  - "How do you construct a palette that changes lightness uniformly across hues?"
rosetta_stone: []
css_implementation:
  -
    property: "color"
    example: "color: oklab(0.7 0.1 -0.08);"
    support: "baseline"
  -
    property: "color"
    example: "color: hsl(200deg 50% 60%);"
    support: "baseline"
---

# Quick Definition
Ottosson compares selected colour models using stated datasets and error measures. The results describe those tests; they are not a universal ranking.

# Core Definition
The prepared article compares Oklab, CIELAB, CIELUV, OSA-UCS, IPT, JzAzBz, HSV and CAM16-UCS. Its table includes HSV, not HSL. The lightness and chroma pairs were generated with CAM16 under normal viewing conditions and limited to Pointer’s Gamut; perceived-hue pairs come from a separate uniform-perceived-hue dataset used to derive IPT. The generated L/C data are not experimental human ground truth. Preserve each reported value as an attributed result scoped to its dataset and metric; do not transfer the CAM16 generation claim to the separate hue data. The author’s qualitative assessments describe those tested models and tasks, not categorical usability across all work.

Error table (RMS errors; best non-CAM16 in bold):

| Metric | Oklab | CIELAB | CIELUV | OSA-UCS | IPT | JzAzBz | HSV |
|--------|-------|--------|--------|---------|-----|--------|-----|
| L RMS  | **0.20** | 1.70 | 1.72 | 2.05 | 4.92 | 2.38 | 11.59 |
| C RMS  | **0.81** | 1.84 | 2.32 | 1.28 | 2.18 | 1.79 | 3.38 |
| H RMS  | 0.49 | 0.69 | 0.68 | 0.49 | 0.48 | **0.43** | 1.10 |

# Prerequisites

- **Perceptual uniformity** — The comparison is structured around which spaces achieve it.
- **Oklab** — The primary space being advocated.
- **Colour space** — Background on what each space is.
- **Chroma (perceptual)** and **Lightness (perceptual)** — The metrics being compared.

# Key Properties
1. The seven displayed non-CAM16 RMS columns and values are retained from the article.
2. 1.70/0.20=8.5 is the table's L RMS ratio, not an 8.5-fold perceptual-quality result.
3. HSV appears in the table; HSL does not.
4. Metric rankings do not establish universal superiority; CAM16-derived reference data are not independent human ground truth.
5. Source plot descriptions are attributed and were not visually inspected here.

# Construction / Recognition

## To Construct/Create:
1. The article's coordinate-swap method selects relevant pairs and swaps the tested coordinate.
2. It measures two colour differences for each pair and retains the smaller difference before computing RMS across pairs.
3. Interpret values with the stated dataset, metric, coordinate scaling and CAM16-derived reference caveat. This is a method readback, not an independent reproduction.

## To Identify/Recognise:
1. Read each result as a dataset- and metric-specific prediction error.
2. A low L RMS alone does not prove all constant-L hue sweeps look even.
3. Plot descriptions support only their stated examples and conditions.

# Context & Application

- **Typical contexts**: Comparing model predictions for the article’s named datasets and metrics.
- **Common applications**: Treat the table as one scoped input to a task-specific choice, then assess the intended data, output gamut and rendered use.

# Examples

**Example 1** (from source): Blending white with blue: Oklab produces no hue shift; CIELAB, CIELUV, and HSV all shift toward purple. CAM16 desaturates rapidly. (Section: "Blending colors")

**Example 2** (from source): Munsell chroma data plotted in each space: Oklab and CAM16 produce near-circular rings; CIELAB, CIELUV, IPT, and OSA-UCS all show distorted rings. (Section: "Munsell data")

**Example 3** (from source): Luo-Rigg ellipses: "The shape of the full gamut is quite odd in CIELAB and OSA-UCS, which likely means that their predictions are quite bad for highly saturated colors." (Section: "Luo-Rigg dataset and full gamut")

# Relationships
## Builds Upon
- **Perceptual uniformity** — The comparison operationalizes selected measures.
- **Individual colour models** — Needed to interpret reported metrics.

## Enables
- **Colour-space selection** — Provides one scoped input to a task-specific choice.
- **Tradeoff analysis** — Keeps reported metrics separate.

## Related
- **Colour interpolation** — The article reports selected blend examples.
- **Chroma / Lightness** — Included as metrics.

## Contrasts With
- **HSV** — Included in the table; HSL is not.
- **CIELAB** — The article reports selected outcomes, not categorical unusability.

# Common Errors
- **Error**: Treating 8.5× lower L RMS as 8.5× better perception.
  **Correction**: It is the ratio of the reported L RMS values under the article's data and method.
- **Error**: Applying the HSV measurements to HSL or all design tasks.
  **Correction**: Keep model, dataset and metric explicit.

# Common Confusions
- **Confusion**: The smallest RMS makes a model best overall.
  **Clarification**: The table separates metrics and uses CAM16-derived predictions; it is not independent human ground truth.

# Source Reference

"What about existing models?"; "Comparison with other color spaces"; "Blending colors"; "Munsell data"; "Luo-Rigg dataset and full gamut" sections.

# Verification Notes
Seven non-CAM16 columns were checked against the prepared comparison table. The method readback includes the per-pair minimum before RMS. No experiment was reproduced and source plots were not visually inspected.
