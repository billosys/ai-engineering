---
# === CORE IDENTIFICATION ===
concept: Pass Variables to Closure
slug: pass-variables-to-closure

# === CLASSIFICATION ===
category: idiom
subcategory: closures
tier: intermediate

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Pass variables to closure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "closure variable rebinding"
  - "closure capture control"
  - "scoped closure variables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - closures
  - move-semantics
  - clone-trait
extends: []
related:
  - temporary-mutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I move some variables into a closure while cloning or borrowing others?"
  - "How do I avoid polluting the outer scope with temporary clones needed by a closure?"
  - "What is the variable rebinding pattern for closures in Rust?"
---

# Quick Definition

Use a separate block scope `{ ... }` to rebind variables before creating a `move` closure. Inside the block, clone, borrow, or transform variables as needed using the same names, then create the `move` closure. This groups capture preparation with the closure definition and avoids polluting the outer scope with temporary bindings.

# Core Definition

> "By default, closures capture their environment by borrowing. Or you can use a `move`-closure to move the whole environment. However, often you want to move just some variables to the closure, give it a copy of some data, pass by reference, or perform some other transformation." -- Rust Design Patterns, "Pass variables to closure"

> "Use variable rebinding in a separate scope for that." -- Rust Design Patterns, "Pass variables to closure"

The pattern wraps the closure creation in a block expression where variables are rebound (cloned, borrowed, etc.) before the `move` closure captures them. This keeps the rebindings co-located with the closure and allows the closure to use the same variable names as surrounding code.

# Prerequisites

- Understanding of closures and the `move` keyword
- Knowledge of `Clone` trait and `.clone()`
- Understanding of Rust's scoping and shadowing rules

# Key Properties

1. **Block scope groups preparation**: Clones and borrows are declared in the same block as the closure.
2. **Same variable names**: Rebinding with the same name (shadowing) means the closure body reads naturally.
3. **Immediate drop**: Cloned data not consumed by the closure is dropped when the block ends.
4. **Selective capture**: Move some variables, clone others, borrow yet others -- all in one pattern.
5. **Avoids outer-scope pollution**: No `_cloned` or `_borrowed` variable names leak into the surrounding scope.

# Construction / Recognition

## To Apply:
1. Identify which variables need different capture modes (move, clone, borrow)
2. Open a block expression: `let closure = { ... };`
3. Inside the block, rebind variables: `let x = x.clone();`, `let y = y.as_ref();`
4. Create a `move || { ... }` closure as the last expression in the block
5. The closure captures the rebound variables

## To Recognize:
- A block expression `{ let x = x.clone(); move || { ... } }` assigned to a variable
- Variable shadowing immediately before a `move` closure
- Cloned or borrowed variables with the same names as outer-scope originals

# Context & Application

When using `move` closures, all captured variables are moved. But often you want mixed capture modes: move one variable, clone another, borrow a third. Without this pattern, you would create auxiliary variables like `num2_cloned` in the outer scope, cluttering it. The block-scoped rebinding pattern keeps the preparation co-located with the closure and drops unused clones immediately.

# Examples

**Good -- rebinding in a block scope:**

```rust
use std::rc::Rc;

let num1 = Rc::new(1);
let num2 = Rc::new(2);
let num3 = Rc::new(3);
let closure = {
    // `num1` is moved
    let num2 = num2.clone();  // `num2` is cloned
    let num3 = num3.as_ref();  // `num3` is borrowed
    move || {
        *num1 + *num2 + *num3;
    }
};
```

**Bad -- auxiliary variables in outer scope:**

```rust
use std::rc::Rc;

let num1 = Rc::new(1);
let num2 = Rc::new(2);
let num3 = Rc::new(3);

let num2_cloned = num2.clone();
let num3_borrowed = num3.as_ref();
let closure = move || {
    *num1 + *num2_cloned + *num3_borrowed;
};
```

# Relationships

## Related
- **temporary-mutability** -- Similar use of scoping to control variable properties

# Common Errors

- **Error**: Forgetting to use `move` after rebinding, causing the closure to borrow the block-local variables (which are about to be dropped)
  **Correction**: Always use `move` on the closure inside the rebinding block

- **Error**: Rebinding in the outer scope instead of a block, polluting the namespace
  **Correction**: Wrap the rebindings and closure creation in a block expression

# Common Confusions

- **Confusion**: Thinking this is the same as just using `move ||`
  **Clarification**: `move` captures everything by move; this pattern lets you selectively clone or borrow before moving

- **Confusion**: Worrying that the block scope will drop values the closure needs
  **Clarification**: The `move` closure takes ownership of the rebound values; they are not dropped with the block

# Source Reference

Chapter 1: Idioms, Section "Pass variables to closure".

# Verification Notes

- Definition source: Directly from "Pass variables to closure" section
- Confidence rationale: HIGH -- clear good/bad examples with explanation
- Uncertainties: None
- Cross-reference status: Standalone idiom
