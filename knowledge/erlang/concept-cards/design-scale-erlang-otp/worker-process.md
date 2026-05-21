---
# === CORE IDENTIFICATION ===
concept: Worker Process
slug: worker-process

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "OTP Supervisors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "worker"
  - "worker behavior"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
extends: []
related:
  - supervisor
  - child-specification
  - otp-behaviors
contrasts_with:
  - supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a supervisor from a worker process?"
  - "How do supervisors relate to the worker processes they manage?"
---

# Quick Definition

A worker is a process at the leaf of a supervision tree that performs the system's actual work, as opposed to a supervisor, which only monitors children. In a child specification the atom `worker` declares a child to be a worker rather than a supervisor.

# Core Definition

In OTP supervision trees, worker behaviors are the leaves: when describing supervision trees, worker behaviors are usually represented as circles, while supervisors are represented as squares (Cesarini & Vinoski, p. 173). A worker performs business logic — for example, a `gen_server`, `gen_fsm`/`gen_statem`, or `gen_event` process. In a child specification, the `ProcessType` field is set to the atom `worker` (as opposed to `supervisor`) to indicate that the child is a worker; this field is used during software upgrades to control how processes are suspended (pp. 181-182).

# Prerequisites

- **Supervision tree** — A worker is defined by its role as a leaf of a supervision tree.

# Key Properties

1. Workers do the system's actual work; supervisors do not.
2. A worker is the leaf of a supervision tree (drawn as a circle).
3. Workers are declared in a child specification with `type => worker` (or `worker` in the tuple form).
4. A worker must be an OTP-compliant behavior (or a special process) so the supervisor can link to and manage it.
5. There is nothing stopping a worker from trapping exits, though typically only supervisors do.

# Construction / Recognition

## To Construct/Create:
1. Implement the worker as an OTP behavior (`gen_server`, `gen_statem`, `gen_event`) or a special process.
2. Provide a `start_link` function the supervisor can call, returning `{ok, Pid}`.
3. In the parent supervisor's child specification, set the process type to `worker`.

## To Identify/Recognize:
1. The child specification's process type is `worker`.
2. The process is a leaf — it does not itself monitor children.

# Context & Application

- **Typical contexts**: The leaves of every OTP supervision tree.
- **Common applications**: Servers handling requests, FSMs handling protocol state, event managers handling alarms.
- **Historical/stylistic notes**: In the frequency example the `freq_overload` event manager and `frequency` server are both permanent workers (p. 182).

# Examples

**Example 1** (p. 175): In `frequency_sup`, the children `freq_overload` and `frequency` are declared with the `worker` atom in `child/1`.

**Example 2** (p. 191): In `bsc_sup`, `freq_overload` and `frequency` are `worker`s while `simple_phone_sup` is a `supervisor`.

## Worked Example

A child specification declaring a worker (p. 175):

```erlang
child(Module) ->
    {Module, {Module, start_link, []},
     permanent, 2000, worker, [Module]}.
```

The fifth element, `worker`, marks the child as a worker rather than a supervisor.

# Relationships

## Builds Upon
- *(none — worker is defined relative to the tree, not built on another concept)*

## Enables
- **Supervision tree** — Workers populate the leaves of the tree.

## Related
- **Supervisor** — The process that starts and monitors the worker.
- **Child specification** — Declares a child's type as `worker`.
- **OTP behaviour** — Workers are normally implemented as standard behaviors.

## Contrasts With
- **Supervisor** — A supervisor only monitors children; a worker does the actual work.

# Common Errors

- **Error**: Mislabeling a child supervisor as `worker` (or vice versa) in the child spec.
  **Correction**: Set the type accurately; it controls how processes are suspended during upgrades.

- **Error**: Attaching a plain Erlang process as a worker.
  **Correction**: Workers must be OTP behaviors or special processes that handle system messages; otherwise use a supervisor bridge.

# Common Confusions

- **Confusion**: Believing "worker" is a distinct OTP behavior module.
  **Clarification**: "Worker" is a *role* in a supervision tree; the worker is implemented by an ordinary behavior such as `gen_server`.

# Source Reference

Chapter 7: Supervisors, "OTP Supervisors" and "The child specification," pages 173-182.

# Verification Notes

- Definition source: Synthesized from pp. 173 and 181-182 (worker as tree leaf; `worker` process type field).
- Confidence rationale: HIGH — the worker role is explicit, with the `worker` atom shown in every child-spec example.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
