---
# === CORE IDENTIFICATION ===
concept: Code Replacement
slug: code-replacement

# === CLASSIFICATION ===
category: core-idioms
subcategory: code-loading
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Compilation and Code Loading"
chapter_number: null
pdf_page: null
section: "Code Replacement"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "hot code loading"
  - "hot code swapping"
  - "code upgrade"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - code-server
  - export-attribute
  - current-and-old-code
extends: []
related:
  - erlang-module
  - on-load-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does hot code loading work in Erlang?"
  - "How do I upgrade code in a running Erlang system?"
  - "What is code replacement in Erlang?"
---

# Quick Definition
Erlang supports replacing code in a running system at the module level. The system can maintain two versions (current and old) of a module simultaneously, and processes switch to new code by making fully qualified function calls.

# Core Definition
The Erlang Reference Manual states: "Erlang supports change of code in a running system. Code replacement is done on the module level." It explains: "The code of a module can exist in two variants in a system: _current_ and _old_. When a module is loaded into the system for the first time, the code becomes 'current'. If then a new instance of the module is loaded, the code of the previous instance becomes 'old' and the new instance becomes 'current'." Further: "Both old and current code are valid, and can be evaluated concurrently. Fully qualified function calls always refer to current code. Old code can still be evaluated because of processes lingering in the old code." (Compilation and Code Loading, "Code Replacement" section).

The manual also explains the purge mechanism: "If a third instance of the module is loaded, the code server removes (purges) the old code and any processes lingering in it are terminated."

# Prerequisites
- **code-server** -- The code server manages code versions
- **export-attribute** -- Functions must be exported for fully qualified calls that trigger code switching
- **current-and-old-code** -- Understanding the two-version model

# Key Properties
1. Code replacement is done at the module level
2. At most two versions exist simultaneously: current and old
3. Fully qualified calls (`Module:Function(Args)`) always refer to current code
4. Local calls (without module prefix) continue executing in the same version
5. A process switches to new code by making a fully qualified function call
6. Loading a third version purges the old code and terminates lingering processes
7. The function being called must be exported for the code switch to work

# Construction / Recognition
## To Construct/Create:
1. Write code that uses fully qualified calls at strategic points (e.g., in a receive loop)
2. Export the function used for the fully qualified call
3. Load the new module version (using `l(Module)` or `code:load_file(Module)`)

## To Identify/Recognize:
1. Processes making fully qualified calls to their own module in receive loops
2. The `code_switch` or similar message pattern triggering `Module:loop()`

# Context & Application
Hot code loading is one of Erlang's signature features, enabling systems to be upgraded without downtime. It is fundamental to building highly available telecom and distributed systems. The OTP release handler automates code replacement for production systems, but understanding the underlying mechanism is essential for designing upgradeable processes.

# Examples
**Example 1** (Code Replacement section):
```erlang
-module(m).
-export([loop/0]).

loop() ->
    receive
        code_switch ->
            m:loop();
        Msg ->
            ...
            loop()
    end.
```

To make the process change code, send the message `code_switch` to it. The process then makes a fully qualified call to `m:loop()` and changes to current code. Notice that `m:loop/0` must be exported.

**Example 2** (code replacement with funs):
For code replacement of funs to work, use the syntax `fun Module:FunctionName/Arity`.

# Relationships
## Builds Upon
- **code-server** -- Manages the loading and purging of code versions
- **export-attribute** -- Fully qualified calls require exported functions
- **current-and-old-code** -- The two-version model underlies code replacement

## Enables
- Hot upgrades in production systems
- Zero-downtime deployments

## Related
- **erlang-module** -- Code replacement operates at the module level
- **on-load-function** -- On-load functions run during module loading

## Contrasts With
None.

# Common Errors
- **Error**: Forgetting to export the function used for code switching
  **Correction**: The function called with a fully qualified call must be exported; `m:loop/0` must appear in `-export`

- **Error**: Using a local call (`loop()`) instead of a fully qualified call (`m:loop()`) when code switching is desired
  **Correction**: Only fully qualified calls (`Module:Function()`) switch to current code; local calls stay in the same version

- **Error**: Loading a third version without checking for processes in old code
  **Correction**: Loading a third version purges old code and terminates lingering processes; use `code:soft_purge/1` to check first

# Common Confusions
- **Confusion**: Thinking all processes automatically switch to new code when it is loaded
  **Clarification**: Processes only switch to new code when they make a fully qualified function call. Processes executing local calls continue running old code.

- **Confusion**: Thinking anonymous funs (`fun(X) -> ...`) automatically update with code replacement
  **Clarification**: Anonymous funs capture the code version in which they were created. Use `fun Module:Function/Arity` syntax for funs that should resolve to current code.

# Source Reference
"Compilation and Code Loading" chapter, "Code Replacement" section.

# Verification Notes
- Definition source: Direct quotes from source
- Confidence rationale: High -- explicit definition with mechanism details and example
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
