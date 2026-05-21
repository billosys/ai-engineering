---
concept: Event Process as Timer
slug: event-process-timer
category: processes-concurrency
subcategory: application-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Designing a Concurrent Application"
chapter_number: 13
pdf_page: null
section: "An Event Module"
extraction_confidence: high
aliases:
  - "process as timer"
  - "event process"
prerequisites:
  - process
  - receive-timeout
  - stateful-process
extends: []
related:
  - concurrent-application-design
contrasts_with: []
answers_questions:
  - "How can a process act as a timer?"
  - "How do I handle Erlang's ~49-day timeout limit?"
---

# Event Process as Timer

## Quick Definition

An event process as timer is a process whose loop is just a `receive` with an `after` clause: it waits a duration, then fires a notification — and can be cancelled by a message in the meantime.

## Core Definition

In the reminder application, "the x, y, and z processes represent a notification waiting to fire — they're basically just timers linked to the event server." Each event process runs a `loop/1` that does `receive {Server, Ref, cancel} -> ... after Delay -> ...`: the `after` part fires the `{done, Name}` notification when the time elapses, while the `cancel` clause lets the server stop it early. The chapter hits a real limitation — "Erlang's timeout value is limited to about 50 days in milliseconds" — and works around it with a `normalize/1` function that splits a long delay into a list of 49-day chunks; `loop/1` then consumes the list chunk by chunk. The chapter notes that at scale "using one process per event... would likely be overkill," and `timer:send_after/2-3` is a lighter alternative (Hébert, ch. 13, "An Event Module").

## Prerequisites

- **Process** — The timer is a dedicated process
- **Receive timeout** — The `after` clause is what makes the process fire after a delay
- **Stateful process** — The loop carries the remaining time and event name as state

## Key Properties

1. A timer process loops on a `receive` with an `after Delay` clause
2. The `after` clause fires the notification when the delay elapses
3. A `cancel` message clause lets the process be stopped before it fires
4. Erlang's `receive` timeout is limited to about 49–50 days in milliseconds
5. The work-around: split a long delay into a list of ≤49-day chunks (`normalize/1`)
6. The loop consumes the chunk list, recursing until the list is empty, then notifies
7. One process per event is fine at small scale; `timer:send_after/2-3` is lighter at scale

## Construction / Recognition

## To Build a Timer Process

1. Write a `loop(State)` with `receive {Server, Ref, cancel} -> reply after T*1000 -> fire end`
2. Carry the server pid, event name, and remaining time in the loop state (a record)
3. Normalize a long delay into ≤49-day chunks before starting the loop
4. In the `after` branch, fire the notification if the chunk list is empty, else recurse with the rest
5. Provide `start`/`start_link` and a `cancel/1` interface function

## Examples

> **Loop skeleton** (ch. 13): `loop(S = #state{server=Server, to_go=[T|Next]}) -> receive {Server, Ref, cancel} -> Server ! {Ref, ok} after T*1000 -> ... end.`
>
> **Timeout-limit work-around** (ch. 13): `normalize(N) -> Limit = 49*24*60*60, [N rem Limit | lists:duplicate(N div Limit, Limit)].`

## Relationships

## Related

- **Concurrent application design** — Timer processes are part of the reminder app's architecture

## Common Errors

- **Error**: Passing a multi-month delay straight into a `receive` timeout
  **Correction**: Erlang caps timeouts near 49 days; split the delay with a `normalize`-style function
- **Error**: Spawning one timer process per event in a large-scale system
  **Correction**: Use `timer:send_after/2-3` to avoid spawning thousands of processes

## Common Confusions

- **Confusion**: Thinking a `receive` timeout can be arbitrarily long
  **Clarification**: It is limited to about 49–50 days in milliseconds; longer waits must be chunked

## Source Reference

Chapter 13, "Designing a Concurrent Application," section "An Event Module," subsection "Events and Loops."

## Verification Notes

- Loop pattern, 49-day limit, normalize work-around: directly from ch. 13
- Confidence: HIGH — explicitly demonstrated with code
