---
# === CORE IDENTIFICATION ===
concept: GPU Offloading and Automatic Differentiation
slug: compiler-gpu-and-autodiff

# === CLASSIFICATION ===
category: compiler-internals
subcategory: experimental-backends
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "GPU and Autodiff"
chapter_number: 12
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "std::offload"
  - "std::autodiff"
  - "GPU offloading in Rust"
  - "automatic differentiation"
  - "Enzyme"
  - "LLVM offload"
  - "differentiable programming"
  - "TypeTrees"
  - "abi_gpu_kernel"
  - "autodiff_reverse"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiler-mir
  - compiler-cli-and-drivers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is std::offload and how does GPU offloading work in Rust?"
  - "What is std::autodiff and how does automatic differentiation work?"
  - "What is the two-pass compilation approach for GPU offloading?"
  - "How does Enzyme integrate with the Rust compiler for autodiff?"
  - "What are TypeTrees and why does Enzyme need them?"
  - "What RUSTFLAGS control autodiff behavior (PrintTA, LooseTypes, etc.)?"
  - "How do you build rustc with GPU offload and autodiff support?"
  - "How do you report and minimize autodiff backend crashes?"
---

# Quick Definition

The Rust compiler has two experimental features for high-performance computing: `std::offload` for running Rust code on GPUs, and `std::autodiff` for automatic differentiation (computing derivatives of functions). GPU offloading uses a single-source, two-pass compilation approach built on LLVM's "offload" project, compiling code separately for device (GPU) and host (CPU). Automatic differentiation uses the Enzyme LLVM plugin to transform functions into their derivatives at the LLVM IR level, supporting both forward and reverse mode differentiation. Both features are experimental and require building rustc from source or using nightly with additional components.

# Core Definition

**`std::offload`** implements GPU programming by compiling Rust functions marked with `#[rustc_offload_kernel]` and `extern "gpu-kernel"` ABI for GPU targets (e.g., `nvptx64`, `amdgcn-amd-amdhsa`). The compilation uses a **single-source, two-pass approach**: (1) first pass compiles device code for the GPU target, and (2) second pass compiles host code for the CPU, generating calls to the OpenMP offload runtime for data movement and kernel launching. The runtime uses type information to determine whether kernel arguments need to be moved to the device (e.g., `&[f32; 1024]`), from the device, or both (e.g., `&mut [f64]`). The second pass loads kernel artifacts from the first compilation, with the path communicated via `RUSTFLAGS`.

A single-pass approach was explicitly rejected: the Rust frontend (AST stage) drops dead code behind inactive `cfg` attributes, and teaching the entire compiler to handle two implementations per symbol would add unacceptable complexity for minimal runtime performance benefit.

**`std::autodiff`** enables differentiable programming through the `#[autodiff_reverse]` and `#[autodiff_forward]` attributes. The implementation uses the Enzyme LLVM plugin, which operates at the LLVM IR level. The compilation pipeline with autodiff is: (1) run the normal compilation pipeline (with vectorization/unrolling disabled for release builds), (2) differentiate functions using Enzyme, (3) re-run the optimization pipeline on the whole module.

**TypeTrees** are memory layout descriptors that tell Enzyme how types are structured so it can compute derivatives efficiently. Each `TypeTree` contains a vector of `Type` entries with `offset` (byte position, or `-1` for "everywhere/all elements"), `size`, `kind` (Float, Integer, Pointer), and a `child` TypeTree for nested structures. Single values use offset `0` for precision; arrays use offset `-1` to avoid listing every element individually. Without TypeTrees, Enzyme would have to guess pointer layouts from generic LLVM IR, leading to slow analysis or incorrect derivatives.

Various `RUSTFLAGS` control autodiff behavior: debug flags (`PrintTA`, `PrintAA`, `Print`, `PrintModBefore/After/Final`, `LooseTypes`) and benchmark flags (`NoPostopt`, `RuntimeActivity`, `Inline`). The `LooseTypes` flag can suppress "Can not deduce type" errors but risks producing incorrect gradients.

# Prerequisites

Understanding of LLVM IR and the Rust compilation pipeline. Familiarity with GPU computing concepts (kernels, device/host memory) for offloading, or calculus concepts (derivatives, gradients) for autodiff.

# Key Properties

