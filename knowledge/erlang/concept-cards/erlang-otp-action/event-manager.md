---
# === CORE IDENTIFICATION ===
concept: Event Manager
slug: event-manager

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Logging and event handling the Erlang/OTP way"
chapter_number: 7
pdf_page: null
section: "7.2.1 Introducing the gen_event behaviour"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_event container"
  - "event handler process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
extends: []
related:
  - event-handler
  - supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event manager?"
  - "How is an event manager started?"
  - "How do I refer to an event manager to add handlers?"
---

# Quick Definition

An event manager is the `gen_event` container process: a long-lived process that holds a dynamic set of event handler modules and dispatches every posted event to all of them.

# Core Definition

An event manager is the container process created by the `gen_event` behaviour. Unlike a `gen_server` container, it is not tied to a callback module at startup; instead it holds a set of handler modules that are added and removed dynamically. When an event is posted to the manager, it calls each registered handler in turn. An event manager can be registered under a name when it starts (with `gen_event:start_link/1`, passing e.g. `{local, Name}`), which makes it easy to talk to and add handlers to. It is typically started directly from a supervisor via a child specification such as `{my_logger, {gen_event, start_link, [{local, my_logger}]}, permanent, 1000, worker, [gen_event]}` (Ch. 7, Sections 7.2.1 and 7.3.1).

# Prerequisites

- **gen_event** — The event manager is the container the `gen_event` behaviour provides; the behaviour concept comes first.

# Key Properties

1. The `gen_event` container process.
2. Starts with no callback module.
3. Holds a dynamic, possibly empty set of handler modules.
4. Dispatches each posted event to every registered handler.
5. Can be registered under a name (e.g., locally) for easy reference.
6. Usually started by a supervisor, tagged as a `worker`.

# Construction / Recognition

## To Create an Event Manager:
1. Call `gen_event:start_link/0` or `gen_event:start_link({local, Name})` to register it.
2. Or give a supervisor a child spec naming `gen_event` as the start module.
3. Add handlers afterward with `gen_event:add_handler/3`.

## To Recognize:
1. A registered process that other code adds `gen_event` handlers to is an event manager.

# Context & Application

- **Typical contexts**: The `error_logger` process; custom application event streams.
- **Common applications**: A central point through which events flow to multiple subscribers.
- **Historical/stylistic notes**: The book also calls it the `gen_event` container; "event manager" is the official term.

# Examples

**Example 1** (Section 7.3.1, Listing 7.5): The `sc_event` module's `start_link()` hides a call to `gen_event:start_link/1`, starting an event manager registered locally under the module's name.

**Example 2** (Section 7.3.1): A supervisor child specification `{my_logger, {gen_event, start_link, [{local, my_logger}]}, permanent, 1000, worker, [gen_event]}` starts an event manager named `my_logger`.

# Relationships

## Builds Upon
- **gen_event** — The behaviour that defines the event manager container.

## Enables
- **event-handler** — Handlers are registered with an event manager.

## Related
- **supervisor** — Event managers are typically started under a supervisor.

## Contrasts With
- None.

# Common Errors

- **Error**: Hardcoding the registered name of the manager throughout client code.
  **Correction**: Provide wrapper API functions so callers need not know the manager's name.

# Common Confusions

- **Confusion**: Thinking the event manager itself contains the event-handling logic.
  **Clarification**: The logic lives in the handler modules; the manager only dispatches.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Sections 7.2.1 "Introducing the gen_event behaviour" and 7.3.1 "The event stream API."

# Verification Notes

- Definition source: Directly adapted from Sections 7.2.1 and 7.3.1.
- Confidence rationale: HIGH — the book explicitly names and describes the event manager.
- Uncertainties: None.
- Cross-reference status: Verified.
