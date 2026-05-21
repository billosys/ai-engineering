---
# === CORE IDENTIFICATION ===
concept: Input Validation
slug: input-validation

# === CLASSIFICATION ===
category: error-handling
subcategory: data-safety
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Rules / Secure Coding Standard"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "DSG-007"
  - "know your data"
  - "data validation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
  - be-restrictive-rule
extends: []
related:
  - atom-exhaustion
  - trusted-data-deserialization
  - sensitive-data-protection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should untrusted external input be validated in Erlang?"
  - "What is the 'Know Your Data' rule (DSG-007)?"
  - "How do you prevent path traversal attacks in Erlang?"
  - "How do you prevent OS command injection in Erlang?"
  - "How should match specifications handle untrusted data?"
  - "What are nominal types and how do they help with data safety?"
---

# Quick Definition

Input validation in Erlang requires knowing and documenting what data your code operates on, distinguishing between trusted and untrusted data, and applying specific validation strategies for different attack vectors including path traversal, command injection, match specification injection, and link-following attacks.

# Core Definition

The Secure Coding Guidelines establish input validation through several interrelated rules. DSG-007 (Know Your Data, priority: Medium) states: "Always know what data your code is operating on, and make sure it is documented. Preferably in a way such that it can be checked by automated tools such as declaring -nominal types to distinguish conceptually different but otherwise identical data." The document further notes: "Something as simple as marking data as trusted or untrusted can be a great help since all code implicitly trusts the data it is given to different degrees."

This principle is reinforced by specific attack-prevention rules: MSC-002 (path traversal, priority: Medium), MSC-003 (OS command injection, priority: High), MSC-005 (match specification injection, priority: High), and MSC-006 (link following, priority: Medium).

# Prerequisites

- **Erlang Threat Model** -- understanding the trust boundary and the definition of trusted vs untrusted data.
- **Be Restrictive Rule** -- restrictive pattern matching is the foundation for input validation.

# Key Properties

1. **Document data provenance** -- use nominal types (`-nominal`) to distinguish conceptually different data (e.g., `20 meters` vs `20 feet` when both are just `20`).
2. **Mark data as trusted/untrusted** -- all code implicitly trusts data to different degrees; making this explicit prevents injection attacks and data leakage.
3. **Path traversal defense** (MSC-002) -- use `filelib:safe_relative_path/2` to get a safe path relative to a given directory when dealing with untrusted paths.
4. **OS command injection defense** (MSC-003) -- use `open_port/2` with `{spawn_executable, _}` and explicit `{args, Args}` instead of `{spawn, _}` or `os:cmd/1,2` which invoke a shell.
5. **Match specification injection defense** (MSC-005) -- wrap untrusted data in `{const, UntrustedData}` expressions in match specifications; parse rather than validate untrusted queries.
6. **Link-following defense** (MSC-006) -- use `filelib:safe_relative_path/2` and beware of TOCTOU race conditions when operating on shared folder structures.
7. **Related CWEs** -- CWE-20 (Input Validation), CWE-22 (Path Traversal), CWE-74 (Injection), CWE-78 (OS Command Injection), CWE-89 (SQL Injection analog), CWE-502 (Deserialization), CWE-532 (Sensitive Data in Logs), CWE-843 (Type Confusion), CWE-918 (SSRF), CWE-1287 (Improper Validation).

# Construction / Recognition

## Path Traversal Defense:
```erlang
%% DO
open(UntrustedPath, Root, Opts) ->
    case filelib:safe_relative_path(UntrustedPath, Root) of
        unsafe -> {error, unsafe};
        Path -> file:open(filename:join(Root, Path), Opts)
    end.

%% DO NOT
file:open(UntrustedPath, Opts).
```

## OS Command Injection Defense:
```erlang
%% DO -- use spawn_executable with explicit args
open_port({spawn_executable, "/usr/bin/program"},
          [{args, ["--flag", Arg]}, {env, SafeEnv}])

%% DO NOT -- shell invocation with PATH search
open_port({spawn, "program --flag " ++ Arg}, [])

%% DO NOT -- os:cmd suffers from the same issues
os:cmd("program --flag " ++ Arg)
```

## Match Specification Injection Defense:
```erlang
%% DO
find(Table, Needle) ->
    ets:match(Table, {'_', {const, Needle}, '$1'}).

%% DO NOT
find(Table, Needle) ->
    ets:match(Table, {'_', Needle, '$1'}).
```

