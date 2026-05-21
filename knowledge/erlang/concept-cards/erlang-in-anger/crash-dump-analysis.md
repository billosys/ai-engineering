---
concept: Crash Dump Analysis
slug: crash-dump-analysis
category: production-ops
subcategory: crash-analysis
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Reading Crash Dumps"
chapter_number: 6
pdf_page: null
section: "General View"
extraction_confidence: high
aliases:
  - erl_crashdump_analyzer.sh
  - reading a crash dump
prerequisites:
  - crash-dump
extends: []
related:
  - full-mailbox-diagnosis
  - process-count-anomaly
  - port-count-anomaly
  - out-of-memory-crash
contrasts_with: []
answers_questions:
  - "How do I read a crash dump?"
  - "What is a crash dump?"
---

# Quick Definition

Crash dump analysis is the workflow of extracting and interpreting a crashed node's state from its `erl_crash.dump` — typically starting with recon's `erl_crashdump_analyzer.sh` to get a quick summary, then correlating the figures to find the cause.

# Core Definition

"Reading the crash dump will be useful to figure out possible reasons for a node to die *a posteriori*. One way to get a quick look at things is to use recon's `erl_crashdump_analyzer.sh` and run it on a crash dump" (Chapter 6, "General View").

# Prerequisites

- `crash-dump`: analysis operates on the `erl_crash.dump` file.

# Key Properties

1. `erl_crashdump_analyzer.sh` is a recon script that summarizes a dump.
2. The summary includes: the crash slogan, a memory breakdown, the largest message-queue lengths, error logger queue length, file descriptors open (UDP/TCP/Files), process count, the largest process heap+stack sizes, the largest old-heap sizes, and process states at crash time.
3. The dump "won't point out a problem directly to your face, but will be a good clue as to where to look."
4. The core technique is *correlation*: "Correlate it with the number of processes and the size of mailboxes. One may explain the other."
5. There is no generic recipe — interpretation depends on knowing the node's normal values.
6. Common follow-up paths: full mailboxes, too many/few processes, too many ports, can't allocate memory.

# Construction / Recognition

1. Run `./recon/script/erl_crashdump_analyzer.sh erl_crash.dump`.
2. Look for anything surprising — especially in the Memory section.
3. Correlate memory with process count and mailbox sizes.
4. Branch into the specific diagnosis (full mailboxes, process/port anomalies, OOM) based on what stands out.

# Context & Application

Used after a node crash to determine the cause. Effective analysis depends on having a sense of the node's normal baseline (process count, port count, memory).

# Examples

From Chapter 6, "General View", the analyzer output includes:

```text
Slogan: eheap_alloc: Cannot allocate 2733560184 bytes of memory
(of type "old_heap").
Memory:
  ... total: 11079 Mb
Different message queue lengths (5 largest different):
      1 5010932
      ...
Number of processes:
36496
Process States when crashing (sum):
      1 Garbing
     74 Scheduled
  36421 Waiting
```

The book reads this as: the node ran out of memory (11079 Mb of a 15 Gb instance), and one process had ~5 million messages queued — "That's telling."

# Relationships

## Builds Upon
- crash-dump

## Enables
- full-mailbox-diagnosis
- process-count-anomaly
- port-count-anomaly
- out-of-memory-crash

## Related

## Contrasts With

# Common Errors

- Expecting the dump to name the culprit outright — it gives clues, not verdicts.
- Reading a single section in isolation instead of correlating memory, process count, and mailbox sizes.

# Common Confusions

- Crash dump analysis is interpretive, not mechanical — without a baseline, "high" and "low" are meaningless.
- The analyzer script summarizes; deeper questions still require reading the raw dump or a similar live node.

# Source Reference

Chapter 6: Reading Crash Dumps, Section "General View". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly described with full analyzer output.
- Uncertainties: none.
- Cross-reference status: Verified
