---
# === CORE IDENTIFICATION ===
concept: Exit Signals
slug: exit-signals

# === CLASSIFICATION ===
category: error-handling
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Error Handling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - exit signal
  - exit signal propagation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
  - process-links
  - process-termination
extends: []
related:
  - trapping-exits
  - signal-delivery
  - signal-irregularities
contrasts_with:
  - process-monitors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when a linked process terminates?"
  - "How are exit signals propagated in Erlang?"
  - "What is the difference between exit signals sent by links and by exit_signal/2?"
  - "What does an exit signal contain?"
  - "What does the link flag in an exit signal do?"
---

# Quick Definition
An exit signal is a signal sent to linked processes when a process terminates, or sent explicitly via `exit_signal/2`. Exit signals carry the sender's identity, the exit reason, and a link flag indicating whether the signal was sent due to a link. They are the mechanism through which process failures propagate in Erlang.

# Core Definition
The Erlang Reference Manual states: "Erlang has a built-in feature for error handling between processes. Terminating processes emit exit signals to all linked processes, which can terminate as well or handle the exit in some way. This feature can be used to build hierarchical program structures where some processes are supervising other processes, for example, restarting them if they terminate abnormally." (Processes chapter, "Error Handling" section).

Exit signals sent due to a link contain: the sender identifier (pid or port of the terminated process), the receiver identifier, the `link` flag (set), and the exit reason. Exit signals sent explicitly via `exit_signal(PidOrPort, Reason)` contain: the sender identifier (pid of the caller), the receiver identifier, the `link` flag (not set), and the exit reason. (Processes chapter, "Sending Exit Signals" section).

# Prerequisites
- **erlang-process** -- Exit signals flow between processes
- **erlang-signals** -- Exit signals are a type of asynchronous signal
- **process-links** -- Links are the primary trigger for exit signal propagation
- **process-termination** -- Process termination triggers exit signals to linked processes

# Key Properties
1. Exit signals contain four components: sender identifier, receiver identifier, link flag, and exit reason
2. When a process terminates, it sends exit signals to all linked processes and ports
3. The exit signal is sent after all directly visible Erlang resources have been released
4. The exit reason for link-triggered signals is the terminated process's exit reason, or `noproc` if the process never existed, or `noconnection` if the node connection was lost
5. Exit signals can be sent explicitly via `exit_signal(PidOrPort, Reason)` -- these have the link flag unset
6. The `link` flag matters: it determines whether `kill` reason is trappable and whether an inactive link causes the signal to be dropped
7. Exit reason `kill` sent via `exit_signal/2` (link flag not set) is unconditionally fatal and cannot be trapped
8. Exit reason `kill` sent via a link (link flag set) can be trapped and is not converted to `killed`

# Construction / Recognition
## To Construct/Create:
1. A process terminating while linked to other processes automatically sends exit signals to all linked participants
2. Call `exit_signal(PidOrPort, Reason)` to explicitly send an exit signal (link flag not set)
3. Exit reason `kill` via `exit_signal/2` creates an unconditionally fatal signal

## To Identify/Recognize:
1. When trapping exits, exit signals become `{'EXIT', SenderID, Reason}` messages in the message queue
2. Without trapping exits, a process receiving an exit signal with a non-normal reason terminates
3. Exit signals with reason `normal` are silently dropped when the receiver is not trapping exits

# Context & Application
Exit signals are the core mechanism for Erlang's "let it crash" philosophy. When a process crashes, its exit signal propagates through links, potentially bringing down related processes. Supervisors trap these exits to detect child failures and restart them. This creates a natural error containment and recovery hierarchy.

**Typical contexts:**
- Supervision trees: supervisor traps exits from worker children
- Cascading failures: linked worker groups fail together
- Forceful termination: `exit_signal(Pid, kill)` for unconditional process killing
- Graceful shutdown: `exit_signal(Pid, shutdown)` following OTP conventions

# Examples
**Example 1** (Processes, "Sending Exit Signals" section): When a linked process terminates, the exit signal contains:
- Sender identifier: the pid of the terminated process
- Receiver identifier: the pid of the linked process
- Link flag: set (indicating the signal was sent due to a link)
- Exit reason: the exit reason of the terminated process

**Example 2** (Processes, "Sending Exit Signals" section): Explicitly sending an exit signal:
```erlang
exit_signal(Pid, Reason)
```
This sends an exit signal with the link flag not set. If `Reason` is `kill`, the receiver "cannot trap the exit signal and will unconditionally terminate."

**Example 3** (Processes, "Sending Exit Signals" section): Special exit reasons for link signals:
- `noproc` -- "in case no process or port was found when setting up a link in a preceding call to `link(PidOrPort)`"
- `noconnection` -- "in case the linked processes reside on different nodes and the connection between the nodes was lost or could not be established"

# Relationships
## Builds Upon
- **erlang-process** -- Exit signals flow between processes
- **erlang-signals** -- Exit signals are a signal type
- **process-links** -- Links are the primary trigger for exit signal emission
- **process-termination** -- Termination triggers exit signal sending

## Enables
- **trapping-exits** -- Trapping exits converts exit signals into messages

## Related
- **signal-delivery** -- Exit signals follow the same delivery guarantees as other signals
- **signal-irregularities** -- Exit reason `kill` behaves differently depending on the link flag

## Contrasts With
- **process-monitors** -- Monitors deliver DOWN messages (informational, never fatal). Exit signals can terminate the receiver.

# Common Errors
- **Error**: Using `exit(Pid, Reason)` instead of `exit_signal(Pid, Reason)` (or vice versa) without understanding the difference
  **Correction**: `exit(Reason)` terminates the calling process with the given reason. `exit_signal(PidOrPort, Reason)` sends an exit signal to another process. Be clear about which operation you intend.

- **Error**: Assuming `exit_signal(Pid, normal)` will terminate the target process
  **Correction**: An exit signal with reason `normal` is silently dropped by a process that is not trapping exits. Only non-normal exit reasons cause termination.

# Common Confusions
- **Confusion**: Thinking exit reason `kill` always behaves the same way
  **Clarification**: The behavior of `kill` depends on the link flag. When sent via `exit_signal/2` (link flag not set), it is unconditionally fatal and cannot be trapped. When sent via a link (link flag set), it can be trapped and the reason is not converted to `killed`.

- **Confusion**: Thinking exit signals and DOWN messages are the same
  **Clarification**: Exit signals come from links and can terminate the receiver. DOWN messages come from monitors and are always informational -- they never cause the recipient to terminate.

# Source Reference
Processes chapter, "Error Handling" section, including "Sending Exit Signals" and "Receiving Exit Signals" subsections.

# Verification Notes
- Definition source: Direct from source -- all key behaviors quoted from dedicated subsections
- Confidence rationale: High -- detailed, explicit section with precise behavioral descriptions
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to existing or planned cards
