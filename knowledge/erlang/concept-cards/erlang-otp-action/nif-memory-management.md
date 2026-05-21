---
# === CORE IDENTIFICATION ===
concept: NIF Memory Management and Term Construction
slug: nif-memory-management

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
  - "enif_alloc"
  - "enif_make_list_from_array"
  - "enif_make_tuple_from_array"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nif
  - nif-implementation-function
extends: []
related:
  - erl-nif-api
contrasts_with:
  - driver-memory-management

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a NIF allocate memory?"
  - "How does a NIF build Erlang lists and tuples?"
  - "Why can't a NIF back-patch list and tuple sizes like the ei library?"
---

# Quick Definition

A NIF allocates memory with the `erl_nif` functions `enif_alloc`/`enif_realloc`/`enif_free`, and builds compound terms by collecting elements in a C array, then calling `enif_make_tuple_from_array` or `enif_make_list_from_array`.

# Core Definition

In a NIF you must use the `enif_alloc` functions provided by the `erl_nif` library for memory allocation, rather than the `driver_alloc` functions used in a linked-in driver. One main complication of switching from the `ei` library to `erl_nif` is that there is no `ei_x_buff` to incrementally build lists and tuples — the `erl_nif` functions need to know sizes when terms are created, so you cannot back-patch a size. The solution is `enif_make_tuple_from_array` and `enif_make_list_from_array`, which let you prepare your own C array of Erlang terms and turn them into a tuple or list with a single call. Each container therefore manages a dynamic array of elements while a JSON container is being parsed ("Erlang and OTP in Action," Ch. 12, Sections 12.4.2 — "Memory management" and "Keeping track of container contents").

# Prerequisites

- **NIF** — These rules apply to NIF C code.
- **NIF implementation function** — Memory and term building happen inside the NIF function and its callbacks.

# Key Properties

1. Use `enif_alloc`, `enif_realloc`, `enif_free` instead of `malloc`/`free` or `driver_alloc`/`driver_free`.
2. In the R13 API the `enif_alloc` functions take an `ErlNifEnv` pointer as the first argument (dropped in R14).
3. There is no `ei_x_buff` — you cannot incrementally build a term and back-patch its size.
4. `enif_make_tuple_from_array` / `enif_make_list_from_array` build a compound term from a prepared C array.
5. Each `container_t` keeps an `array` and `arraysz` field; elements are accumulated, then converted in `handle_end`.
6. `add_element` (replacing `count_element`) inserts a term into the current container's array, resizing as needed.
7. The YAJL allocation context is set to the `ErlNifEnv` so YAJL's allocations also use `enif_alloc`.

# Construction / Recognition

## To Construct/Create:
1. Replace `driver_alloc`/`driver_realloc`/`driver_free` with `enif_alloc`/`enif_realloc`/`enif_free`.
2. Set `alloc_funcs.ctx = st->env` before `yajl_alloc` so YAJL uses `enif_alloc`.
3. Add `array`/`arraysz` fields to `container_t`; drop the `index` field.
4. Accumulate elements with `add_element`, resizing the array when full.
5. In `handle_end`, build the term with `enif_make_tuple_from_array` or `enif_make_list_from_array`.

## To Identify/Recognize:
1. NIF C code calling `enif_alloc` and `enif_make_*_from_array`, with per-container element arrays.

# Context & Application

- **Typical contexts**: Building Erlang results inside a NIF.
- **Common applications**: The NIF JSON parser collects array/map elements in container arrays and converts them at container end.
- **Historical/stylistic notes**: Because there is no back-patching, most of the YAJL callback code had to be rewritten when moving from the `ei` driver to the NIF.

# Examples

**Example 1** (Listing 12.12): `add_element` resizes the container array if full, then either folds a key/value into a 2-tuple (when `st->key` is set) or inserts a plain element and increments the count.

**Example 2** (Listing 12.14): `handle_end` unlinks the container, calls `enif_make_tuple_from_array` or `enif_make_list_from_array` to build the term from the accumulated array, then adds it to the parent container.

# Relationships

## Builds Upon
- **NIF** — Memory rules apply to NIF code.
- **NIF implementation function** — Term construction happens within the NIF and its callbacks.

## Related
- **erl_nif API** — Provides the `enif_*` functions used here.

## Contrasts With
- **Linked-in driver memory management** — A driver uses `driver_alloc` and can back-patch via `ei_x_buff`; a NIF uses `enif_alloc` and must build compound terms from prepared arrays.

# Common Errors

- **Error**: Trying to incrementally build a tuple/list and patch its size, as with `ei_x_buff`.
  **Correction**: Collect elements in a C array and build the term in one call with `enif_make_tuple_from_array`/`enif_make_list_from_array`.

- **Error**: Using `driver_alloc` or `malloc` in NIF code.
  **Correction**: Use the `erl_nif` library's `enif_alloc` family.

# Common Confusions

- **Confusion**: Assuming NIF code can reuse the `ei`-based term-building code from the port driver.
  **Clarification**: NIFs use a different API with no incremental buffer; most callback code must be rewritten.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.4.2 — subsections "Memory management," "Keeping track of container contents," and "Rewriting the YAJL parser callbacks." See Listings 12.12 and 12.14.

# Verification Notes

- Definition source: Direct adaptation of Section 12.4.2.
- Confidence rationale: HIGH — the book explicitly contrasts `enif_alloc` with `driver_alloc` and explains the array-based term construction.
- Uncertainties: Listings 12.12 and 12.14 appear as images; behavior described from surrounding prose.
- Cross-reference status: `nif`, `nif-implementation-function` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
