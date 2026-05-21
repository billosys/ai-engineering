---
concept: Success Typing
slug: success-typing
category: tooling
subcategory: static-analysis
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "Success Typing"
extraction_confidence: high
aliases:
  - "success typings"
prerequisites:
  - dynamic-typing
  - dialyzer
related:
  - type-specification
  - dialyzer-warning
contrasts_with: []
answers_questions:
  - "What is success typing?"
  - "Why does Dialyzer only report errors that are guaranteed to crash?"
---

# Success Typing

## Quick Definition

Success typing is the type-inference principle behind Dialyzer: it over-approximates the types a function can accept and return, so it never reports a false error, only ones guaranteed to crash.

## Core Definition

Dialyzer's designers chose not to prove a program is free of type errors, but to find as many errors as possible without ever contradicting what happens at runtime. A *success typing* is a type signature that over-approximates the set of types for which a function can evaluate to a value: its domain includes all values the function could accept, and its range includes all possible return values. Because of this over-approximation, if a function is used in a way *not* allowed by its success typing, that use will *definitely* fail — exactly the property a defect-detection tool that "never cries wolf" needs. Success typing works without type declarations, is automatic, respects the language's semantics, and imposes no code rewrites (Chapter 30, "Success Typing," quoting the "Practical Type Inference Based on Success Typings" paper).

## Prerequisites

- **Dynamic typing** — Success typing is a type-checking approach designed for a dynamically typed language
- **Dialyzer** — Success typing is the principle Dialyzer implements

## Key Properties

1. Over-approximates each function's accepted and returned types
2. Never reports a false positive — flagged uses are guaranteed to fail
3. Does not prove absence of errors — a trade-off for never crying wolf
4. Fully automatic; requires no type declarations (accepts them as hints)
5. Optimistic: Dialyzer assumes every function succeeds, accepts anything, returns anything, until analysis narrows it
6. May stay silent about uses that fail only *sometimes* (e.g., one branch of a `case`)
7. Once a call succeeds within a function body, Dialyzer may ignore later errors in the same code unit

## Construction / Recognition

## To Reason About Success Typing

1. Start optimistically — assume the function works for all inputs
2. As operations constrain it (e.g., `+` forces numbers), narrow the inferred domain and range
3. Flag a use only when it provably falls outside the inferred success typing

## Context & Application

Success typing explains Dialyzer's behavior: warnings about unknown functions during PLT building are harmless because Dialyzer optimistically assumes any use is fine. It also explains the silences — `convert/1` typed only as `list() | tuple() -> list() | tuple()` hides a real bug, and reordering calls in `zoo.erl` so a correct call comes first makes Dialyzer ignore the subsequent wrong call. Keeping Dialyzer's optimism in mind is vital to working efficiently with it.

## Examples

**Example** (Chapter 30, "Success Typing"): a function with `+` between its arguments gets the success typing "accepts two numbers, returns a number"; calling it with an atom and a number provably cannot return, so Dialyzer reports it.

**Example** (Chapter 30, "Success Typing"): given `convert(X)` where `fetch()` returns 1 or 2, Dialyzer stays silent because `convert/1` *could* succeed for some path — it does not prove the eventual failure.

## Relationships

## Builds Upon

- **Dialyzer** — Success typing is the inference algorithm Dialyzer is built around

## Related

- **Type specification** — `-spec` signatures supplement success typing as hints
- **Dialyzer warning** — Warnings are emitted only when a use violates the success typing

## Common Errors

- **Error**: Reordering calls so a correct one runs before a buggy one and assuming the code is fine because Dialyzer is silent
  **Correction**: Once a call succeeds in a code unit, Dialyzer may ignore later errors there; silence is not proof of correctness

## Common Confusions

- **Confusion**: Thinking success typing proves a program is type-safe
  **Clarification**: Success typing over-approximates and never cries wolf, but explicitly does *not* prove absence of errors

## Source Reference

Chapter 30: Type Specifications and Dialyzer, section "Success Typing" and the cautions in "Polymorphic Types."

## Verification Notes

- Definition: Direct adaptation from "Success Typing," including the quoted paper
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined and quoted from the source paper
- Cross-references: `dynamic-typing` is a shared slug from Agent 1
