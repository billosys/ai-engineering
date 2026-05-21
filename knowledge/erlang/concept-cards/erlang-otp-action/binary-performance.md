---
# === CORE IDENTIFICATION ===
concept: Heap Binaries vs. Reference-Counted Binaries
slug: binary-performance

# === CLASSIFICATION ===
category: performance
subcategory: memory
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.3.1. Binaries and bitstrings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "heap binary"
  - "reference-counted binary"
  - "refc binary"
  - "bin_opt_info"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - data-type-sizes
extends: []
related:
  - list-performance
  - boxed-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between a heap binary and a reference-counted binary?"
  - "When is binary data copied between processes?"
  - "How can you check whether your code uses binaries efficiently?"
---

# Quick Definition

Erlang has two main binary kinds: small heap binaries (up to 64 bytes, copied like any term) and large reference-counted binaries (shared globally, passed between processes as just a pointer).

# Core Definition

Binaries and bitstrings are chunks of bytes whose representation resembles bignums but is more complex because several kinds exist under the surface. There are two main types. *Heap binaries* (small) are up to 64 bytes; they are stored on the process's own heap, like a float or bignum, and are copied when passed in a message. *Reference-counted binaries* (large) are stored in a separate global memory area shared by all processes, with garbage collection handled by reference counting; when passed between processes within the same VM, only a pointer is transferred, saving copying. The compiler flag `bin_opt_info` makes the compiler print warnings about how binaries are used (Chapter 14, Section 14.3.1).

# Prerequisites

- **Memory sizes of Erlang data types** — Binaries are the "3-6 words + data size / word size" entry in Table 14.1.

# Key Properties

1. Heap binaries are up to 64 bytes, stored on the owning process's heap.
2. Heap binaries are copied when passed in a message, like any other term.
3. Reference-counted ("refc") binaries are large, stored in a global shared memory area.
4. Refc binaries are garbage collected by reference counting.
5. Passing a refc binary between processes in the same VM transfers only a pointer — no copy.
6. The distinction is invisible to the programmer; exploiting it for efficiency hacks is discouraged.
7. The `bin_opt_info` compiler flag (e.g. via `ERL_COMPILER_OPTIONS=[bin_opt_info]`) reports how binaries are used.

# Construction / Recognition

## To Identify/Recognize:
1. Compile with the `bin_opt_info` flag to get compiler warnings about binary usage.
2. Set `ERL_COMPILER_OPTIONS` to `[bin_opt_info]` as an OS environment variable to enable it.

# Context & Application

- **Typical contexts**: Handling large blobs of data — files, network buffers, stored text.
- **Common applications**: Letting one process read a large binary from a file or port and pass it on to another without copying.
- **Historical/stylistic notes**: The book says exploiting the no-copy property deliberately is "ugly" and should be a last resort.

# Examples

**Example 1** (Section 14.3.1): A process reads a large chunk of binary data from a file or port and passes it to a second process; only a pointer is transferred.

**Example 2** (Section 14.3.1 sidebar): Converting strings to binaries can shrink them by a factor of 8 (or 16 on 64-bit) compared to lists of character codes.

# Relationships

## Related
- **List performance** — Strings as lists cost two words per character; binaries are far more compact.
- **Boxed representation** — Binaries, like bignums, use a multi-word boxed-style layout.

# Common Errors

- **Error**: Assuming all binaries avoid copying between processes.
  **Correction**: Only large reference-counted binaries are passed by pointer; small heap binaries (≤64 bytes) are copied.

# Common Confusions

- **Confusion**: Thinking the heap vs. refc distinction is something you choose explicitly.
  **Clarification**: The runtime decides based on size; the difference is invisible to your code.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.1 "Binaries and bitstrings."

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.1.
- Confidence rationale: HIGH — both binary kinds are explicitly defined.
- Uncertainties: The 64-byte heap-binary threshold is implementation-specific.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
