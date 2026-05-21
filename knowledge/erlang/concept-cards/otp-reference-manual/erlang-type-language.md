---
# === CORE IDENTIFICATION ===
concept: Erlang Type Language
slug: erlang-type-language

# === CLASSIFICATION ===
category: data-types
subcategory: type-system-overview
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "The Erlang Type Language"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "type notation"
  - "type system"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - predefined-types
  - type-union
  - type-declaration
  - function-specification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
  - "How does the type specification system relate to Dialyzer?"
---

# Quick Definition
Erlang's type language is a notation for declaring sets of Erlang terms to form particular types, used to document interfaces, assist bug-detection tools like Dialyzer, and generate documentation.

# Core Definition
Erlang is a dynamically typed language that provides a notation for "declaring sets of Erlang terms to form a particular type," effectively forming "specific subtypes of the set of all Erlang terms" (Erlang Reference Manual, "Types and Function Specifications"). These types can specify record field types and function argument/return types. The type information serves three purposes: documenting function interfaces, providing information for tools like Dialyzer, and supporting documentation generators such as ExDoc or EDoc.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Erlang remains dynamically typed at runtime; the type language is a compile-time/analysis-time annotation system
2. Types describe sets of Erlang terms
3. Types are built from predefined types (e.g., `integer()`, `atom()`, `pid()`) and user-defined types
4. The type language supersedes and replaces the older comment-based `@type` and `@spec` EDoc declarations
5. Type information is used for documentation, static analysis (Dialyzer), and documentation generation

# Construction / Recognition
## To Use the Type Language:
1. Use `-type` attributes to declare user-defined types
2. Use `-spec` attributes to specify function signatures
3. Compose types using predefined types and type unions
4. Export types with `-export_type` to make them available as remote types

## To Identify/Recognize:
1. Look for `-type`, `-opaque`, `-nominal`, or `-spec` attributes in module source
2. Type expressions use the form `name()` with parentheses
3. Type unions use the `|` operator

# Context & Application
The type language is used throughout Erlang/OTP codebases to make function contracts explicit. While Erlang does not enforce types at compile time, tools like Dialyzer use type annotations to find bugs statically. The type language is the foundation on which all type specifications, user-defined types, opaque types, and nominal types are built.

# Examples
**Example 1** (Types and Function Specifications, "The Erlang Type Language"):
```erlang
%% Type information can be used for:
%% - To document function interfaces
%% - To provide more information for bug detection tools, such as Dialyzer
%% - To be leveraged by documentation tools
```

# Relationships
## Builds Upon
This is a foundational concept.

## Enables
- **predefined-types** -- The type language defines the set of predefined types
- **type-union** -- Union is a core composition mechanism in the type language
- **type-declaration** -- User-defined types use the type language
- **function-specification** -- Specs use the type language to annotate functions

## Related
- **dynamic-type** -- Special type for gradual typing

## Contrasts With
None within this source.

# Common Errors
- **Error**: Assuming type annotations are enforced at runtime
  **Correction**: Erlang type annotations are checked only by external tools like Dialyzer; the runtime remains dynamically typed

# Common Confusions
- **Confusion**: Believing the type language makes Erlang statically typed
  **Clarification**: Erlang remains dynamically typed. The type language provides optional annotations for tooling and documentation, not runtime enforcement

# Source Reference
"Types and Function Specifications" chapter, section "The Erlang Type Language."

# Verification Notes
- Definition source: Direct from opening paragraphs of the chapter
- Confidence rationale: High -- the source explicitly describes what the type language is and its purposes
- Uncertainties: None
- Cross-reference status: All slugs reference planned cards in this extraction
