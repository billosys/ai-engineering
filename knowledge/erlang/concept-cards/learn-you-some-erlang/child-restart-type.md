---
concept: Child Restart Type
slug: child-restart-type
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Restart"
extraction_confidence: high
aliases:
  - "permanent"
  - "temporary"
  - "transient"
  - restart option
prerequisites:
  - child-specification
extends: []
related:
  - supervisor-restart-strategy
contrasts_with: []
answers_questions:
  - "What distinguishes temporary, transient, and permanent child restart?"
  - "How do I write a supervisor?"
---

# Child Restart Type

## Quick Definition

The restart type — `permanent`, `temporary`, or `transient` — is the `Restart` field of a child specification, telling the supervisor whether to restart that child when it dies.

## Core Definition

"`Restart` tells the supervisor how to react when that particular child dies. This can take one of three values: `permanent`, `temporary`, `transient`" (Ch. 17, "Restart").

- **`permanent`** — "should always be restarted, no matter what."
- **`temporary`** — "a process that should never be restarted."
- **`transient`** — "meant to run until they terminate normally, and then they won't be restarted. However, if they die of abnormal causes ... they will be restarted."

## Prerequisites

- **Child specification** — The restart type is the `Restart` field of a child spec.

## Key Properties

1. `permanent` — always restarted; for vital, long-living processes/services.
2. `temporary` — never restarted; for short-lived workers expected to fail.
3. `transient` — restarted only if it exits abnormally (any reason other than `normal`, `shutdown`, or `{shutdown, Reason}`).
4. All three types can be mixed under one supervisor.
5. The restart type interacts with the restart strategy: a `one_for_all` restart is not triggered by a `temporary` child dying, but a `temporary` child can still be restarted if a `permanent` sibling dies first.

## Construction / Recognition

## To Choose a Restart Type

1. Vital service that must always run → `permanent`.
2. Short-lived, disposable, expected-to-fail worker → `temporary`.
3. Worker that must succeed at a task but is not needed afterward → `transient`.

## Context & Application

In the `band_supervisor`, the singer is `permanent` ("the band could never work without a singer"), the bass player is `temporary` ("the band could still play fine without a bass player"), and the drummer and keytar player are `transient` ("they can leave on their own, but they might still need to be replaced in case of errors").

## Examples

**Example 1** (Ch. 17): `{singer, {musicians, start_link, [singer, good]}, permanent, 1000, worker, [musicians]}` — restarted whatever happens.

**Example 2** (Ch. 17): `{bass, {musicians, start_link, [bass, good]}, temporary, 1000, worker, [musicians]}` — never restarted.

**Example 3** (Ch. 17): `{drum, {musicians, start_link, [drum, bad]}, transient, 1000, worker, [musicians]}` — restarted only on an abnormal crash.

## Relationships

## Builds Upon

- **Child specification** — The restart type is one of the six child-spec fields.

## Related

- **supervisor-restart-strategy** — Restart type and strategy together determine restart behaviour.

## Common Errors

- **Error**: Marking a worker that must succeed `temporary`.
  **Correction**: Use `transient` so an abnormal crash retries the work, but a normal completion does not restart it.

## Common Confusions

- **Confusion**: Thinking `transient` means "restarted on any termination."
  **Clarification**: `transient` restarts *only* on abnormal exit; a `normal`/`shutdown` exit leaves it stopped.
- **Confusion**: Thinking `temporary` children are unsupervised.
  **Clarification**: They are still supervised — the supervisor tracks them and can shut them down cleanly — they are just never restarted.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Child Specifications," subsection "Restart."

## Verification Notes

- Definition: Direct quotes from the "Restart" subsection.
- Key Properties: Adapted from the subsection and the strategy-interaction note.
- Confidence: HIGH — all three types explicitly defined; directly answers diagnostic CQ7.
