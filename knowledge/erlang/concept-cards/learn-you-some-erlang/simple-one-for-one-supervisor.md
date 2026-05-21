---
concept: simple_one_for_one Supervisor
slug: simple-one-for-one-supervisor
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Using a simple_one_for_one Supervisor"
extraction_confidence: high
aliases:
  - "simple_one_for_one"
  - simple supervisor
prerequisites:
  - supervisor
  - supervisor-restart-strategy
extends:
  - supervisor-restart-strategy
related:
  - dynamic-supervision
  - child-specification
contrasts_with: []
answers_questions:
  - "What is a supervisor?"
  - "How do I write a supervisor?"
---

# simple_one_for_one Supervisor

## Quick Definition

A `simple_one_for_one` supervisor manages one kind of child only and is built to add children dynamically on demand. It holds a single child specification and stores its children in a dictionary.

## Core Definition

"This type of supervisor takes only one kind of child, and it's used when you want to dynamically add children to the supervisor, rather than having them started statically. ... a `simple_one_for_one` supervisor just sits around, and it knows it can produce one kind of child only. Whenever you want a new child, you ask for it and you get it" (Ch. 17, "simple_one_for_one").

## Prerequisites

- **Supervisor** — `simple_one_for_one` is a kind of supervisor.
- **Supervisor restart strategy** — It is one of the four restart strategies.

## Key Properties

1. Holds a *single* child specification used for all children.
2. Children are stored in a dictionary, making lookups fast for large numbers of children.
3. You never delete a child spec or store child specs yourself.
4. The `{M, F, A}` argument list is *not* the whole argument list — `supervisor:start_child(Sup, Args)` calls `erlang:apply(M, F, A ++ Args)`.
5. `supervisor:start_child/2` therefore changes meaning: its second argument is extra args, not a child spec.
6. Differs from `one_for_one`, which keeps an ordered list of all started children.

## Construction / Recognition

## To Use a simple_one_for_one Supervisor

1. Return `{ok, {{simple_one_for_one, MaxR, MaxT}, [SingleChildSpec]}}` from `init/1`.
2. The child spec's `{M, F, A}` holds only the *common* leading arguments.
3. Add children with `supervisor:start_child(Sup, ExtraArgs)`.
4. The supervisor appends `ExtraArgs` to `A` when starting each child.

## Context & Application

`simple_one_for_one` is the right choice "when you need quick access to many children" — think of a web server spawning a process per connection. The book adds a `jamband` clause to `band_supervisor` returning `{simple_one_for_one, 3, 60}` with a single `jam_musician` spec; `supervisor:start_child(band_supervisor, [drum, good])` then starts a new musician.

**Version note:** The book notes that before Erlang R14B03, `simple_one_for_one` children did not respect the `Shutdown` timeout and `supervisor:terminate_child/2` by pid was not supported. Modern OTP supports both.

## Examples

**Example 1** (Ch. 17): `init(jamband) -> {ok, {{simple_one_for_one, 3, 60}, [{jam_musician, {musicians, start_link, []}, temporary, 1000, worker, [musicians]}]}};`.

**Example 2** (Ch. 17): `supervisor:start_child(band_supervisor, [djembe, good])` — `[djembe, good]` is appended to the empty `A` list, calling `musicians:start_link(djembe, good)`.

## Relationships

## Builds Upon

- **Supervisor restart strategy** — It is the fourth restart strategy.

## Related

- **dynamic-supervision** — `simple_one_for_one` is the preferred tool for dynamic supervision.
- **child-specification** — It uses exactly one child spec for all children.

## Common Errors

- **Error**: Passing a full child spec to `supervisor:start_child/2` under `simple_one_for_one`.
  **Correction**: Pass only the *extra* arguments; the child spec is fixed in `init/1`.
- **Error**: Registering each dynamically started child under the same fixed name.
  **Correction**: This causes `{already_started, Pid}`; use unique names or anonymous children.

## Common Confusions

- **Confusion**: Thinking `simple_one_for_one` is "simple" / a basic version of `one_for_one`.
  **Clarification**: Despite the name, it is a distinct strategy specialised for many dynamic children of one type — internally a dictionary, not a list.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", sections "simple_one_for_one" (under Restart Strategies) and "Using a simple_one_for_one Supervisor."

## Verification Notes

- Definition: Direct quotes from the source.
- Key Properties: Adapted from both `simple_one_for_one` sections, including the `apply(M,F,A++Args)` detail.
- Confidence: HIGH — explicitly defined with code.
