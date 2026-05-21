---
# === CORE IDENTIFICATION ===
concept: Dynamic Children
slug: dynamic-children

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
section: "Dynamic Children"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "dynamic child processes"
  - "runtime children"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - child-specification
extends: []
related:
  - simple-one-for-one-strategy
  - one-for-one-strategy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a supervisor and define its child specifications?"
  - "What is a supervisor?"
---

# Quick Definition

Dynamic children are supervised processes started after the supervisor itself is running, rather than statically at startup, using `supervisor:start_child/2` at runtime.

# Core Definition

Beyond static children started along with the supervisor, another approach is viable: dynamically creating children at runtime (Cesarini & Vinoski, p. 184). A supervisor can start with an empty (or computed) child specification list and then have children added later — for instance, when a mobile device attaches itself to the network after the supervisor has started. Dynamic children are created with `supervisor:start_child(Name, ChildSpecOrArgs)`; they can be stopped with `supervisor:terminate_child/2`, restarted with `supervisor:restart_child/2`, and removed with `supervisor:delete_child/2` (pp. 184-186, 189). For homogeneous high-volume dynamic children, the `simple_one_for_one` strategy is preferred.

# Prerequisites

- **Supervisor** — Dynamic children are added to a running supervisor.
- **Child specification** — Each dynamic child is described by (or shares) a child specification.

# Key Properties

1. Started after the supervisor is running, not at startup.
2. Added via `supervisor:start_child/2`.
3. With non-`simple_one_for_one` strategies, a terminated child's spec remains (pid set to `undefined`) until `delete_child/2` removes it.
4. Children are referenced by their unique `id`/name (except under `simple_one_for_one`, which uses pids).
5. Names persist across restarts even though pids change.
6. `which_children/1` and `count_children/1` report dynamic children.

# Construction / Recognition

## To Construct/Create:
1. Start the supervisor with an empty or computed child specification list in `init/1`.
2. At runtime, build a child specification and call `supervisor:start_child(?MODULE, ChildSpec)`.
3. To remove a child: `terminate_child/2`, then `delete_child/2`.

## To Identify/Recognize:
1. The supervisor's `init/1` returns few or no static child specs.
2. Children appear via `start_child` calls at runtime.

# Context & Application

- **Typical contexts**: Supervisors for entities that come and go — connections, sessions, devices.
- **Common applications**: A phone supervisor adding a worker per attached mobile device.
- **Historical/stylistic notes**: The book notes children crash and are restarted, so pids change, but the unique names stay the same — hence management calls use names, not pids (p. 187).

# Examples

**Example 1** (pp. 184-186): `phone_sup` — an empty `one_for_one` supervisor whose `attach_phone/1` builds a child spec and calls `supervisor:start_child(?MODULE, ChildSpec)`.

**Example 2** (p. 186): Shell session showing `start_child`, `terminate_child`, `restart_child`, and `delete_child` on `phone_sup`.

## Worked Example

`phone_sup` adding a dynamic child (pp. 184-185):

```erlang
attach_phone(Ms) ->
    case hlr:lookup_id(Ms) of
        {ok, _Pid} ->
            {error, attached};
        _NotAttached ->
            ChildSpec = {Ms, {phone_fsm, start_link, [Ms]},
                         transient, 2000, worker, [phone_fsm]},
            supervisor:start_child(?MODULE, ChildSpec)
    end.
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Simple one for one strategy** — The strategy designed for homogeneous, high-volume dynamic children.
- **One for one strategy** — Used by `phone_sup` for heterogeneous dynamic children.

## Contrasts With
- *(none — dynamic vs. static children is captured in Key Properties)*

# Common Errors

- **Error**: Calling `delete_child/2` on a still-running dynamic child.
  **Correction**: Terminate the child first (`terminate_child/2`), then delete it; `delete_child` on a running child returns `{error, running}`.

- **Error**: Tracking dynamic children by pid under a list-based strategy.
  **Correction**: Use the child's unique name; pids change across restarts.

# Common Confusions

- **Confusion**: Believing a terminated dynamic child's specification is automatically removed.
  **Clarification**: Under `one_for_one`/`one_for_all`/`rest_for_one` the spec remains (pid `undefined`) until `delete_child/2`; only `simple_one_for_one` removes it automatically.

# Source Reference

Chapter 7: Supervisors, "Dynamic Children" and "Gluing it all together," pages 184-189. See Figure 8-10 (Dynamic children).

# Verification Notes

- Definition source: Direct adaptation from pp. 184-187.
- Confidence rationale: HIGH — explicitly defined with full `phone_sup` code and a shell walkthrough.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
