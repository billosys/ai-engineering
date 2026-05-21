---
# === CORE IDENTIFICATION ===
concept: Port Protocol
slug: port-protocol

# === CLASSIFICATION ===
category: tooling
subcategory: interfacing
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Interfacing Techniques"
chapter_number: 15
pdf_page: null
section: "Interfacing an External C Program with a Port"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "byte-stream protocol"
  - "packet protocol"
  - "encode/decode protocol"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
  - port-program
extends: []
related:
  - binary
  - linked-in-driver
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is data framed between Erlang and a port program?"
  - "What protocol does Erlang use to talk to external programs?"
  - "How do I encode function calls for a port?"
---

# Quick Definition

The port protocol is the agreed byte-stream convention that both the Erlang side and the external port program must follow — typically a length-prefixed packet plus an application-specific encoding of calls and results.

# Core Definition

To call external routines, function calls must be turned into sequences of bytes sent to the external program through the port (Chapter 15, "Interfacing an External C Program with a Port"). The port adds a length count to the byte sequence and sends it to the external program; the external program replies, and the port delivers the result to the connected process. The protocol used in the book's example is: all packets start with a 2-byte length code (`Len`) followed by `Len` bytes of data — this header is added automatically by the port when opened with `{packet, 2}`; the call `sum(N, M)` is encoded as the byte sequence `[1, N, M]`; the call `twice(N)` as `[2, N]`; arguments and return values are assumed to be a single byte. Both the external program and the Erlang program must follow this protocol. On the Erlang side this is implemented by `encode/1` and `decode/1` functions.

# Prerequisites

- **Port** — The protocol is the data convention carried over a port.
- **Port program** — The external program must implement the same protocol.

# Key Properties

1. Both ends — Erlang and the external program — must follow the identical protocol.
2. The `{packet, N}` port option auto-frames data with an N-byte length header (N is 1, 2, or 4).
3. Above the framing, an application-specific encoding maps calls and results to bytes.
4. In the book's example, `sum(N, M)` -> `[1, N, M]`, `twice(N)` -> `[2, N]`.
5. The port adds the length header outbound and removes it inbound.

# Construction / Recognition

## To Define a Port Protocol:
1. Choose a `{packet, N}` framing so the port handles length headers automatically.
2. Define an encoding of each call into a byte sequence (e.g. a tag byte plus arguments).
3. Implement matching `encode`/`decode` on the Erlang side and equivalent logic in the port program.

## To Recognize It:
1. Look for `encode/1` and `decode/1` functions paired with port communication.
2. Look for `{packet, N}` options and tag-byte conventions.

# Context & Application

- **Typical contexts**: Any port-based interface between Erlang and a foreign program.
- **Common applications**: The `example1` C interface; the same protocol is used by linked-in drivers.
- **Historical/stylistic notes**: The protocol the example implements is "the principal way in which Erlang communicates with the external world."

# Examples

**Example 1** (Chapter 15, "Interfacing an External C Program with a Port"): Calling `example1:sum(12,23)` encodes to `[1,12,23]`; the port adds the 2-byte header, sending `0,3,1,12,23`; the C program replies `0,1,35`; the port strips the header and delivers `{Port, {data, [35]}}`.

**Example 2** (Chapter 15, "The Erlang Program"): The Erlang side implements `encode({sum, X, Y}) -> [1, X, Y]; encode({twice, X}) -> [2, X].` and `decode([Int]) -> Int.`

# Relationships

## Builds Upon
- **Port** and **port program** — the protocol is the contract between the two.

## Enables
- Reliable structured communication with external programs.

## Related
- **Binary** — packets and length headers are naturally handled as binaries/I/O lists.
- **Linked-in driver** — obeys the same protocol as port drivers.

## Contrasts With
- A protocol convention; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Implementing different framing on the two ends (e.g. `{packet, 2}` in Erlang, 1-byte header in C).
  **Correction**: The length-header size must match exactly on both ends.
- **Error**: Assuming multi-byte arguments when the protocol defines single-byte values.
  **Correction**: Define and respect the agreed argument width on both sides.

# Common Confusions

- **Confusion**: The application must add the length header itself.
  **Clarification**: With `{packet, N}` the port adds and strips the header automatically; the application only encodes the payload.
- **Confusion**: The protocol is fixed by Erlang.
  **Clarification**: Only the framing is provided by `{packet, N}`; the call/result encoding above it is application-defined.

# Source Reference

Chapter 15: Interfacing Techniques, section "Interfacing an External C Program with a Port" (the protocol description and the five-step data flow) and "The Erlang Program" (the `encode`/`decode` functions).

# Verification Notes

- Definition source: Direct adaptation of the protocol description and the `encode`/`decode` code.
- Confidence rationale: HIGH — the protocol and a worked encoding example are explicitly given.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `binary` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
