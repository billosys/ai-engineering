---
concept: "MIR Optimizations, Constant Evaluation, and Monomorphization"
slug: compiler-mir-optimizations
category: compiler-internals
subcategory: mir-backend
tier: advanced
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "22-mir-optimizations"
chapter_number: 22
pdf_page: null
section: "MIR optimizations, MIR debugging, Constant evaluation, Interpreter, Monomorphization, Lowering MIR to codegen IR"
extraction_confidence: high
aliases:
  - "MIR optimization passes"
  - "constant evaluation"
  - "CTFE interpreter"
  - "monomorphization collector"
  - "codegen unit partitioning"
  - "MIR lowering"
  - "optimized_mir"
prerequisites: []
extends: []
related:
  - compiler-code-generation
  - compiler-backends
contrasts_with: []
answers_questions:
  - "How do I add a new MIR optimization pass?"
  - "What are the MIR optimization levels and how do they work?"
  - "How does constant evaluation work in the Rust compiler?"
  - "What is the CTFE interpreter and how does it execute MIR?"
  - "How does monomorphization collection work?"
  - "What are codegen units and how are they partitioned?"
  - "How is MIR lowered to LLVM IR?"
  - "How do I debug MIR with dump flags?"
  - "What is the relationship between the interpreter and Miri?"
  - "How does the interpreter's virtual memory work?"
---

# Quick Definition

MIR optimizations are compiler passes that improve MIR before codegen, running after borrow checking. They operate on generic (pre-monomorphization) code, making optimizations especially effective since they apply to all instantiations. After optimization, the monomorphization collector discovers all concrete type instantiations needed, partitions them into codegen units (CGUs), and then each MIR function is lowered to a codegen IR (typically LLVM IR) for final code generation.

# Core Definition

"MIR optimizations are optimizations run on the MIR to produce better MIR before codegen. This is important for two reasons: first, it makes the final generated executable code better, and second, it means that LLVM has less work to do, so compilation is faster. Note that since MIR is generic (not monomorphized yet), these optimizations are particularly effective; we can optimize the generic version, so all of the monomorphizations are cheaper!" (Ch. 22, MIR optimizations)

The constant evaluation system (CTFE) uses a virtual machine interpreter that executes MIR at compile time, shared between the compiler and the Miri tool. "The interpreter is a virtual machine for executing MIR without compiling to machine code. It is usually invoked via `tcx.const_eval_*` functions." (Ch. 22, Interpreter)

Monomorphization stamps out concrete copies of generic code: "Rust takes a different approach: it monomorphizes all generic types. This means that compiler stamps out a different copy of the code of a generic function for each concrete type needed." (Ch. 22, Monomorphization)

# Prerequisites

None listed, though familiarity with the MIR representation and the query system is assumed.

# Key Properties

1. **Optimization pass pipeline**: The list of passes and their order is defined by `run_optimization_passes`, which returns an array of `&dyn MirPass` trait objects; each pass is typically implemented in its own module of `rustc_mir_transform`
2. **optimized_mir query**: The `optimized_mir` query ensures borrow checking has run, steals the MIR, optimizes it, and returns the improved MIR
3. **Pass examples**: `CleanupPostBorrowck` removes analysis-only info not needed for codegen; `ConstProp` does constant propagation; many more implementors exist
4. **MIR opt levels**: Experimental passes can be controlled via `-Z mir-opt-level`; levels are defined in the compiler MCP; check `tcx.sess.opts.unstable_opts.mir_opt_level` at runtime
5. **MIR debugging**: `-Z dump-mir=F` dumps MIR for functions matching filter F, supporting `&` (and) and `|` (or) combinators; `-Z dump-mir-graphviz` and `-Z dump-mir-dataflow` produce `.dot` files
6. **Constant evaluation categories**: Either "influencing the type system" (array lengths, enum discriminants, const generic params) or "precomputing expressions to be used at runtime"
7. **Interpreter virtual memory**: Each allocation gets its own `Allocation` with a unique `AllocId`; a `Pointer` is a pair of `AllocId` + offset, not an integer address, since compile-time addresses are unknown
8. **Pointer values vs pointer types**: Being a pointer value (`Scalar::Ptr`) and having a pointer type (`*const T`) are independent; integers can hold pointer values and pointers can hold integer values via casts/transmutes
9. **Monomorphization collection**: `collect_and_partition_mono_items` query discovers all concrete instantiations (functions, statics) and partitions them into codegen units; runs just before codegen
10. **CGU partitioning**: Two CGUs per source-level module -- one for stable (non-generic) code, one for volatile (monomorphized/specialized) instances; generic and `#[inline]` functions from dependencies land in a single CGU for the dependent crate
11. **MIR-to-codegen-IR lowering**: `rustc_codegen_ssa::mir::codegen_mir` does the lowering, with submodules for blocks/terminators, statements, operands, places, and rvalues; a pre-lowering analysis pass identifies SSA-like variables for direct SSA translation
12. **Basic block mapping**: Usually one MIR basic block maps to one LLVM basic block, with exceptions for intrinsic/function calls and `assert` statements that may generate multiple blocks

