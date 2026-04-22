---
# === CORE IDENTIFICATION ===
concept: Compiler Type Representation and Generics
slug: compiler-types-and-generics

# === CLASSIFICATION ===
category: compiler-internals
subcategory: type-system
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Types and Generics"
chapter_number: 18
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ty::Ty"
  - "TyKind"
  - "TyCtxt"
  - "AdtDef"
  - "GenericArgs"
  - "GenericArg"
  - "EarlyBinder"
  - "Binder"
  - "early bound parameters"
  - "late bound parameters"
  - "DebruijnIndex"
  - "TypeFoldable"
  - "TypeFolder"
  - "ParamEnv"
  - "TypingEnv"
  - "type aliases and normalization"
  - "variance inference"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiler-trait-solving
  - compiler-type-checking
  - compiler-borrow-checker
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between rustc_hir::Ty and ty::Ty?"
  - "How does rustc represent types internally using TyKind?"
  - "What are ADTs and how are they represented with AdtDef and GenericArgs?"
  - "How does EarlyBinder work for instantiating generic parameters?"
  - "What is the difference between early bound and late bound parameters?"
  - "How do Binder and higher-ranked types (for<'a>) work internally?"
  - "What is a DebruijnIndex and how are bound variables represented?"
  - "How do TypeFoldable and TypeFolder enable type transformations?"
  - "What is a ParamEnv and how are typing environments managed?"
  - "How does type normalization work (structural vs deep)?"
  - "What are aliases (type aliases, associated types, opaque types) and how are they normalized?"
  - "How does variance inference work for type and lifetime parameters?"
---

# Quick Definition

Rustc represents types internally through the interned `ty::Ty` type (distinct from the syntactic `rustc_hir::Ty`), which wraps a `TyKind` enum with variants for every kind of Rust type -- primitives, references, ADTs, function pointers, generic parameters, and more. Generic parameters are tracked by `ty::Generics` and instantiated through `EarlyBinder` (for item-level generics) and `Binder` (for higher-ranked `for<'a>` types). The system distinguishes between early bound parameters (provided when naming a function) and late bound parameters (provided when calling it). Types are transformed via the `TypeFoldable`/`TypeFolder` trait pattern. The `ParamEnv` captures in-scope where clauses, and normalization resolves type aliases to their underlying types through structural or deep normalization.

# Core Definition

**`ty::Ty` vs `rustc_hir::Ty`**: "The HIR in rustc can be thought of as the high-level intermediate representation... it represents the syntax that the user wrote." In contrast, "`ty::Ty` represents the semantics of a type, that is, the meaning of what the user wrote." For example, in `fn foo(x: u32) -> u32`, there are two `rustc_hir::Ty` nodes (one per usage of `u32`) but only one `ty::Ty` for `u32` across the entire program. The `hir_ty_lowering` module converts `rustc_hir::Ty` to `ty::Ty` via the `lower_ty` routine.

**`TyKind`**: The inner enum of `ty::Ty` with variants including: `Adt` (structs, enums, unions), `Ref` (references with region, type, mutability), `Param` (generic parameters like `T`), `Str`, `Slice`, `Array`, `RawPtr`, `Error` (type errors), and many more. Types are interned via `TyCtxt` and compared cheaply with `==`, though semantic comparison during inference requires `infcx.can_eq()`.

**ADTs and GenericArgs**: A type like `MyStruct<u32>` is represented as `TyKind::Adt(AdtDef, GenericArgs)` where `AdtDef` references the struct definition (without type parameters) and `GenericArgs` is a thin pointer to `&[GenericArg]` containing the substituted arguments. This separation is efficient because "we can instantiate `MyStruct<A>` as `MyStruct<B>` very cheaply, by just replacing the one reference." `GenericArg` stores type/lifetime/const arguments compactly with the discriminant in the lower 2 bits.

**EarlyBinder**: "Given an item that introduces generic parameters, when accessing types inside the item from outside, the generic parameters must be instantiated." `EarlyBinder<T>` wraps a type `T` and requires calling `instantiate(args)` to discharge the binder, replacing generic parameters with concrete arguments. When already inside the binder, `instantiate_identity` is used instead.

