---
# === CORE IDENTIFICATION ===
concept: Length-Prefixed Packet Protocol
slug: length-prefixed-packet-protocol

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
  - "{packet, 4} protocol"
  - packet header protocol

# === TYPED RELATIONSHIPS ===
prerequisites:
  - open-port
  - port-message-passing
extends: []
related:
  - port
  - external-term-format
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the {packet, N} option frame data over a port?"
  - "Why must packet headers be in network byte order?"
  - "How does C code read a length-prefixed packet?"
---

# Quick Definition

The length-prefixed packet protocol frames each chunk of port data with an N-byte big-endian length header, so the receiving side knows exactly how many bytes to read.

# Core Definition

When a port is opened with the `{packet, N}` option, Erlang puts an N-byte integer (1, 2, or 4 bytes) at the head of each chunk of data, specifying the number of bytes that follow. The packet header bytes are always in network byte order (big-endian), regardless of platform. This convention makes reading and writing on the C side straightforward: once the length is known, the rest of the data can be read in a single operation, and writing back requires first emitting a properly formed length header. The C code provides `write_packet` (prefixes output with a 4-byte network-order header), `read_bytes` (reads up to *max* bytes), and `read_packet` (reads an entire length-prefixed packet) ("Erlang and OTP in Action," Ch. 12, Sections 12.2.1 and 12.2.2).

# Prerequisites

- **open_port BIF** — `{packet, N}` is an option to `open_port/2`.
- **Port message-passing protocol** — Framing applies to the data carried in port messages.

# Key Properties

1. Enabled by the `{packet, N}` option, with N being 1, 2, or 4 bytes.
2. Each data chunk is prefixed with an N-byte integer giving the length of what follows.
3. Headers are always network byte order (big-endian), independent of platform.
4. The same N is used in both directions.
5. The known length lets the receiver read the rest of a packet in a single, fast operation.
6. On the C side: `write_packet` adds the header on output; `read_packet` reads a full framed packet.
7. The `{packet, N}` option is not used for linked-in drivers — the `erl_driver` API supplies the size directly.

# Construction / Recognition

## To Construct/Create:
1. Open the port with `{packet, N}` (e.g., `{packet, 4}`).
2. On the C side, write a `write_packet` that emits an N-byte big-endian length then the data.
3. Write a `read_packet` that reads the N-byte header, decodes it endianness-independently, then reads that many bytes.
4. Exit with a nonzero status if reading or writing fails (desynchronization).

## To Identify/Recognize:
1. A port opened with `{packet, N}`, and C code reading/writing a fixed-size big-endian length header.

# Context & Application

- **Typical contexts**: Framing variable-length messages between Erlang and an external port program.
- **Common applications**: The `jp_prog` JSON parser uses `{packet, 4}` to frame requests and replies.
- **Historical/stylistic notes**: If the protocol desynchronizes, it is better to exit with a nonzero status and let Erlang restart the program.

# Examples

**Example 1** (Section 12.2.1): The port is opened with `[binary, {packet, 4}, exit_status]`, so each chunk is prefixed with a 4-byte length.

**Example 2** (Section 12.2.2): `write_packet` outputs bytes prefixed with a 4-byte network-order length header; `read_packet` reads an entire length-prefixed data packet; the `main` loop reads one packet at a time and processes it.

# Relationships

## Builds Upon
- **open_port BIF** — `{packet, N}` is supplied as a port option.
- **Port message-passing protocol** — Framing structures the `Data` exchanged.

## Related
- **Port** — The protocol frames data flowing through a port.
- **External term format** — The framed payload is often a term in external format.

# Common Errors

- **Error**: Reading the 4-byte header straight into a `uint32_t` and assuming it works.
  **Correction**: Headers are big-endian; decode them endianness-independently regardless of platform.

- **Error**: Using `{packet, N}` with a linked-in driver.
  **Correction**: Drop `{packet, N}` for linked-in drivers — `erl_driver` already provides the data size.

# Common Confusions

- **Confusion**: Thinking the header byte order depends on the host platform.
  **Clarification**: Packet headers are always network byte order (big-endian), independent of the platform.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Sections 12.2.1 and 12.2.2 — subsection "Reading and writing data" and sidebar "Network endianism alert." See Listings 12.2 and 12.5.

# Verification Notes

- Definition source: Direct adaptation of Sections 12.2.1 and 12.2.2.
- Confidence rationale: HIGH — the book explicitly describes the packet framing and the endianness requirement.
- Uncertainties: Listing 12.2 appears as an image; function behavior described from surrounding prose.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
