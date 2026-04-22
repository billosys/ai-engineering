---
# === CORE IDENTIFICATION ===
concept: Compiler THIR and MIR
slug: compiler-mir

# === CLASSIFICATION ===
category: compiler-internals
subcategory: intermediate-representations
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "THIR and MIR"
chapter_number: 15
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Typed High-Level Intermediate Representation"
  - "THIR"
  - "Mid-level Intermediate Representation"
  - "MIR"
  - "HAIR"
  - "basic blocks"
  - "MIR construction"
  - "MIR visitor"
  - "MIR passes"
  - "MIR stealing"
  - "control-flow graph"
  - "inline assembly in MIR"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiler-hir
extends: []
related:
  - compiler-syntax-and-ast
  - rustdoc-internals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the THIR and how does it differ from the HIR?"
  - "What is MIR and what are its key characteristics?"
  - "What are basic blocks, statements, terminators, locals, places, rvalues, and operands in MIR?"
  - "How does MIR construction (lowering from THIR) work?"
  - "How are expressions lowered to Place, Rvalue, Operand, or temporary forms?"
  - "How does the MIR query pipeline work (mir_built, mir_const, mir_promoted, optimized_mir)?"
  - "What is the stealing mechanism in intermediate MIR queries?"
  - "How do MIR visitors work and when would you use them?"
  - "How are constants represented in MIR (ConstValue vs ValTree)?"
  - "How does inline assembly flow through THIR and MIR?"
  - "What is the unpack! macro and why is it needed for MIR construction?"
---

# Quick Definition

The THIR (Typed High-Level Intermediate Representation) and MIR (Mid-level Intermediate Representation) are two successive IRs in the Rust compiler pipeline. THIR is generated after type checking from the HIR -- it only represents executable code (bodies), makes all types explicit, and further desugars automatic references/dereferences and operator overloading. MIR, introduced by RFC 1211, is a radically simplified control-flow-graph-based IR with no nested expressions, used for borrow checking, optimization, and code generation. The pipeline flows: HIR -> THIR -> MIR, with THIR as a short-lived intermediate between type-checked HIR and the fully lowered MIR.

# Core Definition

**THIR** ("Typed HIR", formerly "HAIR") is produced after type checking and lives in `rustc_mir_build::thir`. It differs from the HIR in key ways: (1) it only represents body owners (functions, closures, const initializers) -- no structs, traits, or other items; (2) each body is stored temporarily and dropped when no longer needed (unlike HIR, which persists for the whole compilation); (3) all types are filled in; (4) automatic references, dereferences, and method calls are made explicit, and overloaded operators are converted to plain function calls; (5) destruction scopes are explicit; (6) statements, expressions, and match arms are stored in separate arrays, cross-referenced by index (`ExprId`). THIR is constructed via `thir_body` and viewed with `-Zunpretty=thir-tree`.

**MIR** is Rust's mid-level IR, defined in `compiler/rustc_middle/src/mir/` with manipulation logic in `rustc_mir_build`, `rustc_mir_transform`, and `rustc_mir_dataflow`. It is based on a **control-flow graph** (CFG), has **no nested expressions**, and all types are **fully explicit**. The main data type is `Body`, containing:

- **Basic blocks** (`BasicBlockData`): units of the CFG, stored in a vector and referenced by `BasicBlock` indices. Each block contains statements and ends with a terminator.
- **Statements**: actions with exactly one successor (e.g., `StorageLive`, assignments).
- **Terminators**: actions with potentially multiple successors (e.g., function calls with unwind paths, `SwitchInt` for conditionals). Always the last element of a block.
- **Locals** (`Local`): stack-allocated memory locations -- function arguments, local variables, temporaries. Indexed as `_0` (return place via `RETURN_PLACE`), `_1`, `_2`, etc. User variables are distinguished by `debug <Name> => <Place>` annotations.
- **Places** (`Place`): expressions identifying memory locations, like `_1` or `_1.f`. Projections (fields, dereferences) use `ProjectionElem`.
- **Rvalues** (`Rvalue`): expressions that produce values (right-hand side of assignments). Cannot be nested -- they reference only places and constants.
- **Operands** (`Operand`): arguments to rvalues, either a constant or a `copy`/`move` of a place.

**MIR construction** lowers THIR to MIR via the `mir_built` query, processing THIR expressions recursively. There are four target representations for expressions: `Place` (existing memory location), `Rvalue` (assignable to a place), `Operand` (argument to an operation), and temporary variable. Functions that may generate new basic blocks return `BlockAnd<ResultType>`, and the `unpack!` macro manages the "cursor" `block` variable that tracks the current insertion point.

**Constants** in MIR come in two forms: MIR constants (`mir::Constant`) evaluate to `mir::ConstValue` (with optimized variants for literals), and type system constants (`ty::Const`) evaluate to `ty::ValTree` (a tree of `Branch` and `Leaf` nodes with unique representation guarantees -- no unions or raw pointers allowed).

