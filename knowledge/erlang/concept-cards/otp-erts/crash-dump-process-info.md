---
concept: Crash Dump Process Information
slug: crash-dump-process-info
category: production-ops
subcategory: crash-dumps
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "How to Interpret the Erlang Crash Dumps"
chapter_number: null
pdf_page: null
section: "Process Information"
extraction_confidence: high
aliases:
  - "crash dump process data"
  - "crash dump process section"
prerequisites:
  - crash-dump
  - crash-dump-slogans
extends:
  - crash-dump
related:
  - erts-alloc
contrasts_with: []
answers_questions:
  - "How do I interpret an Erlang crash dump?"
  - "How do I interpret process data in crash dumps?"
---

# Quick Definition

The process information section of an Erlang crash dump contains a listing of every living Erlang process at the time of the crash, including its state, registered name, memory usage, reductions, message queue, heap sizes, stack data, and links. This is typically the most useful section for diagnosing the root cause of a crash.

# Core Definition

Each process in the crash dump is listed under the tag `=proc:<pid>`. The section provides detailed per-process data that reveals which processes were consuming excessive resources, what state they were in, and how they relate to each other (Ericsson AB, "How to Interpret the Erlang Crash Dumps," section "Process Information").

Key fields for each process include:

- **State**: One of `Scheduled` (in run queue), `Waiting` (in receive), `Running` (currently executing -- if `erlang:halt/1` was called, this is the calling process), `Exiting` (on its way to exit), `Garbing` (garbage collecting when dump was written -- limited remaining info), or `Suspended` (via `erlang:suspend_process/1` or busy port).
- **Registered name**: The registered name, if any.
- **Spawned as / Spawned by**: Entry point and parent process.
- **Message queue length**: Number of queued messages.
- **Reductions**: Reduction count consumed by the process.
- **Stack+heap**: Combined size in words.
- **OldHeap**: Size of the tenured (old generation) heap in words. The BEAM uses generational GC with two generations; data surviving two collections is tenured to this less-frequently-collected heap.
- **Memory**: Total memory in bytes, including call stack, heap, and internal structures (same as `erlang:process_info(Pid, memory)`).
- **Link list**: Linked/monitored processes and ports, with direction indicators ("to" = this process monitors the other, "from" = the other monitors this one).

# Prerequisites

- **crash-dump** -- Understanding crash dump structure and how to open/navigate one
- **crash-dump-slogans** -- Reading the slogan first to understand the crash category before diving into process data

# Key Properties

1. Every living process at crash time is listed, not just the failing one
2. The `State` field reveals what each process was doing: `Running` processes are the most interesting for `erlang:halt/1` crashes
3. `Garbing` state means the process was mid-garbage-collection; its data is limited
4. `Stack+heap` and `OldHeap` together constitute most of the process's allocated memory
5. Large `Message queue length` values indicate a process that cannot keep up with incoming messages
6. The `Memory` field gives total memory usage comparable to `erlang:process_info(Pid, memory)`
7. `Link list` shows both links and monitors with direction, revealing supervision and dependency relationships
8. Process data sections (`=proc_stack`, `=proc_heap`, `=proc_messages`, `=proc_dictionary`) contain raw memory that the Crashdump Viewer can decode
9. The scheduler section (`=scheduler`) shows a more current snapshot of running processes than the `=proc` section

# Construction / Recognition

## Identifying Problem Processes

1. **Sort by Memory**: Look for processes with unusually large `Stack+heap`, `OldHeap`, or `Memory` values
2. **Check Message Queues**: Find processes with high `Message queue length` -- these are often overwhelmed receivers
3. **Check Heap Fragments**: High `Number of heap fragments` and `Heap fragment data` values indicate heavy message passing or BIF usage
4. **Look at State**: `Running` processes during an `erlang:halt/1` crash are the direct cause; `Waiting` processes with huge heaps may indicate memory leaks

## Reading Stack Dumps

Stack variables are shown as `y(N)` entries containing live data:

```erlang
y(0)     ["/path/to/kernel/ebin", "/path/to/stdlib/ebin"]
y(1)     <0.1.0>
y(2)     {state,[],none,#Fun<erl_prim_loader.6.7085890>,...}
y(3)     infinity
```