# Context & Application

Input validation is where the abstract Erlang threat model meets concrete code. The source emphasizes that Erlang does not provide web frameworks or SQL adapters, so many classic injection attacks (XSS, SQL injection) are not directly applicable to OTP itself. However, Erlang has its own injection vectors: match specifications in ETS serve a role analogous to SQL queries, path handling functions do not protect against traversal by default, and `open_port` with `{spawn, _}` invokes a shell. The guidelines recommend treating match specifications as code (MSC-005) and using `spawn_executable` instead of shell invocation (MSC-003). For CWE-362 (race conditions), Erlang's message-passing concurrency naturally avoids classical data races, but TOCTOU conditions can still occur with filesystem operations.

# Examples

**Example 1** (secure_coding.md, MSC-005): Match specification injection with ETS:
```erlang
%% DO -- wraps untrusted data safely
find(Table, Needle) ->
    ets:match(Table, {'_', {const, Needle}, '$1'}).

%% DO NOT -- Needle could contain match spec operations
find(Table, Needle) ->
    ets:match(Table, {'_', Needle, '$1'}).
```

**Example 2** (secure_coding.md, MSC-002): Path traversal defense:
```erlang
%% DO
open(UntrustedPath, Root, Opts) ->
    case filelib:safe_relative_path(UntrustedPath, Root) of
        unsafe -> {error, unsafe};
        Path -> file:open(filename:join(Root, Path), Opts)
    end.
```

**Example 3** (secure_coding.md, DSG-007): "Preferably in a way such that it can be checked by automated tools such as declaring -nominal types to distinguish conceptually different but otherwise identical data (consider 20 meters and 20 feet, when both are represented as the number 20)."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- input validation enforces the trust boundary defined by the threat model
- **Be Restrictive Rule** -- restrictive pattern matching is the coding practice that implements input validation

## Enables
- **Sensitive Data Protection** -- knowing what data is trusted vs untrusted is prerequisite for protecting sensitive data

## Related
- **Atom Exhaustion** -- atom creation from untrusted input is a specific input validation concern
- **Trusted Data Deserialization** -- deserialization of untrusted data is a specific input validation concern

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Using `open_port/2` with `{spawn, _}` or `os:cmd/1` when executing external programs with user-controlled arguments.
  **Correction**: Use `open_port/2` with `{spawn_executable, _}` and pass arguments via `{args, Args}` where no shell is invoked and no environment variable expansion occurs.

- **Error**: Passing untrusted data directly into ETS match specifications without wrapping in `{const, _}`.
  **Correction**: Wrap untrusted data in `{const, UntrustedData}` expressions. For general queries based on untrusted data, parse the data into a match specification rather than attempting to validate it.

- **Error**: Using `file:open/2` directly on paths from untrusted sources.
  **Correction**: Use `filelib:safe_relative_path/2` to normalize the path relative to an expected root directory before opening.

# Common Confusions

- **Confusion**: Thinking that Erlang's type system alone prevents type confusion attacks.
  **Clarification**: Erlang's dynamic typing means conceptually different data with the same type representation (e.g., meters vs feet as integers) can be confused. Nominal types (`-nominal`) help, but disciplined data labeling and documentation are also necessary.

- **Confusion**: Believing `filelib:safe_relative_path/2` eliminates all filesystem attack vectors.
  **Clarification**: While it prevents path traversal, TOCTOU race conditions can still occur where "a file or symbolic link is swapped out in the middle of operations." When operating on a shared folder structure, ensure only one entity has access.

# Source Reference

OTP Design Principles, Secure Coding Guidelines: DSG-007 (lines 904-927), MSC-002 (lines 1165-1177), MSC-003 (lines 1180-1218), MSC-005 (lines 1273-1300), MSC-006 (lines 1302-1336).

# Verification Notes

- Definition source: Synthesized from DSG-007, MSC-002, MSC-003, MSC-005, and MSC-006 rules with code examples from source.
- Confidence rationale: High -- multiple detailed rules with specific code examples, CWE references, and priority ratings.
- Uncertainties: None.
- Cross-reference status: References CWE-20, CWE-22, CWE-59, CWE-61, CWE-74, CWE-78, CWE-89, CWE-502, CWE-532, CWE-843, CWE-918, CWE-1287.
