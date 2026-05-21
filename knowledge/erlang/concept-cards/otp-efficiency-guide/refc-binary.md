---
concept: Refc Binary
slug: refc-binary
category: performance
subcategory: binary-types
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Refc Binaries"
extraction_confidence: high
aliases:
  - "reference-counted binary"
  - "refc binary"
  - "ProcBin"
prerequisites: []
extends: []
related:
  - heap-binary
  - sub-binary
  - match-context
  - binary-append-optimization
  - forced-copying
contrasts_with:
  - heap-binary
answers_questions:
  - "What is a refc binary?"
  - "What distinguishes a refc binary from a heap binary?"
---

# Quick Definition

A refc binary is a reference-counted binary stored outside all process heaps, accessible via a ProcBin object on the process heap. It is used for binaries larger than 64 bytes and can be shared across multiple processes without copying the binary data.

# Core Definition

Refc binaries consist of two parts: a ProcBin object stored on the process heap, and the binary object itself stored outside all process heaps. The binary object can be referenced by any number of ProcBins from any number of processes. The object contains a reference counter to keep track of the number of references, so that it can be removed when the last reference disappears. All ProcBin objects in a process are part of a linked list, so that the garbage collector can keep track of them and decrement the reference counters in the binary when a ProcBin disappears (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Refc Binaries").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Consists of two parts: a ProcBin (on-heap) and the binary object (off-heap)
2. The binary object is stored outside all process heaps
3. Multiple ProcBins from multiple processes can reference the same binary object
4. Uses reference counting for memory management
5. Garbage collector tracks ProcBins via a linked list per process
6. Reference counters are decremented when a ProcBin is garbage-collected
7. The binary object is freed when its reference count reaches zero
8. Used for binaries larger than 64 bytes

# Construction / Recognition

## How a Refc Binary Is Created

1. When a binary larger than 64 bytes is created, the runtime allocates a binary object outside the process heap
2. A ProcBin is placed on the process heap pointing to the off-heap binary object
3. The binary object's reference counter is set to 1
4. When the binary is shared (e.g., sent to another process), a new ProcBin is created and the reference counter is incremented

## Recognizing a Refc Binary

1. Any binary larger than 64 bytes is a refc binary
2. A binary created by an append operation on a heap binary is promoted to a refc binary (with extra space allocated for growth)

# Context & Application

Refc binaries are the primary mechanism for efficient handling of large binary data in Erlang. Because the binary data lives outside the process heap and is reference-counted, sending a large binary to another process only copies the small ProcBin structure, not the entire binary payload. This makes message passing with large binaries efficient.

**Typical contexts:**
- File I/O buffers
- Network packet data
- Any binary data larger than 64 bytes
- Binaries shared across processes

The append optimization for binary construction creates refc binaries with extra allocated space (either twice the current size or 256 bytes, whichever is larger) to allow cheap subsequent appends.

# Examples

**Example** (source: "Constructing Binaries" section): When appending to a heap binary, the runtime creates a new refc binary:

```erlang
Bin0 = <<0>>,                    %% heap binary (1 byte)
Bin1 = <<Bin0/binary,1,2,3>>,    %% Bin0 copied into a NEW refc binary
```

Line 2 creates a refc binary because `Bin0` has not been involved in an append operation before. The ProcBin's size is set to the size of the data stored, while the binary object has extra space allocated -- either twice the size of `Bin1` or 256, whichever is larger (in this case, 256).

# Relationships

## Related

- **heap-binary** -- The other container type for binary data; binaries <= 64 bytes
- **sub-binary** -- A reference object that can point into a refc binary
- **match-context** -- An optimized reference object used during binary matching
- **binary-append-optimization** -- The append optimization creates refc binaries with extra space
- **forced-copying** -- Operations that invalidate the append optimization for refc binaries

## Contrasts With

- **heap-binary** -- Heap binaries are small (<= 64 bytes), stored directly on the process heap, and copied during garbage collection and message passing. Refc binaries are larger, stored off-heap, and shared via reference counting.

# Common Errors

- **Error**: Assuming sending a large binary in a message copies the binary data
  **Correction**: Only the ProcBin (a small on-heap structure) is copied; the binary object is shared via reference counting

- **Error**: Holding references to many large refc binaries without triggering garbage collection
  **Correction**: Unreferenced ProcBins are cleaned up during GC, which decrements the binary's reference counter. If GC runs infrequently, binary memory can accumulate.

# Common Confusions

- **Confusion**: Believing refc binaries are always more expensive than heap binaries
  **Clarification**: For large data, refc binaries are more efficient because they avoid copying the data during GC and message passing. The overhead of reference counting is small compared to the cost of copying large data.

- **Confusion**: Thinking the ProcBin contains the binary data
  **Clarification**: The ProcBin is just a pointer/reference on the process heap. The actual binary data is stored in a separate off-heap allocation.

# Source Reference

"Constructing and Matching Binaries," section "Refc Binaries." The source explicitly defines the two-part structure (ProcBin + binary object), the reference-counting mechanism, and the garbage collector's linked-list tracking of ProcBins.

# Verification Notes

- Definition: Directly from source section "Refc Binaries" -- explicit two-part structure described
- Key Properties: All items derived from explicit source statements
- The 64-byte threshold is stated in the "Heap Binaries" section (heap binaries are "up to 64 bytes")
- Example: Adapted from the line-by-line walkthrough in "Constructing Binaries"
- Confidence: HIGH -- explicit definition with detailed implementation description in official OTP documentation
