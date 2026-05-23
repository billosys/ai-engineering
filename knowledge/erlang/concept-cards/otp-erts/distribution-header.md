---
# === CORE IDENTIFICATION ===
concept: Distribution Header
slug: distribution-header

# === CLASSIFICATION ===
category: distribution
subcategory: encoding
tier: advanced

# === PROVENANCE ===
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "External Term Format"
chapter_number: null
pdf_page: null
section: "Distribution Header"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "dist header"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - external-term-format
  - distribution-protocol
extends:
  - external-term-format
related:
  - distribution-connection
  - distribution-handshake
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the distribution header in Erlang?"
  - "How does the atom cache work in Erlang distribution?"
  - "How does message fragmentation work in Erlang distribution?"
---

# Quick Definition

The distribution header is a metadata preamble sent before each control message and payload in inter-node communication. It manages the atom cache for efficient atom transmission and, since OTP 22, supports fragmenting large messages into smaller pieces for interleaving with other traffic.

# Core Definition

The ERTS documentation states: "The distribution header is sent by the erlang distribution to carry metadata about the coming control message and potential payload. It is primarily used to handle the atom cache in the Erlang distribution." Since OTP 22, it also supports fragmenting large distribution messages into multiple smaller fragments.

The normal (non-fragmented) distribution header format starts with version byte `131`, tag `68`, followed by `NumberOfAtomCacheRefs`, then half-byte flags for each reference, then the atom cache reference data itself. The atom cache consists of 8 segments of 256 entries each, allowing up to 2048 cached atoms. Each atom cache reference uses a 4-bit flag field containing a `NewCacheEntryFlag` bit and a 3-bit `SegmentIndex`.

Fragmented messages (since OTP 22) use tag `69` for the start fragment and tag `70` for continuation fragments. The start fragment includes a `SequenceId` and `FragmentId` along with atom cache data. Fragment IDs count down from the total number of fragments to 1 (the final fragment).

# Prerequisites

- **external-term-format** -- The distribution header wraps terms encoded in external term format
- **distribution-protocol** -- The distribution header is part of the protocol between connected nodes

# Key Properties

1. Normal header: version `131`, tag `68`, `NumberOfAtomCacheRefs`, `Flags`, `AtomCacheRefs`
2. Atom cache supports up to 2048 entries across 8 segments of 256 entries each
3. At most 255 different atom cache references can be made per distribution header
4. New cache entries include `InternalSegmentIndex`, `Length`, and `AtomText`; cached entries include only `InternalSegmentIndex`
5. The `LongAtoms` flag enables 2-byte atom lengths instead of 1 byte
6. Fragmented start header: version `131`, tag `69`, `SequenceId` (8 bytes), `FragmentId` (8 bytes), then atom cache data
7. Fragmented continuation header: version `131`, tag `70`, `SequenceId`, `FragmentId`
8. Fragment IDs count down: the start has the total count, then n-1, n-2, ..., 1 (final)
9. Fragmentation requires the `DFLAG_FRAGMENTS` distribution flag
10. The entire atom cache and control message must be in the starting fragment; only the payload may be split

# Construction / Recognition

## To Construct/Create:
1. The runtime system automatically constructs distribution headers when sending messages between connected nodes
2. When implementing an alternative distribution carrier, you must handle distribution headers in the data stream

## To Identify/Recognize:
1. Starts with byte `131` followed by tag `68` (normal) or `69` (fragment start) or `70` (fragment continuation)
2. Appears before every control message in inter-node communication

# Context & Application

The distribution header is a performance optimization for Erlang distribution. Without the atom cache, every message would need to encode all atom names as full UTF-8 strings. The atom cache allows frequently used atoms to be sent once and then referenced by index. Message fragmentation prevents large messages from blocking smaller, potentially higher-priority messages on the same connection. Both features are negotiated during the distribution handshake via capability flags.

# Examples

**Example 1** (Distribution Header section): A fragmented message sending `{call, <0.245.2>, {set_get_state, <<0:1024>>}}` to registered process `reg` with a fragment size of 128 bytes. The first fragment (tag `69`) contains atom cache updates and the control message, plus the beginning of the payload. The second fragment (tag `70`) contains the remaining payload bytes.

**Example 2** (Distribution Header section): Atom cache flags in binary half-byte form:
```
0000, 0100, 1000, 1001, 1001
```
The high bit of each half-byte is the `NewCacheEntryFlag`. The first two atoms (high bit 0) are already cached; the last three (high bit 1) are new entries that include atom text.

# Relationships

## Builds Upon
- **external-term-format** -- The header precedes terms encoded in external format; the version byte is omitted from those terms
- **distribution-protocol** -- The header is exchanged as part of the connected-nodes protocol

## Related
- **distribution-connection** -- Connected nodes use distribution headers on all messages
- **distribution-handshake** -- The `DFLAG_DIST_HDR_ATOM_CACHE` and `DFLAG_FRAGMENTS` flags are negotiated during the handshake

## Contrasts With
None

# Common Errors

- **Error**: Splitting the atom cache or control message across fragments
  **Correction**: The entire atom cache and control message must be in the starting fragment. Only the payload (message body) may be split across fragments.

- **Error**: Sending fragmented messages to a node that does not support them
  **Correction**: Fragmented messages are only used if the receiving node has set the `DFLAG_FRAGMENTS` distribution flag during the handshake.

# Common Confusions

- **Confusion**: Thinking fragment IDs count upward
  **Clarification**: Fragment IDs count downward from the total number of fragments to 1. The start fragment has the highest ID; the final fragment has ID 1.

- **Confusion**: Assuming all atom names are sent in every message
  **Clarification**: The atom cache means atoms only need to be sent as full text once. Subsequent references use a single-byte `InternalSegmentIndex` combined with the `SegmentIndex` from the flags.

# Source Reference

"External Term Format" chapter, sections "Distribution Header", "Normal Distribution Header", and "Distribution Header for fragmented messages", including the worked fragmentation example.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: HIGH -- explicitly defined with detailed wire format and example
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
