---
concept: Borrowed Types for Arguments
slug: borrowed-types-for-arguments
category: idiom
subcategory: null
tier: foundational
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Use borrowed types for arguments"
extraction_confidence: high
aliases:
  - "use borrowed types for arguments"
  - "deref coercion for function arguments"
  - "prefer &str over &String"
  - "prefer &[T] over &Vec<T>"
prerequisites: []
extends: []
related:
  - constructor-idiom
  - default-trait
  - collections-as-smart-pointers
contrasts_with: []
answers_questions:
  - "Why should I use &str instead of &String in function parameters?"
  - "Why should I use &[T] instead of &Vec<T> in function parameters?"
  - "What is deref coercion and how does it affect function argument types?"
  - "How do I make my Rust function accept more input types?"
---

# Quick Definition

When declaring function arguments, prefer borrowed types (`&str`, `&[T]`, `&T`) over borrowing owned types (`&String`, `&Vec<T>`, `&Box<T>`). This leverages deref coercion to accept a wider range of input types and avoids unnecessary layers of indirection.

# Core Definition

"Using a target of a deref coercion can increase the flexibility of your code when you are deciding which argument type to use for a function argument. In this way, the function will accept more input types." (Ch. 1, "Use borrowed types for arguments")

"You should always prefer using the **borrowed type** over **borrowing the owned type**. Such as `&str` over `&String`, `&[T]` over `&Vec<T>`, or `&T` over `&Box<T>`."

"Using borrowed types you can avoid layers of indirection for those instances where the owned type already provides a layer of indirection. For instance, a `String` has a layer of indirection, so a `&String` will have two layers of indirection. We can avoid this by using `&str` instead, and letting `&String` coerce to a `&str` whenever the function is invoked."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Always prefer `&str` over `&String` for function parameters
2. Always prefer `&[T]` over `&Vec<T>` for function parameters
3. Always prefer `&T` over `&Box<T>` for function parameters
4. Deref coercion automatically converts `&String` to `&str`, `&Vec<T>` to `&[T]`, etc. when the function expects the borrowed type
5. Using the borrowed type avoids unnecessary double indirection
6. A `&str` type will not coerce to a `&String` type (coercion only goes one direction)
7. String slices from `.split()` are `&str`, not `&String`, so using `&str` parameters accepts them directly

# Construction / Recognition

## To Apply This Idiom:
1. When writing a function that takes a reference to a `String`, change the parameter type from `&String` to `&str`
2. When writing a function that takes a reference to a `Vec<T>`, change the parameter type from `&Vec<T>` to `&[T]`
3. When writing a function that takes a reference to a `Box<T>`, change the parameter type from `&Box<T>` to `&T`
4. The function body remains the same -- the borrowed types support the same methods via deref

## To Recognize Violations:
1. Look for function signatures with `&String`, `&Vec<T>`, or `&Box<T>` parameters
2. Clippy will flag these as warnings (e.g., `clippy::ptr_arg`)

# Context & Application

This idiom is one of the most fundamental in Rust. It matters because Rust's type system does not implicitly allocate, so `&str` cannot be coerced to `&String` (that would require a heap allocation). However, `&String` coerces to `&str` for free via deref coercion.

**Typical contexts:**
- Any function that reads (but does not own) string data
- Any function that reads (but does not own) a sequence of elements
- Library APIs where callers may have data in various forms (`String`, `&str`, string literals, slices from `.split()`)

**Why it matters:** A function taking `&String` cannot accept string literals (`"hello"`), string slices from `.split()`, or `Cow<str>` without explicit conversion. A function taking `&str` accepts all of these automatically.

# Examples

**Example 1** (Ch. 1, "Use borrowed types for arguments"): A function checking for three consecutive vowels, first with `&String`:

```rust
fn three_vowels(word: &String) -> bool {
    let mut vowel_count = 0;
    for c in word.chars() {
        match c {
            'a' | 'e' | 'i' | 'o' | 'u' => {
                vowel_count += 1;
                if vowel_count >= 3 {
                    return true;
                }
            }
            _ => vowel_count = 0,
        }
    }
    false
}
```

With `&String`, calling `three_vowels("Ferris")` fails because a `&str` cannot coerce to `&String`.

**Example 2** (Ch. 1): Changing the signature to `fn three_vowels(word: &str) -> bool` allows both `&String` and `&str` callers. Now iterating over words from `.split(' ')` works:

```rust
fn main() {
    let sentence_string =
        "Once upon a time, there was a friendly curious crab named Ferris".to_string();
    for word in sentence_string.split(' ') {
        if three_vowels(word) {
            println!("{word} has three consecutive vowels!");
        }
    }
}
```

This prints: `curious has three consecutive vowels!`

With `&String` as the parameter type, this would not compile because `.split(' ')` yields `&str` slices, and "converting from `String` to `&str` is cheap and implicit" while the reverse "would require an allocation to be converted to `&String` which is not implicit."

# Relationships

## Builds Upon
- None -- this is a foundational idiom

## Enables
- **collections-as-smart-pointers** -- the Deref-based design that makes this coercion possible

## Related
- **constructor-idiom** -- constructors may accept owned types where ownership transfer is needed
- **default-trait** -- another foundational API design idiom

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Declaring a function parameter as `&String` and then being unable to pass string literals or slices.
  **Correction**: Change the parameter to `&str`. Deref coercion handles `&String` -> `&str` automatically.

- **Error**: Declaring a function parameter as `&Vec<T>` and being unable to pass array slices or sub-slices.
  **Correction**: Change the parameter to `&[T]`.

# Common Confusions

- **Confusion**: Thinking you need `&String` because you want to call `String` methods.
  **Clarification**: Most useful `String` methods are actually defined on `str` (e.g., `.chars()`, `.len()`, `.contains()`), so `&str` provides the same functionality.

- **Confusion**: Thinking deref coercion works in both directions.
  **Clarification**: `&String` coerces to `&str` (free, via Deref), but `&str` does NOT coerce to `&String` (would require allocation). This asymmetry is exactly why you should use the more general borrowed type.

# Source Reference

Chapter 1: Idioms, "Use borrowed types for arguments" section. See also linked resources: Rust Language Reference on Type Coercions, Herman J. Radtke III's blog series on String vs &str (2015), Steve Klabnik's blog post on "When should I use String vs &str?"

# Verification Notes

- Definition: Direct quotation from the Description subsection
- Key Properties: All from explicit statements in the source
- Examples: Both examples are directly from the source text with original code
- Confidence: HIGH -- the source provides a thorough, explicit description with multiple code examples
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set
