---
# === CORE IDENTIFICATION ===
concept: Child Specification
slug: child-specification

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Making a System with OTP"
chapter_number: 23
pdf_page: null
section: "The Supervision Tree"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "child spec"
  - "worker specification"
  - "start specification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
extends: []
related:
  - supervision-tree
  - restart-strategy
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a child specification?"
  - "How does a supervisor know how to start a worker?"
---

# Quick Definition

A child specification is a tuple in a supervisor's `init/1` that tells the supervisor how to start one child process — its start function, restart type, shutdown time, process type, and callback modules.

# Core Definition

In a supervisor's `init/1` the children "are tuples describing how to start each of the worker processes" (Programming Erlang, "The Supervision Tree"). A child (worker) specification has the form:

```erlang
{Tag, {Mod, Func, ArgList},
 Restart,
 Shutdown,
 Type,
 [Mod1]}
```

- `Tag` — an atom used to refer to the child later.
- `{Mod, Func, ArgList}` — the start function, used as `apply(Mod, Func, ArgList)`.
- `Restart` — `permanent` (always restarted), `transient` (restarted only on non-normal exit), or `temporary` (never restarted).
- `Shutdown` — the maximum time the worker may take to terminate before it is killed.
- `Type` — `worker` or `supervisor`.
- `[Mod1]` — the callback module name if the child is a supervisor or `gen_server`.

# Prerequisites

- **Supervisor** — child specifications are the children listed in a supervisor's `init/1`.

# Key Properties

1. A six-element tuple `{Tag, {Mod, Func, ArgList}, Restart, Shutdown, Type, [Mod1]}`.
2. `Tag` names the child for later reference.
3. `{Mod, Func, ArgList}` is applied to start the worker — typically the worker's `start_link`.
4. `Restart` is `permanent`, `transient`, or `temporary`.
5. `Shutdown` bounds how long termination may take before the worker is killed.
6. `Type` is `worker` or `supervisor`; a `supervisor` child deepens the supervision tree.

# Construction / Recognition

## To Write a Child Specification:
1. Choose an atom `Tag` for the child.
2. Supply `{Mod, Func, ArgList}` — usually `{my_server, start_link, []}`.
3. Pick a `Restart` type appropriate to the child's role.
4. Set a `Shutdown` time limit.
5. Set `Type` to `worker` (or `supervisor` for a nested supervisor).
6. List the callback module in `[Mod1]`.

## To Recognize:
1. A six-element tuple inside a supervisor `init/1` child list is a child specification.

# Context & Application

- **Typical contexts**: Inside every supervisor callback module's `init/1`.
- **Common applications**: `sellaprime_supervisor` specifies the `area_server` and `prime_server` as permanent workers with a 10000 ms shutdown.
- **Historical/stylistic notes**: The book reassures that "you can cut and paste the values from the earlier area server code and insert the name of your module" — most child specs are boilerplate.

# Examples

**Example 1** ("The Supervision Tree"): The `area_server` child specification:

```erlang
{tag1,
 {area_server, start_link, []},
 permanent,
 10000,
 worker,
 [area_server]}
```

**Example 2** ("The Supervision Tree"): The `prime_server` spec has the same shape with `tag2`, `{prime_server, start_link, []}`, `permanent`, `10000`, `worker`, `[prime_server]`.

# Relationships

## Builds Upon
- **Supervisor** — child specs are the worker list a supervisor's `init/1` returns.

## Enables
- **Supervision tree** — child specs of `Type = supervisor` extend the tree.

## Related
- **Restart strategy** — the supervisor-level strategy and the per-child `Restart` together govern restarts.
- **gen_server** — the workers named in child specs are usually gen_servers.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Marking a one-shot helper process `permanent`.
  **Correction**: Use `temporary` for processes that should never be restarted, or `transient` if only abnormal exits should trigger a restart.

- **Error**: Pointing `{Mod, Func, ArgList}` at a function that doesn't link the child to the supervisor.
  **Correction**: The start function should `start_link` the worker so the supervisor is notified of its failure.

# Common Confusions

- **Confusion**: Confusing the per-child `Restart` type with the supervisor's restart strategy.
  **Clarification**: `Restart` (`permanent`/`transient`/`temporary`) decides whether *this* child is restarted; the strategy (`one_for_one`/`one_for_all`) decides *how many* children are affected.

- **Confusion**: Thinking `Type` must always be `worker`.
  **Clarification**: `Type` can be `supervisor`, which is how a supervision tree gains depth.

# Source Reference

Chapter 23: Making a System with OTP, section "The Supervision Tree". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "The Supervision Tree".
- Confidence rationale: HIGH — the worker specification tuple and each field are explicitly enumerated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
