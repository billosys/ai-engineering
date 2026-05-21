---
concept: Port Count Anomaly
slug: port-count-anomaly
category: production-ops
subcategory: crash-analysis
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Reading Crash Dumps"
chapter_number: 6
pdf_page: null
section: "Too Many Ports"
extraction_confidence: high
aliases:
  - too many ports
prerequisites:
  - crash-dump-analysis
  - port
extends: []
related:
  - process-count-anomaly
  - port-types
contrasts_with: []
answers_questions:
  - "How do I read a crash dump?"
  - "How do I diagnose a port leak from a crash dump?"
---

# Quick Definition

A port count anomaly is a crash-dump port count that is abnormally high relative to the node's usual values, indicating overload, a denial-of-service attack, or a resource leak.

# Core Definition

"Similarly to the process count, the port count is simple and mostly useful when you know your usual values. A high count may be the result of overload, Denial of Service attacks, or plain old resource leaks" (Chapter 6, "Too Many Ports").

# Prerequisites

- `crash-dump-analysis`: this is one branch of the crash-dump workflow.
- `port`: interpreting the anomaly requires understanding the port data type and its types.

# Key Properties

1. Meaningful only against the node's usual port-count values.
2. A high count can mean: overload, a Denial of Service attack, or a plain resource leak.
3. The crash-dump "File descriptors open" section breaks the count into UDP, TCP, and Files.
4. Looking at *which type* of port leaked helps reveal whether there was contention on a specific resource, or whether the code using that resource is simply wrong.

# Construction / Recognition

Compare the dump's port/file-descriptor counts against the baseline. If high, examine the per-type breakdown (TCP/UDP/Files) to narrow down the leaking resource and the responsible code.

# Context & Application

Used during crash-dump analysis when the file-descriptor section looks abnormal — to distinguish a DoS or overload from a code-level descriptor leak.

# Examples

From Chapter 6, "General View", the analyzer's file descriptor section:

```text
File descriptors open:
===
  UDP:  0
  TCP:  19951
  Files:  2
  ---
  Total:  19953
```

A TCP count of nearly 20,000 — if far above normal — points toward overload, DoS, or a socket leak.

# Relationships

## Builds Upon
- crash-dump-analysis
- port

## Enables

## Related
- process-count-anomaly
- port-types

## Contrasts With

# Common Errors

- Reading the total port count without the per-type breakdown — the type (TCP/UDP/Files) is what localizes the bug.
- Interpreting a count as "high" with no baseline to compare against.

# Common Confusions

- A high port count is not automatically a code bug — it can equally be external load or an attack; the per-type pattern and baseline help tell them apart.

# Source Reference

Chapter 6: Reading Crash Dumps, Section "Too Many Ports" (and the file-descriptor section of "General View"). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly described.
- Uncertainties: none.
- Cross-reference status: Verified
