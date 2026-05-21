---
concept: Polymorphic Type
slug: polymorphic-type
category: data-types
subcategory: typespecs
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "Polymorphic Types"
extraction_confidence: high
aliases:
  - "parameterized type"
  - "parametric type"
prerequisites:
  - type-specification
  - type-annotation
related:
  - dialyzer
  - opaque-type
contrasts_with: []
answers_questions:
  - "What is a polymorphic type in Erlang?"
  - "How do I make a generic data structure carry a specific element type?"
---

# Polymorphic Type

## Quick Definition

A polymorphic type is an Erlang type parameterized by another type, letting a generic data structure be specialized to hold only a particular element type.

## Core Definition

A polymorphic type (also called a *parameterized type*) is a type that can be "configured" with other types — it accepts a type as an argument. The need arises when typing data structures: you may want a queue to sometimes hold anything, sometimes only integers, sometimes only cards, and to have Dialyzer complain if the wrong element type is used. The syntax is already familiar — `[integer()]` and `list(integer())` are polymorphic types. A custom polymorphic type is declared with type variables, e.g., `-type queue(Type) :: {fifo, list(Type), list(Type)}.`, and exported as `-export_type([queue/1]).`. When another module uses it, it parameterizes the type, as in `-spec new() -> fifo:queue(card()).` (Chapter 30, "Polymorphic Types").

## Prerequisites

- **Type specification** — A polymorphic type is a parameterized `-type` declaration
- **Type annotation** — Polymorphic types are used in `-spec` signatures with a concrete parameter

## Key Properties

1. A type declared with one or more type variables as parameters
2. Built-in examples already exist: `[Type()]`, `list(Type())`
3. Declared as `-type name(TypeVar) :: definition-using-TypeVar.`
4. Exported with its arity: `-export_type([name/1]).`
5. A consuming module parameterizes it with a concrete type (e.g., `fifo:queue(card())`)
6. A free type variable `A` in a definition is resolved when the type is parameterized
7. Lets Dialyzer detect wrong element types (e.g., a float in an integer queue)

## Construction / Recognition

## To Define a Polymorphic Type

1. Declare it with type-variable parameters: `-type food(A) :: fun(() -> A).`
2. Export it with its arity: `-export_type([food/1]).`
3. In `-spec` signatures, parameterize it with concrete types: `food(red_panda())`, `food(squid())`

## Context & Application

Polymorphic types let Dialyzer enforce element-type correctness in otherwise generic structures. The chapter's `zoo.erl` example types an animal feeder with `-type food(A) :: fun(() -> A).` and specs `feed_red_panda(food(red_panda())) -> red_panda()` and `feed_squid(food(squid())) -> squid()`, so feeding a squid with a red panda's feeder is caught. The author cautions (per Dialyzer's optimism): if a function is first called correctly within a code unit, Dialyzer may ignore a later wrong call in the same unit.

## Examples

**Example** (Chapter 30, "We Bought a Zoo"): with `-type food(A) :: fun(() -> A).`, Dialyzer reports that `feed_squid(FeederRP)` cannot be right because the inferred return is the red panda's food, not `squid()`.

**Example** (Chapter 30, "Polymorphic Types"): `-type queue(Type) :: {fifo, list(Type), list(Type)}.` lets a `cards` module declare `-spec new() -> fifo:queue(card()).`

## Relationships

## Builds Upon

- **Type specification** — A polymorphic type is a parameterized type declaration
- **Type annotation** — Parameterized types are consumed in `-spec` signatures

## Related

- **Dialyzer** — Uses polymorphic types to check element-type correctness
- **Opaque type** — Polymorphic types can also be exported and made opaque

## Common Errors

- **Error**: Calling a function with the right kind of value first and assuming a later wrong call will be caught
  **Correction**: Once a call succeeds in a code unit, Dialyzer (as of R15B01) may ignore subsequent errors there

## Common Confusions

- **Confusion**: Thinking polymorphic types need exotic new syntax
  **Clarification**: `[integer()]` and `list(integer())` are already polymorphic; custom ones just add type-variable parameters

## Source Reference

Chapter 30: Type Specifications and Dialyzer, section "Polymorphic Types" (subsections "We Bought a Zoo," "Some Cautions").

## Verification Notes

- Definition: Direct adaptation from "Polymorphic Types"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined with the zoo example
- Cross-references: verified against planned cards in this extraction
