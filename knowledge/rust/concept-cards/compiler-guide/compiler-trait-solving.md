---
# === CORE IDENTIFICATION ===
concept: Compiler Trait Solving
slug: compiler-trait-solving

# === CLASSIFICATION ===
category: compiler-internals
subcategory: trait-system
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Trait Solving"
chapter_number: 19
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "trait resolution"
  - "trait solver"
  - "old trait solver"
  - "new trait solver"
  - "chalk"
  - "selection"
  - "fulfillment"
  - "obligation"
  - "candidate assembly"
  - "winnowing"
  - "confirmation"
  - "coherence"
  - "overlap check"
  - "orphan check"
  - "specialization"
  - "coinduction"
  - "implied bounds"
  - "FOHH clauses"
  - "hereditary harrop"
  - "lowering to logic"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiler-types-and-generics
extends: []
related:
  - compiler-type-checking
  - compiler-borrow-checker
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is trait resolution and what are obligations?"
  - "What are the three major parts of trait resolution (selection, fulfillment, evaluation)?"
  - "How does candidate assembly work and what is winnowing?"
  - "What is the difference between the old trait solver and the new (chalk-based) solver?"
  - "How does the trait system map onto logic programming (lowering to logic)?"
  - "What are goals and clauses in the trait solver?"
  - "What are domain goals (Implemented, ProjectionEq, Normalize, FromEnv, WellFormed)?"
  - "How does coherence checking work (overlap checks, orphan check)?"
  - "How does specialization work with the specialization graph?"
  - "What are implied bounds and how are they computed?"
  - "How does higher-ranked trait bound (HRTB) resolution work?"
  - "How does coinduction work in the trait solver?"
  - "What is canonicalization and how are queries handled in the new solver?"
  - "How does caching work in the trait solver?"
---

# Quick Definition

Trait solving (or trait resolution) is the process of pairing trait references with their implementations. It consists of three major parts: **selection** (deciding how to resolve an obligation via impls, where clauses, or built-in rules), **fulfillment** (tracking that obligations are completely satisfied through a worklist), and **evaluation** (checking obligation validity without constraining inference variables). The old solver uses a direct depth-first approach, while the new chalk-based solver recasts the trait system as logic programming using first-order hereditary harrop (FOHH) clauses. Coherence ensures no overlapping impls exist. The system handles higher-ranked trait bounds, specialization, implied bounds, and coinduction for recursive types.

# Core Definition

**Obligations**: "We use the term obligation to refer to a trait reference in need of an impl. Basically, the trait resolution system resolves an obligation by proving that an appropriate impl does exist." During type checking, trait selection verifies that obligations can be satisfied; at codegen time, selection is repeated to choose specific implementations.

## Old-Style Trait Resolution

**Selection** decides whether an obligation can be resolved and how, returning a `SelectionResult`: `Ok(Some(selection))` (resolved), `Ok(None)` (ambiguous, often due to unbound type variables), or `Err(err)` (definitely cannot resolve). Selection has two phases:

1. **Candidate assembly**: Searches for impls/where-clauses/etc. that might satisfy the obligation. For impl candidates, "this amounts to unifying the impl header (the `Self` type and the trait arguments) while ignoring nested obligations."

2. **Winnowing**: If multiple candidates exist, reduces the set using where clauses and `evaluate_candidate`. "If this reduced set yields a single, unambiguous entry, we're good to go, otherwise the result is considered ambiguous."

**Confirmation** then "unifies the output type parameters of the trait with the values found in the obligation, possibly yielding a type error."

**Fulfillment** is "a worklist of obligations to be selected: once selection is successful, the obligation is removed from the worklist and any nested obligations are enqueued. Fulfillment constrains inference variables."

**Caching** uses local (attached to `ParamEnv`) and global (attached to `tcx`) caches. "If there are any where-clauses in scope, then we use the local cache."

## Lowering to Logic (New Solver Foundation)

"The key observation here is that the Rust trait system is basically a kind of logic, and it can be mapped onto standard logical inference rules." For example, `impl<T> Clone for Vec<T> where T: Clone` becomes the Horn clause `Clone(Vec<?T>) :- Clone(?T)`.

Type-checking generic functions requires more than Horn clauses -- it needs first-order hereditary harrop (FOHH) clauses supporting universal quantification (`forall`) and implication (`if`) in goals. For `fn foo<T: Eq<T>>() { bar::<T>() }`, the type-checking goal is: `forall<T> { if (Eq(T, T)) { barWellFormed(T) } }`.

## Goals and Domain Goals

Goals have the meta-structure:
```
Goal = DomainGoal | Goal && Goal | Goal || Goal
     | exists<K> { Goal } | forall<K> { Goal }
     | if (Clause) { Goal } | true | ambiguous
```

Domain goals include:
- **Implemented(TraitRef)**: the trait is implemented for the given types
- **ProjectionEq(Projection = Type)**: associated type equals a type
- **Normalize(Projection -> Type)**: associated type normalizes to a type
- **FromEnv(TraitRef)**: trait is assumed true from in-scope where clauses
- **WellFormed(TraitRef/Type)**: type or trait reference is well-formed

