---
concept: Heap Binary
slug: heap-binary
category: performance
subcategory: binary-types
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Heap Binaries"
extraction_confidence: high
aliases:
  - "heap binary"
prerequisites: []
extends: []
related:
  - refc-binary
  - sub-binary
  - match-context
contrasts_with:
  - refc-binary
answers_questions:
  - "What is a heap binary?"
  - "What distinguishes a refc binary from a heap binary?"
---

# Quick Definition

A heap binary is a small binary (up to 64 bytes) stored directly on the process heap. Unlike refc binaries, heap binaries are copied during garbage collection and when sent as messages, and require no special handling by the garbage collector.

# Core Definition

Heap binaries are small binaries, up to 64 bytes, and are stored directly on the process heap. They are copied when the process is garbage-collected and when they are sent as a message. They do not require any special handling by the garbage collector (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Heap Binaries").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Maximum size is 64 bytes
2. Stored directly on the process heap (inline with other heap data)
3. Copied during garbage collection (like any other heap term)
4. Copied when sent as a message to another process
5. No reference counting needed
6. No special garbage collector handling required
7. When used in an append operation, the result is promoted to a refc binary

# Construction / Recognition

## How a Heap Binary Is Created

1. Create any binary that is 64 bytes or smaller: `<<1,2,3>>`, `<<"hello">>`, etc.
2. The binary data is allocated directly on the process heap

## Recognizing a Heap Binary

1. Any binary of 64 bytes or fewer is a heap binary
2. Binaries created by literals or small constructions are typically heap binaries

# Context & Application

Heap binaries are the simple, lightweight form of binary storage in Erlang. For small binaries, the overhead of reference counting (as used by refc binaries) would outweigh the cost of simply copying the data. By storing small binaries directly on the heap, the runtime avoids the indirection and bookkeeping of ProcBin structures and off-heap allocation.

**Typical contexts:**
- Small protocol headers or tags
- Short strings stored as binaries
- Small binary literals in code
- Intermediate results in binary pattern matching

**Important behavior during append:** When a heap binary is used as the base for a binary append operation, the runtime copies it into a new refc binary with extra space allocated for growth. This is a one-time cost that enables subsequent appends to be cheap.

# Examples

**Example** (source: "Constructing Binaries" section):

```erlang
Bin0 = <<0>>,                    %% 1-byte heap binary
Bin1 = <<Bin0/binary,1,2,3>>,    %% Bin0 (heap binary) copied into a refc binary
```

`Bin0` is a 1-byte binary, well under the 64-byte threshold, so it is stored as a heap binary. When it is used in the append operation on line 2, the runtime copies it into a new refc binary because heap binaries are not set up for the append optimization.

# Relationships

## Related

- **refc-binary** -- The other container type for binary data; used for binaries > 64 bytes
- **sub-binary** -- A reference object that can point into a heap binary
- **match-context** -- An optimized reference object that can reference a heap binary during matching

## Contrasts With

- **refc-binary** -- Refc binaries are larger (> 64 bytes), stored off-heap, reference-counted, and shared across processes without copying. Heap binaries are small (<= 64 bytes), stored on-heap, and fully copied during GC and message passing.

# Common Errors

- **Error**: Creating many small binaries and sending them between processes, expecting zero-copy behavior
  **Correction**: Heap binaries are fully copied when sent as messages. Only refc binaries benefit from shared, reference-counted storage.

# Common Confusions

- **Confusion**: Thinking the 64-byte threshold can be configured or tuned
  **Clarification**: The 64-byte boundary is a fixed implementation detail of the Erlang runtime system

- **Confusion**: Believing that a heap binary involved in an append stays a heap binary
  **Clarification**: When a heap binary is the base of an append operation, it is promoted to a refc binary. The heap binary data is copied into a new off-heap binary object with extra space for growth.

# Source Reference

"Constructing and Matching Binaries," section "Heap Binaries." The source provides a concise definition (one paragraph) specifying the 64-byte limit, on-heap storage, copying behavior during GC and messaging, and the absence of special GC handling.

# Verification Notes

- Definition: Quoted nearly verbatim from source -- "Heap binaries are small binaries, up to 64 bytes, and are stored directly on the process heap"
- Key Properties: All items explicitly stated or directly derivable from the source paragraph
- The promotion-to-refc behavior during append is from the "Constructing Binaries" section
- Confidence: HIGH -- explicit, concise definition in official OTP documentation
