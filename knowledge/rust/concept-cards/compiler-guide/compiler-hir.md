---
# === CORE IDENTIFICATION ===
concept: Compiler HIR (High-Level Intermediate Representation)
slug: compiler-hir

# === CLASSIFICATION ===
category: compiler-internals
subcategory: intermediate-representations
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "The HIR"
chapter_number: 14
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "High-Level Intermediate Representation"
  - "HIR"
  - "AST lowering"
  - "HIR lowering"
  - "HirId"
  - "DefId"
  - "LocalDefId"
  - "HIR bodies"
  - "HIR map"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiler-syntax-and-ast
extends: []
related:
  - compiler-mir
  - rustdoc-internals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the HIR and how does it differ from the AST?"
  - "What desugaring happens during AST lowering to HIR?"
  - "What are DefId, LocalDefId, HirId, and BodyId, and how do they differ?"
  - "Why does the HIR use out-of-band storage instead of a directly nested tree?"
  - "How does the HIR support incremental compilation?"
  - "What is a HIR Body and what is an 'owner'?"
  - "How do you look up HIR nodes using TyCtxt?"
  - "What invariants must AST lowering uphold?"
  - "How are ambiguous type/const positions handled during lowering?"
  - "How do you inspect the HIR with -Z unpretty=hir?"
---

# Quick Definition

The HIR (High-Level Intermediate Representation) is the primary IR used in most of rustc. It is a compiler-friendly representation of the AST created after parsing, macro expansion, and name resolution via a process called "AST lowering." The HIR resembles Rust surface syntax but with key simplifications: `for` loops are desugared to `loop` + `match`, `impl Trait` is converted to generic arguments or virtual existential type declarations, and parentheses are removed since tree structure makes order explicit. This makes HIR more amenable to analysis than the raw AST.

# Core Definition

The HIR is defined after the AST undergoes lowering in the `rustc_ast_lowering` crate. The entry point is `lower_to_hir`, which retrieves the post-expansion AST and resolver data from `TyCtxt` and builds the `hir::Crate`. Lowering is organized around HIR owners -- `lower_to_hir` first indexes the crate, then `ItemLowerer::lower_node` lowers each crate, item, associated item, and foreign item. The `LoweringContext` manages the lowering state, with implementation split across files (`item.rs`, `expr.rs`, `pat.rs`, `path.rs`).

The top-level HIR data structure is `Crate`, which stores the contents of the crate being compiled. Unlike the AST (which nests items directly), the HIR uses **out-of-band storage**: items are stored in maps, and parent nodes hold only `ItemId` references to their children. To get details about a function `bar()` inside module `foo`, you look up its `ItemId` in the items map. This design serves two purposes: (1) you can iterate all items without traversing the whole tree, and (2) it enables incremental compilation by making data access observable for dependency tracking.

The HIR uses a family of identifier types:
- **`DefId`** identifies a definition (top-level item) in any crate, composed of a `CrateNum` and `DefIndex`. More stable across compilations than `NodeId` since not every expression gets one.
- **`LocalDefId`** is a `DefId` known to come from the current crate, enabling type-system enforcement that only local definitions are passed to functions expecting them.
- **`HirId`** uniquely identifies any node in the current crate's HIR, composed of an `owner` (a `LocalDefId`) and a `local_id` unique within that owner. This two-part structure provides incremental compilation stability.
- **`BodyId`** identifies a HIR `Body` (executable code such as a function body or const initializer), currently a wrapper around `HirId`.

A **HIR Body** (`rustc_hir::Body`) represents executable code associated with an **owner** (typically an item like `fn()` or `const`, but also closure expressions). Bodies are stored separately and accessed via `TyCtxt` methods like `hir_maybe_body_owned_by` and `hir_body_owner_def_id`.

During lowering, several invariants must be upheld: (1) a `HirId` must be used if created; (2) lowering a `HirId` must happen in the scope of its owning item (using `with_hir_id_owner`); (3) a `NodeId` placed into HIR must be lowered even if its `HirId` is unused; (4) new nodes not from the AST must get fresh IDs via `next_id`.

# Prerequisites

