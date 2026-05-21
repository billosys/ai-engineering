---
concept: Named Process
slug: named-process
category: processes-concurrency
subcategory: process-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Processes"
chapter_number: 12
pdf_page: null
section: "Naming Processes"
extraction_confidence: high
aliases:
  - "registered process"
  - "process registration"
  - "register/2"
prerequisites:
  - process
  - message-passing
extends: []
related:
  - keeping-processes-alive
contrasts_with: []
answers_questions:
  - "How do I give a process a name?"
  - "Why use a named process instead of passing a pid around?"
---

# Named Process

## Quick Definition

A named process is a process registered under an atom so that other processes can address it by that stable name instead of an unpredictable pid. Registration is done with `erlang:register/2`.

## Core Definition

When a process can be restarted, its pid changes, so callers cannot rely on it. "One of the solutions Erlang provides is to give names to processes. The act of giving a name to a process allows you to replace the unpredictable pid with an atom. This atom can then be used exactly as a pid when sending messages." Registration uses `erlang:register(Name, Pid)`; a process automatically loses its name when it dies, and `unregister/1` removes it manually. `registered/0` lists registered names, and `whereis/1` returns the pid for a name. The chapter warns that referring to a registered process introduces *shared state* and a possible *race condition* if you assume the name maps to the same pid across calls — best fixed by tagging messages with `make_ref()`. Because atoms are limited, only important, VM-unique, long-lived services should be named (Hébert, ch. 12, "Naming Processes").

## Prerequisites

- **Process** — A name is attached to a process
- **Message passing** — A registered name is used as a send target like a pid

## Key Properties

1. Registration: `erlang:register(Name, Pid)` maps an atom to a process
2. A registered name can be used directly as a send target: `name ! Message`
3. A process automatically loses its name when it dies; `unregister/1` removes it manually
4. `registered/0` lists names; `whereis/1` resolves a name to its current pid
5. Referring to a named process is shared state and can cause race conditions across restarts
6. Tagging messages with `make_ref()` makes replies match the right request despite restarts
7. Atoms are a limited resource — name only important, unique, long-lived processes; never create dynamic names

## Construction / Recognition

## To Name a Process

1. Spawn the process and capture its pid
2. Register it: `register(critic, Pid)`
3. Send messages using the name: `critic ! {self(), Ref, Request}`
4. Resolve to a pid when needed: `whereis(critic)`
5. Tag request/reply messages with `make_ref()` to avoid race conditions after restarts

## Examples

> **Registering the critic** (ch. 12): `register(critic, Pid)` lets `judge2/2` send `critic ! {self(), {Band, Album}}` without a pid.
>
> **Race condition** (ch. 12): if the critic dies and restarts between `critic ! Message` and `whereis(critic)`, code may match the wrong pid — fixed by using `make_ref()` to tag messages.
>
> **Killed and instantly back** (ch. 12): `exit(whereis(critic), kill)` followed by `judge2(...)` still works because the restarter re-registers a new critic under the same name.

## Relationships

## Related

- **Keeping processes alive** — Named processes pair with restarters so callers reach the latest instance

## Common Errors

- **Error**: Assuming a registered name maps to the same pid between two calls
  **Correction**: A restart changes the pid; tag messages with references rather than trusting `whereis/1` continuity
- **Error**: Creating dynamic atoms to name many transient processes
  **Correction**: Atoms are limited; name only unique long-lived services, and represent groups differently

## Common Confusions

- **Confusion**: Thinking a named process is free of concurrency hazards
  **Clarification**: A registered name is shared state visible to many processes and can produce race conditions

## Source Reference

Chapter 12, "Errors and Processes," section "Naming Processes" (including the "Name What's Worth Naming" sidebar).

## Verification Notes

- Definition, register/whereis, race condition warning: directly from ch. 12
- Confidence: HIGH — explicitly defined with examples
