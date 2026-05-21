---
concept: Out-of-Memory Crash
slug: out-of-memory-crash
category: production-ops
subcategory: crash-analysis
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Reading Crash Dumps"
chapter_number: 6
pdf_page: null
section: "Can't Allocate Memory"
extraction_confidence: high
aliases:
  - can't allocate memory
  - eheap_alloc crash
prerequisites:
  - crash-dump-analysis
extends: []
related:
  - full-mailbox-diagnosis
  - vm-memory-reporting
  - memory-fragmentation
contrasts_with: []
answers_questions:
  - "How do I read a crash dump?"
  - "What should I explore if a crash dump shows the node ran out of memory?"
---

# Quick Definition

An out-of-memory crash is the most common Erlang node crash, in which the VM fails to allocate memory; the crash dump's process mailboxes and heap/stack sizes are the primary clues for finding the cause.

# Core Definition

"These are by far the most common types of crashes you are likely to see... In any case, the crash dump will help figure out what the problem was after the fact. The process mailboxes and individual heaps are usually good indicators of issues" (Chapter 6, "Can't Allocate Memory").

# Prerequisites

- `crash-dump-analysis`: OOM diagnosis is a branch of the crash-dump workflow.

# Key Properties

1. The most common class of Erlang node crash.
2. The dump's slogan often names the failed allocation, e.g. `eheap_alloc: Cannot allocate N bytes of memory (of type "old_heap")`.
3. Diagnostic order: first check mailboxes; if none is outrageously large, look at process heap and stack sizes from the recon script.
4. Large outliers at the top of heap/stack sizes → a small set of processes is eating most of the node's memory.
5. If process sizes are all roughly equal → judge whether the total amount sounds like a lot.
6. If totals look reasonable, check the dump's "Memory" section for a large *type* (e.g. ETS or Binary), which can reveal an unexpected resource leak.
7. Possible underlying causes for an OOM dump: memory fragmentation, memory leaks in C code or drivers, or lots of memory garbage-collected just before the dump was written (notably refc binary memory, which may be underreported).

# Construction / Recognition

1. Confirm the slogan indicates an allocation failure.
2. Check mailbox counters for an outrageously large queue.
3. If none, inspect process heap+stack sizes — look for top outliers vs. uniform sizes.
4. If totals are reasonable, inspect the Memory section for an oversized type (ETS, Binary).
5. Map the finding to a cause: fragmentation, C/driver leak, or pre-dump GC.

# Context & Application

Used during crash-dump analysis when a node died from memory exhaustion. The book devotes a whole later chapter (Memory Leaks) to live debugging of these; the crash dump handles the after-the-fact view.

# Examples

From Chapter 6, "General View", the slogan: `eheap_alloc: Cannot allocate 2733560184 bytes of memory (of type "old_heap").` The book notes the node "ran out of memory and had 11079 Mb out of 15 Gb used."

# Relationships

## Builds Upon
- crash-dump-analysis

## Enables

## Related
- full-mailbox-diagnosis
- vm-memory-reporting
- memory-fragmentation

## Contrasts With

# Common Errors

- Jumping straight to heap sizes before ruling out a runaway mailbox — a single 5-million-message mailbox can be the whole story.
- Forgetting that refc binary memory may be underreported in the dump (it is GC'd before the dump is written), so binary leaks can look smaller than they are.

# Common Confusions

- "Can't allocate memory" does not pinpoint a leak — it can be fragmentation, a C/driver leak, or simply pre-dump garbage collection skewing the numbers.
- Uniform process sizes vs. top outliers lead to different conclusions: a few greedy processes vs. systemic high usage.

# Source Reference

Chapter 6: Reading Crash Dumps, Section "Can't Allocate Memory" (and the OOM discussion in "General View"). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly described with slogan example and diagnostic path.
- Uncertainties: none.
- Cross-reference status: Verified
