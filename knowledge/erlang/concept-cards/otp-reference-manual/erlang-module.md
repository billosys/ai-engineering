---
# === CORE IDENTIFICATION ===
concept: Erlang Module
slug: erlang-module

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Modules"
chapter_number: null
pdf_page: null
section: "Module Syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "module"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - module-declaration
  - export-attribute
  - function-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang module?"
  - "How is Erlang code organized?"
  - "What does a module consist of?"
---

# Quick Definition
An Erlang module is the fundamental unit of code organization. It consists of a sequence of attributes and function declarations, each terminated by a period (`.`).

# Core Definition
The Erlang Reference Manual states: "Erlang code is divided into _modules_. A module consists of a sequence of attributes and function declarations, each terminated by a period (`.`)." (Modules, "Module Syntax" section). The module is the unit of compilation, code loading, and namespace isolation in Erlang.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. A module consists of attributes and function declarations
2. Each attribute and function declaration is terminated by a period (`.`)
3. Module attributes define properties of the module
4. The `-module(Name)` attribute is the only mandatory attribute
5. The module name must match the file name (minus the `.erl` extension) for code loading to work
6. Modules are the unit of compilation -- each module compiles to a `.beam` file

# Construction / Recognition
## To Construct/Create:
1. Create a file named `ModuleName.erl`
2. Begin with the `-module(ModuleName).` declaration
3. Add export and other module attributes
4. Define functions
5. Terminate each declaration with a period

## To Identify/Recognize:
1. A `.erl` file containing a `-module(...)` attribute
2. A sequence of attributes followed by function declarations
3. Each element terminated by a period

# Context & Application
Modules are the primary organizational unit in Erlang. All code lives in modules. The module system provides namespace isolation (functions must be fully qualified with the module name when called externally), supports hot code loading (code can be replaced at the module level in a running system), and enables compilation as independent units.

# Examples
**Example 1** (Module Syntax section): A complete simple module:
```erlang
-module(m).          % module attribute
-export([fact/1]).   % module attribute

fact(N) when N>0 ->  % beginning of function declaration
    N * fact(N-1);   %  |
fact(0) ->           %  |
    1.               % end of function declaration
```

# Relationships
## Builds Upon
This is a foundational concept with no prerequisites.

## Enables
- **module-declaration** -- Every module must have a module declaration
- **export-attribute** -- Modules control function visibility through exports
- **erlang-compilation** -- Modules are the unit of compilation
- **code-replacement** -- Code replacement operates at the module level

## Related
- **function-declaration** -- Modules contain function declarations

## Contrasts With
None.

# Common Errors
- **Error**: Forgetting to terminate attributes or function declarations with a period
  **Correction**: Every attribute and function declaration must end with `.`

- **Error**: Module name does not match the file name
  **Correction**: The atom in `-module(Name)` must match the file name minus `.erl`

# Common Confusions
- **Confusion**: Thinking modules can be nested or that one module can contain another
  **Clarification**: Erlang has a flat module namespace -- there is no module nesting. Module names can contain dots by convention (e.g., `my.module`) but this has no structural meaning.

# Source Reference
"Modules" chapter, "Module Syntax" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
