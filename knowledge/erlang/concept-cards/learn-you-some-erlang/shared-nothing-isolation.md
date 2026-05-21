---
concept: Shared-Nothing Isolation
slug: shared-nothing-isolation
category: fault-tolerance
subcategory: isolation
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Scalability"
extraction_confidence: high
aliases:
  - "shared-nothing"
  - "process isolation"
  - "no shared memory"
prerequisites:
  - process
extends: []
related:
  - message-passing
  - let-it-crash
contrasts_with: []
answers_questions:
  - "Why do Erlang processes not share memory?"
  - "How does process isolation support fault tolerance?"
---

# Shared-Nothing Isolation

## Quick Definition

Shared-nothing isolation is Erlang's design choice that processes share no memory; all data passed between them is copied. This isolation prevents one process's crash from corrupting another's state.

## Core Definition

Because telephony applications "needed a lot of reliability, it was decided that the cleanest approach was to forbid processes from sharing memory." Shared memory "could leave things in an inconsistent state after some crashes... and had some complications. Instead, processes should communicate by sending messages where all the data is copied. This might end up being slower but safer." The chapter ties this to crash safety: making all crashes equivalent to clean shutdowns is done "through practices such as *shared-nothing* (all memory is separated for subparts of the system) and single assignment (which can further isolate a process's memory), avoiding locks." Isolation also makes distribution nearly transparent — processes "work the same way whether they're local or on a different computer" (Hébert, ch. 10, "Scalability," "Fault Tolerance").

## Prerequisites

- **Process** — Isolation is a property of processes

## Key Properties

1. Processes share no memory — each has fully separate state
2. Data passed between processes is copied, not shared
3. Copying is slower than sharing but safer — no inconsistent shared state after a crash
4. Single assignment further isolates a process's memory
5. Avoiding locks prevents one crash from leaving data locked or inconsistent for others
6. Isolation makes a crash containable — it cannot corrupt other processes
7. Isolation makes local and remote processes behave the same, easing distribution

## Construction / Recognition

## To Rely on Shared-Nothing Isolation

1. Communicate between processes only by message passing — never by shared mutable state
2. Accept that messages are copied; design data sizes accordingly
3. Treat each process's state as private and self-contained
4. Trust that a crash in one process cannot corrupt another's data

## Examples

> **Design decision** (ch. 10): "it was decided that the cleanest approach was to forbid processes from sharing memory... processes should communicate by sending messages where all the data is copied."
>
> **Crash safety** (ch. 10): shared-nothing and single assignment help make "all crashes the same as clean shutdowns."

## Relationships

## Builds Upon

- **Process** — Each process is the unit of isolation

## Related

- **Message passing** — The copy-based communication that replaces shared memory
- **Let it crash** — Isolation is what makes crashing a process safe

## Common Errors

- **Error**: Trying to share large mutable state between processes for speed
  **Correction**: Erlang has no shared memory; pass copied messages or rethink the design

## Common Confusions

- **Confusion**: Thinking message copying is purely a performance cost
  **Clarification**: Copying buys isolation — a crash cannot leave another process's memory inconsistent

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "Concurrency Concepts," subsections "Scalability" and "Fault Tolerance."

## Verification Notes

- Shared-nothing rationale: directly from ch. 10
- Confidence: HIGH — explicitly discussed
