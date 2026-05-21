---
# === CORE IDENTIFICATION ===
concept: Erlang Memory Safety
slug: erlang-memory-safety

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: security-model
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Memory Management"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "BEAM memory management"
  - "Erlang memory model"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
extends: []
related:
  - native-code-safety
  - atom-exhaustion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang prevent memory safety vulnerabilities?"
  - "Can use-after-free or buffer overflow bugs occur in Erlang?"
  - "What memory-related CWEs are eliminated by the BEAM?"
  - "Can memory leaks occur in Erlang despite garbage collection?"
---

# Quick Definition

Erlang is a memory-safe language with automatic memory management: per-process heaps with individual garbage collection, shared large binaries, and ETS for in-memory term storage. This eliminates entire classes of memory vulnerabilities (use-after-free, buffer overflows, uninitialized variables) while still requiring developers to manage data references to avoid retention issues.

# Core Definition

As stated in the Secure Coding Guidelines: "Erlang is a memory-safe language, with automatic memory management handled by its runtime system. Each process primarily allocates data on its own heap, while large binaries can be shared efficiently between processes. Process heaps undergo individual garbage collection, ensuring that unused memory within a process is reclaimed promptly." The source further notes that "CWE categories related to memory safety (both spatial and temporal), such as CWE-416, CWE-465, or CWE-1218, cannot occur."

# Prerequisites

- **Erlang Threat Model** -- understanding the scope of safety guarantees requires knowing the overall threat model.

# Key Properties

1. **Per-process heaps** -- each process allocates data on its own heap, providing natural isolation.
2. **Individual garbage collection** -- process heaps undergo independent GC, ensuring unused memory is reclaimed promptly without global pauses.
3. **Shared large binaries** -- large binaries can be shared efficiently between processes without copying.
4. **ETS automatic allocation** -- memory for ETS entries is allocated on insertion and freed on removal.
5. **No spatial memory safety violations** -- out-of-bounds read (CWE-125), out-of-bounds write (CWE-787), buffer overflow (CWE-120), stack-based overflow (CWE-121), heap-based overflow (CWE-122), and improper buffer operations (CWE-119) cannot occur.
6. **No temporal memory safety violations** -- use-after-free (CWE-416) and similar errors cannot occur.
7. **No uninitialized variables** -- errors relating to the use of uninitialized variables cannot occur.
8. **No classical data races** -- race conditions can only affect application logic; CWE-362 cannot occur unless the programmer has explicitly built a shared resource.
9. **No classical memory leaks** -- memory that is no longer referenced will eventually be reclaimed by the garbage collector (CWE-401).

# Construction / Recognition

## To Apply:
1. Write pure Erlang code to benefit from full memory safety guarantees.
2. Drop references to unused data promptly -- while GC prevents leaks, holding unnecessary references can cause memory retention (similar to leaks in managed languages).
3. Avoid importing memory-unsafe code through FFI (NIFs, drivers) unless absolutely necessary.
4. Monitor binary reference counting -- large shared binaries may not be reclaimed promptly if references persist across processes.

## To Recognize:
1. Pure Erlang code is inherently memory-safe -- no special effort required.
2. Memory retention issues manifest as growing process heaps or unreleased binary references, not as safety violations.

# Context & Application

Erlang's memory safety eliminates the most severe and commonly exploited vulnerability classes in systems programming. Out of the CWE Top 25 for 2025, the source explicitly marks CWE-787 (Out-of-bounds Write, rank 5), CWE-416 (Use After Free, rank 7), CWE-125 (Out-of-bounds Read, rank 8), CWE-120 (Buffer Overflow, rank 11), CWE-476 (NULL Pointer Dereference, rank 13), CWE-121 (Stack-based Buffer Overflow, rank 14), CWE-122 (Heap-based Buffer Overflow, rank 16), and CWE-119 (Improper Buffer Operations, rank 38) as issues that "cannot occur because Erlang is memory safe." This safety can be violated by loading native code through NIFs or drivers.

# Examples

**Example 1** (secure_coding.md, "What is protected against"): "This safety extends to concurrent operation and race conditions can only affect application logic, which is further limited as Erlang only provides message-passing (as opposed to memory-sharing) concurrency; a classical data race (CWE-362) cannot occur unless the programmer has explicitly built a shared resource for which it can happen."

**Example 2** (secure_coding.md, "Memory Management"): "Erlang's automatic memory management prevents memory leaks by releasing memory once there are no remaining references. However, developers must still make sure to drop references to unused data, just as in other programming languages. Failing to do so can lead to memory retention issues similar to leaks, which may cause performance degradation or potentially become exploitable vulnerabilities."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- memory safety is one of the core guarantees defined by the threat model

## Enables
- **Secure Error Handling** -- memory safety means a crash always leaves the system in a well-defined state, enabling safe process restart

## Related
- **Native Code Safety** -- NIFs and drivers can violate memory safety guarantees
- **Atom Exhaustion** -- atoms are a special case of memory management where allocation is permanent

## Contrasts With
- No direct contrasts in source, though the document implicitly contrasts Erlang with C/C++ and other memory-unsafe languages.

# Common Errors

- **Error**: Assuming that garbage collection eliminates all memory-related concerns.
  **Correction**: Developers must still drop references to unused data; holding references indefinitely creates retention issues similar to memory leaks that can cause performance degradation or become exploitable.

- **Error**: Assuming memory safety extends to NIF and driver code.
  **Correction**: "Importing memory-unsafe code through the Foreign Function Interfaces (FFI), such as drivers and Native Implemented Functions (NIFs), may, of course, violate this property."

# Common Confusions

- **Confusion**: Believing "no memory leaks" means memory usage is always optimal.
  **Clarification**: Classical memory leaks (unreferenced memory never freed) cannot occur, but data explicitly referenced longer than necessary can grow unboundedly -- for example, a cache without an eviction strategy.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, "Memory Management" section and "What is protected against" subsection (secure_coding.md, lines 96-141, 204-226). Also informed by the "Top 40 CWEs" section where memory safety CWEs are marked as non-applicable.

# Verification Notes

- Definition source: Directly quoted from the "Memory Management" and "What is protected against" sections.
- Confidence rationale: High -- explicit statements with specific CWE references throughout the document.
- Uncertainties: None.
- Cross-reference status: References CWE-416, CWE-465, CWE-1218, CWE-362, CWE-190, CWE-401, CWE-787, CWE-125, CWE-120, CWE-476, CWE-121, CWE-122, CWE-119.
