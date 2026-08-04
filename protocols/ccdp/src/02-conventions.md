# 2. Status of This Memo and Conventions

## 2.1. Status of This Memo

This document specifies a protocol for composite cognition dispatch. It is published as an initial specification for examination, implementation feedback, and iterative refinement. Distribution is unlimited.

This specification is versioned following Semantic Versioning [SemVer] (MAJOR.MINOR.PATCH). The current version is 0.2.0. A MAJOR version increment indicates breaking changes to the wire format or core semantics. A MINOR version increment indicates backward-compatible additions. A PATCH version increment indicates clarifications or corrections.

This specification uses two independent version identifiers. The **document version** (currently 0.2.0) tracks the maturity of the specification text — its completeness, internal consistency, and review status. The **wire protocol version** (currently `"1.0"`, carried in every message's `envelope.ccdp_version` field) tracks the on-the-wire format. A document revision that clarifies prose, tightens conformance requirements, or adds non-breaking features increments the document version without changing the wire protocol version. A document revision that changes message structure, adds required envelope fields, or alters wire semantics increments the wire protocol version. Implementations negotiate by wire protocol version; the document version is for human readers and specification governance.

## 2.2. Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC 2119] [RFC 8174] when, and only when, they appear in all capitals, as shown here.

## 2.3. Data Format Conventions

This specification uses JSON [RFC 8259] for all data representation. Field names use `snake_case`. Timestamps use ISO 8601 format with mandatory UTC timezone designator (`Z`). Unique identifiers use UUID v4 [RFC 9562] unless otherwise specified.

Trace identifiers (`trace_id`) and span identifiers (`span_id`) use W3C Trace Context format — 32-character and 16-character lowercase hexadecimal strings respectively — not UUID format. Where this specification says "unique identifiers use UUID v4," it refers to application-level identifiers such as `request_id` and `idempotency_key`, not trace-context identifiers.

All examples in this document are informative unless explicitly marked as normative. Where examples show JSON structures, elided fields are indicated by comments (`// ...`) and do not imply that those fields are optional.

Where examples show JSON structures with `// ...` comments, the comments are an expository convenience and are not valid JSON. Implementations MUST NOT include comments in wire-format messages. The content type for all CCDP messages is `application/json` with charset UTF-8. JSON numbers follow IEEE 754 double-precision semantics; implementations requiring higher precision for monetary or cryptographic values SHOULD use string-encoded representations. Enumeration values in this specification use `UPPER_SNAKE_CASE` (e.g., `FORMALLY_VERIFIED`, `SEARCH_EXHAUSTED`). URI-form identifiers (capability types, metadata namespace keys) use dot-separated segments (e.g., `org.ccdp.language.generation`). These conventions are normative for wire-format values.

## 2.4. Notation

When this specification refers to a message field, it uses dot notation: `envelope.request_id` refers to the `request_id` field within the `envelope` object. Array elements are indicated by bracket notation: `envelope.provenance.evidence[0]` refers to the first element of the `evidence` array within the `provenance` object.

The notation `Section N` refers to sections of this specification by their number. Cross-references to other standards use their document identifier (e.g., [RFC 2119]).

## 2.5. Normative Status of Non-Prose Elements

All examples in this specification are informative unless explicitly marked as normative. Tables that list requirements use normative language (MUST, SHOULD, MAY) and carry the same force as prose requirements. Diagrams are informative aids. Design notes (marked as such) are informative rationale and do not create protocol obligations.
