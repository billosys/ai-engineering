---
concept: Inline Assembly
slug: rust-inline-assembly
category: unsafe-rust
subcategory: low-level
tier: advanced
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Inline Assembly"
chapter_number: 16
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "asm! macro"
  - "global_asm!"
  - "naked_asm!"
  - "inline asm"
  - "register operands"
  - "assembly template strings"
prerequisites:
  - rust-unsafety-reference
extends: []
related:
  - rust-abi-and-runtime
  - rust-linkage
  - nomicon-ffi
contrasts_with: []
answers_questions:
  - "How do you embed assembly code in Rust using asm!, naked_asm!, and global_asm!?"
  - "What operand types does inline assembly support (in, out, inout, sym, const, label)?"
  - "What register classes are available on each supported architecture?"
  - "What options (pure, nomem, readonly, noreturn, etc.) modify asm! behavior?"
  - "What rules must be followed to avoid undefined behavior in inline assembly?"
  - "How does clobber_abi work for calling convention clobbers?"
---

# Quick Definition

Rust provides `asm!`, `naked_asm!`, and `global_asm!` macros for embedding handwritten assembly into compiler-generated output. Inline assembly supports six operand types (`in`, `out`, `lateout`, `inout`, `inlateout`, `sym`, `const`, `label`), register class or explicit register selection, template string formatting, optimization options, and ABI-based clobber declarations. Strict rules govern register preservation, memory access, and stack usage to prevent undefined behavior.

# Core Definition

Inline assembly is stable on x86/x86-64, ARM, AArch64/Arm64EC, RISC-V, LoongArch, s390x, and PowerPC/PowerPC64. It operates in three scopes:

**`asm!`** emits assembly within a function, integrated into compiler-generated code. It must obey strict rules to avoid UB. The compiler may duplicate or deduplicate the assembly.

**`naked_asm!`** constitutes the entire body of a `#[naked]` function. Only `sym` and `const` operands are allowed; only `att_syntax` and `raw` options apply.

**`global_asm!`** emits assembly at global scope, outside any function. Like `naked_asm!`, only `sym` and `const` operands are permitted.

**Operand types:**
- `in(reg) expr` -- loads value into register at entry; register must be preserved at exit
- `out(reg) expr` -- register contains undefined value at entry; writes to place expression at exit; `_` discards (clobber)
- `lateout(reg) expr` -- like `out` but may reuse an `in` register
- `inout(reg) expr` or `inout(reg) in_expr => out_expr` -- input at entry, output at exit; separate in/out expressions may have different types if both are pointers or integers of same size
- `inlateout` -- like `inout` but may reuse another `in` register
- `sym path` -- substitutes mangled symbol name for a `fn` or `static`
- `const expr` -- substitutes integer constant expression value as text
- `label { block }` -- substitutes address of a Rust block; assembly may jump to it; block starts a new safety context

**Template strings** use format-string syntax with `{}` placeholders. Multiple strings are joined with `\n`. All template strings must precede other arguments. Positional arguments must precede named arguments and explicit register operands.

**Register specification:** operands use either a register class identifier (e.g., `reg`, `xmm_reg`) or an explicit register string (e.g., `"eax"`). Same explicit register cannot be used for two inputs or two outputs. Register aliases (e.g., `eax`/`rax`/`ax`) are treated as equivalent. Template modifiers (e.g., `:e`, `:l`, `:h` on x86) control how register names appear in output.

# Prerequisites

Understanding of unsafe Rust, raw pointers, and the concept of undefined behavior. Familiarity with assembly language for the target architecture.

# Key Properties

1. Operand expressions are evaluated left to right; outputs are written left to right (rightmost wins for overlapping outputs)
2. Values smaller than the register width leave upper bits undefined for inputs and ignored for outputs (except RISC-V `freg` where `f32` is NaN-boxed)
3. Only integers, floats, thin pointers, function pointers, and `#[repr(simd)]` Copy types are allowed as register operands
4. `clobber_abi("C")` automatically inserts `lateout("...") _` for all registers not preserved by the specified calling convention; when used, all outputs must use explicit registers
5. Options: `pure` (no side effects, deterministic), `nomem` (no memory access), `readonly` (no memory writes), `preserves_flags` (flags unchanged), `noreturn` (does not fall through), `nostack` (no stack usage), `att_syntax` (x86 AT&T mode), `raw` (no `{}` processing)
6. `nomem` and `readonly` are mutually exclusive; `pure` requires `nomem` or `readonly`; `pure` requires at least one non-discarded output
7. The compiler treats assembly as a black box -- it cannot assume the written instructions are what actually executes (runtime patching is allowed)
8. On x86, the direction flag (DF) must be clear on exit; the x87 stack must be unchanged unless all st(0)-st(7) are clobbered
9. Two adjacent `asm!` blocks cannot be assumed to produce successive instructions in the binary
10. An `asm!` block cannot be assumed to appear exactly once -- the compiler may duplicate it (e.g., via inlining)

# Construction / Recognition

## Writing Safe Inline Assembly

1. Choose the right scope: `asm!` for function-level, `global_asm!` for standalone routines, `naked_asm!` for naked functions
2. Specify all input operands with `in`/`inout` and all output operands with `out`/`lateout`/`inlateout`
3. For function calls within assembly, use `clobber_abi` with the appropriate ABI and explicit register outputs
4. Use `sym` for function/static references and `const` for compile-time integer constants
5. Apply optimization hints: `pure` + `nomem`/`readonly` for side-effect-free computations; `preserves_flags` when flags are untouched; `nostack` when no stack is used
6. Use template modifiers (e.g., `{x:e}` for 32-bit view on x86-64) to avoid subregister width warnings
7. Ensure all registers not specified as outputs are restored to their entry values
8. Restore the stack pointer to its original value before exiting

