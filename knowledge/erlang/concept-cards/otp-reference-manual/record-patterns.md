---
# === CORE IDENTIFICATION ===
concept: Record Patterns
slug: record-patterns

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: records
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Records in Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "record matching"
  - "record pattern matching"
  - "records in function heads"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
  - pattern-matching
extends:
  - pattern-matching
related:
  - record-creation
  - record-in-guards
contrasts_with:
  - native-record-patterns

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I pattern match on a record in a function head?"
  - "Can I use unbound variables in a record pattern?"
  - "Do I need to match all fields in a record pattern?"
---

# Quick Definition
Record patterns use the same syntax as record creation (`#Name{Field1=Expr1, ..., FieldK=ExprK}`) but in pattern context, where one or more of the expressions can be unbound variables. Only the fields mentioned are matched; unmentioned fields are ignored.

# Core Definition
The Erlang Reference Manual states: "A pattern that matches a certain record is created in the same way as a record is created: `#Name{Field1=Expr1, ..., FieldK=ExprK}`. In this case, one or more of `Expr1` ... `ExprK` can be unbound variables." (Records, "Records in Patterns" section).

# Prerequisites
- **record-definition** -- The record type must be defined for pattern matching
- **pattern-matching** -- General understanding of Erlang pattern matching

# Key Properties
1. Syntax is identical to record creation: `#Name{Field1=Pattern1, ..., FieldK=PatternK}`
2. Expressions can be unbound variables for extracting field values
3. Fields not mentioned in the pattern are not matched (they can be any value)
4. Can be used in function heads, case expressions, and receive expressions
5. Compiled to tuple pattern matching at the underlying level

# Construction / Recognition
## To Write a Record Pattern:
1. Use `#RecordName{Field=Pattern, ...}` in a pattern position
2. Use variables to extract specific field values
3. Omit fields you do not care about

## To Recognize:
1. Look for `#RecordName{...}` in function heads, case clauses, or receive clauses
2. Fields contain patterns (variables, literals, nested patterns) rather than expressions

# Context & Application
Record patterns are used extensively in Erlang for dispatching on record types and extracting fields in function heads and case expressions. Since only mentioned fields participate in matching, patterns can be concise. This is particularly useful in `gen_server` callbacks where different message types are distinguished by their record tags.

# Examples
**Example 1** (Records in Patterns section, inferred from creation example):
```erlang
-record(person, {name, phone, address}).

get_name(#person{name=Name}) ->
    Name.

handle_person(#person{name="Joe", phone=Phone}) ->
    {joe, Phone};
handle_person(#person{name=Name}) ->
    {other, Name}.
```

# Relationships
## Builds Upon
- **record-definition** -- Pattern uses field names from the definition
- **pattern-matching** -- Record patterns are a specialization of general pattern matching

## Enables
- **record-in-guards** -- Guard tests can further constrain record pattern matches

## Related
- **record-creation** -- Uses identical syntax in a different context
- **record-field-access** -- Alternative to pattern matching for extracting field values

## Contrasts With
- **native-record-patterns** -- Native record patterns use the captured definition and can fail if field names were not present at construction time

# Common Errors
- **Error**: Expecting a record pattern to fail if the record has extra fields not mentioned in the pattern
  **Correction**: Unmentioned fields are ignored in patterns. The match succeeds as long as the record tag matches and the mentioned fields match.

# Common Confusions
- **Confusion**: Thinking you must list all fields in a record pattern
  **Clarification**: You only need to list the fields you want to match or extract. Omitted fields are not checked.

# Source Reference
Records chapter, "Records in Patterns" section.

# Verification Notes
- Definition source: Direct quote from source text
- Confidence rationale: High -- explicit definition
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
