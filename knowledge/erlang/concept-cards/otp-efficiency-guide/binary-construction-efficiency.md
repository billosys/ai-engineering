---
concept: Binary Construction Efficiency
slug: binary-construction-efficiency
category: performance
subcategory: binary-operations
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "efficient binary building"
  - "binary construction"
prerequisites: []
extends: []
related:
  - binary-append-optimization
  - compiler-binary-optimization
  - refc-binary
  - heap-binary
  - forced-copying
  - binary-matching-efficiency
contrasts_with: []
answers_questions:
  - "How do I efficiently construct a binary by appending data?"
  - "What must I understand before optimizing binary construction?"
---

# Quick Definition

Binaries in Erlang can be efficiently built by appending data to the end of an accumulator binary, with the accumulator always as the first segment. The runtime system specially optimizes this pattern to avoid copying the accumulator on each iteration.

# Core Definition

Binaries can be efficiently built by placing the binary to be appended to as the first segment of the binary construction expression: `<<Acc/binary, NewData>>`. This pattern is specially optimized by the runtime system to avoid copying the accumulator binary every time. Conversely, prepending data to a binary (`<<NewData, Acc/binary>>`) forces a full copy of the accumulator on each iteration and is not efficient for long lists (Ericsson/OTP Team, "Constructing and Matching Binaries").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The binary being appended to must always be the first segment: `<<Acc/binary, ...>>`
2. Prepending (`<<NewData, Acc/binary>>`) causes a full copy of `Acc` on every iteration
3. The runtime system applies a special optimization to the append pattern
4. The optimization works without any compiler support in its basic form
5. Both tail-recursive and body-recursive styles can be efficient, as long as the append pattern is correct

# Construction / Recognition

## Efficient Binary Construction Pattern

1. Initialize an accumulator as an empty binary: `<<>>`
2. In each recursive step, append new data to the end: `<<Acc/binary, NewByte>>`
3. The accumulator binary must be the first segment in the binary expression
4. Return the accumulator when done

## Recognizing the Anti-Pattern

1. Look for binary construction where the accumulator appears as a non-first segment
2. `<<H, Acc/binary>>` -- prepending forces a copy of `Acc` on every call
3. Any pattern where the growing binary is not the leftmost segment

# Context & Application

This is the most fundamental rule for binary construction in Erlang. The runtime system's append optimization depends on the binary being the first segment, because the extra allocated space is at the end of the binary object. Prepending would require moving all existing data.

**Typical contexts:**
- Converting a list to a binary
- Building network packets incrementally
- Accumulating data from a stream

Understanding this pattern is the prerequisite for understanding the deeper optimization mechanisms (append optimization, compiler support, forced copying).

# Examples

**DO** -- Efficient append with accumulator as first segment (source: opening examples):

```erlang
my_list_to_binary(List) ->
    my_list_to_binary(List, <<>>).

my_list_to_binary([H|T], Acc) ->
    my_list_to_binary(T, <<Acc/binary,H>>);
my_list_to_binary([], Acc) ->
    Acc.
```

**DO NOT** -- Prepending forces a copy every iteration (source: opening examples):

```erlang
rev_list_to_binary(List) ->
    rev_list_to_binary(List, <<>>).

rev_list_to_binary([H|T], Acc) ->
    rev_list_to_binary(T, <<H,Acc/binary>>);
rev_list_to_binary([], Acc) ->
    Acc.
```

**DO** -- Body-recursive style also works, as long as the base binary is the first segment (source: opening examples):

```erlang
rev_list_to_binary([H|T]) ->
    RevTail = rev_list_to_binary(T),
    <<RevTail/binary,H>>;
rev_list_to_binary([]) ->
    <<>>.
```

# Relationships

## Related

- **binary-append-optimization** -- The underlying mechanism that makes the append pattern efficient
- **compiler-binary-optimization** -- Compiler hints that make the append optimization even more efficient
- **refc-binary** -- Append operations create or grow refc binaries
- **heap-binary** -- Initial small binaries are heap binaries before being promoted during append
- **forced-copying** -- Circumstances that defeat the append optimization
- **binary-matching-efficiency** -- The counterpart: efficient binary deconstruction

# Common Errors

- **Error**: Placing the accumulator as a non-first segment: `<<H, Acc/binary>>`
  **Correction**: Always place the accumulator first: `<<Acc/binary, H>>`

- **Error**: Reversing the list first, then appending (unnecessary overhead)
  **Correction**: The source marks this as "DO NOT" -- use the correct segment order instead, or use the body-recursive style

# Common Confusions

- **Confusion**: Believing the tail-recursive style is always necessary for binary construction
  **Clarification**: The body-recursive style also works efficiently. The key requirement is that the binary to be appended to is always the first segment.

- **Confusion**: Thinking the optimization is purely a compiler optimization
  **Clarification**: The basic append optimization is applied by the runtime system and does not need compiler help (though the compiler can add hints to make it more efficient).

# Source Reference

"Constructing and Matching Binaries," opening section (before "How Binaries are Implemented"). The source provides four code examples (two DO, two DO NOT) demonstrating correct and incorrect binary construction patterns.

# Verification Notes

- Definition: Directly from source -- "Appending data to a binary as in the example is efficient because it is specially optimized by the runtime system to avoid copying the Acc binary every time"
- Key Properties: All derived from explicit source statements
- Examples: All four taken directly from source opening section
- The note about both styles being valid is explicitly from the source
- Confidence: HIGH -- explicit documentation with multiple DO/DO NOT examples in official OTP documentation
