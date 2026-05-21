---
concept: Deep vs Flat Lists
slug: deep-vs-flat-lists
category: data-structures
subcategory: list-operations
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "List Handling"
chapter_number: null
pdf_page: null
section: "Deep and Flat Lists"
extraction_confidence: high
aliases:
  - "deep lists"
  - "flat lists"
  - "iolists"
  - "nested lists"
prerequisites:
  - list-construction-efficiency
extends: []
related:
  - append-operator-efficiency
contrasts_with: []
answers_questions:
  - "How do I avoid unnecessary list flattening?"
  - "What distinguishes lists:flatten/1 from lists:append/1?"
---

# Quick Definition

`lists:flatten/1` builds an entirely new list and is expensive -- even more expensive than `++`. In many cases, flattening is unnecessary because ports and BIFs like `list_to_binary/1` accept deep (nested) lists directly. When the list is only one level deep, `lists:append/1` is a cheaper alternative.

# Core Definition

`lists:flatten/1` builds an entirely new list. It is therefore expensive, and even more expensive than the `++` operator (which copies its left argument, but not its right argument). Flattening is unnecessary in several situations: when sending data to a port (ports understand deep lists), when calling BIFs that accept deep lists such as `list_to_binary/1` or `iolist_to_binary/1`, and when the list is only one level deep (use `lists:append/1` instead). (Ericsson/OTP Team, "List Handling," section "Deep and Flat Lists").

# Prerequisites

- **list-construction-efficiency** -- Understanding list copying costs is needed to appreciate why flattening is expensive

# Key Properties

1. `lists:flatten/1` builds an entirely new list (copies all elements at all nesting levels)
2. `lists:flatten/1` is more expensive than `++` (which only copies its left operand)
3. Ports understand deep lists -- no need to flatten before `port_command/2`
4. BIFs like `list_to_binary/1` and `iolist_to_binary/1` accept deep lists
5. `lists:append/1` handles one-level-deep lists more efficiently than `lists:flatten/1`
6. Deep lists (iolists) can be used to avoid both flattening and `++` overhead

# Construction / Recognition

## Recognizing Unnecessary Flattening

1. Flattening before sending to a port: `port_command(Port, lists:flatten(DeepList))` -- the flatten is unnecessary
2. Flattening before calling `list_to_binary/1` or `iolist_to_binary/1` -- unnecessary
3. Flattening a one-level-deep list -- use `lists:append/1` instead

## Using Deep Lists to Avoid Copying

1. Instead of `String ++ [0]` (copies String), use `[String, 0]` (creates a deep list, no copying)
2. Pass the deep list directly to the consumer (port, BIF, etc.)

# Context & Application

Deep lists (iolists) are a powerful idiom in Erlang for avoiding unnecessary data copying. By keeping data in a nested list structure and only flattening at the boundary (if needed at all), programs can construct complex output with minimal allocation.

**Typical contexts:**
- Building output for ports (network sockets, file I/O)
- Constructing binary data from mixed sources
- String concatenation (using iolists instead of flat strings)
- Any output pipeline where the final consumer accepts deep lists

**Key insight:** Many Erlang I/O operations accept iolists (deep lists of bytes, binaries, and nested lists). Leveraging this avoids the O(n) cost of flattening and the O(n) cost of `++` copying.

# Examples

**DO** -- Send deep list directly to port (source: "Deep and Flat Lists" section):

```erlang
port_command(Port, DeepList)
```

**DO NOT** -- Unnecessary flatten before port (source: same section):

```erlang
port_command(Port, lists:flatten(DeepList))
```

**DO** -- Use deep list instead of `++` for zero-terminated string (source: same section):

```erlang
TerminatedStr = [String, 0],
port_command(Port, TerminatedStr)
```

**DO NOT** -- Copying with `++` to append a terminator (source: same section):

```erlang
TerminatedStr = String ++ [0],
port_command(Port, TerminatedStr)
```

**DO** -- Use `lists:append/1` for one-level-deep lists (source: same section):

```erlang
1> lists:append([[1], [2], [3]]).
[1,2,3]
```

**DO NOT** -- Use `lists:flatten/1` for one-level-deep lists (source: same section):

```erlang
1> lists:flatten([[1], [2], [3]]).
[1,2,3]
```

Both produce the same result, but `lists:append/1` is more efficient for one-level-deep lists.

# Relationships

## Related

- **append-operator-efficiency** -- The `++` operator is related but distinct; `lists:flatten/1` is even more expensive than `++`

# Common Errors

- **Error**: Calling `lists:flatten/1` before `port_command/2`
  **Correction**: Ports accept deep lists directly; skip the flatten

- **Error**: Using `String ++ [0]` to append a terminator, copying the entire string
  **Correction**: Use `[String, 0]` to create a deep list without copying

- **Error**: Using `lists:flatten/1` when the list is only one level deep
  **Correction**: Use `lists:append/1`, which is more efficient for single-level nesting

# Common Confusions

- **Confusion**: Thinking `lists:flatten/1` and `lists:append/1` are interchangeable
  **Clarification**: `lists:append/1` only removes one level of nesting. `lists:flatten/1` recursively flattens all levels. For one-level-deep lists the result is the same, but `lists:append/1` is cheaper. For deeper nesting, only `lists:flatten/1` fully flattens.

- **Confusion**: Believing all functions require flat lists as input
  **Clarification**: Many Erlang I/O functions and BIFs accept deep lists (iolists). Check the documentation of the consuming function before flattening.

- **Confusion**: Thinking deep lists waste memory compared to flat lists
  **Clarification**: Deep lists share the underlying data. A flat list created by `lists:flatten/1` is a complete copy. Deep lists typically use less total memory.

# Source Reference

"List Handling," section "Deep and Flat Lists." The source lists three situations where flattening is unnecessary (ports, deep-list BIFs, one-level-deep lists), provides DO/DO NOT examples for each, and establishes the cost hierarchy: `lists:flatten/1` > `++` > `lists:append/1`.

# Verification Notes

- Definition: Directly from source -- "lists:flatten/1 builds an entirely new list. It is therefore expensive, and even more expensive than the ++ operator"
- Three unnecessary-flattening scenarios: All explicitly enumerated in source
- Cost comparison: Explicitly stated (flatten > ++)
- All examples directly from source
- `lists:append/1` recommendation for one-level: Explicitly stated
- Confidence: HIGH -- explicit enumeration with DO/DO NOT examples in official OTP documentation
