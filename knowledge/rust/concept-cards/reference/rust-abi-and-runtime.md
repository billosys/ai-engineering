---
concept: ABI and Runtime
slug: rust-abi-and-runtime
category: compilation
subcategory: abi
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Application Binary Interface / The Rust Runtime"
chapter_number: 19
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Rust ABI"
  - "no_mangle attribute"
  - "export_name attribute"
  - "link_section attribute"
  - "used attribute"
  - "global_allocator attribute"
  - "windows_subsystem attribute"
prerequisites: []
extends: []
related:
  - rust-linkage
  - rust-unsafety-reference
  - nomicon-ffi
contrasts_with: []
answers_questions:
  - "How do the ABI-related attributes (used, no_mangle, link_section, export_name) work?"
  - "Why are no_mangle, link_section, and export_name unsafe attributes?"
  - "How do you set a custom global allocator in Rust?"
  - "How do you configure the Windows subsystem for a Rust application?"
  - "What keeps a static item in the compiled output even if it is unused?"
---

# Quick Definition

Chapters 19 (ABI) and 20 (Runtime) define attributes that control how compiled Rust code interacts at the binary level and how the runtime is configured. The ABI chapter covers `#[used]`, `#[no_mangle]`, `#[link_section]`, and `#[export_name]` -- attributes that control symbol visibility, naming, and placement. The Runtime chapter covers `#[global_allocator]` for memory allocator selection and `#[windows_subsystem]` for Windows application type.

# Core Definition

**ABI Attributes (Chapter 19):**

**`#[used]`** -- applied to `static` items only. Forces the compiler to keep the variable in object files even if unreferenced. However, the linker may still remove it. Without `#[used]`, unreferenced private statics are removed by the compiler.

**`#[unsafe(no_mangle)]`** -- may be applied to any item. Disables standard symbol name mangling so the symbol is the item's identifier. Also publicly exports the item from the library or object file. This is `unsafe` because an unmangled symbol may collide with another symbol, causing undefined behavior. Before Edition 2024, `unsafe` qualification was not required.

**`#[unsafe(link_section = "...")]`** -- applied to functions or statics. Places the item's content into the specified object file section. This is `unsafe` because it can place data/code into unexpected memory sections (e.g., mutable data in read-only areas). Only the first use on an item takes effect.

**`#[unsafe(export_name = "...")]`** -- applied to functions or statics. Specifies a custom exported symbol name. This is `unsafe` because a custom symbol may collide with other symbols. Only the first use on an item takes effect.

**Runtime Attributes (Chapter 20):**

**`#[global_allocator]`** -- applied to a `static` item whose type implements `GlobalAlloc`. Selects the memory allocator for the program. May only be used once in the entire crate graph. Exported from the standard library prelude.

**`#[windows_subsystem = "..."]`** -- applied to the crate root. Sets the Windows linker subsystem. Accepts `"console"` (default, attaches to existing console or creates new) or `"windows"` (runs detached from any console, used by GUI applications). Ignored on non-Windows targets and non-`bin` crate types. Only the first use takes effect.

# Prerequisites

Understanding of Rust's compilation model, static items, and the concepts of symbol mangling and linking.

# Key Properties

1. `#[used]` only prevents the compiler from removing a static; the linker may still remove it during dead code elimination
2. `#[no_mangle]` both disables mangling and publicly exports the symbol -- it has a dual effect
3. `#[no_mangle]`, `#[link_section]`, and `#[export_name]` are all unsafe attributes because they can cause symbol collisions or memory layout violations leading to UB
4. All three unsafe ABI attributes require `#[unsafe(...)]` wrapping since Edition 2024; before 2024, bare usage was allowed
5. `#[link_section]` and `#[export_name]` only apply their first use -- duplicate uses are linted with a future-compatibility warning
6. `#[global_allocator]` may only appear once in the entire crate dependency graph
7. `#[global_allocator]` requires the static's type to implement the `GlobalAlloc` trait
8. `#[windows_subsystem]` has no effect on non-Windows targets or non-`bin` crate types
9. The `"windows"` subsystem is commonly used by GUI applications to suppress a console window on startup
10. A static is kept in the object file if it is: `#[used]`, publicly reachable, or referenced by a reachable function

# Construction / Recognition

## Exporting a C-Compatible Symbol

```rust
#[unsafe(no_mangle)]
extern "C" fn my_function() {
    // This function is exported with symbol name "my_function"
    // and uses the C calling convention
}
```

## Custom Global Allocator

```rust
use core::alloc::{GlobalAlloc, Layout};
use std::alloc::System;

struct MyAllocator;

unsafe impl GlobalAlloc for MyAllocator {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        unsafe { System.alloc(layout) }
    }
    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        unsafe { System.dealloc(ptr, layout) }
    }
}

#[global_allocator]
static GLOBAL: MyAllocator = MyAllocator;
```

## Placing Data in a Specific Section

```rust
#[unsafe(no_mangle)]
#[unsafe(link_section = ".example_section")]
pub static VAR1: u32 = 1;
```

