---
# === CORE IDENTIFICATION ===
concept: Code Path
slug: code-path

# === CLASSIFICATION ===
category: applications-releases
subcategory: runtime-configuration
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "System Principles"
chapter_number: null
pdf_page: null
section: "Code Loading Strategy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "search path"
  - "module search path"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - interactive-mode
extends: []
related:
  - code-loading-strategy
  - embedded-mode
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the code path in Erlang/OTP?"
  - "How does the code path relate to code loading strategy?"
---

# Quick Definition

The code path is an ordered list of directories that the Erlang code server searches to find and load modules, used primarily in interactive mode to locate modules on demand.

# Core Definition

As described in OTP System Principles: "Initially, the code path consists of the current working directory and all object code directories under `ROOT/lib`, where `ROOT` is the installation directory of Erlang/OTP." Directories under `ROOT/lib` can be named `Name[-Vsn]`, where the `-Vsn` suffix is optional. By default, the code server chooses the directory with the highest version number among those with the same `Name`. If an `ebin` directory exists under the `Name[-Vsn]` directory, that `ebin` directory is added to the code path.

# Prerequisites

- **interactive-mode** — the code path is primarily relevant in interactive mode, where the code server searches it to find unloaded modules

# Key Properties

1. Initially contains the current working directory plus all `ebin` directories under `ROOT/lib`.
2. Directories under `ROOT/lib` follow the naming convention `Name[-Vsn]`.
3. When multiple versions of the same `Name` exist, the highest version is chosen by default.
4. Can be extended at the head using `-pa Directories`.
5. Can be extended at the tail using `-pz Directories`.
6. Can be modified and queried at runtime using functions in the `code` module.

# Construction / Recognition

## To Construct/Create:
1. The initial code path is automatically built from `ROOT/lib` at startup.
2. Use `-pa /path/to/dir` to prepend directories (searched first).
3. Use `-pz /path/to/dir` to append directories (searched last).
4. Use `code:add_path/1`, `code:add_patha/1`, `code:add_pathz/1` at runtime.

## To Identify/Recognize:
1. Call `code:get_path()` to list the current code path.
2. The code path is an ordered list of directory strings.

# Context & Application

The code path is essential for interactive mode: when a function call references a module that is not yet loaded, the code server searches the code path in order to find the module's `.beam` file. In embedded mode, the code path exists but is not used for automatic module discovery. Developers commonly use `-pa` during development to add project build directories (e.g., `_build/default/lib/myapp/ebin`) to the front of the code path.

# Examples

**Example 1** (System Principles, "Code Loading Strategy"): Extending the code path at startup:
```text
% erl -pa /home/arne/mycode
```

**Example 2** (System Principles, "Code Loading Strategy"): The `code` module is referenced for modifying and querying the search path: "The `m:code` module contains a number of functions for modifying and querying the search path."

# Relationships

## Builds Upon
- **interactive-mode** — the code path is used by the code server when loading modules on demand in interactive mode

## Enables
- Module discovery — the code path makes it possible for the code server to find `.beam` files

## Related
- **code-loading-strategy** — the code path is most relevant in interactive mode
- **embedded-mode** — in embedded mode, code path exists but is not used for automatic loading

## Contrasts With
- No direct contrast in source.

# Common Errors

- **Error**: Expecting `-pz` to override existing modules when the same module already exists earlier in the path.
  **Correction**: Use `-pa` to prepend directories so they are searched first, overriding earlier versions.

- **Error**: Assuming the code path includes the current working directory automatically in all contexts.
  **Correction**: The current working directory is included initially, but this depends on how the runtime was started.

# Common Confusions

- **Confusion**: Thinking `-pa` and `-pz` do the same thing.
  **Clarification**: `-pa` prepends directories to the head of the code path (searched first), while `-pz` appends them to the end (searched last). The order matters because the first match wins.

# Source Reference

"Code Loading Strategy" section, "System Principles" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text, with details on initial composition, `-pa`/`-pz` flags, and versioning.
- Confidence rationale: High — explicit description with concrete details.
- Uncertainties: None.
- Cross-reference status: References interactive-mode, embedded-mode, code-loading-strategy (cards in this extraction).
