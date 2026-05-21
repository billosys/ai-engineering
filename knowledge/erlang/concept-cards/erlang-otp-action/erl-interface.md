---
# === CORE IDENTIFICATION ===
concept: Erl_Interface (ei) Library
slug: erl-interface

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
section: "12.2.2. The C side of the port"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ei library
  - Erl_Interface
  - ei

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
  - external-term-format
extends: []
related:
  - port-message-passing
  - linked-in-driver
contrasts_with:
  - erl-nif-api

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erl_Interface (ei) library?"
  - "How does C code decode and encode Erlang terms?"
  - "What is an ei_x_buff?"
---

# Quick Definition

Erl_Interface (the `ei` library) is a C library, shipped with Erlang/OTP, for decoding and encoding Erlang terms in the external term format on the foreign side of a port.

# Core Definition

The Erl_Interface `ei` C library provides support functions for passing complex data between Erlang and C code over a port. It helps you decode and encode serialized Erlang terms in the *external term format* — the same format used by `erlang:term_to_binary/1` and the Erlang distribution protocol. The `ei` decoding functions use an index variable that is advanced as each decode succeeds; encoding is done into an `ei_x_buff`, a dynamic buffer that automatically manages memory for the term being built. Using `ei` is more heavyweight than a hand-rolled byte protocol but lets C code work with Erlang terms on both sides ("Erlang and OTP in Action," Ch. 12, Sections 12.1.1 and 12.2.2).

# Prerequisites

- **Port** — `ei` is used on the C side of a port.
- **External term format** — `ei` decodes and encodes this format.

# Key Properties

1. A C library included with Erlang/OTP for handling serialized Erlang terms.
2. Works with the external term format used by `term_to_binary/1` and Erlang distribution.
3. Decoding functions advance an index variable into the input buffer as each step succeeds; `ei_decode_version` must be called first.
4. `ei_get_type` inspects a term's type and size without advancing the index.
5. `ei_x_buff` is a dynamic output buffer; `ei_x_new_with_version` allocates it and inserts the version byte.
6. `ei_x_encode_*` functions build terms with automatic memory management; `ei_encode_*` functions leave memory management to the caller (used for back-patching).
7. An alternative to `ei` is a simple hand-coded byte protocol when no structured terms are exchanged.

# Construction / Recognition

## To Construct/Create:
1. `#include` the `ei.h` header on the C side.
2. Initialize an `ei_x_buff` output buffer with `ei_x_new_with_version`.
3. Decode input starting with `ei_decode_version`, then inspect with `ei_get_type` and decode specific terms.
4. Encode results with `ei_x_encode_tuple_header`, `ei_x_encode_atom`, `ei_x_encode_binary`, etc.
5. Link with the `ei` library (`-lei_st`) when compiling the C program.

## To Identify/Recognize:
1. C code including `ei.h` and calling `ei_x_*` / `ei_decode_*` / `ei_encode_*` functions.

# Context & Application

- **Typical contexts**: The C side of a port that exchanges structured Erlang data.
- **Common applications**: `jp_prog` decodes the JSON-text binary sent from Erlang and encodes the parsed result as `{ok, ...}` / `{error, ...}` tuples.
- **Historical/stylistic notes**: For plain text or raw byte chunks you can skip `ei` and do encoding/decoding yourself; `ei` is for complex terms.

# Examples

**Example 1** (Section 12.2.2): `ei_x_new_with_version` allocates a dynamic buffer and inserts the external-term-format version byte; `ei_decode_version` reads it back from the input.

**Example 2** (Section 12.2.2): To build `{ok, Result}`, the C code calls `ei_x_encode_tuple_header` for a 2-tuple, then `ei_x_encode_atom` for `ok`, leaving the next encoded term as the second element.

# Relationships

## Builds Upon
- **External term format** — `ei` reads and writes this serialization.

## Related
- **Port message-passing protocol** — `ei` processes the `Data` carried by port messages.
- **Linked-in driver** — A driver using `ei` is linked with `-lei_st`.

## Contrasts With
- **erl_nif API** — NIFs use the `erl_nif` API for terms, not `ei` and the external term format.

# Common Errors

- **Error**: Decoding input without first calling `ei_decode_version`.
  **Correction**: The external term format begins with a version byte — decode it first with `ei_decode_version`.

- **Error**: Confusing `ei_encode_*` with `ei_x_encode_*`.
  **Correction**: `ei_x_encode_*` manage memory automatically; `ei_encode_*` leave memory to you and are used for back-patching headers.

# Common Confusions

- **Confusion**: Thinking you must understand the byte-level external term format to use `ei`.
  **Clarification**: The `ei` library handles the byte-level details; you work with decode/encode calls.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Sections 12.1.1 "Plain ports," 12.2.2 "The C side of the port" — subsections "Data structures" and "Decoding and encoding Erlang terms with ei." See Figure 12.3.

# Verification Notes

- Definition source: Direct adaptation of Section 12.2.2.
- Confidence rationale: HIGH — the book describes the `ei` library and its key functions in detail.
- Uncertainties: None.
- Cross-reference status: `external-term-format` and `erl-nif-api` referenced; `port` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