Anonymous funs are named after the function where they were created, with a sequential number (starting at 0).

# Context & Application

Process information is the most frequently consulted section during crash dump analysis:

- **Memory exhaustion crashes**: Sort processes by memory to find the biggest consumers. Look at heap sizes and message queue lengths.
- **Stuck system crashes**: Check process states -- many `Waiting` processes with one or two `Running` or `Suspended` processes may indicate a bottleneck.
- **Supervisor tree failures**: Follow the `Link list` and `Spawned by` fields to trace the supervision tree and find the original failing process.

The Crashdump Viewer tool is strongly recommended for process analysis, as it can decode raw stack and heap data into readable Erlang terms, and allows sorting processes by various fields.

# Examples

**Process states and their meaning** (source: "How to Interpret the Erlang Crash Dumps," section "Process Information"):

| State     | Meaning                                              |
| --------- | ---------------------------------------------------- |
| Scheduled | In the run queue, waiting to be executed             |
| Waiting   | Blocked in a `receive` expression                    |
| Running   | Currently executing; the `erlang:halt/1` caller      |
| Exiting   | In the process of terminating                        |
| Garbing   | Mid-garbage-collection; limited data available       |
| Suspended | Suspended via BIF or blocked on a busy port          |

**Link list direction** (source: same section):

A link "to" process B means the current process was monitoring B. A link "from" process B means B was monitoring the current process.

**Generational GC** (source: same section):

"The Erlang virtual machine uses generational garbage collection with two generations. There is one heap for new data items and one for the data that has survived two garbage collections."

# Relationships

## Extends

- **crash-dump** -- Process information is the most detailed section within the crash dump

## Related

- **erts-alloc** -- Memory fields in process information relate to allocator behavior documented in erts_alloc

# Common Errors

- **Error**: Only looking at the process that was `Running` and ignoring all others
  **Correction**: Memory exhaustion crashes are often caused by a different process than the one that was running when the dump was taken; sort all processes by memory

- **Error**: Ignoring the difference between `=scheduler` and `=proc` snapshots
  **Correction**: The scheduler section shows process state at the exact moment the dump started, which may differ from the `=proc` section and is often "more telling"

- **Error**: Attempting to read raw `=proc_stack` and `=proc_heap` data manually
  **Correction**: Use the Crashdump Viewer tool which decodes this data into readable Erlang terms

# Common Confusions

- **Confusion**: `Stack+heap` and `OldHeap` are separate memory allocations that add up to total memory
  **Clarification**: They constitute "most of" the allocated memory but not all -- the `Memory` field includes additional internal structures

- **Confusion**: `Heap fragment data` indicates a problem
  **Clarification**: Heap fragments are normal -- they are data created by messages or BIFs. The source states this field "depends on so many things that this field is usually uninteresting"

- **Confusion**: The `Garbing` state indicates a GC bug
  **Clarification**: It simply means the process happened to be garbage collecting when the crash dump was written; it is "bad luck" and limits the available information but is not itself an error

# Source Reference

"How to Interpret the Erlang Crash Dumps," sections "Process Information" and "Process Data." The source lists all per-process fields with descriptions, explains the six possible process states, describes the generational GC model, link list direction semantics, and provides a stack dump example with annotation. It notes that the Crashdump Viewer tool is recommended for decoding raw process data.

# Verification Notes

- All process states (Scheduled, Waiting, Running, Exiting, Garbing, Suspended): Directly listed and described in source
- Link direction semantics ("to" = monitoring, "from" = monitored by): Directly from source
- Generational GC description: Directly quoted from source OldHeap field
- Stack dump example: Verbatim from source section "Process Data"
- Fun naming convention: Directly from source -- "A name constructed from the name of the function in which they are created"
- "Heap fragment data... usually uninteresting": Directly quoted from source
- Garbing as "bad luck": Directly quoted from source
- Scheduler vs proc snapshot difference: Directly stated in source Scheduler Information section
- Confidence: HIGH -- all content directly from official ERTS documentation
