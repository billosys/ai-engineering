---
concept: "erlang:system_info/1"
slug: erlang-system-info
category: production-ops
subcategory: introspection
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erlang:system_info"
chapter_number: null
pdf_page: null
section: "erlang:system_info"
extraction_confidence: high
aliases:
  - "system_info"
  - "erlang:system_info"
  - "system introspection BIF"
prerequisites:
  - erl-command
extends: []
related:
  - emulator-flags
  - erlang-monotonic-time
  - erlang-system-time
  - time-warp-modes
  - erts-alloc
  - crash-dump
contrasts_with: []
answers_questions:
  - "How do I query runtime system information in Erlang?"
  - "How do I find out how many schedulers are running?"
  - "How do I check the memory allocation state?"
  - "How do I get the OTP version at runtime?"
---

# Quick Definition

`erlang:system_info/1` is a BIF that returns information about the current Erlang runtime system. It accepts an atom or tuple key and returns data about memory allocation, CPU topology, processes, system limits, time, schedulers, distribution, and general system properties.

# Core Definition

The documentation states: "Returns information about the current system." The function is organized into the following categories:

**Memory Allocation:** `allocated_areas`, `allocator`, `{allocator, Alloc}`, `alloc_util_allocators`, `{allocator_sizes, Alloc}` -- information about memory allocators and their state.

**CPU Topology:** `cpu_topology`, `{cpu_topology, defined | detected | used}`, `logical_processors`, `logical_processors_available`, `logical_processors_online`, `cpu_quota`, `update_cpu_info` -- CPU and processor layout detection.

**Process Information:** `fullsweep_after`, `garbage_collection`, `heap_sizes`, `heap_type`, `max_heap_size`, `message_queue_data`, `min_heap_size`, `min_bin_vheap_size`, `procs` -- default process heap settings and process dumps.

**System Limits:** `atom_count`, `atom_limit`, `ets_count`, `ets_limit`, `port_count`, `port_limit`, `process_count`, `process_limit` -- current counts and configured maximums for atoms, ETS tables, ports, and processes.

**System Time:** `end_time`, `os_monotonic_time_source`, `os_system_time_source`, `start_time`, `time_correction`, `time_offset`, `time_warp_mode`, `tolerant_timeofday` -- time source and correction information.

**Scheduler Information:** `dirty_cpu_schedulers`, `dirty_cpu_schedulers_online`, `dirty_io_schedulers`, `multi_scheduling`, `schedulers`, `schedulers_online`, `scheduler_id`, `scheduler_bind_type`, `scheduler_bindings`, `thread_pool_size` -- scheduler thread configuration and state.

**Distribution Information:** `creation`, `dist`, `dist_ctrl`, `dist_buf_busy_limit`, `delayed_node_table_gc`, `async_dist` -- distributed node connectivity and settings.

**System Information:** `system_version`, `otp_release`, `version`, `wordsize`, `machine`, `system_architecture`, `kernel_poll`, `emu_flavor`, `emu_type`, `nif_version`, `driver_version`, `c_compiler_used` -- version strings, architecture, and build information.

# Prerequisites

- **erl-command** -- The values returned by `system_info` reflect settings established by erl command-line flags

# Key Properties

1. Takes a single argument -- an atom or a tuple -- specifying what information to return
2. Return types vary by key: integers, strings, booleans, tuples, lists, or binaries
3. Many keys correspond directly to emulator flags (e.g., `schedulers` reflects `+S`, `process_limit` reflects `+P`)
4. Some keys return formatted binary strings similar to crash dump output (`info`, `procs`, `dist`)
5. `update_cpu_info` is unique in that it triggers a side-effect (re-reading CPU info) and returns `changed` or `unchanged`
6. `wordsize` returns the Erlang term word size in bytes (4 on 32-bit, 8 on 64-bit); `{wordsize, external}` returns the true pointer size

# Construction / Recognition

## To Construct/Create:

Call the BIF with the desired information key:

```erlang
1> erlang:system_info(schedulers).
8
2> erlang:system_info(process_limit).
1048576
3> erlang:system_info(otp_release).
"27"
4> erlang:system_info(system_version).
"Erlang/OTP 27 [erts-15.0] [source] [64-bit] [smp:8:8] ..."
5> erlang:system_info(wordsize).
8
```

