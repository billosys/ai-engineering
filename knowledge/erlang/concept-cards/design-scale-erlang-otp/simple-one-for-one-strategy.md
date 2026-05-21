---
# === CORE IDENTIFICATION ===
concept: Simple One for One Strategy
slug: simple-one-for-one-strategy

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "Simple one for one"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "simple_one_for_one"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-strategy
  - dynamic-children
extends:
  - restart-strategy
related:
  - child-specification
contrasts_with:
  - one-for-one-strategy
  - one-for-all-strategy
  - rest-for-one-strategy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the one_for_one and one_for_all restart strategies?"
  - "How do I write a supervisor and define its child specifications?"
---

# Quick Definition

`simple_one_for_one` is the supervisor restart strategy for a supervisor whose children are all started from a single shared child specification and added dynamically at runtime. It scales better than other strategies for large numbers of identical dynamic children.

# Core Definition

The `simple_one_for_one` restart strategy is used when there is only one child specification shared by all the processes under a single supervisor (Cesarini & Vinoski, p. 187). It is used for children of the same type added dynamically at runtime, not at startup (p. 180). Children are started with `supervisor:start_child(SupRef, StartArgs)`, which appends `StartArgs` to the child specification's argument list and calls `apply(Module, Function, ChildSpecArgs ++ StartArgs)`. Children are referenced by pid (not by name), are deleted automatically when terminated, and the supervisor stores child specifications in a `dict` key-value dictionary rather than a list, so it scales better with many dynamic children (pp. 187-188).

# Prerequisites

- **Restart strategy** — `simple_one_for_one` is one of the four restart strategy values.
- **Dynamic children** — `simple_one_for_one` exists specifically to manage children added dynamically at runtime.

# Key Properties

1. All children share a single child specification supplied in `init/1`.
2. Children are added dynamically via `supervisor:start_child(SupRef, StartArgs)`; `StartArgs` is appended to the spec's arguments.
3. Children are referenced by pid, not by name/id.
4. A terminated child is deleted from the specification automatically — only `terminate_child/2` works; `restart_child/1` and `delete_child/1` do not.
5. On shutdown, children are terminated in no specific order, often concurrently.
6. Child specifications are stored in a `dict`, so it scales better with large numbers of dynamic children than list-based supervisors.

# Construction / Recognition

## To Construct/Create:
1. In `init/1`, return one child specification (the shared template) and `strategy => simple_one_for_one`.
2. Add children at runtime with `supervisor:start_child(?MODULE, StartArgs)`.
3. Terminate children with `supervisor:terminate_child/2`.

## To Identify/Recognize:
1. The supervisor specification's strategy is `simple_one_for_one`.
2. `init/1` returns exactly one child specification, used as a template for all children.

# Context & Application

- **Typical contexts**: Supervisors managing one process per concurrent request or per connected device.
- **Common applications**: A supervisor for phone-controller FSMs added and removed as devices attach.
- **Historical/stylistic notes**: The book notes `simple_one_for_one` scales better than other supervisor types, but still has limits if children start and terminate at very high frequency (p. 188; "Scalability and Short-Lived Processes").

# Examples

**Example 1** (pp. 187-188): `simple_phone_sup` — `init/1` returns `{ok, {{simple_one_for_one, 10, 3600}, [{ms, {phone_fsm, start_link, []}, transient, 2000, worker, [phone_fsm]}]}}`, and `attach_phone/1` calls `supervisor:start_child(?MODULE, [Ms])`.

## Worked Example

`simple_phone_sup` using `simple_one_for_one` (pp. 187-188):

```erlang
init([]) ->
    hlr:new(),
    {ok, {{simple_one_for_one, 10, 3600},
          [{ms, {phone_fsm, start_link, []},
            transient, 2000, worker, [phone_fsm]}]}}.

attach_phone(Ms) ->
    case hlr:lookup_id(Ms) of
        {ok, _Pid}   -> {error, attached};
        _NotAttached -> supervisor:start_child(?MODULE, [Ms])
    end.
```

`start_child(?MODULE, [Ms])` appends `[Ms]` to the spec's empty argument list, calling `phone_fsm:start_link(Ms)`.

# Relationships

## Builds Upon
- **Restart strategy** — `simple_one_for_one` is one specific restart strategy.

## Enables
- *(none)*

## Related
- **Child specification** — A `simple_one_for_one` supervisor uses exactly one, as a template.

## Contrasts With
- **One for one strategy** — Handles heterogeneous static children; `simple_one_for_one` handles homogeneous dynamic ones.
- **One for all strategy** — Coordinates restarts of a fixed interdependent set; `simple_one_for_one` children are independent.
- **Rest for one strategy** — Restarts an ordered suffix of static children; `simple_one_for_one` children are unordered and dynamic.

# Common Errors

- **Error**: Calling `restart_child/1` or `delete_child/1` on a `simple_one_for_one` supervisor.
  **Correction**: These are not allowed; only `terminate_child/2` works, and termination also removes the child.

- **Error**: Referencing a `simple_one_for_one` child by name/id.
  **Correction**: Reference such children by pid; they have no per-child id.

# Common Confusions

- **Confusion**: Thinking `simple_one_for_one` is just `one_for_one` with a shorter name.
  **Clarification**: It uses a single shared spec, dynamic children referenced by pid, automatic deletion on termination, and `dict`-based storage for scalability — all distinct from `one_for_one`.

# Source Reference

Chapter 7: Supervisors, "Simple one for one" and "Scalability and Short-Lived Processes," pages 180, 187-188, 196-197.

# Verification Notes

- Definition source: Direct adaptation from pp. 187-188.
- Confidence rationale: HIGH — explicitly defined with a full rewritten code example and detailed contrasts.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
