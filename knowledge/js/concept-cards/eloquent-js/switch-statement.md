---
# === CORE IDENTIFICATION ===
concept: Switch Statement
slug: switch-statement

# === CLASSIFICATION ===
category: control-flow
subcategory: branching
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "Dispatching on a value with switch"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - switch/case

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conditional-execution
  - break-statement
extends: []
related:
  - conditional-execution
  - break-statement
contrasts_with:
  - conditional-execution

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
---

# Quick Definition

A `switch` statement dispatches execution to one of several `case` labels based on the value of an expression, continuing execution (including through subsequent labels) until a `break` is encountered.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 765-766 of 02-program-structure.md): "There is a construct called `switch` that is intended to express such a 'dispatch' in a more direct way." And (lines 789-793): "The program will start executing at the label that corresponds to the value that `switch` was given, or at `default` if no matching value is found. It will continue executing, even across other labels, until it reaches a `break` statement."

# Prerequisites

- **Conditional Execution** -- Switch is an alternative to if/else chains.
- **Break Statement** -- Break is essential for correct switch behavior.

# Key Properties

1. Matches a value against **`case` labels** (lines 789-791).
2. Starts executing at the **matching label** or `default` (lines 791-792).
3. **Falls through** to subsequent cases until `break` is reached (lines 793-794).
4. Fall-through can be intentional (sharing code between cases) or accidental (lines 794-798).
5. Inherited from C/Java -- the syntax is "somewhat awkward" (lines 767-768).
6. A chain of `if` statements "may look better" according to the source (line 769).

# Construction / Recognition

## To Construct/Create:
```js
switch (expression) {
  case value1:
    // code
    break;
  case value2:
    // code
    break;
  default:
    // code
    break;
}
```

## To Identify/Recognize:
1. The `switch` keyword followed by a parenthesized expression and a block of `case` labels.

# Context & Application

Switch statements are used for dispatching on a single value when there are multiple possible matches. The source notes that if/else chains are often clearer, but switch is standard JavaScript.

# Examples

**Example 1** (Ch 2, lines 772-786): Weather dispatch:
```js
switch (prompt("What is the weather like?")) {
  case "rainy":
    console.log("Remember to bring an umbrella.");
    break;
  case "sunny":
    console.log("Dress lightly.");
  case "cloudy":
    console.log("Go outside.");
    break;
  default:
    console.log("Unknown weather type!");
    break;
}
```
Note: `"sunny"` intentionally falls through to `"cloudy"`.

# Relationships

## Builds Upon
- **Conditional Execution** -- Switch is an alternative to if/else chains.
- **Break Statement** -- Required to prevent fall-through.

## Enables
- Value-based dispatch patterns.

## Related
- **Break Statement** -- Essential for switch behavior.

## Contrasts With
- **Conditional Execution** -- if/else chains are more flexible; switch is more concise for value matching.

# Common Errors

- **Error**: Forgetting `break` in a case, causing unintended fall-through.
  **Correction**: "It is easy to forget such a `break`, which will cause the program to execute code you do not want executed" (lines 796-798). Always include `break` unless fall-through is intentional.

# Common Confusions

- **Confusion**: Switch is always better than if/else chains.
  **Clarification**: The source says "a chain of `if` statements may look better" (line 769). Switch is best when dispatching on a single value with many cases.

# Source Reference

Chapter 2: Program Structure, Section "Dispatching on a value with switch", lines 751-798 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with explicit definition and examples
- Cross-reference status: verified within chapter
