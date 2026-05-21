---
concept: Match Context
slug: match-context
category: performance
subcategory: binary-types
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Match Context"
extraction_confidence: high
aliases:
  - "match context"
  - "binary match context"
prerequisites:
  - refc-binary
  - heap-binary
  - sub-binary
extends:
  - sub-binary
related:
  - binary-matching-efficiency
  - bin-opt-info
contrasts_with:
  - sub-binary
answers_questions:
  - "What is a match context in binary matching?"
---

# Quick Definition

A match context is a reference object similar to a sub binary but optimized for binary matching: it contains a direct pointer to the binary data and a position that is incremented as fields are matched out. The compiler reuses match contexts across recursive calls to avoid creating intermediate sub binaries.

# Core Definition

A match context is similar to a sub binary, but is optimized for binary matching. For example, it contains a direct pointer to the binary data. For each field that is matched out of a binary, the position in the match context is incremented. The compiler tries to avoid generating code that creates a sub binary, only to shortly afterwards create a new match context and discard the sub binary. Instead of creating a sub binary, the match context is kept. The compiler can only do this optimization if it knows that the match context will not be shared. If it would be shared, the functional properties (also called referential transparency) of Erlang would break (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Match Context").

# Prerequisites

- **refc-binary** -- Match contexts reference refc binaries (or heap binaries); understanding the container types is needed
- **heap-binary** -- Match contexts can also reference heap binaries
- **sub-binary** -- A match context is an optimized variant of a sub binary; understanding sub binaries provides the baseline

# Key Properties

1. Contains a direct pointer to the binary data (more efficient than sub binary's indirect reference)
2. Maintains a position that is incremented as fields are matched out
3. Optimized specifically for sequential binary matching
4. The compiler reuses match contexts across recursive calls when safe
5. Can only be reused when the compiler proves the match context will not be shared
6. Sharing a match context would violate referential transparency
7. The instruction that initializes matching does nothing when passed an existing match context

# Construction / Recognition

## When a Match Context Is Created

1. The first time a binary is matched in a function clause: `<<H, T/binary>> = Bin`
2. Created automatically by the runtime when binary pattern matching begins

## When a Match Context Is Reused

1. When the binary tail is passed directly to a recursive call to the same function
2. When the binary tail is passed to another function that immediately begins matching
3. The matching instruction detects it received a match context (not a binary) and skips initialization

## When a Match Context Cannot Be Reused

1. When the match context would be shared (e.g., stored in a data structure and also matched)
2. When the binary tail must be returned from the function (a sub binary is created instead)

# Context & Application

Match contexts are the key optimization that makes recursive binary matching in Erlang efficient. Without this optimization, each recursive step in a binary traversal would create a sub binary (allocating memory) and then immediately create a new match context from it (more allocation). By passing the match context directly, the runtime avoids both allocations.

**Typical contexts:**
- Recursive binary parsing functions
- Binary-to-list conversions
- Protocol decoders that process binaries byte-by-byte or field-by-field

The compiler's ability to reuse match contexts is what makes the idiomatic `<<H, T/binary>>` recursive pattern as efficient as imperative pointer-based parsing.

# Examples

**Match context reuse in recursive matching** (source: "Matching Binaries" section):

```erlang
my_binary_to_list(<<H,T/binary>>) ->
    [H|my_binary_to_list(T)];
my_binary_to_list(<<>>) -> [].
```

The first call creates a match context pointing to the first byte. Each recursive call receives the same match context (with updated position) instead of a sub binary. When `<<>>` matches, the match context is simply discarded. Result: one match context, zero sub binaries.

**Selective match context reuse** (source: "Matching Binaries" section):

```erlang
after_zero(<<0,T/binary>>) ->
    T;                          %% sub binary created (T is returned)
after_zero(<<_,T/binary>>) ->
    after_zero(T);              %% match context reused
after_zero(<<>>) ->
    <<>>.
```

The second clause reuses the match context. The first clause must create a sub binary because `T` is returned from the function.

**Match context to sub binary conversion** (source: "Matching Binaries" section):

```erlang
all_but_zeroes_to_list(Buffer, Acc, 0) ->
    {lists:reverse(Acc), Buffer};    %% Buffer converted from match context to sub binary
all_but_zeroes_to_list(<<0,T/binary>>, Acc, Remaining) ->
    all_but_zeroes_to_list(T, Acc, Remaining-1);
all_but_zeroes_to_list(<<Byte,T/binary>>, Acc, Remaining) ->
    all_but_zeroes_to_list(T, [Byte|Acc], Remaining-1).
```

The compiler adds an instruction to the first clause that converts `Buffer` from a match context to a sub binary (or does nothing if `Buffer` is already a binary).

# Relationships

## Builds Upon

- **sub-binary** -- A match context is an optimized form of sub binary, specialized for sequential matching

## Related

- **binary-matching-efficiency** -- Match context reuse is the core mechanism behind efficient binary matching
- **bin-opt-info** -- The compiler option that reveals whether match contexts are being reused

## Contrasts With

- **sub-binary** -- Sub binaries are general-purpose references suitable for storage and return. Match contexts are mutable, position-tracking structures that exist only during active matching and cannot be safely shared.

# Common Errors

- **Error**: Writing code that prevents match context reuse (e.g., storing the binary tail in a tuple before recursing)
  **Correction**: Pass the binary tail directly to the next matching function

- **Error**: Not checking whether the optimization is applied in performance-critical code
  **Correction**: Use `bin_opt_info` to verify match context reuse

# Common Confusions

- **Confusion**: Thinking a new match context is created on every recursive call
  **Clarification**: The existing match context is passed directly; the matching instruction detects it and skips initialization

- **Confusion**: Believing match contexts are just a compiler concept with no runtime representation
  **Clarification**: Match contexts are real runtime objects with a direct pointer and position. The compiler controls when they are created and reused, but the runtime manages their lifecycle.

# Source Reference

"Constructing and Matching Binaries," section "Match Context" (definition) and section "Matching Binaries" (detailed optimization examples). The match context concept is defined in one section and its optimization behavior is demonstrated extensively in the matching section.

# Verification Notes

- Definition: Directly from source -- "A match context is similar to a sub binary, but is optimized for binary matching"
- Direct pointer property: Explicitly stated -- "it contains a direct pointer to the binary data"
- Position increment: Explicitly stated -- "For each field that is matched out of a binary, the position in the match context is incremented"
- Sharing constraint: Explicitly stated -- "The compiler can only do this optimization if it knows that the match context will not be shared"
- Referential transparency: Explicitly mentioned as the reason sharing is forbidden
- Examples: All from the "Matching Binaries" section walkthrough
- Confidence: HIGH -- explicit definition and extensive worked examples in official OTP documentation
