---
# === CORE IDENTIFICATION ===
concept: Process Type
slug: process-type

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-fundamentals
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.1.2 Behaviour basics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - spawn signature
  - initial call

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - behaviour-instantiation
  - behaviour-container
  - canonical-behaviour-module-layout
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a process type in Erlang?"
  - "When are two processes of the same type?"
  - "What is a process's spawn signature?"
---

# Quick Definition

A process type is an informal notion that lets you talk about processes that run mainly the same code and understand mainly the same messages. Two such processes differ only in their individual state.

# Core Definition

The informal notion of process *type* (regardless of whether behaviours are involved) lets us talk about things like "a `gen_server` process" (Ch. 3, "Process type" sidebar). Processes are of the same type if they are running mainly the same code, which means they understand mainly the same kind of messages. The only difference between two processes of the same type is their individual state. Processes of the same type generally have the same *spawn signature* or *initial call* — that is, they had the same function as a starting point.

# Prerequisites

- **Process** — Process type is a way of classifying processes.

# Key Properties

1. It is an informal classification, not a runtime construct.
2. Two processes are of the same type if they run mainly the same code.
3. Same-type processes understand mainly the same kind of messages.
4. The only difference between same-type processes is their state.
5. Same-type processes generally share a spawn signature / initial call (the same starting function).

# Construction / Recognition

## To Recognize Process Type:
1. Identify the function each process was spawned from (its initial call).
2. Processes spawned from the same function are of the same type.
3. The set of messages a process accepts (its protocol) is shared within a type.

# Context & Application

The notion is used to reason about systems: "the `gen_server` processes," "the `sc_element` processes." It underpins the rule that a module should hold code for only one process type.

- **Typical contexts**: Describing behaviour-based processes; reasoning about a module's role.
- **Common applications**: The canonical rule "only one process type per module" relies on this concept.

# Examples

**Example 1** (Ch. 3): All `gen_server`-based processes are of one informal type because they run the `gen_server` framework code.

**Example 2** (Ch. 6): The many `sc_element` processes are all the same type — same code, different stored values and lease times.

# Relationships

## Builds Upon
- **Process** — A type classifies processes.

## Related
- **behaviour-instantiation** — Behaviour instances are processes of the same type.
- **behaviour-container** — Containers of one behaviour share a type.
- **canonical-behaviour-module-layout** — The "one process type per module" rule rests on this notion.

## Contrasts With
- This is a classification concept; the source draws no direct contrast.

# Common Errors

- **Error**: Mixing code for several process types in one module.
  **Correction**: Keep one process type per module so the module's role is clear.

# Common Confusions

- **Confusion**: Thinking process type is something Erlang tracks at runtime.
  **Clarification**: It is an informal notion used by programmers to reason about systems, not a runtime tag.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.1.2 "Behaviour basics," "Process type" sidebar. See also the "Only one process type per module" sidebar in Section 3.2.3.

# Verification Notes

- Definition source: Direct adaptation of the "Process type" sidebar.
- Confidence rationale: HIGH — explicit definition in a dedicated sidebar.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
