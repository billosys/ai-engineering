---
# === CORE IDENTIFICATION ===
concept: External Term Format
slug: external-term-format

# === CLASSIFICATION ===
category: data-types
subcategory: serialization
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.2.1. The Erlang side of the port"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "term_to_binary"
  - "binary_to_term"
  - Erlang external transport format

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
extends: []
related:
  - erl-interface
  - port-message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the external term format?"
  - "How do you serialize an Erlang term to send it over a port?"
  - "Why does the external term format begin with a version byte?"
---

# Quick Definition

The external term format is Erlang's standard binary serialization for terms — produced by `term_to_binary/1`, read by `binary_to_term/1`, and shared with the Erlang distribution protocol.

# Core Definition

The *external term format* is the serialization used by `erlang:term_to_binary/1` to turn an Erlang term into binary data; it is the same format used in the Erlang distribution protocol. On the Erlang side of a port, `term_to_binary(Msg)` encodes any Erlang term as binary data in this format for sending to foreign code, and `binary_to_term/1` transforms incoming data in the same format back into an Erlang term. The format requires a version number as the first byte of the data chunk, allowing different nodes and clients to be sure they are exchanging data in a compatible way; the exact byte-level representation is documented in the ERTS User's Guide, but the `ei` library handles the details ("Erlang and OTP in Action," Ch. 12, Sections 12.2.1 and 12.2.2).

# Prerequisites

- **Port** — The format is used to marshal data sent over a port.

# Key Properties

1. Erlang's standard binary serialization for arbitrary terms.
2. Produced by `erlang:term_to_binary/1`; consumed by `binary_to_term/1`.
3. The same format the Erlang distribution protocol uses.
4. Begins with a version byte so peers can confirm compatible encodings.
5. Can serialize any Erlang term — atoms, numbers, tuples, lists, binaries, etc.
6. On the C side, the `ei` library decodes and encodes this format; you need not know the byte layout.
7. A binary term is encoded as 1 type byte (109) plus 4 size bytes followed by the data.

# Construction / Recognition

## To Construct/Create:
1. On the Erlang side, call `term_to_binary(Term)` to serialize.
2. Send the result over a port; on receipt call `binary_to_term(Data)` to deserialize.
3. On the C side, use `ei` functions, which insert/check the version byte automatically.

## To Identify/Recognize:
1. A binary whose first byte is the external-term-format version, processed by `term_to_binary`/`binary_to_term` or `ei`.

# Context & Application

- **Typical contexts**: Marshalling structured Erlang data across a port boundary.
- **Common applications**: `jp_server` sends `term_to_binary(Msg)` to `jp_prog` and decodes the reply with `binary_to_term`.
- **Historical/stylistic notes**: NIFs use the `erl_nif` API instead and do not use the external term format.

# Examples

**Example 1** (Section 12.2.1): `Port ! {self(),{command, term_to_binary(Msg)}}` sends any Erlang term in external format; the reply is decoded with `binary_to_term(Data)`.

**Example 2** (Section 12.2.2, Figure 12.3): A binary term in the input buffer is encoded as 1 type byte (109) plus 4 size bytes, then the actual data starting at `buf[index+5]`.

# Relationships

## Builds Upon
- **Port** — The format marshals data carried over ports.

## Related
- **Erl_Interface (ei) library** — Decodes and encodes the external term format on the C side.
- **Port message-passing protocol** — The `Data` exchanged is often in this format.

# Common Errors

- **Error**: Reading external-format data without checking the version byte.
  **Correction**: Decode the version byte first (`ei_decode_version` in C) to confirm compatibility.

# Common Confusions

- **Confusion**: Thinking NIFs also use the external term format.
  **Clarification**: NIFs use the `erl_nif` API's own term functions and do not use the external term format.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Sections 12.2.1 "The Erlang side of the port" and 12.2.2 "The C side of the port." See Figure 12.3.

# Verification Notes

- Definition source: Direct adaptation of Sections 12.2.1 and 12.2.2.
- Confidence rationale: HIGH — the book explicitly describes the external term format and its version byte.
- Uncertainties: None.
- Cross-reference status: `port` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
