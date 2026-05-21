---
# === CORE IDENTIFICATION ===
concept: Map Pattern Matching
slug: map-pattern-matching

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: pattern-matching
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Records and Maps"
chapter_number: 5
pdf_page: null
section: "Pattern Matching the Fields of a Map"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - map pattern
  - matching maps

# === TYPED RELATIONSHIPS ===
prerequisites:
  - map
  - pattern-matching
extends:
  - pattern-matching
related:
  - map-update-operators
contrasts_with:
  - record

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I pattern match the fields of a map?"
  - "Can I use maps in function heads?"
  - "What restrictions apply to keys in a map pattern?"
---

# Quick Definition

A map pattern uses the `:=` operator to extract values from a map by key. The keys in the pattern must be fully ground, but the values may contain variables that become bound on a successful match.

# Core Definition

The `:=` syntax used in map literals can also serve as a map pattern. "As before, the keys in a map pattern cannot contain any unbound variables, but the value can now contain variables that become bound if the pattern match succeeds" ("Records and Maps", *Pattern Matching the Fields of a Map*). The number of keys in a map pattern can be fewer than the number of keys in the map being matched — the pattern only needs to mention the keys of interest. Map patterns may be used in function heads provided all the keys in the pattern are known (bound).

# Prerequisites

- **Map** — Map patterns match against map values.
- **Pattern matching** — Map matching is a specialized form of Erlang's general pattern matching.

# Key Properties

1. Map patterns use `:=` to associate a key with a value pattern.
2. Keys in a pattern must be fully ground — no unbound variables.
3. Value positions may contain unbound variables that bind on success.
4. A pattern may mention fewer keys than the matched map contains.
5. Map patterns can appear in function clause heads when all their keys are bound.

# Construction / Recognition

## To Construct/Create:
1. Write `#{ Key := Var } = Map` to bind `Var` to the value of `Key`.
2. In a function head, write a clause like `count_characters([H|T], #{ H := N }=X)` where `H` is bound from elsewhere in the head.

## To Identify/Recognize:
1. A `#{...}` form on the left of `=` or in a function head, using `:=`, is a map pattern.

# Context & Application

- **Typical contexts**: extracting specific values from a map without destructuring the whole structure.
- **Common applications**: function heads that branch on whether a map already contains a key.
- **Historical/stylistic notes**: in the character-count function, the key variable `H` is bound elsewhere in the same head, satisfying the "all keys known" requirement.

# Examples

**Example 1** (*Pattern Matching the Fields of a Map*): extracting one value:

```erlang
1> Henry8 = #{ class => king, born => 1491, died => 1547 }.
2> #{ born := B } = Henry8.
3> B.
1491
```

**Example 2** (*Pattern Matching the Fields of a Map*): an unbound key fails:

```erlang
4> #{ D => 1547 }.
* 4: variable 'D' unbound
```

## Worked Example

A map pattern in a function head, where `H` is bound by the list pattern (*Pattern Matching the Fields of a Map*):

```erlang
count_characters([H|T], #{ H := N }=X) ->
    count_characters(T, X#{ H := N+1 });
```

# Relationships

## Builds Upon
- **Pattern matching** — Map patterns are a kind of Erlang pattern.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Map update operators** — The same `:=` operator is used for both patterns and updates.

## Contrasts With
- **Record** — Record patterns reference compile-time field names; map patterns use runtime key values that must be ground.

# Common Errors

- **Error**: Putting an unbound variable in the key position of a map pattern.
  **Correction**: All keys in a map pattern must be bound or literal; only value positions may be unbound.

- **Error**: Expecting a map pattern to fail because it does not list every key in the map.
  **Correction**: A map pattern may mention a subset of keys; extra keys in the matched map are ignored.

# Common Confusions

- **Confusion**: Thinking `=>` can be used in a map pattern.
  **Clarification**: Map patterns use `:=`; `=>` is for map literals and add-or-update.

- **Confusion**: Believing map patterns require an exact key-set match.
  **Clarification**: The pattern's keys are a subset; the matched map may have more keys.

# Source Reference

Chapter 5: "Records and Maps", section "Pattern Matching the Fields of a Map".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Pattern Matching the Fields of a Map*.
- Confidence rationale: HIGH — the source explicitly states the rules and gives worked examples.
- Uncertainties: None.
- Cross-reference status: Slugs `map`, `map-update-operators`, `record` extracted in this chapter; `pattern-matching` assumed canonical.
- Re-extraction notes: Fresh extraction; overwrote prior card of the same slug.
