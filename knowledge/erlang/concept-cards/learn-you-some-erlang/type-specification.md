---
concept: Type Specification
slug: type-specification
category: data-types
subcategory: typespecs
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "Typing About Types of Types"
extraction_confidence: high
aliases:
  - "typespec"
  - "type definition"
  - "-type"
prerequisites:
  - dynamic-typing
related:
  - type-annotation
  - dialyzer
  - polymorphic-type
  - opaque-type
  - typed-record
contrasts_with: []
answers_questions:
  - "What is a type specification?"
  - "How do I declare types in Erlang?"
---

# Type Specification

## Quick Definition

A type specification is an Erlang type declaration — written with `-type` — that names and defines a type out of singleton, built-in, and union types, for documentation and Dialyzer analysis.

## Core Definition

To help Dialyzer and to formalize the implicit type expectations in code, Erlang lets you declare types with the module attribute `-type TypeName() :: TypeDefinition.`. Type definitions are built from *singleton types* (a literal value such as `42` or `'cat'`), *built-in types* (predefined types written `TypeName()`, such as `integer()` or `pid()`), and *union types* (combinations joined with the pipe `|`, such as `integer() | float()`). A type defined in terms of a single other type is an *alias*. Many aliases and unions are predefined (e.g., `number()`, `boolean()`, `string()`, `iolist()`). Dialyzer supports recursive type definitions (since R13B04) (Chapter 30, "Typing About Types of Types").

## Prerequisites

- **Dynamic typing** — Type specifications add optional, explicit type information to a dynamically typed language

## Key Properties

1. Declared with `-type TypeName() :: TypeDefinition.`
2. Built from singleton types (literal values), built-in types (`integer()`, `atom()`, etc.), and union types
3. Union types join alternatives with the pipe: `integer() | float()`
4. A single-alternative type is an alias (e.g., `term()` aliases `any()`)
5. Variable names may annotate parts of a definition as comments: `{'node', Left::tree(), Right::tree()}`
6. Type definitions may be recursive (Dialyzer supports it since R13B04)
7. Types can be exported with `-export_type([TypeName/Arity]).` and referenced elsewhere as `module:type()`
8. Declaring types alone does not affect Dialyzer's inference — they must be attached to functions via `-spec`

## Construction / Recognition

## To Declare a Type

1. Pick a name and write `-type name() :: definition.`
2. Compose the definition from singleton, built-in, and union types
3. For recursive structures, refer to the type within its own definition
4. Export it with `-export_type([name/0]).` if other modules need it

## Context & Application

Type specifications serve as documentation and feed Dialyzer's analysis when attached to functions. The chapter defines a binary tree as `-type tree() :: {'node','nil'} | {'node', Key::any(), Val::any(), Left::tree(), Right::tree()}.` — a recursive union. Card games are modeled with `-type suit() :: spades | clubs | hearts | diamonds.`, `-type value() :: 1..10 | j | q | k.`, and `-type card() :: {suit(), value()}.`

## Examples

**Example** (Chapter 30, "Typing Functions"): `-type card() :: {suit(), value()}.` combines two union types into a tuple type.

**Example** (Chapter 30, "Exporting Types"): adding `-export_type([card/0]).` to the `cards` module lets other modules reference `cards:card()` in their specs.

## Relationships

## Related

- **Type annotation** — `-spec` signatures attach declared types to functions
- **Dialyzer** — Consumes type specifications to sharpen analysis
- **Polymorphic type** — Type specifications parameterized by another type
- **Opaque type** — A type exported so others cannot inspect its internals
- **Typed record** — Records given field-level type specifications

## Common Errors

- **Error**: Declaring types and expecting Dialyzer to use them automatically
  **Correction**: A bare `-type` does not affect inference; attach it to functions with `-spec`

## Common Confusions

- **Confusion**: Confusing the singleton type `atom` with the built-in type `atom()`
  **Clarification**: `atom` is the specific atom; `atom()` is all atoms — many programmers quote singletons (`'atom'`) to make the distinction explicit

## Source Reference

Chapter 30: Type Specifications and Dialyzer, section "Typing About Types of Types" (subsections "Singleton Types," "Union and Built-in Types," "Defining Types"), and "Exporting Types."

## Verification Notes

- Definition: Direct adaptation from "Typing About Types of Types"
- Key Properties: All explicit in the chapter, including Tables 30-1, 30-2, 30-3
- Confidence: HIGH — extensively defined with examples
- Cross-references: `dynamic-typing` is a shared slug from Agent 1; canonical slug `type-specification` per extraction instructions
