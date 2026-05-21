---
concept: Behaviour as Navigation Clue
slug: behaviour-as-navigation-clue
category: otp-behaviours
subcategory: code-navigation
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "How to Dive into a Code Base"
chapter_number: 1
pdf_page: null
section: "Regular Applications"
extraction_confidence: high
aliases:
  - "Behaviour role clues"
prerequisites:
  - regular-application
extends: []
related:
  - supervision-tree-navigation
  - supervisor-restart-strategy
contrasts_with: []
answers_questions:
  - "Why would someone use a gen_fsm behaviour over a gen_server?"
  - "How do I dive into an unfamiliar code base?"
---

# Quick Definition

The OTP behaviour a worker process implements (`gen_server`, `gen_fsm`, `gen_event`) is a strong clue about that process's purpose when navigating an unfamiliar code base.

# Core Definition

From Chapter 1, section "Regular Applications": "For each worker process supervised, the behaviour it implements will give a good clue about its purpose":

- A `gen_server` "holds resources and tends to follow client/server patterns (or more generally, request/response patterns)."
- A `gen_fsm` "will deal with a sequence of events or inputs and react depending on them, as a Finite State Machine. It will often be used to implement protocols."
- A `gen_event` "will act as an event hub for callbacks, or as a way to deal with notifications of some sort."

# Prerequisites

- `regular-application` — behaviours are recognized while navigating a regular application's processes.

# Key Properties

1. `gen_server` → resource holder / client-server / request-response.
2. `gen_fsm` → reacts to a sequence of events as a finite state machine; commonly implements protocols.
3. `gen_event` → event hub for callbacks or notifications.
4. All three behaviour modules share the same internal layout: user-facing interface functions first, callback-module functions next, then private functions.
5. Reading the inter-module interface together with the implemented behaviour reveals a lot about the program.

# Construction / Recognition

When examining a worker module: check its `-behaviour(...)` declaration; map the behaviour to the role above; then read the exported interface functions (which appear first) to learn how the process is used.

# Context & Application

Used alongside supervision tree navigation: the tree position tells you a process's importance and dependencies, while its behaviour tells you what kind of work it does. Together they let you build a mental map of an unfamiliar application quickly.

# Examples

From Chapter 1, section "Regular Applications": the book gives `gen_fsm` "implementing protocols" as a concrete role, contrasting with `gen_server`'s "request/response patterns" — directly answering why one would choose `gen_fsm` over `gen_server` (the work is a stateful sequence of events, not isolated requests).

# Relationships

## Builds Upon
- `regular-application` — behaviours appear in its worker processes.

## Enables
Faster comprehension of a worker's purpose.

## Related
- `supervision-tree-navigation` — the structural complement.
- `supervisor-restart-strategy` — another clue read while navigating.

## Contrasts With
Nothing directly.

# Common Errors

- Assuming a module with no behaviour is broken — a behaviour-less module in a library application is likely a functional, stateless library.

# Common Confusions

- The behaviour indicates a *typical* role, not a guarantee — a `gen_server` could be used in unusual ways; treat it as a strong heuristic, not a rule.

# Source Reference

Chapter 1: How to Dive into a Code Base, Section "Regular Applications". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 1, section "Regular Applications."
- Confidence rationale: high — each behaviour's role explicitly stated.
- Uncertainties: `gen_fsm` is the older behaviour name used by the source; modern OTP uses `gen_statem`.
- Cross-reference status: Verified
