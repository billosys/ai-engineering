---
# === CORE IDENTIFICATION ===
concept: Automatic Semicolon Insertion
slug: automatic-semicolon-insertion

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: lexical-structure
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Lexical Structure"
chapter_number: 2
pdf_page: 36
section: "2.6 Optional Semicolons"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ASI
  - optional semicolons

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - statements-overview
extends: []
related:
  - arrow-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Automatic Semicolon Insertion (ASI) is JavaScript's mechanism for treating line breaks as statement-terminating semicolons in certain contexts, allowing semicolons to be omitted between statements on separate lines.

# Core Definition

"JavaScript uses the semicolon (;) to separate statements from one another." However, "you can usually omit the semicolon between two statements if those statements are written on separate lines." JavaScript "does not treat every line break as a semicolon: it usually treats line breaks as semicolons only if it can't parse the code without adding an implicit semicolon." More formally: "JavaScript treats a line break as a semicolon if the next nonspace character cannot be interpreted as a continuation of the current statement." (pp. 36-37)

# Prerequisites

- **javascript-language-overview** — ASI is a fundamental parsing rule
- **statements-overview** — ASI applies to statement separation

# Key Properties

1. Semicolons can be omitted between statements on separate lines
2. JavaScript only inserts semicolons when it cannot parse without them
3. Three exceptions to the general rule:
   - After `return`, `throw`, `yield`, `break`, `continue` — line break always treated as semicolon
   - Before `++` and `--` when used as postfix operators — must be on same line
   - Arrow (`=>`) must appear on same line as parameter list
4. Statements beginning with `(`, `[`, `/`, `+`, or `-` may be parsed as continuation of previous statement
5. Defensive semicolons can be placed at the start of lines beginning with `(` or `[`

# Construction / Recognition

```javascript
// These two lines are parsed as separate statements:
a = 3;
b = 4;

// Without explicit semicolons, also works:
a = 3
b = 4

// But this is ambiguous — parsed as one statement:
let y = x + f
(a+b).toString()
// Parsed as: let y = x + f(a+b).toString();
```

# Context & Application

ASI is one of JavaScript's most subtle features. While it allows omitting semicolons in many cases, it can lead to surprising bugs. Developers typically adopt one of two styles: always write semicolons explicitly, or omit them whenever possible with defensive semicolons where needed.

# Examples

From the source text (pp. 37-38):

Dangerous case — line break after `return`:
```javascript
return
true;
// JavaScript assumes you meant: return; true;
// But you probably meant: return true;
```

Defensive semicolon (p. 37):
```javascript
let x = 0                         // Semicolon omitted here
;[x,x+1,x+2].forEach(console.log) // Defensive ; keeps this statement separate
```

Ambiguous parsing (p. 37):
```javascript
let y = x + f
(a+b).toString()
// Parsed as: let y = x + f(a+b).toString();
```

# Relationships

## Builds Upon
- **statements-overview** — ASI affects how statements are separated

## Enables
- Understanding of semicolon-free coding styles

## Related
- **arrow-functions** — The `=>` must be on the same line as parameters (ASI exception)

## Contrasts With
- None within this source

# Common Errors

- **Error**: Putting a line break after `return` before the return value.
  **Correction**: The return value must be on the same line as `return`, or at least start on that line. `return\ntrue;` is parsed as `return; true;`.

- **Error**: Starting a line with `(` or `[` after omitting a semicolon.
  **Correction**: Use a defensive semicolon: `;[x,x+1].forEach(...)` or always end statements with explicit semicolons.

# Common Confusions

- **Confusion**: JavaScript inserts semicolons at every line break.
  **Clarification**: JavaScript only inserts semicolons when it cannot parse the code without one — many line breaks are not treated as semicolons.

# Source Reference

Chapter 2: Lexical Structure, Section 2.6, pages 36-38.

# Verification Notes

- Definition source: Direct quotes from pp. 36-37
- Confidence rationale: High — thoroughly explained with examples and exceptions
- Uncertainties: None
- Cross-reference status: Verified
