---
concept: "mem::take and mem::replace"
slug: mem-take-replace
category: idiom
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "mem::{take(_), replace(_)} to keep owned values in changed enums"
extraction_confidence: high
aliases:
  - "mem::take"
  - "mem::replace"
  - "take and replace pattern"
  - "Indiana Jones swap"
  - "owned values in changed enums"
prerequisites:
  - default-trait
extends: []
related:
  - finalisation-in-destructors
  - constructor-idiom
contrasts_with: []
answers_questions:
  - "How do I change an enum variant in place without cloning?"
  - "What does mem::take do in Rust?"
  - "What does mem::replace do in Rust?"
  - "How do I move a value out of a mutable reference?"
  - "How do I avoid cloning to satisfy the borrow checker?"
---

# Quick Definition

`mem::take` and `mem::replace` allow you to move an owned value out of a mutable reference by swapping it with a replacement (the default value for `take`, or a specified value for `replace`). This is essential for changing enum variants in place without cloning, because the borrow checker requires that a valid value always exists behind a reference.

# Core Definition

"Say we have a `&mut MyEnum` which has (at least) two variants, `A { name: String, x: u8 }` and `B { name: String }`. Now we want to change `MyEnum::A` to a `B` if `x` is zero, while keeping `MyEnum::B` intact. We can do this without cloning the `name`." (Ch. 1, "mem::{take(_), replace(_)}")

"`mem::take` lets us swap out the value, replacing it with its default value, and returning the previous value. For `String`, the default value is an empty `String`, which does not need to allocate. As a result, we get the original `name` *as an owned value*. We can then wrap this in another enum." (Motivation)

"`mem::replace` is very similar, but allows us to specify what to replace the value with. An equivalent to our `mem::take` line would be `mem::replace(name, String::new())`."

# Prerequisites

- **default-trait** -- `mem::take` requires the type to implement `Default`, because it replaces the taken value with `Default::default()`

# Key Properties

1. `mem::take(place)` moves the value out of `place` and replaces it with `Default::default()`
2. `mem::replace(place, new_value)` moves the value out and replaces it with `new_value`
3. Both return the original value as an owned value
4. `mem::take` requires `T: Default`; `mem::replace` does not
5. The borrow checker requires that a valid value always exists behind a `&mut` reference -- these functions maintain that invariant
6. This avoids the "clone to satisfy the borrow checker" anti-pattern
7. For `String`, `take` replaces with an empty string (no allocation needed)
8. For `Option<T>`, the `.take()` method is a shorter alternative that replaces with `None`

# Construction / Recognition

## To Apply mem::take:
1. Identify a `&mut` reference to a value you need to take ownership of
2. Ensure the value's type implements `Default`
3. Call `mem::take(place)` to get the owned value, leaving `Default::default()` behind
4. Use the owned value to construct the new variant or value

## To Apply mem::replace:
1. Identify a `&mut` reference to a value you need to take ownership of
2. Choose a replacement value of the same type
3. Call `mem::replace(place, replacement)` to get the owned value
4. Use the owned value as needed

## When to Use Which:
- Use `mem::take` when the type implements `Default` and the default is cheap (e.g., empty `String`, zero)
- Use `mem::replace` when the type doesn't implement `Default`, or you want a specific replacement
- Use `Option::take()` when working with `Option` values (replaces with `None`)

# Context & Application

This pattern is unique to Rust. In garbage-collected languages, taking a reference is sufficient (the GC tracks lifetimes). In C, you can alias a pointer and fix things later. In Rust, the ownership system requires that a valid value always exists behind a mutable reference -- you cannot simply "take" a value and leave nothing.

The source uses an evocative analogy: "like Indiana Jones, replacing the artifact with a bag of sand." You must put something back when you take something out.

**Typical contexts:**
- Changing enum variants in place (the primary use case in the source)
- Implementing state machines where states carry owned data
- Processing owned data from a struct field without consuming the struct
- Any situation where you need to move data out of a `&mut` reference

