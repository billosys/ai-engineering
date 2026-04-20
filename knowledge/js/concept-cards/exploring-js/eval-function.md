---
concept: eval() Function
slug: eval-function
category: functions
subcategory: dynamic-evaluation
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Evaluating code dynamically: `eval()`, `new Function()` (advanced)"
chapter_number: 28
pdf_page: null
section: "28.1 `eval()`"
extraction_confidence: high
aliases:
  - "eval"
  - "dynamic evaluation"
prerequisites:
  - ordinary-function
extends: []
related:
  - new-function-constructor
contrasts_with:
  - new-function-constructor
answers_questions:
  - "How can I evaluate JavaScript code from a string?"
---

# Quick Definition

`eval()` evaluates a string of JavaScript code and returns the result, with direct eval using the current scope and indirect eval using global scope.

# Core Definition

As described in "Exploring JavaScript" Ch. 28, `eval(str)` evaluates the JavaScript code in `str` and returns the result. Direct eval (called as `eval(...)`) evaluates in the current scope. Indirect eval (any other invocation form, such as `eval?.()`, `(0,eval)()`, or `globalThis.eval()`) evaluates in global scope. Indirect eval is safer because the code has access to fewer internals.

# Prerequisites

- Ordinary function

# Key Properties

1. Direct eval: evaluates in current scope (security risk).
2. Indirect eval: evaluates in global scope (safer).
3. Any invocation that doesn't look like `eval(...)` is indirect.
4. Security risk: enables arbitrary code execution.
5. May be disabled by Content Security Policy in browsers.

# Construction / Recognition

```js
// Direct eval (current scope)
eval('myVariable');

// Indirect eval (global scope)
eval?.('myVariable');
(0, eval)('myVariable');
```

# Context & Application

Should be avoided whenever possible. JavaScript is usually dynamic enough to avoid `eval()`. If dynamic evaluation is necessary, prefer `new Function()` or indirect `eval`.

# Examples

From the source text (Ch. 28, section 28.1):

```js
globalThis.myVariable = 'global';
function func() {
  const myVariable = 'local';
  assert.equal(eval('myVariable'), 'local');       // direct
  assert.equal(eval.call(undefined, 'myVariable'), 'global'); // indirect
}
```

# Relationships

## Related
- **new Function() Constructor** -- safer alternative for dynamic code

## Contrasts With
- **new Function() Constructor** -- `new Function()` always uses global scope and provides a clean interface

# Common Errors

- **Error**: Using `eval()` when bracket notation would suffice.
  **Correction**: Use `obj[propKey]` instead of `eval('obj.' + propKey)`.

# Common Confusions

- **Confusion**: Thinking all `eval` calls behave the same.
  **Clarification**: Direct eval (looks exactly like `eval(...)`) uses local scope; all other forms use global scope.

# Source Reference

Chapter 28: Evaluating code dynamically, Section 28.1, lines 21-68.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with direct/indirect distinction
- Cross-reference status: verified
