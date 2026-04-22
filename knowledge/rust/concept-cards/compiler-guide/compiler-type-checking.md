---
# === CORE IDENTIFICATION ===
concept: Compiler Type Checking
slug: compiler-type-checking

# === CLASSIFICATION ===
category: compiler-internals
subcategory: type-system
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Type Checking"
chapter_number: 20
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "type inference"
  - "inference variables"
  - "InferCtxt"
  - "inference context"
  - "type collection"
  - "hir_analysis"
  - "hir_typeck"
  - "FnCtxt"
  - "ObligationCtxt"
  - "region constraints"
  - "coercions"
  - "LUB coercion"
  - "subtyping obligations"
  - "Hindley-Milner"
  - "unification"
  - "snapshots"
  - "variance"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiler-types-and-generics
  - compiler-trait-solving
extends: []
related:
  - compiler-diagnostics
  - compiler-borrow-checker
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type collection and how does it convert HIR types to internal types?"
  - "How does type inference work in rustc (Hindley-Milner extension)?"
  - "What are inference variables and what kinds exist (type, integral, float, region, const)?"
  - "How does the InferCtxt work and how is it created?"
  - "How do equality and subtyping constraints work?"
  - "What are snapshots and how do they enable backtracking?"
  - "How are region constraints collected and solved?"
  - "What are coercions and what is the difference between one-to-one and LUB coercions?"
  - "How does variance inference work for type and lifetime parameters?"
  - "What is coherence checking and how are overlapping impls detected?"
  - "How does HIR type checking differ from MIR type checking?"
  - "What is the relationship between type checking and trait solving?"
---

# Quick Definition

Type checking in rustc is spread across multiple phases and intermediate representations. **Type collection** converts HIR types (`rustc_hir::Ty`) into the compiler's internal representation (`ty::Ty`), focusing on function signatures and item definitions without examining function bodies. **Type inference**, based on extended Hindley-Milner, uses an inference context (`InferCtxt`) containing five kinds of inference variables (general type, integral, float, region, const) that get progressively constrained through equality and subtyping operations. Region constraints are collected during type checking but solved only at the very end. **Coercions** handle implicit type conversions at one-to-one sites (known target type) and LUB sites (computing a common type from multiple sources). Variance of type parameters is inferred from definitions using a fixed-point algorithm.

# Core Definition

Type checking is performed across two main crates: **`hir_analysis`** (type collection and signature-level checking) and **`hir_typeck`** (function body checking). These crates "draw heavily on the type inference and trait solving" subsystems.

## Type Collection

Type collection "is the process of converting the types found in the HIR (`hir::Ty`), which represent the syntactic things that the user wrote, into the internal representation used by the compiler (`Ty<'tcx>`)." It is "concerned with interprocedural things -- for example, for a function definition, collection will figure out the type and signature of the function, but it will not visit the body of the function in any way, nor examine type annotations on local variables (that's the job of type checking)."

## Type Inference

"Type inference is the process of automatic detection of the type of an expression." It extends Hindley-Milner with subtyping, region inference, and higher-ranked types.

The **InferCtxt** is created via `tcx.infer_ctxt().build()` and houses five kinds of **inference variables**: (1) general type variables that can unify with any type, (2) integral type variables from integer literals like `22`, (3) float type variables from float literals like `22.0`, (4) region variables for lifetimes, and (5) const variables. "We use the notation `?T` to refer to inference variables."

**Equality** (`infcx.at(..).eq(t, u)`) forces two types to be the same. It returns `InferOk<()>` -- the "primary" result is `()` (executed for side-effects), but `InferOk` carries extra trait obligations that must be fulfilled. **Subtyping** (`infcx.at(..).sub(..)`) works similarly. **Trying** equality with `infcx.can_eq` tests possibility without committing side-effects, but "the success or failure of these methods is always modulo regions."

**Snapshots** enable backtracking: `snapshot()` records changes, then `rollback_to` undoes them or `confirm` makes them permanent. Higher-level patterns like `commit_if_ok` and `probe` encapsulate common usage.

**Subtyping obligations**: When `?T <: &'a i32`, rustc generalizes to `?T = &'?b i32` and adds the region constraint `'?b: 'a`. For unbound variables `?T <: ?U`, an obligation `Subtype(?T, ?U)` is enqueued for later resolution.

## Region Constraints

"Rather than eagerly unifying things, we simply collect constraints as we go." Constraints take the form `'a: 'b` (outlives/subregion). One exception: region equality `'a = 'b` is recorded in a unification table for termination. Region constraints are "only solved at the very end of typechecking, once all other constraints are known and all other obligations have been proven."

**Lexical resolution** (`resolve_regions_and_report_errors`) assigns empty values to region variables and iteratively grows them using outlives constraints until a fixed-point. **NLL resolution** uses `take_and_reset_region_constraints` to extract constraints with location information for the MIR-based borrow checker.

