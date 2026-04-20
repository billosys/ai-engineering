---
concept: Scale Application to Typographic Hierarchy
slug: scale-application-typographic-hierarchy
category: typography
subcategory: type-hierarchy
tier: intermediate
layer: 2-domain
source: "More Meaningful Typography"
source_slug: posts
authors: "Tim Brown"
chapter: "Applying a modular scale in web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - [applying a modular scale, type hierarchy from scale, scale-based sizing]
prerequisites:
  - modular-scale
  - modular-scale-construction
  - scale-ratio
extends:
  - modular-scale
related:
  - typographic-rhythm-modular-scale
  - scale-base-unit
contrasts_with:
  - []
answers_questions:
  - "What distinguishes a modular scale from arbitrary type size selection?"
  - "What makes a type hierarchy feel harmonious vs arbitrary?"
  - "How do you construct a modular scale for a typographic system?"
rosetta_stone: []
css_implementation:
  - property: "font-size"
    example: "body { font-size: 18px; } /* scale origin */ h1 { font-size: 29.124px; } /* one step up */ h2 { font-size: 190px; } /* scale origin, second strand */ .side p { font-size: 15px; } /* improvised */"
    support: baseline
  - property: "width"
    example: ".main { width: 497.406px; } /* scale-derived measure */ .group { width: 845.479px; } /* scale-derived container */"
    support: baseline
  - property: "margin"
    example: "h1 { margin: 44.856px 0 0 307.420px; } /* scale values */ .side { margin: 27.723px 29.124px 0 0; } /* scale values */"
    support: baseline
  - property: "line-height"
    example: "p { line-height: 1.54; } /* scale-informed */ .main, p.intro { line-height: 1.394; } /* combined from scale */"
    support: baseline
---

# Quick Definition

Scale application is the process of selecting values from a constructed modular scale and assigning them to CSS measurements \u2014 font sizes, widths, margins, and line heights \u2014 to produce a typographic hierarchy in which all measurements share a common proportional logic.

# Core Definition

Brown describes the application phase directly: "Having marked up my text, and with my scale at my side, I applied CSS rules to our example, grabbing an exact number from my scale for each decision. Throughout the process, I made educated guesses that built a harmonious composition, one measurement at a time."

The scope of application extends far beyond font sizes alone: "Using a modular scale on the web means choosing numbers from the scale for type sizes, line height, line length, margins, column widths, and more." The scale is applied holistically \u2014 every significant measurement in the composition is drawn from the same proportional sequence.

The application process is iterative and visual, not mechanical: "I alternate between CSS editor and browser, checking to see how each value looks... I keep an eye on the overall density of my paragraphs (typographic color) and the readability of the text as a whole."

Brown explicitly endorses improvisation: scale values are "educated suggestions." Designers may round them (22.162 \u2192 22), combine them (3.56 + 16 = 19.56), or use non-scale values when the result looks better ("15px Minion Pro Caption sure looks good next to 18px Minion Pro").

# Prerequisites

- **Modular scale** \u2014 You must have a constructed scale before you can apply it.
- **Modular scale construction** \u2014 The procedure that produces the scale to be applied.
- **Scale ratio** \u2014 Understanding the ratio determines what values are available.

# Key Properties

1. **Holistic scope**: Type sizes, line heights, column widths, and margins all come from the same scale \u2014 not from separate systems.
2. **Iterative visual testing**: Values are tried, viewed in the browser, and adjusted; visual judgment arbitrates between adjacent scale options.
3. **Permissive improvisation**: Non-scale values are acceptable when they look better, but should be documented.
4. **Comment math**: When combining scale values arithmetically, the calculation should be noted in CSS comments (e.g., `font-size: 21.178px; /* 27.723 - 6.545 */`).
5. **Progressive enhancement**: Base/fallback CSS with generic fonts and conventional measurements should precede scale-based measurements; scale values depend on the specific typeface and may render poorly with fallback fonts.

# Construction / Recognition

## To Construct/Create:
1. Mark up content semantically (h1, h2, h3, p, aside, etc.) before applying measurements.
2. Apply scale values from largest (display/hero) to smallest (caption, footnote), testing each in the browser.
3. For each element, try several adjacent scale values; keep the one that best serves typographic color, readability, and hierarchy.
4. Apply scale values to widths and margins as well as type sizes.
5. Where no single scale value works, try combining two scale values or rounding one.
6. Document any non-scale values or combined values in CSS comments.
7. Specify progressive-enhancement fallback CSS before scale-based CSS.

## To Identify/Recognise:
1. Check whether type sizes in the CSS correspond to values in a geometric sequence.
2. Check whether widths and margins also correspond to the same sequence.
3. Look for CSS comment math documenting combinations.
4. Look for the scale URL or parameters in a CSS header comment.

