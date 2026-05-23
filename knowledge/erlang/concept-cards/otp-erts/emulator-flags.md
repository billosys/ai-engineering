---
concept: Emulator Flags
slug: emulator-flags
category: tooling
subcategory: runtime-configuration
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erl"
chapter_number: null
pdf_page: null
section: "Emulator Flags"
extraction_confidence: high
aliases:
  - "+flags"
  - "erl emulator flags"
  - "BEAM VM flags"
prerequisites:
  - erl-command
extends:
  - erl-command
related:
  - init-flags
  - erts-alloc
  - erlang-system-info
contrasts_with:
  - init-flags
answers_questions:
  - "What distinguishes the erl command flags from emulator flags?"
  - "How do I configure the number of schedulers in the BEAM?"
  - "How do I set the maximum number of processes?"
  - "How do I configure kernel poll and async threads?"
---

# Quick Definition

Emulator flags are `erl` arguments prefixed with `+` that configure the BEAM virtual machine itself -- controlling schedulers, process and port limits, memory allocation, time behavior, and other low-level VM settings. They are read left to right, with later flags overriding earlier ones.

# Core Definition

The erl documentation states: "Any argument starting with character `+` is interpreted as an emulator flag. As indicated by the name, emulator flags control the behavior of the emulator." These flags are processed by the BEAM VM before Erlang code executes.

Key emulator flag groups include:

**Scheduler configuration:**
- `+S Schedulers:SchedulersOnline` -- Sets the number of scheduler threads. Defaults to logical processors configured/available. Valid range 1-1024.
- `+SP Pct:PctOnline` -- Sets schedulers as percentages of logical processors.
- `+SDcpu DirtyCPU:DirtyCPUOnline` -- Dirty CPU scheduler threads (limited by normal schedulers).
- `+SDio N` -- Dirty I/O scheduler threads (default 10, not limited by normal schedulers).
- `+sbt BindType` -- Binds schedulers to logical processors (u, ns, ts, ps, s, db, etc.).

**System limits:**
- `+P Number` -- Maximum simultaneous processes (default 1,048,576, range 1024-134,217,727).
- `+Q Number` -- Maximum simultaneous ports (default 65,536).
- `+t size` -- Maximum atoms (default 1,048,576).
- `+e Number` -- Maximum ETS tables (partially obsolete).

**Async and I/O:**
- `+A size` -- Async thread pool size (default 1, range 1-1024).
- `+K true|false` -- Enables kernel poll (I/O polling mechanism).
- `+IOt PollThreads` -- I/O poll threads (default 1, max 1024).

**Time:**
- `+c true|false` -- Enables/disables time correction.
- `+C Mode` -- Sets time warp mode (no_time_warp, single_time_warp, multi_time_warp).

**Warnings and diagnostics:**
- `+W w|i|e` -- Maps warning messages to warnings, info reports, or errors.

**Memory:**
- `+MFlag Value` -- Memory allocator flags (see erts_alloc).

# Prerequisites

- **erl-command** -- Emulator flags are a category of erl arguments

# Key Properties

1. All emulator flags start with `+`
2. Flags are read left to right; later flags override earlier ones
3. They configure the VM before any Erlang code runs
4. Scheduler settings interact with auto-detected CPU topology
5. The `+SP` percentage flags interact multiplicatively with `+S` absolute values (e.g., `+S 4:4 +SP 50:25` yields 2 schedulers, 1 online)
6. Dirty CPU schedulers are bounded by normal scheduler counts to prevent starvation
7. Dirty I/O schedulers are not bounded by normal schedulers since they handle only I/O-bound work
8. Many limits (like `+P`, `+Q`) are rounded up to powers of 2 internally

# Construction / Recognition

## To Construct/Create:

Pass `+` flags on the `erl` command line:

```text
% erl +S 4:2 +P 2000000 +A 10 +K true +W w
```

Or set via environment variables:

```text
% export ERL_AFLAGS="+S 4:2 +K true"
% erl
```

## To Identify/Recognize:

1. Any `erl` argument starting with `+` is an emulator flag
2. At runtime, query current settings via `erlang:system_info/1` (e.g., `erlang:system_info(schedulers)`, `erlang:system_info(process_limit)`)

# Context & Application

Emulator flags are critical for production tuning. The scheduler configuration (`+S`, `+SDcpu`, `+SDio`) directly affects how well the runtime uses available CPU cores. The process limit (`+P`) must be raised for applications running hundreds of thousands of concurrent processes. Async thread pool size (`+A`) matters for linked-in drivers.

The documentation notes that dirty CPU schedulers are bounded: "The amount of dirty CPU schedulers is limited by the amount of normal schedulers in order to limit the effect on processes executing on ordinary schedulers." Dirty I/O schedulers have no such limit since "only I/O bound work is expected to execute on dirty I/O schedulers."

Use `msacc` (microstate accounting) to measure scheduler load and adjust dirty scheduler counts accordingly.

# Examples

**Example 1** (erl documentation, "erl <arguments>" section): Mixed emulator and init flags:

```text
% erl +W w -sname arnie +S 2 -s my_init -extra +bertie
```

Here `+W w` sets warning mapping and `+S 2` sets the number of schedulers.

**Example 2** (erl documentation, "+sct" section): Running two Erlang systems on different cores of a quad-core machine:

```text
% erl +sct L0-3c0-3 +sbt db +S3:2 -detached -noinput -noshell -sname one
% erl +sct L3-0c0-3 +sbt db +S3:2 -detached -noinput -noshell -sname two
```

Each runtime has two schedulers online, all on different cores.

# Relationships

## Builds Upon

- **erl-command** -- Emulator flags are one of three argument types to erl

## Related

- **init-flags** -- The `-` flags that configure the Erlang-level runtime, as opposed to the VM
- **erts-alloc** -- Memory allocator configuration via `+M` flags
- **erlang-system-info** -- The BIF used to query at runtime the values set by emulator flags

## Contrasts With

- **init-flags** -- Init flags (`-` prefix) configure the Erlang runtime and applications; emulator flags (`+` prefix) configure the VM itself

# Common Errors

- **Error**: Setting `+SDcpu` higher than `+S` and expecting all dirty CPU schedulers to be available
  **Correction**: Dirty CPU schedulers are capped by normal scheduler count -- set `+S` at least as high as desired `+SDcpu`

- **Error**: Using `+P 100` to limit processes, then wondering why the system uses more
  **Correction**: The minimum is 1024, and the runtime often rounds up to a power of 2

# Common Confusions

- **Confusion**: Believing `+S` sets an exact number of schedulers
  **Clarification**: `+S Schedulers:SchedulersOnline` sets both total schedulers and schedulers online; the total is fixed at boot while online can be changed at runtime via `erlang:system_flag(schedulers_online, N)`

- **Confusion**: Thinking `+SDio` is limited by the normal scheduler count like `+SDcpu`
  **Clarification**: Dirty I/O schedulers are intentionally not bounded by normal schedulers because they only handle I/O-bound work

# Source Reference

"erl" command documentation, "Emulator Flags" section, covering `+S`, `+SP`, `+SDcpu`, `+SDio`, `+P`, `+Q`, `+A`, `+K`, `+W`, `+t`, `+M`, `+c`, `+C`, `+sbt`, `+sct`, and related flags.

# Verification Notes

- Flag syntax and defaults: Directly from erl "Emulator Flags" section
- Scheduler interaction rules: Directly from `+SDcpu` documentation
- Process limit defaults and ranges: Directly from `+P` documentation
- Confidence: HIGH -- all values and behaviors explicitly documented
