---
concept: Process Memory Keys
slug: process-memory-keys
category: performance
subcategory: memory
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Digging In > Processes"
extraction_confidence: high
aliases:
  - heap_size
  - total_heap_size
  - process memory
prerequisites:
  - process-inspection
extends:
  - process-inspection
related:
  - reduction
contrasts_with: []
answers_questions:
  - "What kinds of memory information are available for a specific process?"
  - "How do I safely inspect a process?"
---

# Quick Definition

Process memory keys are the `process_info` entries that describe a single process's memory: `memory`, `heap_size`, `total_heap_size`, `garbage_collection`, `message_queue_len`, and `messages` — some reported in words, some in bytes, and some unsafe to fetch.

# Core Definition

These keys come from the commonly-used `process_info(Pid, Key)` list in Chapter 5, "Digging In > Processes", which documents the memory-related entries available for a process and notes the units and the production-safety of each.

# Prerequisites

- `process-inspection`: these keys are a subset of the process inspection interface.

# Key Properties

1. `memory` — the size of the process in *bytes*, including call stack, heaps, and internal VM structures.
2. `heap_size` — the newest-generation heap size, usually including the stack; reported in *words*. A process has an 'old' and a 'new' heap and uses generational GC.
3. `total_heap_size` — like `heap_size` but including all heap fragments, including the old heap; reported in *words*.
4. `garbage_collection` — GC information (number of GCs, full-sweep options, heap sizes); documented as 'subject to change'.
5. `message_queue_len` — how many messages are waiting in the mailbox; safe and cheap.
6. `messages` — *all* messages in the mailbox; *extremely dangerous* in production since a mailbox may hold millions of messages. Always call `message_queue_len` first.
7. Unit mismatch is deliberate and easy to trip on: `memory` is in bytes, `heap_size`/`total_heap_size` are in words.

# Construction / Recognition

Use `recon:info(Pid, memory_used)` for a safe categorized view, or `process_info(Pid, [memory, heap_size, total_heap_size, message_queue_len])`. Never request `messages` without checking `message_queue_len` first.

# Context & Application

Used to investigate which process is consuming memory and whether its mailbox is the cause. These keys feed `recon:proc_count(memory, N)` and the memory section of crash-dump analysis.

# Examples

From Chapter 5, "Digging In > Processes", the `memory_used` category of `recon:info/1`:

```erlang-repl
{memory_used,[{memory,2808},
              {message_queue_len,0},
              {heap_size,233},
              {total_heap_size,233},
              {garbage_collection,[{min_bin_vheap_size,46422},
                                   {min_heap_size,233},
                                   {fullsweep_after,65535},
                                   {minor_gcs,0}]}]}
```

# Relationships

## Builds Upon
- process-inspection

## Enables

## Related
- reduction

## Contrasts With

# Common Errors

- Requesting `messages` on a stuck process with a huge mailbox — copying it to the shell can kill the node. Always check `message_queue_len` first.
- Comparing a `heap_size` (words) directly against a `memory` value (bytes) — different units.

# Common Confusions

- `heap_size` covers only the new generation; `total_heap_size` includes the old heap and other fragments — they are not interchangeable.
- A large `message_queue_len` is the safe warning sign; the actual `messages` content is the dangerous thing to fetch.

# Source Reference

Chapter 5: Runtime Metrics, Section "Digging In > Processes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter key list.
- Confidence rationale: high — each key explicitly documented with units and safety notes.
- Uncertainties: `garbage_collection` content is documented as subject to change.
- Cross-reference status: Verified
