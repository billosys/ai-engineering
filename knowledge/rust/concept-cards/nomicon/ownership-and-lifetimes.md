---
concept: Ownership and Lifetimes
slug: ownership-and-lifetimes
category: unsafe-rust
subcategory: ownership-system
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Ownership and Lifetimes"
chapter_number: 3
pdf_page: null
section: "References / Aliasing / Lifetimes / Limits of Lifetimes"
extraction_confidence: high
aliases:
  - "borrow checking"
  - "reference rules"
  - "aliasing model"
  - "lifetime regions"
  - "borrow semantics"
prerequisites:
  - nomicon-overview
extends: []
related:
  - lifetime-elision-and-bounds
  - subtyping-and-variance
  - drop-check-and-phantom-data
  - splitting-borrows
contrasts_with: []
answers_questions:
  - "What are the two fundamental rules of Rust references?"
  - "Why does aliasing matter for compiler optimizations?"
  - "What is a lifetime in the Nomicon's formulation?"
  - "When does the borrow checker over-reject valid programs?"
  - "What does it mean for a reference to be 'alive'?"
  - "How does the borrow checker reason about lifetimes across function boundaries?"
---

# Quick Definition

Rust's ownership system enforces two rules for references: a reference cannot outlive its referent, and a mutable reference cannot be aliased. Lifetimes are named regions of code that a reference must be valid for, and the borrow checker enforces these rules through lifetime analysis -- sometimes rejecting programs that are semantically correct but inexpressible in the lifetime system.

# Core Definition

References come in two kinds: shared (`&T`) and mutable (`&mut T`), obeying two rules: (1) a reference cannot outlive its referent, and (2) a mutable reference cannot be aliased. "That's it. That's the whole model references follow." (Ch. 3, "References")

**Aliasing** means variables or pointers refer to overlapping regions of memory. Aliasing matters because it constrains compiler optimizations: without aliasing guarantees, the compiler cannot cache reads, eliminate writes, reorder operations, or vectorize loops. The source provides a detailed example where `compute(&x, &mut x)` would defeat an optimization that caches `*input` -- Rust's `&mut` non-aliasing guarantee makes this optimization sound. "The key thing to remember about alias analysis is that writes are the primary hazard for optimizations." (Ch. 3, "Aliasing")

**Lifetimes** are "named regions of code that a reference must be valid for." They may have holes (a reference can be invalidated and reinitialized) and may correspond to paths of execution, not just lexical scopes. The borrow checker minimizes lifetime extents. Within a function, lifetimes are inferred; across function boundaries, they must be declared. Each `let` statement implicitly introduces a scope, and the borrow checker desugars references into these implicit scopes.

A reference (borrow) is **alive** from its creation to its last use. A borrowed value needs to outlive only borrows that are alive. If a value has a destructor, the destructor counts as a use at end of scope, extending the borrow's liveness. Lifetimes can have pauses -- a variable can be reborrowed after a previous borrow dies.

The lifetime system is "much more coarse than the reference semantics we're actually interested in preserving." The source shows two concrete cases where valid programs are rejected: `mutate_and_share` (returning `&Self` from `&mut self` extends the mutable borrow's lifetime) and `get_default` on `HashMap` (the borrow checker cannot see that the first mutable borrow is dead before the second begins in different match arms).

# Prerequisites

- **nomicon-overview** -- understanding the safe/unsafe boundary and soundness is needed to appreciate why these rules exist and where they become limiting

# Key Properties

1. Two reference rules: (a) cannot outlive referent, (b) mutable reference cannot be aliased
2. Aliasing = variables/pointers referring to overlapping memory regions
3. No-aliasing guarantees enable: caching reads, eliminating writes, reordering operations, loop vectorization
4. Lifetimes are regions of code (not just scopes) that may have holes
5. The borrow checker minimizes lifetime extents -- borrows shrink to the minimum necessary region
6. Each `let` statement implicitly introduces a scope boundary for lifetime analysis
7. A reference is alive from creation to last use; destructors count as a use
8. Cross-function lifetimes must be declared explicitly with `'a` syntax
9. The lifetime system is coarser than true reference semantics -- it rejects some valid programs
10. Rust's aliasing model is not yet formally defined; the Nomicon uses a "broadest possible definition"

# Construction / Recognition

## To Understand Why a Borrow Check Fails

1. Identify all borrows (shared and mutable) and their creation points
2. Find the last use of each borrow (including implicit destructor calls)
3. The region between creation and last use is the borrow's lifetime
4. Check if any mutable borrow's lifetime overlaps with another borrow of the same data
5. Check if any borrow outlives its referent
6. If the program is correct but rejected, it may be a limitation of the lifetime system's coarseness

## To Trace Lifetime Desugaring

1. Annotate each `let` with an implicit scope
2. For references, determine the minimum lifetime needed (smallest containing scope)
3. For cross-function references, identify which input lifetime constrains the output
4. Check if lifetime extension from destructors causes unexpected overlap

# Context & Application

The Nomicon's treatment of lifetimes goes deeper than The Book by showing the desugared form of lifetime inference. Where The Book teaches "lifetimes prevent dangling references," the Nomicon shows exactly how the borrow checker reasons by assigning implicit scope labels and tracking liveness. This understanding is essential for unsafe code authors who must uphold these invariants manually.

The aliasing discussion is particularly important for understanding why `&mut` exclusivity exists: it's not just about preventing data races (that's a concurrent concern), but fundamentally about enabling compiler optimizations. The `compute(input, output)` example shows that without aliasing guarantees, the compiler cannot cache a read of `*input` across a write to `*output`, preventing basic optimizations like constant folding and branch elimination.

