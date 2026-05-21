---
# === CORE IDENTIFICATION ===
concept: Native Record Patterns
slug: native-record-patterns

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: native-records
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Native Records"
chapter_number: null
pdf_page: null
section: "Records in Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "native record matching"
  - "anonymous pattern matching"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-construction
  - pattern-matching
extends:
  - pattern-matching
related:
  - native-record-field-access
  - native-record-in-guards
contrasts_with:
  - record-patterns

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I pattern match on a native record?"
  - "What is anonymous pattern matching with #_{...}?"
  - "Do I need the record to be exported for pattern matching?"
  - "Can I match just the record name with no fields?"
---

# Quick Definition
Native record pattern matching uses `#Name{Field1=Pattern1, ...}`, `#Module:Name{Field1=Pattern1, ...}`, or the anonymous form `#_{Field1=Pattern1, ...}`. Matching uses the captured definition and respects export status, but matching only the record name (empty field list) succeeds regardless of export status.

# Core Definition
The Erlang Reference Manual states: "Pattern matching uses the same syntax as construction: `#Name{Field1=Expr1, ..., FieldN=ExprN}` or `#Module:Name{Field1=Expr1, ..., FieldN=ExprN}`. In this case, one or more of `Expr1` ... `ExprN` can contain unbound variables." Matching "will fail if one or more of the field names are not present in the record definition captured at the time the record was constructed." For external matching, "matching can also fail if at least one field is being matched and, at the time of construction, the record was not exported. If the list of fields to match is empty, the match succeeds as long as the module and record names match." Anonymous matching `#_{...}` follows similar rules regarding export status (Native Records, "Records in Patterns" and "Anonymous Pattern Matching" sections).

# Prerequisites
- **native-record-construction** -- The captured definition governs what fields can be matched
- **pattern-matching** -- General understanding of Erlang pattern matching

# Key Properties
1. Local syntax: `#Name{Field1=Pattern1, ...}`
2. External syntax: `#Module:Name{Field1=Pattern1, ...}`
3. Anonymous syntax: `#_{Field1=Pattern1, ...}`
4. Uses the captured definition from construction time
5. Matching fails if field names are not in the captured definition
6. External matching with fields requires the record to have been exported at construction
7. Empty field list `#Module:Name{}` matches on name alone, regardless of export status
8. Anonymous matching without fields would match any native record

# Construction / Recognition
## To Pattern Match:
1. Use `#Name{field=Var}` in function heads, case, or receive clauses
2. Use `#Module:Name{field=Var}` for external records
3. Use `#_{field=Var}` for anonymous matching
4. Use `#Name{}` or `#Module:Name{}` to match only the record type

## To Recognize:
1. Look for `#Name{...}`, `#Module:Name{...}`, or `#_{...}` in pattern positions

# Context & Application
The ability to match just the record name with an empty field list is particularly useful for type-dispatching without requiring export access. This enables guard-like checks on record types. The anonymous pattern form enables polymorphic functions that operate on any record with matching field names.

# Examples
**Example 1** (Records in Patterns section): Local pattern matching:
```erlang
-record #vec{}.

len(#vec{x=X, y=Y}) ->
    math:sqrt(X * X + Y * Y).
```

**Example 2** (Records in Patterns section): External name-only matching (no export required):
```erlang
is_vec(#geom_2d:vec{}) -> true;
is_vec(_) -> false.
```

**Example 3** (The Guard BIF is_record/2 section): Matching used as alternative to is_record:
```erlang
-record #vec{x, y}.

increment(#vec{}=Vec) ->
    ... .
```

# Relationships
## Builds Upon
- **native-record-construction** -- Captured definition determines matchable fields
- **pattern-matching** -- Specialization of general pattern matching

## Enables
- **native-record-in-guards** -- Guards can further constrain pattern matches

## Related
- **native-record-field-access** -- Alternative way to extract field values

## Contrasts With
- **record-patterns** -- Tuple-based record patterns have no export checks, no module qualification, and no anonymous form

# Common Errors
- **Error**: Matching on a field that was added after the record was constructed
  **Correction**: The captured definition governs matching. Fields added in newer module versions are not available for matching on old record values.

- **Error**: Expecting external pattern matching with fields to work on unexported records
  **Correction**: External matching with at least one field requires the record to have been exported at construction time.

# Common Confusions
- **Confusion**: Thinking `#Module:Name{}` (empty fields) requires export
  **Clarification**: Matching only the record name succeeds regardless of export status, as long as the module and record names match.

# Source Reference
Native Records chapter, "Records in Patterns" and "Anonymous Pattern Matching" sections.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit rules and examples
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
