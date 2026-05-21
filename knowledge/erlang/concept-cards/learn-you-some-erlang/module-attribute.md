---
concept: Module Attribute
slug: module-attribute
category: tooling
subcategory: code-organization
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Modules"
chapter_number: 2
pdf_page: null
section: "Creating Modules"
extraction_confidence: high
aliases:
  - "attribute"
  - "module metadata"
prerequisites:
  - module
  - atom
extends: []
related:
  - function-export
  - compiler-options
  - macro
contrasts_with: []
answers_questions:
  - "What is a module?"
---

# Module Attribute

## Quick Definition

A module attribute is metadata describing the module itself — its name, exported functions, author, and so on. Attributes follow the form `-Name(Attribute).`.

## Core Definition

Attributes are metadata describing the module itself, such as its name, the functions visible outside, and the author. This metadata gives hints to the compiler and lets people retrieve information from compiled code without consulting the source. All module attributes follow the form `-Name(Attribute).`. Only `-module(Name)` is mandatory for a module to compile. Custom attributes are allowed; the compiler stores most of them, accessible via the generated `module_info/0` and `module_info/1` functions (Hébert, ch. 2, "Creating Modules" and "Metadata").

## Prerequisites

- **Module** — Attributes are declared inside a module file
- **Atom** — Attribute names and many attribute values are atoms

## Key Properties

1. Syntax: `-Name(Attribute).`.
2. `-module(Name)` is the only required attribute and must come first.
3. Common attributes include `-export`, `-import`, `-compile`, `-vsn`, and `-author`.
4. Programmers may declare custom attributes.
5. Most attributes are stored by the compiler and retrievable via `module_info/0` / `module_info/1`.
6. `vsn` is an auto-generated unique value identifying a code version, used in hot code loading.

## Construction / Recognition

To add a module attribute, write `-Name(Value).` near the top of the module file, after `-module`.

## Context & Application

Module attributes have limited use in production code but are handy for tooling — for example, the book's testing script reads custom attributes to flag functions needing better tests. The `vsn` attribute supports hot-loading and release handling.

## Examples

**Example** (ch. 2): `useless:module_info(attributes).` returns `[{vsn,[174839656007867314473085021121413256129]}]`.

**Example** (ch. 2): Adding `-author("An Erlang Champ").` stores the author alongside `vsn` in the attributes section.

## Relationships

### Prerequisites

- **Module** — Attributes live in a module
- **Atom** — Attribute names are atoms

### Related

- **Function export** — `-export` is a module attribute
- **Compiler options** — `-compile` is a module attribute that sets compile flags
- **Macro** — `-define` is a module attribute that declares macros

## Common Errors

- **Error**: Placing `-module` anywhere but first
  **Correction**: `-module` must be the first attribute and statement of the file

## Common Confusions

- **Confusion**: Thinking attributes are runtime code
  **Clarification**: Attributes are compile-time metadata, not executable expressions

## Source Reference

Chapter 2: "Modules," sections "Creating Modules" and "Metadata."

## Verification Notes

- Definition: Adapted from the attributes discussion in chapter 2
- Confidence: HIGH — explicit treatment
- Uncertainties: None