**Why not clone?** Cloning is the "Clone to satisfy the borrow checker" anti-pattern -- it introduces unnecessary allocations. `mem::take` achieves the same result with zero allocations (for types like `String` where the default is empty).

# Examples

**Example 1** (Ch. 1, "mem::{take(_), replace(_)}"): Converting enum variant A to B, moving the `name` without cloning:

```rust
use std::mem;

enum MyEnum {
    A { name: String, x: u8 },
    B { name: String },
}

fn a_to_b(e: &mut MyEnum) {
    if let MyEnum::A { name, x: 0 } = e {
        // This takes out our `name` and puts in an empty String instead
        // (note that empty strings don't allocate).
        // Then, construct the new enum variant (which will
        // be assigned to `*e`).
        *e = MyEnum::B {
            name: mem::take(name),
        }
    }
}
```

**Example 2** (Ch. 1): A multi-variant swizzle function:

```rust
use std::mem;

enum MultiVariateEnum {
    A { name: String },
    B { name: String },
    C,
    D,
}

fn swizzle(e: &mut MultiVariateEnum) {
    use MultiVariateEnum::*;
    *e = match e {
        // Ownership rules do not allow taking `name` by value, but we cannot
        // take the value out of a mutable reference, unless we replace it:
        A { name } => B {
            name: mem::take(name),
        },
        B { name } => A {
            name: mem::take(name),
        },
        C => D,
        D => C,
    }
}
```

This swaps A and B variants (carrying the name) and swaps C and D variants, all without any allocation.

# Relationships

## Builds Upon
- **default-trait** -- `mem::take` requires `Default` to provide the replacement value

## Enables
- Zero-allocation enum variant changes
- Clean state machine implementations

## Related
- **finalisation-in-destructors** -- another pattern for managing resources in complex control flow
- **constructor-idiom** -- constructors create the values that may later be taken/replaced

## Contrasts With
- "Clone to satisfy the borrow checker" anti-pattern (see anti_patterns/borrow_clone.md) -- `mem::take` achieves the same result without cloning

# Common Errors

- **Error**: Trying to move a value out of a `&mut` reference directly, causing a compile error.
  **Correction**: Use `mem::take` or `mem::replace` to swap in a replacement while extracting the owned value.

- **Error**: Using `mem::take` on a type that doesn't implement `Default`.
  **Correction**: Use `mem::replace` instead, providing an explicit replacement value.

- **Error**: Cloning a value just to satisfy the borrow checker when `mem::take` would work.
  **Correction**: If you have `&mut` access and only need the value once, use `mem::take` to avoid the allocation.

# Common Confusions

- **Confusion**: Thinking `mem::take` and `mem::replace` are unsafe operations.
  **Clarification**: Both are completely safe. They maintain the invariant that a valid value always exists behind the mutable reference -- they just swap it with something else.

- **Confusion**: Thinking this pattern applies to other languages.
  **Clarification**: "This pattern is only of interest in Rust. In GC'd languages, you'd take the reference to the value by default (and the GC would keep track of refs), and in other low-level languages like C you'd simply alias the pointer and fix things later."

- **Confusion**: Not knowing when to use `mem::take` vs `Option::take()`.
  **Clarification**: "If we are using an `Option` and want to replace its value with a `None`, `Option`'s `take()` method provides a shorter and more idiomatic alternative."

# Source Reference

Chapter 1: Idioms, "mem::{take(_), replace(_)} to keep owned values in changed enums" section. Covers Description, Example (two code examples), Motivation, Advantages, Disadvantages, Discussion, and See Also (links to "Clone to satisfy the borrow checker" anti-pattern and Default trait).

# Verification Notes

- Definition: Direct quotation from the Description and Motivation subsections
- Key Properties: All from explicit statements in the source
- Examples: Both code examples directly from the source with original comments
- Confidence: HIGH -- the source provides thorough description with two code examples, detailed motivation, and discussion
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set
