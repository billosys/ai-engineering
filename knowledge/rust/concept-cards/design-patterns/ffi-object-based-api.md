---
concept: Object-Based APIs for FFI
slug: ffi-object-based-api
category: ffi-pattern
subcategory: null
tier: advanced
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Object-Based APIs"
extraction_confidence: high
aliases:
  - "object-based FFI"
  - "encapsulated type API"
  - "opaque pointer FFI"
prerequisites:
  - contain-unsafety
extends: []
related:
  - ffi-type-consolidation
  - contain-unsafety
  - raii-guards
contrasts_with: []
answers_questions:
  - "How do I design a safe FFI API in Rust?"
  - "What is the difference between encapsulated and transactional types in FFI?"
  - "How do I avoid lifetime and pointer provenance issues in FFI?"
---

# Quick Definition

When designing Rust APIs exposed to other languages via FFI, use an object-based design where encapsulated types are owned by Rust, managed by the user, and opaque, while transactional data types are owned by the user and transparent. All library behavior is expressed as functions acting on encapsulated types, with lifetimes consolidated by provenance rather than exposed as separate objects.

# Core Definition

The source defines four design principles for FFI APIs: "1. All Encapsulated types should be owned by Rust, managed by the user, and opaque. 2. All Transactional data types should be owned by the user, and transparent. 3. All library behavior should be functions acting upon Encapsulated types. 4. All library behavior should be encapsulated into types not based on structure, but provenance/lifetime."

The three goals for any foreign API are: "1. Make it easy to use in the target language. 2. Avoid the API dictating internal unsafety on the Rust side as much as possible. 3. Keep the potential for memory unsafety and Rust undefined behaviour as small as possible." (Ch. 2, "Object-Based APIs")

# Prerequisites

- **contain-unsafety** -- understanding how to isolate unsafe code in small modules directly applies to FFI boundary design, where unsafe pointer operations must be contained

# Key Properties

1. **Encapsulated types** are opaque to the user, owned by Rust (library), managed (created/destroyed) by the user through library functions
2. **Transactional types** are transparent to the user, owned by the user, used for data exchange (like C's `datum` -- a pointer and size)
3. The user never creates encapsulated types directly; they receive opaque pointers from library functions
4. All behavior is expressed as functions taking encapsulated types as parameters
5. Lifetimes and iteration state are consolidated into the encapsulated type, not exposed as separate objects
6. Memory for transactional data is allocated by the library using the user's allocator (e.g., C `malloc`) and ownership is transferred to the user

# Construction / Recognition

## To Design an Object-Based FFI API:
1. Identify types that hold internal library state -- make these encapsulated (opaque, library-owned)
2. Identify types used for data exchange -- make these transactional (transparent, user-owned)
3. Expose only opaque pointers for encapsulated types; provide `open`/`close` functions for lifecycle management
4. Express all operations as `extern "C"` functions taking encapsulated type pointers
5. Consolidate related lifetimes: embed iterators and sub-objects into their parent encapsulated type
6. For transactional types, transfer ownership of allocated memory to the user

## To Recognize This Pattern:
1. An opaque struct type with no public fields, accessed only through function pointers
2. Separate creation/destruction functions (e.g., `open`/`close`)
3. All operations take the opaque type as the first parameter
4. No separate iterator or sub-object types exposed across the FFI boundary

# Context & Application

The source uses the POSIX DBM database API as a detailed example. `DBM` is the encapsulated type: users receive a pointer from `dbm_open` and must call `dbm_close` to free it. `datum` is the transactional type: a transparent struct with a pointer and size, owned by the user. All operations (`dbm_store`, `dbm_fetch`, `dbm_delete`, etc.) take `DBM*` as the first argument.

The source contrasts this with a naive approach that exposes separate iterator types (`DbmKeysIter`), demonstrating how this creates lifetime safety issues. When an iterator is a separate object with a borrowed reference to the database, users in C can easily cause use-after-free by closing the database while the iterator is still alive. The POSIX API avoids this by consolidating iteration into the `DBM` type itself via `dbm_firstkey`/`dbm_nextkey`, binding all lifetimes together.

The source provides an extended C code example showing a subtle bug with separate iterator types: closing the database during iteration causes use-after-free that may silently corrupt memory rather than immediately crashing.

# Examples

**Example 1** (Ch. 2, "Object-Based APIs" -- POSIX DBM): The C header defines `DBM` as an opaque struct, `datum` as a transparent `{void *dptr, size_t dsize}`, and functions like `dbm_open`, `dbm_close`, `dbm_store`, `dbm_fetch`, `dbm_firstkey`, `dbm_nextkey`. Iteration is consolidated into `DBM` rather than exposed as a separate iterator type.

**Example 2** (Ch. 2, "Object-Based APIs" -- Bad Alternative): A naive FFI exposes `dbm_iter_new`, `dbm_iter_next`, `dbm_iter_del` as separate functions. The source shows a C bug where the database is closed during iteration (missing `break` statement), causing the iterator to operate on freed memory. "The worst part about this bug? If the Rust implementation was careful, this code will work most of the time!" -- producing intermittent corruption rather than reliable failure.

# Relationships

## Builds Upon
- **contain-unsafety** -- the object-based API is a specific application of containing unsafe pointer manipulation behind a safe boundary

## Enables
- Safe FFI consumption from C, Python, and other languages
- Memory safety guarantees as strong as the API design allows

## Related
- **ffi-type-consolidation** -- the companion pattern for wrapping multiple Rust types into a single opaque FFI object
- **raii-guards** -- the `open`/`close` lifecycle resembles RAII, though the user must manage it manually in C

## Contrasts With
- Exposing Rust iterators and lifetime-bounded types directly across FFI (unsafe and error-prone)
- Exposing internal Rust types transparently to foreign callers

# Common Errors

- **Error**: Exposing a separate iterator type across FFI with a lifetime dependency on the parent object.
  **Correction**: Consolidate iteration state into the parent object. Use `first_key`/`next_key` methods on the parent rather than separate iterator objects.

- **Error**: Letting the library allocate memory that the user cannot free with their allocator.
  **Correction**: For transactional types, allocate with the user's allocator (e.g., C `malloc`) so they can call `free`. Or provide explicit deallocation functions.

# Common Confusions

- **Confusion**: Thinking object-based FFI means using Rust traits or objects across FFI.
  **Clarification**: "Object-based" here refers to the C API design style where opaque structs (objects) are manipulated through free functions. Rust traits and vtables are not exposed.

- **Confusion**: Thinking the pattern eliminates all unsafety.
  **Clarification**: The user must still follow rules: "1. Do not call any function with a pointer not returned by dbm_open. 2. Do not call any function on a pointer after close. 3. The dptr on any datum must be NULL, or point to a valid slice of memory at the advertised length." The pattern minimizes but cannot eliminate user-side responsibility.

# Source Reference

Chapter 2: Design Patterns, "Object-Based APIs" section (FFI Patterns). Extensive section with POSIX DBM as the primary example, detailed discussion of encapsulated vs. transactional types, a complete C code example demonstrating use-after-free with separate iterators, and Rust code showing both the idiomatic and naive FFI approaches.

# Verification Notes

- Definition source: Direct quotation of the four design principles from "Description" subsection
- Key Properties: Derived from "Description", "Motivation", "Code Example", and "Advantages" subsections
- Confidence rationale: HIGH -- the source provides extensive detail with real-world POSIX examples, complete C and Rust code, and thorough discussion of trade-offs
- Uncertainties: None
- Cross-reference status: `contain-unsafety` and `ffi-type-consolidation` are in this extraction set; `raii-guards` from Agent 3
