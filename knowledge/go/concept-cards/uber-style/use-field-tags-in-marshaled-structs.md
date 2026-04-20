---
# === CORE IDENTIFICATION ===
concept: Use Field Tags in Marshaled Structs
slug: use-field-tags-in-marshaled-structs

# === CLASSIFICATION ===
category: code-safety
subcategory: serialization
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Use field tags in marshaled structs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "struct field tags"
  - "json tags on structs"
  - "marshaling tags"
  - "serialization tags"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - be-consistent
  - group-similar-declarations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should struct fields always have json/yaml tags?"
  - "What happens if you rename a struct field without tags?"
  - "How do field tags protect serialization contracts?"
---

# Quick Definition

Any struct field that is marshaled into JSON, YAML, or other tag-based formats should always be annotated with the relevant tag (e.g., `json:"name"`) to make the serialization contract explicit and guard against breakage from field renaming.

# Core Definition

The serialized form of a structure is a contract between different systems. When struct fields are marshaled to JSON, YAML, or other formats that support tag-based field naming, the field names become part of that contract. Without explicit tags, Go uses the exported field name directly, meaning any rename of the Go field silently changes the serialized output and breaks the contract.

By always specifying field names inside tags, the contract is made explicit. Refactoring or renaming fields in Go code will not accidentally change the serialized form.

# Prerequisites

Understanding of Go struct tags and the `encoding/json` (or equivalent) marshaling mechanism.

# Key Properties

1. **Explicit contract** -- Tags make the mapping between Go field names and serialized field names visible and intentional.
2. **Refactoring safety** -- Renaming a Go struct field does not change the serialized output when tags are present.
3. **Cross-system compatibility** -- External systems consuming serialized data depend on stable field names; tags ensure stability.
4. **Applies to all tag-based formats** -- JSON, YAML, and any format that supports tag-based field naming.

# Construction / Recognition

## To Construct/Create:
1. For every exported struct field that will be marshaled, add the appropriate tag: `json:"fieldName"`, `yaml:"field_name"`, etc.
2. Use consistent casing conventions in tags (typically camelCase for JSON, snake_case for YAML).

## To Identify/Recognize:
1. Look for structs used with `json.Marshal`, `yaml.Marshal`, or similar serialization functions.
2. Check that all exported fields in such structs have the corresponding format tags.

# Context & Application

- **Typical contexts**: API request/response types, configuration structs, data transfer objects.
- **Common applications**: REST API payloads, configuration file parsing, database record serialization.

# Examples

**Example 1** (source: Uber Go Style Guide, Ch 2):

Bad:
```go
type Stock struct {
  Price int
  Name  string
}

bytes, err := json.Marshal(Stock{
  Price: 137,
  Name:  "UBER",
})
```

Good:
```go
type Stock struct {
  Price int    `json:"price"`
  Name  string `json:"name"`
  // Safe to rename Name to Symbol.
}

bytes, err := json.Marshal(Stock{
  Price: 137,
  Name:  "UBER",
})
```

# Relationships

- **Related to** `be-consistent`: Consistent use of tags across all marshaled structs is part of maintaining codebase consistency.
- **Related to** `group-similar-declarations`: Struct field declarations benefit from organized, consistent formatting including tags.

# Common Errors

1. **Omitting tags on exported fields** -- Without tags, renaming `Name` to `Symbol` changes the JSON output from `"Name"` to `"Symbol"`, breaking consumers.
2. **Inconsistent tag casing** -- Mixing `json:"Name"` and `json:"name"` across structs creates an inconsistent API surface.
3. **Forgetting tags on new fields** -- When adding fields to an existing tagged struct, forgetting to add the tag breaks the pattern.

# Common Confusions

1. **Tags vs. field names** -- Tags control the serialized name; the Go field name controls how the field is referenced in code. They serve different purposes.
2. **Unexported fields** -- Unexported (lowercase) fields are never marshaled by `encoding/json`, so tags on them are unnecessary for serialization (though they may be used by other libraries).

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Guidelines" (Ch 2)
- Section: "Use field tags in marshaled structs"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with clear Bad/Good example and rationale about serialization contracts.