# Construction / Recognition

## To Add a New MIR Optimization Pass:
1. Create a test in `tests/mir-opt` with minimal Rust code demonstrating the target optimization
2. Run `./x test --bless tests/mir-opt/<test>.rs` to generate baseline MIR dumps
3. Commit the baseline (so reviewers see before/after diffs)
4. Implement the pass in `compiler/rustc_mir_transform/src` -- copy a small pass like `remove_storage_markers` as a starting point
5. Register the pass in `run_optimization_passes()`
6. Re-run `./x test --bless` and verify diffs; run `./x test tests/ui` for regressions
7. Open a PR (WIP is fine) for early feedback

## To Inspect MIR Dumps:
1. Use `-Z dump-mir=foo` to dump MIR for functions matching "foo"
2. Files are in `mir_dump/` with names like `rustc.main.000-000.CleanEndRegions.after.mir`
3. Use filter combinators: `main & CleanEndRegions | main & NoLandingPads`
4. Use `-Z unpretty=mir-cfg` for a graphviz CFG diagram of the whole crate

## To Trigger Constant Evaluation:
1. Call `tcx.const_eval_global_id_for_typeck()` to get a valtree for type-system inspection
2. Call `tcx.const_eval_global_id()` for an opaque blob for codegen backends
3. Call `tcx.eval_static_initializer()` specifically for statics (which have special handling)

# Context & Application

This chapter covers the critical bridge between the type-checked MIR and executable machine code. Three major subsystems work in sequence: MIR optimization passes improve the generic MIR, constant evaluation computes compile-time values using a virtual machine interpreter, and monomorphization collection discovers all concrete type instantiations. Finally, the MIR is lowered to a codegen IR (typically LLVM IR).

The CTFE interpreter is particularly notable because it is shared with Miri, the undefined behavior detector. The interpreter's virtual memory model, where pointers are symbolic `(AllocId, offset)` pairs rather than integer addresses, is a fundamental design choice that enables precise tracking of pointer provenance at compile time. The `Operand::Immediate` optimization avoids allocating virtual memory for small stack variables that never have their address taken.

The monomorphization collector and CGU partitioner are performance-critical: CGU partitioning directly affects incremental build times and parallel compilation. The two-CGU-per-module strategy balances incremental reuse (stable code rarely changes) with parallelism (each CGU can be compiled independently).

# Examples

**Example 1** (Ch. 22, Interpreter walkthrough): Evaluating `const FOO: usize = 1 << 12` with usage `type Foo = [u8; FOO - 42]`:
```mir
Foo::{{constant}}#0: usize = {
    let mut _0: usize;
    let mut _1: (usize, bool);

    bb0: {
        _1 = CheckedSub(const FOO, const 42usize);
        assert(!move (_1.1: bool), "attempt to subtract with overflow") -> bb1;
    }
    bb1: {
        _0 = move (_1.0: usize);
        return;
    }
}
```
The interpreter evaluates this: `_1` becomes `ScalarPair(4054, 0)` (value, overflow-bool), the assert passes, and `_0` gets `Scalar(4054)`. The result is converted from `Operand` to `ConstValue::Scalar(4054)` for use by the rest of the compiler.

