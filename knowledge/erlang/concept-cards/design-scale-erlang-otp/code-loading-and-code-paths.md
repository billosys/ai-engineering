---
# === CORE IDENTIFICATION ===
concept: Code Loading and Code Paths
slug: code-loading-and-code-paths

# === CLASSIFICATION ===
category: applications-releases
subcategory: code-loading
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Arguments and Flags"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - code search path
  - "-mode embedded"
  - interactive vs embedded code loading

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-directory-structure
extends: []
related:
  - boot-script-file
  - arguments-and-flags
  - erlang-loader
  - module-versioning
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does code loading work and what is the code search path?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

The code search path is the ordered list of directories the runtime searches to load modules. Code-loading mode (`interactive` or `embedded`) determines whether modules are searched for on demand or all loaded at startup.

# Core Definition

The code search path is a list of directories used to load modules; directories are added to it from `path` entries in the boot script and from command-line arguments `-pa`, `-pz`, and `-path` (Cesarini & Vinoski, p. 277, 293, pdf p. 282). The `-mode` flag establishes how code is loaded: in `interactive` mode, calls to modules that have not been loaded are automatically searched for in the code search path; in `embedded` mode, all modules should be loaded at startup by the boot file, and calls to nonexisting modules result in a crash. Embedded mode is recommended for all production systems.

# Prerequisites

- **Release directory structure** — The code path points into `lib/App-Vsn/ebin`; understanding the layout is required.

# Key Properties

1. The code search path is an ordered list of directories searched to load modules.
2. `-pa` adds directories to the beginning of the path; `-pz` adds to the end.
3. Boot-script `path` entries can use absolute paths or `$ROOT`-relative paths; paths can include wildcards (`lib/*/ebin`).
4. `-mode interactive` — modules load on demand from the search path.
5. `-mode embedded` — all modules load at startup; missing-module calls crash.
6. Embedded mode is recommended for production — avoids pausing a process mid-call to traverse the path.
7. In embedded mode you can still load modules with `l(Module)` or `code:load_file(Module)`.
8. The `ebin` directories of `kernel`, `compiler`, and `stdlib` are sticky by default, preventing accidental overrides (disable with `-nostick`).

# Construction / Recognition

## To Configure Code Loading:
1. Add application `ebin` directories with `-pa`/`-pz` or boot-script `path` actions.
2. Set `-mode embedded` for production so all modules load at startup.
3. Use `-pa patches` to point at a temporary patches directory ahead of release paths.

## To Recognize the Mode:
1. `-mode embedded` -> all modules loaded at startup, missing-module calls crash.
2. `-mode interactive` -> modules searched and loaded on demand.

# Context & Application

- **Typical contexts**: Configuring how a node finds and loads its modules.
- **Common applications**: Adding a `patches` directory at the front of the path for between-release fixes; running production nodes in embedded mode for determinism.
- **Historical/stylistic notes**: Generated boot-script paths assume the standard `$ROOT/lib/App-Vsn/ebin` layout, not a development `App/ebin` layout.

# Examples

**Example 1** (p. 273): The boot script looks for application versions using the code search path and any `{path, PathList}` environment variable; starting Erlang with `erl -pa bsc/ebin` adds `bsc/ebin` to the path.

**Example 2** (p. 277): The generated `bsc` path is `$ROOT/lib/bsc-1.0/ebin`, not `bsc/ebin` — the target environment assumes the standard OTP directory structure with version numbers.

**Example 3** (Ch. 11, p. 325): Starting the runtime with `-pa patches` so beam files placed in `patches` override later beam files of the same module — used to apply between-release fixes.

# Relationships

## Builds Upon
- **Release directory structure** — The code path points into `lib/App-Vsn/ebin`.

## Related
- **Boot script file** — `path` and `primLoad` actions populate the path and load modules.
- **Arguments and flags** — `-pa`, `-pz`, `-path`, `-mode`, `-nostick` configure code loading.
- **Erlang loader** — `erl_prim_loader` fetches modules using the path.
- **Module versioning** — Two versions of a module can be loaded at once.

# Common Errors

- **Error**: Forgetting to add an application's `ebin` to the code path.
  **Correction**: `primLoad` fails if the path is incorrect; add the directory with `-pa`/`-pz` or fix the boot-script path.

- **Error**: Running a production node in interactive mode.
  **Correction**: Use embedded mode so a process is never paused mid-call to search the path for an unloaded module.

# Common Confusions

- **Confusion**: Thinking embedded mode forbids loading any module after startup.
  **Clarification**: You can still load modules in embedded mode with `l(Module)` or `code:load_file(Module)`.

- **Confusion**: Believing `-pa` and `-pz` are interchangeable.
  **Clarification**: `-pa` prepends to the path; `-pz` appends — order matters when modules of the same name exist in multiple directories.

# Source Reference

Chapter 10: System Principles and Release Handling, sections "Script files" and "Arguments and Flags," pages 277 and 293-294 (pdf p. 282).

# Verification Notes

- Definition source: Synthesized from the `path` action description (p. 277) and the `-mode`/`-pa`/`-pz`/`-nostick` flag descriptions (pp. 293-294).
- Confidence rationale: HIGH — the source explicitly describes the code search path and the interactive/embedded modes.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
