---
concept: Refc Binary
slug: refc-binary
category: data-types
subcategory: binaries
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Binaries"
extraction_confidence: high
aliases:
  - "Reference-counted binary"
  - "ProcBin"
prerequisites:
  - erlang-memory-model
related:
  - refc-binary-leak
  - erlang-memory-model
contrasts_with:
  - refc-binary-leak
answers_questions:
  - "What is a refc binary?"
  - "What are the two main types of binaries in Erlang?"
  - "What is the difference between a ProcBin and a refc binary?"
---

# Quick Definition

Erlang binaries come in two main types: small binaries (up to 64 bytes) allocated directly on a process's heap, and refc (reference-counted) binaries — larger binaries allocated in a global binary heap, referenced by a small ProcBin pointer on each process's local heap.

# Core Definition

From section "Binaries": "Erlang's binaries are of two main types: ProcBins and Refc binaries. Binaries up to 64 bytes are allocated directly on the process's heap, and their entire life cycle is spent in there. Binaries bigger than that get allocated in a global heap for binaries only, and each process to use one holds a local reference to it in its local heap. These binaries are reference-counted, and the deallocation will occur only once all references are garbage-collected from all processes that pointed to a specific binary."

# Prerequisites

- `erlang-memory-model` — refc binaries live in the `binary_alloc` allocator and use a virtual binary heap, both part of the memory model.

# Key Properties

1. Binaries up to 64 bytes ("heap binaries") live entirely on the owning process's heap.
2. Binaries larger than 64 bytes are refc binaries, allocated in a global binary-only heap (`binary_alloc`).
3. Each process using a refc binary holds a small local reference (a ProcBin) on its own heap.
4. A refc binary is reference-counted; deallocation happens only when every reference is garbage-collected from every process.
5. A virtual binary heap accounts for the real size of refc binaries when deciding when to garbage collect a process.
6. Refc binaries stored in an ETS table remain in the `binary_alloc` allocator.

# Construction / Recognition

A binary is created in the ordinary way; the runtime chooses heap allocation versus refc allocation based on the 64-byte threshold. A process's refc-binary references are visible through the `binary` process-info attribute, which lists the binaries that process points to.

# Context & Application

Refc binaries make passing large binaries between processes cheap — only the small ProcBin reference is copied, not the data. This mechanism "works entirely fine" in 99% of cases. The remaining cases — processes that do too little work to trigger GC, or that grow large heaps and then start handling many binaries — produce refc-binary leaks.

# Examples

From section "Binaries": "Binaries up to 64 bytes are allocated directly on the process's heap ... Binaries bigger than that get allocated in a global heap for binaries only, and each process to use one holds a local reference to it in its local heap."

# Relationships

## Builds Upon
- `erlang-memory-model` — refc binaries are allocated by the `binary_alloc` sub-allocator.

## Enables
- `refc-binary-leak` — refc binaries are the substrate that leaks when garbage collection lags.

## Related
- `refc-binary-leak-detection`, `refc-binary-leak-fixes` — diagnosis and remediation of refc-binary problems.

## Contrasts With
- `refc-binary-leak` — the binary itself is a normal data type; the leak is a pathological failure to reclaim it.

# Common Errors

- Treating all binaries identically; the 64-byte threshold determines heap vs. refc allocation and is the root of leak behaviour.

# Common Confusions

- A ProcBin is not the binary data — it is the small reference on a process's heap pointing to the actual refc binary in the global binary heap. The two are distinct (DG7).
- The 64-byte boundary separates heap binaries (no refcounting, no leak risk) from refc binaries (refcounted, leak-prone).

# Source Reference

Chapter 7: Memory Leaks, Section "Binaries". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Binaries."
- Confidence rationale: high — the source explicitly defines both binary types and the 64-byte threshold.
- Uncertainties: none.
- Cross-reference status: Verified
