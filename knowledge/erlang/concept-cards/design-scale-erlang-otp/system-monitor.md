---
# === CORE IDENTIFICATION ===
concept: System Monitor
slug: system-monitor

# === CLASSIFICATION ===
category: production-ops
subcategory: runtime-monitoring
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "The System Monitor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "erlang:system_monitor"
  - system monitor BIF

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
extends: []
related:
  - sockets-and-ssl-transport
  - bottleneck
  - metrics
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the system monitor BIF?"
  - "How do I detect a congested distributed Erlang port?"
---

# Quick Definition

The system monitor is an Erlang BIF, `erlang:system_monitor/2`, that triggers trace messages on memory- and scheduler-related events such as a congested distributed port, long garbage collections, or unusually large heaps.

# Core Definition

"A call to `erlang:system_monitor(Pid, [busy_dist_port])` sets up monitoring. A trace message of the format `{monitor, SusPid, busy_dist_port, Port}` will be sent to Pid every time a process gets suspended because it is trying to send a message through an internode communication port already being used by another process. SusPid is the suspended process" (Cesarini & Vinoski, p. 392). Other scheduler-related items that can be monitored include `busy_port` and `long_schedule`; important memory-related monitors include `long_gc` and `large_heap`, triggered if a process spends too long garbage collecting or allocates an unusually large heap.

# Prerequisites

- **Distributed Erlang** — A key use is detecting a congested distributed Erlang port; understand distributed Erlang first.

# Key Properties

1. Invoked via the `erlang:system_monitor(Pid, Options)` BIF.
2. `busy_dist_port` reports when a process is suspended trying to use a busy internode port.
3. Scheduler-related options include `busy_port` and `long_schedule`.
4. Memory-related options include `long_gc` and `large_heap`.
5. Trace messages are sent to a designated monitoring process.
6. Can generate huge volumes of messages under load if used carelessly.

# Construction / Recognition

## To Construct/Create:
1. Call `erlang:system_monitor(Pid, [busy_dist_port])` (or other options) to enable monitoring.
2. Receive `{monitor, SusPid, Tag, Detail}` trace messages in the designated process.
3. Take appropriate action (or count events) rather than logging every message.

## To Identify/Recognize:
1. Recognize system-monitor events as `{monitor, ...}` trace messages tied to scheduler or memory conditions.

# Context & Application

- **Typical contexts**: Detecting distributed-port congestion, long GCs, and memory spikes.
- **Common applications**: Diagnosing bottlenecks during capacity testing; finding the cause of node crashes.
- **Historical/stylistic notes**: The BIF is "hidden deep in the documentation of Erlang/OTP" (p. 392); monitoring is covered further in chapter 15.

# Examples

**Example 1** (p. 392): `erlang:system_monitor(Pid, [busy_dist_port])` sends `{monitor, SusPid, busy_dist_port, Port}` whenever a process is suspended on a busy internode port.

**Example 2** (p. 436): Turning on the system monitor revealed an unusually high number of long-GC and large-heap trace events seconds before a node crash, traced to memory spikes when parsing XML session data.

# Relationships

## Builds Upon
- **Distributed Erlang** — `busy_dist_port` monitoring reports on the distributed port

## Enables
- **Bottleneck** — System monitor events surface scheduler and memory bottlenecks

## Related
- **Sockets and ssl transport** — System monitor detects the dist-port congestion that motivates sockets
- **Metrics** — System-monitor events can be counted as metrics

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Logging every system-monitor message in a live system
  **Correction**: Millions can be generated per hour under heavy load; use an incremental counter and toggle detailed logging only when debugging.

# Common Confusions

- **Confusion**: The system monitor is a separate tool or application.
  **Clarification**: It is a built-in BIF (`erlang:system_monitor`) of the Erlang runtime.

# Source Reference

Chapter 12: Distributed Architectures, "The System Monitor," pages 392-393. See also the `erlang` manual page for `system_monitor` and Chapter 15 on monitoring.

# Verification Notes

- Definition source: Direct quote from p. 392.
- Confidence rationale: HIGH — the source names the BIF, its options, and message format explicitly.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
