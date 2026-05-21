---
# === CORE IDENTIFICATION ===
concept: Native Implemented Function
slug: native-implemented-function

# === CLASSIFICATION ===
category: performance
subcategory: native-code
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Scaling with Native Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - NIF
  - NIFs
  - native implemented functions

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - scalability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a native implemented function (NIF)?"
  - "How do I call non-Erlang code from Erlang?"
---

# Quick Definition

A native implemented function (NIF) is a function callable from Erlang but implemented in C or C++, executing directly within the Erlang runtime for performance or library reuse.

# Core Definition

"Erlang/OTP provides support for calling non-Erlang functions, termed native implemented functions (NIFs), directly from Erlang code ... To other Erlang functions, NIFs look like regular Erlang functions. They accept regular Erlang terms as arguments and return regular terms as well, but under the covers these functions are implemented in a different language, typically C or C++. However, they execute directly within the Erlang runtime. When the runtime loads an Erlang module containing NIFs, it loads along with it a shared library containing the native function implementations, and then patches the module's BEAM code with instructions that invoke the native functions instead" (Cesarini & Vinoski, p. 427).

# Prerequisites

This is a foundational/advanced concept with no prerequisites within chapters 12-15. It assumes general Erlang knowledge from earlier chapters but introduces NIFs afresh here.

# Key Properties

1. A function callable from Erlang but implemented in a different language, typically C or C++.
2. Looks like a regular Erlang function — accepts and returns regular Erlang terms.
3. Executes directly within the Erlang runtime, on the runtime's scheduler threads.
4. Loaded as a shared library; the runtime patches the module's BEAM code to invoke it.
5. Has a C API to access/create terms, send messages, raise exceptions, and schedule other NIFs.
6. A crashing NIF takes down the entire VM; a NIF running longer than 1-2 ms hogs a scheduler thread.

# Construction / Recognition

## To Construct/Create:
1. Implement the function in C or C++ using the `erl_nif` C API.
2. Build it into a shared library.
3. Load it from the Erlang module; the runtime patches the BEAM code to call the native code.
4. Keep NIFs fast, or break work into chunks via `enif_schedule_nif()`, or use dirty schedulers.

## To Identify/Recognize:
1. Recognize a NIF as an Erlang-callable function backed by a loaded native shared library.

# Context & Application

- **Typical contexts**: Performance-critical code, or reuse of existing C/C++ libraries.
- **Common applications**: Database drivers, JSON parsers, special-purpose web clients/servers; parts of the lists, maps, ets, and crypto standard modules are NIFs.
- **Historical/stylistic notes**: "Forget the 'let it crash' philosophy if you're writing a NIF" — a NIF crash takes down the VM (p. 427). Dirty schedulers were experimental in Erlang 17/18, off by default.

# Examples

**Example 1** (p. 427): Some parts of Erlang/OTP itself are written as NIFs — portions of the lists, maps, ets, and crypto standard modules.

**Example 2** (pp. 427-428): A NIF running for more than 1-2 milliseconds hogs a VM scheduler thread; over time this can lead to "scheduler collapse," where schedulers wrongly go to sleep, leaving one to handle the entire workload.

# Relationships

## Builds Upon
- This is a foundational concept within chapters 12-15; it builds on general Erlang knowledge.

## Enables
- NIFs enable performance-critical native code and reuse of existing C/C++ libraries.

## Related
- **Scalability** — NIFs are presented as a scaling-with-native-code technique

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Writing a long-running NIF
  **Correction**: Keep NIFs under 1-2 ms; break work into chunks with `enif_schedule_nif()`, or run them on dirty schedulers, to avoid hogging scheduler threads and scheduler collapse.

# Common Confusions

- **Confusion**: A crashing NIF behaves like a crashing Erlang process.
  **Clarification**: NIFs run on the runtime's scheduler threads — a crashing NIF takes the entire VM down, so "let it crash" does not apply.

# Source Reference

Chapter 14: Scaling Out, "Scaling with Native Code," pages 426-428. See the `erl_nif` manual page.

# Verification Notes

- Definition source: Direct quote from p. 427.
- Confidence rationale: HIGH — the source dedicates a named section to NIFs with an explicit definition and caveats.
- Uncertainties: Dirty-scheduler status stated as of Erlang 17/18.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
