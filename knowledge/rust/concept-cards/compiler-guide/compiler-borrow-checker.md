---
# === CORE IDENTIFICATION ===
concept: Compiler Borrow Checker
slug: compiler-borrow-checker

# === CLASSIFICATION ===
category: compiler-internals
subcategory: borrow-checking
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Borrow Checker"
chapter_number: 21
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "MIR borrow check"
  - "NLL"
  - "non-lexical lifetimes"
  - "region inference"
  - "dataflow analysis"
  - "move paths"
  - "drop elaboration"
  - "drop check"
  - "dropck_outlives"
  - "rustc_borrowck"
  - "universal regions"
  - "placeholder regions"
  - "universes"
  - "member constraints"
  - "constraint propagation"
  - "MIR type check"
  - "user type annotations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiler-types-and-generics
  - compiler-trait-solving
  - compiler-type-checking
extends: []
related:
  - compiler-diagnostics
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What properties does the borrow checker enforce?"
  - "What are the major phases of the MIR borrow checker?"
  - "How does dataflow analysis work in rustc (Analysis trait, transfer functions, fixpoint)?"
  - "What is drop elaboration and how are dynamic drops handled?"
  - "How do move paths track initialization and moves at field granularity?"
  - "What is the MIR type-check and how does it relate to region inference?"
  - "How does NLL region inference work (universal regions, region variables, constraints)?"
  - "What are placeholders and universes and how do they prevent illegal lifetimes?"
  - "How does drop check (dropck_outlives) determine what regions must be live when dropping?"
  - "What is the difference between use-live and drop-live?"
  - "What are member constraints and how do they work with opaque types?"
  - "How are user type annotations preserved through MIR type checking?"
---

# Quick Definition

The MIR borrow checker is "Rust's secret sauce" -- it enforces that variables are initialized before use, values aren't moved twice, values aren't accessed while mutably borrowed, and places aren't mutated while immutably borrowed. It operates on MIR (enabling non-lexical lifetimes) through multiple phases: replacing regions with inference variables, performing dataflow analyses for move/initialization tracking, running a MIR type-check to generate region constraints, performing region inference to compute lifetime values as sets of control-flow graph points, and finally walking the MIR to check borrowing rules against the computed state. Supporting infrastructure includes dataflow analysis (lattice-based fixpoint computation), drop elaboration (transforming imprecise drops into precise ones using drop flags), and move paths (tracking initialization at field granularity).

# Core Definition

## MIR Borrow Check Overview

The borrow checker enforces multiple properties: "that all variables are initialized before they are used; that you can't move the same value twice; that you can't move a value while it is borrowed; that you can't access a place while it is mutably borrowed; that you can't mutate a place while it is immutably borrowed."

Operating on MIR has key advantages: "the MIR is far less complex than the HIR; the radical desugaring helps prevent bugs" and "using the MIR enables 'non-lexical lifetimes', which are regions derived from the control-flow graph."

### Major Phases

The main entry point is the `mir_borrowck` query in `rustc_borrowck`:

1. **Create local MIR copy** and invoke `replace_regions_in_mir` to replace all regions with fresh inference variables
2. **Dataflow analyses** compute what data is moved and when
3. **MIR type-check** walks the MIR to determine all region constraints between different regions
4. **Region inference** computes values for each region as sets of control-flow-graph points
5. **Compute borrows in scope** at each point
6. **Final walk** over MIR to check actions and report errors

## Dataflow Analysis

The dataflow framework is defined by the `Analysis` trait. The domain must be a join-semilattice with a well-behaved join operator. Transfer functions are specified per-statement/terminator as "effects" applied successively. The framework supports both forward and backward analyses.

Convergence requires: `bottom join x = x` and `top join x = top`. The framework iterates to fixpoint, which always exists. Results can be inspected via `ResultsCursor` (for specific locations) or `ResultsVisitor` (for all locations).

Key analyses include `MaybeInitializedPlaces` and `MaybeUninitializedPlaces`, used by drop elaboration.

## Drop Elaboration

"The presence of `Drop` terminators does not guarantee that a destructor will run" because the target may be uninitialized. Drop elaboration transforms imprecise drops into precise ones using drop flags.

Each drop is classified as: **Static** (always initialized), **Dead** (always uninitialized), **Conditional** (wholly initialized or wholly uninitialized), or **Open** (may be partly initialized). For Open drops, individual fields are recursively categorized, with enum variants treated as fields where only the active variant's drops apply.

