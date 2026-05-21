---
# === CORE IDENTIFICATION ===
concept: Process Links
slug: process-links

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
section: "Links"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - link
  - bidirectional link
  - process link

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
  - process-termination
extends: []
related:
  - exit-signals
  - trapping-exits
  - process-creation
contrasts_with:
  - process-monitors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes propagate failures to each other?"
  - "What is the difference between link/1 and spawn_link?"
  - "How do links differ from monitors?"
  - "What happens when a linked process terminates?"
---

# Quick Definition
A link is a bidirectional connection between two processes (or a process and a port on the same node) that causes an exit signal to be sent to the survivor when either participant terminates. Links are the foundation of Erlang's error-propagation mechanism.

# Core Definition
The Erlang Reference Manual states: "Two processes can be _linked_ to each other. Also, a process and a port that reside on the same node can be linked to each other." A link is created by calling `link/1` with the other process's pid, or atomically at spawn time using `spawn_link()`, `spawn_opt()`, or `spawn_request()`. "If one of the participants of a link terminates, it will send an exit signal to the other participant. The exit signal will contain the exit reason of the terminated participant." Links are bidirectional, and "there can only be one link between two processes. Repeated calls to `link()` have no effect. Either one of the involved processes may create or remove a link." A link is removed by calling `unlink/1`. (Processes chapter, "Links" section).

# Prerequisites
- **erlang-process** -- Links connect processes to each other
- **erlang-signals** -- Links operate through the signal mechanism (link, unlink, and exit signals)
- **process-termination** -- Links trigger exit signals upon process termination

# Key Properties
1. Bidirectional -- if A links to B, then B is also linked to A
2. At most one link between any two processes -- repeated `link/1` calls are idempotent
3. Either participant can create or remove the link
4. When a linked process terminates, an exit signal carrying the exit reason is sent to the other participant
5. Links can be created atomically with spawn using `spawn_link/1,2,3,4`, `spawn_opt/2,3,4,5`, or `spawn_request/1,2,3,4,5`
6. Links can also exist between a process and a port on the same node
7. The exit signal sent due to a link has the `link` flag set, which affects how it is handled
8. The exit signal is sent after all directly visible Erlang resources used by the terminating process have been released

# Construction / Recognition
## To Construct/Create:
1. Call `link(PidOrPort)` to create a link to an existing process or port
2. Use `spawn_link(Module, Function, Args)` to atomically spawn and link -- this prevents a race condition where the spawned process could die before the link is established
3. Use `spawn_opt/4,5` with the `link` option
4. Use `spawn_request/1,2,3,4,5` with the `link` option

## To Remove:
1. Call `unlink(PidOrPort)` to deactivate the link

## To Identify/Recognize:
1. Use `process_info(Pid, links)` to see all processes linked to `Pid`
2. Exit signals with the `link` flag set indicate they were sent due to a link

# Context & Application
Links are the mechanism that makes Erlang's supervision trees possible. When a worker process crashes, the link ensures its supervisor is notified via an exit signal. The supervisor (which traps exits) receives the exit as a message and can decide how to respond -- typically by restarting the failed process.

**Typical contexts:**
- Supervision trees: supervisors link to their child processes
- Worker groups: workers that should fail together are linked
- Any scenario where one process's failure should affect another
- Atomic spawn-and-link to avoid race conditions

# Examples
**Example 1** (Processes, "Links" section): Creating a link with `link/1`:
```erlang
link(Pid2)
```
This creates a bidirectional link between the calling process and `Pid2`.

**Example 2** (Processes, "Process Creation" section): Atomic spawn and link:
```erlang
spawn_link(Module, Name, Args) -> pid()
```
The spawn and link operations are performed atomically, ensuring no race condition.

**Example 3** (Processes, "Links" section): When `Pid2` terminates, an exit signal is sent to `Pid1` containing the exit reason. If the link was created between `Pid1` and `Pid2`, and `Pid2` exits with reason `crashed`, then `Pid1` receives an exit signal with reason `crashed`.

# Relationships
## Builds Upon
- **erlang-process** -- Links connect processes
- **erlang-signals** -- Link/unlink operations and exit signals are all signals
- **process-termination** -- Termination triggers exit signal propagation through links

## Enables
- **exit-signals** -- Links are the primary mechanism that triggers exit signal propagation
- **trapping-exits** -- Trapping exits is the mechanism to handle exit signals from links

## Related
- **process-creation** -- `spawn_link` combines creation and linking atomically

## Contrasts With
- **process-monitors** -- Links are bidirectional and propagate exits (potentially killing the recipient); monitors are unidirectional and deliver informational DOWN messages without affecting the monitoring process

# Common Errors
- **Error**: Creating a link with `link/1` after `spawn/3` and assuming no race condition
  **Correction**: Use `spawn_link/3` to atomically spawn and link. With separate `spawn` + `link` calls, the spawned process could terminate before the link is established, and the exit signal would be lost.

- **Error**: Calling `link/1` on a nonexistent process and not handling the resulting `noproc` exit signal
  **Correction**: If the process does not exist when `link/1` is called, an exit signal with reason `noproc` is sent back to the caller. Be prepared to handle this or use monitors instead.

# Common Confusions
- **Confusion**: Thinking links are unidirectional (like monitors)
  **Clarification**: Links are always bidirectional. If process A calls `link(B)`, then B is also linked to A. Either process terminating will send an exit signal to the other.

- **Confusion**: Thinking multiple `link/1` calls create multiple links
  **Clarification**: There can only be one link between two processes. Repeated calls to `link()` have no effect.

# Source Reference
Processes chapter, "Links" section, with additional context from "Error Handling", "Sending Exit Signals", and "Process Creation" sections.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit definitions and behavior described in dedicated section
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction set
