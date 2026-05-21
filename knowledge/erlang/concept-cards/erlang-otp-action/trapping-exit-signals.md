---
# === CORE IDENTIFICATION ===
concept: Trapping Exit Signals
slug: trapping-exit-signals

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: links-and-signals
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.2.2 Supervision and trapping of exit signals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - trap_exit
  - signal trapping
  - process flag

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exit-signal
  - process-link
extends:
  - exit-signal
related:
  - supervision
  - fault-tolerance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does trapping exit signals mean?"
  - "What is the trap_exit process flag?"
  - "How does a process turn an exit signal into a message?"
---

# Quick Definition

Trapping exit signals means setting the `trap_exit` process flag so that incoming exit signals are delivered as ordinary `{'EXIT', Pid, Reason}` messages instead of causing the process to exit.

# Core Definition

"One of the main ways fault tolerance is achieved in OTP is by overriding the default propagation of exit signals. By setting a *process flag* called `trap_exit`, you can make a process *trap* any incoming exit signal rather than obey it" (Chapter 1, section 1.2.2). When the signal is trapped, "it's dropped in the process's mailbox as a normal message on the form `{'EXIT', Pid, Reason}` that describes in which other process the failure originated and why, allowing the trapping process to check for such messages and take action." A signal-trapping process is sometimes called a *system process* and acts as a bulwark preventing exit signals from propagating further.

# Prerequisites

- **Exit signal** — trapping changes how an exit signal is handled.
- **Process link** — exit signals arrive via links.

# Key Properties

1. Trapping is enabled by setting the `trap_exit` process flag.
2. A trapping process does not obey an incoming exit signal.
3. The signal becomes a normal mailbox message `{'EXIT', Pid, Reason}`.
4. The message identifies the failing process and the failure reason.
5. A trapping process insulates linked processes by stopping signal propagation.

# Construction / Recognition

## To Construct/Create:
1. In the process, set the `trap_exit` process flag.
2. From then on, exit signals arrive as `{'EXIT', Pid, Reason}` messages.
3. Handle these messages in a `receive` expression and take corrective action.

# Context & Application

- **Typical contexts**: Supervisor and other system processes.
- **Common applications**: Detecting worker failures, reporting them, and restarting failed subsystems.
- **Historical/stylistic notes**: Signal trapping is the mechanism that makes supervisors possible.

# Examples

**Example 1** (section 1.2.2): A trapped exit signal is dropped in the mailbox as `{'EXIT', Pid, Reason}`, letting the trapping process check for such messages and act.

**Example 2** (Figure 1.3): A supervisor traps exit signals, acting as a bulwark that stops the crash in a worker from propagating beyond it, and then restarts the group.

# Relationships

## Builds Upon
- **Exit signal** — trapping is an alternative handling of the signal.

## Enables
- **Supervision** — supervisors trap signals to detect and recover from failures.
- **System process** — a trapping process is called a system process.

## Related
- **Fault tolerance** — trapping is a main way OTP achieves fault tolerance.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Forgetting to set `trap_exit` and expecting `{'EXIT', ...}` messages anyway.
  **Correction**: Without the flag, the process simply exits; the flag must be set first.

# Common Confusions

- **Confusion**: Believing a trapping process ignores failures entirely.
  **Clarification**: It still learns of failures — as messages — and is expected to act on them; it just does not die.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.2.2 "Supervision and trapping of exit signals." See Figure 1.3.

# Verification Notes

- Definition source: Direct adaptation from section 1.2.2.
- Confidence rationale: HIGH — the `trap_exit` flag and its effect are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
