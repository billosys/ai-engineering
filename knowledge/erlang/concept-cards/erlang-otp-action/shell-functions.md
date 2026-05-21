---
# === CORE IDENTIFICATION ===
concept: Shell Functions
slug: shell-functions

# === CLASSIFICATION ===
category: tooling
subcategory: interactive-environment
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.1.3 Shell functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - shell commands
  - "v(N)"
  - "help()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-shell
extends: []
related:
  - shell-expression
  - compiling-modules
contrasts_with:
  - bif

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are shell functions?"
  - "Which shell functions should a beginner know?"
  - "How do you list available shell functions?"
---

# Quick Definition

Shell functions are special functions available only in the Erlang shell — such as `v(N)`, `help()`, `c(...)`, and `q()` — typically with short, cryptic names.

# Core Definition

"Some functions like `v(N)` are available only in the shell and nowhere else in Erlang. These *shell functions* usually have short (and somewhat cryptic) names" (Chapter 2, section 2.1.3). Entering `help()` (itself a shell function) lists the available shell functions. The book highlights the ones a beginner should know: `help()` (prints available shell functions), `h()` (history of entered commands), `v(N)` (fetches the value computed at prompt N), `cd(Dir)`, `ls()`/`ls(Dir)`, `pwd()`, `q()` (quits — shorthand for `init:stop()`), `i()` (system information), and `memory()` (memory usage). Related shell functions `f()` and `f(X)` forget bound variables.

# Prerequisites

- **Erlang shell** — shell functions exist only within the shell.

# Key Properties

1. Shell functions are available only in the shell, nowhere else in Erlang.
2. They usually have short, cryptic names.
3. `help()` lists the available shell functions.
4. They include `v(N)`, `h()`, `cd`, `ls`, `pwd`, `q()`, `i()`, `memory()`, `f()`.
5. `q()` is shorthand for `init:stop()` and shuts the system down cleanly.

# Construction / Recognition

## To Identify/Recognize:
1. A function that works at the shell prompt but is not in any module.
2. Short cryptic name; appears in the `help()` listing.

# Context & Application

- **Typical contexts**: Interactive development and live system inspection.
- **Common applications**: Reusing results (`v(N)`), compiling code (`c(...)`), inspecting the system (`i()`), quitting (`q()`).
- **Historical/stylistic notes**: `i()` shows that, like an operating system, many things run in the background besides the shell prompt.

# Examples

**Example 1** (Table 2.1, "Important Erlang shell functions"): The book tabulates `help()`, `h()`, `v(N)`, `cd(Dir)`, `ls()`/`ls(Dir)`, `pwd()`, `q()`, `i()`, and `memory()` as the shell functions to know from the start.

**Example 2** (section 2.1.3): `q()` is described as a shorthand for the function `init:stop()`.

# Relationships

## Builds Upon
- **Erlang shell** — shell functions are shell-only.

## Enables
- Interactive result reuse, compilation, and system inspection.

## Related
- **Shell expression** — `v(N)` fetches the result of a previous expression.
- **Compiling modules** — `c(...)` is a shell function that compiles and loads.

## Contrasts With
- **Built-in function** — BIFs are part of the language/runtime and available everywhere; shell functions exist only in the shell.

# Common Errors

- **Error**: Trying to call a shell function such as `v(1)` from within a compiled module.
  **Correction**: Shell functions exist only in the shell; they are not available in module code.

# Common Confusions

- **Confusion**: Confusing the shell function `q()` with the hard-shutdown `q` in the Ctrl-G menu.
  **Clarification**: `q()` shuts down cleanly via `init:stop()`; the Ctrl-G `q` is a hard shutdown.

# Source Reference

Chapter 2: Erlang language essentials, section 2.1.3 "Shell functions." See Table 2.1.

# Verification Notes

- Definition source: Direct adaptation from section 2.1.3 and Table 2.1.
- Confidence rationale: HIGH — shell functions are explicitly defined and tabulated.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
