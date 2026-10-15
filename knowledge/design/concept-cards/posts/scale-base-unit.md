---
concept: "Base Unit (for Scale Construction)"
slug: "scale-base-unit"
category: "typography"
subcategory: "type-scale"
tier: "foundational"
layer: "2-domain"
source: "More Meaningful Typography"
source_slug: "posts"
authors: "Tim Brown"
chapter: "Modular scales and how they apply to web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "starting number"
    - "scale origin"
    - "base value"
    - "important number"
prerequisites: []
extends: []
related:
  - "modular-scale"
  - "scale-ratio"
  - "modular-scale-construction"
contrasts_with: []
answers_questions:
  - "How do you construct a modular scale for a typographic system?"
rosetta_stone: []
css_implementation:
  -
    property: "font-size"
    example: "body { font-size: 18px; /* Scale origin */ } h2 { font-size: 190px; /* Scale origin (second strand) */ }"
    support: "baseline"
---

# Quick Definition

A base unit is a positive starting value for one declared scale strand. Pair it with that strand's positive ratio and indexing convention; the base is an input, not a claim that one font size or measurement is universally optimal.

# Core Definition

Brown presents the starting number alongside the ratio: “You start with a ratio (for example, 1:1.618) and a number (like 10), then multiply and divide to get many resonant numbers.” In his project he first chose a text face and tested sizes, then used 18px Minion as one starting value. That is his typeface-first method and contextual example, not a requirement for every project or proof of a unique optimum.

Brown also uses a second “important” number, 190px for an h2 in his example, to make a double-stranded scale. He suggests that a caption size or a media dimension may be relevant when the project calls for it. These are possible contextual inputs; they are not mandatory choices. A convenient fixed value can also be valid when it suits the intended system and is declared clearly.

A scale strand is generated from its own positive starting value and ratio. A double-stranded construction can start from two numbers or two ratios, as Brown says in “Modular scales and how they apply to web design” (prepared article, line 156). The two geometric strands should be distinguished from a sorted merge of their values: adjacent values in the merged list need not be adjacent steps within either strand.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. **Positive declared input**: A strand starts from a positive value and uses a declared ratio and indexing convention. The value may be selected by contextual testing, convenience, or another stated constraint.
2. **Contextual choice, not a universal optimum**: Brown tests typeface sizes in his project and describes his approach; the article does not establish that body text must supply every scale's base or that a single size is objectively best.
3. **More than one strand**: A double-stranded scale may use two starting numbers or two ratios. Keep each strand's construction separate from any sorted merge of its outputs.
4. **Documentation**: CSS comments that explain intended origins can help future readers. A comment does not prove that the body font size is the computational base or that every value outside one sequence has another origin.

# Construction / Recognition

## To Construct/Create:
1. Declare a positive starting value, ratio, and indexing convention for each strand.
2. Choose the inputs that suit the project. Brown's typeface-first trial is one approach: he tested Minion and selected 18px. A fixed or convenient value is also usable when it meets the stated design or implementation constraints.
3. If a second strand is useful, declare its starting number or ratio as an additional input. Brown's 190px h2, caption size, and project-required media dimension are attributed possibilities, not a required recipe.
4. Generate each strand from its own inputs. Keep strand indices explicit; if values are sorted and merged, do not describe every neighbor in that merged list as a step in one strand.
5. Document the chosen inputs and their roles. CSS comments are documentation, not independent evidence of how values were computed.

## To Identify/Recognise:
1. Look for declared base values, ratios, and indexing rules in the scale specification or implementation.
2. Treat CSS comments such as `/* Scale origin */` as evidence of stated intent only.
3. Check whether values follow a strand's declared rule before assigning an origin. Body `font-size` is not necessarily the computational base, and an outlier does not by itself establish a second strand.

# Context & Application

- **Typical contexts**: Declaring the starting value for a modular scale; deciding whether a second strand is useful.
- **Common applications**: Brown's 18px Minion example and his 190px h2 example; his article also mentions a caption size or a project-required media dimension as possible inputs.
- **Historical/stylistic notes**: Brown's “start with type” approach chooses a text face and tests its size before layout decisions. He relates that approach to going from content out rather than canvas in. This is an attributed design method, not a universal rule for choosing bases.

# Examples

**Example 1** (from source, “Modular scales and how they apply to web design”): “If 16px Adobe Caslon is readable and renders well, we'll multiply and divide from 16 to create our scale. Thus, an entire system of harmonious measurement can be grounded in a visual decision—body text size—that designers routinely make with confidence.” This is Brown's illustration, not evidence that 16px is appropriate for every typeface, context, or user.

**Example 2** (from source, “Creating a modular scale for web design”): Brown writes that web type is sensitive to one-pixel changes and that after testing he liked 18px for Minion. The prepared source records this project-specific choice; it does not independently establish a general optimum.

**Example 3** (from source, “Creating a modular scale for web design”): Brown says he included a second “important” number for a double-stranded scale; he selected 190px for his h2 after working with the text.

**Example 4** (from source, “Creating a modular scale for web design”): Brown suggests that a caption size or a media width may be a second number when the project calls for captions, ads, or embedded video. The choice remains contextual.

# Relationships

## Builds Upon
- (None in this source — a starting value is a primitive input.)

## Enables
- **Modular scale** — A declared starting value paired with a ratio contributes one scale strand.
- **Modular scale construction (procedure)** — The procedure needs the strand's starting value and ratio.
- **Double-stranded modular scale** — Brown's construction allows two starting numbers or two ratios. These inputs define two strands; the sorted merge is a separate representation.

## Related
- **Scale ratio** — The complementary input for generating a strand; neither input alone specifies it.

## Contrasts With
- **Undeclared starting values** — A sequence whose starting value or role is not stated is harder to reproduce. This is a documentation distinction, not a claim that convenient numerical choices are invalid.

# Common Errors

- **Error**: Treating Brown's typeface-first method as a requirement to find the objectively optimal body size before choosing any scale input.
  **Correction**: Attribute the method to Brown and state the project context. A fixed or convenient positive input can be valid; its suitability depends on the declared use and constraints.

- **Error**: Treating every large or small CSS value as a separate scale origin, or assuming the body font size is necessarily the base.
  **Correction**: Compare values with declared per-strand rules and indices. Comments document intent but do not establish the arithmetic.

# Common Confusions

- **Confusion**: The base value and the scale ratio are interchangeable.
  **Clarification**: They are separate declared inputs: the value sets a strand's starting magnitude, while the ratio sets its multiplicative progression. A double-stranded scale may use two numbers or two ratios; merged-list adjacency remains distinct from per-strand steps.

# Source Reference

"Modular scales and how they apply to web design"; "Creating a modular scale for web design" — More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Definition and examples: Brown's prepared article, “Modular scales and how they apply to web design” and “Creating a modular scale for web design,” especially lines 133–189; the article describes worked inputs rather than giving a standalone universal definition.
- Available-evidence review: The card's definitions and procedures have been qualified to distinguish Brown's contextual method from general requirements; arithmetic/construction is checked against the declared strand inputs; relation language is limited to the input dependency described here; the existing construction question is addressed only at this input level. Original capture identity/fidelity and broader endpoint/CQ review remain pending.
- Legacy evidence: “High,” “Verified,” and OCR observations are inherited extraction-era records, not new semantic or fidelity acceptance. The locator points to prepared text; no immutable original capture or lineage was reviewed. CDC review remains pending.
