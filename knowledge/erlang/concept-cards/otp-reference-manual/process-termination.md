---
# === CORE IDENTIFICATION ===
concept: Process Termination
slug: process-termination

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Process Termination"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - exit reason
  - normal termination

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - exit-signals
  - links
  - monitors
  - error-handling-between-processes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does an Erlang process terminate?"
  - "What is an exit reason in Erlang?"
---

# Quick Definition
When an Erlang process terminates, it always does so with an exit reason, which can be any term. A process terminates normally when its exit reason is the atom `normal`, which happens when it has no more code to execute.

# Core Definition
The Erlang Reference Manual states: "When a process terminates, it always terminates with an _exit reason_. The reason can be any term." A process "is said to terminate _normally_ if the exit reason is the atom `normal`. A process with no more code to execute terminates normally." A process terminates with `{Reason,Stack}` on a run-time error. A process can also terminate itself by calling `exit(Reason)`, `error(Reason)`, or `error(Reason, Args)`. Additionally, "A process can also be terminated if it receives an exit signal with an exit reason other than `normal`." (Processes chapter, "Process Termination" section).

# Prerequisites
- **erlang-process** -- Must understand what a process is

# Key Properties
1. Every termination has an exit reason, which can be any term
2. Exit reason `normal` indicates normal termination
3. A process with no more code to execute terminates with reason `normal`
4. Run-time errors produce exit reason `{Reason, Stack}`
5. `exit(Reason)` terminates the process with the given reason
6. `error(Reason)` terminates the process with reason `{Reason, Stack}`
7. `error(Reason, Args)` terminates the process with reason `{Reason, Stack}`
8. Receiving an exit signal with a reason other than `normal` can also terminate a process

# Construction / Recognition
## To Construct/Create:
1. Let the process run to completion (all code executed) for normal termination
2. Call `exit(Reason)` to terminate with a specific reason
3. Call `error(Reason)` to terminate with `{Reason, Stack}`
4. Trigger a run-time error for abnormal termination
5. Send an exit signal from another process via `exit_signal/2`

## To Identify/Recognize:
1. A process has terminated when `is_process_alive/1` returns `false`
2. Monitors deliver `{'DOWN', Ref, process, Pid, Reason}` messages upon termination
3. Links cause exit signals to propagate to linked processes

# Context & Application
Process termination is central to Erlang's fault-tolerance model. The exit reason communicates why a process ended: `normal` means everything is fine, while any other reason signals an abnormal condition. This exit reason propagates through links as exit signals, enabling supervision trees to detect and respond to failures. Understanding the distinction between normal and abnormal termination is essential for designing robust OTP applications.

# Examples
**Example 1** (Processes, "Process Termination" section): The three BIFs for self-termination:
- `exit(Reason)` -- terminates with reason `Reason`
- `error(Reason)` -- terminates with reason `{Reason, Stack}`
- `error(Reason, Args)` -- terminates with reason `{Reason, Stack}`

# Relationships
## Builds Upon
- **erlang-process** -- Termination is one end of a process's lifecycle

## Enables
- **exit-signals** -- Termination of a linked process triggers exit signals
- **error-handling-processes** -- Exit reasons drive error handling decisions

## Related
- **links** -- Linked processes receive exit signals upon termination
- **monitors** -- Monitors deliver DOWN messages upon termination

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Forgetting that `error/1` wraps the reason in `{Reason, Stack}` while `exit/1` uses the reason directly
  **Correction**: Use `exit(Reason)` when you want the exit reason to be exactly `Reason`. Use `error(Reason)` when you want the stack trace included.

# Common Confusions
- **Confusion**: Thinking that calling `exit(normal)` is somehow different from a process naturally running out of code
  **Clarification**: Both produce the same exit reason (`normal`) and trigger the same behavior in linked processes (the exit signal is silently dropped by default).

# Source Reference
Processes chapter, "Process Termination" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit definitions of termination and exit reasons
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
