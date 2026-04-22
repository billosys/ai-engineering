---
concept: "Code Generation: LLVM Pipeline, Debugging, and Track Caller"
slug: compiler-code-generation
category: compiler-internals
subcategory: codegen
tier: advanced
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "23-code-generation"
chapter_number: 23
pdf_page: null
section: "Code generation, Updating LLVM, Debugging LLVM, Backend agnostic codegen, Implicit caller location"
extraction_confidence: high
aliases:
  - "codegen"
  - "LLVM IR generation"
  - "rustc_codegen_ssa"
  - "rustc_codegen_llvm"
  - "updating LLVM"
  - "debugging LLVM"
  - "#[track_caller]"
  - "backend agnostic codegen"
  - "LTO"
  - "codegen units"
prerequisites: []
extends: []
related:
  - compiler-mir-optimizations
  - compiler-backends
  - compiler-debug-info
contrasts_with: []
answers_questions:
  - "How does rustc generate machine code from MIR?"
  - "What is the relationship between rustc_codegen_ssa and rustc_codegen_llvm?"
  - "How do I update the LLVM version used by rustc?"
  - "How do I debug LLVM code generation issues?"
  - "How do I get the LLVM IR that rustc generates?"
  - "How does the backend-agnostic codegen abstraction work?"
  - "How does #[track_caller] work at the compiler level?"
  - "What LLVM tools are useful for debugging codegen bugs?"
  - "How does link-time optimization (LTO) work in rustc?"
  - "How do I file an LLVM bug report?"
---

# Quick Definition

Code generation is the final phase of the Rust compiler where MIR is translated into executable machine code through a codegen backend (LLVM, Cranelift, or GCC). The `rustc_codegen_ssa` crate provides the backend-agnostic abstraction layer, while `rustc_codegen_llvm` implements the LLVM-specific codegen. LLVM IR is grouped into codegen units, optimized by LLVM's pass pipeline, and linked into the final binary. The chapter also covers the LLVM update process, LLVM debugging techniques, and the `#[track_caller]` feature implementation.

# Core Definition

"Code generation (or 'codegen') is the part of the compiler that actually generates an executable binary. Usually, rustc uses LLVM for code generation, but there is also support for Cranelift and GCC. The key is that rustc doesn't implement codegen itself." (Ch. 23, Code generation)

The backend abstraction was created by refactoring `rustc_codegen_llvm`: "The goal of this refactoring is to separate inside this crate code that is specific to the LLVM from code that can be reused for other rustc backends." (Ch. 23, Backend Agnostic Codegen)

LLVM takes LLVM IR as input: "LLVM takes input in the form of LLVM IR. It is basically assembly code with additional low-level types and annotations added. These annotations are helpful for doing optimizations on the LLVM IR and outputted machine code." (Ch. 23, What is LLVM?)

# Prerequisites

None listed, though understanding MIR, monomorphization, and the query system from Chapter 22 is assumed.

# Key Properties

1. **LLVM IR modules as codegen units**: "LLVM IR is grouped into 'modules'. Multiple 'modules' can be codegened at the same time to aid in multi-core utilization. These 'modules' are what we refer to as codegen units."
2. **LTO timing**: "With certain kinds of LTO, the optimization might happen at the linking time instead. It is also possible for some optimizations to happen before objects are passed on to the linker and some to happen during the linking."
3. **Key crates**: `rustc_codegen_ssa` contains backend-agnostic code; `rustc_codegen_llvm` contains LLVM-specific code; the `back` module handles object files, archives, and parallel codegen
4. **Backend trait hierarchy**: `BuilderMethods` is the master trait for IR instruction generation; it has an associated type `CodegenCx` satisfying `CodegenMethods`; `ExtraBackendMethods` drives high-level codegen functions like `codegen_crate`
5. **Lifetime parameters**: `'tcx` for the original TyCtxt, `'ll` for LLVM object references, `'a` for short-lived references to CodegenCx or other structs
6. **LOC breakdown after refactoring**: `mir` folder is 4,400 LOC backend-agnostic (0 LLVM-specific); `back` folder split ~50/50; `builder.rs` is 1,400 LOC backend-agnostic; approximately 10,000 LOC reused across backends
7. **LLVM update types**: Three procedures -- backports while upstream supports the release, backports after upstream drops support (cherry-pick), and full major version updates (requires `llvm-wrapper` C++ binding updates)
8. **LLVM debugging tools**: `llc` (bitcode to executable), `opt` (optimization passes), `bugpoint` (test case reducer); all built to `build/host/llvm/bin`
9. **Key compiler flags**: `--emit llvm-ir/llvm-bc` for IR output, `-C no-prepopulate-passes` for raw IR, `-C llvm-args=-print-after-all` for pass tracing, `-C save-temps` for intermediate bitcode, `-C llvm-args=-opt-bisect-limit=N` for bisecting optimizations
10. **#[track_caller] mechanism**: Appends an implicit `&'static core::panic::Location<'static>` argument to tracked functions at codegen time; in const contexts, walks up the interpreter stack to find the first untracked caller
11. **ReifyShim for function pointers**: When taking a pointer to a `#[track_caller]` function, a `ReifyShim` wraps it because the ABI change is invisible to the type system; the shim reports the definition site rather than the call site
12. **Trait method tracking**: `#[track_caller]` on a trait method prototype applies to all implementations; on a default implementation, it applies to that implementation and any overrides

