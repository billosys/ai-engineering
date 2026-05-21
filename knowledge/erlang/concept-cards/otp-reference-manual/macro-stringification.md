---
# === CORE IDENTIFICATION ===
concept: Macro Stringification
slug: macro-stringification

# === CLASSIFICATION ===
category: core-idioms
subcategory: preprocessor
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Preprocessor"
chapter_number: null
pdf_page: null
section: "Stringifying Macro Arguments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "?? operator"
  - "double question mark operator"
  - "macro argument stringification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-definition
  - constant-vs-function-macros
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert a macro argument to a string in Erlang?"
  - "What does ?? do in Erlang macros?"
  - "How can I stringify a macro argument?"
---

# Quick Definition
The `??Arg` construction inside a macro definition expands a macro argument to a string containing the tokens of the argument. It is similar to the `#arg` stringifying operator in C.

# Core Definition
The Erlang Reference Manual states: "The construction `??Arg`, where `Arg` is a macro argument, is expanded to a string containing the tokens of the argument. This is similar to the `#arg` stringifying construction in C." (Preprocessor, "Stringifying Macro Arguments" section).

# Prerequisites
- **macro-definition** -- Stringification is used within macro definitions
- **constant-vs-function-macros** -- Only applicable to function macros (which have arguments)

# Key Properties
1. Syntax: `??Arg` where `Arg` is a macro parameter name
2. Produces a string representation of the argument's tokens
3. Only works within function macro definitions (constant macros have no arguments)
4. The resulting string contains the tokens with spaces between them
5. Useful for debugging and tracing -- shows both the expression and its value

# Construction / Recognition
## To Construct/Create:
1. In a macro definition, use `??Arg` to stringify the argument:
```erlang
-define(TESTCALL(Call), io:format("Call ~s: ~w~n", [??Call, Call])).
```

## To Identify/Recognize:
1. The `??` prefix before a macro parameter name in a `-define` directive

# Context & Application
Macro stringification is primarily used in debugging and testing macros. It allows a macro to output both the source code expression and its runtime value, providing valuable diagnostic information. Test frameworks use this to show the exact assertion expression that failed.

# Examples
**Example 1** (Stringifying Macro Arguments section):
```erlang
-define(TESTCALL(Call), io:format("Call ~s: ~w~n", [??Call, Call])).

?TESTCALL(myfunction(1,2)),
?TESTCALL(you:function(2,1)).
```

Results in:
```erlang
io:format("Call ~s: ~w~n",["myfunction ( 1 , 2 )",myfunction(1,2)]),
io:format("Call ~s: ~w~n",["you : function ( 2 , 1 )",you:function(2,1)]).
```

This produces trace output showing both the function called (as a string) and the resulting value.

# Relationships
## Builds Upon
- **macro-definition** -- Stringification is a feature of macro definitions
- **constant-vs-function-macros** -- Only available in function macros

## Enables
- Debugging and tracing macros that show source expressions

## Related
None.

## Contrasts With
None.

# Common Errors
- **Error**: Using `??` with a name that is not a macro parameter
  **Correction**: `??Arg` only works when `Arg` is a parameter of the enclosing function macro definition

- **Error**: Expecting the stringified output to have no spaces between tokens
  **Correction**: The expansion inserts spaces between tokens, so `myfunction(1,2)` becomes `"myfunction ( 1 , 2 )"`

# Common Confusions
- **Confusion**: Expecting `??Arg` to produce the same string as the source code
  **Clarification**: The stringification produces tokens separated by spaces, which may differ from the original formatting. For example, `myfunction(1,2)` becomes `"myfunction ( 1 , 2 )"` with spaces around parentheses and commas.

# Source Reference
"Preprocessor" chapter, "Stringifying Macro Arguments" section.

# Verification Notes
- Definition source: Direct quote from source with expansion example
- Confidence rationale: High -- explicit definition with clear example
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
