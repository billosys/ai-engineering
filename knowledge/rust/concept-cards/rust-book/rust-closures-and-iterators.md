---
# === CORE IDENTIFICATION ===
concept: Closures and Iterators
slug: rust-closures-and-iterators

# === CLASSIFICATION ===
category: functional-programming
subcategory: closures-and-iterators
tier: intermediate

# === PROVENANCE ===
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Functional Language Features: Iterators and Closures"
chapter_number: 13
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Fn traits"
  - "FnOnce"
  - "FnMut"
  - "Fn"
  - "iterator adapters"
  - "consuming adapters"
  - "lazy iterators"
  - "move closures"
  - "zero-cost abstractions"
  - "Iterator trait"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-generics-traits-lifetimes
  - rust-ownership-and-borrowing
  - rust-enums-and-pattern-matching
extends:
  - rust-common-programming-concepts
related:
  - rust-testing
  - rust-concurrency
  - rust-smart-pointers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a closure and how does it differ from a function?"
  - "How do closures capture values from their environment?"
  - "What are the three Fn traits and when does each apply?"
  - "What is the Iterator trait and what method must I implement?"
  - "What is the difference between consuming adapters and iterator adapters?"
  - "Why are iterators lazy and what does that mean?"
  - "How do closures and iterators perform compared to hand-written loops?"
  - "When should I use the move keyword with a closure?"
  - "What is the difference between iter, into_iter, and iter_mut?"
  - "How do I chain iterator adapters for complex transformations?"
---

# Quick Definition

Closures are anonymous functions that can capture values from their enclosing scope, and iterators provide a lazy, composable pattern for processing sequences of elements. Both are zero-cost abstractions: they compile down to code as efficient as hand-written loops while enabling a higher-level, functional programming style.

# Core Definition

The source defines closures as "anonymous functions you can save in a variable or pass as arguments to other functions. You can create the closure in one place and then call the closure elsewhere to evaluate it in a different context. Unlike functions, closures can capture values from the scope in which they're defined" (Ch. 13, "Closures").

Closures capture values in three ways, mapping to the three `Fn` traits: "**`FnOnce`** applies to closures that can be called once. All closures implement at least this trait." "**`FnMut`** applies to closures that don't move captured values out of their body but might mutate the captured values. These closures can be called more than once." "**`Fn`** applies to closures that don't move captured values out of their body and don't mutate captured values" (Ch. 13, "Moving Captured Values Out of Closures").

The **iterator pattern** "allows you to perform some task on a sequence of items in turn." In Rust, "iterators are _lazy_, meaning they have no effect until you call methods that consume the iterator to use it up" (Ch. 13, "Processing a Series of Items with Iterators"). All iterators implement the `Iterator` trait, which requires defining one method: `next`, returning `Option<Self::Item>`.

Regarding performance, the source states: "Iterators, although a high-level abstraction, get compiled down to roughly the same code as if you'd written the lower-level code yourself. Iterators are one of Rust's _zero-cost abstractions_" (Ch. 13, "Performance in Loops vs. Iterators").

# Prerequisites

- **Generics, Traits, and Lifetimes** -- closures implement `Fn` traits, iterators use the `Iterator` trait with associated types, and trait bounds constrain which closures functions accept
- **Ownership and Borrowing** -- closure capture modes (immutable borrow, mutable borrow, move) directly correspond to ownership rules
- **Enums and Pattern Matching** -- the `Iterator::next` method returns `Option<Self::Item>`, and closures are commonly used with `Option::unwrap_or_else`

# Key Properties

1. **Closure syntax**: `|params| body` -- pipes delimit parameters, type annotations are optional, braces are optional for single-expression bodies
2. **Type inference**: closure parameter and return types are inferred from usage, then locked to those concrete types for all subsequent calls
3. **Three capture modes**: closures borrow immutably, borrow mutably, or take ownership, depending on what the body does with captured values
4. **`move` keyword**: forces a closure to take ownership of captured values, essential when passing closures to new threads
5. **`Fn` trait hierarchy**: `FnOnce` (superset, all closures) > `FnMut` (can be called multiple times, may mutate) > `Fn` (can be called multiple times, no mutation) -- each is a superset of the next
6. **Functions implement `Fn` traits**: named functions can be used wherever a closure implementing an `Fn` trait is expected (e.g., `unwrap_or_else(Vec::new)`)
7. **`Iterator` trait**: requires only `fn next(&mut self) -> Option<Self::Item>`; all other methods have default implementations
8. **Associated type `Item`**: defines the type of elements the iterator yields
9. **Three iterator constructors**: `iter()` yields immutable references, `iter_mut()` yields mutable references, `into_iter()` yields owned values
10. **Consuming adapters** (e.g., `sum`, `collect`): call `next` internally and consume the iterator
11. **Iterator adapters** (e.g., `map`, `filter`): produce new iterators by transforming the original; they are lazy until consumed
12. **Chaining**: iterator adapters can be chained for readable, composable data transformations
13. **`collect`**: consumes an iterator and gathers results into a collection (Vec, HashMap, etc.)
14. **Zero-cost**: benchmark results show iterator-based code matches `for` loop performance; the compiler applies unrolling and bounds-check elimination

