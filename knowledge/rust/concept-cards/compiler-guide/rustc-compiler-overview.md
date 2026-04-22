---
# === CORE IDENTIFICATION ===
concept: Rust Compiler Architecture Overview
slug: rustc-compiler-overview

# === CLASSIFICATION ===
category: compiler-internals
subcategory: architecture
tier: foundational

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Compiler Overview"
chapter_number: 9
pdf_page: null
section: "High-Level Architecture, Compilation Pipeline, Source Structure, Intermediate Representations, Memory Management, Serialization, Parallel Compilation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustc architecture"
  - "compiler pipeline"
  - "rustc internals"
  - "intermediate representations"
  - "TyCtxt"
  - "tcx"
  - "HIR"
  - "MIR"
  - "THIR"
  - "AST"
  - "LLVM-IR"
  - "arena allocation"
  - "interning"
  - "rustc crate structure"
  - "compiler source layout"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - rustc-compiler-query-system
  - rustc-compiler-bootstrapping
  - rustc-compiler-dev-practices
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the major phases of Rust compilation?"
  - "What intermediate representations (IRs) does rustc use and what is each for?"
  - "What is TyCtxt and why is it central to the compiler?"
  - "How is the compiler source code organized across crates?"
  - "What is the difference between AST, HIR, THIR, MIR, and LLVM-IR?"
  - "How does rustc manage memory with arenas and interning?"
  - "What is monomorphization and when does it happen?"
  - "How does parallel compilation work in rustc?"
  - "What is the 'tcx lifetime and what does it represent?"
  - "How does serialization work for crate metadata and incremental compilation?"
  - "What design constraints shape the compiler's architecture?"
  - "How does the compiler crate dependency graph work?"
---

# Quick Definition

The Rust compiler (`rustc`) transforms source code through a pipeline of intermediate representations: source text -> tokens -> AST (Abstract Syntax Tree) -> HIR (High-level IR, desugared) -> THIR (Typed HIR) -> MIR (Mid-level IR, control-flow graph) -> LLVM-IR -> machine code. The compiler is organized as approximately 50 interdependent `rustc_*` crates centered on `rustc_middle` (which defines core data structures and the query system). All major operations are organized as queries on the `TyCtxt` ("typing context"), which serves as the central hub for compilation state, query caching, and arena-allocated memory. Memory is managed through arena allocation and interning, allowing efficient pointer-based equality comparisons.

# Core Definition

The Rust compiler performs several unique analyses not found in typical compilers (borrow checking, trait solving) and uses an unconventional demand-driven architecture (the query system) rather than sequential passes.

## The Compilation Pipeline

**Lexing and parsing**: The lexer (`rustc_lexer`) produces tokens supporting Unicode with full fidelity for IDEs and proc-macros. A higher-level lexer in `rustc_parse` performs string interning. The parser uses recursive descent (top-down) to produce an AST. Macro expansion, AST validation, name resolution, and early linting also occur at this stage. The parser tries to recover from errors by parsing a superset of Rust's grammar.

