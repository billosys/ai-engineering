---
# === CORE IDENTIFICATION ===
concept: NIF Library Loading
slug: nif-loading

# === CLASSIFICATION ===
category: tooling
subcategory: interoperability
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.4.1. The Erlang side of the NIF"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "erlang:load_nif/2"
  - "-on_load"
  - "erlang:nif_error/1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nif
extends: []
related:
  - priv-directory
  - nif-implementation-function
contrasts_with:
  - erl-ddll

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is a NIF library loaded into a module?"
  - "What is the -on_load attribute used for?"
  - "Why do NIF stub functions call erlang:nif_error/1?"
---

# Quick Definition

A NIF library is loaded with `erlang:load_nif/2`, triggered automatically by the module's `-on_load` attribute; stub functions call `erlang:nif_error/1` until the real NIFs override them.

# Core Definition

To make NIFs available, the Erlang module must load its shared library by calling `erlang:load_nif(Path, LoadInfo)`, where `Path` is the library file without extension and `LoadInfo` is passed to the C `load` callback. So users do not have to call this manually, the module attribute `-on_load(init/0)` (added along with the `erl_nif` API) specifies a function to call automatically when the module is loaded. The module must also provide exported stub functions for each NIF; the stub body calls `erlang:nif_error(nif_not_loaded)`, which raises a runtime error if called before the library loads and signals to tools like Dialyzer that the function's real behavior is not visible in the Erlang code. When the library loads, the NIF implementations override the Erlang stubs ("Erlang and OTP in Action," Ch. 12, Section 12.4.1).

# Prerequisites

- **NIF** — Loading is how a NIF library is brought into a module.

# Key Properties

1. `erlang:load_nif(Path, LoadInfo)` loads, links, and publishes the NIFs of a shared library.
2. `Path` is the library file without extension; the library normally lives in the application's `priv` directory.
3. `LoadInfo` is passed to the C `load` callback (useful for version upgrades); the example passes `0`.
4. The `-on_load(init/0)` attribute makes the loading function run automatically when the module loads.
5. Each NIF needs an exported Erlang stub function.
6. Stub bodies call `erlang:nif_error(nif_not_loaded)`, which behaves like `erlang:error/1` and informs Dialyzer.
7. Once loaded, the C NIF implementations override the Erlang stub functions.

# Construction / Recognition

## To Construct/Create:
1. Write `init/0` that gets `code:priv_dir(?APPNAME)` and calls `erlang:load_nif(filename:join([PrivDir, "jp_nifs"]), 0)`.
2. Add the attribute `-on_load(init/0)`.
3. For each NIF, export a stub function whose body is `erlang:nif_error(nif_not_loaded)`.

## To Identify/Recognize:
1. A module with `-on_load`, an `erlang:load_nif/2` call, and stub functions calling `erlang:nif_error/1`.

# Context & Application

- **Typical contexts**: The Erlang side of a NIF-based integration.
- **Common applications**: The `json_parser` module loads `jp_nifs.so` and provides a `parse_document/1` stub.
- **Historical/stylistic notes**: With NIFs there is no `gen_server`, no supervision tree, and no need to start the application — all functionality is in the module.

# Examples

**Example 1** (Section 12.4.1): `init/0` calls `erlang:load_nif(filename:join([PrivDir, "jp_nifs"]), 0)`; `-on_load(init/0)` makes it run on module load.

**Example 2** (Section 12.4.1): The stub `parse_document(Data) -> erlang:nif_error(nif_not_loaded).` is overridden by the C NIF once the library is loaded.

# Relationships

## Builds Upon
- **NIF** — Loading publishes a module's NIFs.

## Related
- **priv directory** — The NIF library lives in `priv`.
- **NIF implementation function** — The C functions that override the stubs.

## Contrasts With
- **erl_ddll driver loading** — A linked-in driver is loaded with `erl_ddll:load/2` and opened as a port; a NIF library is loaded with `erlang:load_nif/2` and involves no ports.

# Common Errors

- **Error**: Omitting `erlang:nif_error/1` from stub bodies.
  **Correction**: Always use `erlang:nif_error/1` so a pre-load call fails cleanly and Dialyzer is correctly informed.

- **Error**: Expecting users to call `init/0` manually.
  **Correction**: Use `-on_load(init/0)` so the NIF library loads automatically with the module.

# Common Confusions

- **Confusion**: Thinking the Erlang stub function bodies are the real implementation.
  **Clarification**: The stubs are placeholders; the loaded C NIFs override them at module-load time.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.4.1 "The Erlang side of the NIF." See sidebar "Using erlang:nif_error/1 in stub functions."

# Verification Notes

- Definition source: Direct adaptation of Section 12.4.1.
- Confidence rationale: HIGH — the book shows the loading code and explains `-on_load` and `nif_error`.
- Uncertainties: None.
- Cross-reference status: `nif` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
