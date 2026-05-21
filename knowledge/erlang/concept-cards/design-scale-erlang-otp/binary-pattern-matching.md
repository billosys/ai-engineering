---
# === CORE IDENTIFICATION ===
concept: Binary Pattern Matching
slug: binary-pattern-matching

# === CLASSIFICATION ===
category: data-types
subcategory: binaries
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Recursion and Pattern Matching"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bit syntax
  - binary matching
  - bitstring pattern matching

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends:
  - pattern-matching
related:
  - macros
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang match on binary data at the bit level?"
  - "How do I decode a network packet in Erlang?"
---

# Quick Definition

Binary pattern matching extends pattern matching to bit-level data, letting you extract named fields of specified bit/byte widths from a binary in a single expression. It is especially powerful for decoding network protocols.

# Core Definition

"Erlang also allows pattern matching over binary data, where we match on a bit level. This is an incredibly powerful and efficient construct for decoding frames and dealing with network protocol stacks" (Cesarini & Vinoski, p. 24). A binary pattern is "delimited by `<<` and `>>` and containing a number of fields. ... The numbers following most of the fields specify the number of bits (or bytes for binaries) each field occupies" (pp. 24-25). A field's size may be fixed (`Flgs:3`) or computed dynamically; trailing data is captured as a binary of unknown length.

# Prerequisites

- **Pattern matching** — Binary matching is a specialized form of pattern matching; the same clause-selection and binding semantics apply.

# Key Properties

1. Binary patterns are delimited by `<<` and `>>`.
2. A field's bit count is given after a colon, e.g., `HLen:4`; binaries use byte counts.
3. A field defaults to an integer unless typed as `/binary`.
4. Field sizes can be computed dynamically from earlier-bound variables (e.g., `Opts:OptsLen/binary`).
5. A successful match extracts all named fields in a single statement.
6. The final field can be left as a binary of unknown length (`Body/binary`).

# Construction / Recognition

## To Construct:
1. Write the binary pattern on the left of `=` with the binary value on the right.
2. Specify each field as `Name:Size` (bits) or `Name:Size/binary` (bytes).
3. Use a trailing `Rest/binary` for variable-length remainders.

## To Recognize:
1. Look for `<<...>>` on the left-hand side of a match or in a function head.
2. Fields with `:` size specifiers indicate bit-level decoding.

# Context & Application

- **Typical contexts**: Decoding network frames, protocol stacks, file formats.
- **Common applications**: Extracting header fields from packets received over sockets.
- **Historical/stylistic notes**: The authors contrast this with the verbose bit-twiddling needed in Java or C.

# Examples

**Example 1** (pp. 24-25): Decoding an IPv4 packet (ellipses mark omitted fields, not legal code):

```erlang
-define(IP_VERSION, 4).
-define(IP_MIN_HDR_LEN, 5).
handle(Dgram) ->
    DgramSize = byte_size(Dgram),
    <<?IP_VERSION:4, HLen:4, SrvcType:8, TotLen:16, ID:16, ...,
      Flgs:3, FragOff:13, TTL:8, Proto:8, HdrChkSum:16, ...,
      SrcIP:32, DestIP:32, Body/binary>> = Dgram,
    if
        (HLen >= 5) and (4*HLen =< DgramSize) ->
            OptsLen = 4*(HLen - ?IP_MIN_HDR_LEN),
            <<Opts:OptsLen/binary, Data/binary>> = Body,
            ...
    end.
```

Here `Flgs:3` binds 3 bits to `Flgs`, and `OptsLen` is computed dynamically to drive a second match against `Body`.

# Relationships

## Builds Upon
- **Pattern matching** — Binary matching applies the same matching semantics at the bit level.

## Enables
- *(none specific in scope)*

## Related
- **Macros** — The IPv4 example uses `-define` macros for protocol constants.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Writing literal ellipses (`...`) inside a binary pattern.
  **Correction**: Ellipses in the book example are illustrative only and are not legal Erlang.
- **Error**: Forgetting `/binary` on a multi-byte trailing field, causing it to be treated as an integer.
  **Correction**: Type variable-length remainders explicitly as `/binary`.

# Common Confusions

- **Confusion**: Thinking the size number always means bytes.
  **Clarification**: The size is in bits for integer fields and in bytes for `/binary` fields.

# Source Reference

Chapter 1: Introducing Erlang, Section "Recursion and Pattern Matching," pages 24-25.

# Verification Notes

- Definition source: Direct quotes from pp. 24-25.
- Confidence rationale: HIGH — explicit description with a worked IPv4 example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
