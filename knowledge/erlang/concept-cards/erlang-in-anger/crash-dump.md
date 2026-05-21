---
concept: Crash Dump
slug: crash-dump
category: production-ops
subcategory: crash-analysis
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Reading Crash Dumps"
chapter_number: 6
pdf_page: null
section: "General View"
extraction_confidence: high
aliases:
  - erl_crash.dump
  - crashdump
prerequisites: []
extends: []
related:
  - crash-dump-analysis
  - out-of-memory-crash
contrasts_with: []
answers_questions:
  - "What is a crash dump?"
  - "How do I control where a crash dump is written?"
---

# Quick Definition

A crash dump is a file the Erlang VM generates when a node crashes, recording a post-mortem snapshot of the VM's state — memory, processes, mailboxes, ports — for after-the-fact diagnosis.

# Core Definition

"Whenever an Erlang node crashes, it will generate a crash dump" (Chapter 6, intro).

"The crash dump is going to be named `erl_crash.dump` and be located wherever the Erlang process was running by default. This behaviour (and the file name) can be overridden by specifying the `ERL_CRASH_DUMP` environment variable."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Generated automatically when an Erlang node crashes.
2. Default name `erl_crash.dump`, written to the VM's working directory.
3. Both the name and location can be overridden via the `ERL_CRASH_DUMP` environment variable.
4. The format is mostly documented in Erlang's official documentation.
5. It may *not* be generated if the OS kills the VM for violating `ulimit` while dumping, or if the VM segfaults.
6. It contains, among other things: a slogan (crash reason), a memory breakdown, message queue lengths, file descriptor counts, process count, and per-process heap/stack/old-heap sizes and states.

# Construction / Recognition

The dump is produced automatically on crash. To control its destination, set `ERL_CRASH_DUMP` before starting the node (the book notes Heroku's `heroku_crashdumps` app does exactly this, naming dumps by boot time and placing them in a preset location).

# Context & Application

Used for *a posteriori* diagnosis — figuring out why a node died after the fact. It is the starting artifact for the whole crash-dump analysis workflow.

# Examples

From Chapter 6, intro: "Reading the crash dump will be useful to figure out possible reasons for a node to die *a posteriori*."

A dump's slogan line example (Chapter 6, "General View"): `eheap_alloc: Cannot allocate 2733560184 bytes of memory (of type "old_heap").`

# Relationships

## Builds Upon

## Enables
- crash-dump-analysis

## Related
- out-of-memory-crash

## Contrasts With

# Common Errors

- Assuming a crash dump always exists — if the OS killed the VM mid-dump (ulimit) or the VM segfaulted, there may be none.
- Letting dumps land in the working directory and get lost — set `ERL_CRASH_DUMP` to a known, persistent location.

# Common Confusions

- A crash dump is a post-mortem snapshot, not a live debugging tool — it captures the moment of death only.
- The dump's reported memory can *underreport* reference-counted binary memory, which is garbage-collected before the dump is written.

# Source Reference

Chapter 6: Reading Crash Dumps, intro and "General View" sections. (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined.
- Uncertainties: none.
- Cross-reference status: Verified