## To Identify/Recognize:

1. Any call to `erlang:system_info(Key)` is querying the runtime system
2. The function is in the `erlang` module and is a BIF (built-in function)
3. It is a read-only introspection function (except `update_cpu_info`)

# Context & Application

`erlang:system_info/1` is the primary introspection BIF for production monitoring and diagnostics. It is used by tools like `observer`, `recon`, and custom monitoring code to understand the state of a running system. The system limits keys (`process_count`, `port_count`, `atom_count` vs. their `_limit` counterparts) are commonly checked to detect resource exhaustion risks.

The `otp_release` key returns only the major version number (e.g., "27"), not the full patch version. The documentation notes: "No `erlang:system_info()` argument gives the exact OTP version. This is because the exact OTP version in the general case is difficult to determine."

Allocator information (`allocator`, `{allocator, Alloc}`) is "intended for debugging, and the content is highly implementation-dependent" and can change without notice.

# Examples

**Example 1** (erlang:system_info documentation, "System Limits" section): Checking process counts:

```erlang
erlang:system_info(process_count).  %% Current number of processes
erlang:system_info(process_limit).  %% Maximum configured via +P
```

**Example 2** (erlang:system_info documentation, "System Information" section): Getting system version:

```erlang
erlang:system_info(system_version).
%% Returns a string like:
%% "Erlang/OTP 27 [erts-15.0] [source] [64-bit] [smp:8:8] ..."
```

**Example 3** (erlang:system_info documentation, "Scheduler Information" section): Querying scheduler state:

```erlang
erlang:system_info(schedulers).              %% Total scheduler threads
erlang:system_info(schedulers_online).       %% Currently active schedulers
erlang:system_info(dirty_cpu_schedulers).    %% Dirty CPU scheduler threads
erlang:system_info(dirty_io_schedulers).     %% Dirty I/O scheduler threads
```

# Relationships

## Builds Upon

- **erl-command** -- Many system_info keys reflect values set by erl command-line flags

## Related

- **emulator-flags** -- System_info keys like `schedulers`, `process_limit`, `port_limit` reflect emulator flag settings
- **erlang-monotonic-time** -- `os_monotonic_time_source` and `start_time` keys relate to the monotonic time system
- **erlang-system-time** -- `os_system_time_source` key relates to system time
- **time-warp-modes** -- `time_warp_mode` and `time_offset` keys relate to time warp configuration
- **erts-alloc** -- `allocator` and `{allocator, Alloc}` keys provide allocator introspection
- **crash-dump** -- `info`, `procs`, and `dist` keys return data formatted as in crash dumps

# Common Errors

- **Error**: Using `erlang:system_info(otp_release)` to get the exact OTP version
  **Correction**: `otp_release` returns only the major version. The exact version requires checking release files or `application:which_applications()`

- **Error**: Relying on the specific format of `allocated_areas` or `{allocator, Alloc}` output in production code
  **Correction**: The documentation warns this content is "highly implementation-dependent" and can change without notice

# Common Confusions

- **Confusion**: Thinking `process_limit` returns the value passed to `+P`
  **Clarification**: The runtime system often rounds up to a power of 2, so the actual limit may be larger than the value specified with `+P`

- **Confusion**: Confusing `wordsize` with `{wordsize, external}`
  **Clarification**: `wordsize` (same as `{wordsize, internal}`) returns the Erlang term word size; `{wordsize, external}` returns the true pointer size. On current systems both are typically 8 (64-bit).

# Source Reference

"erlang:system_info" reference documentation, covering sections: Memory Allocation, CPU Topology, Process Information, System Limits, System Time, Scheduler Information, Distribution Information, and System Information.

# Verification Notes

- Category organization: Directly from the documentation's section structure
- Key descriptions and return values: From individual key documentation
- OTP release limitation: Verbatim from `otp_release` documentation
- Allocator warning: Verbatim from `allocated_areas` documentation
- Confidence: HIGH -- reference documentation with explicit descriptions per key
