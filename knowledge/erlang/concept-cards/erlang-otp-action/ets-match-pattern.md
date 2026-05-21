---
# === CORE IDENTIFICATION ===
concept: ETS Match Pattern
slug: ets-match-pattern

# === CLASSIFICATION ===
category: performance
subcategory: in-memory-storage
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Implementing a caching system"
chapter_number: 6
pdf_page: null
section: "6.4.2 Implementing the sc_store module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - match pattern
  - "ETS match patterns"
  - "ets:match_delete"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
  - pattern-matching
extends:
  - ets
related:
  - sc-store
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ETS match pattern?"
  - "How do you delete ETS entries by value rather than by key?"
  - "What do the underscore atom and pattern variables mean in an ETS match pattern?"
---

# Quick Definition

An ETS match pattern is a pattern expressed as an Erlang term that lets ETS search through tables without extracting every entry — used to match, retrieve, or delete entries by any field, not just the key.

# Core Definition

ETS tables have a powerful mechanism for using patterns to search through tables without extracting every entry (Ch. 6, Section 6.4.2). A match pattern is a pattern expressed as an Erlang term, consisting of three kinds of things: normal Erlang terms and already-bound variables; the underscore as a single-quoted atom `'_'` (a don't-care wildcard, like `_` in a regular pattern); and pattern variables of the form `'$<integer>'` such as `'$1'`, `'$2'`. For example, given a stored tuple `{erlang, number, 1}`, the pattern `{erlang, '_', 1}` matches it, and `{'$2', '$1', '_'}` yields `[number, erlang]` — pattern variable values are returned in the order they are numbered. Matching scans the whole table but is fast because it is done in C with minimal data copying.

# Prerequisites

- **ETS** — Match patterns are used with ETS table functions.
- **Pattern matching** — Match patterns mirror ordinary Erlang pattern matching.

# Key Properties

1. A pattern expressed as an Erlang term, used with ETS functions.
2. Made of: literal terms/bound variables; the `'_'` wildcard atom; `'$N'` pattern variables.
3. `'_'` is a don't-care wildcard, like `_` in a regular pattern.
4. `'$1'`, `'$2'`, ... capture values, returned in numeric order.
5. Scans the whole table but is fast (C code, minimal copying).
6. Enables deleting/matching entries by any field, not only the key.

# Construction / Recognition

## To Use a Match Pattern:
1. Build a tuple shaped like the stored tuples.
2. Put literal values where you require a match.
3. Put `'_'` where you do not care.
4. Put `'$N'` variables where you want to capture values.
5. Pass it to an ETS function such as `ets:match/2` or `ets:match_delete/2`.

# Context & Application

Match patterns let code operate on ETS entries by value — for instance, deleting a cache entry given only its pid.

- **Typical contexts**: Deleting or searching ETS entries by a non-key field.
- **Common applications**: `sc_store:delete/1` uses `ets:match_delete(?TABLE_ID, {'_', Pid})` to delete the entry whose value (second element) is `Pid`.

# Examples

**Example 1** (Ch. 6, Listing 6.6): `sc_store:delete/1` calls `ets:match_delete(?TABLE_ID, {'_', Pid})` — the pattern matches any 2-tuple with `Pid` as the second element.

**Example 2** (Ch. 6): With a stored tuple `{erlang, number, 1}`, the pattern `{'$2', '$1', '_'}` yields `[number, erlang]`.

# Relationships

## Builds Upon
- **ETS** — Match patterns are part of the ETS interface.

## Related
- **sc-store** — `sc_store:delete/1` uses a match pattern.

## Contrasts With
- This card has no direct contrast within the source's treatment.

# Common Errors

- **Error**: Writing the wildcard as a bare `_` instead of the atom `'_'`.
  **Correction**: In ETS match patterns the wildcard is the single-quoted atom `'_'`.

# Common Confusions

- **Confusion**: Thinking a match scan is slow because it traverses the table.
  **Clarification**: It scans the whole table but is fast — done in C with minimal copying.

# Source Reference

Chapter 6: Implementing a caching system, Section 6.4.2, "Deleting an entry using match patterns" and the "Match patterns" sidebar.

# Verification Notes

- Definition source: Direct adaptation of the "Match patterns" sidebar and surrounding text.
- Confidence rationale: HIGH — explicit definition in a dedicated sidebar.
- Uncertainties: Full ETS matching (match specs) is explicitly out of scope per the source.
- Cross-reference status: References Agent-1 slug `pattern-matching` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
