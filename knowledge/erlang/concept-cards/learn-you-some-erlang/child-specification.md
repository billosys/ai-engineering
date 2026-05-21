---
concept: Child Specification
slug: child-specification
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Child Specifications"
extraction_confidence: high
aliases:
  - "ChildSpec"
  - child spec
prerequisites:
  - supervisor
extends: []
related:
  - supervisor-restart-strategy
  - child-restart-type
  - worker-process
contrasts_with: []
answers_questions:
  - "How do I write a supervisor?"
  - "What is a supervisor?"
---

# Child Specification

## Quick Definition

A child specification is a tuple describing one child a supervisor manages: its id, how to start it, when to restart it, how to shut it down, its type, and its callback modules.

## Core Definition

"`ChildSpec` stands for *child specification*" (Ch. 17, "Child Specifications"). Its abstract form is:

```erlang
{ChildId, StartFunc, Restart, Shutdown, Type, Modules}.
```

The supervisor's `init/1` returns a list of these inside `{ok, {{Strategy, MaxRestart, MaxTime}, [ChildSpec]}}`.

## Prerequisites

- **Supervisor** — Child specifications populate a supervisor's `init/1` return.

## Key Properties

1. **`ChildId`** — Any term naming the child internally; used for debugging and listing children.
2. **`StartFunc`** — An `{M, F, A}` tuple specifying how to start the child; the function must be OTP-compliant and link to its caller.
3. **`Restart`** — `permanent`, `temporary`, or `transient` (see `child-restart-type`).
4. **`Shutdown`** — A timeout in milliseconds, `infinity`, or `brutal_kill`, giving a deadline for orderly termination.
5. **`Type`** — `worker` or `supervisor` (the latter implements `supervisor` or `supervisor_bridge`).
6. **`Modules`** — A one-element list naming the child's callback module, or `dynamic` when the module is not known beforehand (e.g. event handlers).

## Construction / Recognition

## To Write a Child Spec

1. Pick a readable `ChildId` term.
2. Provide the `{M, F, A}` start tuple, using a `start_link` wrapper.
3. Choose `permanent` / `temporary` / `transient`.
4. Set a `Shutdown` deadline (ms, `infinity`, or `brutal_kill`).
5. Set `Type` to `worker` or `supervisor`.
6. List the callback module, or use `dynamic`.

## Context & Application

When a supervisor shuts down a child, it calls `exit(ChildPid, shutdown)`; a worker trapping exits runs its `terminate` function. If the `Shutdown` deadline passes, the process is brutally killed with `exit(Pid, kill)`. `brutal_kill` kills immediately and untrappably. The book warns that mismatched `Shutdown` values in a supervisor chain (e.g. 5 → 2 → 5 → 5) can cause processes to be brutally killed because an ancestor's cutoff is shorter.

Modern OTP also accepts a *map* form of child specification; the book uses the six-tuple form.

## Examples

**Example 1** (Ch. 17): `{fake_id, {fake_mod, start_link, [SomeArg]}, permanent, 5000, worker, [fake_mod]}`.

**Example 2** (Ch. 17): `{other_id, {event_manager_mod, start_link, []}, transient, infinity, worker, dynamic}` — `Modules` is `dynamic` because event-handler identities are unknown.

**Example 3** (Ch. 17): `{singer, {musicians, start_link, [singer, good]}, permanent, 1000, worker, [musicians]}`.

## Relationships

## Builds Upon

- **Supervisor** — Child specs are part of the supervisor's configuration.

## Related

- **supervisor-restart-strategy** — Determines how a child's death affects siblings.
- **child-restart-type** — The `Restart` field's three values.
- **worker-process** — Most child specs describe workers.

## Common Errors

- **Error**: Using a non-linking start function in `StartFunc`.
  **Correction**: Use a `gen_*:start_link` wrapper; the supervisor must be linked to the child.
- **Error**: Setting too-short `Shutdown` deadlines on workers that need to close files or sockets.
  **Correction**: Choose a deadline long enough for the worker's `terminate` to finish, or `infinity` if needed.

## Common Confusions

- **Confusion**: Thinking `Modules` lists all modules the child uses.
  **Clarification**: It is a one-element list naming the *callback* module (for code upgrades), or `dynamic`.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Child Specifications" (subsections `ChildId`, `StartFunc`, `Restart`, `Shutdown`, `Type`, `Modules`).

## Verification Notes

- Definition: Direct quote and the six-tuple form from the source.
- Key Properties: Adapted from each field's subsection.
- Confidence: HIGH — every field explicitly described with examples.