1. **Experimental status**: Both features require nightly Rust and are under active development; `std::offload` is not yet ready for general usage
2. **Two-pass GPU compilation**: Device code is compiled first for the GPU target, then host code is compiled with references to the device artifacts
3. **OpenMP offload runtime**: GPU offloading leverages LLVM's existing OpenMP offload infrastructure for data movement and kernel execution
4. **Enzyme-based autodiff**: Automatic differentiation happens at the LLVM IR level using the Enzyme plugin, supporting forward and reverse mode
5. **TypeTree memory descriptors**: Explicit layout information (offset, size, kind, nesting) tells Enzyme which bytes are differentiable vs metadata
6. **Offset -1 convention**: In TypeTrees, offset `-1` means "this pattern repeats for all elements" -- used for arrays and slices instead of listing every element
7. **Three-phase autodiff pipeline**: Compile (with vectorization disabled) -> differentiate with Enzyme -> re-optimize the whole module
8. **LooseTypes risk**: The `LooseTypes` flag can produce silently incorrect gradients for certain inputs while appearing correct for others
9. **Fat LTO required**: Autodiff currently requires `lto="fat"` in Cargo.toml for user projects

# Construction / Recognition

## Using autodiff:
```rust,ignore
#![feature(autodiff)]
use std::autodiff::*;

// f(x) = x * x, f'(x) = 2.0 * x
#[autodiff_reverse(bar, Active, Active)]
fn foo(x: f32) -> f32 { x * x }

fn main() {
    assert_eq!(bar(3.0, 1.0), (9.0, 6.0));
}
```

## Building rustc with autodiff:
```bash
git clone git@github.com:rust-lang/rust
cd rust
./configure --release-channel=nightly --enable-llvm-enzyme \
  --enable-llvm-link-shared --enable-llvm-assertions \
  --enable-ninja --enable-option-checking --disable-docs \
  --set llvm.download-ci-llvm=false
./x build --stage 1 library
rustup toolchain link enzyme build/host/stage1
```

## Running autodiff in user projects:
```bash
# Add lto="fat" to Cargo.toml
RUSTFLAGS="-Zautodiff=Enable" cargo +enzyme build
```

## TypeTree example for `&f32`:
```rust,ignore
TypeTree(vec![Type {
    offset: -1, size: 8, kind: Pointer,
    child: TypeTree(vec![Type {
        offset: 0, size: 4, kind: Float, // Single value: offset 0
        child: TypeTree::new()
    }])
}])
```

## TypeTree example for `&[f32]` (slice):
```rust,ignore
TypeTree(vec![Type {
    offset: -1, size: 8, kind: Pointer,
    child: TypeTree(vec![Type {
        offset: -1, size: 4, kind: Float, // All elements: offset -1
        child: TypeTree::new()
    }])
}])
```

# Context & Application

These features target high-performance computing domains:
- **GPU offloading**: Scientific computing, machine learning inference, data-parallel workloads
- **Automatic differentiation**: Neural network training (backpropagation), numerical optimization, computational physics (fluid dynamics, solid mechanics), ODE solvers, differentiable rendering, quantum computing

Both features represent Rust's expansion into domains traditionally dominated by C++/Fortran (for GPU computing) and Python/Julia (for autodiff). The Enzyme-based approach is notable because it differentiates at the LLVM IR level, meaning it works with optimized code rather than requiring source-level transformations.

The debugging workflow for autodiff backend crashes involves generating LLVM IR reproducers (`-Z autodiff=Enable,PrintModBefore`), minimizing with `llvm-extract` and `llvm-reduce`, and reporting to the Enzyme issue tracker with Compiler Explorer links.

# Examples

**Example 1** (Ch. 12, "Basic autodiff"):
```rust,ignore
#![feature(autodiff)]
use std::autodiff::*;

#[autodiff_reverse(bar, Active, Active)]
fn foo(x: f32) -> f32 { x * x }

fn main() {
    assert_eq!(bar(3.0, 1.0), (9.0, 6.0));  // (f(3), f'(3)) = (9, 6)
    assert_eq!(bar(4.0, 1.0), (16.0, 8.0)); // (f(4), f'(4)) = (16, 8)
}
```

**Example 2** (Ch. 12, "GPU kernel"): A GPU kernel using `extern "gpu-kernel"` ABI:
```rust,ignore
#![feature(abi_gpu_kernel)]
#[unsafe(no_mangle)]
#[rustc_offload_kernel]
pub extern "gpu-kernel" fn kernel_1(x: *mut [f64; 256]) {
    unsafe { (*x)[0] = 21.0 };
}
```
Launched via `core::intrinsics::offload(_kernel_1, [256, 1, 1], [32, 1, 1], (x,))`.

