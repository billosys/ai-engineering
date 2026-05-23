---
# === CORE IDENTIFICATION ===
concept: External Term Format
slug: external-term-format

# === CLASSIFICATION ===
category: distribution
subcategory: encoding
tier: intermediate

# === PROVENANCE ===
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "External Term Format"
chapter_number: null
pdf_page: null
section: "Introduction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Erlang external format"
  - "binary term format"
  - "ETF"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - distribution-header
  - distribution-protocol
  - distribution-connection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the external term format?"
  - "How does the external term format relate to distribution?"
  - "How does Erlang serialize terms for distribution?"
---

# Quick Definition

The external term format is the binary encoding used to represent Erlang terms outside the runtime system. It is the standard serialization format used by the distribution mechanism for sending terms between nodes and by `erlang:term_to_binary/1,2` and `erlang:binary_to_term/1` for explicit serialization.

# Core Definition

The ERTS documentation states: "The external term format is mainly used in the distribution mechanism of Erlang." Because Erlang has a fixed number of types, there is no need for programmers to define an external format specification for applications -- all Erlang terms have an external representation and the interpretation is application-specific. The distribution uses this format implicitly when sending messages across node boundaries.

The overall format begins with a version byte (131), followed by a one-byte tag identifying the term type, then the type-specific data. Compressed terms use tag 80 with a 4-byte uncompressed size followed by zlib-compressed data. When used with a distribution header, the leading version byte (131) is omitted since it is implied by the header.

# Prerequisites

None -- this is a foundational encoding concept for understanding Erlang distribution.

# Key Properties

1. Every term starts with version byte `131`, a 1-byte `Tag`, then `Data`
2. Each Erlang type has its own tag: atoms (118/119), integers (97/98), tuples (104/105), lists (108), binaries (109), pids (88), ports (89/120), references (90), maps (116), funs (112/113), and more
3. Compressed format uses tag `80` with a 4-byte uncompressed size followed by zlib-compressed data
4. Atoms sent over distribution are always encoded in UTF-8 (since ERTS 9.0 / OTP 20)
5. The maximum number of allowed characters in an atom is 255; each UTF-8 character can need up to 4 bytes
6. The version byte is omitted when terms follow a distribution header
7. Multi-byte integers are in big-endian order

# Construction / Recognition

## To Construct/Create:
1. Call `erlang:term_to_binary/1` or `erlang:term_to_binary/2` to convert any Erlang term to its external binary representation
2. Call `erlang:term_to_iovec/1,2` to get the same encoding as an I/O vector (avoids copying)
3. The distribution does this implicitly when sending messages across node boundaries

## To Identify/Recognize:
1. A binary beginning with byte `131` is in external term format
2. The second byte is a tag identifying the term type

# Context & Application

The external term format is the foundation of all inter-node communication in Erlang. Every message, signal, and control message sent between distributed nodes is encoded using this format. It is also used for persistent storage of terms (e.g., DETS, disk_log) and for communication with external programs via ports and NIFs. Understanding the format is essential when implementing alternative distribution carriers, debugging distribution issues, or interfacing with Erlang from other languages.

# Examples

**Example 1** (Introduction): Converting a term to binary and back:
```erlang
Bin = erlang:term_to_binary({hello, world}),
{hello, world} = erlang:binary_to_term(Bin).
```

**Example 2** (Overall format): The binary encoding structure:
```
| 1     | 1     | N      |
| 131   | Tag   | Data   |
```

**Example 3** (Atom encoding): Atoms over distribution use UTF-8 with `ATOM_UTF8_EXT` (tag 118) or `SMALL_ATOM_UTF8_EXT` (tag 119), or `ATOM_CACHE_REF` (tag 82) when using the atom cache.

# Relationships

## Builds Upon
None

## Related
- **distribution-header** -- The distribution header precedes external-format terms in inter-node messages and manages the atom cache
- **distribution-protocol** -- The protocol that carries messages encoded in external term format
- **distribution-connection** -- Connected nodes exchange messages using external term format with distribution headers

## Contrasts With
None

# Common Errors

- **Error**: Assuming atoms are always encoded in Latin-1
  **Correction**: Since ERTS 9.0 (OTP 20), atoms are always encoded in UTF-8 over distribution. The `ATOM_EXT` (Latin-1) encoding is deprecated.

- **Error**: Expecting the version byte (131) in terms that follow a distribution header
  **Correction**: When a distribution header is present, the version byte is omitted from the following terms since it is implied by the header.

# Common Confusions

- **Confusion**: Thinking external term format is only for `term_to_binary`
  **Clarification**: The format is the same whether produced by `term_to_binary` or by the distribution. The distribution uses it implicitly for all inter-node messages.

- **Confusion**: Conflating the external term format with the distribution protocol
  **Clarification**: The external term format is the encoding of individual terms. The distribution protocol defines how connections are established and how messages (containing external-format terms) are framed and delivered.

# Source Reference

"External Term Format" chapter, sections "Introduction", "Encoding atoms", and the individual term type sections.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: HIGH -- explicitly defined with comprehensive specification
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
