---
concept: Blocking Operation in a Hub Process
slug: blocking-operation-in-hub-process
category: anti-patterns
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Locks and Blocking Operations"
extraction_confidence: high
aliases:
  - "Locks and blocking operations"
prerequisites:
  - message-queue-overload
extends: []
related:
  - error-logger-overload
  - back-pressure
contrasts_with: []
answers_questions:
  - "How can long-running operations be made safer?"
  - "Name the common sources of overload in Erlang systems."
---

# Quick Definition

This anti-pattern is performing a blocking or long-running operation inside a central hub process that constantly receives new tasks, so messages pile up in its mailbox while it is blocked.

# Core Definition

From Chapter 3, section "Locks and Blocking Operations": "Locking and blocking operations will often be problematic when they're taking unexpectedly long to execute in a process that's constantly receiving new tasks... During blocking operations of this kind, messages are free to pile up in the message queue."

The principle: "When there is *any* point of your program that ends up being a central hub for receiving messages, lengthy tasks should be moved out of there if possible."

# Prerequisites

- `message-queue-overload` — the anti-pattern causes queue overload.

# Key Properties

1. A central hub process blocks (e.g. on a TCP accept or socket receive) while messages keep arriving.
2. A small per-operation slowdown is amplified by the message rate, so latency can spike non-linearly.
3. Fix 1: move blocking work to the caller processes, while the hub still enforces the limits.
4. Fix 2: add helper processes that either perform the blocking work or act as a buffer while the main process blocks.
5. Fix 3: make the blocking task asynchronous — start the job with a unique token, and have the result sent back later so the hub is never blocked.
6. More processes add complexity for work that is not intrinsically concurrent — confirm you need them before "programming defensively."

# Construction / Recognition

Recognize a hub process whose `handle_*` callbacks perform blocking I/O. Fix by relocating the blocking work (to callers or helper processes) or by converting it to an asynchronous request/token/reply pattern.

# Context & Application

This is the second common overload source in Chapter 3. The fix is a key technique for "handling predictable overload" — overload you know for a fact will occur in production.

# Examples

From Chapter 3, section "Locks and Blocking Operations": in a forked `lhttpc` HTTP connection pool, a 10 ms connection timeout was fine until a remote server went down. Then "all connecting operations would take at least 10 milliseconds... With around 9,000 messages per second to the central process, each usually taking under 5 milliseconds, the impact became similar to roughly 18,000 messages a second and things got out of hand." The fix: "leave the task of connecting to the caller process, and enforce the limits as if the manager had done it on its own."

# Relationships

## Builds Upon
Nothing — it is an anti-pattern card.

## Enables
Nothing.

## Related
- `error-logger-overload` — another common overload source in the same chapter section.
- `back-pressure` — the hub can still enforce limits while delegating the blocking work.

## Contrasts With
Nothing directly.

# Common Errors

- Setting a "safe" short timeout and assuming the hub is protected — when a downstream service degrades, every call hits the timeout and the cumulative load explodes.
- Adding helper processes reflexively for work that is not concurrent, adding needless complexity.

# Common Confusions

- The async-with-token fix is not free — it "can quickly devolve into callback hell," though it uses fewer resources than spawning many processes.
- The problem is not the blocking operation itself but its location *inside a constantly-fed hub*.

# Source Reference

Chapter 3: Planning for Overload, Section "Locks and Blocking Operations". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Locks and Blocking Operations."
- Confidence rationale: high — described with a concrete production example and three fixes.
- Uncertainties: none.
- Cross-reference status: Verified
