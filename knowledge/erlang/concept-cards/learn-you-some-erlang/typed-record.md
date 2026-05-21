---
concept: Typed Record
slug: typed-record
category: data-types
subcategory: typespecs
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "Types for Records"
extraction_confidence: high
aliases:
  - "record type"
prerequisites:
  - type-specification
related:
  - type-annotation
  - dialyzer
contrasts_with: []
answers_questions:
  - "How do I give types to record fields?"
  - "What is a typed record in Erlang?"
---

# Typed Record

## Quick Definition

A typed record is an Erlang record whose field declarations include type specifications, letting Dialyzer check the values stored in each field.

## Core Definition

Records have a convenient syntax for declaring field types. The general record syntax for type declarations is `Field :: Type` within the record definition, and with a default value it becomes `Field = Default :: Type`. A record can itself be used as a type by writing it as `#RecordName{}`. To give type declarations a uniform style, programmers commonly add an alias such as `-type user() :: #user{}.`. If a field has no default value, all record field definitions get an implicit `'undefined'` union added to them, so creating a record without setting that field is not a type error (Chapter 30, "Types for Records").

## Prerequisites

- **Type specification** — Field types are written using declared and built-in types

## Key Properties

1. Field type syntax: `Field :: Type`, or `Field = Default :: Type` with a default
2. A record can be used as a type via `#RecordName{}`
3. A field with no default value implicitly gains an `'undefined'` union, so it may be unset without a type error
4. A record type is conventionally aliased as `-type name() :: #record{}.`
5. Field types may reference other declared types, including recursive ones and lists of the record itself
6. Earlier Erlang versions raised type errors for unset fields without defaults; the implicit `'undefined'` union avoids that

## Construction / Recognition

## To Type a Record

1. In the `-record` definition, append `:: Type` to each field (after `= Default` if present)
2. Optionally add `-type name() :: #record{}.` as an alias
3. Reference other declared types in field types as needed

## Context & Application

Typed records let Dialyzer verify the contents of structured data. The chapter's `#user{}` record stores a name (`string()`), notes (a `tree()`), age (`non_neg_integer()`), a friends list, and a biography (`string() | binary()`). The friends field can be `[#user{}]` or, with an alias, `[user()]` — showing a record both holding a list of itself and being usable as a named type.

## Examples

**Example** (Chapter 30, "Types for Records"):
`-record(user, {name = "" :: string(), notes :: tree(), age :: non_neg_integer(), friends=[] :: [user()], bio :: string() | binary()}).` with `-type user() :: #user{}.` — `#user{age=5}` causes no type error because unset fields gain an implicit `'undefined'`.

## Relationships

## Builds Upon

- **Type specification** — Field types are composed from declared and built-in types

## Related

- **Type annotation** — `-spec` signatures can use record types as argument/return types
- **Dialyzer** — Uses field types to check stored values

## Common Errors

- **Error**: Expecting a type error when creating a record without setting an untyped-default field
  **Correction**: Fields without defaults get an implicit `'undefined'` union, so leaving them unset is valid

## Common Confusions

- **Confusion**: Thinking a record name and its type must differ
  **Clarification**: A record is usable directly as a type via `#RecordName{}`; the `-type name() :: #record{}.` alias is just a stylistic convenience

## Source Reference

Chapter 30: Type Specifications and Dialyzer, section "Types for Records."

## Verification Notes

- Definition: Direct adaptation from "Types for Records"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined with the `#user{}` example
- Cross-references: verified against planned cards in this extraction
