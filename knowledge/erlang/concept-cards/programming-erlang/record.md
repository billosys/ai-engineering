---
# === CORE IDENTIFICATION ===
concept: Record
slug: record

# === CLASSIFICATION ===
category: data-types
subcategory: compound-data
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Records and Maps"
chapter_number: 5
pdf_page: null
section: "Naming Tuple Items with Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-record"
  - record declaration
  - tagged tuple

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tuple
  - pattern-matching
extends:
  - tuple
related:
  - record-update
  - include-files
  - map
contrasts_with:
  - map

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a record?"
  - "How do records relate to tuples?"
  - "When should I use a record instead of a map?"
---

# Quick Definition

A record is a named, fixed-structure data type that lets you refer to the elements of a tuple by name instead of by position. Records are "tuples in disguise" — at runtime they are ordinary tuples.

# Core Definition

A record is declared with the `-record` attribute, which associates a name with a fixed set of named fields, each of which may have a default value. The declaration has the form `-record(Name, {key1=Default1, key2=Default2, key3, ...})`. `Name` is the record name, and the keys (`key1`, `key2`, ...) are the field names; they must always be atoms. Each field may have a default value used when no value is supplied at construction. A field declared without a default (e.g. `key3`) defaults to the atom `undefined`. Records "are just tuples in disguise" — they have the same storage and performance characteristics as tuples ("Records and Maps," *Naming Tuple Items with Records*; *Records Are Tuples in Disguise*).

# Prerequisites

- **Tuple** — A record is internally represented as a tuple; understanding tuples is necessary to understand how records store data.
- **Pattern matching** — Extracting fields and dispatching on records both rely on pattern matching.

# Key Properties

1. Declared with `-record(Name, {...})` in source modules or `.hrl` files — never in the shell.
2. Field names must always be atoms.
3. Each field may have a default value; a field with no default value defaults to the atom `undefined`.
4. Uses a fixed and predefined set of names that do not change at runtime.
5. Internally a record is a tuple whose first element is the record name (e.g. `#todo{...}` prints as `{todo, ...}` once the shell forgets the definition).
6. Records are a purely syntactic convenience resolved at compile time.

# Construction / Recognition

## To Construct/Create:
1. Declare the record with `-record(Name, {...})` in the source file or an included `.hrl` file.
2. In the shell, read the record definition with `rr("file.hrl")` before using it.
3. Create an instance with `#Name{key1=Val1, ..., keyN=ValN}`; omitted keys take their default values.

## To Identify/Recognize:
1. In a function head or guard, use `is_record(X, Name)` to test whether `X` is a record of type `Name`.
2. Pattern match with a record pattern such as `#todo{status=S, who=W}` to bind field values.

# Context & Application

Records should be used when data can be represented with a fixed number of predetermined atoms, when the number and names of elements will not change over time, and when storage is an issue — typically when there is a large array of tuples all with the same structure.

- **Typical contexts**: Representing structured records with a known schema, e.g. a to-do item.
- **Common applications**: Sharing common definitions across modules via included `.hrl` files; building APIs around structured data.
- **Historical/stylistic notes**: File inclusion is the only way to ensure several modules use the same record definitions, analogous to C `.h` files.

# Examples

**Example 1** (*Naming Tuple Items with Records*): A `todo` record stored in `records.hrl`:

```erlang
-record(todo, {status=reminder, who=joe, text}).
```

**Example 2** (*Creating and Updating Records*): Creating and copying records in the shell.

```erlang
%% Create with defaults
#todo{}.
%% => #todo{status = reminder, who = joe, text = undefined}

X1 = #todo{status=urgent, text="Fix errata in book"}.
%% => #todo{status = urgent, who = joe, text = "Fix errata in book"}
```

**Example 3** (*Pattern Matching Records in Functions*): A function that pattern matches a record and returns an updated copy.

```erlang
clear_status(#todo{status=S, who=W} = R) ->
    %% Inside this function S and W are bound to the field
    %% values in the record; R is the *entire* record
    R#todo{status=finished}.
```

# Relationships

## Builds Upon
- **Tuple** — A record is a tuple with a name tag and named positions.

## Enables
- **Record update** — Updating a record copies the underlying tuple.
- **Include file** — `.hrl` files exist largely to share record definitions.

## Related
- **Map** — Both add names to data; maps allow dynamic keys, records do not.

## Contrasts With
- **Map** — Records use a fixed, compile-time set of names with tuple-like storage; maps use dynamic keys, more storage, and slower lookup.

# Common Errors

- **Error**: Trying to declare a record with `-record(...)` in the shell.
  **Correction**: Record declarations are only valid in Erlang source modules and `.hrl` files; use `rr` in the shell to read existing definitions.

- **Error**: Mutating a record in place and expecting the original to change.
  **Correction**: `X1#todo{status=done}` creates a *copy*; the original record is unchanged.

# Common Confusions

- **Confusion**: Believing records are a distinct runtime data type.
  **Clarification**: Records are a compile-time syntactic convenience; internally there are only tuples.

- **Confusion**: Thinking new fields can be added to a record at runtime.
  **Clarification**: A record's field set is fixed at compile time; only maps support adding names dynamically.

# Source Reference

Chapter 5: Records and Maps, sections "When to Use Maps or Records," "Naming Tuple Items with Records," "Creating and Updating Records," "Extracting the Fields of a Record," "Pattern Matching Records in Functions," and "Records Are Tuples in Disguise." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the `-record` syntax description and the "Records Are Tuples in Disguise" section.
- Confidence rationale: HIGH — the source explicitly defines records, their syntax, and their tuple representation with worked shell examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards (tuple, pattern-matching, record-update, include-file, map).
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
