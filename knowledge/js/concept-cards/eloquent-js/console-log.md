---
# === CORE IDENTIFICATION ===
concept: Console.log
slug: console-log

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
section: "The console.log function"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - side-effect
  - environment
extends: []
related:
  - expression
  - binding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

`console.log` is a function that writes its arguments to a text output device (the browser console or terminal), providing the primary way to inspect values during development.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 288-292 of 02-program-structure.md): "Most JavaScript systems (including all modern web browsers and Node.js) provide a `console.log` function that writes out its arguments to *some* text output device. In browsers, the output lands in the JavaScript console."

# Prerequisites

- **Side Effect** -- `console.log` produces a side effect (output).
- **Environment** -- `console.log` is a binding available in the default environment.

# Key Properties

1. Writes arguments to a **text output device** (line 291).
2. Available in **all modern browsers** and **Node.js** (lines 289-290).
3. In browsers, output goes to the **JavaScript console** (line 292).
4. Not a simple binding -- it is an **expression** that retrieves the `log` property from the `console` binding (lines 300-302).
5. Used throughout the source to **demonstrate program output**.

# Construction / Recognition

## To Construct/Create:
1. `console.log("Hello");` -- pass any value(s) as arguments.
2. `console.log(value1, value2);` -- multiple arguments.

## To Identify/Recognize:
1. A call to `console.log(...)` in code.

# Context & Application

`console.log` is the most commonly used debugging and output tool in JavaScript. It is used throughout the source to show what programs produce. Understanding it is essential for testing and verifying code behavior.

# Examples

**Example 1** (Ch 2, lines 128-132 of 02-program-structure.md):
```js
let ten = 10;
console.log(ten * ten);
// → 100
```

**Example 2** (Ch 2, lines 299-302): Why the name has a dot:
"Though binding names cannot contain period characters, `console.log` does have one. This is because `console.log` isn't a simple binding, but an expression that retrieves the `log` property from the value held by the `console` binding."

# Relationships

## Builds Upon
- **Side Effect** -- `console.log` produces output as a side effect.
- **Environment** -- Available as a standard binding.

## Enables
- Debugging and inspecting program state.
- Demonstrating program output.

## Related
- **Expression** -- `console.log(...)` is an expression (a function call).
- **Binding** -- `console` is a binding; `log` is a property.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Expecting `console.log` to return the value it prints.
  **Correction**: `console.log` returns `undefined`. Its purpose is the side effect of displaying output, not producing a return value.

# Common Confusions

- **Confusion**: `console.log` is a single binding name.
  **Clarification**: `console` is a binding holding an object, and `log` is a property of that object. The dot accesses the property.

# Source Reference

Chapter 2: Program Structure, Section "The console.log function", lines 285-304 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with clear explanation
- Cross-reference status: verified within chapter
