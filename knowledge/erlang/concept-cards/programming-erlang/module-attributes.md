---
# === CORE IDENTIFICATION ===
concept: Module Attributes
slug: module-attributes

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-module"
  - "-export"
  - "-import"
  - "-compile"
  - "-vsn"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arity
extends: []
related:
  - module-info
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are module attributes?"
  - "What is the difference between predefined and user-defined attributes?"
  - "How do I extract a module's attributes?"
---

# Quick Definition

Module attributes are declarations of the form `-AtomTag(...)` that define properties of a source file; some are predefined (`-module`, `-export`, `-import`, `-compile`, `-vsn`) and others are user-defined.

# Core Definition

"Module attributes have the syntax `-AtomTag(...)` and are used to define certain properties of a file" ("The Rest of Sequential Erlang", *Attributes*). There are two types: predefined and user-defined. Predefined attributes must precede any function definitions and include `-module(modname)` (the module declaration — must be the first attribute), `-import(Mod, [Name1/Arity1, ...])` (imports functions so they can be called without the module qualifier), `-export([Name1/Arity1, ...])` (makes functions callable from outside the module), `-compile(Options)` (adds compiler options), and `-vsn(Version)` (a module version, any literal term). A user-defined attribute has the syntax `-SomeTag(Value)`, where `SomeTag` is an atom and `Value` is a literal term; these are compiled into the module and can be extracted at runtime. Note that `-record(...)` and `-include(...)` use a similar syntax but are *not* considered module attributes.

# Prerequisites

- **Arity** — `-export` and `-import` lists refer to functions by `Name/Arity`.

# Key Properties

1. Syntax is `-AtomTag(...)`.
2. Predefined attributes must appear before any function definitions.
3. `-module` must be the first attribute; `modname` should match the filename `modname.erl`.
4. `-import` lets imported functions be called without a module qualifier.
5. `-export` makes the listed functions callable from outside the module.
6. `-compile(export_all)` exports all functions — common when debugging.
7. User-defined attribute values are compiled in and retrievable via `module_info` or `beam_lib`.
8. `-record(...)` and `-include(...)` are not module attributes despite the similar syntax.

# Construction / Recognition

## To Construct/Create:
1. Place `-module(name).` first, then `-export([...]).`, optional `-import`, `-compile`, `-vsn`.
2. Add user-defined attributes such as `-author({joe,armstrong}).` or `-purpose("...").`.

## To Identify/Recognize:
1. `Mod:module_info()` returns a property list of module metadata; `Mod:module_info(X)` returns a specific part.
2. `beam_lib:chunks("mod.beam", [attributes])` extracts attributes without loading the module.

# Context & Application

- **Typical contexts**: the header of every Erlang source module.
- **Common applications**: `-compile(export_all)` while debugging; user-defined attributes for documentation or analysis tooling.
- **Historical/stylistic notes**: `module_info/0` and `module_info/1` are automatically created for every compiled module.

# Examples

**Example 1** (*Attributes*): a module with user-defined attributes:

```erlang
-module(attrs).
-vsn(1234).
-author({joe,armstrong}).
-purpose("example of attributes").
-export([fac/1]).

fac(1) -> 1;
fac(N) -> N * fac(N-1).
```

**Example 2** (*Attributes*): extracting attributes without loading the module:

```erlang
3> beam_lib:chunks("attrs.beam",[attributes]).
{ok,{attrs,[{attributes,[{author,[{joe,armstrong}]},
            {purpose,"example of attributes"},
            {vsn,[1234]}]}]}}
```

# Relationships

## Builds Upon
- **Arity** — Export/import lists identify functions by arity.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **module_info** — The auto-generated functions that expose attributes at runtime.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Placing `-module` after another attribute or after a function.
  **Correction**: `-module` must be the first attribute, and all predefined attributes must precede function definitions.

- **Error**: Naming a module differently from its file.
  **Correction**: The code for `modname` should be in `modname.erl`, or automatic code loading will not work correctly.

# Common Confusions

- **Confusion**: Believing `-record` and `-include` are module attributes.
  **Clarification**: They share the `-tag(...)` syntax but are not considered module attributes.

- **Confusion**: Confusing the `-vsn` attribute with the compiler version in `{compile, ...}`.
  **Clarification**: `{version,"4.8"}` is the compiler version; `vsn` is the user-supplied module version.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Attributes" (Predefined Module Attributes, User-Defined Attributes).

# Verification Notes

- Definition source: Direct adaptation of the *Attributes* section.
- Confidence rationale: HIGH — the source explicitly defines each predefined and user-defined attribute with examples.
- Uncertainties: None.
- Cross-reference status: Slug `arity` extracted in this chapter; `module-info` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
