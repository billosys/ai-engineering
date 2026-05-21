---
# === CORE IDENTIFICATION ===
concept: Monitors
slug: monitors

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Monitors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process monitor
  - erlang:monitor
  - DOWN message
  - reference

# === TYPED RELATIONSHIPS ===
prerequisites:
  - processes-and-message-passing
extends: []
related:
  - exit-signals
contrasts_with:
  - links

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a monitor in Erlang?"
  - "How do links relate to monitors?"
  - "What distinguishes links from monitors?"
---

# Quick Definition

A monitor is a unidirectional mechanism for one process to observe another's termination. When the monitored process dies, the monitoring process receives a `'DOWN'` message; it is not itself terminated.

# Core Definition

"Monitors provide an alternative, unidirectional mechanism for processes to observe the termination of other processes" (Cesarini & Vinoski, p. 38). "A monitor is set up when process A calls `erlang:monitor(process, B)` ... This causes A to monitor B." Monitors "have an identity given by an Erlang reference, which is a unique value returned by the call." A monitor "is unidirectional rather than bidirectional." "When a monitored process terminates, a message of the form `{'DOWN', Reference, process, Pid, Reason}` is sent to the monitoring process." A monitor is removed with `erlang:demonitor(Reference)`; the `[flush]` option additionally clears any pending `'DOWN'` messages.

# Prerequisites

- **Processes and message passing** — Monitors observe processes and deliver `'DOWN'` messages via the mailbox.

# Key Properties

1. `erlang:monitor(process, B)` sets up a monitor and returns a unique reference.
2. Monitors are unidirectional: A monitoring B does not mean B monitors A.
3. Multiple monitors of B by A are allowed, each with a distinct reference.
4. Termination delivers `{'DOWN', Reference, process, Pid, Reason}` to the monitor.
5. `erlang:demonitor(Reference)` removes a monitor; `[flush]` also clears pending `'DOWN'` messages.
6. Monitoring a nonexistent process yields a `'DOWN'` with reason `noproc` (it does not crash the caller).
7. A monitoring process not trapping exits is *not* terminated when the monitored process dies.

# Construction / Recognition

## To Construct:
1. Call `erlang:monitor(process, B)` and keep the returned reference.
2. Handle `{'DOWN', Ref, process, Pid, Reason}` in a `receive`.
3. Call `erlang:demonitor(Ref, [flush])` to remove the monitor and flush stale messages.

## To Recognize:
1. Look for `erlang:monitor/2` / `erlang:demonitor` calls or `{'DOWN', ...}` patterns.

# Context & Application

- **Typical contexts**: A client observing a server without risking being killed by it.
- **Common applications**: `gen_server:call` uses a monitor to detect a crashed server during a synchronous request.
- **Historical/stylistic notes**: References, which monitors generate, guarantee message identity across a multinode system.

# Examples

**Example 1** (p. 39): Setting up a monitor and seeing the `'DOWN'` message:

```erlang
1> Pid = spawn(echo, loop, []).
<0.34.0>
2> erlang:monitor(process, Pid).
#Ref<0.0.0.34>
3> exit(Pid, kill).
true
4> flush().
Shell got {'DOWN',#Ref<0.0.0.34>,process,<0.34.0>,killed}
ok
```

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- *(none specific in scope)*

## Related
- **Exit signals** — Both are failure-detection mechanisms; monitors deliver messages rather than signals.

## Contrasts With
- **Links** — Links are bidirectional and propagate termination; monitors are unidirectional and never kill the observer.

# Common Errors

- **Error**: Forgetting `[flush]` on `demonitor`, leaving a stale `'DOWN'` message in the mailbox.
  **Correction**: Use `erlang:demonitor(Ref, [flush])` to avoid a memory leak from lingering `'DOWN'` messages.

# Common Confusions

- **Confusion**: Thinking monitoring a dead process crashes the monitor (as linking would).
  **Clarification**: Monitoring a nonexistent process simply yields a `'DOWN'` message with reason `noproc`.

# Source Reference

Chapter 1: Introducing Erlang, Section "Monitors," pages 38-39. See the "References" sidebar on p. 39.

# Verification Notes

- Definition source: Direct quotes from pp. 38-39.
- Confidence rationale: HIGH — explicit definition with itemized link/monitor differences.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