**MIR queries** form a pipeline: `mir_built` -> `mir_const` (simple transforms for const qualification) -> `mir_promoted` (extract promotable temps, prepare for borrow checking) -> `mir_drops_elaborated_and_const_checked` (borrow checking, drop elaboration) -> `optimized_mir` (all optimizations). Intermediate queries yield `&'tcx Steal<Body<'tcx>>`, allowing subsequent queries to steal the result as an optimization to avoid cloning. The stealing mechanism requires careful ordering of queries to ensure readers execute before stealers.

# Prerequisites

Understanding of the HIR (compiler-hir) and the general concept of control-flow graphs. Familiarity with the compiler query system is helpful for understanding MIR passes.

# Key Properties

1. **THIR is transient**: Each THIR body is allocated in an arena and dropped as soon as it is no longer needed, keeping peak memory in check
2. **THIR makes implicit things explicit**: Automatic references/dereferences, method call resolution, operator overloading, and destruction scopes are all made explicit in THIR
3. **MIR has no nested expressions**: All expressions are flattened into assignments between locals, places, rvalues, and operands
4. **CFG-based structure**: MIR is organized as basic blocks with statements (one successor) and terminators (potentially multiple successors)
5. **Locals are indexed**: All variables (`_0`, `_1`, ...) are anonymous indices; user variables are distinguished only by `debug` annotations in scope blocks
6. **Rvalues cannot nest**: A complex expression like `a + b + c` becomes `TMP1 = a + b; x = TMP1 + c`
7. **Four expression representations**: Place (memory location), Rvalue (produces a value), Operand (argument to an operation), and temporary (a fresh local)
8. **Pipeline of query-grouped passes**: `mir_built` -> `mir_const` -> `mir_promoted` -> `mir_drops_elaborated_and_const_checked` -> `optimized_mir`, each adding transformations
9. **Stealing mechanism**: Intermediate MIR results can be stolen by subsequent queries to avoid cloning; readers must execute before stealers
10. **Two constant forms**: MIR constants (`ConstValue` with optimized literal variants) and type system constants (`ValTree` with unique representation guarantees)
11. **Operator lowering split**: Built-in type operators become `Rvalue` primitives (codegened to LLVM intrinsics); all other operators become trait method calls

# Construction / Recognition

## THIR construction:
1. After type checking, call `thir_body` with a memory arena
2. THIR is allocated in the arena; dropping the arena frees the THIR
3. View with `rustc -Zunpretty=thir-tree`

## MIR construction from THIR:
1. `mir_built` query triggers MIR building from THIR
2. Local variables are created for function arguments and bindings
3. The body (a `Block` expression) is lowered recursively
4. Result is written to `RETURN_PLACE` (`_0`)
5. Expression lowering follows the chain: body -> `Rvalue` -> `Operand` -> `Place` -> temporary -> `Rvalue` (recursive)
6. The `unpack!` macro manages the `block` cursor through `BlockAnd` return values

## MIR query pipeline:
```text
mir_built(D) -> mir_const(D) -> mir_promoted(D) ->
mir_drops_elaborated_and_const_checked(D) -> optimized_mir(D)
```

## Implementing a MIR pass:
1. Define a unit struct: `pub struct MyPass;`
2. Implement `MirPass<'tcx>` with `run_pass(&self, tcx: TyCtxt<'tcx>, body: &mut Body<'tcx>)`
3. Register in the appropriate query's pass list

## Viewing MIR:
- Rust Playground: click the "MIR" button
- CLI: `rustc file.rs -Z mir-opt-level=0 --emit mir` (nightly, unoptimized)

# Context & Application

MIR is where Rust's defining safety checks happen -- the borrow checker operates on MIR, as do many optimization passes and code generation. Understanding MIR is essential for:

- Working on the borrow checker or adding new safety checks
- Implementing compiler optimizations (registered as `MirPass` implementations)
- Understanding how Rust code maps to machine operations (MIR is the last architecture-independent representation before codegen)
- Debugging why certain code patterns fail borrow checking
- Understanding how constants are evaluated at compile time (CTFE operates on MIR)

THIR understanding is important for:
- Exhaustiveness checking (pattern matching completeness)
- Unsafety checking
- Understanding how type information flows from type checking to MIR construction

# Examples

**Example 1** (Ch. 15, "THIR structure"): For `fn main() { let x = 1 + 2; }`, the THIR contains expressions stored in an array: literal `1` (e0), scope around it (e1), literal `2` (e2), scope around it (e3), binary add `e1 + e3` (e4), scope (e5), block (e6), and outer scopes (e7, e8). Statement s0 is a `Let` binding pattern `x` with initializer `e5`.

**Example 2** (Ch. 15, "MIR basic blocks"):
```mir
bb0: {
    StorageLive(_1);
    _1 = const <std::vec::Vec<T>>::new() -> bb2;
}
bb2: {
    StorageLive(_3);
    _3 = &mut _1;
    _2 = const <std::vec::Vec<T>>::push(move _3, const 1i32) -> [return: bb3, unwind: bb4];
}
```
`StorageLive` marks a variable as alive. Function calls are terminators (not statements) because they may unwind.

