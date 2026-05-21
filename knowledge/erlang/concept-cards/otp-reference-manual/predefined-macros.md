---
# === CORE IDENTIFICATION ===
concept: Predefined Macros
slug: predefined-macros

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
section: "Predefined Macros"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "built-in macros"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-definition
extends: []
related:
  - file-attribute
  - conditional-compilation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What predefined macros are available in Erlang?"
  - "What does ?MODULE expand to?"
  - "How do I get the current line number at compile time?"
---

# Quick Definition
Erlang provides several predefined macros that expand to compile-time information: `?MODULE`, `?MODULE_STRING`, `?FILE`, `?LINE`, `?MACHINE`, `?FUNCTION_NAME`, `?FUNCTION_ARITY`, `?OTP_RELEASE`, and the feature-checking macros.

# Core Definition
The Erlang Reference Manual defines the following predefined macros:
- `?MODULE` -- The name of the current module, as an atom
- `?MODULE_STRING` -- The name of the current module, as a string
- `?FILE` -- The file name of the current module, as a string
- `?LINE` -- The current line number, as an integer
- `?MACHINE` -- The machine name, `'BEAM'`
- `?FUNCTION_NAME` -- The name of the current function, as an atom
- `?FUNCTION_ARITY` -- The arity for the current function, as an integer
- `?OTP_RELEASE` -- The OTP release of the runtime system running the compiler, as an integer
- `?FEATURE_AVAILABLE(Feature)` -- Expands to `true` if the feature is available
- `?FEATURE_ENABLED(Feature)` -- Expands to `true` if the feature is enabled

(Preprocessor, "Predefined Macros" section).

# Prerequisites
- **macro-definition** -- Predefined macros are used with the same `?` syntax as user-defined macros

# Key Properties
1. All predefined macros use the `?Name` syntax
2. Cannot be redefined or overloaded (unlike user-defined macros)
3. `?MODULE` and `?MODULE_STRING` differ in type: atom vs string
4. `?FUNCTION_NAME` and `?FUNCTION_ARITY` are only valid within function bodies
5. `?OTP_RELEASE` was introduced in Erlang/OTP 21
6. `?FEATURE_AVAILABLE` and `?FEATURE_ENABLED` were introduced in Erlang/OTP 25
7. `?OTP_RELEASE` returns the compile-time OTP release, not the runtime release

# Construction / Recognition
## To Construct/Create:
Predefined macros cannot be created -- they are built in. They are used like any other macro: `?MODULE`, `?LINE`, etc.

## To Identify/Recognize:
1. The standard names: `MODULE`, `MODULE_STRING`, `FILE`, `LINE`, `MACHINE`, `FUNCTION_NAME`, `FUNCTION_ARITY`, `OTP_RELEASE`
2. Always uppercased by convention (like user-defined macros)

# Context & Application
Predefined macros are heavily used in debugging, logging, and error reporting. A common pattern is to define logging macros that embed `?MODULE`, `?FUNCTION_NAME`, and `?LINE` to provide context in log messages. `?OTP_RELEASE` is particularly useful in combination with conditional compilation (`-if`/`-elif`) to write code that adapts to different OTP versions.

# Examples
**Example 1** (common logging macro using predefined macros):
```erlang
-define(LOG(X), io:format("{~p,~p}: ~p~n", [?MODULE,?LINE,X])).
```

**Example 2** (OTP version conditional from Conditional Compilation section):
```erlang
-if(?OTP_RELEASE >= 26).
%% Code that will work in OTP 26 or higher
-elif(?OTP_RELEASE >= 25).
%% Code that will work in OTP 25 or higher
-else.
%% Code that will work in OTP 24 or lower.
-endif.
```

# Relationships
## Builds Upon
- **macro-definition** -- Uses the same `?` invocation syntax

## Enables
- **conditional-compilation** -- `?OTP_RELEASE` and feature macros enable version-conditional code

## Related
- **file-attribute** -- The `-file` attribute modifies the values of `?FILE` and `?LINE`

## Contrasts With
None.

# Common Errors
- **Error**: Using `?FUNCTION_NAME` or `?FUNCTION_ARITY` outside a function body
  **Correction**: These macros are only valid within function definitions

- **Error**: Using `?OTP_RELEASE` to determine the runtime OTP version
  **Correction**: `?OTP_RELEASE` reflects the compile-time version. Use `erlang:system_info(otp_release)` for the runtime version.

# Common Confusions
- **Confusion**: Thinking `?MODULE` returns a string
  **Clarification**: `?MODULE` returns an atom; use `?MODULE_STRING` if you need a string

- **Confusion**: Thinking `?OTP_RELEASE` reflects the runtime environment
  **Clarification**: It returns the OTP release of the system that compiled the module, not the one running it. These may differ if cross-compiling or deploying to a different version.

# Source Reference
"Preprocessor" chapter, "Predefined Macros" section.

# Verification Notes
- Definition source: Direct enumeration from source
- Confidence rationale: High -- explicit list with descriptions in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