# Construction / Recognition

## Defining Closures (Four Equivalent Forms):
```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }   // function
let add_one_v2 = |x: u32| -> u32 { x + 1 };   // fully annotated closure
let add_one_v3 = |x|             { x + 1 };   // type-inferred closure
let add_one_v4 = |x|               x + 1  ;   // minimal closure
```

## Closure Capturing an Immutable Reference:
```rust
let list = vec![1, 2, 3];
let print_list = || println!("{list:?}");
print_list();
```

## Closure with `move` for Thread Safety:
```rust
use std::thread;
let list = vec![1, 2, 3];
thread::spawn(move || println!("{list:?}"))
    .join()
    .unwrap();
```

## Implementing the Iterator Pattern:
```rust
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
    // methods with default implementations elided
}
```

## Chaining Iterator Adapters:
```rust
let v1: Vec<i32> = vec![1, 2, 3];
let v2: Vec<i32> = v1.iter().map(|x| x + 1).collect();
// v2 == [2, 3, 4]
```

## Using `filter` with Environment-Capturing Closure:
```rust
fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
    shoes.into_iter()
         .filter(|s| s.size == shoe_size)
         .collect()
}
```

## Replacing `clone` with Iterator Ownership (from Ch. 12 refactoring):
```rust
// Before: fn build(args: &[String]) with clone
// After: fn build(mut args: impl Iterator<Item = String>)
//   args.next() returns owned String values, no clone needed
```

# Context & Application

Chapter 13 presents closures and iterators as Rust's answer to functional programming idioms. The chapter builds on the Ch. 12 `minigrep` project to demonstrate how iterators eliminate unnecessary `clone` calls and how `filter` + `collect` replaces mutable accumulator patterns.

**Practical contexts:**
- Passing behavior as arguments to functions (sorting with `sort_by_key`, error handling with `unwrap_or_else`)
- Transforming collections with `map`, `filter`, `flat_map`, and other adapters
- Building lazy processing pipelines that only compute on demand
- Moving data into threads with `move` closures
- Writing idiomatic Rust that favors iterator chains over manual loops

**Design philosophy:** The source notes that "most Rust programmers prefer to use the iterator style" because "the code focuses on the high-level objective of the loop. This abstracts away some of the commonplace code so that it's easier to see the concepts that are unique to this code, such as the filtering condition" (Ch. 13, "Choosing Between Loops and Iterators").

**Performance insight:** A benchmark in the source comparing `for` loop vs. iterator implementations of `search` showed nearly identical performance (~19.6M ns/iter vs. ~19.2M ns/iter), confirming the zero-cost abstraction claim (Ch. 13, "Performance in Loops vs. Iterators").

# Examples

**Example 1** (Ch. 13, Listing 13-1): The `giveaway` method uses `unwrap_or_else` with a closure that captures `&self`:
```rust
user_preference.unwrap_or_else(|| self.most_stocked())
```
The closure captures an immutable reference to the `Inventory` instance.

**Example 2** (Ch. 13, Listing 13-3): Type inference locks closure types after first use -- calling a closure first with `String` then with `i32` produces a compile error because the types were inferred and locked on the first call.

**Example 3** (Ch. 13, Listings 13-7 through 13-9): `sort_by_key` requires `FnMut`, so a closure that moves a value out of the environment (implementing only `FnOnce`) is rejected. The fix: use a mutable counter reference instead of moving values out.

**Example 4** (Ch. 13, Listing 13-12): Calling `next()` directly on an iterator demonstrates that it returns `Some(&1)`, `Some(&2)`, `Some(&3)`, then `None`.

**Example 5** (Ch. 13, Listing 13-14 and 13-15): Calling `map` alone produces a warning because iterators are lazy. Adding `collect()` consumes the iterator and produces the transformed vector.

**Example 6** (Ch. 13, Listing 13-16): `shoes_in_size` uses `into_iter().filter(|s| s.size == shoe_size).collect()` -- the closure captures `shoe_size` from the environment.

