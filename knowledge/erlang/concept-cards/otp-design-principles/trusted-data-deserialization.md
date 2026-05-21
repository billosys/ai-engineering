---
# === CORE IDENTIFICATION ===
concept: Trusted Data Deserialization
slug: trusted-data-deserialization

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
  - "DSG-011"
  - "deserialization safety"
  - "binary_to_term safety"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
  - atom-exhaustion
extends: []
related:
  - input-validation
  - be-restrictive-rule
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is deserializing untrusted Erlang terms dangerous?"
  - "What serialization functions should not be used on untrusted data?"
  - "What formats should be used instead for untrusted data?"
  - "Is binary_to_term with the safe option sufficient for untrusted data?"
  - "Why is xmerl_scan unsafe for untrusted XML?"
---

# Quick Definition

Erlang's term serialization functions (`binary_to_term`, `file:consult`, mnesia backups, dets, disk_log) are designed for trusted environments and must not be used on data from untrusted sources. For untrusted data, use structured formats like JSON (`m:json`) or XML (`m:xmerl_sax_parser`) with validation during decoding.

# Core Definition

The Secure Coding Guidelines state under DSG-011 (priority: High): "Erlang/OTP provides various functionality that serializes and deserializes general Erlang terms. Such functionality is intended to be used in a trusted environment and is not suitable for communication with untrusted entities." The source explains: "One issue with this being the potential for atom exhaustion, but more importantly you could potentially end up with a mnesia table containing harmful data (CWE-502)."

# Prerequisites

- **Erlang Threat Model** -- understanding the trust boundary is essential for knowing when deserialization is safe.
- **Atom Exhaustion** -- atom creation from deserialized data is a primary risk vector.

# Key Properties

1. **Term serialization is for trusted environments only** -- `binary_to_term`, `file:consult`, mnesia backups, dets, and disk_log are not suitable for untrusted data.
2. **The `safe` option is insufficient** -- even `binary_to_term/2` with `safe` still requires validation and sanitization because "it can still be harmful to the Erlang application in other ways."
3. **Best to avoid entirely** -- "In general, it is best to avoid using such functions altogether on untrusted data, even with the safe option."
4. **Use JSON for untrusted data** -- the `m:json` module provides encoding/decoding with SAX-style callbacks for validation during decoding.
5. **Use xmerl_sax_parser for untrusted XML** -- `xmerl_scan` dynamically produces atoms and is not suitable for untrusted XML; `xmerl_sax_parser` with `disallow_entities` option prevents XML entity attacks.
6. **Validate during decoding** -- both `json` and `xmerl_sax_parser` support SAX-style decoding with user-defined callbacks for inline validation, preventing issues like memory exhaustion.
7. **Potentially unsafe functions** -- `binary_to_term/1`, `binary_to_term/2` (without `safe`), `file:consult/1`, `file:path_consult/2`, `xmerl_scan:file/1,2`, `xmerl_scan:string/1,2`, `xmerl_sax_parser:file/2` (without `disallow_entities`), `xmerl_sax_parser:stream/2` (without `disallow_entities`) are all listed in the "Potentially Unsafe Functionality" table.

# Construction / Recognition

## Safe Alternatives:
```erlang
%% For untrusted data -- use JSON
json:decode(UntrustedBinary).

%% For untrusted XML -- use SAX parser with entity protection
xmerl_sax_parser:file(File, [{disallow_entities, true}]).

%% For SAX-style validation during decoding (JSON)
json:decode(UntrustedBinary, Acc, DecodeFun).

%% For SAX-style validation during decoding (XML)
xmerl_sax_parser:stream(Data, [{disallow_entities, true},
                                {event_fun, ValidationFun}]).
```

