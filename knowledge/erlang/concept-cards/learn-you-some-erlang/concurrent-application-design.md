---
concept: Concurrent Application Design
slug: concurrent-application-design
category: processes-concurrency
subcategory: application-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Designing a Concurrent Application"
chapter_number: 13
pdf_page: null
section: "Understanding the Problem"
extraction_confidence: high
aliases:
  - "designing a concurrent application"
  - "process architecture"
prerequisites:
  - process
  - message-passing
  - process-monitor
extends: []
related:
  - message-protocol
  - keeping-processes-alive
contrasts_with: []
answers_questions:
  - "How do I design a concurrent application in Erlang?"
  - "How do I decide what processes my application needs?"
---

# Concurrent Application Design

## Quick Definition

Concurrent application design is the method of building an Erlang application by first writing a specification, then deciding which processes exist, then defining the messages between them — before writing code.

## Core Definition

Chapter 13 builds an event-reminder application and distills a design method. The first step is "to know what the hell we're doing" — write a specification and stick to it ("developing software from a specification is easy if both are frozen"). Then decide the process architecture: the reminder app has a client process, an event server, and one event process per pending reminder. Each process is given explicit tasks. Drawing every process and the arrows between them yields "a high-level protocol, or at least its skeleton." Modules are implemented from least-dependent to most-dependent (event module first, then event server, then clients). The chapter shows that with message passing "we could have a bunch of concurrent processes without thinking too hard about it... There's no need to synchronize them, no locks, and no real main loop" (Hébert, ch. 13, "Understanding the Problem," closing remarks).

## Prerequisites

- **Process** — The unit of the architecture
- **Message passing** — Processes coordinate only through messages
- **Process monitor** — The client monitors the server rather than linking, for extensibility

## Key Properties

1. Start with a frozen specification of what the software does
2. Decide the process architecture — which processes exist and their responsibilities
3. Choose one process per concurrent activity (the app uses one process per pending event)
4. Define the message protocol by drawing processes and the arrows between them
5. Implement modules in dependency order — least dependent first
6. Message passing removes the need for locks, synchronization, or a global main loop
7. Choose links vs. monitors deliberately: the client monitors the server (no obligatory codependence)
8. Per-process-per-event is fine for a single user; at scale, prefer `timer:send_after` over many processes

## Construction / Recognition

## To Design a Concurrent Application

1. Write and freeze a specification of features
2. Sketch the process hierarchy and assign each process its tasks
3. Draw all messages between processes to define the protocol skeleton
4. Lay down the standard Erlang directory structure (`ebin/`, `include/`, `priv/`, `src/`)
5. Implement modules from least dependent to most dependent
6. Decide links vs. monitors per relationship based on whether processes must die together

## Examples

> **Process architecture** (ch. 13): client, event server, and x/y/z event processes — each with an explicit task list (subscribe, add/cancel events, fire notifications).
>
> **Monitor over link** (ch. 13): the client monitors the server because "there is no obvious dependency" — other clients should not crash when the server dies.
>
> **No locks needed** (ch. 13): "supervisors, clients, servers, processes used as timers... There's no need to synchronize them, no locks, and no real main loop."

## Relationships

## Related

- **Message protocol** — The defined-messages step of the design method
- **Keeping processes alive** — The app's `sup` restarter supervises the event server

## Common Errors

- **Error**: Writing process code before defining the protocol
  **Correction**: Draw processes and messages first; the protocol skeleton guides implementation
- **Error**: Using one process per entity at scale without thought
  **Correction**: One process per event is fine for one user; at scale use `timer:send_after/2-3` instead

## Common Confusions

- **Confusion**: Thinking concurrent design requires locks and synchronization
  **Clarification**: Message passing compartmentalizes the app; no locks or shared main loop are needed

## Source Reference

Chapter 13, "Designing a Concurrent Application," sections "Understanding the Problem," "Lay Them Foundations," and the closing discussion.

## Verification Notes

- Design method and architecture: directly from ch. 13
- Confidence: HIGH — the chapter is an explicit worked design walkthrough
