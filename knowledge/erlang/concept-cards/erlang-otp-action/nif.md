---
# === CORE IDENTIFICATION ===
concept: Natively Implemented Function (NIF)
slug: nif

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
section: "12.1.3. Natively implemented functions (NIFs)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - NIF
  - natively implemented function
  - erl_nif

# === TYPED RELATIONSHIPS ===
prerequisites:
  - foreign-code-integration
extends: []
related:
  - nif-loading
  - nif-implementation-function
  - linked-in-driver
contrasts_with:
  - port
  - linked-in-driver

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a NIF?"
  - "How does a NIF differ from a port or a linked-in driver?"
  - "Why are NIFs only suitable for functions that return quickly?"
---

# Quick Definition

A NIF (natively implemented function) is a C function, written with the `erl_nif` API, that belongs to an Erlang module and is called like a normal Erlang function — fast, but a bug can crash the entire VM.

# Core Definition

Natively implemented functions (NIFs) allow you to create functions that behave just like Erlang's built-in functions (BIFs). Each NIF belongs to a specific Erlang module and is called like a normal Erlang function, although it is implemented in C via the `erl_nif` library. NIFs have minimal communication overhead and do not involve ports. The dangers are significant: a single bug in NIF code can easily crash the entire Erlang VM, and the native function runs in the context of the VM thread that calls it — that thread cannot be rescheduled until the NIF returns. This makes NIFs suitable only for functions that execute and return quickly ("Erlang and OTP in Action," Ch. 12, Sections 12.1.3 and 12.4).

# Prerequisites

- **Foreign code integration mechanisms** — A NIF is one of the three integration mechanisms.

# Key Properties

1. Implemented in C via the `erl_nif` library; on the Erlang side it looks like a normal function.
2. Belongs to a specific Erlang module and does not involve ports.
3. Minimal communication overhead — efficient.
4. A bug can crash the whole Erlang VM (a hard crash with only a core dump).
5. Runs in the calling VM thread, which cannot be rescheduled until the NIF returns.
6. Suitable only for functions that execute and return quickly; long-running NIFs hold up a scheduler.
7. `erl_nif` has its own functions for passing data and does not use the external term format.

# Construction / Recognition

## To Construct/Create:
1. On the Erlang side, write a module with exported stub functions whose bodies call `erlang:nif_error(nif_not_loaded)`.
2. Add an `init/0` that calls `erlang:load_nif(Path, LoadInfo)` and an `-on_load(init/0)` attribute.
3. On the C side, `#include <erl_nif.h>`; implement NIF functions with the signature `(ErlNifEnv*, int argc, const ERL_NIF_TERM argv[])`.
4. Fill in an `ErlNifFunc` array and register it with the `ERL_NIF_INIT` macro.
5. Compile to a shared library (no `erl_interface` linking needed).

## To Identify/Recognize:
1. A module with an `-on_load` attribute and stub functions calling `erlang:nif_error/1`, backed by C code using `ERL_NIF_INIT`.

# Context & Application

- **Typical contexts**: Adding fast, BIF-like library functions when ports are too slow.
- **Common applications**: Reimplementing the YAJL JSON parser interface as the `parse_document/1` NIF.
- **Historical/stylistic notes**: NIFs were a new addition to Erlang at the time of writing; the NIF API was finalized in OTP R14 (the book describes R13).

# Examples

**Example 1** (Section 12.4): The JSON parser is reimplemented as a NIF — no `gen_server`, no port, no supervision tree; all functionality lives in the `json_parser` module.

**Example 2** (Section 12.4.3): `json_parser:parse_document(<<"[null, true, {\"int\": 42}]">>)` returns `{ok,{undefined,true,[{<<"int">>,42}]}}` — identical results to the port and driver versions, but faster.

# Relationships

## Builds Upon
- **Foreign code integration mechanisms** — One of the three mechanisms.

## Enables
- **NIF library loading** — A NIF library is loaded via `erlang:load_nif/2` and `-on_load`.
- **NIF implementation function** — The C function that backs an Erlang NIF.

## Related
- **Linked-in driver** — Another in-VM mechanism, but port-based; NIFs share less code with port drivers.

## Contrasts With
- **Port** — A port isolates foreign code in a separate OS process; a NIF runs inside the VM thread.
- **Linked-in driver** — Both run in the VM, but a driver is still a port; a NIF is called like an ordinary function.

# Common Errors

- **Error**: Implementing long-running work as a NIF.
  **Correction**: NIFs block their scheduler thread until they return — keep them short, or use a port/driver for long work.

- **Error**: Choosing a NIF as the first integration approach.
  **Correction**: Consider the consequences of a hard VM crash; start with a plain port and use a NIF only when justified.

# Common Confusions

- **Confusion**: Thinking a NIF is just a faster kind of port.
  **Clarification**: A NIF does not involve ports at all — it is a C-implemented Erlang function with its own `erl_nif` API.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Sections 12.1.3 "Natively implemented functions (NIFs)" and 12.4 "Implementing the parser as a NIF."

# Verification Notes

- Definition source: Direct adaptation of Sections 12.1.3 and 12.4.
- Confidence rationale: HIGH — the book explicitly defines NIFs and their concurrency caveats.
- Uncertainties: The book describes the R13 NIF API; R14+ finalized it (allocation functions dropped the `ErlNifEnv` argument).
- Cross-reference status: `foreign-code-integration` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
