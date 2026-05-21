---
# === CORE IDENTIFICATION ===
concept: Native Code Safety
slug: native-code-safety

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: ffi-security
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Native Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "NIF safety"
  - "driver safety"
  - "FFI security"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
  - erlang-memory-safety
extends: []
related:
  - be-restrictive-rule
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What security risks do NIFs and drivers introduce?"
  - "How does native code affect Erlang's memory safety guarantees?"
  - "When should native code be avoided in Erlang systems?"
  - "What precautions should be taken when writing NIFs or drivers?"
---

# Quick Definition

Native code linked into the BEAM via NIFs (Native Implemented Functions) or drivers can violate Erlang's memory safety and stability guarantees. While sometimes unavoidable, native code introduces the full range of memory-unsafe vulnerabilities that pure Erlang eliminates, and should be minimized and written with extreme care.

# Core Definition

As stated in the Secure Coding Guidelines: "Native code can be dynamically linked into the Erlang runtime system either as a driver or NIF library. Drivers and NIF libraries are typically written in C or C++ and have, if not full access, access to a large part of the runtime system internals." The source further notes: "Drivers and NIF libraries are, of course, not necessarily unsafe and sometimes their use is unavoidable, but it is much easier to avoid introducing vulnerabilities and other problems by writing Erlang code whenever possible."

# Prerequisites

- **Erlang Threat Model** -- understanding what is protected against (and that native code is the exception).
- **Erlang Memory Safety** -- native code is the primary way memory safety guarantees can be violated.

# Key Properties

1. **Full runtime access** -- drivers and NIF libraries have access to a large part of the runtime system internals.
2. **Memory safety violation** -- "Importing memory-unsafe code through the Foreign Function Interfaces (FFI), such as drivers and Native Implemented Functions (NIFs), may, of course, violate this property."
3. **Well-defined behavior violation** -- "Like with memory safety, this property can be violated if the foreign function interfaces are misused."
4. **Dual guideline requirement** -- native code must follow both secure programming guidelines for its implementation language (C, C++, etc.) and the guidelines for writing drivers and NIF libraries.
5. **Stability risk** -- poorly written native code can introduce both vulnerabilities and stability problems (crashes, scheduling issues).
6. **Loading mechanisms** -- NIF libraries are loaded via `erlang:load_nif/2`; drivers via `erl_ddll` load functions. Both are listed as "Potentially Unsafe Functionality" (CWE-676).
7. **Prefer Erlang** -- the guideline is to write Erlang code whenever possible and reserve native code for cases where it is truly unavoidable.

# Construction / Recognition

## To Apply:
1. Prefer pure Erlang implementations whenever possible.
2. When native code is unavoidable, follow secure programming guidelines for the implementation language (e.g., CERT C Coding Standard for C).
3. Follow the Erlang-specific guidelines for writing NIF libraries (`erl_nif`) and drivers (`erl_driver`).
4. Be aware that a buggy NIF can crash the entire VM, not just the calling process.
5. Consider using dirty schedulers for long-running NIFs to avoid blocking the BEAM scheduler.

## To Recognize:
1. Any use of `erlang:load_nif/2` or `erl_ddll:load*/2,3` functions.
2. C or C++ source files that include `erl_nif.h` or `erl_driver.h`.
3. Functions in the "Potentially Unsafe Functionality" table related to native code loading.

# Context & Application

Native code is one of only two ways to break the BEAM's safety guarantees (the other being loading malicious BEAM modules, which falls under the trusted-code assumption). This makes NIFs and drivers the most security-critical components of any Erlang system. The Secure Coding Guidelines list six NIF/driver loading functions in the "Potentially Unsafe Functionality" table: `erlang:load_nif/2`, `erl_ddll:load/2`, `erl_ddll:load_driver/2`, `erl_ddll:try_load/3`, `erl_ddll:reload/2`, and `erl_ddll:reload_driver/2`. All are classified under CWE-676 (Use of Potentially Dangerous Function).

# Examples

**Example 1** (secure_coding.md, "Native Code"): "Thorough care needs to be taken both to follow secure programming guidelines for the language that the native code is written in as well as the guidelines for writing drivers and NIF libraries. Poorly written native code can both introduce vulnerabilities as well as stability problems."

**Example 2** (secure_coding.md, "What is protected against"): "Importing memory-unsafe code through the Foreign Function Interfaces (FFI), such as drivers and Native Implemented Functions (NIFs), may, of course, violate this property, but there are no unsafe constructs in the language itself."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- native code is explicitly identified as an exception to the safety guarantees
- **Erlang Memory Safety** -- NIFs/drivers are the primary mechanism through which memory safety can be violated

## Enables
- No concepts directly enabled.

## Related
- **Be Restrictive Rule** -- restrictive coding practices are even more important at the boundary between Erlang and native code

## Contrasts With
- No direct contrasts in source, though the concept implicitly contrasts with the safety of pure Erlang code.

# Common Errors

- **Error**: Writing performance-critical code as a NIF when a pure Erlang implementation would suffice.
  **Correction**: "It is much easier to avoid introducing vulnerabilities and other problems by writing Erlang code whenever possible." Only use NIFs when truly necessary.

- **Error**: Following only C/C++ secure coding guidelines without also following Erlang-specific NIF/driver guidelines.
  **Correction**: Both sets of guidelines must be followed. The Erlang-specific guidelines address BEAM scheduler integration, memory allocation through enif_* functions, and proper error handling at the FFI boundary.

# Common Confusions

- **Confusion**: Thinking that a NIF crash is isolated to the calling process like a normal Erlang crash.
  **Clarification**: A segfault or memory corruption in a NIF can crash the entire BEAM VM, not just the calling process. This is fundamentally different from a pure Erlang process crash.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, "Native Code" section (secure_coding.md, lines 243-264). Also referenced in "What is protected against" (lines 107-110, 128-130) and the "Potentially Unsafe Functionality" table (lines 1401-1406).

# Verification Notes

- Definition source: Directly quoted from the "Native Code" section.
- Confidence rationale: High -- explicitly covered with clear guidance and listed in the unsafe/potentially-unsafe functionality tables.
- Uncertainties: None.
- Cross-reference status: Referenced by CWE-676 table entries. Related to erlang-threat-model and erlang-memory-safety.
