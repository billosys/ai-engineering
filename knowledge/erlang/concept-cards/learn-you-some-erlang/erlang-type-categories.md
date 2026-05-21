---
concept: Erlang Type Categories
slug: erlang-type-categories
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
  - "singleton type"
  - "built-in type"
  - "union type"
prerequisites:
  - type-specification
related:
  - type-annotation
  - dialyzer
contrasts_with: []
answers_questions:
  - "What kinds of types does Erlang's type language provide?"
  - "What is a singleton type vs a built-in type vs a union type?"
---

# Erlang Type Categories

## Quick Definition

Erlang's type language is built from three categories: singleton types (literal values), built-in types (predefined types like `integer()`), and union types (alternatives joined with `|`).

## Core Definition

Erlang types come in three categories used to build type specifications. *Singleton types* refer to a value itself — any atom (`'some atom'`), a given integer (`42`), an empty list (`[]`), empty tuple (`{}`), or empty binary (`<<>>`). *Built-in types* are predefined types, generally written `TypeName()` (e.g., `integer()`, `atom()`, `pid()`, `any()`, `none()`), some with special syntax for binaries, tuples, lists, and funs. *Union types* combine alternatives with the pipe (`|`): `TypeName` is the union `Type1 | Type2 | ... | TypeN`. The parentheses on built-in types distinguish, e.g., `atom()` (all atoms) from `atom` (the specific atom) (Chapter 30, "Typing About Types of Types").

## Prerequisites

- **Type specification** — These categories are the building blocks of `-type` declarations

## Key Properties

1. Singleton types are individual values: `'atom'`, `42`, `[]`, `{}`, `<<>>`
2. Built-in types are predefined, written `TypeName()`: `any()`, `none()`, `pid()`, `port()`, `reference()`, `atom()`, `binary()`, `integer()`, `float()`, `fun()`, `tuple()`, etc.
3. `none()` means no term is valid — a function whose return boils down to `none()` should crash
4. Integer ranges (`N..M`) and refinements (`non_neg_integer()`, `pos_integer()`, `neg_integer()`) are built-in
5. Union types join alternatives with `|`; a single-alternative "union" is an alias
6. Many unions/aliases are predefined: `term()` (= `any()`), `boolean()` (`'true' | 'false'`), `byte()` (`0..255`), `number()` (`integer() | float()`), `string()` (`[char()]`), `iolist()`, `module()`, `timeout()`, `node()`, `no_return()`
7. Parentheses distinguish a built-in type `atom()` from the singleton atom `atom`

## Construction / Recognition

## To Choose a Type

1. Use a singleton when the value must be exactly one literal
2. Use a built-in type for a general category (`integer()`, `pid()`, ...)
3. Combine alternatives into a union with `|` when several types are valid
4. Prefer a predefined union/alias (`number()`, `boolean()`) where one exists

## Context & Application

These categories make type specifications expressive: singleton types alone could not describe "any integer," and built-in plus union types fill that gap. The chapter notes `number()` is itself a predefined union (`integer() | float()`), and that quoting singleton atoms (`'atom'`) makes it explicit they are not built-in types missing their parentheses.

## Examples

**Example** (Chapter 30, "Union and Built-in Types"): `number()` can be written `integer() | float()`; a Boolean is `'true' | 'false'`.

**Example** (Chapter 30, Table 30-2): a binary tree node typed as `{'node', any(), any(), any(), any()}`; a list of integers as `[integer()]` or `list(integer())`.

## Relationships

## Builds Upon

- **Type specification** — Singleton, built-in, and union types are what `-type` declarations are composed from

## Related

- **Type annotation** — `-spec` signatures reference these type categories
- **Dialyzer** — Reasons in terms of these types when inferring success typings

## Common Errors

- **Error**: Writing `atom` when you mean all atoms
  **Correction**: All atoms is the built-in `atom()`; `atom` is the singleton — keep the parentheses

## Common Confusions

- **Confusion**: Thinking `none()` is a normal value type
  **Clarification**: `none()` means "no term is valid"; when a function's return reduces to `none()`, it means the function should crash

## Source Reference

Chapter 30: Type Specifications and Dialyzer, section "Typing About Types of Types" (subsections "Singleton Types," "Union and Built-in Types"), Tables 30-1, 30-2, 30-3.

## Verification Notes

- Definition: Direct adaptation from "Typing About Types of Types"
- Key Properties: All explicit in the chapter and its tables
- Confidence: HIGH — the three categories are explicitly named and tabulated
- Cross-references: verified against planned cards in this extraction
