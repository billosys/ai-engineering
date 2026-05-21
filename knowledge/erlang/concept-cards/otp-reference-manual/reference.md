---
# === CORE IDENTIFICATION ===
concept: Reference
slug: reference

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
section: "Reference"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ref

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-term
  - pid
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
A reference is a term that is unique among connected nodes, created by calling `make_ref/0`. References are commonly used as unique identifiers for request-response matching.

# Core Definition
The Erlang Reference Manual describes a reference as "a term that is unique among connected nodes." References are created by calling the `make_ref/0` BIF and tested with the `is_reference/1` BIF. Their uniqueness guarantee makes them suitable for correlating requests with responses and for other situations requiring unique tags (Data Types, "Reference" section).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Unique among connected nodes
2. Created by calling `make_ref/0`
3. Tested with `is_reference/1` BIF
4. Printed representation: `#Ref<...>`
5. Uniqueness is subject to system limits (eventually wraps, but the period is extremely long)

# Construction / Recognition
## To Construct/Create:
1. Call `make_ref/0` to create a new unique reference

## To Identify/Recognize:
1. Use `is_reference/1` BIF
2. References print as `#Ref<X.Y.Z.W>`

# Context & Application
References are used for:
- Request-response correlation: tag a request with a reference, match the response
- Unique identifiers in `gen_server:call` (internally uses `make_ref/0`)
- Monitor references (returned by `erlang:monitor/2`)
- Timer references (returned by `erlang:send_after/3`)

# Examples
**Example 1** (Data Types, "Reference" section):
```erlang
1> Ref = make_ref().
#Ref<0.76482849.3801088007.198204>
2> is_reference(Ref).
true
```

# Relationships
## Builds Upon
This is a foundational type with no prerequisites.

## Enables
No direct dependents within this extraction scope.

## Related
- **erlang-term** -- References are a kind of term
- **pid** -- Both are process-related identifiers; pids identify processes while references are unique tags

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Assuming references are globally unique across disconnected nodes
  **Correction**: References are unique among *connected* nodes, not across all possible nodes

# Common Confusions
- **Confusion**: Confusing references with pids
  **Clarification**: A pid identifies a specific process; a reference is a unique value used for correlation. Pids can be reused after process termination; references are unique for a very long period.

# Source Reference
Data Types chapter, "Reference" section.

# Verification Notes
- Definition source: Direct from source ("a term that is unique among connected nodes")
- Confidence rationale: High -- explicit definition
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
