---
concept: Restart Intensity
slug: restart-intensity
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Restart Limits"
extraction_confidence: high
aliases:
  - restart limit
  - "MaxRestart"
  - "MaxTime"
  - maximum restart frequency
prerequisites:
  - supervisor
  - supervisor-restart-strategy
extends: []
related:
  - child-specification
contrasts_with: []
answers_questions:
  - "What is a supervisor?"
  - "How do supervisors relate to the \"let it crash\" philosophy?"
---

# Restart Intensity

## Quick Definition

Restart intensity is the `MaxRestart`/`MaxTime` limit in a supervisor's flags. If more than `MaxRestart` restarts happen within `MaxTime` seconds, the supervisor gives up, shuts down its children, and terminates itself.

## Core Definition

"The last part of the `RestartStrategy` tuple contains the variables `MaxRestart` and `MaxTime`. The idea is that if more than the `MaxRestart` limit happens within `MaxTime` (in seconds), the supervisor just gives up on your code, shuts it down, and then kills itself, never to return. And that is based on restarts for *all* children of the supervisor, not any one of them individually" (Ch. 17, "Restart Limits").

## Prerequisites

- **Supervisor** — Restart intensity is part of a supervisor's `init/1` flags.
- **Supervisor restart strategy** — `MaxRestart`/`MaxTime` accompany the strategy in the same tuple.

## Key Properties

1. The flags tuple is `{RestartStrategy, MaxRestart, MaxTime}`; `MaxTime` is in seconds.
2. The limit counts restarts across *all* children of the supervisor, not per-child.
3. Exceeding the limit makes the supervisor terminate itself and all its children.
4. A failed supervisor may still be revived by its own (higher) supervisor.
5. The intuition: a supervisor should retry a few times, then give up rather than loop forever (like trying a broken TV remote).

## Construction / Recognition

## To Set Restart Intensity

1. Estimate how often legitimate transient failures occur.
2. Set `MaxRestart` to a count that tolerates those but not a runaway crash loop.
3. Set `MaxTime` to the window (in seconds) over which the count applies.
4. Rely on a parent supervisor to recover if this one gives up.

## Context & Application

The `band_supervisor` uses intensity to express tolerance: the lenient supervisor `{one_for_one, 3, 60}` allows three restarts in 60 seconds and fails on the fourth; the angry one `{rest_for_one, 2, 60}` allows two; the jerk `{one_for_all, 1, 60}` allows only one. When the limit is hit, the manager "is mad and fired the whole band," and the supervisor exits with reason `shutdown`.

## Examples

**Example 1** (Ch. 17): `{one_for_one, 3, 60}` — up to 3 restarts per 60 seconds before giving up.

**Example 2** (Ch. 17): `{one_for_all, 1, 60}` — a single restart in 60 seconds is the limit; the supervisor is very strict.

## Relationships

## Builds Upon

- **Supervisor** — Intensity is part of supervisor configuration.
- **Supervisor restart strategy** — Shares the flags tuple with the strategy.

## Related

- **child-specification** — Children are what get restarted toward the limit.

## Common Errors

- **Error**: Setting `MaxRestart` too high, letting a broken process crash-loop indefinitely.
  **Correction**: Pick a limit that lets the supervisor give up so a parent can take corrective action.

## Common Confusions

- **Confusion**: Thinking the limit is per-child.
  **Clarification**: It counts *all* children's restarts together; a single noisy child can trip the limit for the whole supervisor.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Restart Limits"; intensity values appear in `band_supervisor`'s `init/1`.

## Verification Notes

- Definition: Direct quote from "Restart Limits."
- Key Properties: Adapted from the section and the `band_supervisor` examples.
- Confidence: HIGH — explicitly defined.
