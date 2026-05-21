---
# === CORE IDENTIFICATION ===
concept: erl_nif API
slug: erl-nif-api

# === CLASSIFICATION ===
category: tooling
subcategory: interoperability
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.4. Implementing the parser as a NIF"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - erl_nif library
  - erl_nif.h

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nif
extends: []
related:
  - nif-implementation-function
  - nif-memory-management
contrasts_with:
  - erl-interface

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the erl_nif API?"
  - "How does the erl_nif API differ from the ei library?"
  - "What header and functions does NIF C code use?"
---

# Quick Definition

The `erl_nif` API is the C library for writing NIFs — it has its own functions for passing data between Erlang and C and, unlike the `ei` library, does not use the external term format.

# Core Definition

NIFs are based on a C API using a few callbacks, but on the Erlang side they look like normal functions and do not involve ports. The `erl_nif` API has its own functions for passing data structures between Erlang and C and does not use the external term format; this means much less code can be shared between a NIF implementation and a port driver. NIF C code includes the `erl_nif.h` header. The API provides `ErlNifEnv` (an environment handle), `ERL_NIF_TERM` (the Erlang-term type), `enif_*` functions for allocation and term construction/inspection, the `ErlNifFunc` registration array, and the `ERL_NIF_INIT` macro ("Erlang and OTP in Action," Ch. 12, Sections 12.4 and 12.4.2).

# Prerequisites

- **NIF** — The `erl_nif` API is the toolkit for implementing NIFs.

# Key Properties

1. The C library for implementing NIFs; code includes `erl_nif.h`.
2. Has its own data-passing functions; does not use the external term format.
3. `ErlNifEnv` is an environment handle passed to NIF functions and required by most `erl_nif` calls.
4. `ERL_NIF_TERM` is the C type representing an Erlang term.
5. `enif_*` functions cover allocation (`enif_alloc`), inspection (`enif_inspect_binary`), and construction (`enif_make_*`).
6. `ErlNifFunc` array plus `ERL_NIF_INIT` macro register NIFs with the VM.
7. Documented in the ERTS Reference Manual; the API was finalized in OTP R14 (the book describes R13).
8. Because it differs from `ei`, little code is shared between a NIF and a port-driver implementation.

# Construction / Recognition

## To Construct/Create:
This is a standard library API; you use it by including `erl_nif.h` and calling its functions. There is nothing to create.

## To Identify/Recognize:
1. C code including `erl_nif.h` and using `ErlNifEnv`, `ERL_NIF_TERM`, `enif_*`, `ErlNifFunc`, `ERL_NIF_INIT`.

# Context & Application

- **Typical contexts**: Implementing the C side of a NIF.
- **Common applications**: The NIF JSON parser is built entirely on `erl_nif`, requiring no `erl_interface` linking.
- **Historical/stylistic notes**: In R14 the `enif_alloc` functions no longer take an `ErlNifEnv` pointer; removing that argument makes R13 code work under R14.

# Examples

**Example 1** (Section 12.4): "The `erl_nif` API has its own functions for passing data structures between Erlang and C and doesn't use the external term format."

**Example 2** (Section 12.4.3): Compiling a NIF library does not require including or linking with `erl_interface`, unlike the port and driver versions.

# Relationships

## Builds Upon
- **NIF** — `erl_nif` is the API used to implement NIFs.

## Enables
- **NIF implementation function** — Written against the `erl_nif` API.
- **NIF memory management** — Uses `erl_nif`'s `enif_*` functions.

## Contrasts With
- **Erl_Interface (ei) library** — `ei` decodes/encodes the external term format for ports; `erl_nif` has its own term API and does not use that format.

# Common Errors

- **Error**: Linking NIF code with `erl_interface`.
  **Correction**: A NIF needs only `erl_nif`; do not include or link `erl_interface`.

# Common Confusions

- **Confusion**: Thinking NIF code can reuse port-driver `ei` code directly.
  **Clarification**: `erl_nif` works differently from `ei`; little code is shared between the two implementations.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Sections 12.4 "Implementing the parser as a NIF" and 12.4.2 "The C side of the NIF."

# Verification Notes

- Definition source: Direct adaptation of Sections 12.4 and 12.4.2.
- Confidence rationale: HIGH — the book explicitly describes the `erl_nif` API and contrasts it with `ei`.
- Uncertainties: The book describes the R13 API; R14 finalized it.
- Cross-reference status: `nif` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
