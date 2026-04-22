---
concept: Imperative vs Declarative Programming
slug: imperative-vs-declarative
category: functional-programming
subcategory: null
tier: foundational
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "Functional Usage of Rust"
chapter_number: 4
pdf_page: null
section: "Programming paradigms"
extraction_confidence: high
aliases:
  - "programming paradigms"
  - "imperative vs functional"
  - "how vs what"
prerequisites: []
extends: []
related:
  - generics-as-type-classes
  - functional-optics
contrasts_with: []
answers_questions:
  - "What is the difference between imperative and declarative programming in Rust?"
  - "How does Rust support functional programming paradigms?"
  - "What is fold and how does it relate to declarative programming?"
---

# Quick Definition

Imperative programs describe **how** to do something (step-by-step mutation of state), while declarative programs describe **what** to do (composing functions to transform data). Rust is fundamentally an imperative language but supports many functional/declarative paradigms through iterators, closures, and combinators like `fold`.

# Core Definition

Functional programming is a programming paradigm where programs are constructed by applying and composing functions. It is a declarative programming paradigm in which function definitions are trees of expressions that each return a value, rather than a sequence of imperative statements which change the state of the program. One of the biggest hurdles to understanding functional programs when coming from an imperative background is the shift in thinking: imperative programs describe **how** to do something, whereas declarative programs describe **what** to do. Rust supports both paradigms, allowing developers to choose the most expressive approach for each situation.

# Prerequisites

None -- this is a foundational concept about programming paradigms.

# Key Properties

1. Imperative style uses mutable state and explicit loops (`for`, `while`) to describe step-by-step computation
2. Declarative style uses function composition, closures, and iterator combinators to describe the desired result
3. Rust supports both paradigms -- it is an imperative language that follows many functional programming paradigms
4. `fold` is a key combinator from functional programming (named after the Haskell convention) that composes a function over a sequence with an accumulator
5. The declarative style often produces more concise code but requires familiarity with combinators
6. Both styles produce equivalent results; the choice is about expressiveness and readability

# Construction / Recognition

## Imperative Style (the "how"):
```rust
let mut sum = 0;
for i in 1..11 {
    sum += i;
}
println!("{sum}");
```
Uses mutable variable `sum`, explicit loop, and step-by-step accumulation.

## Declarative Style (the "what"):
```rust
println!("{}", (1..11).fold(0, |a, b| a + b));
```
Uses `fold` to compose an addition closure over the range. No mutable state. The `0` is the initial accumulator value; `a` is the running accumulator and `b` is each element from the range.

## Fold Step-by-Step:

| `a` | `b` | result |
| :-: | :-: | :----: |
|  0  |  1  |   1    |
|  1  |  2  |   3    |
|  3  |  3  |   6    |
|  6  |  4  |   10   |
| 10  |  5  |   15   |
| 15  |  6  |   21   |
| 21  |  7  |   28   |
| 28  |  8  |   36   |
| 36  |  9  |   45   |
| 45  | 10  |   55   |

# Context & Application

Rust's iterator combinators (`map`, `filter`, `fold`, `collect`, etc.) are the primary way to write declarative-style code. The compiler optimizes iterator chains aggressively through monomorphization and inlining, so the declarative style often has zero overhead compared to hand-written imperative loops. This makes Rust unusual among systems languages -- you can write in a functional style without sacrificing performance. The source presents this as a foundational concept before introducing more advanced functional patterns like generics as type classes and optics.

# Examples

**Example 1** (Ch. 4, "Programming paradigms"): Summing 1 to 10 imperatively:

```rust
let mut sum = 0;
for i in 1..11 {
    sum += i;
}
println!("{sum}");
```

The source notes: "With imperative programs, we have to play compiler to see what is happening. Here, we start with a `sum` of `0`. Next, we iterate through the range from 1 to 10. Each time through the loop, we add the corresponding value in the range."

**Example 2** (Ch. 4, "Programming paradigms"): The same computation declaratively:

```rust
println!("{}", (1..11).fold(0, |a, b| a + b));
```

The source explains: "`fold` is a function that composes functions. The name is a convention from Haskell." The closure `|a, b| a + b` is composed over the range, starting from accumulator `0`.

# Relationships

## Builds Upon
- Basic Rust syntax (closures, ranges, iterators)

## Enables
- **generics-as-type-classes** -- the functional paradigm extends to how Rust's type system encodes behavior
- **functional-optics** -- optics are a purely functional concept that builds on declarative composition

## Related
- Rust's iterator trait and combinator methods (`map`, `filter`, `fold`, `collect`)

## Contrasts With
- None in this extraction set

# Common Errors

- **Error**: Assuming declarative style is always more readable.
  **Correction**: For simple operations like summing, declarative style is often clearer. For complex multi-step transformations with side effects, imperative style may be more readable. Choose based on the situation.

- **Error**: Mixing mutable state with iterator chains (e.g., using `for_each` to mutate external state).
  **Correction**: If you need side effects, either use an imperative loop or use `fold`/`collect` to produce a new value rather than mutating in place.

# Common Confusions

- **Confusion**: Thinking Rust is a functional language.
  **Clarification**: The source explicitly states "Rust is an imperative language, but it follows many functional programming paradigms." Rust supports both styles; it is not purely functional.

- **Confusion**: Thinking `fold` is specific to Rust.
  **Clarification**: `fold` is a standard functional programming combinator named after the Haskell convention. It is equivalent to `reduce` in Python/JavaScript (with an initial value) or `inject` in Ruby.

# Source Reference

Chapter 4: Functional Usage of Rust, "Programming paradigms" section. The source presents both imperative and declarative styles with the same summing example, including step-by-step tables showing the computation.

# Verification Notes

- Definition source: Direct quotation from the chapter introduction and "Programming paradigms" section
- Key Properties: All from explicit statements in the source
- Confidence rationale: HIGH -- the source provides clear definitions, concrete examples with tables, and explicit contrast between paradigms
- Uncertainties: None for the definition
- Cross-reference status: `generics-as-type-classes` and `functional-optics` are sibling cards in this extraction set