**AST lowering**: The AST is converted to HIR, a "more compiler-friendly representation" that involves extensive desugaring of constructs like loops and `async fn`. Type inference, trait solving, and type checking operate on the HIR. Type checking converts user-written types (`hir::Ty`) to the compiler's internal representation (`Ty<'tcx>`).

**MIR lowering**: HIR is lowered through THIR (used for pattern and exhaustiveness checking) to MIR, a control-flow graph representation. MIR is the level at which borrow checking occurs. Many optimizations happen at MIR level "because it is generic and that improves later code generation and compilation speed." Monomorphization collection (determining which concrete types to generate code for) also happens at MIR level.

**Code generation**: MIR is converted to LLVM-IR, where actual monomorphization occurs. LLVM performs further optimizations and emits machine code. The resulting libraries/binaries are linked to produce the final output.

## Key Intermediate Representations

- **Token stream**: Atomic source code units from the lexer
- **AST**: "Represents pretty much exactly what the user wrote"
- **HIR**: Desugared AST, "close to what the user wrote syntactically" but with implicit things made explicit (elided lifetimes, etc.); amenable to type checking
- **THIR**: "Fully typed and a bit more desugared" HIR where method calls and implicit dereferences are made explicit; easier to lower to MIR
- **MIR**: "Basically a Control-Flow Graph (CFG)" with basic blocks containing simple typed statements and control flow edges; used for borrow checking, dataflow analysis, optimizations, and constant evaluation via Miri; still generic (pre-monomorphization)
- **LLVM-IR**: "A sort of typed assembly language with lots of annotations"; standard input format for LLVM

## The Central Data Structure: `TyCtxt`

The `TyCtxt<'tcx>` struct is "at the center of all things." All queries are methods on `TyCtxt`, and the in-memory query cache is stored there. The `'tcx` lifetime ties data to the typing context's arena. Despite the name, it is "not a 'typing context' in the sense of G or D from type theory" -- the name is historical.

## Memory Management

The compiler uses arena allocation and interning pervasively. "Each are allocated once from a long-lived arena." For interned types, identical values are allocated only once and compared by pointer equality. The `CtxtInterners` type contains the interning maps and the arena. The `ty::TyKind` type, representing types, "should never be constructed on the stack" -- it is always arena-allocated and interned.

## Crate Organization

The `rust-lang/rust` repository has three main directories: `compiler/` (~50 `rustc_*` crates), `library/` (standard libraries), and `tests/`. The crate dependency chain runs roughly:
1. `rustc` binary calls `rustc_driver::main`
2. `rustc_driver` depends on `rustc_interface` (generic compilation driver)
3. `rustc_interface` depends on most other compiler crates
4. Most crates depend on `rustc_middle` (central data structures, query system)
5. `rustc_middle` depends on foundational crates: `rustc_data_structures`, `rustc_span`, `rustc_errors`

The dependency structure is shaped by both code organization and compile-time considerations -- "by breaking the compiler into multiple crates, we can take better advantage of incremental/parallel compilation using cargo."

# Prerequisites

Understanding of basic compiler concepts (lexing, parsing, type checking, code generation). Familiarity with Rust's type system, ownership, and borrowing model. Knowledge of what LLVM is and its role as a compiler backend.

# Key Properties

1. **Demand-driven architecture**: Major steps are organized as queries that call each other, not sequential passes; this enables incremental compilation
2. **Multiple IRs**: Six distinct representations (tokens, AST, HIR, THIR, MIR, LLVM-IR), each optimized for specific analyses
3. **Arena allocation**: Data structures are allocated from a global arena with lifetime `'tcx`, enabling pointer-based equality comparison
4. **String interning**: All string values (symbols) are interned so identical strings share one allocation
5. **Partial query-fication**: As of the source's writing, only steps between HIR and LLVM-IR are query-driven; lexing, parsing, name resolution, and macro expansion are still done all-at-once
6. **`ty::Ty` centrality**: The internal type representation is "so important that we have a whole chapter on `ty::Ty`"
7. **Code generation parallelism**: Codegen units are generated by independent LLVM instances running in parallel; this is the only part parallel by default
8. **Serialization for crate metadata**: Query outputs are serialized to `.rlib`/`.rmeta` binary format using `Encodable`/`Decodable` traits with special handling for arena-allocated types via `TyEncoder`/`TyDecoder`
9. **`LazyValue<T>` for deferred deserialization**: Crate metadata stores offsets to serialized values, allowing deferred loading since metadata is loaded before `TyCtxt` exists
10. **Monomorphization at MIR level**: Concrete type copies are collected at MIR level for efficiency (pre-LLVM), but actual monomorphization occurs during LLVM-IR generation
11. **Parallel front-end (work in progress)**: Type checking, borrow checking, and MIR optimization are parallelized in nightly via `-Z threads=n`; lexing and HIR lowering remain serial
12. **Thread-safe data structures**: `Lock<T>` and `RwLock<T>` in `rustc_data_structures::sync` switch between `parking_lot` mutexes (parallel) and `RefCell` (non-parallel)

# Construction / Recognition

## Compilation Pipeline (Phase Ordering):

1. **Invocation**: CLI parsing in `rustc_driver`, configuration via `rustc_interface::Config`
2. **Lexing**: `rustc_lexer::Cursor::advance_token` -> token stream
3. **Parsing**: `Parser::parse_crate_mod` -> AST (`rustc_ast`)
4. **Macro expansion, name resolution, early linting**
5. **AST lowering**: AST -> HIR (`rustc_hir`)
6. **Type inference and checking**: `typeck` query
7. **HIR -> THIR -> MIR lowering**: Pattern checking, MIR building
8. **Borrow checking**: `mir_borrowck` query (runs on all functions)
9. **MIR optimizations**: `optimized_mir` query
10. **Monomorphization collection**: `collect_and_partition_mono_items`
11. **Code generation**: `rustc_codegen_ssa::base::codegen_crate` -> LLVM-IR -> machine code
12. **Linking**: Final binary assembly

## Key Source Locations:

- Lexer: `compiler/rustc_lexer/`
- Parser: `compiler/rustc_parse/src/parser/` (organized by construct: `expr.rs`, `pat.rs`, `ty.rs`, `stmt.rs`)
- HIR: `compiler/rustc_hir/`
- MIR: `compiler/rustc_middle/src/mir/`
- Type system: `compiler/rustc_middle/ty/`
- Borrow checker: `compiler/rustc_borrowck/`
- Code generation: `compiler/rustc_codegen_ssa/`
- LLVM integration: `compiler/rustc_llvm/` + `src/llvm-project` submodule

