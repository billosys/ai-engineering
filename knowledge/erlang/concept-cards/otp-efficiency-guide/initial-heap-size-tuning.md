---
concept: Initial Heap Size Tuning
slug: initial-heap-size-tuning
category: performance
subcategory: null
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Initial Heap Size"
extraction_confidence: high
aliases:
  - "min_heap_size"
  - "process heap tuning"
  - "+h option"
prerequisites:
  - erlang-process-creation
extends:
  - erlang-process-creation
related:
  - message-sending-cost
  - literal-pool
contrasts_with: []
answers_questions:
  - "How do I tune the initial heap size for short-lived processes?"
  - "What are the trade-offs of increasing the minimum heap size?"
---

# Quick Definition

The default initial heap size of 233 words can be increased system-wide via the `+h` emulator option or per-process via the `min_heap_size` option to `spawn_opt/4`, reducing garbage collection overhead at the cost of higher memory usage.

# Core Definition

The default initial heap size of 233 words is quite conservative to support Erlang systems with hundreds of thousands or even millions of processes. The garbage collector grows and shrinks the heap as needed. In systems that use comparatively few processes, performance might be improved by increasing the minimum heap size using either the `+h` option for `erl` or on a process-per-process basis using the `min_heap_size` option for `spawn_opt/4` (Ericsson/OTP Team, "Processes" chapter, "Initial Heap Size" section).

# Prerequisites

- **erlang-process-creation** -- Understanding the default process memory layout (327 words total, 233 words heap) is required

# Key Properties

1. Default initial heap size is 233 words
2. The garbage collector grows the heap step-by-step, which is more costly than establishing a larger heap at spawn time
3. The garbage collector can also shrink the heap; setting a minimum prevents this unnecessary shrinking
4. Two mechanisms for tuning: `+h` (system-wide) and `min_heap_size` in `spawn_opt/4` (per-process)
5. Larger heaps mean less frequent garbage collections
6. Less frequent garbage collections means huge binaries may be retained longer (a downside)
7. The runtime system will probably use more memory overall

# Construction / Recognition

## To Tune System-Wide

Pass the `+h` option when starting the Erlang emulator:
```
erl +h <size_in_words>
```

## To Tune Per-Process

Use `spawn_opt/4` with the `min_heap_size` option:
```erlang
spawn_opt(Module, Function, Args, [{min_heap_size, Size}])
```

## Strategy for Short-Lived Computation Processes

1. Estimate the memory needed for the computation
2. Set `min_heap_size` to that estimate when spawning
3. The process performs its computation and sends the result to another process
4. The process terminates -- if the heap was sized correctly, no garbage collection occurred at all

# Context & Application

This optimization targets two specific scenarios: systems with relatively few processes where a larger default heap is beneficial, and systems that spawn short-lived computation workers where eliminating garbage collection overhead matters.

**Typical contexts:**

- Batch processing systems with a moderate number of worker processes
- Short-lived computation tasks spawned to offload work
- Systems where GC pauses in individual processes cause latency issues

**Trade-offs:**

- Higher memory usage per process
- Huge binaries may be retained longer due to less frequent GC
- The source explicitly warns: "This optimization is not to be attempted without proper measurements"

# Examples

**Example 1** (Processes chapter, "Initial Heap Size" section): The dual benefit of increasing heap size is described:

> The gain is twofold:
> - Although the garbage collector grows the heap, it grows it step-by-step, which is more costly than directly establishing a larger heap when the process is spawned.
> - The garbage collector can also shrink the heap if it is much larger than the amount of data stored on it; setting the minimum heap size prevents that.

**Example 2** (Processes chapter): Short-lived computation pattern:

> In systems with many processes, computation tasks that run for a short time can be spawned off into a new process with a higher minimum heap size. When the process is done, it sends the result of the computation to another process and terminates. If the minimum heap size is calculated properly, the process might not have to do any garbage collections at all.

# Relationships

## Extends

- **erlang-process-creation** -- Tuning modifies the default memory layout established at process creation

## Related

- **message-sending-cost** -- Results from computation processes are sent via messages
- **literal-pool** -- Literals do not consume heap space, so they do not factor into heap size calculations

# Common Errors

- **Error**: Increasing the minimum heap size without measuring the actual effect
  **Correction**: The source explicitly warns that "this optimization is not to be attempted without proper measurements." Profile before and after to verify the benefit

- **Error**: Setting a very large minimum heap size system-wide in a system with millions of processes
  **Correction**: Use per-process tuning via `spawn_opt/4` for specific processes that benefit; the conservative 233-word default exists precisely to support high-process-count systems

- **Error**: Ignoring the side effect of retaining huge binaries longer
  **Correction**: Less frequent garbage collection means binary references are held longer. Monitor binary memory usage when increasing heap sizes

# Common Confusions

- **Confusion**: Believing that increasing the heap size always improves performance
  **Clarification**: It is a trade-off: less GC overhead but more memory usage. For systems with many processes, the memory cost may outweigh the GC savings

- **Confusion**: Thinking `min_heap_size` sets a fixed heap size
  **Clarification**: It sets a MINIMUM -- the garbage collector can still grow the heap beyond this value, but it will not shrink it below the minimum

# Source Reference

"Processes" chapter, "Initial Heap Size" section. Includes discussion of the default 233-word heap, the `+h` and `min_heap_size` tuning mechanisms, trade-offs, and a warning about requiring proper measurements.

# Verification Notes

- Definition: Directly from source text, "Initial Heap Size" subsection
- The 233-word default is explicitly stated in the source
- Both tuning mechanisms (`+h` and `min_heap_size`) are named in the source
- The warning about proper measurements is a direct quote
- The dual benefit (avoiding step-by-step growth and preventing shrinking) is from a bulleted list in the source
- Confidence: HIGH -- explicit, detailed guidance in official documentation with clear caveats
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
