---
concept: Break Statement
slug: break-statement
category: control-flow
subcategory: loop-control
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.1.1 `break`"
extraction_confidence: high
aliases:
  - "break"
prerequisites:
  - while-loop
  - for-loop
extends: []
related:
  - continue-statement
  - labeled-statement
contrasts_with:
  - continue-statement
answers_questions:
  - "How do I exit a loop early in JavaScript?"
---

# Quick Definition

The `break` statement immediately exits the innermost enclosing loop or `switch` statement. With a label operand, it can exit any labeled statement.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, `break` has two forms: without an operand (exits the current `while`, `do-while`, `for`, `for-of`, `for-await-of`, `for-in`, or `switch`) and with a label operand (`break myLabel`) which exits the statement whose label is `myLabel`, including blocks.

# Prerequisites

- Loop statements

# Key Properties

1. Without operand: exits the nearest enclosing loop or switch.
2. With label: can exit any labeled statement, including blocks.
3. Works in all loop types and `switch`.

# Construction / Recognition

```js
for (const x of ['a', 'b', 'c']) {
  if (x === 'b') break;
}
```

# Context & Application

Used to terminate loops early when a condition is met, or to skip failure-handling code via labeled break.

# Examples

From the source text (Ch. 25, section 25.1.2.1):

```js
function findSuffix(stringArray, suffix) {
  let result;
  searchBlock: {
    for (const str of stringArray) {
      if (str.endsWith(suffix)) {
        result = str;
        break searchBlock;
      }
    }
    result = '(Untitled)';
  }
  return { suffix, result };
}
```

# Relationships

## Related
- **Continue Statement** -- skips to next iteration instead of exiting
- **Labeled Statement** -- enables `break` to target outer statements

## Contrasts With
- **Continue Statement** -- `continue` skips to next iteration; `break` exits the loop entirely

# Common Errors

- **Error**: Using `break` without a label when trying to exit an outer loop from a nested loop.
  **Correction**: Use `break` with a label on the outer loop.

# Common Confusions

- **Confusion**: Thinking `break` with a label can only be used with loops.
  **Clarification**: Labeled `break` can exit any labeled statement, including plain blocks.

# Source Reference

Chapter 25: Control flow statements, Section 25.1.1-25.1.2, lines 80-161.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
