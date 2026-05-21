---
# === CORE IDENTIFICATION ===
concept: Driver Binary Handling
slug: driver-binary-handling

# === CLASSIFICATION ===
category: system-configuration
subcategory: drivers
tier: advanced

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Drivers"
chapter_number: null
pdf_page: null
section: "Avoiding Copying Binaries When Calling a Driver"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "driver binary optimization"
  - "port binary handling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - refc-binary
  - heap-binary
  - driver-concurrency
extends: []
related:
  - binary-construction-efficiency
  - binary-append-optimization
  - forced-copying
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I avoid copying binaries when communicating with a driver?"
  - "How do I return large binaries from a driver without copying?"
  - "When should I return heap binaries vs refc binaries from a driver?"
---

# Quick Definition

Efficient binary handling in Erlang drivers requires careful use of specific API calls to avoid unnecessary copying of binary data when sending to or returning from drivers. The approach differs depending on whether binaries are small (up to 64 bytes) or large.

# Core Definition

When communicating with Erlang port drivers, binaries can be passed and returned without copying if the right API calls are used. For sending binaries to a driver, `port_control/3` passes a pointer to the binary contents without copying when the `Data` argument is a binary (not an iolist). For returning binaries, the driver should use different strategies depending on binary size: small binaries (up to 64 bytes) benefit from being returned as heap binaries, while large binaries should be pre-allocated with `driver_alloc_binary()` to avoid copying (Erlang Efficiency Guide, "Drivers" section).

# Prerequisites

- **Refc binary** — Understanding reference-counted binary storage is essential for knowing when binaries are shared vs copied
- **Heap binary** — Understanding the 64-byte threshold determines the return strategy
- **Driver concurrency** — The port locking model affects whether binary-passing strategies are safe

# Key Properties

1. `port_control/3` with a binary argument passes a pointer without copying
2. `port_control/3` with an iolist argument copies all binaries in the iolist
3. The `outputv` callback in drivers allows refc binaries in iolists to be passed as references via `port_command/2`
4. Binaries up to 64 bytes are best returned as heap binaries using `driver_output()` or `erl_drv_output_term()` with `ERL_DRV_BUF2BINARY`
5. Large binaries should be allocated with `driver_alloc_binary()` to avoid copying
6. Large binaries can be returned via `control` callback (with `PORT_CONTROL_FLAG_BINARY`), `driver_output_binary()`, or `erl_drv_output_term()`/`erl_drv_send_term()`

# Construction / Recognition

## To Send Binaries to a Driver Without Copying

1. Use `port_control/3` with the `Data` argument as a plain binary (not wrapped in a list)
2. If sending both a binary and extra data, call `port_control/3` twice — once with the binary and once with the extra data
3. Note: the two-call approach only works safely with a single process communicating with the port
4. Alternatively, implement an `outputv` callback in the driver and use `port_command/2` with an iolist containing refc binaries

## To Return Binaries From a Driver Without Copying

1. For small binaries (up to 64 bytes): use `driver_output()` or `erl_drv_output_term()` with `ERL_DRV_BUF2BINARY` to let the runtime construct a heap binary
2. For large binaries: allocate with `driver_alloc_binary()`, then send via one of the available methods (`control` callback, `driver_output_binary()`, or term-building functions)

# Context & Application

- **Typical contexts**: High-throughput driver communication, network protocol handlers, file I/O drivers, hardware interface drivers
- **Common applications**: Any driver that transfers significant amounts of binary data between Erlang and C code
- **Performance note**: Heap binaries (up to 64 bytes) require less memory when not sent to other processes and have cheaper garbage collection, making them preferable for small return values

# Examples

**Example 1** (Drivers section, "Avoiding Copying Binaries When Calling a Driver"): When calling `port_control/3`, passing a binary directly avoids copying:

```erlang
port_control(Port, Command, Binary)
```

But passing an iolist causes all binaries to be copied:

```erlang
port_control(Port, Command, [Binary, ExtraData])
```

**Example 2** (Drivers section, "Returning Large Binaries without Copying from a Driver"): To return a large binary from a driver's `control` callback without copying, first call `set_port_control_flags()` with `PORT_CONTROL_FLAG_BINARY`, then allocate the binary with `driver_alloc_binary()` and return it from the callback.

# Relationships

## Builds Upon

- **Refc binary** — Large driver binaries are returned as refc binaries that can be shared across processes
- **Heap binary** — Small driver binaries (up to 64 bytes) are best returned as heap binaries

## Enables

- Efficient driver communication patterns for high-throughput systems

## Related

- **Binary construction efficiency** — General binary construction principles apply to driver output
- **Forced copying** — Understanding when binaries are copied helps choose the right driver API
- **Driver concurrency** — Port locking affects safety of multi-call binary passing

## Contrasts With

- Default iolist passing, which copies all binaries

# Common Errors

- **Error**: Wrapping a binary in a list when calling `port_control/3`, causing an unnecessary copy
  **Correction**: Pass the binary directly as the `Data` argument, not inside a list

- **Error**: Using `port_control/3` twice from multiple processes, causing race conditions
  **Correction**: The two-call approach for sending binary + extra data only works with a single process per port; use `outputv` callback with `port_command/2` for multi-process scenarios

- **Error**: Pre-allocating a binary for small return values in a driver
  **Correction**: For binaries up to 64 bytes, use `driver_output()` or `erl_drv_output_term()` with `ERL_DRV_BUF2BINARY` to let the runtime create a heap binary

# Common Confusions

- **Confusion**: Believing that all binaries passed to drivers are automatically zero-copy
  **Clarification**: Only `port_control/3` with a plain binary argument (not iolist) avoids copying; iolists always copy. For `port_command/2`, the driver must implement the `outputv` callback to receive refc binary references

- **Confusion**: Thinking larger binaries are always more expensive to return from drivers
  **Clarification**: Large binaries allocated with `driver_alloc_binary()` are returned as refc binaries without copying; it is actually small binaries that get copied (as heap binaries), though this is efficient for their size

# Source Reference

Drivers chapter, sections "Avoiding Copying Binaries When Calling a Driver," "Returning Small Binaries from a Driver," and "Returning Large Binaries without Copying from a Driver."

# Verification Notes

- Definition source: Synthesized from three related sections in the Drivers chapter
- Confidence rationale: HIGH — explicit API-level guidance in official OTP documentation
- Uncertainties: None; the driver API calls and their behavior are well-documented
- Cross-reference status: Slugs for refc-binary, heap-binary, driver-concurrency verified as co-extracted cards
