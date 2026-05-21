---
concept: Sub Binary
slug: sub-binary
category: performance
subcategory: binary-types
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Sub Binaries"
extraction_confidence: high
aliases:
  - "sub binary"
  - "sub-binary"
prerequisites:
  - refc-binary
  - heap-binary
extends: []
related:
  - match-context
  - binary-matching-efficiency
contrasts_with:
  - match-context
answers_questions:
  - "What is a sub binary?"
---

# Quick Definition

A sub binary is a reference object that points into a part of an existing refc binary or heap binary, created during binary pattern matching or by `split_binary/2`. Because it is a reference and not a copy, matching out a binary portion is relatively cheap.

# Core Definition

A sub binary is created by `split_binary/2` and when a binary is matched out in a binary pattern. A sub binary is a reference into a part of another binary (refc or heap binary, but never into another sub binary). Therefore, matching out a binary is relatively cheap because the actual binary data is never copied. Sub binaries and match contexts are the two reference object types in Erlang's binary implementation (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Sub Binaries").

# Prerequisites

- **refc-binary** -- Sub binaries reference into refc binaries (or heap binaries); understanding the underlying container type is needed
- **heap-binary** -- Sub binaries can also reference into heap binaries; understanding both container types is needed

# Key Properties

1. A sub binary is a reference, not a copy of binary data
2. Created by `split_binary/2` or when a binary is matched out in a pattern
3. Can reference a refc binary or a heap binary
4. Cannot reference another sub binary (always points to a container binary)
5. Matching out a binary via a sub binary does not copy the data
6. The compiler tries to avoid creating sub binaries when a match context can be reused instead

# Construction / Recognition

## When a Sub Binary Is Created

1. Calling `split_binary/2` on a binary
2. Matching out a binary portion in a pattern: `<<Prefix:N/binary, Rest/binary>> = Bin` creates sub binaries for both `Prefix` and `Rest`
3. When a match context needs to be converted back to a binary (e.g., when a matched-out tail is returned from a function)

## When a Sub Binary Is NOT Created

1. When the compiler determines that a match context can be passed directly to the next function call
2. When the matched-out binary is unused

# Context & Application

Sub binaries are a key part of Erlang's efficient binary handling. By referencing the original binary data rather than copying it, operations like splitting a binary or extracting a portion are O(1) in data copying -- only a small reference structure is allocated.

**Typical contexts:**
- Binary pattern matching that returns a portion of the input
- Protocol parsing where headers and payloads are extracted as separate binaries
- Any use of `split_binary/2`

The compiler actively minimizes sub binary creation during binary matching. When a binary tail is immediately passed to another matching function, the compiler passes the match context directly instead, only creating a sub binary when the result must be stored or returned.

# Examples

**Sub binary created when returning matched data** (source: "Matching Binaries" section):

```erlang
after_zero(<<0,T/binary>>) ->
         %% BINARY CREATED: binary is returned from the function
    T;
after_zero(<<_,T/binary>>) ->
         %% OPTIMIZED: match context reused
    after_zero(T);
after_zero(<<>>) ->
    <<>>.
```

In the first clause, `T` is returned from the function, so the compiler must create a sub binary. In the second clause, `T` is immediately passed to a recursive call, so the compiler reuses the match context instead.

**Match context converted to sub binary when needed** (source: "Matching Binaries" section):

```erlang
all_but_zeroes_to_list(Buffer, Acc, 0) ->
    {lists:reverse(Acc), Buffer};
all_but_zeroes_to_list(<<0,T/binary>>, Acc, Remaining) ->
    all_but_zeroes_to_list(T, Acc, Remaining-1);
all_but_zeroes_to_list(<<Byte,T/binary>>, Acc, Remaining) ->
    all_but_zeroes_to_list(T, [Byte|Acc], Remaining-1).
```

The compiler adds an instruction to the first clause that converts `Buffer` from a match context to a sub binary (or does nothing if `Buffer` is already a binary).

# Relationships

## Related

- **match-context** -- The other reference type; optimized for sequential matching
- **binary-matching-efficiency** -- Sub binaries are part of the overall matching efficiency story

## Contrasts With

- **match-context** -- A match context is similar to a sub binary but optimized for binary matching with a direct pointer and position tracking. The compiler prefers match contexts during active matching and only creates sub binaries when the reference must persist beyond the match.

# Common Errors

- **Error**: Expecting sub binary creation to copy the binary data
  **Correction**: Sub binaries are references; no data is copied. This is why binary matching is efficient.

- **Error**: Writing code that creates a sub binary and then immediately creates a match context from it
  **Correction**: The compiler optimizes this case away, but understanding it helps when reading `bin_opt_info` output

# Common Confusions

- **Confusion**: Thinking sub binaries can chain (sub binary of a sub binary)
  **Clarification**: A sub binary always references a container binary (refc or heap), never another sub binary

- **Confusion**: Conflating sub binaries with match contexts
  **Clarification**: Sub binaries are general-purpose references to binary portions. Match contexts are specialized, mutable structures optimized for sequential binary matching with a position pointer.

# Source Reference

"Constructing and Matching Binaries," section "Sub Binaries." Also referenced in sections "Match Context" and "Matching Binaries" where the compiler's strategy for avoiding sub binary creation is explained.

# Verification Notes

- Definition: Directly from source -- "A sub binary is a reference into a part of another binary (refc or heap binary, but never into another sub binary)"
- Creation triggers: Explicitly listed -- `split_binary/2` and binary pattern matching
- No-copy property: Explicitly stated -- "matching out a binary is relatively cheap because the actual binary data is never copied"
- Compiler avoidance of sub binaries: Described in both "Match Context" and "Matching Binaries" sections
- Confidence: HIGH -- explicit definition and behavior described in official OTP documentation
