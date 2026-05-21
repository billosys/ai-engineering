---
# === CORE IDENTIFICATION ===
concept: Compiling and Loading Modules
slug: compiling-modules

# === CLASSIFICATION ===
category: tooling
subcategory: build-and-load
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.3.5 Compiling and loading modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "c(...)"
  - module loading
  - code path
  - object file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - beam-file
  - erlc
  - erlang-shell
  - beam
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you compile and load a module?"
  - "What is the code path?"
  - "How does Erlang find a module to load?"
---

# Quick Definition

Compiling a module turns its `.erl` source into a `.beam` object file the runtime can load and execute. The shell function `c(...)` compiles and loads in one step; the code path tells Erlang where to find `.beam` files.

# Core Definition

"When you *compile* a module, you produce a corresponding file with the extension `.beam` instead of `.erl`, which contains instructions in a form that the Erlang system can load and execute" (Chapter 2, section 2.3.5). The `.beam` file is a more compact, definite form of the module; it cannot be edited by hand. The simplest way to compile while testing is the shell function `c(...)`, which compiles a module and also loads it; it looks for the source relative to the shell's current directory and you need not write the `.erl` suffix. A successful `c(my_module)` returns `{ok,my_module}` and produces `my_module.beam`. When Erlang tries to call a module not yet loaded, it automatically loads it from a matching `.beam` file if it can find one in the *code path* — the list of directories searched, which by default includes the current directory and all standard library directories. `code:get_path()` shows it; the `code` module can modify it.

# Prerequisites

- **Erlang module** — compilation operates on a module source file.

# Key Properties

1. Compiling produces a `.beam` object file from a `.erl` source file.
2. The `.beam` file is compact, loadable, and not human-editable.
3. The shell function `c(Module)` compiles and loads a module in one step.
4. A successful compile returns `{ok,Module}`.
5. Erlang auto-loads a not-yet-loaded module from a matching `.beam` file in the code path.
6. The code path includes the current directory and standard library directories by default.
7. `code:get_path()` returns the code path; the `code` module can modify it.

# Construction / Recognition

## To Construct/Create:
1. In the shell, run `c(my_module)` (no `.erl` suffix needed).
2. Check the result is `{ok,my_module}`.
3. Call the module's exported functions, e.g. `my_module:pie()`.
4. On restart, the module loads automatically from `my_module.beam` via the code path.

# Context & Application

- **Typical contexts**: Interactive development and testing.
- **Common applications**: Recompiling and reloading after edits without restarting Erlang.
- **Historical/stylistic notes**: Standard library directories conventionally end in `/ebin`, the convention for holding `.beam` files.

# Examples

**Example 1** (section 2.3.5): `c(my_module).` returns `{ok,my_module}`, then `my_module:pie().` returns `3.14`; a `my_module.beam` file appears alongside the source.

**Example 2** (section 2.3.5): After restarting Erlang in the same directory, `my_module:pie()` works without recompiling because Erlang auto-loads `my_module.beam` from the code path.

# Relationships

## Builds Upon
- **Erlang module** — compilation turns a module into a loadable form.

## Enables
- **BEAM file** — the `.beam` object file produced.
- Auto-loading of modules via the code path.

## Related
- **erlc** — the standalone compiler for scripted builds.
- **Erlang shell** — `c(...)` is a shell function.
- **BEAM** — the emulator loads and runs the compiled `.beam`.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Trying to edit a `.beam` file directly.
  **Correction**: `.beam` files are not human-editable; edit the `.erl` source and recompile.

- **Error**: Running `c("my_module.erl")` expecting the shell function to need the extension.
  **Correction**: The shell function `c(...)` does not need the `.erl` suffix (unlike `erlc`).

# Common Confusions

- **Confusion**: Thinking a module must be compiled every session before it can be used.
  **Clarification**: Erlang auto-loads a module from its `.beam` file via the code path on first call.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.5 "Compiling and loading modules" (Compiling from the shell, and Module loading and the code path subsections).

# Verification Notes

- Definition source: Direct adaptation from section 2.3.5.
- Confidence rationale: HIGH — compilation, `.beam` files, `c(...)`, and the code path are explicitly described.
- Uncertainties: None.
- Cross-reference status: `beam-file` and `erlc` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
