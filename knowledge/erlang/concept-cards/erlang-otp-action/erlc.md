---
# === CORE IDENTIFICATION ===
concept: erlc
slug: erlc

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
section: "2.3.6 The stand-alone compiler, erlc"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - standalone compiler
  - stand-alone compiler

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - compiling-modules
extends: []
related:
  - beam-file
  - erlang-shell
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is erlc?"
  - "When do you use erlc instead of the shell's c(...)?"
  - "How do you set the output directory for compiled files?"
---

# Quick Definition

`erlc` is Erlang's standalone command-line compiler, used to run the compiler from the operating system command line — typically as part of a scripted build.

# Core Definition

"In a real software project, you typically want to script your builds using an external build tool, such as GNU Make. In this case, you can use the standalone `erlc` program to run the compiler from your operating system command line" (Chapter 2, section 2.3.6). For example, `erlc my_module.erl` compiles the module. Unlike the shell function `c(...)`, `erlc` needs the full file name including the `.erl` extension. It accepts options much like a C compiler — for instance `erlc -o ./ebin my_module.erl` specifies the output directory for the `.beam` file. On Windows the installer does not add `erl` and `erlc` to the `PATH`; this must be done manually to run them from `cmd.exe`.

# Prerequisites

- **Erlang module** — `erlc` compiles a module source file.
- **Compiling and loading modules** — `erlc` is an alternative to shell-based compilation.

# Key Properties

1. `erlc` is the standalone command-line Erlang compiler.
2. It runs from the operating system command line, suited to scripted builds.
3. It requires the full file name, including the `.erl` extension.
4. It accepts options, such as `-o` to set the output directory.
5. On Windows, `erlc` is not on the `PATH` by default and must be added manually.

# Construction / Recognition

## To Construct/Create:
1. From the OS command line, run `erlc my_module.erl`.
2. Use options as needed, e.g. `erlc -o ./ebin my_module.erl`.
3. The resulting `.beam` file is written to the chosen directory.

# Context & Application

- **Typical contexts**: Real software projects with scripted builds (e.g. GNU Make).
- **Common applications**: Batch compilation of many modules; build automation.
- **Historical/stylistic notes**: Standard library `.beam` files conventionally live in an `ebin` subdirectory, matching the `-o ./ebin` convention.

# Examples

**Example 1** (section 2.3.6): `erlc my_module.erl` compiles the module from the operating system command line — the full `.erl` name is required.

**Example 2** (section 2.3.6): `erlc -o ./ebin my_module.erl` uses the `-o` option to write the `.beam` file into the `ebin` directory.

# Relationships

## Builds Upon
- **Erlang module** — `erlc` compiles module source files.
- **Compiling and loading modules** — `erlc` is the standalone alternative.

## Enables
- **BEAM file** — `erlc` produces `.beam` files.
- Scripted, automated builds.

## Related
- **Erlang shell** — the shell's `c(...)` is the interactive alternative to `erlc`.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Running `erlc my_module` without the `.erl` extension.
  **Correction**: `erlc` requires the full file name including `.erl` (unlike the shell function `c(...)`).

- **Error**: Expecting `erlc` to be on the `PATH` on Windows.
  **Correction**: The Windows installer does not set this; add the Erlang `bin` directory to `PATH` manually.

# Common Confusions

- **Confusion**: Treating `erlc` and the shell function `c(...)` as identical.
  **Clarification**: `erlc` runs from the OS command line and needs the `.erl` suffix; `c(...)` runs in the shell, omits the suffix, and also loads the module.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.6 "The stand-alone compiler, erlc."

# Verification Notes

- Definition source: Direct adaptation from section 2.3.6.
- Confidence rationale: HIGH — `erlc` is explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
