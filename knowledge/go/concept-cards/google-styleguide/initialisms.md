---
# === CORE IDENTIFICATION ===
concept: Initialisms
slug: initialisms

# === CLASSIFICATION ===
category: naming
subcategory: capitalisation
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Initialisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "acronym naming"
  - "initialism casing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mixed-caps
extends: []
related:
  - constant-names
  - variable-names
  - getters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should acronyms like URL and ID be capitalized in Go names?"
  - "How do I handle initialisms like gRPC or iOS in exported names?"
  - "Should I write XmlApi or XMLAPI?"
---

# Quick Definition

Initialisms and acronyms keep uniform case within the initialism: all caps or all lower. Special terms like gRPC and iOS follow their standard prose form unless exportedness requires changing the first letter, in which case the entire initialism changes case.

# Core Definition

Words in Go names that are initialisms or acronyms (e.g., `URL`, `NATO`, `ID`, `DB`) should have consistent case throughout -- either all uppercase or all lowercase. For example, `URL` appears as `URL` or `url`, never `Url`. When a name contains multiple initialisms (e.g., `XMLAPI`), each initialism maintains its own internal consistency but the initialisms need not match each other. For initialisms that contain a lowercase letter in standard prose (e.g., `gRPC`, `iOS`, `DDoS`), the standard prose form is used unless the first letter must change for exportedness, in which case the entire initialism shifts to the same case (Google Go Style Guide, "Style Decisions", "Initialisms").

# Prerequisites

- **mixed-caps** -- Understanding MixedCaps convention is essential for knowing where initialisms fit in compound names
- **Go exportedness rules** -- Exported identifiers must start with uppercase, which affects initialism casing

# Key Properties

1. Initialisms keep all letters the same case: `URL` or `url`, never `Url`
2. `ID` not `Id`, `DB` not `Db`
3. Multiple initialisms in one name each maintain their own case: `xmlAPI` is correct for unexported
4. Special initialisms (gRPC, iOS, DDoS) follow prose form when unexported
5. When exportedness forces a first-letter change, the whole initialism shifts: `iOS` becomes `IOS` when exported

# Construction / Recognition

## To Apply:
1. Identify initialisms in the name
2. Keep all letters within each initialism the same case
3. For special-form initialisms (gRPC, iOS), use prose form unless exportedness requires a change
4. If exportedness changes the first letter, change the entire initialism to match

## To Recognize:
1. Look for mixed-case initialisms like `Url`, `Id`, `Xml` -- these are incorrect
2. Check that multi-initialism names keep each initialism internally consistent
3. Verify special initialisms follow the correct rules when exported vs unexported

# Context & Application

This convention comes from the Go community's preference for readability and consistency. Since `URL` is always read as a single unit, mixing its case (`Url`) creates visual ambiguity. The special rules for terms like `gRPC` and `iOS` reflect practical reality: these are established brand names with non-standard capitalization that developers recognize in their standard form.

# Examples

**Example 1 -- Standard initialisms** (Decisions, "Initialisms"):

English Usage | Scope      | Correct  | Incorrect
------------- | ---------- | -------- | ---------
XML API       | Exported   | `XMLAPI` | `XmlApi`, `XMLApi`, `XmlAPI`, `XMLapi`
XML API       | Unexported | `xmlAPI` | `xmlapi`, `xmlApi`
ID            | Exported   | `ID`     | `Id`
ID            | Unexported | `id`     | `iD`
DB            | Exported   | `DB`     | `Db`

**Example 2 -- Special initialisms with lowercase letters** (Decisions, "Initialisms"):

English Usage | Scope      | Correct  | Incorrect
------------- | ---------- | -------- | ---------
iOS           | Exported   | `IOS`    | `Ios`, `IoS`
iOS           | Unexported | `iOS`    | `ios`
gRPC          | Exported   | `GRPC`   | `Grpc`
gRPC          | Unexported | `gRPC`   | `grpc`
DDoS          | Exported   | `DDoS`   | `DDOS`, `Ddos`
DDoS          | Unexported | `ddos`   | `dDoS`, `dDOS`

# Relationships

## Related
- **constant-names** -- Initialisms appear in constant names and follow these rules
- **variable-names** -- Initialisms in variable names follow the same pattern
- **mixed-caps** -- The overarching naming convention that initialisms must work within

# Common Errors

- **Error**: Writing `userId` instead of `userID`
  **Correction**: `ID` is an initialism; keep both letters the same case: `userID`

- **Error**: Writing `Grpc` for an exported name instead of `GRPC`
  **Correction**: When exporting gRPC, the entire initialism shifts to uppercase: `GRPC`

# Common Confusions

- **Confusion**: Thinking `Txn` is an initialism and should be `TXN`
  **Clarification**: `Txn` is an abbreviation (not an initialism/acronym), so only the first letter is capitalized when exported

- **Confusion**: Believing each initialism in a multi-initialism name must have the same case
  **Clarification**: Each initialism is independent -- `xmlAPI` is correct because `xml` is lowercase (unexported position) while `API` is uppercase

# Source Reference

Chapter 3: Style Decisions, Section "Initialisms".

# Verification Notes

- Definition source: Directly from the "Initialisms" section of Google Go Style Decisions
- Confidence rationale: HIGH -- complete table of correct/incorrect examples provided
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