**Example 7** (Ch. 13, Listings 13-17 through 13-20): Refactoring `Config::build` from `&[String]` with `.clone()` to `impl Iterator<Item = String>` with `.next()` eliminates unnecessary allocations.

# Relationships

## Builds Upon
- **Generics, Traits, and Lifetimes** -- `Fn`/`FnMut`/`FnOnce` are traits; `Iterator` uses associated types; `impl Trait` syntax appears in function signatures
- **Ownership and Borrowing** -- closure capture modes are determined by ownership rules

## Enables
- **Concurrency** -- `move` closures are essential for `thread::spawn`; iterators enable parallel processing patterns
- **Custom Iterators** -- implementing `Iterator` for custom types (covered in later chapters)

## Related
- **Testing** -- iterator-based code is demonstrated through test-driven development in Ch. 12
- **Smart Pointers** -- `Deref` and iterator interaction; smart pointers can implement `IntoIterator`

## Contrasts With
- None explicitly within this source; conceptually, the imperative loop style is contrasted with the functional iterator style

# Common Errors

- **Error**: Forgetting to consume a lazy iterator -- calling `map` without `collect` or another consuming adapter has no effect and produces a compiler warning.
  **Correction**: Always terminate an iterator adapter chain with a consuming method like `collect()`, `sum()`, `for_each()`, or use it in a `for` loop.

- **Error**: Trying to use a closure that moves values out of the environment with `sort_by_key` (which requires `FnMut`).
  **Correction**: Ensure the closure only borrows or mutates captured values, never moves them out. Use a mutable counter instead of pushing moved values.

- **Error**: Attempting to use `v1_iter` after calling `sum()` or another consuming adapter on it.
  **Correction**: Consuming adapters take ownership of the iterator. Create a new iterator if you need to iterate again.

- **Error**: Expecting closure types to be flexible after first use -- calling the same closure with a `String` and then an `i32`.
  **Correction**: Closure types are inferred and locked on first use. Use generics or separate closures for different types.

# Common Confusions

- **Confusion**: Thinking closures have runtime overhead because they capture environment values.
  **Clarification**: Closures are compiled into anonymous structs that capture the environment at compile time. There is no dynamic dispatch or heap allocation unless explicitly boxed.

- **Confusion**: Thinking `move` means the closure always takes `FnOnce` semantics.
  **Clarification**: `move` controls how values enter the closure (forces ownership transfer into the closure), not what the closure body does with them. A `move` closure that only reads captured values still implements `Fn`.

- **Confusion**: Believing iterators are slower than manual loops because they are "higher level."
  **Clarification**: Benchmarks in the source show equivalent performance. The compiler applies optimizations like loop unrolling and bounds-check elimination to iterator code.

- **Confusion**: Conflating `iter()`, `into_iter()`, and `iter_mut()`.
  **Clarification**: `iter()` yields `&T` (immutable references), `iter_mut()` yields `&mut T` (mutable references), and `into_iter()` yields `T` (owned values, consuming the collection).

# Source Reference

Chapter 13: Functional Language Features: Iterators and Closures. Sections: "Closures" (capturing the environment, type inference, capturing references/moving ownership, `Fn` traits), "Processing a Series of Items with Iterators" (`Iterator` trait, `next`, consuming adapters, iterator adapters, closures that capture), "Improving Our I/O Project" (removing `clone`, iterator-based `Config::build`, iterator adapters in `search`), "Performance in Loops vs. Iterators" (benchmarks, zero-cost abstractions). Also incorporates refactoring concepts from Chapter 12 as demonstrated in Chapter 13. No page numbers (online documentation source).

# Verification Notes

- Closure definition: directly quoted from Ch. 13, "Closures" section opening
- `Fn` trait descriptions: directly quoted from "Moving Captured Values Out of Closures" section
- Iterator laziness: directly quoted from "Processing a Series of Items with Iterators" opening
- Zero-cost abstraction claim and benchmark: directly quoted from "Performance in Loops vs. Iterators"
- Benchmark numbers: `19,620,300 ns/iter` (for loop) vs `19,234,900 ns/iter` (iterator) from source text
- Chapter 12 refactoring: concepts are presented in Ch. 13 with explicit back-references to Ch. 12 listings
- Confidence: HIGH -- Ch. 13 provides explicit definitions, trait descriptions, and benchmark data
- Cross-references: all slug references correspond to planned or existing concept cards
- Uncertainties: None; all concepts have explicit definitions and worked examples
