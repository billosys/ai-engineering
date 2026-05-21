---
# === CORE IDENTIFICATION ===
concept: Atom Exhaustion
slug: atom-exhaustion

# === CLASSIFICATION ===
category: performance
subcategory: resource-limits
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Atom Exhaustion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "atom table overflow"
  - "atom table limit"
  - "DSG-003"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
extends: []
related:
  - input-validation
  - be-restrictive-rule
  - trusted-data-deserialization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is atom exhaustion and why is it a security vulnerability?"
  - "Why can't atoms be garbage collected?"
  - "How do you safely convert external input to atoms?"
  - "What functions are dangerous for dynamic atom creation?"
  - "What is the difference between binary_to_atom and binary_to_existing_atom?"
---

# Quick Definition

Atom exhaustion is a denial-of-service vulnerability (CWE-770) where dynamically creating atoms from untrusted input can crash the BEAM VM because the atom table has a fixed limit and atoms are never garbage collected.

# Core Definition

As described in the Secure Coding Guidelines: "Data of the type atom is very space efficient and performant to use, but it must be used with care as it is not intended to be used dynamically: the intended use case is to provide named constants in code. The amount of atoms in the system is limited (see system limits and CWE-770) and cannot be reclaimed once created. That is, if you dynamically create a large amount of atoms, the system might crash."

# Prerequisites

- **Erlang Threat Model** -- understanding the trust boundary is essential since atom exhaustion is primarily a risk from untrusted input.

# Key Properties

1. **Atoms are permanent** -- once created, atoms are never garbage collected and persist for the lifetime of the VM.
2. **System-wide limit** -- the atom table has a fixed maximum size; exceeding it crashes the VM.
3. **Dangerous functions** -- `binary_to_atom/1,2` and `list_to_atom/1` create new atoms if they do not already exist.
4. **Safer alternatives** -- `binary_to_existing_atom/1,2` and `list_to_existing_atom/1` throw an exception instead of creating a new atom if it does not exist.
5. **Explicit conversion is best** -- even `*_to_existing_atom()` can return any atom that exists in the system, not just those expected in context; explicit mapping is preferred.
6. **Serialization risk** -- functions like `binary_to_term/1` can create atoms from serialized data; use `binary_to_term/2` with the `safe` option to prevent this (though data still requires validation).
7. **xmerl_scan risk** -- the `xmerl_scan` module dynamically produces new atoms and is not suitable for decoding untrusted XML sources.
8. **Rule priority: High** -- classified as high priority in the secure coding standard with CWE-770 and OWASP API10:2023 references.

# Construction / Recognition

## To Apply:
1. **Prefer explicit mapping** (most secure, aligns with STL-001):
```erlang
%% DO, AND PREFER (see STL-001)
input_to_atom(<<"foo">>) -> foo;
input_to_atom(<<"bar">>) -> bar;
input_to_atom(<<"quux">>) -> quux.
```

2. **Use existing_atom variants** when the set is not fixed:
```erlang
%% DO
input_to_atom(Text) -> binary_to_existing_atom(Text).

%% DO NOT
input_to_atom(Text) -> binary_to_atom(Text).
```

3. **Use the `safe` option** when deserializing terms:
```erlang
%% PREFER
binary_to_term(Data, [safe]).

%% AVOID
binary_to_term(Data).
```

4. **Avoid `xmerl_scan`** for untrusted XML; use `xmerl_sax_parser` instead.

## To Recognize:
1. Any call to `binary_to_atom`, `list_to_atom`, or `binary_to_term` (without `safe`) processing external input.
2. Use of `xmerl_scan` on data from untrusted sources.
3. Any code path that converts user-controlled strings to atoms.

# Context & Application

Atom exhaustion is one of the most Erlang-specific security vulnerabilities. It appears in multiple CWE references (CWE-770, CWE-400, CWE-20) throughout the secure coding guidelines. The vulnerability is particularly insidious because: the atom table is a global, VM-wide resource; the failure mode is a complete VM crash (not just a process crash); and the dangerous functions appear innocent and are commonly used. This concern drives several of the secure coding rules (DSG-003, DSG-011) and is a key motivation for the Be Restrictive rule (STL-001).

# Examples

**Example 1** (secure_coding.md, DSG-003): Safe conversion of known atom sets:
```erlang
%% DO, AND PREFER (see STL-001)
input_to_atom(<<"foo">>) -> foo;
input_to_atom(<<"bar">>) -> bar;
input_to_atom(<<"quux">>) -> quux.

%% DO
input_to_atom(Text) -> binary_to_existing_atom(Text).

%% DO NOT
input_to_atom(Text) -> binary_to_atom(Text).
```

**Example 2** (secure_coding.md, "Atom Exhaustion"): "The amount of atoms in the system is limited (see system limits and CWE-770) and cannot be reclaimed once created. That is, if you dynamically create a large amount of atoms, the system might crash."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- atom exhaustion is a consequence of the trust model; untrusted input can exploit this global resource

## Enables
- **Input Validation** -- atom exhaustion is a primary motivation for validating and restricting input at system boundaries

## Related
- **Be Restrictive Rule** -- explicit pattern matching on known atoms is the preferred defense against atom exhaustion
- **Trusted Data Deserialization** -- deserialization functions like `binary_to_term` can create atoms from untrusted data

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Using `binary_to_atom/1` on user-supplied input.
  **Correction**: Use explicit pattern matching for known atom sets, or `binary_to_existing_atom/1` when the set is dynamic but atoms are guaranteed to exist.

- **Error**: Using `binary_to_term/1` without the `safe` option on data from untrusted sources.
  **Correction**: Use `binary_to_term(Data, [safe])` to prevent creation of new atoms. However, note that even with `safe`, the data still needs validation and sanitization. "In general, it is best to avoid using such functions altogether on untrusted data, even with the safe option."

# Common Confusions

- **Confusion**: Thinking `binary_to_existing_atom` is always sufficient protection.
  **Clarification**: `*_to_existing_atom()` "can return any atom that exists in the system, not just those expected in the context." Explicit conversion is more appropriate when only a few specific atoms are valid.

- **Confusion**: Believing the atom table limit is so large it is unlikely to be reached.
  **Clarification**: While the default limit is large (~1 million), an attacker sending unique strings that are converted to atoms can exhaust it relatively quickly, causing a VM-wide crash.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, "Atom Exhaustion" section (secure_coding.md, lines 228-241) and DSG-003 rule (lines 797-853). Also referenced in the CWE-770, CWE-400, CWE-20 commentaries and the "Potentially Unsafe Functionality" table.

# Verification Notes

- Definition source: Directly quoted from the "Atom Exhaustion" section and DSG-003 rule.
- Confidence rationale: High -- extensively covered across multiple sections of the document with specific CWE references (CWE-770) and code examples.
- Uncertainties: None.
- Cross-reference status: Referenced by DSG-003, DSG-011, STL-001, CWE-770, CWE-400, CWE-20, API10:2023.
