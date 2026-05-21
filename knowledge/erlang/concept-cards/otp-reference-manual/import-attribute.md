---
# === CORE IDENTIFICATION ===
concept: Import Attribute
slug: import-attribute

# === CLASSIFICATION ===
category: api-design
subcategory: module-interface
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
  - "-import"
  - "import declaration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - export-attribute
extends: []
related:
  - module-declaration
  - function-arity
contrasts_with:
  - export-attribute

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I call external functions without a module prefix in Erlang?"
  - "What is the -import attribute?"
  - "Can I import functions from another module in Erlang?"
---

# Quick Definition
The `-import(Module, Functions)` attribute allows functions from another module to be called as if they were local functions, without a module prefix.

# Core Definition
The Erlang Reference Manual states: "`-import(Module, Functions).` -- Imported functions. Can be called the same way as local functions, that is, without any module prefix. `Module`, an atom, specifies which module to import functions from. `Functions` is a list similar to that for `export`." (Modules, "Pre-Defined Module Attributes" section).

# Prerequisites
- **erlang-module** -- Imports are an attribute of a module
- **export-attribute** -- The imported functions must be exported by the source module

# Key Properties
1. Syntax: `-import(Module, [Name1/Arity1, ..., NameN/ArityN]).`
2. Imported functions can be called without the module prefix
3. The imported functions must be exported by the source module
4. Import is a compile-time convenience -- it does not affect runtime behavior
5. The `-import` attribute is rarely used in practice; most Erlang code uses fully qualified calls

# Construction / Recognition
## To Construct/Create:
1. Write `-import(Module, [Name1/Arity1, ...]).`
2. Example: `-import(lists, [map/2, filter/2]).`

## To Identify/Recognize:
1. The `-import(Module, [...])` attribute with two arguments: a module atom and a function list

# Context & Application
The import attribute exists for syntactic convenience, allowing frequently used external functions to be called without their module prefix. However, in practice, the Erlang community strongly prefers explicit fully qualified calls (`Module:Function(Args)`) because they make the code's dependencies immediately visible. The import attribute can reduce readability by obscuring where a function comes from.

# Examples
**Example 1** (from attribute definition):
```erlang
-module(my_module).
-import(lists, [map/2, filter/2]).

%% Can now call map/2 and filter/2 without the lists: prefix
process(L) ->
    map(fun(X) -> X * 2 end, filter(fun(X) -> X > 0 end, L)).
```

# Relationships
## Builds Upon
- **erlang-module** -- Import is a module attribute
- **export-attribute** -- Only exported functions can be imported

## Enables
None directly.

## Related
- **function-arity** -- Import lists use Name/Arity notation

## Contrasts With
- **export-attribute** -- Export makes local functions visible externally; import makes external functions callable locally without module prefix

# Common Errors
- **Error**: Importing a function with the same name and arity as a local function
  **Correction**: This causes a compilation error; either rename the local function or do not import

- **Error**: Importing a function that is not exported by the source module
  **Correction**: Ensure the function is exported from the module being imported from

# Common Confusions
- **Confusion**: Thinking `-import` loads or requires the module
  **Clarification**: `-import` is purely a syntactic convenience at compile time. The module must still be available at runtime. It does not establish a load dependency.

- **Confusion**: Expecting `-import` to work like Python's `from module import *`
  **Clarification**: Erlang has no wildcard import; you must list each function explicitly with its arity

# Source Reference
"Modules" chapter, "Pre-Defined Module Attributes" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
