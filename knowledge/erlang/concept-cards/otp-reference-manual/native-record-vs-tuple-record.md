---
# === CORE IDENTIFICATION ===
concept: Native Record vs Tuple Record Comparison
slug: native-record-vs-tuple-record

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "native vs tuple records"
  - "record type comparison"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
  - native-record-definition
extends: []
related:
  - record-internal-representation
  - native-record-construction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between native records and tuple-based records?"
  - "When should I use native records vs tuple-based records?"
  - "Are native records tuples?"
---

# Quick Definition
Native records are a distinct runtime type with module-scoped ownership and export/import visibility, while tuple-based records are a compile-time abstraction over tagged tuples. The two are not interchangeable and have different syntax, representation, and visibility models.

# Core Definition
The Erlang Reference Manual states: "A native record is a data structure for storing a fixed number of elements in named fields. Unlike traditional tuple-based records described in the previous section, a native record is a distinct type." Key differences synthesized from the source: tuple-based records compile to tuples and use `-record(Name, {...})` syntax with header file sharing; native records use `-record #Name{...}` syntax with module-scoped export/import visibility and are a distinct type at runtime (Native Records, introductory section).

# Prerequisites
- **record-definition** -- Understanding of tuple-based records
- **native-record-definition** -- Understanding of native records

# Key Properties

| Property | Tuple-Based Records | Native Records |
|---|---|---|
| Syntax | `-record(Name, {fields}).` | `-record #Name{fields}.` |
| Runtime type | Tagged tuple | Distinct type |
| `is_record/1` | Returns `false` | Returns `true` |
| Sharing | Header files (`.hrl`) | `-export_record` / `-import_record` |
| Name quoting | Required for variable-like names | Not required |
| Default values | Arbitrary expression (no variables) | Literals or simple compile-time expressions |
| Field initialization | Omitted fields get `undefined` | All fields must have values (explicit or default) |
| Captured definition | N/A (compile-time only) | Definition captured at construction time |
| Hot code update | Requires manual conversion | Captured definition enables cross-version matching |
| Shell support | Since OTP 26 | Yes, under `shell_default` module |

# Construction / Recognition
## To Distinguish:
1. Check the definition syntax: parentheses vs `#` prefix
2. Use `is_record/1` (returns `true` only for native records)
3. Check printed representation: native records print as `#Module:Name{...}`

# Context & Application
The choice between tuple-based and native records depends on the OTP version and requirements. Tuple-based records are mature, universally supported, and well-understood. Native records (OTP 29+, experimental) provide better type safety, module ownership, and runtime distinguishability from tuples. Native records are recommended for new code on OTP 29+ when the experimental status is acceptable.

# Examples
**Example 1**: Definition syntax comparison:
```erlang
%% Tuple-based record
-record(person, {name, phone, address}).

%% Native record
-record #person{name, phone, address}.
```

**Example 2**: Runtime behavior difference:
```erlang
%% Tuple-based record: is_record/1 returns false
R1 = #person{name="Joe", phone="555", address="Stockholm"},
false = is_record(R1),
true = is_tuple(R1),

%% Native record: is_record/1 returns true
R2 = #person{name="Joe", phone="555", address="Stockholm"},
true = is_record(R2),
false = is_tuple(R2).
```

# Relationships
## Builds Upon
- **record-definition** -- Tuple-based records
- **native-record-definition** -- Native records

## Enables
No direct dependents within this extraction scope.

## Related
- **record-internal-representation** -- Explains the tuple nature of traditional records

## Contrasts With
No additional contrasts beyond the inherent comparison nature of this card.

# Common Errors
- **Error**: Treating a native record as a tuple (e.g., using `element/2` on it)
  **Correction**: Native records are not tuples. Use record syntax or the `records` module for field access.

- **Error**: Defining a native record in a header file like a tuple-based record
  **Correction**: Native records should be defined in a module and exported with `-export_record`.

# Common Confusions
- **Confusion**: Assuming code using tuple-based records can transparently switch to native records
  **Clarification**: The types are incompatible. Code that relies on the tuple representation (e.g., `element/2`, `setelement/3`, tuple pattern matching) will break with native records.

# Source Reference
Native Records chapter, introductory section and "Defining Native Records" section.

# Verification Notes
- Definition source: Direct quote plus synthesized comparison from both chapters
- Confidence rationale: High -- differences are explicitly stated in the source
- Uncertainties: Native records are experimental in OTP 29
- Cross-reference status: All referenced slugs correspond to cards in this extraction
