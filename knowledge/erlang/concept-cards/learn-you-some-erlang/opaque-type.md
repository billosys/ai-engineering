---
concept: Opaque Type
slug: opaque-type
category: data-types
subcategory: typespecs
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "Exporting Types"
extraction_confidence: high
aliases:
  - "-opaque"
  - "abstract data type"
prerequisites:
  - type-specification
related:
  - type-annotation
  - dialyzer
contrasts_with:
  - typed-record
answers_questions:
  - "What is an opaque type in Erlang?"
  - "How do I hide a type's implementation from other modules?"
---

# Opaque Type

## Quick Definition

An opaque type is an exported Erlang type whose internal structure only its defining module may inspect, so other modules cannot pattern match on or depend on its representation.

## Core Definition

Types are exported with `-export_type([TypeName/Arity])`, and any module that can see the type may then reference it as `module:type()`. The downside is that other modules can rip the type apart and pattern match on its internals, preventing the defining module from later changing the implementation. To prevent this, you replace a `-type` declaration with an `-opaque` declaration (e.g., `-opaque fifo() :: {fifo, list(), list()}.`) and still export it. Declaring a type `-opaque` means only the module that defined it may look at how it is made or modify it; other modules are forbidden from pattern matching on anything but the whole value, guaranteeing (if they use Dialyzer) that a change of implementation will not bite them (Chapter 30, "Exporting Types").

## Prerequisites

- **Type specification** — An opaque type is a type declaration variant of `-type`

## Key Properties

1. Declared with `-opaque TypeName() :: Definition.` instead of `-type`
2. Still exported with `-export_type([TypeName/Arity])`
3. Only the defining module may inspect or modify the type's internal structure
4. Other modules may pass the value around but not pattern match on its internals
5. Protects the defining module's freedom to change the representation later
6. Especially appropriate for modules representing data structures (e.g., `dict`, a fifo)
7. Dialyzer's opaque-type support can be confused by overly generic types; tagging the tuple often helps

## Construction / Recognition

## To Make a Type Opaque

1. Write `-opaque name() :: definition.` instead of `-type name() :: definition.`
2. Export it with `-export_type([name/0]).`
3. If Dialyzer reports spurious contract breaches, tag the tuple (e.g., `{card, suit(), value()}` instead of `{suit(), value()}`)

## Context & Application

Opaque types enforce abstraction: they tell users "I'm fine with you using my type, but don't look inside." This is valuable for data-structure modules so internal changes do not break clients. The chapter cautions that Dialyzer does not consider a function's `-spec` until it has first inferred the success typing, so an opaque type may be seen as overly generic (e.g., `{atom(), any()}`) and cause false "breaks a type contract" warnings; tagging the tuple usually resolves this. Improving opaque-type inference was a work in progress at the time of writing.

## Examples

**Example** (Chapter 30, "Exporting Types"): replacing `-type fifo() :: {fifo, list(), list()}.` with `-opaque fifo() :: {fifo, list(), list()}.` lets the fifo module export the type while forbidding clients from pattern matching on its internals.

## Relationships

## Builds Upon

- **Type specification** — Opaque is a variant of the `-type` declaration

## Related

- **Type annotation** — Opaque types are used as argument/return types in `-spec` signatures
- **Dialyzer** — Enforces opacity and may need help (tagged tuples) to infer opaque types correctly

## Contrasts With

- **Typed record** — A typed record exposes its fields for pattern matching; an opaque type deliberately hides its representation

## Common Errors

- **Error**: Pattern matching on an opaque type's internals from another module
  **Correction**: Only the defining module may inspect the representation; treat the value as a whole elsewhere

## Common Confusions

- **Confusion**: Thinking `-opaque` changes runtime behavior
  **Clarification**: Opacity is a Dialyzer-enforced abstraction guarantee; it does not change how the value behaves at runtime

## Source Reference

Chapter 30: Type Specifications and Dialyzer, section "Exporting Types" (including the "Don't Drink Too Much Kool-Aid" sidebar).

## Verification Notes

- Definition: Direct adaptation from "Exporting Types"
- Key Properties: All explicit in the chapter, including the inference caveat
- Confidence: HIGH — explicitly defined with the fifo example
- Cross-references: verified against planned cards in this extraction
