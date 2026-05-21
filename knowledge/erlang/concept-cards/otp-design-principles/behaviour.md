---
# === CORE IDENTIFICATION ===
concept: Behaviour
slug: behaviour

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Overview"
chapter_number: null
pdf_page: null
section: "Behaviours"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "behavior"
  - "OTP behaviour"
  - "behaviour module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
extends: []
related:
  - callback-module
  - gen-server
  - gen-event
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a behaviour in OTP?"
  - "How does a behaviour module relate to a callback module?"
  - "What are the standard OTP behaviours?"
---

# Quick Definition

A behaviour is a formalization of a common process pattern in OTP, dividing code into a generic part (the behaviour module) and a specific part (the callback module).

# Core Definition

According to the OTP Design Principles Overview: "Behaviours are formalizations of these common patterns. The idea is to divide the code for a process in a generic part (a behaviour module) and a specific part (a callback module)." The behaviour module is part of Erlang/OTP and handles the generic process logic, while the user implements the callback module, which must "export a pre-defined set of functions, the callback functions."

# Prerequisites

- **Supervision Tree** — behaviours formalize the patterns used by processes in supervision trees.

# Key Properties

1. Divides process code into a generic part (behaviour module) and a specific part (callback module).
2. The behaviour module is part of Erlang/OTP; the user implements only the callback module.
3. The callback module must export a pre-defined set of callback functions.
4. The compiler understands the `-behaviour(Behaviour)` module attribute and warns about missing callback functions.
5. Using behaviours makes code more consistent, manageable, and readable.

# Construction / Recognition

## To Construct/Create:
1. Choose the appropriate OTP behaviour for the process pattern (e.g., `gen_server` for client-server).
2. Create a callback module with the `-behaviour(BehaviourName)` attribute.
3. Implement all required callback functions as defined by the behaviour.
4. The compiler will warn about any missing callback functions.

## To Identify/Recognize:
1. A module with `-behaviour(gen_server)`, `-behaviour(gen_event)`, `-behaviour(supervisor)`, or similar attribute.
2. Exports the callback functions required by the specified behaviour.
3. Code is structured with interface functions and callback functions in the same module.

# Context & Application

Behaviours are central to OTP programming. They provide tested, standardized implementations of common process patterns. The source lists four standard behaviours: `gen_server` (client-server), `gen_statem` (state machines), `gen_event` (event handling), and `supervisor` (supervision). Using behaviours trades some potential efficiency for consistency: "Code written without using behaviours can be more efficient, but the increased efficiency is at the expense of generality."

# Examples

**Example 1** (design_principles.md, "Behaviours"): The source demonstrates the behaviour concept by showing how a plain Erlang server (`ch1`) is refactored into a generic `server` module and a callback module `ch2`. The `server` module contains `call/2`, `cast/2`, and the receive loop, while `ch2` implements `init/0`, `handle_call/2`, and `handle_cast/2`.

**Example 2** (design_principles.md, "Behaviours"): The compiler's behaviour checking is demonstrated:
```erlang
-module(chs3).
-behaviour(gen_server).
...
3> c(chs3).
./chs3.erl:10: Warning: undefined call-back function handle_call/3
{ok,chs3}
```

# Relationships

## Builds Upon
- **Supervision Tree** — behaviours formalize the patterns found in supervision tree processes.

## Enables
- **Callback Module** — the user-written counterpart to a behaviour module
- **gen_server** — one of the standard OTP behaviours
- **gen_event** — one of the standard OTP behaviours
- **gen_statem** — one of the standard OTP behaviours
- **supervisor-behaviour** — one of the standard OTP behaviours

## Related
- **Worker Process** — workers are commonly implemented using behaviours
- **Supervisor Process** — supervisors use the supervisor behaviour

## Contrasts With
- No direct contrasts in source, though behaviours are contrasted with "improvised programming structures" which are "possibly more efficient" but "always more difficult to understand."

# Common Errors

- **Error**: Forgetting to export required callback functions.
  **Correction**: The compiler will issue warnings for missing callbacks when the `-behaviour` attribute is present. Ensure all required callbacks are implemented and exported.

# Common Confusions

- **Confusion**: Confusing the behaviour module with the callback module.
  **Clarification**: The behaviour module (e.g., `gen_server`) is provided by OTP and handles generic process logic. The callback module is written by the user and contains application-specific logic. They work together.

# Source Reference

OTP Design Principles, Overview, "Behaviours" section (design_principles.md).

# Verification Notes

- Definition source: Directly quoted from design_principles.md "Behaviours" section.
- Confidence rationale: High — central concept, explicitly and extensively defined in the source.
- Uncertainties: None.
- Cross-reference status: References callback-module, gen-server, gen-event, gen-statem, supervisor-behaviour (planned cards).