## Coercions

Coercions are "implicit operations which transform a value into a different type." Two kinds:
- **One-to-one**: Coerce from one type to a known target (e.g., `&mut u32` to `&u32`), performed via `FnCtxt::coerce`
- **LUB (Least-Upper-Bound)**: Coerce a set of source types to an unknown target (e.g., both `&mut i32` and `&i32` coerce to `&i32`), producing the target type

## Variance

Variance is inferred for data types (structs/enums) using a fixed-point algorithm from the PLDI'11 paper. It determines whether `T<A>` is a subtype of `T<B>` based on the relationship of `A` and `B`. The algorithm iterates constraints of the form `V(X) <= Term` over a lattice where `*` (bivariant) is top and `o` (invariant) is bottom.

## Coherence

Coherence detects overlapping trait and inherent impls. Overlap checking compares all pairs using two negative checks: explicit (requires actual `!Error` impls) and implicit (proves no impl can possibly exist). The orphan check ensures no unknown external impls could exist.

# Prerequisites

- **compiler-types-and-generics** -- understanding of `ty::Ty`, `TyKind`, `ParamEnv`, and generic parameter representation
- **compiler-trait-solving** -- type checking generates obligations resolved by trait solving

# Key Properties

1. **Type collection is interprocedural**: Processes signatures and item types but never visits function bodies
2. **Five inference variable kinds**: General type, integral, float, region, and const -- each with specific unification rules
3. **HM extension**: Extends standard Hindley-Milner with subtyping, region inference, and higher-ranked types
4. **Side-effect based**: Equality/subtyping operations are executed for side-effects (constraining variables), returning `InferOk<()>` with trait obligations
5. **Region constraints deferred**: Region constraints are collected but not solved until after all other type checking is complete
6. **Two-phase region solving**: Lexical (old, grows regions until fixed-point) and NLL (extracts constraints with locations for borrow checker)
7. **Snapshots enable backtracking**: Record changes, then rollback or confirm; nested following stack discipline; used in `probe` and `commit_if_ok`
8. **Subtyping generalization**: `?T <: &'a i32` generalizes to `?T = &'?b i32` with constraint `'?b: 'a`, introducing a fresh region variable
9. **One-to-one vs LUB coercions**: One-to-one has a known target; LUB computes the least coerced type from multiple sources
10. **Variance from definitions only**: "We only infer variance for type parameters found on data types like structs and enums" -- never from code usage
11. **Variance lattice**: `*` (bivariant, top) >= `+`/`-` >= `o` (invariant, bottom); transform rule: `V3 = V1.xform(V2)`
12. **Coherence = overlap + orphan**: Overlap uses explicit and implicit negative reasoning; orphan prevents unknown external impls
13. **`crate_variances` query**: Whole-crate variance inference uses red-green algorithm -- `variances_of` for individual items depends on `crate_variances` but is usually green after re-evaluation

# Construction / Recognition

## Creating an inference context:
```rust,ignore
let infcx = tcx.infer_ctxt().build();
// infcx has type InferCtxt<'tcx>
```

## Enforcing type equality:
```rust,ignore
// Force two types to be equal
let result = infcx.at(cause, param_env).eq(expected_ty, actual_ty);
match result {
    Ok(InferOk { obligations, .. }) => {
        // Must fulfill these trait obligations
        fulfill_cx.register_predicate_obligations(infcx, obligations);
    }
    Err(err) => {
        // Type error occurred
    }
}
```

## Using snapshots for backtracking:
```rust,ignore
// Test if unification is possible without committing
let can_unify = infcx.probe(|_| {
    infcx.at(cause, param_env).eq(ty1, ty2).is_ok()
});
```

## Coercion examples:
```rust,ignore
// One-to-one: known target type
let one_to_one_coercion: &u32 = &mut 8;  // &mut u32 -> &u32

// LUB: compute common type from multiple sources
let lub_coercion = match my_bool {
    true => &mut 10,   // &mut i32
    false => &12,      // &i32
};
// Result type: &i32 (least upper bound)
```

# Context & Application

- Type checking is the core validation phase where Rust's safety guarantees are established
- The inference context is the central workspace for all type-level reasoning during function body checking
- Region constraints being deferred is crucial -- it allows the borrow checker to use MIR-based (non-lexical) lifetime analysis
- The HM extension to handle subtyping means Rust's type inference is strictly more powerful than standard HM
- Variance inference affects how generic types interact with subtyping -- it's computed per-crate and cached via the query system
- Coherence checking happens during crate compilation and is essential for the safety of the impl resolution mechanism

# Examples

