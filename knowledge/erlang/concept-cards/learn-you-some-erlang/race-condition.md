---
concept: Race Condition
slug: race-condition
category: processes-concurrency
subcategory: concurrency-hazards
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
  - "race condition"
  - "shared state"
prerequisites:
  - named-process
  - message-passing
extends: []
related:
  - named-process
contrasts_with:
  - deadlock
answers_questions:
  - "What is a race condition?"
  - "Is Erlang code free of race conditions?"
---

# Race Condition

## Quick Definition

A race condition is a software error where a value can be accessed and modified by different processes at virtually the same time, producing inconsistent, timing-dependent results.

## Core Definition

While abstracting the `judge2/2` function, the chapter shows that `Pid = whereis(critic)` can return a stale or wrong pid if the critic dies and restarts between calls. The underlying problem is *shared state*: "the value of `critic` can be seen from multiple processes... can be accessed and modified by different processes at virtually the same time, resulting in inconsistent information and software errors. The common term for such things is a *race condition*." Race conditions "are particularly dangerous because they depend on the timing of events," which depends on unpredictable factors like processor load. Although message passing makes Erlang "usually free of race conditions" by ordering events and restricting shared state, "you should never assume your code is entirely free of race conditions." The fix in the chapter is to tag messages with `make_ref()` so each reply matches the right request (Hébert, ch. 12, "Naming Processes").

## Prerequisites

- **Named process** — Named processes are a common source of shared state in this chapter
- **Message passing** — Reference tagging fixes the race in request/reply messaging

## Key Properties

1. A race condition is a timing-dependent inconsistency from concurrent access to shared state
2. It depends on unpredictable factors — processor load, process placement, data
3. Named/registered processes introduce shared state (the name→pid mapping) and thus possible races
4. Message passing reduces races by ordering events and limiting shared state — but does not eliminate them
5. Other sources include concurrent file modification and concurrent database updates
6. Tagging messages with `make_ref()` makes replies match the correct request despite restarts

## Construction / Recognition

## To Avoid Race Conditions

1. Minimize shared state — prefer message passing over registered-name assumptions
2. Do not assume a registered name maps to the same pid across two calls
3. Tag request/reply messages with `make_ref()` so replies are unambiguously matched
4. Be cautious with concurrent file access and concurrent database updates
5. Never assume code is automatically race-free

## Examples

> **Stale whereis** (ch. 12): between `critic ! Message` and `Pid = whereis(critic)`, the critic may die and restart, so `whereis` "picks up wrong pid" and the reply "never matches."
>
> **Reference fix** (ch. 12): `judge2/2` uses `Ref = make_ref()` and matches `{Ref, Criticism}` so the reply is tied to this request.

## Relationships

## Related

- **Named process** — Registered names create the shared state that enables this race

## Contrasts With

- **Deadlock** — A deadlock is permanent blocking; a race condition is an intermittent timing-dependent error

## Common Errors

- **Error**: Assuming a registered name's pid is stable between two operations
  **Correction**: Tag messages with references; do not rely on `whereis/1` continuity

## Common Confusions

- **Confusion**: Believing Erlang programs are immune to race conditions
  **Clarification**: Message passing reduces them, but shared state (named processes, files, databases) can still race

## Source Reference

Chapter 12, "Errors and Processes," section "Naming Processes" (and the "Don't Drink Too Much Kool-Aid" sidebar).

## Verification Notes

- Definition, shared-state cause, reference fix: directly from ch. 12
- Confidence: HIGH — explicitly defined