# Context & Application

- **Typical contexts**: Full-page editorial web design; any project where a modular scale has been constructed.
- **Common applications**: Setting font-size hierarchy (body, h3, h2, h1); deriving column widths from scale; ensuring margins and padding share the scale's proportional logic.
- **Historical/stylistic notes**: Brown's CSS example is fully documented with actual numeric values, making it one of the most detailed public worked examples of modular scale application in web typography.

# Examples

**Example 1 \u2014 Font sizes** (from source, "Applying a modular scale in web design"):
- `body { font-size: 18px; }` \u2014 scale origin
- `h1 { font-size: 29.124px; }` \u2014 one step up from 18px \u00d7 1.618
- `h2 { font-size: 190px; }` \u2014 second scale origin
- `.side p { font-size: 15px; }` \u2014 improvised (not in scale)
- `p.intro { font-size: 21.178px; /* 27.723 - 6.545 */ }` \u2014 combined from scale

**Example 2 \u2014 Column widths** (from source):
- `.main { width: 497.406px; }` \u2014 scale value chosen after testing "many different numbers"
- `.group { width: 845.479px; }` \u2014 scale value chosen to fit h2
- `.side { width: 274px; }` \u2014 derived from resizing image to 190px height (a scale origin)

**Example 3 \u2014 Margins** (from source):
- `h1 { margin: 44.856px 0 0 307.420px; }` \u2014 both values from scale
- `.side { margin: 27.723px 29.124px 0 0; }` \u2014 both values from scale
- `h2 { margin-left: 20px; /* Optical alignment */ }` \u2014 improvised, not from scale

**Example 4 \u2014 Improvisation** (from source):
"Modular scales are a tool, they're not magic. They're not going to work for every measurement, and that's okay. Math is no substitute for an experienced designer's eye, but it can provide both hints and constraints for decision making."

# Relationships

## Builds Upon
- **Modular scale** \u2014 Application is the use of the constructed scale.
- **Modular scale construction** \u2014 The constructed scale is the prerequisite for application.

## Enables
- **Typographic rhythm via modular scale** \u2014 Consistent spacing and sizing rhythm results from holistic scale application.

## Related
- **Typographic color** \u2014 Brown cites monitoring "typographic color" (density of the text block) as part of the visual testing in application.
- **Progressive enhancement** \u2014 Fallback CSS strategy is discussed as part of the application practice.

## Contrasts With
- **Arbitrary measurement** \u2014 "The arbitrary dimensional choices I used to make had nothing to do with my intended designs' underlying meaning. At best, I chose ballpark measurements in CSS, command-tabbed over to my browser, and eyeballed the results."

# Common Errors

- **Error**: Applying scale values only to font sizes, using arbitrary numbers for widths and margins.
  **Correction**: "Using a modular scale on the web means choosing numbers from the scale for type sizes, line height, line length, margins, column widths, and more."

- **Error**: Treating the scale as a mechanical rule that eliminates the need for visual judgment.
  **Correction**: "I alternate between CSS editor and browser, checking to see how each value looks." Brown's process involves constant visual testing, not just numerical assignment.

- **Error**: Forgetting to provide progressive-enhancement fallback styles when the scale is typeface-specific.
  **Correction**: "Because I've based my layout on a modular scale derived partly from a specific size of a specific typeface, my measurements are not meaningful unless that typeface is used... I specify baseline fonts and generic measurements first, followed by preferred fonts and ideal, scale-based measurements."

# Common Confusions

- **Confusion**: If you apply a scale value and it looks wrong, the scale is wrong.
  **Clarification**: A scale value that looks wrong for one element may look right for another. Try adjacent values, combine values, or improvise when needed. "Math is no substitute for an experienced designer's eye."

# Source Reference

"Applying a modular scale in web design" \u2014 More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Definition source: Direct quotes and paraphrase from the "Applying a modular scale in web design" section; CSS code blocks extracted directly from the source.
- Confidence rationale: High \u2014 the section is a detailed worked example with actual CSS values and explicit justification for each decision.
- Uncertainties: Line-height values (1.54, 1.394) \u2014 it is not entirely clear from the text whether these are drawn from the scale or from visual testing independent of the scale. Brown says he "tried many different numbers for measure and line-height before settling on" these values, which suggests visual testing rather than strict scale derivation.
- Cross-reference status: Verified.
- Rosetta Stone check: No mappings \u2014 application is a straightforward CSS/design practice without meaningful cross-domain analogues.
- OCR issues: CSS code blocks have some HTML formatting artifacts; the actual CSS values are cleanly readable.
