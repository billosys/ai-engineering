---
# === CORE IDENTIFICATION ===
concept: Anonymous Variable
slug: anonymous-variable

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: pattern-matching
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.4.4 More about patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - don't-care pattern
  - underscore pattern
  - placeholder

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends:
  - pattern-matching
related:
  - variable
contrasts_with:
  - variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the underscore in an Erlang pattern?"
  - "What is a don't-care pattern?"
  - "Do multiple underscores in a pattern have to match the same value?"
---

# Quick Definition

The anonymous variable `_` is a don't-care placeholder in a pattern, matching anything without binding a name. It is not actually a variable.

# Core Definition

The single underscore `_` indicates a "*don't-care pattern*. In other words, where you wrote `_`, you don't care what value the right side has at that point, and you don't want to know" (Chapter 2, section 2.4.4). You can have several underscores in the same pattern, but unlike repeated variables they "don't have to have the same values in all places." These don't-care patterns "are sometimes referred to as *anonymous variables*, but they aren't variables at all, just placeholders."

# Prerequisites

- **Pattern matching** — the anonymous variable appears only within patterns.

# Key Properties

1. `_` is a don't-care placeholder in a pattern.
2. It matches any value without binding a name.
3. Multiple `_` in one pattern need not match the same value.
4. It is not actually a variable — it is just a placeholder.
5. It carries none of the unused-variable warning concerns of named variables.

# Construction / Recognition

## To Identify/Recognize:
1. A bare `_` in a pattern is the anonymous variable.
2. It accepts any value and discards it.
3. Each `_` is independent of every other `_`.

# Context & Application

- **Typical contexts**: Patterns where some parts of a structure are irrelevant.
- **Common applications**: Ignoring tuple elements, list tails, or function arguments — e.g. `[ {person, [{name,_,Surname},_,{tags, Tags}]} | _ ]`.
- **Historical/stylistic notes**: Named underscore variables (`_Name`) are different — they are real variables that suppress the unused warning, whereas bare `_` is a pure placeholder.

# Examples

**Example 1** (section 2.4.4): In `[ {person, [{name,_,Surname},_,{tags, Tags}]} | _ ]`, the underscores ignore the user's first name, the middle list element, and the rest of the outer list, while `Surname` and `Tags` are captured.

**Example 2** (section 2.5.2): The function clause `either_or_both(true, _) -> true` uses `_` for the second argument, meaning the clause matches regardless of that argument's value.

# Relationships

## Builds Upon
- **Pattern matching** — the anonymous variable is a pattern element.

## Enables
- Concise patterns that ignore irrelevant parts of data.

## Related
- **Variable** — named underscore variables suppress unused warnings but are real variables.

## Contrasts With
- **Variable** — a real variable binds a name and (if repeated) forces equality; `_` binds nothing and each `_` is independent.

# Common Errors

- **Error**: Expecting two `_` in the same pattern to refer to the same value.
  **Correction**: Each `_` is independent; use a repeated named variable to require equality.

# Common Confusions

- **Confusion**: Treating `_` as a variable you could later refer to.
  **Clarification**: `_` is a placeholder, not a variable; it binds no name and cannot be referenced.

# Source Reference

Chapter 2: Erlang language essentials, section 2.4.4 "More about patterns." See also section 2.5.2.

# Verification Notes

- Definition source: Direct adaptation from section 2.4.4.
- Confidence rationale: HIGH — the don't-care pattern is explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
