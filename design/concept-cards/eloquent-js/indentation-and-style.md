---
# === CORE IDENTIFICATION ===
concept: Indentation and Style
slug: indentation-and-style

# === CLASSIFICATION ===
category: fundamentals
subcategory: program-structure
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "Indenting Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - code formatting
  - indentation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - block
  - statement
extends: []
related:
  - comment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
---

# Quick Definition

Indentation is the practice of adding spaces at the beginning of lines inside blocks to visually reflect the structure of the code, making it readable for humans even though the computer does not require it.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 587-601 of 02-program-structure.md): "The role of this indentation inside blocks is to make the structure of the code stand out to human readers. In code where new blocks are opened inside other blocks, it can become hard to see where one block ends and another begins. With proper indentation, the visual shape of a program corresponds to the shape of the blocks inside it."

# Prerequisites

- **Block** -- Indentation reflects block structure.
- **Statement** -- Indentation applies to statements inside blocks.

# Key Properties

1. Spaces before statements are **not required** by the computer (line 587).
2. Indentation makes code structure **visible to humans** (lines 593-594).
3. The source author prefers **two spaces** per block level, though some use four spaces or tabs (lines 598-599).
4. **Consistency** is the important thing -- each new block should add the same amount of space (lines 600-601).
5. JavaScript also uses **camelCase** naming convention (e.g., `fuzzyLittleTurtle`) as the standard style (lines 818-822).

# Construction / Recognition

## To Construct/Create:
1. Add consistent spacing (2 or 4 spaces, or tabs) for each nested block level.

## To Identify/Recognize:
1. Code where nested blocks are visually offset from their containing blocks.

# Context & Application

Proper indentation is essential for code readability and maintenance. While JavaScript does not enforce indentation, consistent style prevents errors and makes code easier to understand for both the original author and others.

# Examples

**Example 1** (Ch 2, lines 603-610): Proper indentation:
```js
if (false != true) {
  console.log("That makes sense.");
  if (1 < 2) {
    console.log("No surprise there.");
  }
}
```

**Example 2** (Ch 2, lines 808-813): Naming conventions:
```
fuzzylittleturtle
fuzzy_little_turtle
FuzzyLittleTurtle
fuzzyLittleTurtle
```
The last style (camelCase) is the JavaScript standard.

# Relationships

## Builds Upon
- **Block** -- Indentation reflects block nesting.

## Enables
- Code readability and maintainability.

## Related
- **Comment** -- Another tool for code readability.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Inconsistent indentation (mixing tabs and spaces, or varying indent width).
  **Correction**: Pick one style and use it consistently. "The important thing is that each new block adds the same amount of space" (lines 600-601).

# Common Confusions

- **Confusion**: Indentation affects how JavaScript executes code.
  **Clarification**: Indentation is purely for human readability. JavaScript ignores whitespace (except in strings). The computer "will accept the program just fine without them" (lines 587-588).

# Source Reference

Chapter 2: Program Structure, Sections "Indenting Code" and "Capitalization", lines 582-830 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (paraphrased from source)
- Confidence rationale: Dedicated section with clear explanation
- Cross-reference status: verified within chapter
