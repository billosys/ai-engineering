---
# === CORE IDENTIFICATION ===
concept: The eval() Function
slug: eval-function

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: expressions
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 105
section: "4.12 Evaluation Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "direct eval"
  - "global eval"
  - "indirect eval"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - use-strict
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

`eval()` interprets a string of JavaScript source code, evaluating it and returning the value of the last expression. It is a powerful but rarely needed feature with significant security and optimization implications.

# Core Definition

"JavaScript has the ability to interpret strings of JavaScript source code, evaluating them to produce a value. JavaScript does this with the global function eval()." A "direct eval" (called by the exact name `eval`) uses the variable environment of the calling context. An "indirect eval" (called by any other name) evaluates in the global scope. (Ch. 4, §4.12)

# Prerequisites

- **primary-expressions** — `eval()` evaluates string expressions.
- **use-strict** — Strict mode restricts `eval()` behavior.

# Key Properties

1. Direct eval (called as `eval(...)`) uses the calling function's variable environment.
2. Indirect eval (called by another name, e.g., `let geval = eval; geval(...)`) uses the global environment.
3. In strict mode, `eval()` gets a private variable environment — it cannot define new variables in the caller's scope.
4. `eval()` is a security risk — never pass user input to it.
5. Functions that call `eval()` cannot be optimized effectively by the interpreter.
6. If the argument is not a string, `eval()` returns it unchanged.

# Construction / Recognition

```js
eval("3+2")           // => 5 (direct eval)
let geval = eval;
geval("x = 1")        // Global eval — sets global variable
```

# Context & Application

`eval()` is almost never necessary in practice. It is a security hole and performance hazard. Its inclusion in Chapter 4 reflects its historical importance and its operator-like semantics.

# Examples

From the source text (§4.12, pp. 105-108):

```js
eval("3+2")   // => 5

const geval = eval;
let x = "global", y = "global";
function f() {
    let x = "local";
    eval("x += 'changed';");   // Direct eval: modifies local x
    return x;                   // => "localchanged"
}
function g() {
    let y = "local";
    geval("y += 'changed';");  // Indirect eval: modifies global y
    return y;                   // => "local" (unchanged)
}
console.log(f(), x);  // "localchanged global"
console.log(g(), y);  // "local globalchanged"
```

# Relationships

## Builds Upon
- **primary-expressions** — `eval()` evaluates expressions within strings

## Enables
- Dynamic code execution (rarely needed)

## Related
- **use-strict** — Strict mode restricts `eval()` behavior

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Passing user-supplied input to `eval()`.
  **Correction**: Never use `eval()` with untrusted input — it is a security hole.

# Common Confusions

- **Confusion**: Believing `eval()` always uses the local scope.
  **Clarification**: Only a "direct eval" (using the exact name `eval`) uses the local scope. Any indirect call uses the global scope.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.12, pages 105-108.

# Verification Notes

- Definition source: Synthesized from §4.12, §4.12.1, §4.12.2, §4.12.3
- Confidence rationale: High — extensive coverage with clear examples
- Uncertainties: None
- Cross-reference status: Verified against §5.6.3 (strict mode)