## Using label Operands

1. Specify `label { block }` -- the block address is substituted into the template
2. Assembly may jump to the label; after the block executes, `asm!` returns
3. The block must have type `()` or `!`; unsafe operations inside require their own `unsafe` block
4. Label blocks cannot coexist with output operands

# Context & Application

Inline assembly enables direct hardware access, SIMD intrinsics not yet wrapped by `core::arch`, system calls, context switching, and performance-critical hot loops. The `asm!` macro replaces the old unstable `llvm_asm!` with a safer, more portable design. The `clobber_abi` feature is essential for calling conventions -- it prevents the common FFI bug of failing to declare clobbered registers. The `label` operand enables structured control flow between assembly and Rust code, avoiding raw address computation. `global_asm!` allows writing entire functions in assembly (e.g., interrupt handlers, boot code) while keeping them in Rust source files.

# Examples

**Example 1** (Basic multiply-by-6 on x86-64):
```rust
use std::arch::asm;
let mut x: u64 = 4;
unsafe {
    asm!(
        "mov {tmp}, {x}",
        "shl {tmp}, 1",
        "shl {x}, 2",
        "add {x}, {tmp}",
        x = inout(reg) x,
        tmp = out(reg) _,
    );
}
assert_eq!(x, 4 * 6);
```

**Example 2** (Calling a C function with clobber_abi):
```rust
extern "C" fn foo() -> i32 { 0 }
let z: i32;
unsafe {
    core::arch::asm!(
        "call {}",
        sym foo,
        out("rax") z,
        clobber_abi("C"),
    );
}
assert_eq!(z, 0);
```

**Example 3** (Label operand for structured jump):
```rust
unsafe {
    core::arch::asm!("jmp {}", label {
        println!("Hello from inline assembly label");
    });
}
```

# Relationships

## Builds Upon
- **rust-unsafety-reference** -- all `asm!` invocations require unsafe blocks and are subject to UB rules

## Enables
- Low-level system programming: interrupt handlers, context switching, bootloaders
- Performance-critical SIMD operations beyond what `core::arch` intrinsics provide

## Related
- **rust-abi-and-runtime** -- `clobber_abi` interacts with calling conventions; `no_mangle`/`export_name` affect symbols referenced via `sym`
- **rust-linkage** -- `global_asm!` emits code at global scope affecting the linked artifact
- **nomicon-ffi** -- inline assembly follows the same memory access rules as FFI functions

## Contrasts With
(none)

# Common Errors

- **Error**: Forgetting to restore non-output registers to their entry values.
  **Correction**: Any register not declared as an output must have the same value on exit as on entry. Use `clobber_abi` to automatically handle calling-convention clobbers, or explicitly declare clobbers with `out("reg") _`.

- **Error**: Using `pure` without `nomem` or `readonly`, or using `pure` without outputs.
  **Correction**: `pure` must be combined with `nomem` (no memory access at all) or `readonly` (reads only). It must also have at least one non-discarded output, or the compiler will error.

- **Error**: Using generic register class outputs with `clobber_abi`.
  **Correction**: When `clobber_abi` is specified, all output operands must use explicit registers (e.g., `out("rax") z`) to avoid accidental overlap with clobbered registers.

# Common Confusions

- **Confusion**: Assuming two adjacent `asm!` blocks will produce adjacent instructions.
  **Clarification**: The compiler makes no guarantee about instruction placement. It may insert code between them, duplicate them, or reorder them. Each `asm!` block is treated independently.

- **Confusion**: Thinking `nostack` means the assembly cannot use any stack memory.
  **Clarification**: `nostack` means the assembly must not push data to the stack or write to the red zone. Without `nostack`, the compiler guarantees proper stack alignment and the assembly may freely use stack space below the stack pointer.

- **Confusion**: Expecting `naked_asm!` to support register operands like `asm!`.
  **Clarification**: `naked_asm!` defines an entire function body, so there is no compiler-generated prologue/epilogue to manage register operands. Only `sym` and `const` operands are allowed; function arguments must be accessed according to the calling convention.

# Source Reference

Chapter 16 (Inline Assembly, 1728 lines): Three macros (asm!, naked_asm!, global_asm!), syntax grammar, template string arguments, operand types (in/out/lateout/inout/inlateout/sym/const/label), register operands and classes (tables for x86, AArch64, Arm64EC, ARM, RISC-V, LoongArch, s390x, PowerPC), value type constraints, register names and aliases, template modifiers, ABI clobbers, options (pure/nomem/readonly/preserves_flags/noreturn/nostack/att_syntax/raw), rules for asm! (19 rules) and naked_asm! (7 rules), directives support.

# Verification Notes

- Definition source: Direct extraction from Chapter 16 (1728 lines), covering all major sections with representative details
- Key Properties: Items 1-10 are direct from source rules and option descriptions
- Confidence rationale: HIGH -- the source is comprehensive with explicit rules, tables, and examples
- Uncertainties: Register classes and supported ABIs may expand as new architectures are added; x86 LLVM modifiers `x`/`t`/`g` for xmm_reg not yet implemented in LLVM
- Cross-reference status: All slugs reference cards in the reference and nomicon extraction sets
