---
# === CORE IDENTIFICATION ===
concept: Built-in Function
slug: bif

# === CLASSIFICATION ===
category: api-design
subcategory: standard-library
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.3.3 Built-in functions and standard library modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - BIF
  - built-in function
  - standard library
  - auto-imported function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-function
  - erlang-module
extends: []
related:
  - remote-call
  - process-spawning
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a BIF?"
  - "What is the Erlang standard library?"
  - "Which functions can be called without a module prefix?"
---

# Quick Definition

A BIF (built-in function) is a function so low-level that it is an intrinsic part of the Erlang runtime, implemented in C. All functions in the `erlang` module are BIFs.

# Core Definition

Erlang comes with a *standard library* of functions spread over many modules; the `erlang` module "contains functions that are central to the entire Erlang system, which everything else builds on" (Chapter 2, section 2.3.3). Some functions "are so low-level that the functions are an intrinsic part of the language and the runtime system. These are commonly referred to as *built-in functions* (BIFs), and like the Erlang runtime system, they're implemented in the C programming language." All functions in the `erlang` module are BIFs. Some BIFs (like `lists:reverse/1`) could in principle be written in Erlang but are implemented in C for efficiency. A few important `erlang` functions are *auto-imported* — `self()`, `spawn(...)`, `length(...)` — so they need no `erlang:` prefix; even operators like `+` are BIFs (`erlang:'+'(1,2)` equals `1+2`).

# Prerequisites

- **Erlang function** — BIFs are functions.
- **Erlang module** — BIFs live in modules (notably `erlang`).

# Key Properties

1. A BIF is a built-in function intrinsic to the language and runtime.
2. BIFs are implemented in the C programming language.
3. All functions in the `erlang` module are BIFs.
4. Some BIFs could be written in Erlang but are in C for efficiency.
5. Important `erlang` functions are auto-imported and need no module prefix.
6. Operators such as `+` are BIFs belonging to the `erlang` module.

# Construction / Recognition

## To Identify/Recognize:
1. A function in the `erlang` module is a BIF.
2. Auto-imported functions (`self()`, `spawn`, `length`) are BIFs callable without a prefix.
3. Operators are BIFs — `erlang:'+'(1,2)` is `1+2`.

# Context & Application

- **Typical contexts**: Core operations used everywhere in Erlang programs and in the shell.
- **Common applications**: Spawning processes, getting the current pid, list length, arithmetic.
- **Historical/stylistic notes**: Useful standard-library modules include `lists`, `io`, `dict`, and `array`; the term *BIF* is used often in the Erlang world.

# Examples

**Example 1** (section 2.3.3): `self()` is a BIF — a remote call to `erlang:self()` — auto-imported so the `erlang:` prefix can be omitted; `spawn(...)` and `length(...)` are likewise auto-imported BIFs.

**Example 2** (section 2.3.3): Even operators are BIFs: `erlang:'+'(1,2)` is the same as `1+2`.

# Relationships

## Builds Upon
- **Erlang function** and **Erlang module** — a BIF is a function in a module.

## Enables
- Core runtime operations available to all Erlang code.

## Related
- **Remote call** — non-auto-imported BIFs are called with a module prefix.
- **Process spawning** — `spawn` is an auto-imported BIF.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming you must write `erlang:` before `self()` or `spawn`.
  **Correction**: These are auto-imported BIFs; the `erlang:` prefix is optional.

# Common Confusions

- **Confusion**: Believing BIFs behave or look different from ordinary functions.
  **Clarification**: BIFs look the same to the eye; the term only signals they are implemented in C as part of the runtime.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.3 "Built-in functions and standard library modules."

# Verification Notes

- Definition source: Direct adaptation from section 2.3.3.
- Confidence rationale: HIGH — BIFs and the standard library are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card. Merged "built-in functions" and "standard library modules" into one card since the source treats them in a single section and the standard library is defined in terms of BIFs and modules.
