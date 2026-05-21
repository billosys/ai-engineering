---
# === CORE IDENTIFICATION ===
concept: JSON-to-Erlang Term Representation
slug: json-erlang-representation

# === CLASSIFICATION ===
category: data-types
subcategory: serialization
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.2.2. The C side of the port"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "json() representation"
  - JSON term mapping

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - sax-style-parsing
  - external-term-format
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is JSON data represented as Erlang terms in this chapter?"
  - "Why is a JSON array represented as a tuple and a map as a list?"
  - "What does JSON null map to in Erlang?"
---

# Quick Definition

The chapter's JSON parser maps JSON values onto Erlang terms: `null` becomes `'undefined'`, strings become binaries, arrays become tuples, and maps (objects) become lists of key/value tuples.

# Core Definition

Before coding the YAJL parser callbacks, the chapter decides how JSON data should be represented as Erlang terms. The representation follows Erlang's conventions, is space-efficient, and is unambiguous: JSON `null` becomes the atom `'undefined'`; `true`/`false` become the atoms `'true'`/`'false'`; integers and floats become Erlang numbers; JSON strings (including map labels) become binaries; a JSON array `[x1, x2, ...]` becomes an Erlang tuple `{json(), json(), ...}`; and a JSON map (object) `{"abc": x1, ...}` becomes an Erlang list of `{binary(), json()}` pairs. Representing arrays as tuples and maps as lists makes the two unambiguously distinguishable ("Erlang and OTP in Action," Ch. 12, Section 12.2.2, Table 12.1).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. JSON `null` → the atom `'undefined'` (matching Erlang conventions better than a `null` atom).
2. JSON `true`/`false` → the atoms `'true'`/`'false'`.
3. JSON numbers (integers and floats) → Erlang `number()`.
4. JSON strings (and map keys) → Erlang `binary()` (space-efficient).
5. JSON array `[x1, x2, ...]` → Erlang tuple `{json(), json(), ...}`.
6. JSON map (object) → Erlang list of `{binary(), json()}` pairs.
7. Arrays-as-tuples vs maps-as-lists makes the two distinguishable; tuples allow indexing and use less space than lists.

# Construction / Recognition

## To Construct/Create:
1. While parsing JSON, emit `'undefined'` for null, atoms for booleans, numbers for numbers, binaries for strings.
2. Emit a tuple for each array and a list of key/value tuples for each map.

## To Identify/Recognize:
1. In a parsed result, a tuple is a JSON array, a list of `{binary, _}` pairs is a JSON map, a bare binary is a JSON string.

# Context & Application

- **Typical contexts**: Translating between JSON documents and Erlang data.
- **Common applications**: The result of `json_parser:parse_document/1`.
- **Historical/stylistic notes**: The chapter refers to JSON objects as *maps*, following YAJL's terminology. The tuple-array representation trades cheap indexing against costlier element insertion/removal.

# Examples

**Example 1** (Table 12.1): JSON `"..."` (string) maps to Erlang `binary()`; JSON `[x1, x2, ...]` maps to `{json(), json(), ...}`; JSON `{"abc": x1, ...}` maps to `[{binary(), json()}, ...]`.

**Example 2** (Section 12.4.3): `parse_document(<<"[null, true, {\"int\": 42, \"float\": 3.14}]">>)` returns `{ok,{undefined,true,[{<<"int">>,42},{<<"float">>,3.14}]}}`.

# Relationships

## Related
- **SAX-style parsing** — The YAJL callbacks build this representation as the document is parsed.
- **External term format** — The representation is what is serialized back to Erlang over a port.

# Common Errors

- **Error**: Representing JSON arrays as Erlang lists.
  **Correction**: Arrays are tuples; lists are reserved for maps, keeping the two unambiguous.

# Common Confusions

- **Confusion**: Expecting JSON `null` to map to a `null` atom.
  **Clarification**: It maps to `'undefined'`, which suits Erlang's conventions better.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.2.2 "The C side of the port," subsection "Encoding JSON data as Erlang terms." See Table 12.1.

# Verification Notes

- Definition source: Direct adaptation of Table 12.1 and the surrounding prose.
- Confidence rationale: HIGH — the book gives an explicit representation table.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
