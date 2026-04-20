---
# === CORE IDENTIFICATION ===
concept: Compound and Empty Statements
slug: compound-and-empty-statements

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 116
section: "5.2 Compound and Empty Statements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "statement block"
  - "block statement"
  - "empty statement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-statements
extends: []
related:
  - if-else-statement
  - while-loop
  - for-loop
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

A compound statement (statement block) groups multiple statements within curly braces into a single statement. The empty statement (`;`) allows zero statements where one is expected.

# Core Definition

"A *statement block* combines multiple statements into a single *compound statement*. A statement block is simply a sequence of statements enclosed within curly braces." The *empty statement* "allows you to include no statements where one is expected. The empty statement looks like this: `;`" (Ch. 5, §5.2)

# Prerequisites

- **expression-statements** — Compound statements group expression statements and other statements.

# Key Properties

1. A statement block does not end with a semicolon — the individual statements inside do.
2. The empty statement is just a bare semicolon: `;`.
3. Compound statements are used where JavaScript syntax expects a single statement (e.g., loop bodies, if bodies).
4. Accidental semicolons after `if`, `for`, or `while` parentheses create empty statement bugs.

# Construction / Recognition

```js
{
    x = Math.PI;
    cx = Math.cos(x);
    console.log("cos(pi) = " + cx);
}

;   // Empty statement
```

# Context & Application

Statement blocks are essential for writing multi-line loop bodies, function bodies, and conditional bodies. The empty statement is occasionally used in loops where all work is done in the loop expression.

# Examples

From the source text (§5.2, p. 116):

```js
// Empty statement in a for loop
for(let i = 0; i < a.length; a[i++] = 0) /* empty */ ;

// Accidental empty statement bug:
if ((a === 0) || (b === 0));   // Oops! This line does nothing...
    o = null;                   // and this line is always executed.
```

# Relationships

## Builds Upon
- **expression-statements** — Block statements contain expression statements

## Enables
- **if-else-statement** — Uses blocks for multi-statement bodies
- **while-loop** — Uses blocks for loop bodies
- **for-loop** — Uses blocks for loop bodies

## Related
- All control flow statements that accept a single substatement

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Placing a semicolon after `if (condition);` creating an unintended empty statement.
  **Correction**: Remove the stray semicolon. When using the empty statement intentionally, add a comment: `/* empty */`.

# Common Confusions

- **Confusion**: Believing a statement block needs a trailing semicolon.
  **Clarification**: The block itself does not end with a semicolon; only the primitive statements inside it do.

# Source Reference

Chapter 5: Statements, Section 5.2, page 116.

# Verification Notes

- Definition source: Direct quote from §5.2
- Confidence rationale: High — clearly explained with cautionary examples
- Uncertainties: None
- Cross-reference status: Verified
