---
concept: If Let Temporary Scope 2024
slug: if-let-temporary-scope-2024
category: edition-2024
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: "if let temporary scope"
extraction_confidence: high
aliases:
  - "if let rescope"
  - "if let temporary lifetime 2024"
  - "if_let_rescope"
  - "temporary scope changes 2024"
  - "tail expression temporary scope 2024"
prerequisites:
  - rust-editions
related:
  - rust-2024-edition
contrasts_with: []
extends: []
answers_questions:
  - "How did if let temporary scope change in Rust 2024?"
  - "Why does my if let cause a deadlock in Rust 2021?"
  - "What is if_let_rescope?"
  - "How did tail expression temporary scope change in Rust 2024?"
  - "What is the tail_expr_drop_order lint?"
  - "When are temporaries dropped in if let expressions?"
---

# Quick Definition

The 2024 Edition changes two related temporary scope rules: (1) in `if let` expressions, temporaries from the scrutinee are dropped before entering the `else` branch (preventing deadlocks from held locks); (2) in tail expressions, temporaries may be dropped before local variables, and the scope is no longer extended outside the block. Both changes also enable `let` chains in `if` and `while` expressions.

# Core Definition

**`if let` temporary scope:** In Rust 2021, temporary values in the scrutinee of `if let $pat = $expr { .. } else { .. }` could be extended beyond the `if let` expression -- they were dropped *after* the `else` block. In Rust 2024, these temporaries are dropped at the point where the then-block completes or before the `else` block executes.

The classic motivating example involves `RwLock`:

```rust
fn f(value: &RwLock<Option<bool>>) {
    if let Some(x) = *value.read().unwrap() {
        println!("value is {x}");
    } else {
        // In 2021: DEADLOCK -- read lock still held here
        // In 2024: OK -- read lock dropped before else block
        let mut v = value.write().unwrap();
        if v.is_none() { *v = Some(true); }
    }
}
```

**Tail expression temporary scope (RFC 3606):** In Rust 2021, temporaries in tail expressions (the last expression in a block) were extended outside the block and dropped after local variables. In 2024, they may be dropped at the end of the block, before local variables. This fixes cases like `fn f() -> usize { let c = RefCell::new(".."); c.borrow().len() }` which errored in 2021 because `c` was dropped before `c.borrow()`.

However, this narrowing can break code that relied on temporaries living past the block: `let x = { &String::from("1234") }.len();` compiles in 2021 but fails in 2024 because the `String` is dropped at the end of the block.

**`let` chains:** As a consequence of the `if let` rescoping, the 2024 Edition also enables `let` chains: `if let Some(a) = x && let Some(b) = y { ... }`.

# Prerequisites

- **Rust editions** -- understanding the edition migration mechanism

# Key Properties

1. `if let` temporaries are dropped before `else` block execution in 2024
2. Tail expression temporaries may be dropped before local variables in 2024
3. The `if let` change prevents deadlocks from held locks in `else` branches
4. The tail expression change fixes the `RefCell::borrow().len()` pattern that errored in 2021
5. The tail expression change may break code relying on temporaries living past blocks
6. `let` chains in `if` and `while` are enabled as a consequence of the `if let` rescoping
7. Converting `if let` to `match` preserves 2021 behavior (match scrutinee temporaries are extended past the match)
8. The `if_let_rescope` lint auto-fixes by converting `if let` to `match`
9. The `tail_expr_drop_order` lint warns but cannot auto-fix -- requires manual review

# Construction / Recognition

## Recognizing Affected `if let` Patterns:

Look for `if let` where the scrutinee creates a temporary with a non-trivial `Drop` (e.g., lock guards, `Ref`/`RefMut`) and the `else` block needs that temporary to be dropped.

## Preserving 2021 `if let` Behavior (if needed):

Convert to `match`, which extends scrutinee temporaries past the entire match:

```rust
match *value.read().unwrap() {
    Some(x) => { println!("value is {x}"); }
    _ => {
        // Read lock still held here (same as 2021 if-let behavior)
        let mut s = value.write().unwrap();  // DEADLOCK
    }
}
```

## Fixing Tail Expression Issues:

Lift the block expression to a local variable:

```rust
// Broken in 2024:
// let x = { &String::from("1234") }.len();

// Fixed:
let s = { &String::from("1234") };
let x = s.len();  // works via temporary lifetime extension
```

## Using `let` Chains (new in 2024):

```rust
fn sum_first_two(nums: &[u8]) -> Option<u8> {
    let mut iter = nums.iter();
    if let Some(first) = iter.next()
        && let Some(second) = iter.next()
    {
        first.checked_add(*second)
    } else {
        None
    }
}
```

# Context & Application

The `if let` temporary scope change is a pragmatic fix for a real-world pain point: holding lock guards through `else` branches often causes deadlocks that are subtle and surprising. The source notes that the read lock in the motivating example "will not be dropped until after the if let expression (that is, after the else block)," which is the opposite of what most programmers expect.

The tail expression change is more nuanced. It fixes an ergonomic issue (the `c.borrow().len()` pattern that should work but did not) at the cost of potentially breaking code that relied on temporaries living longer. The `tail_expr_drop_order` lint cannot auto-fix because there are "no semantics-preserving rewrites to shorten the lifetime for temporary values in tail expressions."

The `let` chains feature is a natural extension of `if let` that was blocked by the old temporary scope rules. It allows combining multiple fallible pattern matches in a single condition, reducing nesting.

# Examples

**Example 1** (`if let` deadlock fix): With `RwLock`, `if let Some(x) = *value.read().unwrap() { ... } else { value.write().unwrap(); }` deadlocks in 2021 but works in 2024 because the read guard is dropped before the `else` branch.

**Example 2** (tail expression fix): `fn f() -> usize { let c = RefCell::new(".."); c.borrow().len() }` fails to compile in 2021 (`c` does not live long enough) but works in 2024 because the borrow temporary is dropped first.

**Example 3** (tail expression breakage): `let x = { &String::from("1234") }.len();` compiles in 2021 but fails in 2024 because the String temporary is dropped at the block boundary.

# Relationships

## Related
- **rust-2024-edition** -- these are significant language changes in the 2024 edition

# Common Errors

- **Error**: Blindly accepting `cargo fix --edition` conversions of `if let` to `match` without reviewing whether the old extended-lifetime behavior was actually desired.
  **Correction**: Review each converted `if let`-to-`match` to determine if you want the temporary to live through the else branch (keep `match`) or be dropped before it (revert to `if let`).

- **Error**: Ignoring `tail_expr_drop_order` warnings because they cannot be auto-fixed.
  **Correction**: These warnings indicate potential behavior changes. Manually inspect each one -- the drop order of temporaries with custom `Drop` may have observable effects.

# Common Confusions

- **Confusion**: Thinking the `if let` change means temporaries are always dropped immediately after evaluation.
  **Clarification**: Temporaries are dropped when the then-block completes OR before the `else` block. They survive through the then-block if the pattern matches.

- **Confusion**: Thinking `let` chains require a special opt-in beyond the 2024 edition.
  **Clarification**: `let` chains are automatically available with `edition = "2024"` -- no feature flag needed. They were gated on the edition because they depend on the `if let` rescoping behavior.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024. Three related sections: "`if let` temporary scope," "Tail expression temporary scope" (RFC 3606), and "`let` chains in `if` and `while`." The `if let` section includes the RwLock deadlock example. The tail expression section includes the RefCell and String temporary examples.

# Verification Notes

- `if let` deadlock example: directly from the source text
- Tail expression examples (RefCell, String): directly from the source
- `let` chain syntax: from the "let chains in if and while" section
- The statement about no auto-fix for tail expressions: direct quote from source
- Confidence: HIGH -- all examples and rules directly from the edition guide
- Cross-references: slugs verified against this extraction set