**Binder and DebruijnIndex**: Higher-ranked types like `for<'a> fn(&'a u32)` use `Binder` to track which parameters are introduced. Bound variables use `DebruijnIndex` (counting binder depth from innermost) plus `BoundVar` (position in that binder's parameter list). Written as `^DebruijnIndex_BoundVar` in debug output (e.g. `^0_0` for the first variable of the innermost binder).

**Early vs Late Bound**: "Early bound parameters are provided in the earliest step (naming the function), whereas late bound parameters are provided in the latest step (calling the function)." Late bound lifetime parameters appear on the `Fn` impl rather than the function item type, enabling higher-ranked function pointers. A parameter must be early bound if: it's a type/const parameter, it's used in a where clause, or it's not constrained by argument types.

**TypeFoldable/TypeFolder**: The visitor/transformer pattern for types. `TypeFoldable` is implemented by types containing type information; `TypeFolder` defines the transformation. The `subst` operation is implemented as a `TypeFolder` that replaces `TyKind::Param` with values from a substitution list.

**ParamEnv**: "The `ParamEnv` is a list of in-scope where-clauses." It includes elaborated supertraits and (in the old solver) normalized aliases. Created via `tcx.param_env(def_id)` for an item's where clauses. "Using the wrong `ParamEnv` when interacting with the type system can lead to ICEs, ill-formed programs compiling, or erroring when we shouldn't."

**Normalization**: The process of replacing alias types with their underlying types. Structural normalization resolves only the outermost alias; deep normalization resolves all aliases recursively. Entry points include `infcx.at.structurally_normalize`, `infcx.at.deeply_normalize`, and `tcx.normalize_erasing_regions`. The old solver requires all types normalized eagerly; the new solver expects aliases may be unnormalized and normalizes on demand.

**Variance**: Inferred for type parameters on data types (structs/enums) using a fixed-point algorithm. Notation: `+` covariant, `-` contravariant, `*` bivariant, `o` invariant. "We only infer variance for type parameters found on data types. We do not infer variance for type parameters found on traits, functions, or impls."

# Prerequisites

- General understanding of the rustc compilation pipeline (AST, HIR, MIR)
- Familiarity with Rust's type system from a user perspective (generics, lifetimes, traits)

# Key Properties

1. **Interned types**: `ty::Ty` is a thin pointer via `Interned<WithCachedTypeInfo<TyKind>>`, enabling cheap equality comparisons and deduplication
2. **Semantic vs syntactic**: `rustc_hir::Ty` represents what the user wrote (syntax); `ty::Ty` represents what it means (semantics), with lifetimes filled in and aliases resolved
3. **TyKind::Error invariant**: "The compiler should never produce `Error` unless we know that an error has already been reported to the user"; it requires an `ErrorGuaranteed` to construct
4. **Nominal types**: ADTs use `(AdtDef, GenericArgs)` representation reflecting Rust's nominal type system -- types are defined by name, not structure
5. **GenericArg packing**: Type/lifetime/const discriminant stored in lower 2 bits of the interned pointer for space efficiency; use `unpack()` to get `GenericArgKind`
6. **Nested generic args**: For `MyStruct::<u32>::func::<bool, char>`, the GenericArgs list is flattened outermost-to-innermost: `[u32, bool, char]`
7. **Early vs late bound**: Late bound lifetimes enable higher-ranked function pointers (`for<'a> fn(&'a u32)`); early bound parameters are on the function item type itself
8. **DebruijnIndex**: Bound variables use de Bruijn indices counting from the innermost binder (0 = innermost), enabling correct handling of nested binders
9. **Placeholders vs bound vars**: `RePlaceholder` has stable representation regardless of binder nesting depth; `ReBound` changes representation based on intervening binders
10. **ParamEnv elaboration**: Where clauses are elaborated with supertraits (e.g., `T: Copy` implies `T: Clone`) and deduplicated during `ParamEnv` construction
11. **Alias kinds**: Rigid (cannot normalize further), ambiguous (may be normalizable once inference resolves), and unnormalized (can be normalized now)
12. **Old vs new solver normalization**: Old solver requires eager normalization everywhere; new solver expects potentially unnormalized aliases and normalizes lazily
13. **Variance lattice**: `*` (bivariant) at top, `o` (invariant) at bottom, with `+` and `-` in between; variance is computed via fixed-point iteration over type definitions

# Construction / Recognition

## Creating and inspecting types:
```rust,ignore
// Allocating a new type
let array_ty = Ty::new_array_with_const_len(tcx, ty, count);
// Common types
let bool_ty = tcx.types.bool;

// Matching on type kind
fn process_ty(ty: Ty<'tcx>) {
    match ty.kind() {
        ty::Adt(adt_def, args) => { /* struct/enum/union */ }
        ty::Ref(region, inner_ty, mutability) => { /* &T or &mut T */ }
        ty::Param(param_ty) => { /* generic parameter T */ }
        _ => {}
    }
}
```

## EarlyBinder instantiation:
```rust,ignore
// From outside an item: instantiate generic parameters
fn foo<T, U>(a: T, _b: U) -> T { a }
// Return type of foo is EarlyBinder(T/#0)
// Calling foo::<i32, u128> instantiates with [i32, u128] -> i32

// From inside an item: use identity instantiation
let self_ty = tcx.type_of(impl_def_id).instantiate_identity();
```

## Working with GenericArgs:
```rust,ignore
fn handle_generic_arg<'tcx>(arg: GenericArg<'tcx>) {
    match arg.unpack() {
        GenericArgKind::Type(ty) => { /* type argument */ }
        GenericArgKind::Lifetime(lt) => { /* lifetime argument */ }
        GenericArgKind::Const(ct) => { /* const argument */ }
    }
}
```

# Context & Application

- Understanding `ty::Ty` is essential for any compiler work involving types -- it is "the central data structure in the compiler"
- The distinction between syntactic HIR types and semantic `ty::Ty` types is fundamental: "We assume two things are distinct until they are proven to be the same thing"
- The early/late bound distinction explains why some lifetime parameters can't be turbofished: late bound parameters are instantiated at call time, not when naming the function
- `ParamEnv` correctness is critical -- using the wrong one has caused multiple ICEs and soundness bugs in the compiler
- The transition from old to new trait solver is changing normalization strategy: from "normalize eagerly everywhere" to "normalize lazily on demand"
- Variance inference only examines type definitions, never code usage, and uses a fixed-point algorithm from the PLDI'11 paper by Altidor et al.

# Examples

**Example 1**: Type representation. Given `fn foo<'a, T>(_: &'a Vec<T>)`, the type `&'a Vec<T>` is represented internally as:
```
TyKind::Ref(
  RegionKind::LateParam(DefId(foo), DefId(foo::'a), "'a"),
  TyKind::Adt(Vec, &[TyKind::Param("T", 0)])
)
```

**Example 2**: Early vs late bound. Given `fn bar<'a>(b: &'a String) -> &'a String`, lifetime `'a` is late bound, so `bar` can be coerced to `for<'a> fn(&'a String) -> &'a String`. But if we add `'a: 'a` bound, `'a` becomes early bound and coercion fails.

**Example 3**: Normalization example. Given `type Foo<T: Iterator> = Bar<T>; type Bar<T: Iterator> = <T as Iterator>::Item`, normalizing `Foo<?x>` cascades: `Foo<?x>` -> `Bar<?x>` -> `<?x as Iterator>::Item` -> `?y` (new inference variable, since the alias is ambiguous).

**Example 4**: Variance. For `enum Option<A> { Some(A), None }`, variance of `A` is `+` (covariant) because `A` only appears in a covariant position. For `enum OptionalFn<B> { Some(fn(B)), None }`, `B` is `-` (contravariant).

# Relationships

## Builds Upon
- The HIR representation (provides the syntactic types that get lowered to `ty::Ty`)
- The query system (type information is computed via queries like `type_of`, `generics_of`, `predicates_of`)

## Enables
- **compiler-trait-solving** -- trait resolution operates on `ty::Ty` types and uses `ParamEnv` for where clauses
- **compiler-type-checking** -- type inference and checking work with `ty::Ty`, inference variables, and `InferCtxt`
- **compiler-borrow-checker** -- MIR borrow checking uses region information from `ty::Ty`

## Related
- **compiler-trait-solving** -- trait solving and normalization are deeply intertwined with type representation
- **compiler-type-checking** -- type checking produces and consumes `ty::Ty` values
- **compiler-borrow-checker** -- regions in `ty::Ty` (EarlyParam, LateParam, Bound, Placeholder) are central to borrow checking

## Contrasts With
- None within this source

# Common Errors

- **Error**: Comparing types with `==` during type inference, which fails to account for inference variables.
  **Correction**: Use `infcx.can_eq(param_env, ty1, ty2)` to check if types can be made equal, which handles inference variables correctly.

- **Error**: Accessing a type inside an `EarlyBinder` without instantiating it first.
  **Correction**: Call `instantiate(args)` with appropriate generic arguments, or `instantiate_identity()` if already inside the binder's scope.

- **Error**: Using the wrong `ParamEnv` for type system operations.
  **Correction**: Use the `ParamEnv` of the item being analyzed. Check for existing environments in `FnCtxt::param_env`, `LateContext::param_env`, etc. before constructing a new one.

- **Error**: Forgetting to normalize types before comparing them.
  **Correction**: Two types may be the same but one is behind an associated type. Use `normalize` (old solver) or `structurally_normalize` (new solver) before comparison.

# Common Confusions

- **Confusion**: `TyKind` refers to the functional programming concept of "kinds" (types of types).
  **Clarification**: "`TyKind` is NOT the functional programming concept of Kind." It is simply an enum of the different varieties of types in Rust.

- **Confusion**: Early and late bound parameters differ only in when their arguments are provided.
  **Clarification**: The distinction has deep consequences: late bound parameters enable higher-ranked types, affect function pointer coercions, and determine whether lifetimes can be turbofished. Only lifetime parameters can be late bound.

- **Confusion**: `ReBound` and `RePlaceholder` serve the same purpose since they carry similar data.
  **Clarification**: `ReBound` is a syntactic representation where the same parameter has different representations depending on intervening binders (via DebruijnIndex). `RePlaceholder` is a semantic representation with stable identity regardless of context, making substitution and unification simpler.

- **Confusion**: Structural and deep normalization always produce the same result.
  **Clarification**: Structural normalization only resolves the outermost alias. For `Vec<<u8 as Identity>::Assoc>`, structural normalization is a no-op (the outer type is already `Vec`), while deep normalization produces `Vec<u8>`.

- **Confusion**: The old and new trait solvers handle normalization the same way.
  **Clarification**: The old solver requires all types normalized eagerly and treats unnormalized aliases as rigid. The new solver expects potentially unnormalized aliases and normalizes lazily, using `PredicateKind::AliasRelate` for equality of aliases.

# Source Reference

Chapter 18: Types and Generics (2416 lines). Covers: `ty::Generics` and `GenericParamDef`; `EarlyBinder` and instantiation; `Binder` and higher-ranked regions with `DebruijnIndex`; early vs late bound parameters (desugaring, differences, turbofishing, liveness); the `ty` module (`ty::Ty`, `rustc_hir::Ty` vs `ty::Ty`, `TyKind` variants, interning, type errors); ADTs and `GenericArgs`; parameter types/consts/regions; `TypeFoldable` and `TypeFolder`; aliases and normalization (rigid, ambiguous, diverging, structural vs deep, normalization entry points, old vs new solver); typing environments (`ParamEnv`, `TypingMode`, `TypingEnv`); and variance inference.

# Verification Notes

- Definition source: All key concepts drawn directly from source text with extensive code examples
- Key Properties: All 13 items directly supported by explicit source content
- Confidence rationale: HIGH -- comprehensive internal documentation covering the core type system infrastructure
- Uncertainties: The transition from old to new trait solver is ongoing; normalization behavior is actively changing
- Cross-reference status: Related slugs reference other cards in this extraction set; many internal links to other guide chapters
