---
concept: Erlang Crash Dump
slug: crash-dump
category: production-ops
subcategory: crash-dumps
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "How to Interpret the Erlang Crash Dumps"
chapter_number: null
pdf_page: null
section: "General Information"
extraction_confidence: high
aliases:
  - erl_crash.dump
  - "crash dump"
  - "BEAM crash dump"
prerequisites: []
extends: []
related:
  - crash-dump-slogans
  - crash-dump-process-info
  - erts-alloc
contrasts_with: []
answers_questions:
  - "What is an Erlang crash dump?"
  - "How do I interpret an Erlang crash dump?"
  - "What must I know before interpreting crash dumps?"
---

# Quick Definition

An Erlang crash dump (`erl_crash.dump`) is a readable text file generated upon abnormal exit of the Erlang runtime system. It contains detailed information about the system state at the time of the crash, including process listings, memory usage, ETS tables, loaded modules, distribution information, and the reason for the crash.

# Core Definition

The crash dump is written to the current directory of the emulator or to the file specified by the `ERL_CRASH_DUMP` environment variable. A writable file system must be mounted for the dump to be created (Ericsson AB, "How to Interpret the Erlang Crash Dumps").

Crash dumps are written for one of two main reasons:

1. The BIF `erlang:halt/1` is called explicitly with a string argument
2. The runtime system detects an error it cannot handle, most commonly caused by external limitations such as running out of memory

Internal errors can also trigger crash dumps, such as exceeding the atom limit or having too many simultaneous ETS tables. On systems supporting OS signals, sending `SIGUSR1` to an Erlang process also generates a crash dump.

The crash dump is structured in tagged sections. The first part shows general information: creation time, the slogan (crash reason), system version, number of atoms, and the runtime thread that caused the dump.

# Prerequisites

- Basic understanding of the BEAM runtime system architecture
- Familiarity with Erlang processes, ETS tables, and OTP applications

# Key Properties

1. The file is a readable text file, but can be difficult to read manually
2. The Crashdump Viewer tool (part of the Observer application) provides a graphical browser for crash dumps
3. The crash dump format evolves between OTP releases
4. The first thing to check is the slogan, which describes the crash reason
5. Major sections include: general info, scheduler info, memory, allocators, processes, ports, ETS tables, timers, distribution info, loaded modules, funs, process data (stacks/heaps), and atoms
6. The number of atoms is shown as `Atoms: <number>` -- tens of thousands is normal; more may indicate dynamic atom generation via `list_to_atom/1`
7. On Unix systems, `SIGUSR1` can be sent to force a crash dump without a real crash

# Construction / Recognition

## Locating the Crash Dump

1. Check the current working directory of the emulator for `erl_crash.dump`
2. Check the `ERL_CRASH_DUMP` environment variable for a custom path

## Reading the Crash Dump

1. Open with the Crashdump Viewer tool: start Observer and use File > Open Crashdump
2. Or read the text file directly, starting with the slogan and general information
3. The slogan line format is: `Slogan: <reason>`

## Major Sections (Tags)

- `=memory` -- Memory information (similar to `erlang:memory()`)
- `=scheduler:id` -- Scheduler state and statistics
- `=proc:<pid>` -- Per-process information
- `=ets:<owner>` -- ETS table details
- `=timer:<owner>` -- Timer information
- `=node:<name>` -- Distribution/node information
- `=mod:<name>` -- Loaded module information
- `=allocated_areas` -- Allocated memory areas
- `=allocator:<A>` -- Allocator-specific information

# Context & Application

Crash dumps are the primary post-mortem debugging tool for Erlang systems. They are generated in production when the runtime encounters unrecoverable errors. Common investigation workflows:

1. **Start with the slogan** to understand the broad category of failure
2. **Check memory information** to see if the system ran out of memory
3. **Examine process listings** to find processes with excessive memory or message queues
4. **Review ETS tables** to identify tables consuming excessive memory
5. **Check the atom count** to detect atom table exhaustion
6. **Review distribution information** if the node was distributed

The usual reason for a crash is that the runtime system cannot handle an error caused by external resource limitations. "Usually the emulator or the operating system can be reconfigured to avoid the crash, which is why interpreting the crash dump correctly is important" (source: introduction).

# Examples

**Triggering a crash dump via SIGUSR1** (source: "How to Interpret the Erlang Crash Dumps"):

On Unix systems, send `SIGUSR1` to the Erlang VM process to force a crash dump for diagnostic purposes.

**Reading process stack data** (source: section "Process Data"):

```erlang
(1)  3cac44   Return addr 0x13BF58 (<terminate process normally>)
(2)  y(0)     ["/view/siri_r10_dev/clearcase/otp/erts/lib/kernel/ebin",
(3)            "/view/siri_r10_dev/clearcase/otp/erts/lib/stdlib/ebin"]
(4)  y(1)     <0.1.0>
(5)  y(2)     {state,[],none,#Fun<erl_prim_loader.6.7085890>,...}
(6)  ...
(7)  y(3)     infinity
```

Stack variables (`y(N)`) show live data including process state records, pids, and funs. Anonymous funs are named after the function in which they were created, with a sequential number.

# Relationships

## Related

- **crash-dump-slogans** -- Common crash dump slogans and their meanings
- **crash-dump-process-info** -- How to interpret per-process data in crash dumps
- **erts-alloc** -- Allocator information referenced in memory-related crash slogans

# Common Errors

- **Error**: Ignoring the crash dump and only looking at application logs
  **Correction**: Application logs may not capture runtime-level failures; the crash dump contains information unavailable anywhere else

- **Error**: Assuming the crash dump format is stable across OTP versions
  **Correction**: The format evolves between releases; use the Crashdump Viewer tool which handles format differences

- **Error**: Not checking the atom count
  **Correction**: Dynamic atom generation via `list_to_atom/1` can exhaust the atom table; the atom count in the crash dump reveals this

# Common Confusions

- **Confusion**: A crash dump means there is a bug in the BEAM VM
  **Clarification**: Most crash dumps are caused by application-level issues (memory exhaustion, configuration errors) or external resource limitations, not VM bugs

- **Confusion**: The crash dump only contains the failing process
  **Clarification**: The crash dump contains the state of ALL processes, ETS tables, ports, timers, and other system resources at the time of the crash

- **Confusion**: The process state shown under `=scheduler` is the same as under `=proc`
  **Clarification**: The scheduler section shows a snapshot at the exact moment the crash dump starts being generated, which is often more telling than the `=proc` section data

# Source Reference

"How to Interpret the Erlang Crash Dumps," all sections. The source covers general information, scheduler data, memory, internal tables, allocated areas, allocators, process information, port information, ETS tables, timers, distribution information, loaded modules, fun information, process data, and atoms. A disclaimer notes the format evolves between releases.

# Verification Notes

- Definition and trigger conditions: Directly from source introduction
- ERL_CRASH_DUMP environment variable: Explicitly stated in source
- SIGUSR1 trigger: Explicitly stated in source
- Atom count guidance: Directly from source -- "Some ten thousands atoms is perfectly normal"
- Stack dump example: Verbatim from source section "Process Data"
- Crashdump Viewer recommendation: Directly from source introduction
- All section tags: Directly from source section headings
- Confidence: HIGH -- all content directly from official ERTS documentation
