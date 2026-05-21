---
# === CORE IDENTIFICATION ===
concept: Atom
slug: atom

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Atom"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-term
  - boolean
  - string
  - tuple
contrasts_with:
  - string

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an atom in Erlang?"
  - "What distinguishes atoms from strings in Erlang?"
  - "How do atoms, tuples, and lists form the foundation of Erlang's type system?"
---

# Quick Definition
An atom is a literal constant with a name. It is a fundamental data type in Erlang used for symbolic identifiers and tags, and must be enclosed in single quotes if it does not begin with a lowercase letter or contains non-alphanumeric characters.

# Core Definition
The Erlang Reference Manual defines an atom as "a literal, a constant with a name." An atom must be enclosed in single quotes (`'`) if it does not begin with a lowercase letter or if it contains characters other than alphanumeric characters, underscore (`_`), or `@` (Data Types, "Atom" section). Atoms are used throughout Erlang as symbolic constants, module names, function names, record tags, and message tags.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. A literal constant with a name -- immutable and self-evaluating
2. Does not need quoting if it starts with a lowercase letter and contains only alphanumeric characters, `_`, or `@`
3. Must be enclosed in single quotes if it starts with an uppercase letter, a digit, or contains special characters
4. Atoms are not strings -- they are a distinct data type
5. Atom comparison is efficient (constant-time equality check)
6. Atoms are stored in a global atom table; creating atoms dynamically (e.g., from user input via `list_to_atom/1`) should be done with care

# Construction / Recognition
## To Construct/Create:
1. Write an unquoted atom starting with a lowercase letter: `hello`, `phone_number`, `name@node`
2. Write a quoted atom for special cases: `'Monday'`, `'phone number'`, `'hello world'`
3. Convert from string: `list_to_atom("hello")` or `binary_to_atom(<<"hello">>)`

## To Identify/Recognize:
1. Use `is_atom/1` BIF to test whether a term is an atom
2. Atoms appear as bareword identifiers (starting with lowercase) or single-quoted strings in source code

# Context & Application
Atoms are one of the most pervasive types in Erlang. They serve as:
- Module and function names
- Record tag names (first element of tuple-based records)
- Message tags in pattern matching (`{ok, Value}`, `{error, Reason}`)
- Boolean values (`true` and `false` are atoms)
- Process signal types (`exit`, `kill`)

Atoms are central to Erlang's philosophy of "let it crash" -- pattern matching on atoms enables clear control flow through tagged tuples.

# Examples
**Example 1** (Data Types, "Atom" section):
```text
hello
phone_number
name@node
'Monday'
'phone number'
```

**Example 2** (Data Types, "Type Conversions" section):
```erlang
1> atom_to_list(hello).
"hello"
2> list_to_atom("hello").
hello
```

# Relationships
## Builds Upon
This is a foundational type with no prerequisites.

## Enables
- **boolean** -- Booleans are the atoms `true` and `false`
- **tuple** -- Atoms are commonly used as the first element (tag) of tuples
- **record-definition** -- Record names and field names must be atoms
- **native-record-definition** -- Native record names and field names must be atoms

## Related
- **erlang-term** -- Atoms are a kind of term

## Contrasts With
- **string** -- Strings are lists of integer code points, not symbolic constants. Atoms are compared by identity; strings are compared character by character.

# Common Errors
- **Error**: Forgetting to quote atoms that start with uppercase or contain spaces
  **Correction**: Use single quotes: `'Monday'`, `'phone number'`

- **Error**: Dynamically creating atoms from untrusted input using `list_to_atom/1`
  **Correction**: Use `list_to_existing_atom/1` to prevent atom table exhaustion

# Common Confusions
- **Confusion**: Treating atoms and strings as interchangeable
  **Clarification**: Atoms are symbolic constants stored in a global table; strings are lists of integers. They serve different purposes and have different performance characteristics.

- **Confusion**: Believing atoms can be garbage collected
  **Clarification**: Once created, atoms persist in the atom table for the lifetime of the VM. This is why dynamic atom creation from user input is dangerous.

# Source Reference
Data Types chapter, "Atom" section.

# Verification Notes
- Definition source: Direct quote from source ("a literal, a constant with a name")
- Confidence rationale: High -- explicit definition in source
- Uncertainties: None; atom table exhaustion caution is well-known but not explicitly stated in this section
- Cross-reference status: All slugs correspond to planned cards
