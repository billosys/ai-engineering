---
concept: Dynamic Supervision
slug: dynamic-supervision
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Dynamic Supervision"
extraction_confidence: high
aliases:
  - dynamic children
  - runtime child management
prerequisites:
  - supervisor
  - simple-one-for-one-supervisor
extends: []
related:
  - simple-one-for-one-supervisor
  - child-specification
contrasts_with: []
answers_questions:
  - "How do I write a supervisor?"
  - "What is a supervisor?"
---

# Dynamic Supervision

## Quick Definition

Dynamic supervision is the runtime management of supervised children — starting, terminating, restarting, and deleting them — rather than specifying all children statically in source code.

## Core Definition

"So far, the kind of supervision we've covered has been static. We specified all the children we would have directly in the source code. ... On the other hand, you may have supervisors who supervise undetermined workers. They're usually there on a per-demand basis" (Ch. 17, "Dynamic Supervision"). The book gives the example of a web server spawning a process per connection.

## Prerequisites

- **Supervisor** — Dynamic supervision uses the supervisor API at runtime.
- **simple_one_for_one supervisor** — The preferred strategy for many dynamic children.

## Key Properties

1. Standard supervisors (`one_for_one`, `rest_for_one`, `one_for_all`) can be used dynamically because each added child spec is appended to the supervisor's internal list.
2. The runtime API: `start_child/2`, `terminate_child/2`, `restart_child/2`, `delete_child/2`, `check_childspecs/1`, `count_children/1`, `which_children/1`.
3. `terminate_child` leaves the child spec in the supervisor; `delete_child` removes the spec.
4. Standard supervisors store children in a list — slow when there are many children.
5. `simple_one_for_one` stores children in a dictionary — fast for many children.

## Construction / Recognition

## To Manage Children Dynamically

1. For few children with infrequent manipulation → use a standard supervisor and `supervisor:start_child/2` with full specs.
2. For many children or high-speed needs → use `simple_one_for_one` and `supervisor:start_child/2` with extra args.
3. Terminate a child with `terminate_child/2`; remove its spec with `delete_child/2`.
4. Inspect with `which_children/1` and `count_children/1`.

## Context & Application

The book's recommendation: "use standard supervisors dynamically only when you know with certainty that you will have few children to supervise and/or they won't need to be manipulated frequently. For other kinds of dynamic supervision, use `simple_one_for_one` where possible."

## Examples

**Example 1** (Ch. 17): `supervisor:which_children(band_supervisor)` lists all four musicians; `supervisor:terminate_child(band_supervisor, drum)` and `supervisor:restart_child(band_supervisor, singer)` manage them at runtime.

**Example 2** (Ch. 17): `supervisor:count_children(band_supervisor)` returns `[{specs,4},{active,3},{supervisors,0},{workers,4}]`.

**Example 3** (Ch. 17): After `delete_child(band_supervisor, drum)`, `restart_child(band_supervisor, drum)` returns `{error, not_found}` — the spec is gone.

## Relationships

## Builds Upon

- **Supervisor** — Dynamic supervision is the supervisor's runtime API.

## Related

- **simple-one-for-one-supervisor** — The strategy designed for dynamic children at scale.
- **child-specification** — `start_child/2` adds a spec (standard supervisors) or extra args (`simple_one_for_one`).

## Common Errors

- **Error**: Using a standard supervisor for thousands of frequently churning children.
  **Correction**: Use `simple_one_for_one`; its dictionary storage scales where the list does not.

## Common Confusions

- **Confusion**: Thinking `terminate_child/2` removes the child permanently.
  **Clarification**: It stops the child but leaves the spec; the child can be restarted unless you also call `delete_child/2`.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Dynamic Supervision" (subsections "Using Standard Supervisors Dynamically" and "Using a simple_one_for_one Supervisor").

## Verification Notes

- Definition: Direct quote from "Dynamic Supervision."
- Key Properties: API list copied from the source's `variablelist`.
- Confidence: HIGH — explicitly defined with worked shell sessions.
