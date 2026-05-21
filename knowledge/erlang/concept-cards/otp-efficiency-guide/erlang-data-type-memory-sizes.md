---
concept: Erlang Data Type Memory Sizes
slug: erlang-data-type-memory-sizes
category: performance
subcategory: data-representation
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Memory Usage"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Erlang memory model"
  - "data type sizes"
  - "heap word sizes"
  - "term memory consumption"
prerequisites: []
extends: []
related:
  - append-operator-efficiency
  - accidental-copying-in-closures
  - loss-of-sharing
  - erlang-system-limits
contrasts_with: []
answers_questions:
  - "What memory model concepts are needed to understand Erlang data type sizes?"
  - "How much memory does each Erlang data type consume?"
  - "What is the difference between 32-bit and 64-bit memory word sizes?"
  - "How much memory does an Erlang process consume at spawn?"
---

# Quick Definition

Erlang data type memory consumption is measured in words (4 bytes on 32-bit, 8 bytes on 64-bit). Each type has a specific size: small integers use 1 word, list elements use 1 word overhead each, tuples use 2 words overhead, and a freshly spawned process uses 338 words.

# Core Definition

A good start when programming efficiently is to know how much memory different data types and operations require. It is implementation-dependent how much memory the Erlang data types and other items consume, but the Efficiency Guide provides figures for the erts-8.0 system in OTP 19.0 (Ericsson/OTP Team, "Memory Usage").

The unit of measurement is memory words. There exists both a 32-bit and a 64-bit implementation. A word is therefore 4 bytes or 8 bytes, respectively. The value for a running system can be determined by calling `erlang:system_info(wordsize)`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Memory is measured in words: 4 bytes (32-bit) or 8 bytes (64-bit)
2. **Small integer**: 1 word (28 bits on 32-bit arch, 60 bits on 64-bit arch)
3. **Large integer**: at least 3 words
4. **Atom**: 1 word (plus shared atom table storage; atom table is NOT garbage-collected)
5. **Float**: 4 words (32-bit) or 3 words (64-bit)
6. **Binary**: 3-6 words + data (can be shared)
7. **List**: 1 word + 1 word per element + size of each element
8. **String** (list of integers): 1 word + 2 words per character
9. **Tuple**: 2 words + size of each element
10. **Small Map** (up to 32 keys): 5 words + size of all keys and values
11. **Large Map** (more than 32 keys): N x F words + size of all keys and values (F is 1.6-1.8 sparsity factor due to HAMT structure)
12. **Pid**: 1 word (local), 5-6 words (remote)
13. **Port**: 1 word (local), 5 words (remote)
14. **Reference**: 4-7 words (local), 6-9 words (remote), varies by architecture
15. **Fun**: 9-13 words + environment size
16. **ETS table**: initially 768 words + 6 words per element + element data size
17. **Erlang process**: 338 words when spawned, including a heap of 233 words

# Construction / Recognition

## Determining Memory Usage at Runtime

1. Call `erlang:system_info(wordsize)` to get the word size in bytes (4 or 8)
2. Use `erts_debug:size/1` to get the size of a term in words (shared subterms counted once)
3. Use `erts_debug:flat_size/1` to get the flat size (no sharing -- what would be copied inter-process)
4. Multiply word count by word size to get byte count

## Estimating Memory for Data Structures

1. For lists: count elements, multiply by (1 + average element size), add 1 word for the list itself
2. For tuples: count elements, add up element sizes, add 2 words overhead
3. For strings: count characters, multiply by 2, add 1 word (since strings are lists of integers)
4. For maps: use the small map formula (up to 32 keys) or large map formula (above 32 keys)

# Context & Application

Understanding data type memory sizes is fundamental to:

- Choosing between lists and tuples for data storage
- Understanding why strings (as lists of integers) are memory-intensive
- Estimating memory requirements for large data structures
- Understanding the cost of spawning processes (338 words base)
- Making informed decisions about ETS vs. process-based state storage

**Important architectural implications:**
- Strings as lists cost 2 words per character, making binaries far more memory-efficient for text
- The 32-key threshold for maps changes the internal representation from flat to HAMT
- Atoms have a 1-word in-process cost but a permanent global cost in the atom table
- Process base cost (338 words = ~2.7 KB on 64-bit) is small enough to make massive concurrency practical

# Examples

**Memory estimation examples** (derived from source: "Memory Usage"):

```
%% A 10-element list of small integers:
%%   1 word (list) + 10 * (1 word per element + 1 word per integer) = 21 words
%%   On 64-bit: 21 * 8 = 168 bytes

%% A 10-element tuple of small integers:
%%   2 words (tuple) + 10 * 1 word per integer = 12 words
%%   On 64-bit: 12 * 8 = 96 bytes

%% A 5-character string "hello":
%%   1 word + 5 * 2 words = 11 words
%%   On 64-bit: 11 * 8 = 88 bytes

%% A 5-byte binary <<"hello">>:
%%   3-6 words + 5 bytes of data
%%   On 64-bit: approximately 29-53 bytes (much less than the string)

%% A freshly spawned process:
%%   338 words = 2,704 bytes on 64-bit
```

**Checking word size at runtime** (derived from source):

```erlang
WordSize = erlang:system_info(wordsize).
%% Returns 4 (32-bit) or 8 (64-bit)
```

# Relationships

## Related

- **append-operator-efficiency** -- Understanding list memory layout explains why `++` copying is expensive
- **accidental-copying-in-closures** -- Memory sizes determine the cost of accidental copying
- **loss-of-sharing** -- The difference between shared and flat sizes matters for inter-process copying
- **erlang-system-limits** -- System limits interact with memory consumption (e.g., max atoms, max processes)

# Common Errors

- **Error**: Assuming strings are memory-efficient because they are a basic type
  **Correction**: Strings are lists of integers and cost 2 words per character; use binaries for text-heavy applications

- **Error**: Assuming lists and tuples have similar memory overhead
  **Correction**: Lists have 1 word per-element overhead (cons cell pointer), while tuples have only 2 words total overhead

# Common Confusions

- **Confusion**: Believing "1 word" means 1 byte
  **Clarification**: A word is 4 bytes on 32-bit and 8 bytes on 64-bit architectures

- **Confusion**: Thinking atom memory cost is just 1 word
  **Clarification**: An atom uses 1 word in the process heap, but also consumes space in the global atom table (which is never garbage-collected)

- **Confusion**: Assuming the memory table applies to all OTP versions identically
  **Clarification**: The figures are for erts-8.0 (OTP 19.0); while broadly applicable, exact sizes may vary across versions

# Source Reference

"Memory Usage" chapter. The source provides a comprehensive table of data type memory sizes for erts-8.0 (OTP 19.0), measured in words. The table covers all major Erlang data types plus ETS tables and processes.

# Verification Notes

- All memory sizes: Directly from the source table
- Word size definition: Explicit in source -- "A word is therefore 4 bytes or 8 bytes"
- Small integer ranges: Exact values from source (28-bit and 60-bit)
- Process size (338 words, 233 word heap): Explicit in source
- Large map sparsity factor (1.6-1.8): Explicit in source
- ETS initial size (768 words): Explicit in source
- Confidence: HIGH -- comprehensive table from official OTP documentation
