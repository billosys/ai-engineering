---
# === CORE IDENTIFICATION ===
concept: Exit Signals
slug: exit-signals

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: process-termination
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Links"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - trap_exit
  - trapping exits
  - EXIT message
  - exit BIF

# === TYPED RELATIONSHIPS ===
prerequisites:
  - links
extends: []
related:
  - processes-and-message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an exit signal in Erlang?"
  - "What does trapping exits do?"
  - "Why does a process exit normally or abnormally?"
---

# Quick Definition

An exit signal is sent between linked processes when one terminates. A process can convert exit signals into ordinary mailbox messages by trapping exits with `process_flag(trap_exit, true)`.

# Core Definition

"Exit signals can be trapped by calling the `process_flag(trap_exit, true)` function. This converts exit signals into messages of the form `{'EXIT', Pid, Reason}`, where Pid is the process identifier of the process that has died and Reason is the reason it has terminated. ... When a process is trapping exits, the exit signal is not propagated to any of the processes in its link set" (Cesarini & Vinoski, p. 37). A process exits *normally* (reason `normal`) when it has no more code to execute; *abnormal termination* arises "in case of a runtime error, receiving an exit signal when not trapping exits, or by calling the exit BIFs" (p. 37). `exit(Reason)` terminates the caller; `exit(Pid, Reason)` sends an exit signal to `Pid`.

# Prerequisites

- **Links** — Exit signals propagate along links; understanding linking is required first.

# Key Properties

1. When a linked process terminates, an exit signal carries the dead pid and a reason.
2. `process_flag(trap_exit, true)` converts exit signals into `{'EXIT', Pid, Reason}` messages.
3. A trapping process does not propagate the signal to its link set.
4. Normal termination carries reason `normal`.
5. `exit(Reason)` terminates the calling process; `exit(Pid, Reason)` signals another process.
6. The `kill` reason force-terminates even a trapping process; the survivor's reason becomes `killed`, which does not itself propagate.
7. Propagation semantics depend on the reason and whether exits are trapped (see Table 2-1).

# Construction / Recognition

## To Construct:
1. Call `process_flag(trap_exit, true)` to trap exits.
2. Handle `{'EXIT', Pid, Reason}` messages in a `receive`.
3. Use `exit(Reason)` or `exit(Pid, Reason)` to terminate processes deliberately.

## To Recognize:
1. A `process_flag(trap_exit, true)` call, or `receive` clauses matching `{'EXIT', ...}`.

# Context & Application

- **Typical contexts**: Supervision; a process that must survive its linked children's deaths.
- **Common applications**: Supervisors trap exits so they receive `'EXIT'` messages instead of dying.
- **Historical/stylistic notes**: Trapping exits plus links is the substrate for OTP's complex supervision strategies.

# Examples

**Example 1** (p. 38, Table 2-1): Propagation semantics — when trapping exits, a `normal` exit yields `{'EXIT', Pid, normal}`; when not trapping, nothing happens. A `kill` always terminates the target with reason `killed`.

**Example 2** (p. 39): `exit(Pid, kill)` on a monitored process produces a `{'DOWN', ..., killed}` message:

```erlang
3> exit(Pid, kill).
true
```

# Relationships

## Builds Upon
- **Links** — Exit signals travel along links.

## Enables
- *(none specific in scope)*

## Related
- **Processes and message passing** — Trapped exit signals become ordinary mailbox messages.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Expecting `kill` to be the survivor's termination reason.
  **Correction**: A `kill` signal terminates the target with reason `killed`, ensuring unconditional termination does not itself propagate.

# Common Confusions

- **Confusion**: Believing a trapping process still propagates exit signals to its link set.
  **Clarification**: When trapping exits, the signal is converted to a message and is *not* propagated further.

# Source Reference

Chapter 1: Introducing Erlang, Section "Links," pages 37-38. See Table 2-1 (propagation semantics).

# Verification Notes

- Definition source: Direct quotes from pp. 37-38.
- Confidence rationale: HIGH — explicit definition, BIF descriptions, and a semantics table.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
