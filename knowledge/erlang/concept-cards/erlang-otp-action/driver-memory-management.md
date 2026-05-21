---
# === CORE IDENTIFICATION ===
concept: Linked-in Driver Memory Management
slug: driver-memory-management

# === CLASSIFICATION ===
category: tooling
subcategory: interoperability
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.3.2. The C side of the driver"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "driver_alloc"
  - "driver_free"
  - "driver_output"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linked-in-driver
  - driver-callbacks
extends: []
related:
  - driver-reentrancy
contrasts_with:
  - nif-memory-management

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should a linked-in driver allocate memory?"
  - "Why must a driver not use malloc and free?"
  - "How does a driver send data back to Erlang?"
---

# Quick Definition

A linked-in driver must manage memory with the `erl_driver` functions `driver_alloc`/`driver_realloc`/`driver_free` rather than C's `malloc`/`free`, and send results back with `driver_output`.

# Core Definition

Because a linked-in driver's code runs in the memory space of the Erlang VM, it should no longer use the standard C library functions `malloc` and `free`; it must instead use the `erl_driver` library functions `driver_alloc()` and `driver_free()` (and `driver_realloc()`), which do memory management in a thread-safe, reentrant way using the VM's specially tailored allocation routines. When the driver wants to send data back to the Erlang node as port output, it uses the `driver_output` API function, which writes a buffer to a specified port. The YAJL library is flexible enough to be told which allocation functions to use, so wrappers around the `driver_alloc` functions are supplied to it ("Erlang and OTP in Action," Ch. 12, Section 12.3.2).

# Prerequisites

- **Linked-in port driver** — These rules apply specifically to driver code.
- **erl_driver callback functions** — Memory management interacts with the driver callbacks.

# Key Properties

1. Use `driver_alloc`, `driver_realloc`, `driver_free` instead of `malloc`, `realloc`, `free`.
2. The `erl_driver` allocators are thread-safe, reentrant, and use the VM's tailored allocation routines.
3. Memory wrappers can be passed to YAJL via a `yajl_alloc_funcs` structure.
4. `driver_output(port, buffer, size)` sends a result buffer back to the port owner.
5. The port is stored in the instance-specific data struct so callbacks know where to output.
6. Both `malloc` sites in the original code (the container struct in `handle_start`, the `free` in `handle_end`) are replaced with `driver_alloc`/`driver_free`.

# Construction / Recognition

## To Construct/Create:
1. Replace every `malloc`/`realloc`/`free` in driver code with `driver_alloc`/`driver_realloc`/`driver_free`.
2. Write `alloc_func`/`realloc_func`/`free_func` wrappers and fill a `yajl_alloc_funcs` struct, passed to `yajl_alloc`.
3. Give `process_data` access to the port (via the instance-specific data) and call `driver_output(d->port, buf, sz)` to return results.

## To Identify/Recognize:
1. Driver C code calling `driver_alloc`/`driver_free`/`driver_output` and no `malloc`/`free`.

# Context & Application

- **Typical contexts**: Converting port-program C code into a linked-in driver.
- **Common applications**: The JSON driver swaps in `driver_alloc` for the container struct and passes `driver_*` wrappers to YAJL.
- **Historical/stylistic notes**: NIFs use the analogous `enif_alloc` family instead.

# Examples

**Example 1** (Listing 12.9): `alloc_func` calls `driver_alloc(sz)`, `realloc_func` calls `driver_realloc(ptr, sz)`, `free_func` calls `driver_free(ptr)`; these fill a `yajl_alloc_funcs` struct passed to `yajl_alloc`.

**Example 2** (Section 12.3.2): At the end of `process_data`, `write_packet(...)` is replaced with `driver_output(d->port, st.x.buff, st.x.buffsz)` to send the result back over the port.

# Relationships

## Builds Upon
- **Linked-in port driver** — Memory rules apply to driver code.
- **erl_driver callback functions** — `driver_output` returns data from within callbacks.

## Related
- **Linked-in driver reentrancy** — Per-instance memory must be allocated with `driver_alloc`.

## Contrasts With
- **NIF memory management** — A NIF uses `enif_alloc`/`enif_free` instead of the `driver_*` family.

# Common Errors

- **Error**: Using `malloc`/`free` in linked-in driver code.
  **Correction**: Use `driver_alloc`/`driver_free` for thread-safe, reentrant allocation in the VM.

- **Error**: Trying to write results to stdout from a driver.
  **Correction**: A driver has no stdout connection; use `driver_output(port, buf, sz)`.

# Common Confusions

- **Confusion**: Thinking driver memory functions are interchangeable with NIF ones.
  **Clarification**: Drivers use `driver_alloc`; NIFs use `enif_alloc` — different APIs for different mechanisms.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.3.2 — subsections "Memory management" and "Sending data back to Erlang." See Listing 12.9.

# Verification Notes

- Definition source: Direct adaptation of Section 12.3.2.
- Confidence rationale: HIGH — the book explicitly prescribes `driver_alloc`/`driver_output` and shows the wrappers.
- Uncertainties: None.
- Cross-reference status: `linked-in-driver` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
