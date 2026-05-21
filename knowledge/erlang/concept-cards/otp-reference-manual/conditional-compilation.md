---
# === CORE IDENTIFICATION ===
concept: Conditional Compilation
slug: conditional-compilation

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
section: "Conditional Compilation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-ifdef"
  - "-ifndef"
  - "-if"
  - "-elif"
  - "-else"
  - "-endif"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-definition
  - preprocessor-directives
extends: []
related:
  - predefined-macros
  - macro-removal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I conditionally compile code in Erlang?"
  - "What are -ifdef and -ifndef?"
  - "How do I write version-specific code in Erlang?"
---

# Quick Definition
Erlang supports conditional compilation through directives that include or exclude code based on whether macros are defined or conditions evaluate to true: `-ifdef`, `-ifndef`, `-if`, `-elif`, `-else`, and `-endif`.

# Core Definition
The Erlang Reference Manual defines the following conditional compilation directives:
- `-ifdef(Macro).` -- Evaluate the following lines only if `Macro` is defined
- `-ifndef(Macro).` -- Evaluate the following lines only if `Macro` is not defined
- `-else.` -- Only allowed after `ifdef`, `ifndef`, `if`, and `elif`; lines following `else` are evaluated if the preceding directive evaluated to false
- `-if(Condition).` -- Evaluates the following lines only if `Condition` evaluates to true
- `-elif(Condition).` -- Only allowed after `if` or another `elif`; if the preceding directive does not evaluate to true and `Condition` evaluates to true, the lines following are evaluated
- `-endif.` -- Specifies the end of a series of control flow directives

The manual notes: "Macro directives cannot be used inside functions." The `Condition` in `-if` and `-elif` must be a guard expression and additionally supports the `defined(Name)` pseudo-function. (Preprocessor, "Conditional Compilation" section).

# Prerequisites
- **macro-definition** -- Conditional compilation tests for macro existence or values
- **preprocessor-directives** -- Conditional directives are preprocessor constructs

# Key Properties
1. `-ifdef`/`-ifndef` test only whether a macro is defined, not its value
2. `-if`/`-elif` evaluate guard expressions and support the `defined(Name)` pseudo-function
3. Every `-ifdef`, `-ifndef`, or `-if` must be terminated by `-endif.`
4. `-else` can follow any of: `-ifdef`, `-ifndef`, `-if`, `-elif`
5. Conditional directives cannot appear inside function bodies
6. Macros can be defined on the command line with `erlc -Dname` or `c(Module, {d, name})`
7. The `defined(Name)` pseudo-function returns `true` if `Name` is a defined macro

# Construction / Recognition
## To Construct/Create:
1. Simple conditional: `-ifdef(debug). ... -else. ... -endif.`
2. Value-based conditional: `-if(?OTP_RELEASE >= 26). ... -endif.`
3. Combined: `-if(?OTP_RELEASE >= 26 andalso defined(debug)). ... -endif.`

## To Identify/Recognize:
1. Any of the directives: `-ifdef`, `-ifndef`, `-if`, `-elif`, `-else`, `-endif`
2. Code blocks delimited by these directives

# Context & Application
Conditional compilation is essential for: writing code that works across multiple OTP versions (using `?OTP_RELEASE`), enabling debug/test-only code paths, and adapting to platform differences. The `-ifdef(debug)` pattern combined with compiler flags is the standard way to add debug logging that has zero runtime cost in production builds.

# Examples
**Example 1** (Conditional Compilation section, debug logging):
```erlang
-module(m).
...

-ifdef(debug).
-define(LOG(X), io:format("{~p,~p}: ~p~n", [?MODULE,?LINE,X])).
-else.
-define(LOG(X), true).
-endif.

...
```
Compile with debug enabled:
```erlang
% erlc -Ddebug m.erl

or

1> c(m, {d, debug}).
{ok,m}
```

**Example 2** (Conditional Compilation section, OTP version):
```erlang
-module(m).
...
-if(?OTP_RELEASE >= 26).
%% Code that will work in OTP 26 or higher
-elif(?OTP_RELEASE >= 25).
%% Code that will work in OTP 25 or higher
-else.
%% Code that will work in OTP 24 or lower.
-endif.
...
```

**Example 3** (Conditional Compilation section, combined condition):
```erlang
-if(?OTP_RELEASE >= 26 andalso defined(debug)).
%% Debugging code that requires OTP 26 or later.
-else.
%% Non-debug code that works in any release.
-endif.
```

# Relationships
## Builds Upon
- **macro-definition** -- Conditional compilation tests macro definitions
- **preprocessor-directives** -- Conditional directives are preprocessor constructs

## Enables
- Platform-adaptive and version-adaptive code
- Zero-cost debug instrumentation

## Related
- **predefined-macros** -- `?OTP_RELEASE` is commonly used in conditions
- **macro-removal** -- `-undef` can change conditional compilation outcomes

## Contrasts With
None.

# Common Errors
- **Error**: Using conditional directives inside function bodies
  **Correction**: Macro directives cannot be used inside functions; restructure so the conditional wraps entire function definitions or macro definitions

- **Error**: Forgetting `-endif.` to close a conditional block
  **Correction**: Every `-ifdef`, `-ifndef`, or `-if` must have a matching `-endif.`

- **Error**: Using non-guard expressions in `-if`/`-elif` conditions
  **Correction**: The condition must be a guard expression (no `case`, `if`, function calls other than `defined/1`)

# Common Confusions
- **Confusion**: Thinking `-ifdef` tests the macro's value
  **Clarification**: `-ifdef` only tests whether the macro is defined, regardless of its value. Use `-if(?MACRO == value)` to test a value.

- **Confusion**: Thinking `defined(Name)` is a regular function
  **Clarification**: `defined/1` is a pseudo-function only available in `-if`/`-elif` conditions; it cannot be called at runtime or in guard expressions outside these directives

# Source Reference
"Preprocessor" chapter, "Conditional Compilation" section.

# Verification Notes
- Definition source: Direct quotes from source with all six directives enumerated
- Confidence rationale: High -- explicit definitions with multiple examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