Understanding of the AST stage (parsing, macro expansion, name resolution) as covered in compiler-syntax-and-ast. The HIR is the direct successor of the AST in the compilation pipeline.

# Key Properties

1. **Desugaring**: `for` loops become `loop` + `match`; universal `impl Trait` becomes generic arguments with flags; existential `impl Trait` becomes virtual `existential type` declarations; parentheses are removed
2. **Out-of-band storage**: Items are stored in maps with `ItemId` references, not directly nested -- enables iteration over all items and supports incremental compilation dependency tracking
3. **Four identifier types**: `DefId` (cross-crate, definitions only), `LocalDefId` (current-crate definitions), `HirId` (any node in current crate, owner + local_id), `BodyId` (executable code bodies)
4. **Incremental compilation support**: The two-part `HirId` structure (owner + local_id) is more stable than `NodeId` under code changes, and out-of-band storage makes data access observable
5. **Owner-based organization**: Each HIR Body has an owner (typically an item). Bodies are accessed via `TyCtxt`, not directly from parent nodes
6. **TyCtxt as the access interface**: Most HIR operations go through `TyCtxt` methods prefixed with `hir_` -- converting between ID types, looking up nodes, finding parents
7. **Lowering invariants**: Strict rules about `HirId` creation and usage ensure the validator in `hir_id_validator.rs` can catch inconsistencies
8. **Ambiguous type/const handling**: In positions where both types and consts are valid, paths are parsed as types and disambiguated during name resolution; inferred arguments (`_`) use `GenericArg::Infer` with a dedicated `visit_infer` method

# Construction / Recognition

## AST lowering process:
1. `lower_to_hir` retrieves the post-expansion AST and resolver data
2. The crate is indexed by `ItemLowerer`
3. Each item/associated item/foreign item is lowered via `lower_node`
4. Each owner is lowered in its own `with_hir_id_owner` scope
5. `lower_node_id` maps AST `NodeId`s to the current owner; `next_id` creates fresh nodes for desugared constructs
6. New `DefId`s should have corresponding `NodeId`s added to the AST beforehand when possible

## Viewing the HIR:
```bash
# Human-readable HIR (closer to source):
cargo rustc -- -Z unpretty=hir

# Full Debug dump of HIR data structures:
cargo rustc -- -Z unpretty=hir-tree

# Correlate NodeIds/DefIds with source code:
cargo rustc -- -Z unpretty=expanded,identified
```

## Looking up HIR nodes via TyCtxt:
- `tcx.local_def_id_to_hir_id(def_id)` -- convert `LocalDefId` to `HirId`
- `tcx.hir_node(n)` -- look up node for a `HirId`, returns `Option<Node<'hir>>`
- `tcx.hir_expect_expr(n)` -- extract expression, panicking if not an expression
- `tcx.parent_hir_node(n)` -- find parent of a node

# Context & Application

The HIR is where most of `rustc`'s analysis happens. Type checking, trait resolution, borrow checking, and many other passes operate on the HIR (or on representations derived from it like THIR and MIR). Understanding the HIR is essential for:

- Working on any compiler analysis pass
- Debugging type-checking or trait-resolution issues
- Understanding how syntactic sugar is desugared
- Contributing to incremental compilation
- Understanding the `DefId`/`HirId` system used throughout the compiler

The HIR sits at a critical juncture in the pipeline: it is the last representation that closely resembles Rust source code while being structured for compiler analysis.

# Examples

**Example 1** (Ch. 14, "Out-of-band storage"):
```rust
mod foo {
    fn bar() { }
}
```
In the HIR, module `foo` (the `Mod` struct) only has the `ItemId` `I` of `bar()`. To get the function details, you look up `I` in the items map.

**Example 2** (Ch. 14, "AST lowering -- desugaring"):
The following constructs are desugared during lowering:
- Parentheses: removed (tree structure makes order explicit)
- `for` loops: converted to `match` + `loop` + `match`
- Universal `impl Trait`: converted to generic arguments with flags
- Existential `impl Trait`: converted to a virtual `existential type` declaration