**Example 3** (Ch. 12, "TypeTree for struct"):
```rust,ignore
struct Point {
    x: f32, // offset 0, size 4
    y: f32, // offset 4, size 4
    id: i32, // offset 8, size 4
}
// TypeTree for &Point:
// {[-1]:Pointer, [-1,0]:Float@float, [-1,4]:Float@float,
//  [-1,8]:Integer, [-1,9]:Integer, [-1,10]:Integer, [-1,11]:Integer}
```

**Example 4** (Ch. 12, "RUSTFLAGS for debugging"):
```bash
# Print the LLVM-IR module before AD runs:
RUSTFLAGS="-Z autodiff=Enable,PrintModBefore" cargo +enzyme build --release

# Use LooseTypes to work around type deduction errors (risk incorrect gradients!):
RUSTFLAGS="-Z autodiff=Enable,LooseTypes,PrintPerf" cargo +enzyme build
```

# Relationships

## Builds Upon
(none directly in this extraction set -- builds on LLVM infrastructure)

## Enables
(none in this extraction set -- these are end-user experimental features)

## Related
- **compiler-mir** -- both features operate at the LLVM IR level, which is generated from MIR during codegen
- **compiler-cli-and-drivers** -- autodiff/offload flags are passed via RUSTFLAGS to the driver

## Contrasts With
(none within this source)

# Common Errors

- **Error**: Using `LooseTypes` and trusting the gradients are correct.
  **Correction**: `LooseTypes` risks producing silently incorrect derivatives. Gradients may be correct for some inputs but wrong for others. Use only as a temporary workaround while waiting for a bug fix; always verify numerical correctness.

- **Error**: Building autodiff projects without `lto="fat"` in Cargo.toml.
  **Correction**: Autodiff currently requires fat LTO. Add `lto = "fat"` to your `[profile.release]` in Cargo.toml.

- **Error**: Using system `clang` instead of the LLVM build matching rustc for GPU offloading.
  **Correction**: The `clang` compiler must be built on the same LLVM as rustc. Use absolute paths or set `PATH` accordingly to avoid picking up an incompatible system clang.

# Common Confusions

- **Confusion**: GPU offloading could use a single-pass compilation approach.
  **Clarification**: The Rust frontend drops dead code behind inactive `cfg` attributes and the AST stage would produce multiple definitions for the same symbol. Teaching the entire middle and backend to handle dual implementations would add prohibitive complexity for no runtime performance benefit.

- **Confusion**: Autodiff operates on Rust source code or the AST.
  **Clarification**: Enzyme operates at the LLVM IR level, after all Rust-specific transformations. This means it works with optimized code, and debugging requires working with LLVM IR reproducers, not Rust source.

- **Confusion**: TypeTrees are optional for Enzyme.
  **Clarification**: While Enzyme can attempt to deduce types from LLVM IR, this is slow and error-prone for complex types. TypeTrees provide explicit layout information that enables correct and efficient derivative computation, especially for nested structures and pointer-heavy code.

# Source Reference

Chapter 12 of the Rust Compiler Dev Guide (759 lines). Covers: `std::offload` (two-pass compilation design, OpenMP runtime, kernel launch, data movement), `std::autodiff` (Enzyme integration, `#[autodiff_reverse]`/`#[autodiff_forward]`, three-phase pipeline), installation and build instructions for both features, GPU compile workflow (device pass, host pass, clang-linker-wrapper), TypeTrees (structure, offset conventions, LLVM IR annotations), RUSTFLAGS for autodiff (debug and benchmark flags), backend crash reporting and minimization workflow (llvm-extract, llvm-reduce, Compiler Explorer), and contributing guidelines.

# Verification Notes

- Definition source: Directly extracted from Chapter 12 sections on std::offload, std::autodiff, TypeTrees, and RUSTFLAGS
- Key Properties: All derived from explicit descriptions in the source text
- Confidence rationale: MEDIUM -- features are experimental and under active development; APIs and workflows may change significantly
- Uncertainties: Both features are explicitly described as work-in-progress; `std::offload` is "not ready for usage" per the documentation; autodiff requires external Enzyme component
- Cross-reference status: Loosely related to MIR (operates at LLVM IR, which is generated from MIR) and CLI/drivers (flags passed through RUSTFLAGS)
