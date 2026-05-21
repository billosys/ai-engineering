---
# === CORE IDENTIFICATION ===
concept: Linked-in Port Driver
slug: linked-in-driver

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
section: "12.1.2. Linked-in port drivers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - port driver
  - linked-in driver
  - erl_driver

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
  - foreign-code-integration
extends:
  - port
related:
  - driver-callbacks
  - driver-reentrancy
  - erl-ddll
  - nif
contrasts_with:
  - port
  - nif

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a linked-in port driver?"
  - "How does a linked-in driver differ from a plain port?"
  - "What is the safety trade-off of a linked-in driver?"
---

# Quick Definition

A linked-in port driver is a shared library, usually written in C, dynamically loaded and linked into the Erlang VM — faster than a plain port but able to crash the entire VM.

# Core Definition

The second kind of port uses linked-in drivers, often called *port drivers*. A linked-in driver is a shared library, usually written in C, that is loaded and linked dynamically with the Erlang VM. Superficially it works exactly like a plain port — communication is byte-oriented, and from the Erlang code's point of view both kinds of port look the same — but the linked-in driver executes in the same operating system process space as the Erlang VM, through the `erl_driver` API of callback functions and buffers. The main purpose is performance: communication is faster. The severe drawback is that if the port driver crashes, it brings down the entire Erlang system ("Erlang and OTP in Action," Ch. 12, Sections 12.1 and 12.1.2).

# Prerequisites

- **Port** — A linked-in driver is a kind of port.
- **Foreign code integration mechanisms** — It is one of the three integration mechanisms.

# Key Properties

1. A shared library (a `.so` on UNIX, a `.dll` on Windows) loaded and linked dynamically into the Erlang VM.
2. Communication is byte-oriented, as with plain ports; both port kinds look identical from Erlang.
3. Executes in the same OS process space as the Erlang VM — faster communication.
4. A crash or corruption in the driver brings down the entire Erlang system.
5. Uses the `erl_driver` C API with callback functions and buffers instead of stdin/stdout.
6. Easy to migrate to from a plain port because the Erlang-side view is the same.
7. Trades safety for speed — make this trade only when speed is proven necessary.

# Construction / Recognition

## To Construct/Create:
1. Take working plain-port C code and replace `main` with `erl_driver` callbacks (`start`, `stop`, `output`).
2. `#include <erl_driver.h>`; fill in an `ErlDrvEntry` struct with callback pointers and a `driver_name`.
3. Register it with the `DRIVER_INIT` macro returning a pointer to the struct.
4. Define an instance-specific data struct; allocate it in `start`, free it in `stop`.
5. Use `driver_alloc`/`driver_free` (not `malloc`/`free`) and `driver_output` to send data back.
6. Compile to a shared library (`gcc -fpic -shared ...`); load it from Erlang with `erl_ddll:load/2`.

## To Identify/Recognize:
1. A C file including `erl_driver.h` and using `DRIVER_INIT` and an `ErlDrvEntry` structure.

# Context & Application

- **Typical contexts**: Speeding up an already-stable port-based integration.
- **Common applications**: Converting the YAJL JSON parser from an external `jp_prog` program to `jp_driver.so`.
- **Historical/stylistic notes**: Creating a linked-in driver should almost never be the first step — start from a proven plain port.

# Examples

**Example 1** (Section 12.1.2, Figure 12.2): A linked-in driver lives in the same OS process space as the Erlang VM, using a C API with callback functions and buffers to transfer data.

**Example 2** (Section 12.3): The chapter copies `jp_prog.c` to `jp_driver.c`, deletes `main`/`write_packet`/`read_packet`/`read_bytes`, and adds `erl_driver` callbacks — the parser logic itself is unchanged.

# Relationships

## Builds Upon
- **Port** — A linked-in driver is the second flavor of port.
- **Foreign code integration mechanisms** — One of the three mechanisms.

## Enables
- **Driver callbacks** — A driver is implemented through `erl_driver` callbacks.
- **Driver reentrancy** — Driver code must be written reentrantly.

## Related
- **erl_ddll module** — Loads the shared library from Erlang.

## Contrasts With
- **Port (plain)** — A plain port isolates foreign code in a separate OS process; a linked-in driver shares the VM's address space.
- **NIF** — Both run inside the VM, but a NIF is called as a normal function; a driver is still a port.

# Common Errors

- **Error**: Using `malloc`/`free` in linked-in driver code.
  **Correction**: Use `driver_alloc`/`driver_free` so memory management is thread-safe and reentrant within the VM.

- **Error**: Choosing a linked-in driver before a plain port has been tried and proven too slow.
  **Correction**: Start with a plain port; move to a driver only when speed is the proven problem.

# Common Confusions

- **Confusion**: Thinking a linked-in driver is as safe as a plain port because "they look the same."
  **Clarification**: They look the same from Erlang, but a driver runs inside the VM — a crash takes down the whole node.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Sections 12.1.2 "Linked-in port drivers" and 12.3 "Making a linked-in driver." See Figure 12.2.

# Verification Notes

- Definition source: Direct adaptation of Sections 12.1.2 and 12.3.
- Confidence rationale: HIGH — the book explicitly defines linked-in drivers and their trade-offs.
- Uncertainties: None.
- Cross-reference status: `port`, `foreign-code-integration` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
