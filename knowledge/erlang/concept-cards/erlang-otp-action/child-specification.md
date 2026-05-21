---
# === CORE IDENTIFICATION ===
concept: Child Specification
slug: child-specification

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "OTP applications and supervision"
chapter_number: 4
pdf_page: null
section: "4.2.3 Writing the child specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - child spec
  - "child specification tuple"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - supervisor-implementation
extends:
  - supervisor
related:
  - supervisor-restart-strategy
  - worker-process
  - simple-one-for-one
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a child specification?"
  - "What are the six elements of a child specification?"
  - "What do permanent, temporary, and transient mean for a child?"
---

# Quick Definition

A child specification is a six-element tuple `{ID, Start, Restart, Shutdown, Type, Modules}` that tells a supervisor how to start and manage one of its child processes.

# Core Definition

A child specification is a tuple that describes a process you want the supervisor to manage (Ch. 4, Section 4.2.3). It has six elements `{ID, Start, Restart, Shutdown, Type, Modules}`:

- **ID** — A term the supervisor uses to identify the specification internally.
- **Start** — An MFA triple `{Module, Function, Arguments}` used to start the process, like `spawn/3`.
- **Restart** — Whether the child is restarted: `permanent` (always restarted), `temporary` (never restarted), or `transient` (restarted only on abnormal termination).
- **Shutdown** — How the process may be killed: an integer (soft shutdown, milliseconds allowed before being killed), `brutal_kill` (terminated immediately), or `infinity` (used when the child is itself a supervisor).
- **Type** — `worker` or `supervisor`.
- **Modules** — The modules this process depends on, used only during hot code upgrades to order module upgrades.

# Prerequisites

- **Supervisor** — Child specifications are consumed by a supervisor.
- **Implementing a supervisor** — Child specs appear in a supervisor's `init/1`.

# Key Properties

1. A six-element tuple `{ID, Start, Restart, Shutdown, Type, Modules}`.
2. `Start` is an MFA triple, like `spawn/3`.
3. `Restart` is `permanent`, `temporary`, or `transient`.
4. `Shutdown` is an integer (milliseconds), `brutal_kill`, or `infinity`.
5. `Type` is `worker` or `supervisor`.
6. `Modules` is used only for hot code upgrade ordering.

# Construction / Recognition

## To Write a Child Specification:
1. Choose an `ID` term (often the child module name).
2. Write the `Start` MFA triple (e.g. `{tr_server, start_link, []}`).
3. Pick a `Restart` value (`permanent`/`temporary`/`transient`).
4. Pick a `Shutdown` value (integer ms, `brutal_kill`, or `infinity`).
5. Set `Type` to `worker` or `supervisor`.
6. List the depended-on `Modules` (usually just the main module).

# Context & Application

Child specifications are how a supervisor learns what to run; they appear as the `Children` list in `init/1`'s return value.

- **Typical contexts**: A static list in a supervisor's `init/1`; or the single template spec of a `simple_one_for_one` supervisor.
- **Common applications**: `tr_sup`'s spec for `tr_server`; `sc_sup`'s template spec for `sc_element`.

# Examples

**Example 1** (Ch. 4): `Server = {tr_server, {tr_server, start_link, []}, permanent, 2000, worker, [tr_server]}` — a `permanent` worker with a 2000 ms soft shutdown.

**Example 2** (Ch. 6): `sc_sup`'s `simple_one_for_one` child spec uses `{sc_element, start_link, []}` with `Restart` `temporary` and `Shutdown` `brutal_kill`; extra args are appended at `start_child` time.

# Relationships

## Builds Upon
- **Supervisor** — Child specs are part of a supervisor's configuration.

## Related
- **supervisor-restart-strategy** — The other half of `init/1`'s return value.
- **worker-process** — `Type` `worker` marks a child as a worker.
- **simple-one-for-one** — Uses a single template child spec.

## Contrasts With
- This is a configuration tuple; the source draws no direct contrast.

# Common Errors

- **Error**: Using an integer `Shutdown` for a child that is itself a supervisor.
  **Correction**: Use `infinity` so a child supervisor gets all the time it needs.

- **Error**: Marking a long-lived service as `temporary`.
  **Correction**: Use `permanent` for services that should always be restarted.

# Common Confusions

- **Confusion**: Confusing `temporary` and `transient`.
  **Clarification**: `temporary` is never restarted; `transient` is restarted only on abnormal termination.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.2.3 "Writing the child specification."

# Verification Notes

- Definition source: Direct adaptation of Section 4.2.3.
- Confidence rationale: HIGH — explicit, element-by-element treatment.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
