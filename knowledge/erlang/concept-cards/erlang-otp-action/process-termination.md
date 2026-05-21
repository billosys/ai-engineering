---
# === CORE IDENTIFICATION ===
concept: Process Termination
slug: process-termination

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-lifecycle
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.1.4 Programming with processes in Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process exit
  - process death

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - exit-signal
  - process-link
  - garbage-collector
  - exception
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when an Erlang process terminates?"
  - "How does a process clean up its resources?"
  - "What is the difference between normal and abnormal termination?"
---

# Quick Definition

Process termination is the end of a process's life. When a process is done — or crashes — it disappears and its memory, mailbox, and other resources are recycled.

# Core Definition

"When a process is done with its work, it disappears. Its working memory, mailbox, and other resources are recycled" (Chapter 1, section 1.1.4). If the process's purpose was to produce data for another process, it must send that data explicitly as a message before terminating. Termination can also happen unexpectedly and prematurely through crashes (exceptions); when this happens, other processes can be informed of the crash. An exception that propagates back past the initial call of a process causes that process to die (Chapter 2, section 2.8). Normal termination — including `exit(normal)` — is not regarded as abnormal by linked processes.

# Prerequisites

- **Erlang process** — termination is the end of a process's lifecycle.

# Key Properties

1. A finished process disappears; its memory, mailbox, and resources are recycled.
2. A process must send any results as messages before it terminates.
3. Crashes (exceptions) can terminate a process prematurely.
4. On termination, linked processes can be informed via an exit signal.
5. Normal termination (including `exit(normal)`) is not treated as abnormal by linked processes.

# Construction / Recognition

## To Identify/Recognize:
1. A process ends when its code finishes or an uncaught exception propagates past its initial call.
2. The runtime reclaims the process's resources automatically.
3. An exit signal carrying the reason is generated for linked processes.

# Context & Application

- **Typical contexts**: Short-lived worker processes; cleanup of complex state.
- **Common applications**: A spawned task that produces a result then dies; the "let it crash" pattern relies on clean termination.
- **Historical/stylistic notes**: Automatic cleanup at termination removes the need to manually free database handles, sockets, and other resources.

# Examples

**Example 1** (section 1.1.4): A spawned process prints "erlang!" and then quits, disappearing afterward.

**Example 2** (section 1.1.4, "Programming with processes in Erlang"): When a complex operation completes, the processes involved "disappear magically into oblivion," taking with them their internal state, database handles, and sockets.

# Relationships

## Builds Upon
- **Erlang process** — termination ends the process lifecycle.

## Enables
- **Exit signal** — abnormal termination generates an exit signal.
- **Garbage collector** — terminated processes' memory is reclaimed.

## Related
- **Process link** — links propagate termination to other processes.
- **Exception** — uncaught exceptions cause premature termination.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Letting a worker process terminate before it has sent its result.
  **Correction**: A process must send any data it produces as a message before it dies.

# Common Confusions

- **Confusion**: Believing a crash leaves resources leaked.
  **Clarification**: The runtime recycles a terminated process's memory, mailbox, and resources automatically.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.4 "Programming with processes in Erlang," "Process termination" subsection. See also Chapter 2, section 2.8 "Exceptions, try, and catch."

# Verification Notes

- Definition source: Direct adaptation from section 1.1.4, supplemented by section 2.8.
- Confidence rationale: HIGH — termination and resource recycling are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