**Example 1**: Type inference in action:
```rust
fn main() {
    let mut things = vec![];     // things: Vec<?T> initially
    things.push("thing");        // constrains ?T = &str
}
// things is inferred to be Vec<&str>
```

**Example 2**: Subtyping with region generalization. Given `?T <: &'a i32`:
1. Generalize `&'a i32` to `&'?b i32` with fresh region variable `'?b`
2. Unify `?T = &'?b i32`
3. Add region constraint `'?b: 'a`

**Example 3**: Variance inference. For three types:
```rust,ignore
enum Option<A> { Some(A), None }        // V(A) = + (covariant)
enum OptionalFn<B> { Some(fn(B)), None } // V(B) = - (contravariant)
enum OptionalMap<C> { Some(fn(C) -> C), None } // V(C) = o (invariant)
```
Constraints: `V(A) <= +`, `V(B) <= -`, `V(C) <= +` AND `V(C) <= -`. Solution: `V(A)=+`, `V(B)=-`, `V(C)=o`.

**Example 4**: Coherence implicit negative check. Given `impl From<MyLocalType> for Box<dyn Error>` in your crate and `impl<E: Error> From<E> for Box<dyn Error>` in std, the check determines that `MyLocalType: Error` cannot hold (no impl exists, downstream crates can't implement a remote trait for a remote type), so the impls don't overlap.

# Relationships

## Builds Upon
- **compiler-types-and-generics** -- all type checking operates on `ty::Ty`, uses `ParamEnv`, and manipulates generic parameters
- **compiler-trait-solving** -- type checking generates trait obligations that must be resolved by the trait solver

## Enables
- **compiler-borrow-checker** -- region constraints from type checking feed into borrow checking; MIR type-check produces the constraints that NLL region inference solves
- **compiler-diagnostics** -- type errors are reported through the diagnostic infrastructure

## Related
- **compiler-diagnostics** -- type checking errors use the diagnostic system for user-facing messages
- **compiler-borrow-checker** -- the NLL borrow checker performs its own MIR-based type check to generate region constraints

## Contrasts With
- None within this source

# Common Errors

- **Error**: Checking if types are equal using `==` on inference variables.
  **Correction**: Use `infcx.can_eq(param_env, ty1, ty2)` which properly handles inference variables and returns results modulo regions.

- **Error**: Ignoring the trait obligations returned by `eq`/`sub` operations.
  **Correction**: Always enroll returned `InferOk` obligations in a fulfillment context. Ignoring them can lead to unsound acceptance of programs.

- **Error**: Attempting to solve region constraints before type checking is complete.
  **Correction**: Region constraints must be solved only after all other type checking is done. Calling `resolve_regions_and_report_errors` too early will cause an ICE.

# Common Confusions

- **Confusion**: Type collection examines function bodies.
  **Clarification**: Type collection "will figure out the type and signature of the function, but it will not visit the body of the function in any way, nor examine type annotations on local variables."

- **Confusion**: Region constraints are solved eagerly like type constraints.
  **Clarification**: "Rather than eagerly unifying things, we simply collect constraints as we go, but make (almost) no attempt to solve regions." They are deferred to the very end.

- **Confusion**: `can_eq` returning `Ok` means the types are definitely equal.
  **Clarification**: "The success or failure of these methods is always modulo regions. That is, two types `&'a u32` and `&'b u32` will return `Ok` for `can_eq`, even if `'a != 'b`."

- **Confusion**: Variance is inferred from how types are used in code.
  **Clarification**: "This inference is explicitly designed not to consider the uses of types within code. To determine the variance of type parameters defined on type `X`, we only consider the definition of the type `X` and the definitions of any types it references."

- **Confusion**: Traits with associated types can have non-invariant parameters.
  **Clarification**: "Traits with associated types -- or at minimum projection expressions -- must be invariant with respect to all of their inputs" because projection relationships become unpredictable when the trait parameters vary.

# Source Reference

Chapter 20: Type Checking (2719 lines). Covers: variance of type and lifetime parameters (algorithm from PLDI'11, constraints, lattice, dependency graph, historical note on trait variance); coherence (overlap checks with explicit/implicit negative reasoning, orphan check); HIR type checking (type collection, hir_analysis and hir_typeck crates); coercions (one-to-one and LUB, FnCtxt::coerce); type inference (HM extension, InferCtxt creation, five kinds of inference variables, equality/subtyping, snapshots/backtracking, subtyping obligations, region constraints, lexical vs NLL region solving).

# Verification Notes

- Definition source: All key concepts drawn directly from source text
- Key Properties: All 13 items directly supported by explicit source content
- Confidence rationale: HIGH -- authoritative compiler team documentation covering core type checking infrastructure
- Uncertainties: Some sections are noted as TODO or incomplete in the source; lexical region resolution is being phased out in favor of NLL
- Cross-reference status: Related slugs reference other cards in this extraction set
