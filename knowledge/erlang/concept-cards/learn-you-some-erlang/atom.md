---
concept: Atom
slug: atom
category: data-types
subcategory: primitive-types
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Atoms"
extraction_confidence: high
aliases:
  - "literal"
  - "constant"
prerequisites: []
extends: []
related:
  - tuple
  - boolean-and-comparison-operators
  - variable
contrasts_with:
  - binary-string
answers_questions:
  - "What is an atom?"
---

# Atom

## Quick Definition

An atom is a literal constant whose only value is its own name. Atoms are used to express or qualify data without needing an underlying numeric value.

## Core Definition

Atoms are literals — constants whose only value is their own name. "What you see is what you get": the atom `cat` means `cat` and nothing more. An atom is written as a single word starting with a lowercase letter, or, if it does not begin with a lowercase letter or contains characters other than alphanumerics, `_`, or `@`, it must be enclosed in single quotes (`'`). A quoted atom is identical to the same atom unquoted (Hébert, ch. 1, "Atoms").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. An atom's value is its own name.
2. Written lowercase-leading, or single-quoted otherwise (e.g., `'Atoms can be cheated!'`).
3. Atoms are stored in a global atom table that consumes memory (4 bytes per atom on 32-bit, 8 on 64-bit) and is not garbage collected.
4. There is a hard limit of 1,048,577 atoms; atoms should never be generated dynamically.
5. `true` and `false` are atoms, not a distinct Boolean type.
6. Some atoms are reserved words (`after`, `and`, `case`, `fun`, `if`, `receive`, etc.) and cannot be used freely.

## Construction / Recognition

To write an atom:

1. If it starts with a lowercase letter and contains only alphanumerics, `_`, or `@`, write it bare (e.g., `atoms_rule@erlang`).
2. Otherwise, enclose it in single quotes.

## Context & Application

Atoms replace named constants (e.g., eye colors `blue`, `brown`, `green`) so the programmer never deals with underlying integer values, and such constants can never clash or be undefined. Atoms are mainly useful coupled with other data, typically tagging a tuple. They are extremely light for message passing.

## Examples

**Example** (ch. 1): `atom = 'atom'.` returns `atom`, showing quoted and unquoted forms are equal.

**Example** (ch. 1): A tagged tuple `{celsius, 23.213}` uses the atom `celsius` to qualify the numeric value.

## Relationships

### Related

- **Tuple** — Atoms are most useful as tags inside tuples
- **Boolean and comparison operators** — `true` and `false` are atoms
- **Variable** — Variables start uppercase precisely so lowercase names can be atoms

### Contrasts With

- **Binary string** — Use atoms (not binary strings) to tag values, since atoms compare in constant time

## Common Errors

- **Error**: Generating atoms dynamically from user input
  **Correction**: Never create atoms dynamically; the atom table fills up and crashes the system

## Common Confusions

- **Confusion**: Treating `true`/`false` as a distinct Boolean type
  **Clarification**: They are ordinary atoms, integrated into the language as Boolean values

## Source Reference

Chapter 1: "Starting Out," section "Atoms," including the "Don't Drink Too Much Kool-Aid" sidebar.

## Verification Notes

- Definition: Adapted from the "Atoms" section
- Confidence: HIGH — explicit definition with sidebar caveats
- Uncertainties: None
