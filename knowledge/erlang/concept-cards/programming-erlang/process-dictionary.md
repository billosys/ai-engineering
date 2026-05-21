---
# === CORE IDENTIFICATION ===
concept: Process Dictionary
slug: process-dictionary

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-state
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "The Process Dictionary"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "put/get"
  - destructive process storage

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related: []
contrasts_with:
  - map

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the process dictionary?"
  - "How do I store and retrieve values in the process dictionary?"
  - "Why should the process dictionary be used sparingly?"
---

# Quick Definition

The process dictionary is each process's private, destructive associative store of key-value pairs, manipulated with `put`, `get`, `get_keys`, and `erase`.

# Core Definition

"Each process in Erlang has its own private data store called the *process dictionary*. The process dictionary is an associative array... composed of a collection of keys and values. Each key has only one value" ("The Rest of Sequential Erlang", *The Process Dictionary*). It is manipulated with BIFs: `put(Key, Value)` adds an association and returns the previous value (or `undefined`); `get(Key)` returns the value for `Key` (or `undefined`); `get()` returns the whole dictionary as a list of `{Key,Value}` tuples; `get_keys(Value)` returns the keys having that value; `erase(Key)` removes and returns a key's value; `erase()` clears the whole dictionary, returning its prior contents. "Variables in the process dictionary behave pretty much like conventional mutable variables in imperative programming languages" — so using it forfeits the benefits of side-effect-free, nondestructive variables. The book advises using it sparingly.

# Prerequisites

- **Process** — The dictionary belongs to a process; each process has its own.

# Key Properties

1. Each process has its own private process dictionary.
2. It is an associative array — each key maps to exactly one value.
3. `put/2` returns the old value (or `undefined`); `get/1` returns the value (or `undefined`).
4. `get/0` returns the whole dictionary; `erase/0` clears it and returns the prior contents.
5. `get_keys/1` returns keys having a given value; `erase/1` removes one key.
6. The dictionary provides destructive (mutable) storage — it breaks side-effect freedom.
7. The book recommends using it sparingly, and at most for write-once variables.

# Construction / Recognition

## To Construct/Create:
1. `put(x, 20)` stores a value.
2. `get(x)` retrieves it; `erase(x)` removes it.

## To Identify/Recognize:
1. Uses of `put/2`, `get/0,1`, `get_keys/1`, or `erase/0,1` indicate process-dictionary access.

# Context & Application

- **Typical contexts**: rare — for occasional destructive storage within a single process.
- **Common applications**: the book approves only of storing "write-once" variables — a key that acquires a value exactly once and never changes it.
- **Historical/stylistic notes**: the author states "I rarely use the process dictionary"; it can introduce subtle bugs and make programs hard to debug.

# Examples

**Example 1** (*The Process Dictionary*): basic put/get/erase:

```erlang
2> put(x, 20).
undefined
3> get(x).
20
5> put(y, 40).
undefined
7> get().
[{y,40},{x,20}]
8> erase(x).
20
9> get().
[{y,40}]
```

# Relationships

## Builds Upon
- **Process** — Each process owns one process dictionary.

## Enables
- This concept does not have downstream cards in scope.

## Related
- No directly related concept in scope.

## Contrasts With
- **Map** — A map is an immutable, value-passed associative structure; the process dictionary is per-process destructive storage that breaks side-effect freedom.

# Common Errors

- **Error**: Using the process dictionary for general mutable state across a program.
  **Correction**: Use it sparingly; prefer explicit nondestructive variables and pass state as arguments.

- **Error**: Storing a key in the process dictionary expecting another process to see it.
  **Correction**: The dictionary is private to each process; it is not shared.

# Common Confusions

- **Confusion**: Thinking the process dictionary is global or shared.
  **Clarification**: Each process has its own private dictionary.

- **Confusion**: Believing using the dictionary keeps code side-effect free.
  **Clarification**: Process-dictionary access is destructive; it forfeits the guarantees of nondestructive variables.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "The Process Dictionary".

# Verification Notes

- Definition source: Direct quotation and adaptation from *The Process Dictionary*.
- Confidence rationale: HIGH — the source defines the dictionary, every BIF, and the cautionary guidance.
- Uncertainties: None.
- Cross-reference status: Slug `process` assumed canonical; `map` extracted in this scope.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