**Example 3** (Ch. 14, "Ambig/Unambig positions"):
```rust
fn func<T, const N: usize>(arg: T) {
    //                          ^ Unambig type position
    func::<T, N>(arg);
    //     ^  ^  -- Ambig position (could be type or const)
    let _: [u8; 10];
    //      ^^  ^^ Unambig const position
}
```
In ambiguous positions, single-segment paths are first resolved in the type namespace; if that fails, the value namespace is tried. Inferred arguments (`_`) in ambiguous positions lower to `GenericArg::Infer`.

**Example 4** (Ch. 14, "HIR Bodies"): A `rustc_hir::Body` represents executable code. Bodies are associated with owners:
- `fn()` items own their function body
- `const` items own their initializer expression
- Closure expressions like `|x, y| x + y` own their body

# Relationships

## Builds Upon
- **compiler-syntax-and-ast** -- the AST (after macro expansion and name resolution) is the input to HIR lowering

## Enables
- **compiler-mir** -- the HIR is used to build THIR, which is then lowered to MIR
- **rustdoc-internals** -- rustdoc crawls the HIR to build its clean AST

## Related
- **compiler-mir** -- THIR and MIR are progressively lower representations built from the HIR

## Contrasts With
(none within this source)

# Common Errors

- **Error**: Trying to use `DefId` to refer to individual expressions or fine-grained syntax nodes.
  **Correction**: `DefId` identifies definitions (top-level items) only. For fine-grained nodes like expressions, use `HirId`, which includes both an owner and a local_id.

- **Error**: Creating a `HirId` during lowering but not using it, or lowering a `HirId` outside its owning item's scope.
  **Correction**: The `hir_id_validator` enforces strict invariants. Every created `HirId` must be used, and lowering must occur within `with_hir_id_owner` for the correct owner. Use `next_id` for desugared nodes that do not correspond to AST nodes.

- **Error**: Generating new `NodeId`s during lowering instead of adding them to the AST earlier.
  **Correction**: When creating new `DefId`s, add the corresponding `NodeId`s to the AST during an earlier phase. This allows `DefCollector` to centralize `DefId` generation and makes the `DefId` findable via its `NodeId`.

# Common Confusions

- **Confusion**: The HIR is just the AST with some minor cleanup.
  **Clarification**: The HIR involves significant structural changes: desugaring of `for` loops, `impl Trait`, parentheses removal, and a fundamentally different storage model (out-of-band maps vs. nested trees). The identifier system (`HirId` vs. `NodeId`) is also completely different.

- **Confusion**: `DefId` and `HirId` are interchangeable.
  **Clarification**: `DefId` identifies definitions (items) and works across crates. `HirId` identifies any node in the current crate's HIR and is composed of an owner (`LocalDefId`) and a local ID. They serve different purposes and have different stability properties for incremental compilation.

- **Confusion**: HIR Bodies are just function bodies.
  **Clarification**: A `Body` represents any executable code, including `const`/`static` initializers, enum discriminant initializers, and closure bodies. The owner can be an item, a closure expression, or other constructs that contain executable code.

# Source Reference

Chapter 14 of the Rust Compiler Dev Guide (382 lines). Covers: HIR overview and desugaring, out-of-band storage and the `Crate` type, identifiers (`DefId`, `LocalDefId`, `HirId`, `BodyId`), HIR operations via `TyCtxt`, HIR Bodies and owners, AST lowering (entry point, invariants, `LoweringContext`, `with_hir_id_owner`), HIR debugging (`-Z unpretty=hir`/`hir-tree`), and ambiguous/unambiguous type and const positions during lowering (paths, inferred arguments, `GenericArg::Infer`).

# Verification Notes

- Definition source: Directly extracted from Chapter 14 "The HIR" and its subsections on lowering, debugging, and ambig/unambig handling
- Key Properties: All derived from explicit descriptions in the source text
- Confidence rationale: HIGH -- official compiler team documentation; HIR is a stable, well-established part of the compiler
- Uncertainties: The ambig/unambig type system (`AmbigArg`, `visit_infer`) is described as a recent addition and may evolve
- Cross-reference status: Depends on compiler-syntax-and-ast; enables compiler-mir and rustdoc-internals
