---
# === CORE IDENTIFICATION ===
concept: Variable
slug: variable

# === CLASSIFICATION ===
category: core-idioms
subcategory: variables
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.4.1 Variable syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - variable syntax
  - underscore variable

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - single-assignment
  - pattern-matching
  - atom
  - anonymous-variable
contrasts_with:
  - atom

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are variables written in Erlang?"
  - "What does a leading underscore on a variable mean?"
  - "Why does the compiler warn about unused variables?"
---

# Quick Definition

An Erlang variable is a name for a value, written starting with an uppercase letter or an underscore. A leading underscore marks a variable as deliberately unused.

# Core Definition

"The most visible difference is that in Erlang, variables begin with an uppercase letter!" (Chapter 2, section 2.4.1) — names starting with lowercase are reserved for atoms. The normal style uses CamelCase, as in `Name`, `ShoeSize12`. A variable can also begin with an underscore; by convention the second character is then uppercase. There is a functional difference: the compiler normally warns when you assign a value to a variable and then never use it, which catches many silly mistakes. A variable starting with an underscore suppresses that warning — useful when a variable is present only to make the program more readable. Unused variables are optimized away and carry no cost.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A variable name begins with an uppercase letter or an underscore.
2. Names starting with a lowercase letter are atoms, not variables.
3. The normal style is CamelCase.
4. A leading underscore marks a variable as deliberately unused, suppressing the unused-variable warning.
5. The compiler warns about variables that are assigned but never used.
6. Unused variables are optimized away and carry no extra cost.

# Construction / Recognition

## To Identify/Recognize:
1. An uppercase-starting name (or underscore-starting) in source is a variable.
2. A lowercase-starting name is an atom.
3. `_SomeThing` is a named variable that suppresses the unused warning.

# Context & Application

- **Typical contexts**: All Erlang code that names values.
- **Common applications**: Binding parts of data structures via pattern matching; annotating code for readability with underscore variables.
- **Historical/stylistic notes**: The compiler's unused-variable warning is valuable; the book advises against turning it off.

# Examples

**Example 1** (section 2.4.1): `Z`, `Name`, `ShoeSize12`, `ThisIsARatherLongVariableName` are variables in CamelCase style.

**Example 2** (section 2.4.1): `_SomeThing`, `_X`, and `_this_may_look_like_an_atom_but_is_really_a_variable` are underscore-prefixed variables — they look like atoms but are variables, and the compiler will not warn if they are unused.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- **Single assignment** — variables follow single-assignment rules.
- **Pattern matching** — variables in patterns are bound to matched values.

## Related
- **Anonymous variable** — the `_` placeholder is related to underscore variables but is not a variable at all.

## Contrasts With
- **Atom** — lowercase-starting names are atoms; uppercase-starting names are variables.

# Common Errors

- **Error**: Starting a variable name with a lowercase letter.
  **Correction**: Lowercase-starting names are atoms; variables must start with uppercase or underscore.

- **Error**: Turning off the unused-variable warning to silence noise.
  **Correction**: Keep the warning; prefix deliberately unused variables with an underscore instead.

# Common Confusions

- **Confusion**: Reading an underscore-prefixed name as an atom.
  **Clarification**: `_this_looks_like_an_atom` is actually a variable; the leading underscore makes it a variable, not an atom.

# Source Reference

Chapter 2: Erlang language essentials, section 2.4.1 "Variable syntax."

# Verification Notes

- Definition source: Direct adaptation from section 2.4.1.
- Confidence rationale: HIGH — variable syntax and underscore conventions are explicitly described.
- Uncertainties: None.
- Cross-reference status: `anonymous-variable` is a planned card in this source.
- Re-extraction notes: Fresh extraction; no prior card.
