---
concept: Splitting Borrows
slug: splitting-borrows
category: unsafe-rust
subcategory: ownership-system
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Ownership and Lifetimes"
chapter_number: 3
pdf_page: null
section: "Splitting Borrows"
extraction_confidence: high
aliases:
  - "borrow splitting"
  - "disjoint borrows"
  - "split_at_mut"
  - "mutable iterators"
  - "IterMut"
prerequisites:
  - ownership-and-lifetimes
extends:
  - ownership-and-lifetimes
related:
  - nomicon-overview
contrasts_with: []
answers_questions:
  - "How can you borrow different parts of a struct mutably at the same time?"
  - "Why can't the borrow checker handle disjoint array element borrows?"
  - "How does split_at_mut work internally?"
  - "How do mutable iterators avoid violating aliasing rules?"
  - "When is unsafe code needed for split borrows vs. when is safe code sufficient?"
---

# Quick Definition

The borrow checker understands disjoint field borrows for structs but not for arrays, slices, or general containers. Splitting borrows -- taking multiple mutable references to non-overlapping parts of a data structure -- requires unsafe code for arrays/slices (via `split_at_mut`) but can often be done safely for linked structures by leveraging `Option::take` and ownership transfer.

# Core Definition

The borrow checker "understands some basic stuff, but will fall over pretty easily." It understands struct field disjointness -- borrowing `x.a`, `x.b`, and `x.c` simultaneously is fine because they are provably non-overlapping. However, it cannot understand array or slice disjointness: `&mut x[0]` and `&mut x[1]` fail because the borrow checker sees both as borrows of `x[..]`. (Ch. 3, "Splitting Borrows")

For slices, `split_at_mut` solves this by consuming the original mutable reference and producing two non-overlapping mutable slices via unsafe code:
```rust
pub fn split_at_mut(&mut self, mid: usize) -> (&mut [T], &mut [T]) {
    let len = self.len();
    let ptr = self.as_mut_ptr();
    unsafe {
        assert!(mid <= len);
        (from_raw_parts_mut(ptr, mid),
         from_raw_parts_mut(ptr.add(mid), len - mid))
    }
}
```

Mutable iterators are a related pattern. The `Iterator` trait's `next(&mut self) -> Option<Self::Item>` signature means `Self::Item` has no connection to `self`, allowing callers to hold multiple results concurrently. This works for mutable iterators because they are one-shot: each element is yielded at most once, so no two mutable references alias.

"Perhaps surprisingly, mutable iterators don't require unsafe code to be implemented for many types!" Safe implementations exist for linked lists (using `Option::take`), slices (using `split_at_mut` and `mem::take`), and trees (using `VecDeque` of node iterators). The key insight: Rust understands that struct fields can be split, and ownership transfer (via `take`) permanently relinquishes the original reference.

# Prerequisites

- **ownership-and-lifetimes** -- the borrow-checking rules and their limitations that splitting borrows addresses

# Key Properties

1. The borrow checker allows disjoint mutable borrows of struct fields simultaneously
2. The borrow checker cannot reason about disjoint borrows of array/slice elements
3. `split_at_mut` uses unsafe code to create two non-overlapping mutable slices from one
4. The `Iterator::next` signature decouples `Self::Item` from `self`, enabling concurrent retention of yielded mutable references
5. Mutable iterators are sound because they are one-shot -- each element is yielded at most once
6. Many mutable iterator implementations require no unsafe code (linked lists, trees)
7. `Option::take` and `mem::take` transfer ownership of the current element while replacing it with `None`/default
8. Slice mutable iterators use `split_at_mut` + `mem::take` to safely split off one element at a time
9. Binary tree mutable iteration can be implemented safely using `VecDeque` of node iterators

# Construction / Recognition

## To Split Borrows on Structs (Safe)

1. Simply borrow different fields: `let a = &mut x.a; let b = &mut x.b;`
2. The borrow checker understands struct field disjointness

## To Split Borrows on Slices (Unsafe Required)

1. Use `split_at_mut(mid)` to consume one mutable slice reference and produce two
2. Internally: construct two slices from raw pointers with `from_raw_parts_mut`
3. Assert that the index is in bounds before the unsafe operation

## To Implement a Safe Mutable Iterator