## Unsafe Patterns:
```erlang
%% DO NOT -- term deserialization of untrusted data
binary_to_term(UntrustedBinary).

%% STILL RISKY -- safe option prevents atoms but not other harm
binary_to_term(UntrustedBinary, [safe]).

%% DO NOT -- consult files from untrusted sources
file:consult(UntrustedFile).

%% DO NOT -- xmerl_scan creates atoms dynamically
xmerl_scan:string(UntrustedXml).

%% DO NOT -- SAX parser without entity protection
xmerl_sax_parser:file(UntrustedFile, []).
```

# Context & Application

Deserialization of untrusted data is a well-known vulnerability class (CWE-502) across many languages. In Erlang, the risk is compounded by atom exhaustion (atoms created during deserialization are permanent) and the ability to inject arbitrary Erlang terms that could corrupt application state. The source specifically warns about mnesia backups from untrusted sources and emphasizes that even with protections like the `safe` option, the fundamental problem remains: the data format allows representing arbitrary terms, which is more expressive than what untrusted communication should permit. JSON and SAX-parsed XML are preferred because their data model is more constrained and validation can occur during parsing rather than after.

# Examples

**Example 1** (secure_coding.md, DSG-011): "For example, you do not want to load a mnesia backup from an untrusted entity. One issue with this being the potential for atom exhaustion, but more importantly you could potentially end up with a mnesia table containing harmful data (CWE-502)."

**Example 2** (secure_coding.md, DSG-011): "JSON is an example of a better format to use when communicating with untrusted entities. Erlang/OTP provides the json module for JSON encoding/decoding."

**Example 3** (secure_coding.md, DSG-003): "There are also a number APIs that create general Erlang terms from data of some serialized format. You should not use such APIs if the data is not trusted (see DSG-011) unless the API also provides some way of preventing creation of atoms. For example, binary_to_term/2 with the safe option will prevent new atoms from being created. However, note that even if the safe option is used and the data originates from an untrusted source, it still has to be validated and sanitized, since it can still be harmful to the Erlang application in other ways."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- the trust boundary determines when deserialization is safe
- **Atom Exhaustion** -- atom creation is a primary risk of deserializing untrusted terms

## Enables
- No concepts directly enabled.

## Related
- **Input Validation** -- deserialization safety is a specific case of input validation for serialized data
- **Be Restrictive Rule** -- restrictive coding practices apply to how deserialized data is consumed

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Using `binary_to_term/1` on data received from an external network connection.
  **Correction**: Use JSON (`m:json`) or XML with SAX parsing (`m:xmerl_sax_parser`) for untrusted external data. Never use Erlang term serialization for untrusted communication.

- **Error**: Assuming `binary_to_term(Data, [safe])` makes untrusted data safe.
  **Correction**: The `safe` option only prevents creation of new atoms. The data "still has to be validated and sanitized, since it can still be harmful to the Erlang application in other ways." The source recommends avoiding these functions entirely on untrusted data.

- **Error**: Using `xmerl_scan` to parse XML from untrusted sources.
  **Correction**: Use `xmerl_sax_parser` with the `disallow_entities` option instead, as `xmerl_scan` "dynamically produces new atoms and is therefore not suitable for decoding XML data originating untrusted sources."

# Common Confusions

- **Confusion**: Thinking that JSON decoding of untrusted data is always safe without validation.
  **Clarification**: "The decoded data, of course, needs to be validated and sanitized if it does not originate from a trusted entity." JSON is safer than Erlang terms because it cannot create atoms or arbitrary terms, but application-level validation is still required.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, DSG-011 rule (secure_coding.md, lines 1017-1045), DSG-003 atom deserialization guidance (lines 820-830), "xmerl Application" section (lines 374-383), and "Potentially Unsafe Functionality" table (lines 1407-1418).

# Verification Notes

- Definition source: Directly quoted from DSG-011 and related sections.
- Confidence rationale: High -- extensively covered across multiple sections with specific CWE references (CWE-502, CWE-74) and detailed unsafe function listings.
- Uncertainties: None.
- Cross-reference status: References CWE-502, CWE-74, OWASP A05:2025. Cross-references atom-exhaustion, input-validation.
