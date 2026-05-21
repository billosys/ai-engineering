---
# === CORE IDENTIFICATION ===
concept: NIF Implementation Function
slug: nif-implementation-function

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
section: "12.4.2. The C side of the NIF"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ERL_NIF_INIT"
  - "ErlNifEnv"
  - "ErlNifFunc"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nif
  - nif-loading
extends: []
related:
  - nif-memory-management
  - external-term-format
contrasts_with:
  - driver-callbacks

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the signature of a NIF implementation function in C?"
  - "What is the ErlNifEnv pointer?"
  - "How do you register NIFs with the Erlang VM?"
---

# Quick Definition

A NIF implementation function is a C function with the fixed signature `(ErlNifEnv*, int argc, const ERL_NIF_TERM argv[])` returning an `ERL_NIF_TERM`, registered with the VM via an `ErlNifFunc` array and the `ERL_NIF_INIT` macro.

# Core Definition

A NIF is implemented by a C function included via `erl_nif.h`. All NIF implementation functions have the same signature: they return an `ERL_NIF_TERM` object and take three arguments — `env` (an `ErlNifEnv` pointer the VM passes, used as a handle in most `erl_nif` API calls), `argc` (the number of Erlang arguments passed in the call), and `argv` (an array of the argument terms). The return value is an `ERL_NIF_TERM` representing the Erlang data to return. To tell the VM which NIFs a library publishes, you fill in an `ErlNifFunc` array with each NIF's Erlang function name, arity, and implementing C function, and use the `ERL_NIF_INIT` macro to register the array and the owning module. The last four arguments of `ERL_NIF_INIT` are optional life-cycle function pointers (`load`, `reload`, `upgrade`, `unload`) ("Erlang and OTP in Action," Ch. 12, Section 12.4.2).

# Prerequisites

- **NIF** — This is the C function that implements a NIF.
- **NIF library loading** — A NIF function backs an Erlang stub published by loading.

# Key Properties

1. Signature: `ERL_NIF_TERM f(ErlNifEnv *env, int argc, const ERL_NIF_TERM argv[])`.
2. `env` is an `ErlNifEnv` pointer used as a handle in most `erl_nif` API calls; it is stored in the state struct.
3. `argc` is the Erlang argument count; `argv` holds the argument terms.
4. The function returns an `ERL_NIF_TERM` (often `{ok, ...}` or `{error, ...}`, or a `badarg` exception term).
5. Argument types should be checked, e.g. `enif_inspect_binary` to read a binary argument.
6. An `ErlNifFunc` array maps each Erlang `{Name, Arity}` to its C function.
7. The `ERL_NIF_INIT` macro registers the array and the owning module (module name unquoted); its last four arguments are `load`, `reload`, `upgrade`, `unload` (may be `NULL`).

# Construction / Recognition

## To Construct/Create:
1. Implement a C function with the fixed three-argument NIF signature.
2. Store `env` in your `state_t` struct; validate `argc` and argument types.
3. Use `erl_nif` functions (e.g., `enif_inspect_binary`) to read inputs and build the result term.
4. Fill an `ErlNifFunc` array with the NIF name/arity/function entries.
5. Register with `ERL_NIF_INIT(ModuleName, funcs, load, reload, upgrade, unload)`.

## To Identify/Recognize:
1. A C function returning `ERL_NIF_TERM` with `(ErlNifEnv*, int, const ERL_NIF_TERM[])` parameters, plus an `ERL_NIF_INIT` call.

# Context & Application

- **Typical contexts**: The C side of a NIF-based integration.
- **Common applications**: `parse_document_1` implements the `json_parser:parse_document/1` NIF, replacing the port version's `process_data`.
- **Historical/stylistic notes**: Sharing a C function across multiple NIFs is possible because `argc` distinguishes the arities.

# Examples

**Example 1** (Listing 12.11): `parse_document_1` stores `env` in `state_t`, sets up a dummy top-level container, checks that the single argument is a binary (else returns a `badarg` term), and uses `enif_inspect_binary` to find the JSON data before calling `parse_json`.

**Example 2** (Listing 12.11): An `ErlNifFunc` array maps `parse_document/1` to `parse_document_1`; `ERL_NIF_INIT(json_parser, ...)` registers it with all four life-cycle pointers as `NULL`.

# Relationships

## Builds Upon
- **NIF** — This C function is the implementation of a NIF.
- **NIF library loading** — It overrides the Erlang stub once loaded.

## Related
- **NIF memory management** — NIF functions allocate with `enif_alloc`.

## Contrasts With
- **erl_driver callback functions** — Driver callbacks use `ErlDrvData`/`ErlDrvEntry` and `DRIVER_INIT`; NIF functions use `ErlNifEnv`/`ErlNifFunc` and `ERL_NIF_INIT`.

# Common Errors

- **Error**: Quoting the module name in `ERL_NIF_INIT`.
  **Correction**: The module name argument to `ERL_NIF_INIT` is unquoted.

- **Error**: Skipping argument count/type checks before doing work.
  **Correction**: Verify `argc` and argument types; return a `badarg`-raising term on mismatch.

# Common Confusions

- **Confusion**: Thinking each NIF needs its own distinct C function.
  **Clarification**: Several NIFs can share one C function because `argc` lets the function tell the arities apart.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.4.2 "The C side of the NIF" — subsections "The NIF implementation function" and "Registering your NIFs." See Listing 12.11.

# Verification Notes

- Definition source: Direct adaptation of Section 12.4.2.
- Confidence rationale: HIGH — the book describes the signature, `ErlNifFunc`, and `ERL_NIF_INIT` explicitly.
- Uncertainties: Listing 12.11 appears as an image; behavior described from surrounding prose.
- Cross-reference status: `nif`, `nif-loading` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