**Example 3** (Ch. 15, "No nested expressions"):
The Rust expression `x = a + b + c` becomes two MIR statements:
```mir
TMP1 = a + b
x = TMP1 + c
```

**Example 4** (Ch. 15, "MIR Pass implementation"):
```rust,ignore
pub struct CleanupPostBorrowck;

impl<'tcx> MirPass<'tcx> for CleanupPostBorrowck {
    fn run_pass(&self, tcx: TyCtxt<'tcx>, body: &mut Body<'tcx>) {
        // Walk body and remove statements not relevant to codegen
    }
}
```

**Example 5** (Ch. 15, "ValTree uniqueness"): A `[u32; 2]` array is always represented as `Branch([Leaf(first_int), Leaf(second_int)])`. Encoding both u32s into a single `u64` `Leaf` is not a legal `ValTree` construction. This uniqueness guarantee means `ValTree` decoding must always match on the type first.

# Relationships

## Builds Upon
- **compiler-hir** -- the HIR (after type checking) is the source for THIR construction; MIR is ultimately derived from HIR via THIR

## Enables
(downstream: MIR optimizations, borrow checking, code generation -- not in this extraction set)

## Related
- **compiler-syntax-and-ast** -- the AST is the starting point of the full pipeline: AST -> HIR -> THIR -> MIR

## Contrasts With
(none within this source)

# Common Errors

- **Error**: Attempting to read from a stolen MIR intermediate result (e.g., reading `mir_const` after `mir_promoted` has stolen it).
  **Correction**: Ensure all queries that need to read an intermediate result execute before the stealing query runs. The pipeline has strict ordering requirements: `mir_const_qualif` must run before `mir_promoted` steals `mir_const`.

- **Error**: Overriding `super_foo` methods on a MIR visitor instead of `visit_foo`.
  **Correction**: Never override `super_foo`. Override `visit_foo` to add custom logic, then call `self.super_foo(...)` within it to continue recursive traversal.

- **Error**: Constructing a `ValTree` that does not have a unique representation (e.g., packing multiple values into a single `Leaf`).
  **Correction**: `ValTree` requires that every value has exactly one valid representation. Arrays must be `Branch` nodes containing individual `Leaf` elements. Unions and raw pointers cannot be represented in `ValTree` at all.

# Common Confusions

- **Confusion**: THIR and MIR serve similar purposes.
  **Clarification**: THIR is a typed, still-somewhat-high-level IR used for exhaustiveness and unsafety checking before MIR construction. MIR is a radically simplified CFG with no nested expressions, used for borrow checking, optimization, and codegen. THIR is transient; MIR persists through the rest of compilation.

- **Confusion**: MIR statements and terminators are the same kind of construct.
  **Clarification**: Statements have exactly one successor (execution always continues to the next statement). Terminators have potentially multiple successors (e.g., function calls can unwind, conditionals branch). Every basic block ends with exactly one terminator.

- **Confusion**: Function calls in MIR are statements.
  **Clarification**: Function calls are always terminators because they can potentially unwind. Even calls that are known not to unwind still appear as terminators in MIR, though they list only one successor block.

- **Confusion**: The `Steal` mechanism is about thread safety.
  **Clarification**: Stealing is an optimization to avoid cloning MIR between pipeline stages. It means a result can only be consumed once. The mechanism enforces ordering: readers must run before the stealer. Attempting to read a stolen result panics.

# Source Reference

Chapter 15 of the Rust Compiler Dev Guide (1184 lines). Covers: THIR overview (purpose, transient storage, additional desugaring, arena-based allocation), MIR introduction (CFG-based, no nesting, fully explicit types), MIR vocabulary (basic blocks, statements, terminators, locals, places, rvalues, operands), MIR data types (`Body`, `BasicBlockData`, `Statement`, `Terminator`, `Local`, `Place`, `ProjectionElem`, `Rvalue`, `Operand`), representing constants (MIR constants vs type system constants, `ConstValue`, `ValTree`, promoted constants), MIR construction (`mir_built`, `unpack!`, expression lowering to Place/Rvalue/Operand/temporary, operator lowering, method call lowering, conditions and pattern matching, aggregate construction), MIR visitor (`Visitor`/`MutVisitor`, `visit_foo`/`super_foo` pattern, traversal orders), MIR queries and passes (pipeline stages, `MirPass` trait, stealing mechanism with `Steal`), and inline assembly representation across AST/HIR/THIR/MIR/codegen stages.

# Verification Notes

- Definition source: Directly extracted from Chapter 15 sections on THIR, MIR, construction, visitors, passes, and constants
- Key Properties: All derived from explicit descriptions, code examples, and diagrams in the source text
- Confidence rationale: HIGH -- official compiler team documentation; MIR is a fundamental, well-established compiler IR (introduced in RFC 1211)
- Uncertainties: Some inline assembly details may evolve; the stealing mechanism is acknowledged as "a bit dodgy" with alternatives discussed in rust-lang/rust#41710
- Cross-reference status: Depends on compiler-hir; part of the AST -> HIR -> THIR -> MIR pipeline
