---
concept: Clone to Satisfy the Borrow Checker
slug: clone-to-satisfy-borrow-checker
category: anti-pattern
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "Anti-patterns"
chapter_number: 3
pdf_page: null
section: "Clone to satisfy the borrow checker"
extraction_confidence: high
aliases:
  - "unnecessary clone"
  - "clone anti-pattern"
  - "borrow checker clone workaround"
prerequisites:
  - ownership
  - borrowing
extends: []
related:
  - newtype-pattern
contrasts_with:
  - borrowed-types-for-arguments
answers_questions:
  - "Why is cloning to avoid borrow checker errors an anti-pattern?"
  - "When is it acceptable to use .clone() to work around the borrow checker?"
  - "What are the consequences of unnecessary cloning in Rust?"
---

# Quick Definition

Resolving borrow checker errors by calling `.clone()` on variables rather than restructuring code to satisfy Rust's ownership rules. This creates hidden data duplication where changes to one copy are silently not reflected in the other.

# Core Definition

The borrow checker prevents Rust users from developing otherwise unsafe code by ensuring that either only one mutable reference exists, or potentially many but all immutable references exist. When code does not satisfy these conditions, this anti-pattern arises when the developer resolves the compiler error by cloning the variable. Using `.clone()` causes a copy of the data to be made, and any changes between the two copies are not synchronized -- as if two completely separate variables exist. If a clone is used to make a borrow checker error disappear, that is a strong indication this anti-pattern may be in use.

# Prerequisites

- **Ownership** -- understanding Rust's ownership model is essential to recognizing when cloning is being used as a workaround versus a genuine design choice
- **Borrowing** -- the borrow checker rules (one mutable XOR many immutable references) are the constraints that this anti-pattern attempts to circumvent

# Key Properties

1. The `.clone()` call creates a full, independent copy of the data
2. Changes to the clone are not reflected in the original, and vice versa -- they are completely separate variables
3. The clone silences the compiler error without addressing the underlying ownership issue
4. `Rc<T>` and `Arc<T>` are special cases where `.clone()` is cheap -- it only increments a reference count and both handles point to the same data
5. `cargo clippy` can detect some cases of unnecessary `.clone()` calls
6. The pattern is sometimes acceptable: for beginners still learning ownership, in prototypes without performance constraints, or when satisfying the borrow checker would significantly harm readability

# Construction / Recognition

## To Recognize This Anti-Pattern:
1. Look for `.clone()` calls that appear immediately before or near a borrow
2. Check if the clone was introduced to resolve a compiler error about conflicting borrows
3. Determine whether both the original and the clone are used afterward -- if only one is used, the clone may be unnecessary
4. Ask whether the code would be correct if the two values diverged -- if not, the clone masks a real design problem

## To Fix This Anti-Pattern:
1. Understand the ownership conflict the compiler is reporting
2. Restructure code to limit the scope of borrows (e.g., introduce blocks to drop borrows earlier)
3. Use references instead of owned values where possible
4. Consider `Rc<T>` or `Arc<T>` if genuine shared ownership is needed
5. Use `mem::take()` or `mem::replace()` to move values out of structures while leaving a valid default behind

# Context & Application

This anti-pattern is especially common among Rust beginners who encounter borrow checker errors and reach for `.clone()` as a quick fix. The source emphasizes that clones should be deliberate, with full understanding of the consequences. The Rust Book's chapter on Ownership should be understood fully before assessing whether a clone is required. Even experienced developers sometimes use `.clone()` intentionally for readability when performance is not critical, but this should be a conscious tradeoff rather than a workaround for a misunderstood ownership issue.

# Examples

**Example 1** (Ch. 3, "Clone to satisfy the borrow checker"):

```rust
// define any variable
let mut x = 5;

// Borrow `x` -- but clone it first
let y = &mut (x.clone());

// without the x.clone() two lines prior, this line would fail on compile as
// x has been borrowed
// thanks to x.clone(), x was never borrowed, and this line will run.
println!("{x}");

// perform some action on the borrow to prevent rust from optimizing this
// out of existence
*y += 1;
```

Here, `x.clone()` creates a separate copy. Mutations through `y` do not affect `x` at all, which may not be the intended behavior.

**Example 2** (Ch. 3, special case): `Rc<T>` and `Arc<T>` are designed to handle clones intelligently. Invoking `.clone()` on `Rc` produces a new `Rc` instance that points to the same data while increasing a reference count. In these cases, `.clone()` is the correct idiom, not an anti-pattern.

# Relationships

## Builds Upon
- Rust's ownership and borrowing rules

## Enables
- Recognizing when to use `Rc<T>` / `Arc<T>` for genuine shared ownership
- Understanding `mem::take` and `mem::replace` as alternatives

## Related
- **newtype-pattern** -- newtype wrappers can help restructure ownership boundaries

## Contrasts With
- **borrowed-types-for-arguments** -- accepting borrowed types in function arguments avoids the need for callers to clone

# Common Errors

- **Error**: Cloning a large data structure (e.g., a `Vec<String>`) inside a hot loop to avoid a borrow conflict.
  **Correction**: Restructure the code to limit borrow scopes, split the data structure, or use indices rather than references.

- **Error**: Cloning an `Rc<T>` and thinking it duplicates the underlying data.
  **Correction**: `Rc::clone()` only increments the reference count. This is a feature, not a problem -- it is the correct usage of `Rc`.

# Common Confusions

- **Confusion**: Thinking all uses of `.clone()` are anti-patterns.
  **Clarification**: Clone is perfectly valid when you genuinely need an independent copy. It is an anti-pattern only when used as a workaround for a borrow checker error without understanding the ownership issue.

- **Confusion**: Believing that `.clone()` is always expensive.
  **Clarification**: For `Copy` types (integers, booleans), cloning is trivially cheap. For `Rc<T>` and `Arc<T>`, it is a reference count increment. Cost depends on the type.

# Source Reference

Chapter 3: Anti-patterns, "Clone to satisfy the borrow checker" section. The anti-pattern is described with a code example, motivation, and links to the Rust Book's ownership chapter and `Rc<T>` / `Arc<T>` documentation.

# Verification Notes

- Definition source: Paraphrased from the Description and Motivation subsections
- Key Properties: All derived from explicit statements in the source
- Confidence rationale: HIGH -- the source provides a clear definition, concrete example, and detailed motivation
- Uncertainties: None for the definition
- Cross-reference status: `borrowed-types-for-arguments` and `newtype-pattern` reference cards from other extraction agents
