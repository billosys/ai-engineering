---
# === CORE IDENTIFICATION ===
concept: supervisor:start_child
slug: supervisor-start-child

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Implementing a caching system"
chapter_number: 6
pdf_page: null
section: "6.3.4 Implementing the supervisor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "supervisor:start_child/2"
  - start_child

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - simple-one-for-one
  - child-specification
extends:
  - simple-one-for-one
related:
  - sc-element
  - simple-one-for-one
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does supervisor:start_child do?"
  - "How do you add a child to a supervisor at runtime?"
  - "How does start_child differ for simple_one_for_one supervisors?"
---

# Quick Definition

`supervisor:start_child/2` asks a running supervisor to start a new child process at runtime; for a `simple_one_for_one` supervisor it takes only the per-child extra arguments.

# Core Definition

`supervisor:start_child/2` is the library function used to ask a running supervisor to start new child processes at any time (Ch. 6, Section 6.3.4). For most kinds of supervisors, adding children dynamically requires giving `start_child/2` a full child specification. With a `simple_one_for_one` supervisor, all children share the same specification, which the supervisor already knows, so the caller only has to say "please start another one" — supplying just the per-child extra arguments. Those extra arguments are appended to the argument list in the template child spec's start MFA before the start function is called.

# Prerequisites

- **Supervisor** — `start_child` adds a child to a supervisor.
- **simple_one_for_one supervision** — The simplified form applies to `simple_one_for_one` supervisors.
- **Child specification** — For other supervisors a full child spec is passed.

# Key Properties

1. Asks a running supervisor to start a new child at runtime.
2. For most supervisors, takes a full child specification.
3. For `simple_one_for_one`, takes only the per-child extra arguments.
4. Extra arguments are appended to the template spec's start-MFA argument list.
5. Sends a message to the supervisor process to perform the start.

# Construction / Recognition

## To Use start_child:
1. For a `simple_one_for_one` supervisor, call `supervisor:start_child(SupRef, ExtraArgs)`.
2. `ExtraArgs` is the list appended to the template start MFA.
3. Wrap the call in a supervisor API function to keep details encapsulated.

# Context & Application

`start_child` is how a `simple_one_for_one` supervisor acts as a factory: each call spawns one more identical worker.

- **Typical contexts**: Spawning per-item worker processes on demand.
- **Common applications**: `sc_sup:start_child/2` calls `supervisor:start_child(?SERVER, [Value, LeaseTime])` to create a new `sc_element`.

# Examples

**Example 1** (Ch. 6): `sc_sup:start_child(Value, LeaseTime)` calls `supervisor:start_child/2`; the args `[Value, LeaseTime]` are appended to the template spec's `{sc_element, start_link, []}`, producing `sc_element:start_link(Value, LeaseTime)`.

# Relationships

## Builds Upon
- **simple_one_for_one supervision** — The simplified form of `start_child` applies to such supervisors.

## Related
- **sc-element** — Each `start_child` call spawns a new `sc_element`.
- **child-specification** — The template spec whose argument list extra args are appended to.

## Contrasts With
- This is a library function; the source draws no direct contrast.

# Common Errors

- **Error**: Passing a full child specification to `start_child` for a `simple_one_for_one` supervisor.
  **Correction**: For `simple_one_for_one`, pass only the per-child extra arguments.

# Common Confusions

- **Confusion**: Thinking the extra args replace the template spec's argument list.
  **Clarification**: They are appended to it before the start function is called.

# Source Reference

Chapter 6: Implementing a caching system, Section 6.3.4 "Implementing the supervisor," "The supervisor module" subsection.

# Verification Notes

- Definition source: Direct adaptation of Section 6.3.4.
- Confidence rationale: HIGH — explicit treatment in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group; the cache's `sc_sup` supervisor is covered by the `simple-one-for-one` card.
- Re-extraction notes: Fresh extraction; no prior card existed.
