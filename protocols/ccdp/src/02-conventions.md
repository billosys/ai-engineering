# 2. Status of This Memo and Conventions

## 2.1. Status of This Memo

This document specifies a protocol for composite cognition dispatch. It is published as an initial specification for examination, implementation feedback, and iterative refinement. Distribution is unlimited.

This specification is versioned using semantic versioning (MAJOR.MINOR.PATCH). The current version is 0.1.0. A MAJOR version increment indicates breaking changes to the wire format or core semantics. A MINOR version increment indicates backward-compatible additions. A PATCH version increment indicates clarifications or corrections.

## 2.2. Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC 2119] [RFC 8174] when, and only when, they appear in all capitals, as shown here.

## 2.3. Data Format Conventions

This specification uses JSON [RFC 8259] for all data representation. Field names use `snake_case`. Timestamps use ISO 8601 format with mandatory UTC timezone designator (`Z`). Unique identifiers use UUID v4 [RFC 9562] unless otherwise specified.

All examples in this document are informative unless explicitly marked as normative. Where examples show JSON structures, elided fields are indicated by comments (`// ...`) and do not imply that those fields are optional.

## 2.4. Notation

When this specification refers to a message field, it uses dot notation: `envelope.request_id` refers to the `request_id` field within the `envelope` object. Array elements are indicated by bracket notation: `envelope.provenance.evidence[0]` refers to the first element of the `evidence` array within the `provenance` object.

The notation `Section N` refers to sections of this specification by their number. Cross-references to other standards use their document identifier (e.g., [RFC 2119]).
