---
concept: Supervisor init Callback
slug: supervisor-init-callback
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Using Supervisors"
extraction_confidence: high
aliases:
  - "supervisor:init/1"
  - "init/1 supervisor callback"
prerequisites:
  - supervisor
  - supervisor-restart-strategy
  - child-specification
extends: []
related:
  - supervisor-restart-strategy
  - child-specification
  - restart-intensity
contrasts_with: []
answers_questions:
  - "How do I write a supervisor?"
  - "What is a supervisor?"
---

# Supervisor init Callback

## Quick Definition

`init/1` is the single callback a supervisor must implement. Its return value packages the restart strategy, restart limits, and the list of child specifications.

## Core Definition

"There is a single callback function to provide: `init/1`. The catch is that its return is quite complex" (Ch. 17, "Using Supervisors"). The general form is:

```erlang
{ok, {{RestartStrategy, MaxRestart, MaxTime}, [ChildSpec]}}.
```

## Prerequisites

- **Supervisor** — `init/1` is the supervisor behaviour's only callback.
- **Supervisor restart strategy** — Part of the `init/1` flags tuple.
- **Child specification** — `init/1` returns a list of these.

## Key Properties

1. It is the *only* callback a supervisor module must implement.
2. It returns `{ok, {SupFlags, ChildSpecs}}`.
3. `SupFlags` is `{RestartStrategy, MaxRestart, MaxTime}`.
4. `ChildSpecs` is a list of child specification tuples.
5. It is called once when `supervisor:start_link/2,3` starts the supervisor.
6. A common idiom is for `init/1` to take a parameter and dispatch to itself with concrete flags.

## Construction / Recognition

## To Write a Supervisor's init/1

1. Choose `RestartStrategy`, `MaxRestart`, `MaxTime`.
2. Build each child specification (`{Id, MFA, Restart, Shutdown, Type, Modules}`).
3. Return `{ok, {{Strategy, MaxR, MaxT}, [ChildSpecs]}}`.

## Context & Application

The `band_supervisor` uses the self-dispatch idiom: `init(lenient) -> init({one_for_one, 3, 60});` and a final `init({RestartStrategy, MaxRestart, MaxTime}) -> {ok, {{...}, [child specs]}}.` This lets one module produce several supervisor "moods" from one `init/1`. The childless top supervisor `ppool_supersup` returns `{ok, {{one_for_one, 6, 3600}, []}}` — an empty child list, with children added dynamically later.

Modern OTP also accepts a *map* return (`#{strategy => ..., intensity => ..., period => ...}`); the book uses the tuple form.

## Examples

**Example 1** (Ch. 17): `init({RestartStrategy, MaxRestart, MaxTime}) -> {ok, {{RestartStrategy, MaxRestart, MaxTime}, [ {singer, {musicians, start_link, [singer, good]}, permanent, 1000, worker, [musicians]}, ... ]}}.`

**Example 2** (Ch. 18): `init([]) -> {ok, {{one_for_one, 6, 3600}, []}}.` — a childless supervisor.

## Relationships

## Builds Upon

- **Supervisor** — `init/1` is its sole callback.

## Related

- **supervisor-restart-strategy** — Part of the `SupFlags` tuple.
- **child-specification** — `init/1` returns a list of these.
- **restart-intensity** — `MaxRestart`/`MaxTime` in the `SupFlags`.

## Common Errors

- **Error**: Returning the child-spec list at the wrong nesting level.
  **Correction**: The shape is `{ok, {SupFlags, ChildSpecs}}` — two nested tuples; mismatched braces are a common mistake.

## Common Confusions

- **Confusion**: Thinking a supervisor needs `handle_call`/`handle_cast` like a `gen_server`.
  **Clarification**: A supervisor has *only* `init/1`; all other behaviour is generic OTP code.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Using Supervisors"; examples in "Band Supervisor" and Chapter 18's `ppool_supersup`.

## Verification Notes

- Definition: Direct quote from "Using Supervisors."
- Key Properties: Synthesised from the return-value discussion and examples.
- Confidence: HIGH — explicitly defined.
