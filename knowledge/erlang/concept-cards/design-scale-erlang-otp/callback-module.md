---
# === CORE IDENTIFICATION ===
concept: Callback Module
slug: callback-module

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: behavior-concept
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Behaviors"
chapter_number: 2
pdf_page: 72
section: "Callback Modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - behavior module
  - callback function
  - callback API

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generic-vs-specific-code
extends: []
related:
  - otp-behaviors
  - gen-server
  - behavior-directive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a callback module?"
  - "How does a behavior relate to its callback module?"
  - "What is a callback function?"
---

# Quick Definition

A callback module holds the specific code for one process implementation, exporting callback functions that the generic behavior module invokes. The behavior and callback modules form a contract.

# Core Definition

"The idea behind OTP behaviors is to split up the code into two modules: one for the generic pattern, referred to as the behavior module, and one for specifics, referred to as the callback module" (Cesarini & Vinoski, p. 57). "The generic behavior module can be seen as the driver. While it doesn't know anything about what the callback module does, it is aware of a set of exported callback functions it has to invoke and the format of their return values. The callback module isn't aware of what the generic module does either; it only complies with the format of the data it has to return" (p. 57). "Another way of explaining this is as a contract between the behavior and callback modules. They have to agree on a set of names and types for the functions in the callback API and respect the return values."

# Prerequisites

- **Generic versus specific code** — The callback module is precisely where the specific code lives, once generic code is extracted.

# Key Properties

1. The behavior module is the generic driver; the callback module holds the specifics.
2. The callback module exports callback functions with agreed names, arities, and return types.
3. The behavior module knows which callbacks to invoke and the format of their return values.
4. Neither module knows the other's internals — they agree only on the callback API contract.
5. The behavior module is supplied by OTP; the callback module is written by the developer.
6. Behavior and callback functions execute within the scope of the same server process.

# Construction / Recognition

## To Construct:
1. Choose a behavior; note its required callback functions and their return-value formats.
2. Write a module exporting those callbacks with the specified arities.
3. Implement each callback to return data in the required format.

## To Recognize:
1. A module exporting `init`, `handle_*`, and `terminate` style functions, declared with a `-behavior` directive.

# Context & Application

- **Typical contexts**: Every OTP behavior usage — each behavior instance has a callback module.
- **Common applications**: The `frequency` module is the callback module for the `server` behavior (Ch. 2) and later for `gen_server` (Ch. 3).
- **Historical/stylistic notes**: The contract framing makes the division of responsibilities explicit and enables tooling such as `dialyzer` checks.

# Examples

**Example 1** (pp. 66-67): The `frequency` callback module exports `init/1`, `terminate/1`, and `handle/2`; the generic `server` module calls `Mod:init/1`, `Mod:handle/2`, and `Mod:terminate/1`.

**Example 2** (p. 67): `init/1` "is required to return the initial process state" — an example of a callback whose return-value format is dictated by the contract.

# Relationships

## Builds Upon
- **Generic versus specific code** — The callback module is the home of the specific code.

## Enables
- **Gen_server** — A `gen_server` is driven by a developer-written callback module.
- **Behavior directive** — A callback module declares which behavior it implements.

## Related
- **OTP behaviors** — The generic counterpart of the callback module.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Returning data from a callback in a format the behavior does not expect.
  **Correction**: Respect the callback API contract — return exactly the tuple formats the behavior requires.

# Common Confusions

- **Confusion**: Thinking the callback module and behavior module know each other's logic.
  **Clarification**: They share no knowledge of internals; they agree only on a set of callback names, types, and return formats.

# Source Reference

Chapter 2: Behaviors, Section "Callback Modules," pages 57-58. See Figure 3-3 (the callback module).

# Verification Notes

- Definition source: Direct quotes from p. 57.
- Confidence rationale: HIGH — explicit definition framed as a contract.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
