---
# === CORE IDENTIFICATION ===
concept: Current and Old Code Versions
slug: current-and-old-code

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
  - "current code"
  - "old code"
  - "code versions"
  - "code purging"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - code-server
  - beam-object-code
extends: []
related:
  - code-replacement
  - on-load-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are current and old code in Erlang?"
  - "How many versions of a module can exist simultaneously?"
  - "What happens when a third version of a module is loaded?"
---

# Quick Definition
The Erlang runtime can maintain two versions of a module's code simultaneously: "current" (the latest loaded version) and "old" (the previous version). Both can be executed concurrently. Loading a third version purges old code and terminates any processes still running it.

# Core Definition
The Erlang Reference Manual states: "The code of a module can exist in two variants in a system: _current_ and _old_. When a module is loaded into the system for the first time, the code becomes 'current'. If then a new instance of the module is loaded, the code of the previous instance becomes 'old' and the new instance becomes 'current'." It continues: "Both old and current code are valid, and can be evaluated concurrently. Fully qualified function calls always refer to current code. Old code can still be evaluated because of processes lingering in the old code." On purging: "If a third instance of the module is loaded, the code server removes (purges) the old code and any processes lingering in it are terminated. Then the third instance becomes 'current' and the previously current code becomes 'old'." (Compilation and Code Loading, "Code Replacement" section).

# Prerequisites
- **code-server** -- The code server manages the two-version scheme
- **beam-object-code** -- Both versions are compiled BEAM code

# Key Properties
1. Maximum two versions can coexist: current and old
2. First load: code becomes current (no old version exists)
3. Second load: previous current becomes old; new code becomes current
4. Third load: old code is purged (and lingering processes terminated); current becomes old; new becomes current
5. Fully qualified calls always dispatch to current code
6. Local (unqualified) calls remain in the same version
7. Both old and current code can execute concurrently
8. A process must make a fully qualified call to switch from old to current code

# Construction / Recognition
## To Construct/Create:
This mechanism is automatic -- loading a new version of a module triggers the version rotation.

## To Identify/Recognize:
1. Check with `code:is_loaded(Module)` -- returns `{file, Filename}` or `false`
2. Check for old code with `code:is_old(Module)` (available through code module)
3. `erlang:check_old_code(Module)` returns `true` if old code exists

# Context & Application
The two-version model is the foundation of Erlang's hot code loading capability. It allows a running system to transition between code versions gracefully: processes can finish their current work in old code and transition to new code at safe points (fully qualified calls). The purge mechanism ensures that at most two versions exist, preventing unbounded memory growth from accumulated code versions.

# Examples
**Example 1** (version lifecycle):
```text
1. Load module m (version 1) -> version 1 is current
2. Load module m (version 2) -> version 2 is current, version 1 is old
3. Processes in version 1 can still run; they switch to version 2 on fully qualified calls
4. Load module m (version 3) -> version 1 is purged (lingering processes killed),
   version 3 is current, version 2 is old
```

**Example 2** (Code Replacement section, switching code):
```erlang
-module(m).
-export([loop/0]).

loop() ->
    receive
        code_switch ->
            m:loop();       %% fully qualified -> switches to current code
        Msg ->
            ...
            loop()          %% local call -> stays in same version
    end.
```

# Relationships
## Builds Upon
- **code-server** -- Manages the two-version scheme
- **beam-object-code** -- Both versions are BEAM code

## Enables
- **code-replacement** -- The two-version model enables hot code loading

## Related
- **on-load-function** -- On-load interacts with the current/old code transition

## Contrasts With
None.

# Common Errors
- **Error**: Loading a third version without ensuring no processes linger in old code
  **Correction**: Processes running old code will be terminated during purge. Use `code:soft_purge/1` to check if old code is still in use before loading a third version.

- **Error**: Expecting more than two versions to coexist
  **Correction**: The system only supports two versions (current and old). A third load always purges the oldest.

# Common Confusions
- **Confusion**: Thinking "purge" only removes the code
  **Clarification**: Purging removes the old code AND terminates any processes still executing it. This can cause unexpected process crashes if not managed carefully.

- **Confusion**: Thinking local calls in a loop will eventually switch to new code
  **Clarification**: Local calls (e.g., `loop()` without module prefix) always stay in the same code version. Only fully qualified calls (e.g., `m:loop()`) switch to current code.

# Source Reference
"Compilation and Code Loading" chapter, "Code Replacement" section.

# Verification Notes
- Definition source: Direct quotes from source
- Confidence rationale: High -- explicit description of the two-version lifecycle
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
