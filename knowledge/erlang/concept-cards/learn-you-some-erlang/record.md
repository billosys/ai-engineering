---
concept: Record
slug: record
category: data-types
subcategory: compound-data
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "Records"
extraction_confidence: high
aliases:
  - "Erlang record"
  - "-record attribute"
prerequisites:
  - pattern-matching
extends: []
related:
  - key-value-store
contrasts_with:
  - proplist
answers_questions:
  - "What is a record?"
  - "How do records relate to tuples?"
  - "How do I read and update fields of a record?"
---

# Record

## Quick Definition

A record is compiler syntactic sugar over a tagged tuple that lets you access fields by name. It is declared with `-record(Name, {Field1, Field2=Default, ...})` and behaves much like a struct in C.

## Core Definition

Records are described in the chapter as "first of all, a hack" — an afterthought to the language. A record is declared as a module attribute, e.g. `-record(robot, {name, type=industrial, hobbies, details=[]})`. Fields may have default values; fields without a default and not set at construction default to the atom `undefined`. Under the hood a record is just a tuple whose first element is the record name, so `#robot{...}` expands to `{robot, ...}`. The shell command `rr(Module)` loads record definitions so records print in record syntax rather than as raw tuples (Hébert, ch. 9, "Records").

## Prerequisites

- **Pattern matching** — Records can be used in function heads and guards to bind specific fields

## Key Properties

1. Declared as a module attribute: `-record(Name, {Fields...})`
2. Fields may carry default values; unset fields with no default become `undefined`
3. A record is internally a tuple `{Name, Field1, ..., FieldN}` — pure compiler trickery
4. Instances are created with `#Name{field=Value, ...}`
5. Field access uses dot syntax: `Var#Name.field`; `#Name.field` alone yields the tuple position index
6. Updates use `Var#Name{field=NewValue}`, which expands to `erlang:setelement/3`
7. Records can be matched in function heads and guards, binding only the fields you care about
8. Records can be shared across modules via `.hrl` header files included with `-include`

## Construction / Recognition

## To Define and Use a Record

1. Declare it: `-record(user, {id, name, group, age}).`
2. Create an instance: `#user{id=1, name="ferd", group=admin, age=96}`
3. Read a field: `U#user.age`
4. Update a field: `U#user{age=97}`
5. Match in a function head: `admin_panel(#user{name=Name, group=admin}) -> ...`
6. Bind the whole record while matching: `adult_section(U = #user{}) when U#user.age >= 18 -> ...`

## Examples

> **Declaration with defaults** (ch. 9): `-record(robot, {name, type=industrial, hobbies, details=[]}).`
>
> **Pattern matching on a field** (ch. 9): `admin_panel(#user{name=Name, group=admin})` matches only admin users; a second clause handles everyone else.
>
> **Nested record access** (ch. 9): `(NestedBot#robot.details)#robot.name` reaches into a record stored in another record's field.

## Relationships

## Related

- **Key-value store** — Records, like proplists, organize named data, but with fixed compile-time field names

## Contrasts With

- **Proplist** — A proplist has dynamic runtime keys and loose structure; a record has fixed compile-time fields and is a tuple

## Common Errors

- **Error**: Trying to match `S#state.server` as a pattern (e.g. in a `receive`)
  **Correction**: `S#state.field` expands to `element/2`, not a valid pattern; bind the field in the function head instead
- **Error**: Defining shared records in a project-wide `.hrl` and editing them freely
  **Correction**: The author recommends keeping record definitions local to one module and exposing accessor functions

## Common Confusions

- **Confusion**: Believing records are a distinct first-class data type
  **Clarification**: Records are syntactic sugar over tuples resolved entirely at compile time
- **Confusion**: Thinking an unset field is an error
  **Clarification**: An unset field with no declared default is silently set to `undefined`

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Records" (subsections "Defining Records," "Reading Values from Records," "Updating Records," "Sharing Records").

## Verification Notes

- Definition and behavior: directly from ch. 9 `records.erl` listings
- Internal tuple representation: explicit in the source ("Erlang records are just syntactic sugar on top of tuples")
- Confidence: HIGH — explicitly defined with multiple examples
