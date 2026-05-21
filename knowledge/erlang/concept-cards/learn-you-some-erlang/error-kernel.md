---
concept: Error Kernel
slug: error-kernel
category: fault-tolerance
subcategory: design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building an Application"
chapter_number: 18
pdf_page: null
section: "The Onion Layer Theory"
extraction_confidence: high
aliases:
  - error kernel
prerequisites:
  - supervision-tree
extends: []
related:
  - onion-layered-design
  - supervision-tree
contrasts_with: []
answers_questions:
  - "How do supervisors relate to the \"let it crash\" philosophy?"
  - "What concepts precede building an OTP application?"
---

# Error Kernel

## Quick Definition

The error kernel is the part of an application where you are not allowed to fail — the safest core holding the most vital, hardest-to-recompute data.

## Core Definition

"The idea is that the most important data (or the data that is most annoying to lose) must be the most protected type. The place where you are actually not allowed to fail is called the *error kernel* of your application" (Ch. 18, "The Onion Layer Theory").

## Prerequisites

- **Supervision tree** — The error kernel is realised as the well-protected core of a supervision tree.

## Key Properties

1. It holds the most vital, non-recomputable state.
2. It is the place "you want to be error-free."
3. It is where `try ... catch` is used most heavily, since exceptional cases must be handled there.
4. It requires careful testing, especially where there is no way to undo an operation.
5. Architecturally it sits closest to the root of the supervision tree.

## Construction / Recognition

## To Identify and Protect the Error Kernel

1. Find the data your application absolutely cannot afford to lose or corrupt.
2. Keep the operations on that data in the safest core, near the supervision-tree root.
3. Push risky, failure-prone operations into deeper, outer layers.
4. Use `try ... catch` and thorough testing around the kernel.

## Context & Application

The book distinguishes three kinds of state: static state (easily refetched from a supervisor or config), dynamic recomputable state (rebuildable on restart), and dynamic non-recomputable state (user input, live data, irreversible event sequences). The error kernel is concerned with the third kind. The classic example: "You don't want to lose a customer's order halfway through processing it."

In the `ppool` design, isolating each pool's worker supervisor so a log-files pool crashing cannot drown out a sockets pool is "one example of an error kernel being better defined."

## Examples

**Example 1** (Ch. 18): A customer's order being processed — losing it halfway is unacceptable, so that processing belongs in the error kernel.

**Example 2** (Ch. 18): In `ppool`, separating the sockets pool from the log-files pool keeps a failure in one from affecting the other's protected core.

## Relationships

## Builds Upon

- **Supervision tree** — The error kernel is the protected root region of the tree.

## Related

- **onion-layered-design** — The design principle that produces a well-defined error kernel.

## Common Errors

- **Error**: Placing irreversible, non-recomputable operations deep in a failure-prone subtree.
  **Correction**: Move them into the protected error kernel near the tree's root.

## Common Confusions

- **Confusion**: Thinking the error kernel means "code that never has bugs."
  **Clarification**: It means code that is *designed and tested to not fail* — heavily guarded, well-tested, and structurally protected — not magically bug-free.

## Source Reference

Chapter 18: "Building an Application," section "The Onion Layer Theory."

## Verification Notes

- Definition: Direct quote from "The Onion Layer Theory."
- Key Properties: Synthesised from the three-kinds-of-state discussion.
- Confidence: HIGH — the term is explicitly defined.
