---
# === CORE IDENTIFICATION ===
concept: erl_driver Callback Functions
slug: driver-callbacks

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
  - ErlDrvEntry
  - DRIVER_INIT
  - driver callbacks

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linked-in-driver
extends: []
related:
  - driver-reentrancy
  - driver-memory-management
  - erl-ddll
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What callback functions does a linked-in driver implement?"
  - "What is the ErlDrvEntry structure?"
  - "What do the start, stop, and output callbacks do?"
---

# Quick Definition

A linked-in driver is implemented as a set of `erl_driver` callback functions registered with the VM through an `ErlDrvEntry` structure and the `DRIVER_INIT` macro.

# Core Definition

In a linked-in driver, communication is performed by a set of callback functions that the Erlang VM calls directly, using the `erl_driver` API (driver code includes `erl_driver.h`). You tell the VM about your callbacks by filling in an `ErlDrvEntry` structure with pointers to the functions you implemented, `NULL` for the rest, and a `driver_name` field; the `DRIVER_INIT` macro registers the structure. Some callbacks are life-cycle functions — `start` (called when `open_port/2` is invoked) and `stop` (called when the port closes) — and others handle data, like `output` (called when output is available from an Erlang process). Drivers may implement over a dozen callbacks but implement only the ones they need ("Erlang and OTP in Action," Ch. 12, Section 12.3.2).

# Prerequisites

- **Linked-in port driver** — Callbacks are how a driver is implemented.

# Key Properties

1. Defined via the `erl_driver` API; driver code includes `erl_driver.h`.
2. An `ErlDrvEntry` struct holds pointers to implemented callbacks (`NULL` for the rest) plus a `driver_name`.
3. The `DRIVER_INIT` macro registers the structure with the VM; its name must match `driver_name` unquoted.
4. `start` — called when `open_port/2` is invoked; allocates instance-specific data, returns it as `ErlDrvData`.
5. `stop` — called when the port closes; deallocates resources.
6. `output` — called when an Erlang process sends data to the port (unless `outputv` is defined).
7. Other callbacks include `init`, `ready_input`, `ready_output`, `finish`, `control`, `timeout`, `outputv`, `ready_async`, `flush`, `call`, `event`.
8. For every callback except `start`, the first argument is the `ErlDrvData` handle that `start` returned.

# Construction / Recognition

## To Construct/Create:
1. `#include <erl_driver.h>` and declare your callback functions.
2. Fill an `ErlDrvEntry` struct with callback pointers and the `driver_name`.
3. Register it with `DRIVER_INIT(name)` whose body returns the struct pointer.
4. Implement `start` (allocate instance data), `stop` (free it), and `output` (process incoming data).
5. Send results back to Erlang with `driver_output`.

## To Identify/Recognize:
1. C code with an `ErlDrvEntry` struct and a `DRIVER_INIT` macro invocation.

# Context & Application

- **Typical contexts**: Implementing the bridge between Erlang and C in a linked-in driver.
- **Common applications**: The JSON driver implements `drv_start`, `drv_stop`, and `drv_output`.
- **Historical/stylistic notes**: Most drivers implement `start`, `stop`, and possibly `init`, plus only the communication callbacks they actually need.

# Examples

**Example 1** (Listing 12.10): `drv_start` allocates a `drv_data_t`, stores the `ErlDrvPort`, and returns it as `ErlDrvData`; `drv_stop` frees it; `drv_output` forwards the buffer to `process_data`.

**Example 2** (Table 12.2): `output` is "called when output is available from some Erlang process to the port. Not used if the outputv callback is defined."

# Relationships

## Builds Upon
- **Linked-in port driver** — Callbacks are the implementation mechanism of a driver.

## Related
- **Linked-in driver reentrancy** — `start` allocates per-instance state passed to other callbacks.
- **erl_ddll module** — Loads the driver whose callbacks these are.

# Common Errors

- **Error**: Giving `DRIVER_INIT` a name different from the `driver_name` field.
  **Correction**: The `DRIVER_INIT` argument must match the `driver_name` string, but without quotes.

- **Error**: Implementing every callback in the `ErlDrvEntry` struct.
  **Correction**: Implement only the callbacks you need; leave the rest as `NULL`.

# Common Confusions

- **Confusion**: Thinking `start` also receives the `ErlDrvData` handle.
  **Clarification**: `start` creates and returns the handle; only the other callbacks receive it as their first argument.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.3.2 "The C side of the driver." See Listings 12.8 and 12.10 and Table 12.2.

# Verification Notes

- Definition source: Direct adaptation of Section 12.3.2 and Table 12.2.
- Confidence rationale: HIGH — the book lists the callbacks and shows their implementation.
- Uncertainties: Listing 12.8 appears as an image; structure described from surrounding prose; Listing 12.10 is given as text.
- Cross-reference status: `linked-in-driver` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