## Coherence

"Coherence checking is what detects both trait impls and inherent impls overlapping with others." It has two parts:
- **Overlap checks**: Compare all pairs of implementations. Uses the explicit negative impl check (`impl_intersection_has_negative_obligation`) and the implicit negative impl check (`impl_intersection_has_impossible_obligation`).
- **Orphan check**: Ensures no other impls could exist from upstream or downstream crates.

## New Solver

The new solver uses **canonicalization** to handle queries: goals are canonicalized by replacing inference variables with bound variables and placeholders, solved in a fresh inference context, then the results are mapped back. It supports **coinduction** for recursive types: auto-traits, `Sized`, and `WF`-goals are treated coinductively, meaning infinite proof trees are valid (e.g., `List<T>: Send` recursing through `Option<Box<List<T>>>`).

# Prerequisites

- **compiler-types-and-generics** -- understanding of `ty::Ty`, `TyKind`, `ParamEnv`, generic parameters, and `Binder`/`EarlyBinder`

# Key Properties

1. **Three parts of resolution**: Selection (choose how), fulfillment (worklist tracking), evaluation (non-constraining check)
2. **Candidate assembly then winnowing**: First collect all possible candidates, then narrow down to one using where clauses and evaluation
3. **Confirmation unifies output types**: After selecting a candidate, its output types are unified with the obligation's expected types
4. **Codegen repeats selection**: "At codegen time, when we have all concrete types available, we repeat the trait selection to choose an actual implementation"
5. **FOHH clauses**: The trait system extends Horn clauses with `forall` and `if` in goals to support generic function type-checking
6. **Coherence = overlap + orphan**: Overlap checks ensure no two impls cover the same types; orphan check prevents unknown external impls
7. **Specialization graph**: Built during coherence; used to propagate defaults, not for selection itself (which does direct comparison)
8. **Implied bounds**: Explicit (computed via `inferred_outlives_of` for ADTs) and implicit (assumed from function signatures/impl headers); have known unsoundnesses (#25860, #84591, #100051)
9. **HRTB resolution**: Replace bound regions with placeholders, match impl against placeholders, check for "placeholder leaks" (no escape to outer regions)
10. **Coinduction**: "To inductively prove a goal you need a finite proof tree. To coinductively prove a goal the provided proof tree may be infinite." Uses fixpoint iteration with provisional results for cycle detection
11. **Canonicalization**: Replaces inference variables with bound existentials and placeholders with bound universals, enabling cached query results
12. **Local vs global cache**: Local cache per `ParamEnv` for context-dependent results; global cache for context-independent results
13. **Negative impls**: Explicit (`&str: !Error`) and implicit (no possible impl exists) negative reasoning used in overlap checks

# Construction / Recognition

## Trait obligation flow:
```rust,ignore
// A trait reference in need of resolution
fn clone_slice<T: Clone>(x: &[T]) -> Vec<T> {
    // At (*), we need to prove T: Clone
    let mut v = Vec::new();
    for e in &x {
        v.push((*e).clone()); // (*)
    }
}
// Selection finds that T: Clone is satisfied via the where clause bound
```

## Lowering to logic:
```text
// Rust:  impl<T> Clone for Vec<T> where T: Clone { }
// Logic: Clone(Vec<?T>) :- Clone(?T).

// Proving Clone(Vec<Vec<usize>>):
// - Clone(Vec<Vec<usize>>) if Clone(Vec<usize>) if Clone(usize) ✓
```

## Type-checking generic functions (FOHH):
```text
// fn foo<T: Eq<T>>() { bar::<T>() }
// fn bar<U: Eq<U>>() { }

fooTypeChecks :-
  forall<T> {
    if (Eq(T, T)) {
      barWellFormed(T)   // which requires Eq(T, T)
    }
  }.
```

# Context & Application

- Trait solving is central to Rust's type system -- it determines whether code is valid, which impls are used, and what associated types resolve to
- The old solver handles most practical cases but has known limitations with GATs, specialization, and some coinductive cycles
- The new solver (under active development by the Types team) recasts everything as logic programming for correctness and extensibility
- Coherence is critical for Rust's ecosystem stability -- the orphan rule ensures that adding an impl in one crate can't break another
- The distinction between `FromEnv` and `Implemented` is crucial for implied bounds: `FromEnv(TraitRef)` implies `Implemented(TraitRef)` but not vice versa
- Specialization allows overlapping impls in a containment hierarchy but is currently unstable due to soundness concerns

# Examples

**Example 1**: Winnowing resolves ambiguity. Given `impl<T: Copy> Get for T` and `impl<T: Get> Get for Box<T>`, when resolving `Get` for `Box<u16>`, both impls match initially. Winnowing eliminates the first because `Box<u16>: Copy` doesn't hold, leaving only the second impl.

**Example 2**: HRTB resolution. To check `AnyInt: for<'a> Foo<&'a isize>`, we: (1) replace `'a` with placeholder `'0`, getting `AnyInt: Foo<&'0 isize>`; (2) match against `impl<'a> Foo<&'a isize> for AnyInt`, unifying `'0 == '$a`; (3) check taint set of `'0` is `{'0, '$a}` -- only the placeholder and impl variables, so it passes. For `StaticInt` with `impl Foo<&'static isize>`, the taint set would be `{'0, 'static}`, which fails the leak check.

**Example 3**: Coinduction for recursive types. `List<T>: Send` requires `T: Send` and `Option<Box<List<T>>>: Send`, which recursively requires `List<T>: Send`. The proof tree is infinite, but coinduction allows this -- the solver detects the cycle and returns a provisional result, iterating to fixpoint.

**Example 4**: Coherence overlap check. For `impl From<MyLocalType> for Box<dyn Error>` and `impl<E: Error> From<E> for Box<dyn Error>`, the implicit negative impl check sees that `MyLocalType: Error` can never hold (no impl exists, and downstream crates can't add one for a remote trait + remote type), so the impls don't overlap.

# Relationships

## Builds Upon
- **compiler-types-and-generics** -- trait solving operates on `ty::Ty`, uses `ParamEnv` for where clauses, and requires understanding of `Binder`/`EarlyBinder` for HRTB

## Enables
- **compiler-type-checking** -- type checking invokes trait solving to verify bounds and resolve associated types
- **compiler-borrow-checker** -- borrow checking uses trait solving for well-formedness and drop check requirements

## Related
- **compiler-type-checking** -- type checking generates obligations that trait solving must satisfy
- **compiler-borrow-checker** -- region constraints from trait solving feed into borrow checking

## Contrasts With
- None within this source

# Common Errors

- **Error**: Expecting trait selection results to be stored during type checking.
  **Correction**: "During type checking, we do not store the results of trait selection. We simply wish to verify that trait selection will succeed." Results are recomputed at codegen time.

- **Error**: Relying on supertrait assumption (FromEnv) while proving the supertrait obligation itself.
  **Correction**: This creates unsound cycles with coinduction. The proposed fix is to remove the `FromEnv` -> `Implemented` implication for supertraits and instead always elaborate bounds explicitly.

- **Error**: Missing normalization of `ParamEnv` before trait solving in the old solver.
  **Correction**: The old solver requires normalized `ParamEnv`s. Use `traits::normalize_param_env_or_error` when constructing environments. The new solver does not have this requirement.

# Common Confusions

- **Confusion**: The old and new solvers are completely different systems.
  **Clarification**: The new solver is based on the same logical foundations but uses a more principled approach (FOHH clauses, canonicalization, and explicit coinduction). The old solver's concepts of selection, fulfillment, and candidate assembly have direct analogs in the new solver.

- **Confusion**: Lifetime matching is considered during selection.
  **Clarification**: "Because of how lifetime inference works, it is not possible to give back immediate feedback as to whether a unification or subtype relationship between lifetimes holds or not. Therefore, lifetime matching is not considered during selection."

- **Confusion**: Coinduction means any cycle in trait proving is acceptable.
  **Clarification**: Currently, only auto-traits, `Sized`, and `WF`-goals are coinductive. Inductive cycles return `Overflow`. Extending coinduction to all traits is planned but requires careful handling of supertrait obligations and `normalizes_to` goals.

- **Confusion**: The specialization graph is used during trait selection.
  **Clarification**: "Specialization is consulted when selecting an impl, and the graph is consulted when propagating defaults down the specialization hierarchy" -- but selection itself does direct candidate comparison rather than consulting the graph.

- **Confusion**: Coherence only checks for overlapping impls.
  **Clarification**: Coherence also includes the orphan check, which "results in an error if any other impls could exist, even if they are currently unknown. This affects impls which may get added to upstream crates in a backwards compatible way, and impls from downstream crates."

# Source Reference

Chapter 19: Trait Solving (3539 lines -- the largest chapter). Covers: old-style trait resolution (selection, candidate assembly, winnowing, where clauses, confirmation, codegen selection); higher-ranked trait bounds (HRTB matching, placeholder leaks); caching (local vs global, where clause interaction); implied bounds (explicit via `inferred_outlives_of`, implicit via WF obligations, known unsoundnesses); specialization (specialization graph, default propagation); chalk-based trait solving (logic programming foundation); lowering to logic (Horn clauses, FOHH, type-checking rules); goals and clauses (meta-structure, domain goals, WhereClause types); coherence (overlap checks, explicit/implicit negative impls, orphan check); HIR type checking and coercions; the new solver (canonicalization, ExternalConstraints, coinduction with fixpoint iteration, caching with overflow handling and cycle detection, proof trees, opaque types).

# Verification Notes

- Definition source: All key concepts drawn directly from source text with extensive examples
- Key Properties: All 13 items directly supported by explicit source content
- Confidence rationale: HIGH -- thorough coverage of both old and new solver architectures from authoritative documentation
- Uncertainties: The new solver is under active development; coinduction extension is planned but not yet fully implemented
- Cross-reference status: Related slugs reference other cards in this extraction set