The "limits of lifetimes" section is crucial for unsafe code: when the lifetime system is too conservative, unsafe code can sometimes bridge the gap by rewriting with raw pointers and manually ensuring the invariants hold. Understanding exactly where and why the system over-rejects helps identify safe uses of unsafe.

# Examples

**Example 1** (Ch. 3, "Lifetimes"): Returning a reference to a local -- the classic dangling reference:
```rust
fn as_str<'a>(data: &'a u32) -> &'a str {
    let s = format!("{}", data);
    &s  // ERROR: s lives in a shorter scope than 'a
}
```

**Example 2** (Ch. 3, "Aliasing"): Why alias analysis matters for optimization. Given `compute(input: &u32, output: &mut u32)`, the compiler can cache `*input` and merge branches because `&mut` guarantees `input` and `output` don't alias.

**Example 3** (Ch. 3, "Limits of Lifetimes"): A method `mutate_and_share(&mut self) -> &Self` that returns a shared reference extends the mutable borrow's lifetime to match the return value's lifetime, preventing subsequent shared borrows even though the mutable phase is over:
```rust
let loan = foo.mutate_and_share();
foo.share(); // ERROR: foo is still mutably borrowed because loan is alive
println!("{:?}", loan);
```

**Example 4** (Ch. 3, "The area covered by a lifetime"): Destructors extend borrow liveness:
```rust
struct X<'a>(&'a i32);
impl Drop for X<'_> { fn drop(&mut self) {} }
let x = X(&data[0]);
println!("{:?}", x);
data.push(4); // ERROR: x's destructor runs at end of scope, extending the borrow
```

# Relationships

## Builds Upon
- **nomicon-overview** -- the ownership system is what makes Safe Rust safe

## Enables
- **lifetime-elision-and-bounds** -- elision rules simplify the lifetime annotations described here
- **subtyping-and-variance** -- subtyping of lifetimes builds on the concept of lifetime regions
- **drop-check-and-phantom-data** -- drop checking extends the lifetime analysis described here
- **splitting-borrows** -- techniques for working around borrow checker limitations

## Related
- **type-conversions** -- lifetime coercions are a form of type conversion

## Contrasts With
(none)

# Common Errors

- **Error**: Assuming the borrow checker tracks field-level aliasing through containers like `Vec`.
  **Correction**: The borrow checker does not understand `Vec` internals. It sees `x = &data[0]` as a borrow of `data`, not of `data`'s first element. So `data.push(4)` conflicts with any live borrow derived from `data`.

- **Error**: Forgetting that destructors count as a "use" of a borrow.
  **Correction**: If a type has a `Drop` impl, the destructor runs at end of scope and counts as the last use of any references it holds. Use `drop(x)` to end the borrow earlier if needed.

# Common Confusions

- **Confusion**: Thinking lifetimes are lexical (scope-based).
  **Clarification**: Since non-lexical lifetimes (NLL), a borrow is alive from creation to last use, not to end of scope. Lifetimes may have gaps and can cover branches differently.

- **Confusion**: Believing the borrow checker rejects only invalid programs.
  **Clarification**: The lifetime system is deliberately coarser than the true reference semantics. It rejects some programs that are valid (like the `mutate_and_share` and `get_default` examples) because the lifetime system cannot express the precise relationships involved.

- **Confusion**: Thinking aliasing only matters for thread safety.
  **Clarification**: Aliasing matters primarily for single-threaded compiler optimizations (caching reads, eliminating writes, reordering). Thread safety is a separate concern addressed by `Send`/`Sync`.

# Source Reference

Chapter 3: Ownership and Lifetimes -- References (two rules), Aliasing (why it matters, optimization examples), Lifetimes (desugaring, scope introduction, liveness), Limits of Lifetimes (mutate_and_share, get_default, improperly reduced borrows).

# Verification Notes

- Definition source: Direct synthesis from Ch. 3, first four major sections (lines 1-671 of source)
- Key Properties: Items 1-2 are direct quotations; items 3-10 are synthesized from explicit discussion with examples
- Confidence rationale: HIGH -- the source provides detailed desugared examples and explicit discussion of limitations
- Uncertainties: The source explicitly states Rust's aliasing model is not yet defined ("Unfortunately, Rust hasn't actually defined its aliasing model")
- Cross-reference status: All slugs reference cards in the nomicon extraction set
