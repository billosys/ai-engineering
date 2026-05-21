---
# === CORE IDENTIFICATION ===
concept: Exit Signal
slug: exit-signal

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: links-and-signals
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.2.1 How process links work"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - exit signal
  - "{'EXIT', Pid, Reason}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-link
  - process-termination
extends: []
related:
  - trapping-exit-signals
  - supervision
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an exit signal?"
  - "When is an exit signal generated?"
  - "How does an exit signal propagate?"
---

# Quick Definition

An exit signal is the signal generated when a process dies; it is delivered to all processes linked to the dying process and, by default, makes them exit too.

# Core Definition

"When an Erlang process dies unexpectedly, an *exit signal* is generated. All processes that are *linked* to the dying process receive this signal" (Chapter 1, section 1.2.1). By default, receiving the signal causes a process to exit and propagate the signal on to its own linked processes. The default propagation can be overridden: a process with the `trap_exit` flag set instead receives the signal as a normal message in its mailbox of the form `{'EXIT', Pid, Reason}`, describing in which process the failure originated and why (section 1.2.2).

# Prerequisites

- **Process link** — exit signals travel along links.
- **Process termination** — an exit signal is generated when a process dies.

# Key Properties

1. Generated when a process dies (especially when it dies unexpectedly).
2. Delivered to all processes linked to the dying process.
3. By default it causes a linked receiver to exit and re-propagate the signal.
4. A trapping process receives it instead as a message `{'EXIT', Pid, Reason}`.
5. The signal carries the originating pid and the reason for the failure.

# Construction / Recognition

## To Identify/Recognize:
1. A process death triggers exit-signal generation.
2. Non-trapping linked processes obey it and exit.
3. Trapping linked processes see a `{'EXIT', Pid, Reason}` message in their mailbox.

# Context & Application

- **Typical contexts**: Failure propagation in groups of linked processes.
- **Common applications**: Supervisors trap exit signals to detect and react to worker failures.
- **Historical/stylistic notes**: The `{'EXIT', Pid, Reason}` message form is the basis on which supervisors observe failures.

# Examples

**Example 1** (Figure 1.2): An exit signal triggered by a crashing process is propagated to all its linked processes, generally making those terminate as well.

**Example 2** (section 1.2.2): When trapped, the signal "is dropped in the process's mailbox as a normal message on the form `{'EXIT', Pid, Reason}`."

# Relationships

## Builds Upon
- **Process link** — links are the conduits for exit signals.
- **Process termination** — termination triggers the signal.

## Enables
- **Supervision** — trapped exit signals let supervisors detect failures.

## Related
- **Trapping exit signals** — changes how a process handles the signal.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Expecting to read an exit signal as a message without setting `trap_exit`.
  **Correction**: Only a process with `trap_exit` set receives the signal as an `{'EXIT', Pid, Reason}` message; otherwise it simply exits.

# Common Confusions

- **Confusion**: Believing an exit signal is an ordinary message.
  **Clarification**: It is a signal; it only *becomes* a normal `{'EXIT', Pid, Reason}` message for processes that trap it.

# Source Reference

Chapter 1: The Erlang/OTP platform, sections 1.2.1 "How process links work" and 1.2.2 "Supervision and trapping of exit signals." See Figure 1.2.

# Verification Notes

- Definition source: Direct adaptation from sections 1.2.1 and 1.2.2.
- Confidence rationale: HIGH — the exit signal and its `{'EXIT', Pid, Reason}` form are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