# Construction / Recognition

## To Get LLVM IR for Debugging:
1. Pass `--emit=llvm-ir` to rustc (or `RUSTFLAGS='--emit=llvm-ir'` with Cargo)
2. Use `cargo llvm-ir [options] path` for a specific function's IR
3. Add `RUSTFLAGS="-C debuginfo=0"` to reduce clutter from debug info
4. Use `-C save-temps` to get bitcode at different compilation stages
5. Extract specific functions with `llvm-extract -func='<mangled_name>'`

## To Debug an LLVM Optimization Bug:
1. Minimize the reproducing Rust code (use `creduce` if needed)
2. Enable LLVM assertions: set `llvm.assertions = true` in bootstrap.toml
3. Use `-C codegen-units=1` to simplify debugging
4. Use `-C llvm-args=-opt-bisect-limit=-1` to list all passes with indices
5. Binary search the pass index to find the errant optimization
6. Create a Godbolt reproducer at llvm.godbolt.org with LLVM-IR as the language

## To Update LLVM in Rustc:
1. For backports (upstream supported): merge upstream release branch into rust-lang/llvm-project fork
2. For backports (unsupported): cherry-pick commits with `git cherry-pick -x`
3. For major updates: create new branch from upstream `release/$N.x`, apply Rust-specific patches, update `llvm-wrapper/*.cpp` bindings with `#ifdef` guards for old versions
4. Always set `llvm.download-ci-llvm = false` in bootstrap.toml during development

# Context & Application

This is the most substantial chapter in the backend section, covering the complete journey from MIR to executable binary. The architecture is deliberately layered: `rustc_codegen_ssa` defines traits (`BuilderMethods`, `CodegenMethods`, `ExtraBackendMethods`) that abstract over the specific backend, allowing LLVM, Cranelift, and GCC to share approximately 10,000 lines of code.

The LLVM debugging section is particularly practical, providing a step-by-step methodology for isolating codegen bugs. The `-opt-bisect-limit` technique is especially powerful -- it assigns stable indices to each LLVM optimization pass, allowing automated binary search to pinpoint which pass introduces a miscompilation.

The `#[track_caller]` implementation is an elegant example of compiler-runtime cooperation. Rather than walking the stack at runtime (expensive), the compiler inverts the problem: it passes location information down the call stack as an extra argument, threading a single `&Location` through multiple function calls. The `ReifyShim` solution for function pointers demonstrates a careful balance between type system soundness and practical codegen constraints.

The backend-agnostic refactoring history is valuable for understanding why the code is structured as it is. The refactoring achieved zero performance regression by using compile-time parametricity (generics) rather than trait objects, confirming that the abstraction has no runtime cost.

# Examples

**Example 1** (Ch. 23, Backend-agnostic function signature): Codegen function parametrized by backend:
```rust
pub fn codegen_instance<'a, 'tcx, Bx: BuilderMethods<'a, 'tcx>>(
    cx: &'a Bx::CodegenCx,
    instance: Instance<'tcx>
) {
    /* ... */
}
```

