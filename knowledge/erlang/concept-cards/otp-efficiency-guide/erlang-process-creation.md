---
concept: Erlang Process Creation
slug: erlang-process-creation
category: performance
subcategory: null
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Creating an Erlang Process"
extraction_confidence: high
aliases:
  - "spawn"
  - "process spawning"
  - "lightweight process"
prerequisites: []
extends: []
related:
  - tail-recursive-main-loop
  - initial-heap-size-tuning
  - message-sending-cost
contrasts_with: []
answers_questions:
  - "How lightweight is an Erlang process compared to OS threads?"
  - "How much memory does a newly spawned Erlang process use?"
---

# Quick Definition

An Erlang process is a lightweight unit of concurrency that costs only 327 words of memory when newly spawned, making it far cheaper than operating system threads or processes.

# Core Definition

An Erlang process is lightweight compared to threads and processes in operating systems. A newly spawned process uses 327 words of memory (2,616 bytes on a 64-bit system), which includes 233 words for the heap area (including the stack). The garbage collector increases the heap as needed (Ericsson/OTP Team, "Processes" chapter, "Creating an Erlang Process" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A newly spawned Erlang process uses 327 words of memory
2. On a 64-bit system, this equals 2,616 bytes
3. The initial allocation includes 233 words for the heap area (which includes the stack)
4. The garbage collector grows the heap automatically as needed
5. Processes are lightweight compared to OS threads and processes

# Construction / Recognition

## To Measure Process Memory

1. Create a function that blocks indefinitely: `Fun = fun() -> receive after infinity -> ok end end`
2. Spawn it and query memory: `{_, Bytes} = process_info(spawn(Fun), memory)`
3. Convert bytes to words: `Bytes div erlang:system_info(wordsize)`

# Context & Application

Erlang's lightweight process model is fundamental to the language's concurrency approach. Because processes are so cheap to create, the idiomatic Erlang style is to spawn a process for each concurrent activity rather than sharing threads. This design enables systems with hundreds of thousands or even millions of concurrent processes.

**Typical contexts:**

- Building concurrent servers with one process per client connection
- Spawning short-lived processes for computation tasks
- Implementing actor-model concurrency patterns

# Examples

**Example** (Processes chapter): Measuring the memory footprint of a newly spawned process:

```erlang
Erlang/OTP 27 [erts-14.2.3] [64-bit] [smp:8:8] [ds:8:8:10] [async-threads:1] [jit]

Eshell V14.2.3 (press Ctrl+G to abort, type help(). for help)
1> Fun = fun() -> receive after infinity -> ok end end.
#Fun<erl_eval.43.39164016>
2> {_,Bytes} = process_info(spawn(Fun), memory).
{memory,2616}
3> Bytes div erlang:system_info(wordsize).
327
```

# Relationships

## Related

- **tail-recursive-main-loop** -- Every process's main loop must be tail-recursive to avoid stack growth
- **initial-heap-size-tuning** -- The default 233-word heap can be tuned for performance
- **message-sending-cost** -- Processes communicate via message passing, which involves copying

# Common Errors

- **Error**: Assuming that process creation is expensive and avoiding spawning new processes
  **Correction**: Erlang processes are designed to be cheap; spawning one costs only 327 words of memory

- **Error**: Not making the main loop tail-recursive, leading to unbounded stack growth
  **Correction**: Always ensure the outer loop function ends with a tail call to itself

# Common Confusions

- **Confusion**: Equating Erlang processes with OS processes or threads
  **Clarification**: Erlang processes are managed by the BEAM VM, not the operating system. They are orders of magnitude lighter than OS threads (327 words vs. typically megabytes for OS threads)

- **Confusion**: Believing the 327-word figure is fixed and unchangeable
  **Clarification**: The 327 words is the initial size; the garbage collector grows the heap as needed. The initial heap size can also be tuned via `+h` or `min_heap_size`

# Source Reference

"Processes" chapter, "Creating an Erlang Process" section. Includes shell session demonstrating memory measurement of a spawned process.

# Verification Notes

- Definition: Directly from source text, first paragraphs of the "Creating an Erlang Process" section
- Memory figures (327 words, 2616 bytes, 233 words heap): Exact values from source shell session and surrounding text
- Confidence: HIGH -- explicit figures and clear explanation in official documentation
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
