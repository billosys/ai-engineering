---
# === CORE IDENTIFICATION ===
concept: Defining a Custom Behaviour
slug: custom-behaviour

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: custom-behaviours
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding an HTTP interface to the cache"
chapter_number: 11
pdf_page: null
section: "11.2.2. Implementing a generic web server behaviour"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - behaviour_info/1
  - custom OTP behaviour

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
extends:
  - otp-behaviour
related:
  - gen-web-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you define your own OTP behaviour?"
  - "What is the behaviour_info/1 function?"
  - "How does the compiler check a -behaviour declaration?"
---

# Quick Definition

A custom behaviour is defined by writing a module named after the behaviour that exports `behaviour_info/1`, which returns the list of callback function name/arity pairs implementations must provide.

# Core Definition

When the compiler sees a `-behaviour(X)` declaration, it calls the module named `X` to find out what the interface should look like — specifically `X:behaviour_info(callbacks)` — to get the list of callback functions an implementation module should export. This means a behaviour's name must equal the name of the module that defines its interface. That module must export a `behaviour_info/1` function whose argument is an atom; for the atom `callbacks` it returns a list of function name/arity pairs naming the required callbacks, and for any other input it returns `undefined`. This information lets the compiler warn you if an implementation module fails to export an expected callback ("Erlang and OTP in Action," Ch. 11, Section 11.2.2).

# Prerequisites

- **OTP behaviour** — A custom behaviour is a new instance of the general behaviour mechanism.

# Key Properties

1. The behaviour name must equal the name of the module defining its interface.
2. That module exports `behaviour_info/1`.
3. `behaviour_info(callbacks)` returns a list of `{Function, Arity}` pairs.
4. For any argument other than `callbacks`, `behaviour_info/1` returns `undefined`.
5. The compiler uses this list to warn about missing callbacks in implementation modules.
6. A behaviour has three parts: the container (reusable code), the interface (the callback contract), and the implementation (the callback module).

# Construction / Recognition

## To Construct/Create:
1. Create a module whose name is the behaviour name (e.g., `gen_web_server`).
2. Export and implement `behaviour_info/1`.
3. Have `behaviour_info(callbacks)` return the `{Name, Arity}` pairs of required callbacks; return `undefined` otherwise.
4. Implement the container code and the API (interface) in that module or its supporting modules.

## To Identify/Recognize:
1. A module exporting `behaviour_info/1`, referenced by `-behaviour(...)` declarations in other modules.

# Context & Application

- **Typical contexts**: Building a reusable framework that several modules will plug into.
- **Common applications**: The `gen_web_server` behaviour defined in this chapter.
- **Historical/stylistic notes**: Previously the reader only implemented existing behaviours; here a new behaviour with potentially many implementations is created.

# Examples

**Example 1** (Section 11.2.2): `gen_server:behaviour_info(callbacks)` returns `[{init,1},{handle_call,3},{handle_cast,2},{handle_info,2},{terminate,2},{code_change,3}]`.

**Example 2** (Listing 11.5): The `gen_web_server` module contains a `behaviour_info/1` function returning a list of nine callbacks (`init/1` plus one per HTTP method).

# Relationships

## Builds Upon
- **OTP behaviour** — A custom behaviour reuses the standard behaviour machinery.

## Enables
- **gen_web_server** — A concrete custom behaviour defined this way.

# Common Errors

- **Error**: Naming the behaviour differently from the module that defines its interface.
  **Correction**: The behaviour name and the interface-defining module name must be identical.

- **Error**: Returning something other than `undefined` for non-`callbacks` arguments to `behaviour_info/1`.
  **Correction**: Return `undefined` for any argument other than `callbacks`.

# Common Confusions

- **Confusion**: Thinking defining a behaviour enforces callbacks at runtime.
  **Clarification**: `behaviour_info/1` gives the compiler information for compile-time warnings; it does not itself enforce anything at runtime.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.2.2, subsection "The gen_web_server module: defining a custom behaviour."

# Verification Notes

- Definition source: Direct adaptation of the "defining a custom behaviour" subsection.
- Confidence rationale: HIGH — the book explicitly explains how to define a behaviour with `behaviour_info/1`.
- Uncertainties: The book describes the R13-era `behaviour_info/1` mechanism; modern OTP also supports `-callback` attributes (not covered here).
- Cross-reference status: `otp-behaviour` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
