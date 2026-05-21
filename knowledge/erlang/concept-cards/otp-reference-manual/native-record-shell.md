---
# === CORE IDENTIFICATION ===
concept: Native Records in the Erlang Shell
slug: native-record-shell

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
section: "Native Records in the Erlang Shell"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "shell native records"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-definition
  - native-record-construction
extends: []
related:
  - native-record-export
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can I define and use native records in the Erlang shell?"
  - "What module do shell-defined native records belong to?"
  - "Can the shell access non-exported records?"
---

# Quick Definition
Native records can be defined and constructed in the Erlang shell using the same syntax as in module code. All records constructed in the shell belong to the `shell_default` module. The shell does not enforce the privacy of non-exported records.

# Core Definition
The Erlang Reference Manual states: "Native records can be defined and constructed in the Erlang shell using the same syntax as in module code. All records constructed in the shell belongs to the `shell_default` module." Furthermore, "The shell does not enforce the privacy of non-exported records. That is, the shell will print non-exported records and it also allows constructing non-exported records." (Native Records, "Native Records in the Erlang Shell" section).

# Prerequisites
- **native-record-definition** -- Understanding native record definition syntax
- **native-record-construction** -- Understanding native record construction syntax

# Key Properties
1. Same syntax as module code for definition and construction
2. Shell-defined records belong to the `shell_default` module
3. The shell bypasses export/privacy restrictions
4. Non-exported records from other modules are both printable and constructable in the shell
5. Records from loaded modules can be constructed using `#Module:Name{...}` syntax

# Construction / Recognition
## To Define in Shell:
1. Enter `-record #Name{fields}.` at the shell prompt

## To Construct in Shell:
1. Use `#Name{...}` for shell-defined records
2. Use `#Module:Name{...}` for records from loaded modules

# Context & Application
Shell support for native records is essential for debugging and experimentation. The relaxation of export restrictions in the shell is a deliberate design choice that enables developers to inspect and construct any record during debugging sessions, even if the record is private in its defining module.

# Examples
**Example 1** (Native Records in the Erlang Shell section): Defining and using in shell:
```erlang
1> -record #pair{a=1, b=1}.
ok
2> #pair{a=42}.
#shell_default:pair{a = 42,b = 1}
```

**Example 2** (Native Records in the Erlang Shell section): Accessing non-exported records from other modules:
```erlang
%% Given a module 'geometry' with non-exported #vec{x, y}:
1> geometry:make_vec(1.0, 7.0).
#geometry:vec{x = 1.0,y = 7.0}
2> #geometry:vec{x = 100.0, y = 99.0}.
#geometry:vec{x = 100.0,y = 99.0}
```

# Relationships
## Builds Upon
- **native-record-definition** -- Shell uses the same definition syntax
- **native-record-construction** -- Shell uses the same construction syntax

## Enables
No direct dependents within this extraction scope.

## Related
- **native-record-export** -- The shell bypasses export restrictions that normally apply

## Contrasts With
No direct contrasts within this extraction scope.

# Common Errors
- **Error**: Expecting shell-constructed records to belong to a specific module
  **Correction**: Records defined in the shell always belong to `shell_default`, not to any user module.

# Common Confusions
- **Confusion**: Thinking the shell enforces export restrictions
  **Clarification**: The shell deliberately relaxes privacy to enable debugging. Code in modules still respects export restrictions.

# Source Reference
Native Records chapter, "Native Records in the Erlang Shell" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit examples and behavior description
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
