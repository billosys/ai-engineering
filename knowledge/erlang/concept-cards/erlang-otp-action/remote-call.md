---
# === CORE IDENTIFICATION ===
concept: Remote Call
slug: remote-call

# === CLASSIFICATION ===
category: core-idioms
subcategory: function-calls
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.3.1 Calling functions in other modules (remote calls)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - qualified call
  - local call
  - module-qualified call

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - erlang-function
extends: []
related:
  - function-arity
  - bif
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a remote call in Erlang?"
  - "How do you call a function in another module?"
  - "What is the difference between a remote call and a local call?"
---

# Quick Definition

A remote call invokes a function in another module, qualifying the function name with the module name and a colon, as in `lists:reverse([1,2,3])`. A local call invokes a function in the same module.

# Core Definition

"When you want to call a function that resides in some other module, you need to qualify the function name with the name of the module it's in, using a colon character as separator" (Chapter 2, section 2.3.1). For example, `lists:reverse([1,2,3])` calls `reverse` in the standard library module `lists`. "This form is called a *remote call* (calls a function in a different module), as opposed to a *local call* (calls a function in the same module)." The book warns this should not be confused with a *remote procedure call* — a distributed-programming concept of asking another process or computer to run a function, which is a completely different thing.

# Prerequisites

- **Erlang module** — a remote call names a module.
- **Erlang function** — a remote call invokes a function.

# Key Properties

1. A remote call qualifies the function name with `Module:` using a colon.
2. It calls a function in a *different* module than the caller.
3. A local call invokes a function in the *same* module — no qualification.
4. A remote call is not the same as a remote procedure call.

# Construction / Recognition

## To Construct/Create:
1. Write the module name, a colon, the function name, and the arguments.
2. Example: `lists:reverse([1,2,3])`.
3. For a function in the same module, omit the `Module:` prefix.

# Context & Application

- **Typical contexts**: Calling standard-library functions and functions in other modules.
- **Common applications**: Using `lists`, `io`, `math`, and other library modules.
- **Historical/stylistic notes**: Some functions in the auto-imported `erlang` module (such as `self()` and `spawn(...)`) can be called without the `erlang:` prefix.

# Examples

**Example 1** (section 2.3.1): `lists:reverse([1,2,3])` is a remote call to the `reverse` function in the `lists` standard-library module.

**Example 2** (section 2.3.3): `self()` is really a remote call to `erlang:self()`, but because `erlang` functions are auto-imported the prefix can be omitted.

# Relationships

## Builds Upon
- **Erlang module** and **Erlang function** — a remote call names both.

## Enables
- Reuse of functions across module boundaries, including the standard library.

## Related
- **Function arity** — exactly identifying a function still needs its arity.
- **Built-in function** — many BIFs are auto-imported and need no module prefix.

## Contrasts With
- None noted in this source (local call is the complementary form, covered here).

# Common Errors

- **Error**: Calling another module's function without the `Module:` prefix.
  **Correction**: Cross-module calls require qualification with the module name and a colon.

# Common Confusions

- **Confusion**: Confusing a remote call with a remote procedure call.
  **Clarification**: A remote call is just a cross-module call within one runtime; a remote procedure call is a distributed-programming concept of running a function on another process or computer.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.1 "Calling functions in other modules (remote calls)."

# Verification Notes

- Definition source: Direct adaptation from section 2.3.1.
- Confidence rationale: HIGH — remote and local calls are explicitly defined and distinguished.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
