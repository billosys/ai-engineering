---
# === CORE IDENTIFICATION ===
concept: Map Pattern Matching
slug: map-pattern-matching

# === CLASSIFICATION ===
category: data-types
subcategory: maps
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Maps in Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "map matching"
  - "map destructuring"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - map-creation
extends:
  - map-creation
related:
  - map-update
  - map-in-guards
  - guard-expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct and use a map in Erlang?"
  - "How do I pattern match on maps?"
  - "Why does map matching use := instead of =>?"
---

# Quick Definition

Map pattern matching uses the `:=` operator to extract values associated with keys from a map. The key must be a guard expression with all variables already bound, and only the `:=` operator (not `=>`) is allowed in map patterns.

# Core Definition

Matching of key-value associations from maps uses the syntax `#{K := V} = M`, where `M` is any map. The key `K` must be a guard expression with all variables already bound. `V` can be any pattern with bound or unbound variables. If `V` is unbound, it becomes bound to the value associated with key `K`, which must exist in `M`. If `V` is bound, it must match the value associated with `K`. Multiple values can be matched: `#{K1 := V1, ..., Kn := Vn} = M`. Only the `:=` operator is allowed in map patterns (not `=>`). The order of key declarations in matching is irrelevant. Duplicate keys are allowed and match each pattern. The empty map `#{}` matches any map (Erlang Reference Manual, "Maps in Patterns" section).

# Prerequisites

- **map-creation** — Must understand map construction and the `=>` vs `:=` distinction.

# Key Properties

1. Only `:=` is allowed in map patterns (not `=>`).
2. Keys must be guard expressions with all variables already bound.
3. Values can contain unbound variables (which become bound on match).
4. `#{}` (empty map pattern) matches any map.
5. The order of key declarations in matching is irrelevant.
6. Duplicate keys are allowed — each associated pattern is matched.
7. Keys can be constructed from expressions (e.g., `#{{tag, length(List)} := V}`).
8. Map patterns are allowed in function heads, case expressions, and receive clauses.
9. Since Erlang/OTP 23, the key expression can be any guard expression (previously limited to variables or literals).

# Construction / Recognition

## To Match a Map:
1. Write `#{Key := Variable} = MapExpr`.
2. Ensure key expressions use only bound variables.
3. Use `:=` (not `=>`).
4. Multiple keys: `#{K1 := V1, K2 := V2} = M`.

## To Recognize:
1. Look for `#{...}` on the left side of a match with `:=` separators.
2. Or `#{...}` patterns in function heads or case clauses.

# Context & Application

Map pattern matching is used extensively for extracting values from maps in function heads, case expressions, and receive clauses. It provides a declarative way to destructure maps. The restriction to `:=` (not `=>`) in patterns ensures that only existing keys can be matched, preventing accidental creation of new associations.

# Examples

**Example 1** (Maps in Patterns section): Extracting a value:

```erlang
1> M = #{"tuple" => {1,2}}.
#{"tuple" => {1,2}}
2> #{"tuple" := {1,B}} = M.
#{"tuple" => {1,2}}
3> B.
2.
```

**Example 2** (Maps in Patterns section): Matching in function heads:

```erlang
%% only start if not_started
handle_call(start, From, #{state := not_started} = S) ->
    ...
    {reply, ok, S#{state := start}};

%% only change if started
handle_call(change, From, #{state := start} = S) ->
    ...
    {reply, ok, S#{state := changed}};
```

**Example 3** (Maps in Patterns section): Key constructed from expression:

```erlang
#{{tag,length(List)} := V} = Map
```

# Relationships

## Builds Upon
- **map-creation** — Pattern matching is the inverse of construction.

## Enables
- **map-in-guards** — Map matching is often combined with map guard BIFs.

## Related
- **map-update** — Both use `:=` but for different purposes (matching vs. update-only).
- **guard-expressions** — Keys in map patterns must be valid guard expressions.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Using `=>` instead of `:=` in a map pattern.
  **Correction**: Only `:=` is allowed in map patterns.

- **Error**: Using an unbound variable as a key in a map pattern.
  **Correction**: All variables in key expressions must be already bound.

# Common Confusions

- **Confusion**: Thinking `#{}` in a pattern only matches empty maps.
  **Clarification**: `#{}` matches any map when used as a pattern, not just the empty map.

- **Confusion**: Expecting map pattern matching to fail if the map has extra keys.
  **Clarification**: Map matching is partial — a pattern `#{a := V}` matches any map containing key `a`, regardless of other keys.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Map Expressions" section, "Maps in Patterns" subsection.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax rules, constraints, and examples
- Uncertainties: None
- Cross-reference status: Related map concepts verified
