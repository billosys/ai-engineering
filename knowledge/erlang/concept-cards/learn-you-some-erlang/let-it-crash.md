---
concept: Let It Crash
slug: let-it-crash
category: fault-tolerance
subcategory: error-philosophy
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Fault Tolerance"
extraction_confidence: high
aliases:
  - "let it crash"
  - "fail fast"
  - "crash-only"
prerequisites:
  - process
extends: []
related:
  - keeping-processes-alive
  - trapping-exits
contrasts_with: []
answers_questions:
  - "What is the let-it-crash philosophy?"
  - "How do supervisors relate to the let-it-crash philosophy?"
---

# Let It Crash

## Quick Definition

"Let it crash" is Erlang's fault-tolerance philosophy: rather than defensively preventing every error, let a faulty process die quickly and cleanly, then restart it — avoiding the propagation of corrupt data.

## Core Definition

The chapter explains that Erlang's designers "always kept in mind that failure is common" — bugs creep in, and hardware eventually fails — so "the idea is to find good ways to handle errors and problems, rather than trying to prevent them all." A guiding principle: "errors that corrupt data should cause the faulty part of the system to die as fast as possible in order to avoid propagating errors and bad data to the rest of the system." Studies show transient/intermittent bugs are a main source of downtime, so "the ideal solution in Erlang is thus to kill processes as fast as possible to avoid data corruption and transient bugs." A safe approach makes "all crashes the same as clean shutdowns," supported by shared-nothing memory, single assignment, and avoiding locks. Lightweight processes — built for quick restart and shutdown — make this practical. The RPN calculator chapter (ch. 8) states it tersely: "Erlang's policy is to let it crash" (Hébert, ch. 10, "Fault Tolerance"; ch. 8).

## Prerequisites

- **Process** — Crashing and restarting operate on isolated processes

## Key Properties

1. Failure is assumed inevitable — handle errors rather than prevent every one
2. A process that detects corrupt data should die immediately to avoid propagation
3. Transient/intermittent bugs are a leading cause of downtime; a fast restart often clears them
4. The aim is to make every crash equivalent to a clean shutdown
5. Shared-nothing memory, single assignment, and avoiding locks keep crashes isolated
6. Lightweight processes make rapid restart and shutdown cheap
7. The pattern needs a watcher (trapping exits / a supervisor) to perform the restart

## Construction / Recognition

## To Apply Let It Crash

1. Write only the "happy case" in worker processes — no defensive error handling
2. Let a process crash on unexpected input rather than guessing a recovery
3. Isolate state per process (shared-nothing) so a crash cannot corrupt others
4. Pair workers with a watcher that traps exits and restarts them
5. Treat a fast restart as the recovery mechanism

## Examples

> **RPN calculator** (ch. 8): a malformed expression crashes on the `[Res]` match — "Given that Erlang's policy is to let it crash, that's the path chosen here."
>
> **Fast death** (ch. 10): "errors that corrupt data should cause the faulty part of the system to die as fast as possible."

## Relationships

## Related

- **Keeping processes alive** — A restarter/supervisor is what makes "let it crash" safe
- **Trapping exits** — The mechanism by which a watcher learns of a crash and restarts the worker

## Common Errors

- **Error**: Wrapping worker code in defensive `try ... catch` for every possible error
  **Correction**: Let the process crash; restart it — defensive code clutters the happy case
- **Error**: Letting a process die without anything to restart it
  **Correction**: Pair crashing workers with a supervisor/restarter

## Common Confusions

- **Confusion**: Thinking "let it crash" means ignoring errors
  **Clarification**: It means handling errors *out of band* via crash-and-restart, not ignoring them
- **Confusion**: Believing crashing is unsafe
  **Clarification**: With shared-nothing isolation a crash is contained and made equivalent to a clean shutdown

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "Concurrency Concepts," subsection "Fault Tolerance"; Chapter 8 RPN calculator discussion.

## Verification Notes

- Philosophy and fast-death principle: directly from ch. 10
- "Let it crash" phrasing: from ch. 8
- Confidence: HIGH — explicitly discussed