**Example 2** (Ch. 22, Monomorphization collection): Given:
```rust
fn banana() { peach::<u64>(); }
fn main() { banana(); }
```
The collector produces `[main, banana, peach::<u64>]` -- the concrete functions needing machine code.

**Example 3** (Ch. 22, MIR dump filter): Selective MIR dumps:
```bash
rustc -Z dump-mir='main & CleanEndRegions' foo.rs
# Produces: rustc.main.000-000.CleanEndRegions.{before,after}.mir
```

# Relationships

## Builds Upon
- MIR representation and the borrow checker (optimizations run after borrow checking)
- The query system (`optimized_mir`, `const_eval_*`, `collect_and_partition_mono_items`)
- `TyCtxt` and the type system (for monomorphization and const evaluation)

## Enables
- Code generation (provides optimized, monomorphized MIR ready for lowering)
- Compile-time function evaluation (CTFE) for `const fn`, `static`, array lengths
- The Miri tool for detecting undefined behavior (shares the interpreter)

## Related
- **compiler-code-generation** -- the downstream consumer of monomorphized, lowered MIR
- **compiler-backends** -- LLVM/Cranelift/GCC backends that process the codegen IR

## Contrasts With
- LLVM's own optimization passes, which operate on LLVM IR after MIR lowering
- Runtime evaluation (the interpreter executes MIR at compile time without generating machine code)

# Common Errors

- **Error**: Writing a MIR optimization test with `println!` or formatting macros.
  **Correction**: "Avoid `println!` or other formatting code if it's not necessary for the optimization. The reason for this is that `println!`, `format!`, etc. generate a lot of MIR that can make it harder to understand what the optimization does to the test."

- **Error**: Accessing an `Allocation` directly from outside the interpreter.
  **Correction**: "You should never have to access an Allocation directly except for translating it to the compilation target (at the moment just LLVM)." Use the `const_eval_*` functions and work with `ConstValue` instead.

- **Error**: Using `const_eval_global_id` or `const_eval_global_id_for_typeck` for statics.
  **Correction**: "Statics are special; all other functions do not represent statics correctly and have thus assertions preventing their use on statics." Use `eval_static_initializer` for statics.

# Common Confusions

- **Confusion**: Thinking MIR optimizations and LLVM optimizations are the same thing.
  **Clarification**: MIR optimizations run on generic MIR before monomorphization, so they optimize once for all instantiations. LLVM optimizations run later on the monomorphized LLVM IR. Both contribute to final code quality, but MIR optimizations also reduce LLVM's workload.

- **Confusion**: Thinking the CTFE interpreter's pointers are real memory addresses.
  **Clarification**: Interpreter pointers are `(AllocId, offset)` pairs -- symbolic references, not integer addresses. "During const evaluation, we cannot know at which actual integer address the allocation will end up -- so we use AllocId as symbolic base addresses."

- **Confusion**: Thinking monomorphization happens during MIR optimization.
  **Clarification**: MIR optimization runs on generic MIR. Monomorphization collection happens afterward, just before codegen, to discover all concrete types needed. The actual monomorphization (substituting concrete types) occurs during the lowering to codegen IR.

# Source Reference

Chapter 22: MIR optimizations (pass pipeline, MirPass trait, opt levels), MIR Debugging (dump-mir filters, graphviz), Constant Evaluation (const_eval queries, valtrees, GlobalId), Interpreter (virtual memory, Allocation, Pointer, AllocId, Frame, step evaluation, Operand/Immediate/Scalar), Monomorphization (collection, CGU partitioning, cross-crate behavior table), Lowering MIR to Codegen IR (codegen_mir, submodules for blocks/statements/operands/places/rvalues, SSA analysis).

# Verification Notes

- Definition source: Direct quotations from Ch. 22 sections on MIR optimizations, Interpreter, and Monomorphization
- Key Properties: Covers all major topics across 738 lines spanning MIR optimization, CTFE, monomorphization, and codegen lowering
- Confidence rationale: HIGH -- well-structured chapter with clear explanations, concrete examples, and extensive code references
- Uncertainties: `-Z mir-opt-level` values and specific pass lists may change between compiler versions
- Cross-reference status: `compiler-code-generation` and `compiler-backends` are in this extraction set
