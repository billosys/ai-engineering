---
concept: Object Destructuring Assignment Pitfall
slug: object-destructuring-assignment-pitfall
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.4.3 Syntax pitfall: assigning via object destructuring"
extraction_confidence: high
aliases: []
prerequisites:
  - object-destructuring
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Object destructuring in an assignment statement cannot start with `{` because JavaScript parses it as a block statement; the workaround is to wrap the entire assignment in parentheses: `({prop} = obj)`.

# Core Definition

When object-destructuring in an assignment (not a declaration), we cannot start a statement with a curly brace because JavaScript thinks we are starting a block. The statement `{prop} = { prop: 'hello' }` throws a SyntaxError because `{prop}` is parsed as a block containing a label. The workaround is parentheses: `({prop} = { prop: 'hello' })`.

# Prerequisites

- **object-destructuring** -- the context for this pitfall

# Key Properties

1. Starting a statement with `{` is parsed as a block
2. Wrap in parentheses: `({prop} = obj)`
3. Only affects assignments, not declarations
4. `const {prop} = obj` works fine (declaration)

# Construction / Recognition

```js
let prop;
// {prop} = { prop: 'hello' }; // SyntaxError!
({prop} = { prop: 'hello' }); // OK
assert.equal(prop, 'hello');
```

# Context & Application

This pitfall arises when destructuring into existing variables (not declaring new ones), commonly in loops or conditional assignments.

# Examples

```js
let prop;
assert.throws(
  () => eval("{prop} = { prop: 'hello' };"),
  SyntaxError
);

({prop} = { prop: 'hello' });
assert.equal(prop, 'hello');
```

(Chapter 40, Section 40.4.3, lines 305-344)

# Relationships

## Builds Upon
- **object-destructuring** -- assignment form

## Enables
- Correct object destructuring assignment

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Writing `{x, y} = obj` as a statement.
  **Correction**: Write `({x, y} = obj)` with parentheses.

# Common Confusions

- **Confusion**: This pitfall also affects `const {x} = obj`.
  **Clarification**: Declarations work fine because `const` makes the intent unambiguous. Only bare assignments starting with `{` have this issue.

# Source Reference

Chapter 40: Destructuring, Section 40.4.3, lines 305-344.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated as a "syntax pitfall"
- Cross-reference status: verified
