---
# === CORE IDENTIFICATION ===
concept: Callback Attribute
slug: callback-attribute

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Modules"
chapter_number: null
pdf_page: null
section: "Behaviour Module Attribute"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-callback"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - behaviour-attribute
  - function-specification
extends: []
related:
  - export-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define what callbacks a behaviour requires?"
  - "What is the -callback attribute?"
  - "What is the difference between behaviour_info/1 and -callback?"
---

# Quick Definition
The `-callback` attribute declares a callback function that a behaviour requires its callback modules to implement. It includes type information, making it preferable to the older `behaviour_info/1` approach.

# Core Definition
The Erlang Reference Manual states: "The callback functions of the module can be specified either directly by the exported function `behaviour_info/1` [...] or by a `-callback` attribute for each callback function." The syntax is: `-callback Name(Arguments) -> Result.` The manual recommends: "The `-callback` attribute is to be preferred since the extra type information can be used by tools to produce documentation or find discrepancies." (Modules, "Behaviour Module Attribute" section).

# Prerequisites
- **erlang-module** -- Callbacks are module attributes
- **behaviour-attribute** -- Callbacks define the contract for a behaviour
- **function-specification** -- The `-callback` syntax mirrors `-spec` type specifications

# Key Properties
1. Syntax: `-callback Name(Arguments) -> Result.`
2. Preferred over the older `behaviour_info/1` exported function approach
3. Includes type information for each callback function
4. Enables tools (like Dialyzer) to check implementations for type correctness
5. Each callback function gets its own `-callback` attribute
6. The compiler warns if a module declaring a `-behaviour` does not implement all callbacks

# Construction / Recognition
## To Construct/Create:
1. In the behaviour module, add: `-callback init(Args :: term()) -> {ok, State :: term()}.`
2. Repeat for each required callback function

## To Identify/Recognize:
1. The `-callback` attribute in a module that defines a behaviour
2. Syntax resembles `-spec` but uses `-callback` instead

# Context & Application
The `-callback` attribute is used when defining new behaviours. It serves as both documentation and a contract: it tells implementors exactly what functions they must provide and what types those functions must conform to. Tools like Dialyzer use callback specifications to verify that callback modules implement the correct function signatures.

# Examples
**Example 1** (from Behaviour Module Attribute section):
```erlang
-callback Name(Arguments) -> Result.
```

**Example 2** (practical example defining a behaviour):
```erlang
-module(my_behaviour).

-callback start(Config :: map()) -> {ok, pid()} | {error, term()}.
-callback stop(Reason :: term()) -> ok.
```

**Older approach** (using behaviour_info/1):
```erlang
behaviour_info(callbacks) -> [{start, 1}, {stop, 1}].
```

# Relationships
## Builds Upon
- **behaviour-attribute** -- Callbacks define the contract for behaviours
- **function-specification** -- Callback syntax is modeled on `-spec`

## Enables
- Compile-time checking that callback modules implement required functions

## Related
- **export-attribute** -- Callback functions must be exported in the implementing module

## Contrasts With
None directly, though it supersedes the older `behaviour_info/1` approach.

# Common Errors
- **Error**: Using `behaviour_info/1` instead of `-callback` attributes
  **Correction**: Prefer `-callback` as it provides type information for tooling

- **Error**: Forgetting to export callback functions in the implementing module
  **Correction**: All callback functions must be listed in `-export`

# Common Confusions
- **Confusion**: Thinking `-callback` is placed in the implementing module
  **Clarification**: `-callback` attributes are placed in the behaviour-defining module, not in the callback module. The callback module uses `-behaviour(Name)` to declare that it implements the behaviour.

# Source Reference
"Modules" chapter, "Behaviour Module Attribute" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition and recommendation in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
