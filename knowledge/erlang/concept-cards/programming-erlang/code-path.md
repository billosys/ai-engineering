---
# === CORE IDENTIFICATION ===
concept: Code Path
slug: code-path

# === CLASSIFICATION ===
category: applications-releases
subcategory: code-loading
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Compiling and Running Your Program"
chapter_number: 10
pdf_page: null
section: "Setting the Search Paths for Loading Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "load path"
  - "code search path"
  - "search path"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiling-modules
  - erlang-startup-file
  - erlang-shell
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang code path?"
  - "How do I tell Erlang where to find my compiled modules?"
  - "How does autoloading find a module's .beam file?"
---

# Quick Definition

The code path is the ordered list of directories the Erlang runtime searches to find compiled `.beam` files. Autoloading consults it on demand when a not-yet-loaded module is first called.

# Core Definition

The Erlang runtime system uses a code autoloading mechanism: "When the system tries to call a function in a module that has not been loaded, an exception occurs, and the system tries to find an object code file for the missing module." For a missing module `myMissingModule`, the code loader "will search for a file called `myMissingModule.beam` in all the directories that are in the current load path. The search stops at the first matching file" (Armstrong, "Compiling and Running Your Program," "Setting the Search Paths for Loading Code"). The current load path is obtained with `code:get_path()`.

# Prerequisites

This is a foundational concept within this chapter — it has no prerequisites among the chapter's other concepts.

# Key Properties

1. It is an ordered list of directories.
2. Autoloading is on demand — a module is loaded the first time one of its functions is called.
3. The loader searches for `<module>.beam` and stops at the first match.
4. `code:get_path()` returns the current load path.
5. `code:add_patha(Dir)` prepends a directory; `code:add_pathz(Dir)` appends one.
6. The `-pa Dir` startup flag prepends a directory; `-pz Dir` appends one.
7. `code:all_loaded()` lists loaded modules; `code:clash()` reports duplicate modules across the path.

# Construction / Recognition

## To Construct/Create:
1. Decide which directories hold your `.beam` files.
2. Add them with `code:add_patha/1` / `code:add_pathz/1`, or with `-pa`/`-pz` flags at startup, or via the `.erlang` file.
3. Verify with `code:get_path()`.

## To Identify/Recognize:
1. An `undef` error for a function usually means the module's directory is not on the path (or the module is uncompiled or misspelled).
2. `code:clash()` flags directories that hold conflicting versions of the same module.

# Context & Application

- **Typical contexts**: Multi-directory projects; including code from other projects with their own directory layouts.
- **Common applications**: Pointing the runtime at compiled output; ordering directories so the intended module version wins.
- **Historical/stylistic notes**: The code-loading mechanism is itself programmed in Erlang (the `code` module).

# Examples

**Example 1** ("Setting the Search Paths for Loading Code"): `code:get_path()` returns a list beginning with `"."` followed by the kernel, stdlib, and other library `ebin` directories.

**Example 2** ("Setting the Search Paths for Loading Code"): `erl -pa Dir1 -pa Dir2 ... -pz DirK1 -pz DirK2` — `-pa` adds to the beginning of the path, `-pz` to the end.

**Example 3** ("Undefined (Missing) Code"): Calling `glurk:oops(1,23)` yields `** exception error: undefined function glurk:oops/2` — one cause is that `glurk.beam`'s directory is not on the code path.

# Relationships

## Builds Upon
- This is foundational within the chapter.

## Enables
- **Compiling modules** — Compiled `.beam` files must sit on the code path to be loadable.

## Related
- **Erlang startup file** — The `.erlang` file is the usual place to set the path with `code:add_patha`/`add_pathz`.
- **The Erlang shell** — `code:get_path()` is run from the shell to inspect the path.

## Contrasts With
- None.

# Common Errors

- **Error**: Running code whose directory was never added to the path, producing an `undef` error.
  **Correction**: Add the directory with `-pa`/`-pz`, `code:add_patha/add_pathz`, or in `.erlang`.

- **Error**: Having two directories with different versions of the same module on the path.
  **Correction**: Run `code:clash()` to detect duplicates and remove the stale directory.

# Common Confusions

- **Confusion**: Thinking modules are loaded eagerly at startup.
  **Clarification**: Loading is on demand — triggered by the first call into a not-yet-loaded module.

- **Confusion**: Believing path order never matters.
  **Clarification**: The search stops at the first matching `.beam`, so `add_patha` vs. `add_pathz` can change which version loads.

# Source Reference

Chapter 10: "Compiling and Running Your Program," sections "Setting the Search Paths for Loading Code" and "Undefined (Missing) Code." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the autoloading description in "Setting the Search Paths for Loading Code."
- Confidence rationale: HIGH — the mechanism and BIFs are described explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-10 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
