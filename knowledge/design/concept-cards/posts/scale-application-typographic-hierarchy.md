---
concept: "Scale Application to Typographic Hierarchy"
slug: "scale-application-typographic-hierarchy"
category: "typography"
subcategory: "type-hierarchy"
tier: "intermediate"
layer: "2-domain"
source: "More Meaningful Typography"
source_slug: "posts"
authors: "Tim Brown"
chapter: "Applying a modular scale in web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "applying a modular scale"
    - "type hierarchy from scale"
    - "scale-based sizing"
prerequisites:
  - "modular-scale"
  - "modular-scale-construction"
  - "scale-ratio"
extends:
  - "modular-scale"
related:
  - "typographic-rhythm-modular-scale"
  - "scale-base-unit"
contrasts_with: []
answers_questions:
  - "What distinguishes a modular scale from arbitrary type size selection?"
  - "What makes a type hierarchy feel harmonious vs arbitrary?"
  - "How do you construct a modular scale for a typographic system?"
rosetta_stone: []
css_implementation:
  -
    property: "font-size"
    example: "body { font-size: 18px; } /* scale origin */ h1 { font-size: 29.124px; } /* one step up */ h2 { font-size: 190px; } /* scale origin, second strand */ .side p { font-size: 15px; } /* improvised */"
    support: "baseline"
  -
    property: "width"
    example: ".main { width: 497.406px; } /* scale-derived measure */ .group { width: 845.479px; } /* scale-derived container */"
    support: "baseline"
  -
    property: "margin"
    example: "h1 { margin: 44.856px 0 0 307.420px; } /* scale values */ .side { margin: 27.723px 29.124px 0 0; } /* scale values */"
    support: "baseline"
  -
    property: "line-height"
    example: "p { line-height: 1.54; } /* Brown example: visually selected */ p.intro { line-height: 1.394; /* 1.54 - 0.146 */ } /* Brown comment math; not a universal line-height */"
    support: "baseline"
---

# Quick Definition

Scale application is an optional design method: a designer may select or adapt values from a constructed modular scale for chosen CSS measurements. Brown presents it as a contextual aid to visual decisions, not a rule that every measurement must come from one scale or sequence.

# Core Definition

Brown describes the application phase directly: "Having marked up my text, and with my scale at my side, I applied CSS rules to our example, grabbing an exact number from my scale for each decision. Throughout the process, I made educated guesses that built a harmonious composition, one measurement at a time."

Brown lists type sizes, line height, line length, margins, column widths, and other measurements as possible applications. His worked example also shows limits: the 15px caption is explicitly outside the scale; the 20px heading margin is an optical adjustment; and the 274px sidebar width came from resizing an image to 190px high. These are contextual choices, not scale-derived defaults.

The application process is iterative and visual, not mechanical: "I alternate between CSS editor and browser, checking to see how each value looks... I keep an eye on the overall density of my paragraphs (typographic color) and the readability of the text as a whole."

Brown explicitly endorses improvisation: scale values are "educated suggestions." Designers may round, combine, or use non-scale values when a contextual visual choice works better. His 18px body size, 29.124px heading, 190px display heading, 497.406px measure, 845.479px container, and margin examples describe one historical composition; they are not universal recommendations. The separate sequences in a double-stranded scale also need not form one geometric sequence.

# Prerequisites

- **Modular scale** — You must have a constructed scale before you can apply it.
- **Modular scale construction** — The procedure that produces the scale to be applied.
- **Scale ratio** — Understanding the ratio determines what values are available.

# Key Properties

1. **Selected scope**: A designer may use scale values for selected type sizes, line heights, widths, or margins; other values may be chosen optically or for the content and assets.
2. **Iterative visual testing**: Values are tried, viewed in the browser, and adjusted; visual judgment arbitrates between adjacent scale options.
3. **Permissive improvisation**: Non-scale values are acceptable when they suit the design; Brown documents several such decisions.
4. **Comment math**: Brown records arithmetic for a combined value. The source states `21.178px` from `27.723 - 6.545`; the displayed arithmetic gives `21.178`. For line height, `1.54 - 0.146 = 1.394`. By contrast, `18 × 1.54 = 27.72`, not `27.723`. Nearby values or their comments do not by themselves establish scale membership.
5. **Brown's fallback approach**: For his typeface-specific composition, Brown reports specifying baseline fonts and generic measurements before preferred-font and scale-based styles. This is a contextual strategy; fallback adequacy and current browser behavior require testing.

# Construction / Recognition

## To Construct/Create:
1. Establish the content, typeface, assets, and visual context before deciding whether a scale will help.
2. Select scale values for measurements where they support the composition; test and adjust them visually.
3. Choose other values when optical alignment, comfortable reading, image dimensions, or another project constraint calls for them.
4. Record meaningful arithmetic or design rationale in CSS comments when it helps explain a choice.
5. Where typeface-specific measurements depend on a preferred font, provide suitable fallback styles; Brown's example discusses this as one progressive-enhancement approach.

