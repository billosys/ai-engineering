---
concept: Circular Dependency
slug: circular-dependency
category: tooling
subcategory: code-organization
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Modules"
chapter_number: 2
pdf_page: null
section: "Circular Dependencies"
extraction_confidence: medium
aliases:
  - "module coupling"
prerequisites:
  - module
extends: []
related:
  - function-export
contrasts_with: []
answers_questions:
  - "What is a module?"
---

# Circular Dependency

## Quick Definition

A circular dependency occurs when module A calls module B and module B also calls module A. Such mutual dependencies make code maintenance difficult and should be avoided.

## Core Definition

A point of module design is to avoid circular dependencies: a module A should not call a module B that also calls module A. Such dependencies usually end up making code maintenance difficult. More broadly, code that depends on too many modules — even without a cycle — makes maintenance harder (Hébert, ch. 2, "Circular Dependencies").

## Prerequisites

- **Module** — Circular dependencies are a relationship between modules

## Key Properties

1. Arises when module A calls module B while module B calls module A.
2. Makes code harder to maintain and reason about.
3. Excessive dependence on many modules (even acyclic) also harms maintainability.
4. It is a design anti-pattern to be avoided, not a syntax error.

## Construction / Recognition

To recognize a circular dependency, trace which modules call which: if following the call chain returns to the starting module, the design has a cycle.

## Context & Application

Avoiding circular dependencies and minimizing inter-module coupling is part of good module design — it keeps modules independently maintainable and changeable.

## Examples

**Example** (ch. 2): The book gives the abstract case: module `A` calling module `B` which in turn calls module `A`, described as a maintenance hazard.

## Relationships

### Prerequisites

- **Module** — The unit involved in dependencies

### Related

- **Function export** — A module's exported interface defines what other modules can depend on

## Common Errors

- **Error**: Letting two modules call each other for convenience
  **Correction**: Restructure so dependencies flow one direction, or extract shared logic into a third module

## Common Confusions

- **Confusion**: Thinking circular dependencies cause a compile error
  **Clarification**: They compile fine; the problem is maintainability, not correctness

## Source Reference

Chapter 2: "Modules," section "Circular Dependencies."

## Verification Notes

- Definition: Adapted from the short "Circular Dependencies" section
- Confidence: MEDIUM — the source treats this briefly as design advice rather than a formally defined concept
- Uncertainties: None