Drop glue "first calls `<T as Drop>::drop` and then recursively calls the drop glue of any recursively owned values." `ManuallyDrop<U>` does not own `U`; `PhantomData<U>` does not own anything.

## Move Paths

Initialization is tracked at field granularity via `MovePath`s that "roughly correspond to the concept of a `Place` from MIR." Not every Place gets a MovePath -- illegal moves (from array elements, through borrowed references) are excluded, reducing overhead.

MovePaths are structured as a tree with parent/child relationships and indexed via `MovePathIndex`. The `MovePathLookup` in `MoveData` provides reverse lookups from Places to MovePathIndices.

## MIR Type-Check

The MIR type-check "walks the MIR and does a complete 'type check'" to uncover region constraints. It preserves **user type annotations** (`CanonicalUserTypeAnnotations`) to enforce explicit lifetime annotations like `let y: &'static u32 = x`, which would otherwise be lost when regions are replaced with inference variables.

Two kinds of annotations: explicit type ascriptions (`UserType::Ty`) and explicit generic arguments (`UserType::TypeOf`). Inference variables in annotations are replaced with existential bound variables.

## Drop Check

"`dropck_outlives` determines what regions must be live when a value is dropped. Two liveness computations: **use-live** (value may be used, entire type must be valid) and **drop-live** (value may be dropped, only dropck-required regions must be valid).

For a type `T`: if `T` has an explicit `Drop`, all generic arguments must be live (unless marked `#[may_dangle]`); regardless, recurse into owned types. Notable difference from `Ty::needs_drop`: `PhantomData<U>` is considered to own `U` by dropck but not by needs_drop; zero-length arrays are treated differently.

## Region Inference (NLL)

**Universal regions** are those appearing free in the function (from signature, like `'a` in `fn foo<'a>(...)`). They are computed by `replace_regions_in_mir`.

**Region variables** have values that are sets of `RegionElement`s: MIR locations (point on entry to a statement), `end('a)` for universal regions (representing the caller's CFG), `end('static)`, and `placeholder(n)` for placeholder regions.

**Constraints**: (1) Outlives constraints (`'a: 'b`) from MIR type-check; (2) Liveness constraints (region must be live where it can be used).

**Inference**: Start each region with its liveness constraint set, then iterate outlives constraints, growing regions until fixpoint. For `'a: 'b`, all points in `'b`'s value are added to `'a`. After propagation, check that universal regions haven't grown "too large."

## Placeholders and Universes

Placeholders represent "some unknown region" used when checking higher-ranked subtyping (e.g., `fn(&'static u32) <: for<'a> fn(&'a u32)`). Bound regions in the supertype are replaced with placeholders (`!1`).

**Universes** form a tree of name scopes. The root universe U0 contains global names (`'static`, generic params). Each `for<'a>` introduces a child universe. "A variable in universe U3 may name `placeholder(1)`, `placeholder(2)`, and `placeholder(3)`, but not `placeholder(4)`." In practice, universes are tracked as a counter, relying on the type checker's structure to prevent illegal communication between sibling universes.

## Member Constraints

Used for opaque types (impl Trait). A member constraint `'0 member of ['a, 'b, 'static]` says the region must equal one of the choices. Resolved by considering lower bounds (region must outlive) and upper bounds (must be outlived by), then selecting the minimal remaining choice.

# Prerequisites

- **compiler-types-and-generics** -- region kinds (`EarlyParam`, `LateParam`, `Bound`, `Placeholder`), `ParamEnv`, generic parameters
- **compiler-trait-solving** -- trait solving generates well-formedness obligations checked during borrow checking
- **compiler-type-checking** -- MIR type-check builds on type inference infrastructure (`InferCtxt`, region constraints)

# Key Properties

