---
concept: Inet Port Inspection
slug: inet-port-inspection
category: production-ops
subcategory: live-debugging
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Digging In > Ports"
extraction_confidence: high
aliases:
  - "recon:port_info"
  - "recon:inet_count"
  - "recon:inet_window"
prerequisites:
  - port
  - process-inspection
extends:
  - port
related:
  - recon-proc-count
  - recon-proc-window
contrasts_with: []
answers_questions:
  - "What values are available when inspecting inet ports?"
  - "How do I find which port is eating the most bandwidth?"
  - "How do I safely inspect a port?"
---

# Quick Definition

Inet port inspection is the use of `recon:port_info/1-2` to query a single port's metadata, signals, IO, and inet statistics, and `recon:inet_count/2` / `recon:inet_window/3` to rank ports by bytes or packets transferred.

# Core Definition

"Similarly to processes, Erlang ports allow a lot of introspection. The info can be accessed by calling `erlang:port_info(Port, Key)`, and more info is available through the `inet` module. Most of it has been regrouped by the `recon:port_info/1-2` functions, which work using a somewhat similar interface to their process-related counterparts" (Chapter 5, "Digging In > Ports").

# Prerequisites

- `port`: inet port inspection examines the port data type.
- `process-inspection`: the recon port interface mirrors the process-inspection interface.

# Key Properties

1. `recon:port_info/1-2` returns categories: `meta` (`id`, `name`, `os_pid`), `signals` (`connected`, `links`, `monitors`), `io` (`input`, `output` byte counts), `memory_used` (`memory`, `queue_size`), and `type` (inet statistics, `peername`, `sockname`, `options`).
2. `connected` is the pid of the port's controlling process.
3. `os_pid` is set for ports representing external programs (not inet sockets).
4. `queue_size` is the size of the port's driver queue, in bytes.
5. `recon:inet_count(Attribute, N)` ranks inet ports by cumulative totals; `recon:inet_window(Attribute, Count, Milliseconds)` ranks by activity within a time window.
6. Supported ranking attributes (inet ports only): octets — `send_oct`, `recv_oct`, `oct`; packets — `send_cnt`, `recv_cnt`, `cnt`.
7. `recon` currently supports these counters only for inet ports; other port types return an empty list.

# Construction / Recognition

Use `recon:inet_count(oct, N)` to find the biggest cumulative bandwidth users, or `recon:inet_window(send_oct, N, Ms)` for the busiest within a window. Then use `recon:port_info("#Port<...>")` on the offender to find its controlling process and details.

# Context & Application

Used to find which socket is consuming bandwidth — "who is slowly but surely eating up all your bandwidth" — and then trace it back to a controlling process and ultimately a user or customer. `inet_count` parallels `proc_count` (cumulative); `inet_window` parallels `proc_window` (sliding window).

# Examples

From Chapter 5, "Digging In > Ports":

```erlang-repl
2> recon:inet_count(oct, 3).
[{#Port<0.6821166>,15828716661,
  [{recv_oct,15828716661},{send_oct,0}]},
 ...]
```

```erlang-repl
3> recon:inet_window(send_oct, 3, 5000).
[{#Port<0.11976746>,2986216,[{send_oct,4421857688}]},
 ...]
```

# Relationships

## Builds Upon
- port
- process-inspection

## Enables

## Related
- recon-proc-count
- recon-proc-window

## Contrasts With

# Common Errors

- Expecting `inet_count`/`inet_window` to work for files or non-inet ports — they support inet ports only.
- For `inet_window`, the middle tuple value is the attribute's *change over the window*, not its absolute total — confusing the two misreads the ranking.

# Common Confusions

- `recon:port_info` parallels `recon:info` for processes; `inet_count`/`inet_window` parallel `proc_count`/`proc_window`.
- Linking a misbehaving port to a user still requires manual work — the tools find the port and its controlling process, not the customer.

# Source Reference

Chapter 5: Runtime Metrics, Section "Digging In > Ports". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with examples and attribute lists.
- Uncertainties: none.
- Cross-reference status: Verified
