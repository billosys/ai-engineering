---
concept: recon:proc_count
slug: recon-proc-count
category: production-ops
subcategory: live-debugging
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
  - "recon:proc_count/2"
  - proc_count
prerequisites:
  - process-inspection
extends: []
related:
  - recon-proc-window
contrasts_with:
  - recon-proc-window
answers_questions:
  - "How do I find top memory-consuming processes?"
  - "How do I find the busiest processes on a node?"
---

# Quick Definition

`recon:proc_count(Attribute, N)` lists the top `N` processes on a node ranked by a chosen `process_info` attribute (e.g. `memory`, `reductions`) — a cumulative, point-in-time ranking.

# Core Definition

"When looking for high memory usage, for example it's interesting to be able to list all of a node's processes and find the top `N` consumers. Using the attributes above and the `recon:proc_count(Attribute, N)` function, we can get these results" (Chapter 5, "Digging In > Processes").

# Prerequisites

- `process-inspection`: `proc_count` ranks processes by the `process_info` attributes that process inspection exposes.

# Key Properties

1. Signature: `recon:proc_count(Attribute, N)`.
2. `Attribute` can be any of the process attributes (`memory`, `reductions`, `message_queue_len`, etc.).
3. Returns the top `N` processes, each as a tuple of pid, attribute value, and identifying metadata.
4. It is a *cumulative* / point-in-time snapshot — it reflects values accumulated over each process's whole lifetime.
5. Best suited to nodes with *long-lived* processes that cause problems.
6. Poorly suited when most processes are short-lived, since brief offenders are missed and long-lived ones dominate.

# Construction / Recognition

Call `recon:proc_count(memory, 3)` to get the three biggest memory users, or substitute another attribute. Read the metadata to identify each process.

# Context & Application

Use `proc_count` when the suspect processes are long-lived — for example, finding which long-running process is slowly accumulating memory. For short-lived processes or a "right now" view, use `recon:proc_window/3` instead.

# Examples

From Chapter 5, "Digging In > Processes":

```erlang-repl
4> recon:proc_count(memory, 3).
[{<0.26.0>,831448,
  [{current_function,{group,server_loop,3}},
   {initial_call,{group,server,3}}]},
 {<0.25.0>,372440,
  [user, ...]},
 {<0.20.0>,372312,
  [code_server, ...]}]
```

# Relationships

## Builds Upon
- process-inspection

## Enables

## Related

## Contrasts With
- recon-proc-window

# Common Errors

- Using `proc_count` to hunt short-lived offenders — they die before the snapshot and are never seen.
- Comparing cumulative attributes (like reductions) across processes of very different ages without realizing the older one is favored.

# Common Confusions

- `proc_count` is a *cumulative* snapshot; `proc_window` is a *sliding-window* sample — they answer different questions.

# Source Reference

Chapter 5: Runtime Metrics, Section "Digging In > Processes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with example.
- Uncertainties: none.
- Cross-reference status: Verified