# Context & Application

The ABI attributes are essential for FFI: `#[no_mangle]` and `#[export_name]` create symbols that C/C++ code can link against, while `#[link_section]` places data in specific memory regions for embedded systems (e.g., interrupt vector tables, DMA buffers, or specific flash regions). The `#[used]` attribute prevents the compiler from optimizing away statics that are referenced only by linker scripts or assembly code rather than by Rust code.

The runtime attributes configure fundamental program behavior: `#[global_allocator]` enables custom allocators for embedded systems (no-std), arena allocators for performance, or tracking allocators for debugging. `#[windows_subsystem = "windows"]` is ubiquitous in Windows GUI applications built with frameworks like `winit`, `egui`, or `druid`.

The Edition 2024 change requiring `#[unsafe(...)]` for `no_mangle`, `link_section`, and `export_name` reflects a broader safety initiative: these attributes can silently cause UB through symbol collisions, and wrapping them in `unsafe` makes the programmer explicitly acknowledge this risk.

# Examples

**Example 1** (Static retention rules -- which statics survive compilation):
```rust
#[used]
static FOO: u32 = 0;          // Kept: #[used]

#[allow(dead_code)]
static BAR: u32 = 0;          // Removed: unused, no #[used]

pub static BAZ: u32 = 0;      // Kept: publicly reachable

static QUUX: u32 = 0;
pub fn quux() -> &'static u32 { &QUUX }  // QUUX kept: referenced by public fn

static CORGE: u32 = 0;
#[allow(dead_code)]
fn corge() -> &'static u32 { &CORGE }    // CORGE removed: referenced by dead fn
```

**Example 2** (Custom export name):
```rust
#[unsafe(export_name = "exported_symbol_name")]
pub fn name_in_rust() { }
// The symbol in the output is "exported_symbol_name", not the mangled form
```

**Example 3** (Windows subsystem for GUI application):
```rust
#![windows_subsystem = "windows"]
// On Windows, this program will run without showing a console window.
// On non-Windows platforms, this attribute is ignored.
```

# Relationships

## Builds Upon
(none -- these are standalone attributes)

## Enables
- **rust-linkage** -- ABI attributes control how symbols appear in linked artifacts
- **nomicon-ffi** -- `no_mangle` and `export_name` are the primary tools for creating FFI-compatible symbols

## Related
- **rust-unsafety-reference** -- symbol collisions from these attributes can cause UB
- **rust-linkage** -- crate types interact with runtime attributes (e.g., `windows_subsystem` only applies to `bin` crates)

## Contrasts With
(none)

# Common Errors

- **Error**: Using `#[no_mangle]` without `extern "C"` on a function intended for FFI.
  **Correction**: `#[no_mangle]` only controls the symbol name; it does not change the calling convention. Add `extern "C"` to use the C ABI, which is necessary for most FFI scenarios.

- **Error**: Applying `#[global_allocator]` to multiple statics across the crate graph.
  **Correction**: Only one `#[global_allocator]` is allowed across all crates in the dependency graph. If a library crate sets the allocator, no other crate (including the binary) can set one.

- **Error**: Expecting `#[used]` to guarantee the symbol appears in the final binary.
  **Correction**: `#[used]` only prevents compiler removal; the linker may still remove the symbol during dead code elimination. Use linker flags (e.g., `--gc-keep-exported`) or linker scripts to ensure the symbol survives linking.

# Common Confusions

- **Confusion**: Thinking `#[no_mangle]` only affects the symbol name.
  **Clarification**: `#[no_mangle]` has two effects: it disables name mangling AND publicly exports the symbol. It acts similarly to `#[used]` in terms of visibility.

- **Confusion**: Using `#[link_section]` or `#[export_name]` multiple times on the same item expecting all to apply.
  **Clarification**: Only the first use of each attribute on an item takes effect. Subsequent uses are linted with future-compatibility warnings and may become hard errors.

- **Confusion**: Assuming `#[windows_subsystem = "windows"]` prevents all console output.
  **Clarification**: The attribute only controls whether a console window is attached/created. The program can still write to stdout/stderr; the output just may not be visible since no console is displayed.

# Source Reference

Chapter 19 (ABI, 156 lines): `#[used]` attribute (static retention), `#[no_mangle]` (symbol naming and export), `#[link_section]` (object file section placement), `#[export_name]` (custom symbol name). Chapter 20 (Runtime, 87 lines): `#[global_allocator]` (GlobalAlloc trait, singleton constraint), `#[windows_subsystem]` (console vs. windows).

# Verification Notes

- Definition source: Direct extraction from Chapter 19 (156 lines) and Chapter 20 (87 lines), covering all attributes in both chapters
- Key Properties: Items 1-10 are direct from source with minimal synthesis
- Confidence rationale: HIGH -- both chapters are concise and explicit with clear attribute specifications
- Uncertainties: None significant; these are well-defined compiler/linker attributes
- Cross-reference status: All slugs reference cards in the reference and nomicon extraction sets
