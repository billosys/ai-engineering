---
# === CORE IDENTIFICATION ===
concept: Native Record Construction
slug: native-record-construction

# === CLASSIFICATION ===
category: data-types
subcategory: native-records
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Native Records"
chapter_number: null
pdf_page: null
section: "Constructing Native Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "native record creation"
  - "local and external record construction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-definition
extends: []
related:
  - native-record-export
  - native-record-import
  - native-record-field-access
  - native-record-update
contrasts_with:
  - record-creation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a native record?"
  - "What is the difference between local and external native record construction?"
  - "What is definition capturing?"
  - "What happens if I omit a field without a default when constructing a native record?"
---

# Quick Definition
Native records are constructed using `#Name{Field1=Expr1, ...}` (local) or `#Module:Name{Field1=Expr1, ...}` (external). At construction time, the record definition is "captured" into the value, enabling subsequent operations to work even if the module changes or unloads.

# Core Definition
The Erlang Reference Manual states that native record construction uses `#Name{Field1=Expr1, ..., FieldK=ExprK}` or `#Module:Name{Field1=Expr1, ..., FieldK=ExprK}`. "The fields can be given in any order, not necessarily the same order as in the record definition, and fields can be omitted. Omitted fields are assigned their default values." It is "an error if not all fields are given values either explicitly or through default values." Construction is *local* when no module prefix is used and the definition appears in the current module; it is *external* when using `#Module:Name{...}` or when the name has been imported. Furthermore, "When constructing a native record, the record definition is 'captured'; that is, included in the created record value" (Native Records, "Constructing Native Records" and "Capturing of the Record Definition" sections).

# Prerequisites
- **native-record-definition** -- The record must be defined (locally or in another module)

# Key Properties
1. Local syntax: `#Name{Field1=Expr1, ..., FieldK=ExprK}`
2. External syntax: `#Module:Name{Field1=Expr1, ..., FieldK=ExprK}`
3. Fields can be in any order; omitted fields use their defaults
4. All fields must have values (explicit or default) -- no implicit `undefined`
5. Local construction: missing fields cause a **compile error**
6. External construction: missing fields cause a **runtime exception**
7. The record definition is **captured** at construction time
8. The export status at construction time is also captured
9. Subsequent operations use the captured definition, not the current module definition

# Construction / Recognition
## Local Construction:
1. Use `#Name{...}` when the record is defined in the current module
2. Missing fields without defaults cause a compile error

## External Construction:
1. Use `#Module:Name{...}` or import the record and use `#Name{...}`
2. The source module must be loaded
3. The record must be exported
4. Missing fields without defaults cause a runtime exception

## To Recognize:
1. `#Name{...}` or `#Module:Name{...}` in expression context (not after another expression)

# Context & Application
The distinction between local and external construction is important for error handling. Local construction catches field errors at compile time. External construction defers errors to runtime because the defining module may change independently. The definition capturing mechanism is a key design feature: it means record values are self-describing and portable across nodes and module versions.

# Examples
**Example 1** (Local Record Construction section):
```erlang
-module(example).
-record #pair{a, b}.

make_pair(A, B) ->
    #pair{a=A, b=B}.
```
```erlang
1> example:make_pair(1, 2).
#example:pair{a = 1,b = 2}
```

**Example 2** (External Record Construction section): Using module prefix:
```erlang
-module(example).

make_pair(A, B) ->
    #pair_library:pair{a=A, b=B}.
```

**Example 3** (External Record Construction section): Runtime error for missing fields:
```erlang
-module(example).

make_empty_pair() ->
    #pair_library:pair{}.
```
```
1> example:make_empty_pair().
** exception error: no value provided for field a in #pair_library:pair{}
```

# Relationships
## Builds Upon
- **native-record-definition** -- Provides the field list and defaults

## Enables
- **native-record-field-access** -- Constructed records can have their fields accessed
- **native-record-update** -- Constructed records can be updated
- **native-record-patterns** -- Constructed records can be pattern matched

## Related
- **native-record-export** -- Export status affects external construction
- **native-record-import** -- Importing enables unqualified external construction

## Contrasts With
- **record-creation** -- Tuple-based record creation always allows omitted fields (defaulting to `undefined`) and never captures definitions

# Common Errors
- **Error**: Omitting fields without defaults during local construction
  **Correction**: Provide values for all fields that lack defaults in the definition.

- **Error**: Attempting external construction when the source module is not loaded
  **Correction**: Ensure the module is loaded before constructing its records externally.

# Common Confusions
- **Confusion**: Thinking external construction with `#Name{...}` (after import) is local
  **Clarification**: Imported records are still external. Errors appear at runtime, not compile time.

- **Confusion**: Not understanding definition capturing
  **Clarification**: The record definition is embedded in the value at construction time. All subsequent operations (access, update, match) use this captured definition, not the module's current definition.

# Source Reference
Native Records chapter, "Constructing Native Records" and "Capturing of the Record Definition" sections.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit examples with error messages
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
