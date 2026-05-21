---
concept: Binary Matching Efficiency
slug: binary-matching-efficiency
category: performance
subcategory: binary-operations
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Matching Binaries"
extraction_confidence: high
aliases:
  - "binary pattern matching"
  - "efficient binary matching"
prerequisites: []
extends: []
related:
  - match-context
  - sub-binary
  - binary-construction-efficiency
  - bin-opt-info
contrasts_with: []
answers_questions:
  - "How does efficient binary matching work in Erlang?"
---

# Quick Definition

Binaries can be efficiently matched by splitting off one element at a time in a recursive function clause, with the remainder bound as a binary tail. The compiler optimizes this pattern to reuse a single match context instead of creating intermediate sub binaries.

# Core Definition

The efficient pattern for binary matching uses a function clause that matches one or more bytes from the head of a binary and binds the rest as a tail: `<<H, T/binary>>`. The first time such a function is called, the runtime creates a match context pointing to the first byte. On each recursive call, the match context position is incremented rather than creating a new sub binary. The compiler avoids generating code that creates a sub binary only to shortly afterwards create a new match context and discard the sub binary (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Matching Binaries").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Binary matching creates a match context on the first call
2. The match context is reused across recursive calls instead of creating sub binaries
3. The compiler eliminates unnecessary sub binary creation when a match context can be passed directly
4. Only one match context is created for the entire traversal
5. A sub binary is created only when the matched-out portion must be returned or stored
6. Unused variables in match patterns cause the bits to be skipped, not matched out

# Construction / Recognition

## Writing Efficient Binary Matching

1. Use a function clause that matches elements from the head: `<<H, T/binary>>`
2. Recursively call the same function (or another matching function) with `T`
3. Provide a base case matching the empty binary: `<<>>`

## Recognizing Optimizable Patterns

1. A function that recursively decomposes a binary head/tail is the primary optimizable pattern
2. The compiler can optimize when it determines the match context will not be shared
3. Use `bin_opt_info` to verify the optimization is being applied

# Context & Application

This pattern is the binary equivalent of recursive list decomposition (`[H|T]`). It provides efficient, sequential access to binary data without copying.

**Typical contexts:**
- Converting a binary to a list
- Parsing binary protocols byte by byte
- Searching through binary data
- Any sequential binary processing

The match context reuse optimization is the key to making binary matching competitive with C-style pointer arithmetic. Without it, each recursive step would allocate a new sub binary referencing the remaining data.

# Examples

**DO** -- Efficient binary-to-list conversion (source: "Matching Binaries" section):

```erlang
my_binary_to_list(<<H,T/binary>>) ->
    [H|my_binary_to_list(T)];
my_binary_to_list(<<>>) -> [].
```

This function creates only one match context and no sub binaries. The match context is passed directly to the recursive call and discarded when the empty binary matches.

**Optimized matching with early return** (source: "Matching Binaries" section):

```erlang
after_zero(<<0,T/binary>>) ->
    T;
after_zero(<<_,T/binary>>) ->
    after_zero(T);
after_zero(<<>>) ->
    <<>>.
```

The compiler removes the sub binary construction in the second clause (match context reused). A sub binary is only created in the first clause because `T` is returned from the function.

**Unused variables generate identical code** (source: "Unused Variables" section):

```erlang
count1(<<_,T/binary>>, Count) -> count1(T, Count+1);
count1(<<>>, Count) -> Count.

count2(<<H,T/binary>>, Count) -> count2(T, Count+1);
count2(<<>>, Count) -> Count.

count3(<<_H,T/binary>>, Count) -> count3(T, Count+1);
count3(<<>>, Count) -> Count.
```

All three generate the same code: the first 8 bits are skipped, not matched out.

# Relationships

## Related

- **match-context** -- The underlying data structure that enables efficient binary matching
- **sub-binary** -- Created only when matched-out binary data must be retained
- **binary-construction-efficiency** -- The counterpart: efficient binary building
- **bin-opt-info** -- Compiler option to verify match optimization is applied

# Common Errors

- **Error**: Creating intermediate variables that prevent match context reuse
  **Correction**: Structure code so the binary tail is passed directly to the next matching function

- **Error**: Assuming all binary match patterns are automatically optimized
  **Correction**: Use `bin_opt_info` to verify; the compiler can only optimize when it knows the match context will not be shared

# Common Confusions

- **Confusion**: Thinking each recursive call creates a new copy of the remaining binary
  **Clarification**: The match context is a lightweight pointer that is incremented, not a copy of the data

- **Confusion**: Believing that naming a variable (e.g., `H` vs `_`) changes the generated code
  **Clarification**: The compiler detects unused variables (`H`, `_H`, `_`) and generates identical skip instructions for all three

# Source Reference

"Constructing and Matching Binaries," section "Matching Binaries" and subsection "Unused Variables." The source provides detailed walkthrough of match context reuse with multiple code examples, including the `after_zero/1` and `all_but_zeroes_to_list/3` examples.

# Verification Notes

- Definition: Synthesized from the detailed walkthrough in "Matching Binaries" section
- Match context reuse: Explicitly described -- "my_binary_to_list/1 calls itself with the match context instead of with a sub binary"
- Sub binary creation rule: Explicitly stated for the `after_zero/1` example
- Unused variables: Directly from "Unused Variables" subsection -- "The same code is generated for each of the following functions"
- Confidence: HIGH -- detailed explanation with multiple examples in official OTP documentation
