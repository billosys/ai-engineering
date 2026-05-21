---
# === CORE IDENTIFICATION ===
concept: Map
slug: map

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Map"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends: []
related:
  - tuple
  - list
  - record-definition
  - native-record-definition
contrasts_with:
  - tuple
  - record-definition

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
  - "How do atoms, tuples, and lists form the foundation of Erlang's type system?"
---

# Quick Definition
A map is a compound data type with a variable number of key-value associations, written as `#{Key1 => Value1, ..., KeyN => ValueN}`. Maps provide named access to data with arbitrary key types.

# Core Definition
The Erlang Reference Manual defines a map as "a compound data type with a variable number of key-value associations," written as `#{Key1 => Value1, ..., KeyN => ValueN}`. Each key-value association is called an association pair, and the key and value parts are called elements. The number of association pairs is the size of the map. Maps were introduced as experimental in Erlang/OTP R17 and became fully supported in Erlang/OTP 18 (Data Types, "Map" section).

# Prerequisites
- **erlang-term** -- Map keys and values are terms

# Key Properties
1. Compound data type with a variable number of key-value associations
2. Written as `#{Key1 => Value1, ..., KeyN => ValueN}`
3. Keys can be any term (atoms, integers, binaries, tuples, etc.)
4. Each key-value pair is called an association pair
5. The empty map `#{}` has size 0
6. Maps support `maps:get/2`, `maps:update/3`, `map_size/1`, and other functions
7. Maps are unordered -- the printed order may differ from the creation order

# Construction / Recognition
## To Construct/Create:
1. Use literal syntax: `#{name => adam, age => 24}`
2. Use `maps:put/3` to add/update a key: `maps:put(key, value, Map)`
3. Use `maps:update/3` to update an existing key: `maps:update(age, 25, M1)`
4. Use map update syntax: `Map#{key := new_value}` (key must exist)

## To Identify/Recognize:
1. Use `is_map/1` BIF
2. Use `map_size/1` to get the number of association pairs
3. Maps print with `#{}` syntax

# Context & Application
Maps are Erlang's built-in key-value data structure, suitable for:
- Configuration and options
- JSON-like data
- Replacing records when field sets need to be dynamic
- Process state in `gen_server` and other behaviours

A collection of map-processing functions is available in the `maps` module in STDLIB.

# Examples
**Example 1** (Data Types, "Map" section):
```erlang
1> M1 = #{name => adam, age => 24, date => {july,29}}.
#{age => 24,date => {july,29},name => adam}
2> maps:get(name, M1).
adam
3> maps:get(date, M1).
{july,29}
4> M2 = maps:update(age, 25, M1).
#{age => 25,date => {july,29},name => adam}
5> map_size(M2).
3
6> map_size(#{}).
0
```

# Relationships
## Builds Upon
- **erlang-term** -- Map keys and values are terms

## Enables
No direct dependents within this extraction scope.

## Related
- **tuple** -- Tuples use positional access; maps use key-based access
- **list** -- Lists are sequential; maps are associative
- **record-definition** -- Records provide named fields like maps but with compile-time checks

## Contrasts With
- **tuple** -- Tuples are fixed-size with positional access; maps are variable-size with key-based access
- **record-definition** -- Records have compile-time field checking; maps have runtime key checking

# Common Errors
- **Error**: Using `:=` to add a new key (`:=` requires the key to already exist)
  **Correction**: Use `=>` to create or update a key; `:=` only updates existing keys

# Common Confusions
- **Confusion**: Expecting maps to preserve insertion order
  **Clarification**: Maps are unordered. The printed representation may differ from the insertion order.

- **Confusion**: Treating maps and records as interchangeable
  **Clarification**: Records have compile-time field validation and are represented as tuples. Maps are dynamic key-value stores. Native records are a distinct type entirely.

# Source Reference
Data Types chapter, "Map" section.

# Verification Notes
- Definition source: Direct quote from source ("a compound data type with a variable number of key-value associations")
- Confidence rationale: High -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