1. **MIR-based**: Operating on MIR (not HIR) enables non-lexical lifetimes and prevents bugs through radical desugaring
2. **Region values as sets**: Each region's value is a set of `RegionElement`s -- CFG locations, `end(universal_region)`, and `placeholder(n)`
3. **Fixpoint constraint propagation**: Outlives constraints `'a: 'b` grow region values until stable; then universal regions are checked for validity
4. **Dataflow framework**: Lattice-based, per-statement transfer functions ("effects"), iterates to fixpoint; supports forward and backward analyses
5. **Drop elaboration classification**: Each drop is Static, Dead, Conditional, or Open; Open drops recursively categorize fields
6. **Move path tree**: Field-granularity initialization tracking; illegal moves excluded; indexed by `MovePathIndex` with parent/child relationships
7. **User type annotations**: Canonical annotations preserve user-specified lifetimes through MIR type-check despite region replacement
8. **Use-live vs drop-live**: Use requires entire type valid; drop only requires dropck-relevant regions valid (those needed by `Drop` impls)
9. **`#[may_dangle]`**: Marks generic parameters on `Drop` impls as not accessed during drop, exempting them from liveness requirements
10. **Placeholder leak check**: For HRTB subtyping, placeholder regions must not escape to outer regions or pre-existing regions -- checked via "taint sets"
11. **Universe hierarchy**: Tree of name scopes tracked as a counter; existential variables can only reference names visible from their universe
12. **Member constraint resolution**: Find minimal choice after filtering by lower bounds (must outlive) and upper bounds (must be outlived by)
13. **`PhantomData` inconsistency**: `dropck_outlives` considers `PhantomData<U>` to own `U`, but `Ty::needs_drop` does not -- this is a known inconsistency

# Construction / Recognition

## Move path example:
```rust,ignore
fn foo() {
    let a: (Vec<u32>, Vec<u32>) = (vec![22], vec![44]);
    // Move paths exist for: a, a.0, a.1
    let b = a.0;   // moves a.0; a.0 is now uninitialized
    let c = a.0;   // ERROR: a.0 not initialized
    let d = a.1;   // OK: a.1 still initialized
}
```

## Drop elaboration:
```rust,ignore
let mut y = vec![];
{
    let x = vec![1, 2, 3];
    if std::process::id() % 2 == 0 {
        y = x; // conditionally move x
    }
} // x goes out of scope -- should it be dropped? Needs drop flag.
```

## Placeholder subtyping check:
```text
fn(&'static u32) <: for<'a> fn(&'a u32)
// Replace 'a with placeholder '!1:
fn(&'static u32) <: fn(&'!1 u32)
// Contravariance of fn args:
&'!1 u32 <: &'static u32
// Requires '!1: 'static -- but !1 is unknown, might not outlive 'static
// Region inference: V1 grows to include end('static)
// Universal region check: V1 grew too large -> ERROR
```

## User type annotations:
```rust,ignore
fn foo<'a>(x: &'a u32) {
    let y: &'static u32 = x;
    // Without user type annotations, replacing regions would lose
    // the 'static requirement. The annotation is preserved as
    // CanonicalUserTypeAnnotation to enforce the constraint.
}
```

# Context & Application

- The borrow checker is the foundation of Rust's memory safety guarantees without garbage collection
- NLL (non-lexical lifetimes) was a major improvement enabled by operating on MIR rather than HIR -- regions are derived from control flow, not lexical scope
- Drop elaboration runs *after* borrow checking, meaning borrowck must conservatively handle all possible drop scenarios
- The dataflow framework is reused across the compiler for many analyses beyond borrow checking (e.g., generator yield points, const evaluation checks)
- Polonius is an experimental alternative borrow checker formulation based on Datalog that handles some cases better than NLL
- The universe system is elegant in its simplicity -- a single counter suffices because the type checker's structure prevents sibling universe communication

# Examples

**Example 1**: Borrow checker phases for a simple function. Given `fn foo<'a>(x: &'a u32)`:
1. Replace `'a` with fresh inference variable, creating universal region for `'a`
2. Dataflow computes initialized/moved places
3. MIR type-check generates constraints like `'a: '0` from subtyping
4. Region inference computes `'0 = {liveness points}`, `'a = {liveness points, end('a)}`
5. Check borrows: verify no conflicting accesses

**Example 2**: Universe preventing illegal lifetimes:
```text
exists<X> {           // X is in U0
  forall<Y> { ... }   // Y is in U1
  forall<Z> { ... }   // Z is in U2
}
// X cannot reference Y or Z because U0 < U1 and U0 < U2
// Y and Z can only interact through X, which can't name either
```

**Example 3**: Member constraints for opaque types. For `fn make(a: &'a u32, b: &'b u32) -> impl Trait<'a, 'b>` returning `(a, b)`, the hidden type has regions `'0` and `'1` with constraints `'0 member of ['a, 'b, 'static]` and `'a: '0`. Upper bounds (`'a` is an upper bound for `'0`) narrow choices from `['a, 'b, 'static]` to `['a]`.