**Example 2** (Ch. 23, #[track_caller] compilation): Source:
```rust
#[track_caller]
fn print_caller() {
    println!("called from {}", Location::caller());
}
fn main() { print_caller(); }
```
Compiled as if:
```rust
fn print_caller(caller: &Location) {
    println!("called from {}", caller);
}
fn main() {
    print_caller(&Location::internal_constructor(file!(), line!(), column!()));
}
```

**Example 3** (Ch. 23, LLVM debugging workflow):
```bash
# Get raw LLVM IR (before LLVM optimizations)
rustc +local my-file.rs --emit=llvm-ir -O -C no-prepopulate-passes -C codegen-units=1
# Run LLVM optimizations manually
build/$TRIPLE/llvm/bin/opt -S -O2 < my-file.ll > my-optimized.ll
# Bisect to find problematic pass
RUSTFLAGS="-C llvm-args=-opt-bisect-limit=-1" cargo build 2>&1 | head
```

# Relationships

## Builds Upon
- MIR optimizations and monomorphization collection (provides the input)
- The query system (`codegen_crate`, `collect_and_partition_mono_items`)
- LLVM's C++ API (via `llvm-wrapper/*.cpp` FFI bindings)

## Enables
- Production of executable binaries, shared libraries, and static libraries
- Cross-compilation to all LLVM-supported targets
- Alternative backends (Cranelift, GCC) through the trait abstraction

## Related
- **compiler-mir-optimizations** -- upstream: provides optimized MIR and monomorphized items for codegen
- **compiler-backends** -- covers backend-specific details for LLVM, Cranelift, and GCC
- **compiler-debug-info** -- debug information generation that occurs alongside codegen

## Contrasts With
- MIR optimizations (operate on generic MIR before monomorphization, vs LLVM optimizations on concrete LLVM IR)
- The frontend (parsing, type checking) which is backend-independent

# Common Errors

- **Error**: Trying to reproduce an LLVM bug with multiple codegen units active.
  **Correction**: "The default rustc compilation pipeline has multiple codegen units, which is hard to replicate manually. [...] passing `-C codegen-units=1` to rustc will make debugging easier."

- **Error**: Using `-print-after-all` without filtering in a multi-CGU build.
  **Correction**: "Because the multiple codegen units run in parallel, the printouts will mix together and you won't be able to read anything." Use `-C codegen-units=1` or add `-filter-print-funcs=EXACT_FUNCTION_NAME`.

- **Error**: Building with `profile = "compiler"` when testing LLVM changes.
  **Correction**: Default profiles download LLVM from CI instead of building from source. Set `llvm.download-ci-llvm = false` in bootstrap.toml to use your local LLVM changes.

# Common Confusions

- **Confusion**: Thinking `rustc_codegen_ssa` means "SSA form."
  **Clarification**: The name `rustc_codegen_ssa` was a suggestion by @eddyb; it stands for the backend-agnostic shared codegen layer, not SSA form specifically (though some SSA-related analysis does occur here).

- **Confusion**: Thinking `#[track_caller]` modifies the function's type signature.
  **Clarification**: "The ABI change must be transparent to type checking and remain sound in all uses." The extra `&Location` argument is added at the codegen level only. For function pointers, a `ReifyShim` preserves soundness by reporting the definition site.

- **Confusion**: Thinking LLVM's `-print-after-all` output can be fed back to `llc`.
  **Clarification**: "The -print family of options to LLVM only prints the IR unit that the pass runs on (e.g., just a function), and does not include any referenced declarations, globals, metadata, etc." Use `.bc` files from `-C save-temps` instead.

# Source Reference

Chapter 23: Code generation (LLVM overview, codegen_crate entry point, modules/CGUs, linking, LTO), Updating LLVM (backport procedures, major version updates, llvm-wrapper bindings), Debugging LLVM (minimization, assertions, raw IR, opt-bisect-limit, Godbolt, compiler flags reference, filing bug reports), Backend Agnostic Codegen (refactoring history, trait hierarchy, BuilderMethods/CodegenMethods, LOC breakdown, lifetime parameters), Implicit Caller Location (#[track_caller] attribute, const evaluation walk, ReifyShim, trait methods, codegen examples).

# Verification Notes

- Definition source: Direct quotations from Ch. 23 introduction, LLVM section, Backend Agnostic Codegen, and Implicit Caller Location
- Key Properties: Covers all major topics across 1,066 lines
- Confidence rationale: HIGH -- comprehensive chapter with clear architecture descriptions, practical debugging guides, and well-documented refactoring history
- Uncertainties: LLVM version numbers and specific PR references will become outdated; `llvm-wrapper` bindings evolve with each LLVM update
- Cross-reference status: `compiler-mir-optimizations`, `compiler-backends`, `compiler-debug-info` are in this extraction set
