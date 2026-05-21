---
# === CORE IDENTIFICATION ===
concept: Process Monitors
slug: process-monitors

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Monitors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - monitor
  - process monitor
  - DOWN monitor

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
  - process-termination
extends: []
related:
  - process-aliases
  - process-registration
contrasts_with:
  - process-links

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a process observe another process's termination without being affected by it?"
  - "What is the difference between a monitor and a link?"
  - "What message does a monitor deliver when the monitored process terminates?"
  - "Can you create multiple monitors for the same process?"
---

# Quick Definition
A monitor is a unidirectional observation mechanism that lets one process watch another. When the monitored process terminates, a `{'DOWN', Ref, process, Pid, Reason}` message is delivered to the monitoring process. Unlike links, monitors do not propagate exits -- they only deliver informational messages.

# Core Definition
The Erlang Reference Manual states: "An alternative to links are _monitors_. A process `Pid1` can create a monitor for `Pid2` by calling the BIF `erlang:monitor(process, Pid2)`. The function returns a reference `Ref`." When `Pid2` terminates with exit reason `Reason`, a DOWN message `{'DOWN', Ref, process, Pid2, Reason}` is sent to `Pid1`. "If `Pid2` does not exist, the 'DOWN' message is sent immediately with `Reason` set to `noproc`." The manual further states: "Monitors are unidirectional. Repeated calls to `erlang:monitor(process, Pid)` create several independent monitors, and each one sends a 'DOWN' message when `Pid` terminates." A monitor can be removed by calling `erlang:demonitor(Ref)`. "Monitors can be created for processes with registered names, also at other nodes." (Processes chapter, "Monitors" section).

# Prerequisites
- **erlang-process** -- Monitors observe process lifecycle events
- **erlang-signals** -- Monitors use the signal mechanism (monitor, demonitor, and down signals)
- **process-termination** -- Monitors detect process termination

# Key Properties
1. Unidirectional -- only the monitoring process receives notification, not the monitored process
2. Returns a unique reference `Ref` used to identify the monitor and the resulting DOWN message
3. Delivers a `{'DOWN', Ref, process, Pid2, Reason}` message upon termination of the monitored process
4. Non-destructive -- the monitoring process is not terminated or affected; it simply receives a message
5. Multiple independent monitors can exist for the same process -- each call to `monitor/2` creates a new one
6. If the target process does not exist, the DOWN message is sent immediately with reason `noproc`
7. Can monitor by registered name, including on remote nodes
8. Removed by calling `demonitor(Ref)` or `demonitor(Ref, [flush])` to also flush any pending DOWN message

# Construction / Recognition
## To Construct/Create:
1. Call `erlang:monitor(process, Pid)` -- returns a reference `Ref`
2. Call `erlang:monitor(process, {Name, Node})` to monitor a registered name on a remote node
3. Use `spawn_monitor(Module, Function, Args)` to atomically spawn and monitor
4. Use `spawn_opt/4,5` with the `monitor` option
5. Use `monitor/3` with additional options such as `{alias, _}` or `priority`

## To Remove:
1. Call `erlang:demonitor(Ref)` to remove the monitor
2. Call `erlang:demonitor(Ref, [flush])` to remove the monitor and flush any DOWN message already in the queue

## To Identify/Recognize:
1. A `{'DOWN', Ref, process, Pid, Reason}` message in the mailbox indicates a monitor was triggered
2. Use `process_info(Pid, monitors)` to see monitors created by `Pid`
3. Use `process_info(Pid, monitored_by)` to see processes monitoring `Pid`

# Context & Application
Monitors are the preferred mechanism when a process needs to know about another process's termination without coupling their fates. Unlike links, a monitor does not cause the monitoring process to crash when the monitored process dies -- it only delivers an informational message. This makes monitors ideal for client-server patterns, request/reply tracking, and any situation where you want to detect failure without being affected by it.

**Typical contexts:**
- Tracking whether a server process is alive during a pending request
- Implementing timeouts that clean up when a peer dies (e.g., `gen_server:call` uses a monitor)
- Observing processes without participating in their failure domain
- Combining with process aliases for robust request/reply patterns

# Examples
**Example 1** (Processes, "Monitors" section): Creating a monitor and receiving the DOWN message:
```erlang
Ref = erlang:monitor(process, Pid2),
receive
    {'DOWN', Ref, process, Pid2, Reason} ->
        %% Pid2 terminated with Reason
        handle_down(Reason)
end
```

**Example 2** (Processes, "Process Creation" section): Atomic spawn and monitor:
```erlang
{Pid, Ref} = spawn_monitor(Module, Function, Args)
```
Returns both the pid and monitor reference, with no race condition.

# Relationships
## Builds Upon
- **erlang-process** -- Monitors observe processes
- **erlang-signals** -- Monitor/demonitor/down are signal types
- **process-termination** -- Monitors detect termination events

## Enables
- **process-aliases** -- Aliases can be created together with monitors via `monitor/3` with `{alias, _}` option

## Related
- **process-registration** -- Monitors can target registered names

## Contrasts With
- **process-links** -- Links are bidirectional and propagate failures (exit signals that can kill the recipient). Monitors are unidirectional and only deliver informational DOWN messages. Links allow at most one per pair; monitors allow multiple independent monitors per pair. Links require `spawn_link` for atomicity; monitors have `spawn_monitor`.

# Common Errors
- **Error**: Forgetting to demonitor after a successful reply, leading to a stale DOWN message arriving later
  **Correction**: Call `demonitor(Ref, [flush])` after receiving the reply. The `flush` option removes any DOWN message already in the queue.

- **Error**: Assuming only one DOWN message can arrive for a given process
  **Correction**: If you call `monitor/2` multiple times for the same process, each creates an independent monitor, and each will deliver its own DOWN message.

# Common Confusions
- **Confusion**: Thinking monitors are bidirectional like links
  **Clarification**: Monitors are strictly unidirectional. The monitored process has no knowledge of the monitor (it does not receive a signal when it terminates because of the monitor -- it would terminate regardless). Only the monitoring process receives the DOWN message.

- **Confusion**: Thinking monitors and links serve the same purpose
  **Clarification**: Links propagate failures -- when a linked process dies, the survivor may die too (unless trapping exits). Monitors only observe -- the monitoring process receives a message but is never terminated by the monitor mechanism.

# Source Reference
Processes chapter, "Monitors" section, with additional context from "Sending Signals" and "Receiving Signals" subsections.

# Verification Notes
- Definition source: Direct from source -- all key statements quoted from the "Monitors" section
- Confidence rationale: High -- concise, self-contained section with explicit definitions
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to existing or planned cards
