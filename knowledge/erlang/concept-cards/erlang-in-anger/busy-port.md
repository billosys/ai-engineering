---
concept: Busy Port
slug: busy-port
category: performance
subcategory: scheduling
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "CPU and Scheduler Hogs"
chapter_number: 8
pdf_page: null
section: "Suspended Ports"
extraction_confidence: high
aliases:
  - "busy_port"
  - "busy_dist_port"
  - "Suspended ports"
prerequisites:
  - long-schedule-monitor
  - port
related:
  - long-schedule-monitor
contrasts_with: []
answers_questions:
  - "Why does my sender process get de-scheduled when writing to a port?"
  - "How do I monitor implicit back-pressure from busy ports?"
---

# Quick Definition

A busy port is a port whose internal queue has filled because a process sent it too many messages; the BEAM scheduler forcibly de-schedules the sender until space frees up — an implicit form of back-pressure.

# Core Definition

From section "Suspended Ports": "When a process sends too many message to a port and the port's internal queue gets full, the Erlang schedulers will forcibly de-schedule the sender until space is freed. This may end up surprising a few users who didn't expect that implicit back-pressure from the VM." The condition is observable by passing the atom `busy_port` to the system monitor; for clustered nodes, `busy_dist_port` catches a local process de-scheduled when contacting a remote process whose inter-node communication runs through a busy distribution port.

# Prerequisites

- `long-schedule-monitor` — busy ports are monitored through the same `erlang:system_monitor/2` mechanism.
- `port` — you must understand what a port is before reasoning about its queue filling.

# Key Properties

1. A full port internal queue causes the scheduler to forcibly de-schedule the sending process.
2. This is implicit back-pressure from the VM, which can surprise users.
3. `busy_port` passed to `erlang:system_monitor/2` reports these de-scheduling events.
4. `busy_dist_port` reports the same for inter-node communication routed through a busy distribution port.
5. The de-scheduling can be avoided with the `nosuspend` option on the sending call.

# Construction / Recognition

To monitor: add `busy_port` (and `busy_dist_port` for clusters) to the `erlang:system_monitor/2` option list. To mitigate in critical paths: use `erlang:port_command(Port, Data, [nosuspend])` for ports and `erlang:send(Pid, Msg, [nosuspend])` for messages to distributed processes — these report when a message could not be sent instead of de-scheduling the sender.

# Context & Application

This matters for processes on critical latency paths that write heavily to ports (file/socket drivers) or to remote nodes. The implicit de-scheduling protects the port but stalls the sender; `nosuspend` lets the sender detect congestion and react rather than block.

# Examples

From section "Suspended Ports": "If you find out you're having problems with these, try replacing your sending functions where in critical paths with `erlang:port_command(Port, Data, [nosuspend])` for ports, and `erlang:send(Pid, Msg, [nosuspend])` for messages to distributed processes. They will then tell you when the message could not be sent and you would therefore have been descheduled."

# Relationships

## Builds Upon
- `long-schedule-monitor` — busy ports use the same system-monitor mechanism.
- `port` — the entity whose queue fills.

## Enables
Nothing — terminal scheduling card.

## Related
- `long-schedule-monitor` — sibling system-monitor option for scheduler diagnosis.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Writing heavily to a port on a critical path without `nosuspend`, leading to surprising de-scheduling stalls.
- Forgetting `busy_dist_port` when the bottleneck is inter-node, not a local port.

# Common Confusions

- Busy-port de-scheduling is implicit back-pressure, not a crash or an error — the sender simply stops running until queue space frees up.
- `busy_port` and `busy_dist_port` are distinct: the former is a local port, the latter the distribution port to a remote node.

# Source Reference

Chapter 8: CPU and Scheduler Hogs, Section "Suspended Ports". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Suspended Ports."
- Confidence rationale: high — the source explicitly defines the mechanism and the `nosuspend` mitigation.
- Uncertainties: none.
- Cross-reference status: Verified
