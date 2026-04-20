---
concept: Labeled Statement
slug: labeled-statement
category: control-flow
subcategory: loop-control
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.1.2 `break` plus label"
extraction_confidence: high
aliases:
  - "label"
  - "statement label"
prerequisites:
  - break-statement
extends: []
related:
  - break-statement
  - continue-statement
contrasts_with: []
answers_questions:
  - "How do I exit a nested loop or block from an inner statement?"
---

# Quick Definition

A label is an identifier placed in front of any statement (including blocks), allowing `break` with that label to exit the labeled statement from within.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, labels can be put in front of any statement, including blocks. The syntax `break myLabel` leaves the statement whose label is `myLabel`. This enables patterns like exiting an outer loop from a nested loop, or skipping failure-handling code in a block.

# Prerequisites

- Break statement

# Key Properties

1. Labels follow the rules of JavaScript identifiers.
2. `break` with a label can exit any labeled statement (not just loops).
3. Labels are primarily useful for `break` to escape nested structures.

# Construction / Recognition

```js
myLabel: {
  if (condition) break myLabel;
  // ... code skipped by break
}
```

# Context & Application

Used when `break` needs to exit more than the immediately enclosing loop or when using blocks as scope containers that can be exited early.

# Examples

From the source text (Ch. 25, section 25.1.2.1):

```js
searchBlock: {
  for (const str of stringArray) {
    if (str.endsWith(suffix)) {
      result = str;
      break searchBlock;
    }
  }
  result = '(Untitled)';
}
```

# Relationships

## Enables
- **Break Statement** -- labeled break can exit outer constructs

## Related
- **Continue Statement** -- `continue` can also use labels to target outer loops

# Common Errors

- **Error**: Trying to use labeled `break` to jump forward to a different location (goto-style).
  **Correction**: Labeled `break` only exits the labeled statement; it does not jump to arbitrary locations.

# Common Confusions

- **Confusion**: Thinking labels can only be placed on loops.
  **Clarification**: Labels can be placed on any statement, including blocks.

# Source Reference

Chapter 25: Control flow statements, Section 25.1.2, lines 109-161.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit examples in source text
- Cross-reference status: verified