**Example 4**: Drop check with `#[may_dangle]`. `PhantomData<T>` is considered to own `T` by `dropck_outlives`, requiring `T`'s regions to be live at drop. But `ManuallyDrop<T>` does *not* own `T`, so `T`'s regions need not be live.

# Relationships

## Builds Upon
- **compiler-types-and-generics** -- region kinds, `ParamEnv`, generic parameter representation are essential to borrow checking
- **compiler-trait-solving** -- well-formedness obligations and trait bounds are checked during MIR type-check
- **compiler-type-checking** -- MIR type-check uses `InferCtxt` and region constraint infrastructure from type checking

## Enables
- Code generation: after borrow checking, the compiler knows all borrows are safe and can generate code without runtime checks
- Drop elaboration: uses borrow check results to generate precise drop code

## Related
- **compiler-diagnostics** -- borrow check errors are reported through the diagnostic infrastructure as fixed (non-lint) errors

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming drop elaboration happens before borrow checking.
  **Correction**: Drop elaboration runs *after* borrowck. This means borrowck must conservatively handle partially moved values and cannot rely on precise drop information.

- **Error**: Confusing `Ty::needs_drop` with `dropck_outlives` for liveness requirements.
  **Correction**: They differ for `PhantomData<U>` (dropck considers it to own `U`, needs_drop does not) and zero-length arrays. "Liveness requirements can change depending on whether a type is contained in a larger local. This is inconsistent, and should be fixed."

- **Error**: Expecting placeholder regions from different `for<'a>` bindings to interact.
  **Correction**: Sibling universes cannot communicate. Variables can only reference names from their own universe and ancestors, not siblings.

# Common Confusions

- **Confusion**: NLL means "no lifetimes."
  **Clarification**: NLL means "non-lexical lifetimes" -- regions are derived from the control-flow graph rather than lexical scope. Lifetimes still exist; they are just more precise.

- **Confusion**: Region variables are solved the same way as type variables.
  **Clarification**: "Rather than eagerly unifying things, we simply collect constraints as we go." Region constraints are solved only at the end of type checking, using fixpoint iteration over outlives constraints.

- **Confusion**: Universe indices form a flat namespace.
  **Clarification**: Universes form a tree, but are tracked as a simple counter. This works because "the structure of our type checker" prevents sibling universes from needing to communicate.

- **Confusion**: Drop flags are inserted for every local variable.
  **Clarification**: Drop flags are only needed for Conditional and Open drops. Static drops (always initialized) and Dead drops (always uninitialized) don't need flags. Further optimizations reduce the number of flags needed.

- **Confusion**: `use-live` and `drop-live` have the same requirements.
  **Clarification**: Use-live requires the entire type to be valid (all regions live). Drop-live only requires regions needed by dropck (those accessed by `Drop` impls), which can be strictly fewer thanks to `#[may_dangle]`.

# Source Reference

Chapter 21: Borrow Checker (2800 lines). Covers: dataflow analysis (Analysis trait, transfer functions, effects, convergence, ResultsCursor/ResultsVisitor, graphviz debugging); drop elaboration (dynamic drops, drop obligations, drop flags, Static/Dead/Conditional/Open classification, drop glue, cleanup paths, const-eval interaction); MIR borrow check (major phases, properties enforced, advantages of MIR); tracking moves and initialization (move paths, MovePathIndex, illegal move paths, projections, cross-references); MIR type-check (user type annotations, CanonicalUserTypeAnnotations, UserTypeProjection); drop check (dropck_outlives, use-live vs drop-live, partial drops, #[may_dangle]); region inference (universal regions, region variables as element sets, constraints, inference overview, constraint propagation); member constraints (for opaque types, lower/upper bounds, minimal choice); placeholders and universes (subtyping with placeholders, universe tree, counter representation, placeholder leak check, outlives constraints with placeholders).

# Verification Notes

- Definition source: All key concepts drawn directly from source text with detailed examples
- Key Properties: All 13 items directly supported by explicit source content
- Confidence rationale: HIGH -- comprehensive authoritative documentation of Rust's most distinctive compiler feature
- Uncertainties: Polonius (experimental alternative) mentioned but not fully covered; some sections marked TODO in source; `PhantomData`/zero-length array inconsistencies are known open issues
- Cross-reference status: Related slugs reference other cards in this extraction set
