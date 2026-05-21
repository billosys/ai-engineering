---
concept: Queue Module
slug: queue-module
category: data-types
subcategory: collections
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "Queues"
extraction_confidence: high
aliases:
  - "queue"
  - "FIFO queue"
prerequisites: []
extends: []
related:
  - array-module
contrasts_with: []
answers_questions:
  - "What is the queue module?"
  - "When should I use a queue instead of a list?"
---

# Queue Module

## Quick Definition

The `queue` module implements a double-ended FIFO queue, built from two lists so elements can be appended and removed efficiently. Use it when items must be processed in arrival order with frequent additions.

## Core Definition

The `queue` module "implements a double-ended first in, first out (FIFO) queue." It is built from two lists used as stacks: one list receives pushed values and the other supplies popped values; when the pop list empties, the push list is reversed to become the new pop list. This gives an efficient queue on the average of all operations over its lifetime, working around the fact that a single list is only fast at its head. The module's functions are split into three APIs: the *Original API* (`new/0`, `in/2`, `out/1`, plus conversions), the *Extended API* (introspection: `get/1`, `peek/1`, `drop/1`), and the *Okasaki API* (derived from Chris Okasaki's *Purely Functional Data Structures*, with backward-written function names — generally not worth using) (Hébert, ch. 9, "Queues").

## Prerequisites

This is a foundational data structure with no prerequisites within this chapter.

## Key Properties

1. A double-ended FIFO queue
2. Internally two lists (stacks): one for additions, one for removals
3. When the removal list empties, the addition list is reversed and becomes the new removal list
4. Efficient on the average of all operations over the queue's lifetime
5. Three APIs: Original (core), Extended (introspection), and Okasaki (peculiar, rarely used)
6. Best when you cannot do all reversing at once and elements are frequently added

## Construction / Recognition

## To Use a Queue

1. Create an empty queue: `queue:new()`
2. Insert an element: `queue:in(Item, Q)`
3. Remove the front element: `queue:out(Q)` → `{{value, Item}, Q2}` or `{empty, Q}`
4. Inspect without removing: `queue:peek(Q)` or `queue:get(Q)`
5. Convert to/from lists: `queue:to_list/1`, `queue:from_list/1`

## Examples

> **Three APIs** (ch. 9): Original (`new/0`, `in/2`, `out/1`), Extended (`get/1`, `peek/1`, `drop/1`), and the Okasaki API with backward function names.
>
> **When to use** (ch. 9): "use queues when you need to ensure that the first item ordered is indeed the first one processed... In cases where you can't just do all the reversing at once, and elements are frequently added."

## Relationships

## Related

- **Array module** — Another specialized standard data structure described in the same chapter

## Common Errors

- **Error**: Using `out/1` and not handling the empty case
  **Correction**: `out/1` returns `{empty, Q}` on an empty queue; match for it
- **Error**: Reaching for the Okasaki API by default
  **Correction**: Use the Original/Extended APIs; the Okasaki API is peculiar and rarely needed

## Common Confusions

- **Confusion**: Thinking a plain list is just as good
  **Clarification**: A list is fast only at its head; the `queue` module's two-list design makes both ends efficient

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Queues."

## Verification Notes

- Definition, two-list design, three APIs: directly from ch. 9
- Confidence: HIGH — explicitly described
