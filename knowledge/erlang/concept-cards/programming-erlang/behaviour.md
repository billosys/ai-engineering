---
# === CORE IDENTIFICATION ===
concept: OTP Behaviour
slug: behaviour

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: otp-foundations
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "Introducing OTP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "behavior"
  - "OTP behavior"
  - "-behaviour"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp
  - callback-module
extends: []
related:
  - gen-server
  - supervisor
  - gen-event
  - otp-application
  - generic-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP behaviour?"
  - "How does a behaviour separate functional from nonfunctional code?"
---

# Quick Definition

An OTP behaviour is an application framework that encapsulates a common behavioural pattern and is parameterized by a callback module. The behaviour solves the nonfunctional part of a problem; the callback solves the functional part.

# Core Definition

"If you want to program your own applications using OTP, then the central concept that you will find useful is the OTP *behavior*. A behavior encapsulates common behavioral patterns — think of it as an application framework that is parameterized by a *callback* module" (Programming Erlang, "Introducing OTP"). The power of OTP comes from the fact that properties such as fault tolerance, scalability, and dynamic-code upgrade can be provided by the behaviour itself, so the writer of the callback does not have to worry about them. "Put simply, the behavior solves the nonfunctional parts of the problem, while the callback solves the functional parts." The compiler uses the `-behaviour(...)` attribute to generate warnings or errors if a required callback function is missing.

# Prerequisites

- **OTP** — behaviours are the central abstraction OTP provides.
- **Callback module** — a behaviour is incomplete without a callback module supplying its functional code.

# Key Properties

1. Splits a problem into a generic (nonfunctional) component and a specific (functional) callback component.
2. The nonfunctional parts — fault tolerance, code upgrade — are the same for all applications using that behaviour.
3. The functional parts, supplied by the callback, differ for every problem.
4. Declared in a module with the `-behaviour(Name)` attribute.
5. The compiler checks, via `-behaviour`, that all required callback functions are exported.
6. Analogous to a J2EE container for the Java-minded reader.

# Construction / Recognition

## To Use a Behaviour:
1. Choose the behaviour that matches your problem (`gen_server`, `supervisor`, `gen_event`, `application`).
2. Create a callback module and add `-behaviour(BehaviourName).`
3. Export and implement every required callback function for that behaviour.
4. Fill in only the sequential, problem-specific logic in the callbacks.

## To Recognize:
1. A module containing `-behaviour(gen_server).` (or similar) is a behaviour callback module.
2. A compiler warning about a missing callback function indicates the `-behaviour` contract is unsatisfied.

# Context & Application

- **Typical contexts**: Every OTP-based server, supervisor, event handler, and application.
- **Common applications**: `gen_server`, `supervisor`, `gen_event`, `application` are the behaviours covered in this and the next chapter.
- **Historical/stylistic notes**: The book builds `gen_server` from scratch precisely to show how a behaviour factors the generic part out of a family of similar servers.

# Examples

**Example 1** ("Step 3: Write the Callback Routines"): The `gen_server` mini template begins with `-behaviour(gen_server).`, so the compiler can warn if a callback is forgotten.

**Example 2** ("Alarm Management"): `my_alarm_handler` declares `-behaviour(gen_event).`, marking it as a callback module for the generic event behaviour.

# Relationships

## Builds Upon
- **OTP** — behaviours are the framework abstraction OTP delivers.

## Enables
- **gen_server** — a behaviour for client/server interactions.
- **Supervisor** — a behaviour for process supervision.
- **gen_event** — a behaviour for event handling.
- **OTP application** — a behaviour for packaging a whole system.

## Related
- **Callback module** — the user-supplied half of every behaviour.
- **Generic server** — the do-it-yourself precursor showing what a behaviour factors out.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Forgetting to export a required callback function.
  **Correction**: The `-behaviour` attribute makes the compiler warn; export all callbacks the behaviour demands.

- **Error**: Putting concurrency code (spawn, send, receive) in the callback module.
  **Correction**: The behaviour supplies the concurrency; callbacks contain only sequential code.

# Common Confusions

- **Confusion**: Thinking a behaviour is a base class to inherit from.
  **Clarification**: A behaviour is a framework that calls *into* your callback module; the relationship is parameterization, not inheritance.

- **Confusion**: Believing `-behaviour` changes runtime semantics.
  **Clarification**: `-behaviour` is mainly a compiler hint for checking the callback contract; the behaviour module itself supplies the runtime logic.

# Source Reference

Chapter 22: Introducing OTP, opening section "Introducing OTP" and "Step 3: Write the Callback Routines". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes from "Introducing OTP".
- Confidence rationale: HIGH — explicitly and repeatedly defined in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card. Spelling "behaviour" chosen as canonical slug per the taxonomy's `-behaviour` notation; the book uses American "behavior".