1. For linked structures: use `Option::take()` to move the current node out, yielding `&mut node.elem`
2. For slices: use `mem::take` to replace `self.0` with an empty slice, then `split_at_mut(1)`
3. For trees: decompose nodes into `Option<&mut elem>`, `Option<&mut left>`, `Option<&mut right>` and use `take()` on each

# Context & Application

Splitting borrows is where everyday Rust programmers encounter the limits of the borrow checker. The inability to borrow `v[0]` and `v[1]` mutably at the same time is a common pain point. The standard library provides `split_at_mut` as the safe abstraction over the necessary unsafe code, and higher-level APIs like `chunks_mut` build on it.

The mutable iterator pattern is elegant: by exploiting the `Iterator` trait's design (where `Item` is decoupled from `self`), plus ownership transfer through `Option::take`, safe mutable iteration over complex data structures becomes possible without any unsafe code. The source provides complete, working implementations for singly-linked lists, slices, and binary trees -- demonstrating that "all of these are completely safe and work on stable Rust!"

The fundamental insight is that Rust's borrow splitting for struct fields "ultimately falls out of the simple struct case" -- encoding permanent consumption of a reference through `Option` makes the pattern safe because the compiler sees that the old borrow is gone.

# Examples

**Example 1** (Ch. 3, "Splitting Borrows"): Struct fields can be borrowed disjointly:
```rust
struct Foo { a: i32, b: i32, c: i32 }
let mut x = Foo { a: 0, b: 0, c: 0 };
let a = &mut x.a;
let b = &mut x.b;
let c = &x.c;
*b += 1;
*a += 10;
println!("{} {} {} {}", a, b, c, &x.c); // Works fine
```

**Example 2** (Ch. 3, "Splitting Borrows"): Array elements cannot:
```rust
let mut x = [1, 2, 3];
let a = &mut x[0];
let b = &mut x[1]; // ERROR: cannot borrow x[..] as mutable more than once
```

**Example 3** (Ch. 3, "Splitting Borrows"): Safe mutable slice iterator using `mem::take` and `split_at_mut`:
```rust
pub struct IterMut<'a, T: 'a>(&'a mut [T]);
impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;
    fn next(&mut self) -> Option<Self::Item> {
        let slice = mem::take(&mut self.0);
        if slice.is_empty() { return None; }
        let (l, r) = slice.split_at_mut(1);
        self.0 = r;
        l.get_mut(0)
    }
}
```

# Relationships

## Builds Upon
- **ownership-and-lifetimes** -- the borrow checker's disjoint field understanding and its limitations with containers

## Enables
(none directly -- this is a practical technique for working within ownership constraints)

## Related
- **nomicon-overview** -- split_at_mut is an example of a sound safe abstraction over unsafe code

## Contrasts With
(none)

# Common Errors

- **Error**: Trying to take `&mut v[0]` and `&mut v[1]` directly, expecting the borrow checker to understand element disjointness.
  **Correction**: Use `split_at_mut(1)` to get two non-overlapping mutable slices, then index each half.

- **Error**: Implementing a mutable iterator that accidentally yields the same element twice.
  **Correction**: Use `Option::take()` or `mem::take()` to permanently move elements out of the iterator state, ensuring each element is yielded exactly once.

# Common Confusions

- **Confusion**: Thinking mutable iterators always require unsafe code.
  **Clarification**: Many mutable iterators (linked lists, trees) can be implemented entirely in safe Rust using `Option::take` and struct field splitting. Only slice-based iterators at the lowest level require unsafe (via `split_at_mut` or raw pointers).

- **Confusion**: Believing the borrow checker should be able to handle disjoint array borrows.
  **Clarification**: While simple cases like `x[0]` and `x[1]` seem obvious, the borrow checker "would still be unable to decide what outlives what in case of vector elements, which are dropped manually via pure-library code." General container disjointness is undecidable.

# Source Reference

Chapter 3: Ownership and Lifetimes, section "Splitting Borrows" -- struct field splitting, array/slice limitations, split_at_mut internals, mutable iterator pattern (Iterator trait design, linked list, slice, and binary tree implementations).

# Verification Notes

- Definition source: Direct synthesis from Ch. 3 "Splitting Borrows" section (lines 1900-2193 of source)
- Key Properties: All items directly demonstrated with complete code examples in the source
- Confidence rationale: HIGH -- the source provides complete, compilable implementations for multiple data structures with detailed explanations
- Uncertainties: None -- this is practical guidance with working code
- Cross-reference status: All slugs reference cards in the nomicon extraction set
