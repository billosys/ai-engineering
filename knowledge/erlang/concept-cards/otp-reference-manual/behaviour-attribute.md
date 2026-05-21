---
# === CORE IDENTIFICATION ===
concept: Behaviour Attribute
slug: behaviour-attribute

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
  - "-behaviour"
  - "-behavior"
  - "behavior attribute"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - export-attribute
extends: []
related:
  - callback-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare that a module implements a behaviour in Erlang?"
  - "What is the -behaviour attribute?"
  - "What standard OTP behaviours exist?"
---

# Quick Definition
The `-behaviour(Behaviour)` attribute declares that a module is the callback module for a specified behaviour, either a user-defined behaviour or one of the OTP standard behaviours.

# Core Definition
The Erlang Reference Manual states: "It is possible to specify that the module is the callback module for a _behaviour_." The syntax is `-behaviour(Behaviour).` where "the atom `Behaviour` gives the name of the behaviour, which can be a user-defined behaviour or one of the following OTP standard behaviours: `gen_server`, `gen_statem`, `gen_event`, `supervisor`." The manual also notes: "The spelling `behavior` is also accepted." (Modules, "Behaviour Module Attribute" section).

# Prerequisites
- **erlang-module** -- The behaviour attribute is a module attribute
- **export-attribute** -- Callback functions must be exported

# Key Properties
1. Syntax: `-behaviour(Behaviour).` where `Behaviour` is an atom
2. Both British (`behaviour`) and American (`behavior`) spellings are accepted
3. OTP standard behaviours: `gen_server`, `gen_statem`, `gen_event`, `supervisor`
4. User-defined behaviours are also supported
5. The compiler will warn if required callback functions are missing
6. Callback functions can be specified via `behaviour_info/1` or `-callback` attributes

# Construction / Recognition
## To Construct/Create:
1. Add `-behaviour(gen_server).` (or another behaviour) to the module attributes
2. Implement all required callback functions and export them

## To Identify/Recognize:
1. The `-behaviour(...)` or `-behavior(...)` attribute in a module
2. The module implements callback functions defined by the specified behaviour

# Context & Application
The behaviour attribute is central to OTP programming. OTP behaviours encapsulate common patterns (client-server, event handling, supervision, state machines) into reusable frameworks. The callback module provides the application-specific logic while the behaviour module handles the generic infrastructure. Declaring a behaviour enables compile-time checking that all required callbacks are implemented.

# Examples
**Example 1** (Behaviour Module Attribute section):
```erlang
-module(my_server).
-behaviour(gen_server).

%% gen_server callbacks
-export([init/1, handle_call/3, handle_cast/2, handle_info/2]).
```

**Example 2** (specifying callbacks for a user-defined behaviour):
```erlang
behaviour_info(callbacks) -> Callbacks.
```

Or using `-callback` attributes:
```erlang
-callback Name(Arguments) -> Result.
```

# Relationships
## Builds Upon
- **erlang-module** -- Behaviour is a module attribute
- **export-attribute** -- Callbacks must be exported

## Enables
- **callback-attribute** -- Behaviours define their required callbacks via `-callback`

## Related
- **callback-attribute** -- The mechanism for specifying what callbacks a behaviour requires

## Contrasts With
None.

# Common Errors
- **Error**: Declaring a behaviour but not implementing all required callbacks
  **Correction**: Implement and export every callback function specified by the behaviour; the compiler issues warnings for missing callbacks

- **Error**: Misspelling the behaviour name
  **Correction**: Use the exact atom name of the behaviour module (e.g., `gen_server`, not `genserver`)

# Common Confusions
- **Confusion**: Thinking `-behaviour` and `-behavior` are different
  **Clarification**: Both spellings are accepted and equivalent

- **Confusion**: Thinking the behaviour attribute causes the module to automatically inherit functionality
  **Clarification**: The attribute only declares intent; the module must still implement all required callback functions

# Source Reference
"Modules" chapter, "Behaviour Module Attribute" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition with enumerated standard behaviours
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
