---
# === CORE IDENTIFICATION ===
concept: OTP Behaviors
slug: otp-behaviors

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: behavior-concept
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Behaviors"
chapter_number: 2
pdf_page: 72
section: "Behaviors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - behavior
  - behaviour
  - OTP behaviour
  - process design pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-skeleton
extends: []
related:
  - callback-module
  - generic-vs-specific-code
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP behavior?"
  - "What behaviors does OTP provide?"
  - "Why use behaviors instead of writing concurrency code by hand?"
---

# Quick Definition

OTP behaviors are generic library modules that abstract the most common Erlang process design patterns. They are, in design-pattern terms, implementation libraries of the concurrency models.

# Core Definition

"Erlang processes that solve radically different tasks follow similar design patterns. The most commonly used patterns have been abstracted and implemented in a set of generic library modules called the OTP behaviors. When reading about behaviors, you should see them as a formalization of process design patterns" (Cesarini & Vinoski, p. 51). They are "implementation libraries of the concurrency models." OTP provides five behaviors: the *generic server*, *generic finite state machine*, *generic event handler/manager*, *supervisor*, and *application* (p. 56). Generic servers, FSMs, and event handlers are *workers*; supervisors and applications hold workers together.

# Prerequisites

- **Process skeleton** — Behaviors formalize the common process skeleton; you must understand that shared lifecycle first.

# Key Properties

1. A behavior abstracts a common process design pattern into a reusable library module.
2. OTP provides five behaviors: generic server, generic FSM, generic event handler/manager, supervisor, application.
3. Generic servers, FSMs, and event handlers are *workers*; supervisors and applications are structural.
4. Behaviors hide tricky concurrency aspects and borderline conditions.
5. They rest on a solid, well-tested code base used in production since the mid-90s.
6. They provide built-in logs, tracing, and statistics, extensible generically.
7. They promote a common programming style and component vocabulary.
8. Costs: a learning curve, and small layering/protocol overhead in performance and memory.

# Construction / Recognition

## To Construct:
1. Choose the behavior matching your process pattern.
2. Implement a callback module exporting the behavior's required callbacks.
3. Let the behavior library supply the generic driver code.

## To Recognize:
1. Look for a `-behavior(...)` directive in a module.

# Context & Application

- **Typical contexts**: Structuring concurrency and supervision in any OTP system.
- **Common applications**: Generic servers model client-server processes; supervisors build supervision trees.
- **Historical/stylistic notes**: The rule of thumb is "always start with behaviors, and optimize when bottlenecks occur" (p. 58).

# Examples

**Example 1** (p. 56): The five behaviors and their roles — generic server for client-server, generic FSM for FSM programming, generic event handler for event-driven programming, supervisor for fault-tolerant supervision trees, application to encapsulate resources and functionality.

**Example 2** (p. 56): Behaviors not in the standard library can be implemented as *special processes* following specific rules (covered in Chapter 10).

# Relationships

## Builds Upon
- **Process skeleton** — Behaviors are the process skeleton formalized into libraries.

## Enables
- **Gen_server** — The most commonly used behavior, the foundation for the others.

## Related
- **Callback module** — Behaviors split code into a generic behavior module and a specific callback module.
- **Generic vs. specific code** — The split that motivates behaviors.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Hand-rolling concurrency code instead of using a behavior.
  **Correction**: Start with behaviors; they handle corner cases a first implementation would miss.

# Common Confusions

- **Confusion**: Equating OTP behaviors with OO design patterns.
  **Clarification**: "The strict concept of design patterns used in object-oriented programming hasn't been applied to Erlang" — behaviors are concrete, reusable library implementations, not informal patterns.

# Source Reference

Chapter 2: Behaviors, Section "Behaviors" (chapter intro) and "Callback Modules," pages 51-58.

# Verification Notes

- Definition source: Direct quotes from pp. 51 and 56.
- Confidence rationale: HIGH — explicit definition and enumeration of the five behaviors.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
