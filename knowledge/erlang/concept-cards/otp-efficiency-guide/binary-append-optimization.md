---
concept: Binary Append Optimization
slug: binary-append-optimization
category: performance
subcategory: binary-memory-layout
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Constructing Binaries"
extraction_confidence: high
aliases:
  - "binary append optimization"
  - "binary growth optimization"
  - "binary construction optimization"
prerequisites:
  - refc-binary
  - heap-binary
  - binary-construction-efficiency
extends:
  - binary-construction-efficiency
related:
  - compiler-binary-optimization
  - forced-copying
contrasts_with: []
answers_questions:
  - "How do I efficiently construct a binary by appending data?"
  - "What must I understand before optimizing binary construction?"
---

# Quick Definition

The binary append optimization is a runtime mechanism that pre-allocates extra space in a refc binary so that subsequent append operations can store new data without copying the existing binary. The binary object is allocated at either twice the current size or 256 bytes, whichever is larger.

# Core Definition

When appending to a binary using the pattern `<<Binary/binary, ...>>` or `<<Binary/bitstring, ...>>`, the runtime system applies a special optimization to avoid copying the binary. On the first append to a heap binary, a new refc binary is created with extra space allocated -- either twice the size of the result or 256 bytes, whichever is larger. Subsequent appends store data in the unused space without copying. The ProcBin's size reflects the actual data, while the binary object's size includes the extra reserved space. Only the binary returned from the latest append operation supports further cheap appends (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Constructing Binaries").

# Prerequisites

- **refc-binary** -- The append optimization creates and grows refc binaries; understanding the ProcBin/binary-object structure is essential
- **heap-binary** -- The first append to a heap binary triggers promotion to a refc binary
- **binary-construction-efficiency** -- The basic rule (accumulator as first segment) must be understood before the optimization mechanism makes sense

# Key Properties

1. Applied automatically by the runtime when the append pattern `<<Bin/binary, ...>>` is used
2. First append to a non-append binary allocates a refc binary with extra space
3. Extra space is max(2 * result_size, 256) bytes
4. Subsequent appends use the reserved space without copying
5. Only the most recent append result supports cheap further appends
6. Appending to a previous version of the binary forces a copy
7. The ProcBin size tracks actual data; the binary object has the full allocation
8. The optimization works in its basic form without compiler support

# Construction / Recognition

## How the Optimization Works (Step by Step)

1. A heap binary `Bin0` exists (e.g., `<<0>>`)
2. First append: `Bin1 = <<Bin0/binary, 1, 2, 3>>` -- runtime creates a new refc binary with 256 bytes allocated (max(2*4, 256) = 256); copies `Bin0` into it; stores new data; ProcBin size = 4
3. Second append: `Bin2 = <<Bin1/binary, 4, 5, 6>>` -- 252 bytes of unused space remain; 3 new bytes stored in-place; no copy needed
4. Third append: `Bin3 = <<Bin2/binary, 7, 8, 9>>` -- 249 bytes remain; 3 bytes stored; no copy needed
5. Branching append: `Bin4 = <<Bin1/binary, 17>>` -- appending to `Bin1` (not the latest `Bin3`) forces a copy of `Bin1` into a new refc binary to preserve `Bin3`'s value

## Recognizing When the Optimization Applies

1. The binary being appended to is the first segment
2. The binary has been involved in a previous append (or is being converted from a heap binary)
3. No forced-copying conditions have been triggered (see forced-copying card)

# Context & Application

This optimization is what makes incremental binary construction in Erlang competitive with mutable buffer approaches in imperative languages. Without it, every append would copy the entire binary, resulting in O(n^2) behavior for building a binary of size n.

**Typical contexts:**
- Building network packets incrementally
- Accumulating binary data from a stream
- Any loop that constructs a binary by repeated appending

**Key insight:** The optimization maintains the illusion of immutability while achieving near-mutable performance. Only one "live" version of the binary supports cheap appends at any time. Appending to an older version triggers a copy to preserve the values of all versions (referential transparency).

# Examples

**Line-by-line append optimization walkthrough** (source: "Constructing Binaries" section):

```erlang
Bin0 = <<0>>,                    %% 1 - heap binary
Bin1 = <<Bin0/binary,1,2,3>>,    %% 2 - new refc binary, 256 bytes allocated
Bin2 = <<Bin1/binary,4,5,6>>,    %% 3 - appended in-place, 252 bytes left
Bin3 = <<Bin2/binary,7,8,9>>,    %% 4 - appended in-place, 249 bytes left
Bin4 = <<Bin1/binary,17>>,       %% 5 - Bin1 COPIED (would corrupt Bin3)
{Bin4,Bin3}                      %% 6
```

Line 5 is the critical case: appending to `Bin1` instead of the latest `Bin3`. The runtime must copy `Bin1` to a new refc binary because writing byte 17 into the existing binary object would change `Bin3`'s value from `<<0,1,2,3,4,5,6,7,8,9>>` to `<<0,1,2,3,4,17,6,7,8,9>>`.

# Relationships

## Builds Upon

- **binary-construction-efficiency** -- The basic "accumulator first" rule is a prerequisite for the optimization to apply

## Related

- **compiler-binary-optimization** -- The compiler can add hints that allow an even more efficient variant of this optimization
- **forced-copying** -- Circumstances that defeat or interrupt the append optimization

# Common Errors

- **Error**: Appending to an older version of the binary and expecting it to be cheap
  **Correction**: Only the most recent append result supports cheap further appends. Appending to an older version forces a copy.

- **Error**: Assuming the extra allocated space is always sufficient
  **Correction**: When the extra space is exhausted, the binary object is reallocated (moved to a larger allocation). The ProcBin pointer is updated. This is why only a single ProcBin can reference a growable binary.

# Common Confusions

- **Confusion**: Thinking the optimization is purely a compiler transformation
  **Clarification**: The basic append optimization is a runtime system feature. The compiler can enhance it with hints (see compiler-binary-optimization), but the fundamental mechanism works without compiler involvement.

- **Confusion**: Believing that all append patterns are equally efficient
  **Clarification**: Only `<<Bin/binary, ...>>` (binary as first segment) triggers the optimization. `<<..., Bin/binary>>` (prepending to the binary) always forces a copy.

- **Confusion**: Thinking that the "extra space" strategy wastes memory
  **Clarification**: The over-allocation follows a doubling strategy (or 256 bytes minimum) which provides amortized O(1) appends -- the same strategy used by dynamic arrays in many languages.

# Source Reference

"Constructing and Matching Binaries," section "Constructing Binaries." The source provides a complete 6-line walkthrough with line-by-line analysis explaining heap-to-refc promotion, in-place appending, and forced copying when branching.

# Verification Notes

- Definition: Synthesized from the detailed walkthrough -- "Appending to a binary or bitstring in the following way is specially optimized to avoid copying the binary"
- Allocation strategy: Explicitly stated -- "either twice the size of Bin1 or 256, whichever is larger"
- Branching copy behavior: Explicitly described in the Line 5 analysis
- Runtime vs. compiler distinction: Explicitly stated -- "The optimization in its basic form does not need any help from the compiler"
- Confidence: HIGH -- detailed line-by-line walkthrough with explicit explanations in official OTP documentation
