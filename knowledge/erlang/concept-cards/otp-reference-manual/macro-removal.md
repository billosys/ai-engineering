---
# === CORE IDENTIFICATION ===
concept: Macro Removal
slug: macro-removal

# === CLASSIFICATION ===
category: core-idioms
subcategory: preprocessor
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Preprocessor"
chapter_number: null
pdf_page: null
section: "Removing a macro definition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-undef"
  - "undef directive"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-definition
extends: []
related:
  - conditional-compilation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I remove a macro definition in Erlang?"
  - "What is the -undef directive?"
  - "Can I redefine a macro in Erlang?"
---

# Quick Definition
The `-undef(Macro)` directive removes a previously defined macro, making it undefined from that point forward in the source file.

# Core Definition
The Erlang Reference Manual states: "A definition of a macro can be removed as follows: `-undef(Macro).`" (Preprocessor, "Removing a macro definition" section).

# Prerequisites
- **macro-definition** -- You must understand macro definition to understand removal

# Key Properties
1. Syntax: `-undef(Macro).` where `Macro` is the macro name (without `?`)
2. The macro becomes undefined after the `-undef` directive
3. The macro can be redefined after being undefined
4. Useful in combination with conditional compilation and include files

# Construction / Recognition
## To Construct/Create:
1. To remove a macro: `-undef(TIMEOUT).`
2. To redefine: `-undef(TIMEOUT). -define(TIMEOUT, 500).`

## To Identify/Recognize:
1. The `-undef(Name)` directive

# Context & Application
The `-undef` directive is useful when an include file defines a macro that needs to be overridden, or when a macro should only be available in a specific section of code. It is also useful in conditional compilation scenarios where a macro must be explicitly removed to change the compilation path for subsequent code.

# Examples
**Example 1** (removing and redefining):
```erlang
-define(TIMEOUT, 200).
%% ... code using ?TIMEOUT as 200 ...

-undef(TIMEOUT).
-define(TIMEOUT, 500).
%% ... code using ?TIMEOUT as 500 ...
```

# Relationships
## Builds Upon
- **macro-definition** -- Undef removes what `-define` creates

## Enables
Allows macro redefinition by first removing the existing definition.

## Related
- **conditional-compilation** -- Often used in combination with `-ifdef`/`-ifndef`

## Contrasts With
None.

# Common Errors
- **Error**: Using a macro after it has been undefined
  **Correction**: The macro does not exist after `-undef`; either redefine it or check with `-ifdef`

# Common Confusions
- **Confusion**: Thinking `-undef` affects other modules
  **Clarification**: `-undef` only affects the current compilation unit (source file). Other modules that define or include the same macro are unaffected.

# Source Reference
"Preprocessor" chapter, "Removing a macro definition" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition, though brief
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
