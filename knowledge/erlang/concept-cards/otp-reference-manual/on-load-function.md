---
# === CORE IDENTIFICATION ===
concept: On-Load Function
slug: on-load-function

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Modules"
chapter_number: null
pdf_page: null
section: "Pre-Defined Module Attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-on_load"
  - "on_load attribute"
  - "on_load directive"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - code-server
extends: []
related:
  - nifs-attribute
  - code-replacement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I run a function automatically when a module is loaded?"
  - "What is the -on_load attribute?"
  - "How do I load NIFs when a module is loaded?"
---

# Quick Definition
The `-on_load(Function)` attribute names a zero-arity function that runs automatically when a module is loaded. The function must return `ok` for the module to become current code.

# Core Definition
The Erlang Reference Manual states: "`-on_load(Function).` -- This attribute names a function that is to be run automatically when a module is loaded." The "Running a Function When a Module is Loaded" section elaborates: "It is not necessary to export the function. It is called in a freshly spawned process (which terminates as soon as the function returns). The function must return `ok` if the module is to become the new current code for the module and become callable." (Modules, "Pre-Defined Module Attributes" and "Compilation and Code Loading", "Running a Function When a Module is Loaded" sections).

# Prerequisites
- **erlang-module** -- On-load is a module attribute
- **code-server** -- The code server triggers the on_load function during module loading

# Key Properties
1. Syntax: `-on_load(Name/0).` where `Name` is the function name
2. The function must have arity 0
3. It does not need to be exported
4. It runs in a freshly spawned process that terminates when the function returns
5. Must return `ok` for the module to become current code
6. Returning any non-`ok` value or raising an exception causes the new code to be unloaded
7. If there is already current code for the module, that code remains callable until the on_load function returns
8. In embedded mode, all on_load functions are called after all modules are loaded; the system terminates unless all return `ok`

# Construction / Recognition
## To Construct/Create:
1. Add `-on_load(my_init/0).` to the module attributes
2. Define the function: `my_init() -> ok.`

## To Identify/Recognize:
1. The `-on_load(Name/0)` attribute in a module
2. The named function returns `ok` on success

# Context & Application
The most common use of `-on_load` is to load NIFs (Native Implemented Functions) via `erlang:load_nif/2`. When a module contains NIF stubs, the on_load function loads the shared library containing the native implementations. If NIF loading fails, the module is not made available, preventing calls to unimplemented NIF stubs.

# Examples
**Example 1** (Compilation and Code Loading, "Running a Function When a Module is Loaded" section):
```erlang
-module(m).
-on_load(load_my_nifs/0).

load_my_nifs() ->
    NifPath = ...,    %Set up the path to the NIF library.
    Info = ...,       %Initialize the Info term
    erlang:load_nif(NifPath, Info).
```

# Relationships
## Builds Upon
- **erlang-module** -- On-load is a module attribute
- **code-server** -- The code server invokes the on_load function

## Enables
- **nifs-attribute** -- On-load is typically used in conjunction with NIF loading

## Related
- **code-replacement** -- On-load interacts with the current/old code mechanism

## Contrasts With
None.

# Common Errors
- **Error**: The on_load function returns a non-`ok` value
  **Correction**: Ensure the function returns the atom `ok` on success; any other return value causes the module code to be unloaded

- **Error**: The on_load function raises an exception
  **Correction**: Handle errors gracefully; an exception in the on_load function prevents the module from becoming current code

# Common Confusions
- **Confusion**: Thinking the on_load function must be exported
  **Clarification**: The on_load function does not need to be exported; it is called internally by the code server

- **Confusion**: Thinking the on_load function runs in the calling process
  **Clarification**: It runs in a freshly spawned process that terminates when the function returns

# Source Reference
"Modules" chapter, "Pre-Defined Module Attributes" section and "Compilation and Code Loading" chapter, "Running a Function When a Module is Loaded" section.

# Verification Notes
- Definition source: Direct quotes from source
- Confidence rationale: High -- explicit definition with detailed behavior description
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
