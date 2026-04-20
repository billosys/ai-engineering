---
concept: Switch Variable Scope Pitfall
slug: switch-variable-scope
category: control-flow
subcategory: conditionals
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.4.5 Pitfall of `switch`: all cases exist in the same variable scope"
extraction_confidence: high
aliases: []
prerequisites:
  - switch-statement
extends: []
related: []
contrasts_with: []
answers_questions:
  - "Why do I get a variable redeclaration error in a switch statement?"
---

# Quick Definition

All `case` clauses in a `switch` statement share a single variable scope, so declaring the same variable name in multiple cases causes a `SyntaxError` unless each case is wrapped in braces `{}`.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, the complete body of `switch` is a single variable scope. Declaring the same `const` or `let` variable in multiple cases results in `SyntaxError: Identifier has already been declared`. The fix is to wrap each case's code in curly braces to create a separate block scope.

# Prerequisites

- Switch statement

# Key Properties

1. All cases share one scope.
2. `const`/`let` redeclaration causes SyntaxError.
3. Fix: wrap case bodies in `{}`.

# Construction / Recognition

```js
// Problem:
switch (x) {
  case 'a': const text = 'hello'; break;
  case 'b': const text = 'world'; break; // SyntaxError!
}

// Fix:
switch (x) {
  case 'a': { const text = 'hello'; break; }
  case 'b': { const text = 'world'; break; }
}
```

# Context & Application

Common pitfall when using `const`/`let` in switch statements.

# Examples

From the source text (Ch. 25, section 25.4.5):

```js
switch (command) {
  case 'once': {
    const text = args[1];
    return text;
  }
  case 'repeat': {
    const text = args[2]; // OK: separate scope
    return text.repeat(times);
  }
}
```

# Relationships

## Builds Upon
- **Switch Statement** -- scope is a property of switch

# Source Reference

Chapter 25: Control flow statements, Section 25.4.5, lines 446-533.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit pitfall with solution
- Cross-reference status: verified