# Context & Application

- **New compiler contributors**: Understanding the pipeline and crate structure is essential for finding where to make changes
- **Performance analysis**: Knowing which phases are parallel (codegen) vs. serial (parsing, HIR lowering) helps identify bottlenecks
- **Tool authors**: `rustc_interface` provides the generic interface for tools like rustdoc, clippy, and Miri to drive compilation
- **Incremental compilation**: The query-driven architecture between HIR and LLVM-IR enables fine-grained caching and recomputation
- **Debugging**: Use `cargo rustc -- -Z unpretty=hir-tree` to view HIR, or `-Z unpretty=mir` for MIR

# Examples

**Example 1**: Invoking a query on the typing context:
```rust
let ty = tcx.type_of(some_def_id);
```

**Example 2**: The arena and interning model -- types are interned so identical types share a single pointer:
```rust
// ty::TyKind should never be constructed on the stack.
// Always use the arena:
let ty = tcx.mk_ty(TyKind::Int(IntTy::I32));
// Two references to the same type are pointer-equal
```

**Example 3**: Viewing the dependency order of compiler crates:
```console
cargo tree --package rustc_driver
```

**Example 4**: The naming pattern across compiler stages -- source files for each construct follow consistent names across crates:
> "You will find either a file or directory with the same name across the parsing, lowering, type checking, THIR lowering, and MIR building sources." (e.g., `expr.rs`, `pat.rs`, `ty.rs`)

# Relationships

## Builds Upon
- None within this extraction set -- this is the foundational architecture card

## Enables
- **rustc-compiler-query-system** -- the query system is the mechanism implementing the demand-driven architecture described here
- **rustc-compiler-bootstrapping** -- bootstrapping builds the compiler described in this architecture
- **rustc-compiler-dev-practices** -- development practices are applied within this crate structure

## Related
- **rustc-compiler-query-system** -- queries are the mechanism for the demand-driven compilation model
- **rustc-compiler-bootstrapping** -- the staged build process produces the compiler described here

## Contrasts With
- None within this source

# Common Errors

- **Error**: Constructing `ty::TyKind` on the stack instead of using the arena.
  **Correction**: "`ty::TyKind` should never be constructed on the stack, and it would be unusable if done so. You always allocate them from this arena and you always intern them so they are unique."

- **Error**: Assuming all compiler phases are query-driven.
  **Correction**: "Lexing, parsing, name resolution, and macro expansion are done all at once for the whole program." Only the steps between HIR and LLVM-IR are currently querified.

- **Error**: Assuming the compiler uses a standard pass-based architecture.
  **Correction**: "The Rust compiler _is not_ organized as a series of passes over the code which execute sequentially." It uses a demand-driven query system for most phases, specifically to enable incremental compilation.

# Common Confusions

- **Confusion**: `TyCtxt` is a typing context in the type-theory sense.
  **Clarification**: "This is _not_ a 'typing context' in the sense of G or D from type theory. The name is retained because that's what the name of the struct is in the source code." It is the central compilation context containing the query cache, arenas, and all major compiler state.

- **Confusion**: HIR and AST are the same thing.
  **Clarification**: The AST "represents pretty much exactly what the user wrote." HIR is a "desugared AST" that makes implicit things explicit (elided lifetimes, loop desugaring, async desugaring). HIR is "more compiler-friendly" and is what type checking operates on.

- **Confusion**: MIR and LLVM-IR serve similar purposes.
  **Clarification**: MIR is a generic (pre-monomorphization) control-flow graph used for Rust-specific analyses (borrow checking, dataflow analysis, Miri). LLVM-IR is a monomorphized, typed assembly language that is LLVM's standard input format. MIR contains Rust semantics; LLVM-IR is target-oriented.

- **Confusion**: Interning is purely a memory optimization.
  **Clarification**: Interning serves two purposes: memory efficiency (each distinct value is allocated once) and cheap equality comparison ("we can just compare pointers which is efficient"). Both are critical for compiler performance.

# Source Reference

Chapter 9: Compiler Overview (1186 lines). Covers high-level compiler architecture including compilation phases, intermediate representations (tokens, AST, HIR, THIR, MIR, LLVM-IR), the `TyCtxt` central data structure, query system overview, crate structure and dependency graph, memory management (arenas and interning), serialization for crate metadata and incremental compilation, parallel compilation status and data structures.

# Verification Notes

- Definition source: Direct quotes from the "Overview of the compiler" and "High-level overview of the compiler source" sections
- Key Properties: All items directly supported by source text with specific crate names, type names, and architectural descriptions
- Confidence rationale: HIGH -- this is the canonical architecture document for the Rust compiler, with explicit descriptions of each phase and design choice
- Uncertainties: Parallel compilation status is evolving rapidly; the source notes sections are "quite outdated" as of November 2024
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
