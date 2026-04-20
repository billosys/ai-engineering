---
concept: Base Unit (for Scale Construction)
slug: scale-base-unit
category: typography
subcategory: type-scale
tier: foundational
layer: 2-domain
source: "More Meaningful Typography"
source_slug: posts
authors: "Tim Brown"
chapter: "Modular scales and how they apply to web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - [starting number, scale origin, base value, important number]
prerequisites:
  - []
extends:
  - []
related:
  - modular-scale
  - scale-ratio
  - modular-scale-construction
contrasts_with:
  - []
answers_questions:
  - "How do you construct a modular scale for a typographic system?"
rosetta_stone: []
css_implementation:
  - property: "font-size"
    example: "body { font-size: 18px; /* Scale origin */ } h2 { font-size: 190px; /* Scale origin (second strand) */ }"
    support: baseline
---

# Quick Definition

The base unit is the meaningful starting number (or numbers) from which a modular scale is generated \u2014 anchoring the entire measurement system to a concrete typographic or design decision.

# Core Definition

Brown describes the base unit as the foundational input to scale construction alongside the ratio: "You start with a ratio (for example, 1:1.618) and a number (like 10), then multiply and divide to get many resonant numbers."

Critically, Brown argues the starting number should not be arbitrary. He recommends grounding it in a direct typographic decision: "By choosing a text face at the beginning of a project...we can use the size at which body text looks most crisp as the basis for a project's modular scale." In his own example: "once I found the size I liked, 18px, I had a number upon which to base my modular scale."

The source also introduces the concept of a second starting number \u2014 an "important number" \u2014 used to create a double-stranded scale. This second number can be: the optimal caption text size; a large media dimension (width of an embedded video or ad unit); or a headline size that "anchor[s] the composition." For Brown's example, 190px (his h2 size) served this function.

Brown's CSS documents both origins with comments: `font-size: 18px; /* Scale origin */` and `font-size: 190px; /* Scale origin */`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. **Meaningful**: The base unit should be derived from a real design decision (e.g., optimal body text size) rather than chosen arbitrarily or for computational convenience.
2. **Typographically grounded**: Using body text size as the base unit anchors the entire measurement system to a visual quality judgment designers make with confidence.
3. **Multiple bases possible**: A double-stranded scale uses two starting numbers, generating two interleaved geometric sequences that together provide more measurement options.
4. **Documented in CSS**: Best practice (per Brown) is to comment the scale origin(s) in the stylesheet, enabling future designers to recreate or extend the scale.

# Construction / Recognition

## To Construct/Create:
1. Set the body text face before making layout decisions.
2. Try different font-sizes to find the one at which that face looks best at your target rendering conditions.
3. Record that size (e.g., 18px) as the scale's primary base unit.
4. Optionally, identify a second "important number" \u2014 a size that has special significance in the composition (a large headline, a media width, a caption size).
5. Feed both numbers into the scale generator alongside the chosen ratio.

## To Identify/Recognise:
1. Look for CSS comments marking `/* Scale origin */` or similar notations.
2. Identify the body `font-size` value \u2014 this is typically the primary base unit.
3. Check whether large or small outlier sizes in the CSS (very large headlines, very small captions) correspond to secondary scale origins.

# Context & Application

- **Typical contexts**: Beginning of any project using a modular scale; body text size selection; double-stranded scale construction.
- **Common applications**: Using body text size as the primary base; using a significant headline or image dimension as a secondary base for double-stranded scales.
- **Historical/stylistic notes**: Brown's recommendation to "start with type" \u2014 to select the text face and its optimal size before layout \u2014 represents a content-out design philosophy (he cites Mark Boulton's "going from content out, rather than canvas in" as a kindred approach).

# Examples

**Example 1** (from source, "Modular scales and how they apply to web design"): "If 16px Adobe Caslon is readable and renders well, we'll multiply and divide from 16 to create our scale. Thus, an entire system of harmonious measurement can be grounded in a visual decision\u2014body text size\u2014that designers routinely make with confidence."

**Example 2** (from source, "Creating a modular scale for web design"): "Sizing type on the web is tricky because of the limited resolution involved. One pixel of font-size up or down can completely change how a typeface\u2014and thus a whole text\u2014looks. But once I found the size I liked, 18px, I had a number upon which to base my modular scale."

**Example 3** (from source, "Creating a modular scale for web design"): "I also decided to include a second, 'important' number, because I wanted the flexibility of a double-stranded modular scale... I played with the text a bit, and the resulting font-size, 190px, became my important number."

**Example 4** (from source, "Creating a modular scale for web design"): Other possible second numbers: "The size at which caption text looks best, for instance, or a large number like the width of a piece of media\u2014if the project at hand mandates ads or embedded videos, for instance\u2014ensures that something about those elements resonates with the layout as a whole."

# Relationships

## Builds Upon
- (None in this source \u2014 the base unit is a primitive input.)

## Enables
- **Modular scale** \u2014 The base unit, combined with the ratio, generates the full scale.
- **Modular scale construction (procedure)** \u2014 The base unit is the required first input to the construction procedure.
- **Double-stranded modular scale** \u2014 Requires two base units (or two ratios).

## Related
- **Scale ratio** \u2014 The complementary required input to scale generation; neither alone produces the scale.

## Contrasts With
- **Arbitrary starting numbers** \u2014 Choosing 10 or 16 out of convenience rather than because those sizes represent the optimal rendering of a chosen typeface.

# Common Errors

- **Error**: Choosing a base number (e.g., 10, 16) without first checking whether that size is actually the optimal rendering size for the chosen typeface.
  **Correction**: Test the typeface at various sizes in context before committing. "One pixel of font-size up or down can completely change how a typeface\u2014and thus a whole text\u2014looks" (Brown).

- **Error**: Selecting an "important number" arbitrarily rather than deriving it from a real compositional element.
  **Correction**: The important number should emerge from the design \u2014 a headline tested until it "anchor[s] the composition," or a media element resized until it "resonates."

# Common Confusions

- **Confusion**: The base unit and the scale ratio are the same concept.
  **Clarification**: They are two distinct inputs. The base unit anchors the scale to a specific size in CSS units. The ratio determines how widely spaced the scale steps are. Both are required; neither substitutes for the other.

# Source Reference

"Modular scales and how they apply to web design"; "Creating a modular scale for web design" \u2014 More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Definition source: Synthesised from procedural description; no standalone definition of "base unit" given. The concept is described through worked examples and justification.
- Confidence rationale: High \u2014 the article provides multiple explicit examples, rationale, and CSS documentation practice for the base unit concept.
- Uncertainties: None significant within the scope of this source.
- Cross-reference status: Verified.
- Rosetta Stone check: No mappings \u2014 the base unit is a straightforward typographic/computational concept without meaningful cross-domain analogues in this source.
- OCR issues: None significant.