## To Identify/Recognise:
1. Check whether type sizes in the CSS correspond to values in a geometric sequence.
2. Check which widths and margins are asserted to come from a scale; verify each against the declared scale rather than assuming one sequence.
3. Look for CSS comment math documenting combinations.
4. Look for the scale URL or parameters in a CSS header comment.

# Context & Application

- **Typical contexts**: Full-page editorial web design; any project where a modular scale has been constructed.
- **Common applications**: Selecting some type sizes and spatial measurements from a scale, with other values chosen for their context.
- **Historical/stylistic notes**: Brown's prepared article contains a worked CSS example with numeric values and his explanations. The inspected inputs do not establish a ranking against other public examples.

# Examples

**Example 1 — Font sizes** (from source, "Applying a modular scale in web design"):
- `body { font-size: 18px; }` — scale origin
- `h1 { font-size: 29.124px; }` — an example value Brown describes as selected from his scale
- `h2 { font-size: 190px; }` — second scale origin
- `.side p { font-size: 15px; }` — improvised (not in scale)
- `p.intro { font-size: 21.178px; /* 27.723 - 6.545 */ }` — Brown's stated comment math

**Example 2 — Column widths** (from source):
- `.main { width: 497.406px; }` — Brown's visually selected measure after testing alternatives
- `.group { width: 845.479px; }` — Brown's contextual container example
- `.side { width: 274px; }` — chosen in a composition after resizing an image to 190px high; the passage does not assert scale membership for 274px

**Example 3 — Margins** (from source):
- `h1 { margin: 44.856px 0 0 307.420px; }` — both values from scale
- `.side { margin: 27.723px 29.124px 0 0; }` — Brown's example values
- `h2 { margin-left: 20px; /* Optical alignment */ }` — Brown says this value does not come from his scale

**Example 4 — Improvisation** (from source):
"Modular scales are a tool, they're not magic. They're not going to work for every measurement, and that's okay. Math is no substitute for an experienced designer's eye, but it can provide both hints and constraints for decision making."

# Relationships

## Builds Upon
- **Modular scale** — Application is the use of the constructed scale.
- **Modular scale construction** — The constructed scale is the prerequisite for application.

## Enables
- **Typographic rhythm via modular scale** — This is an optional interpretive relationship; a scale does not guarantee a perceptual outcome.

## Related
- **Typographic color** — Brown cites monitoring "typographic color" (density of the text block) as part of the visual testing in application.
- **Progressive enhancement** — Fallback CSS strategy is discussed as part of the application practice.

## Contrasts With
- **Arbitrary measurement** — "The arbitrary dimensional choices I used to make had nothing to do with my intended designs' underlying meaning. At best, I chose ballpark measurements in CSS, command-tabbed over to my browser, and eyeballed the results."

# Common Errors

- **Error**: Assuming a scale must govern every measurement.
  **Correction**: Brown names many possible applications but also describes improvisation and values he selected for optical or image-related reasons.

- **Error**: Treating the scale as a mechanical rule that eliminates the need for visual judgment.
  **Correction**: "I alternate between CSS editor and browser, checking to see how each value looks." Brown's process involves constant visual testing, not just numerical assignment.

- **Error**: Forgetting to provide progressive-enhancement fallback styles when the scale is typeface-specific.
  **Correction**: "Because I've based my layout on a modular scale derived partly from a specific size of a specific typeface, my measurements are not meaningful unless that typeface is used... I specify baseline fonts and generic measurements first, followed by preferred fonts and ideal, scale-based measurements."

# Common Confusions

- **Confusion**: Values near a scale sequence must belong to it.
  **Clarification**: Brown's examples include visually selected, combined, rounded, and non-scale values. Establish provenance for each value rather than inferring membership from numerical proximity.

# Source Reference

"Applying a modular scale in web design" — More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

Current bounded review (Slice14): The “Verified”, confidence-rationale and OCR entries below are retained extraction-era observations, not current whole-card or original-source verification. Current support is limited to inspected prepared passages and separately checked arithmetic; browser/fallback behavior, empirical benefit and original capture fidelity remain unassessed or unresolved.

- Definition source: Direct quotes and paraphrase from the "Applying a modular scale in web design" section; CSS code blocks extracted directly from the source.
- Confidence rationale: High — the section is a detailed worked example with actual CSS values and explicit justification for each decision.
- Uncertainties: Line-height values (1.54, 1.394) — it is not entirely clear from the text whether these are drawn from the scale or from visual testing independent of the scale. Brown says he "tried many different numbers for measure and line-height before settling on" these values, which suggests visual testing rather than strict scale derivation.
- Cross-reference status: Verified.
- Rosetta Stone check: No mappings — application is a straightforward CSS/design practice without meaningful cross-domain analogues.
- OCR issues: CSS code blocks have some HTML formatting artifacts; the actual CSS values are cleanly readable.
