---
# === CORE IDENTIFICATION ===
concept: Function and Method Names (Best Practices)
slug: function-and-method-names-bp

# === CLASSIFICATION ===
category: naming
subcategory: function-naming
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Function and method names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "function name repetition"
  - "method name conventions"
  - "avoid repetition in names"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clarity-principle
extends:
  - repetition
related:
  - naming-principles
  - package-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What information should be omitted from function and method names?"
  - "How do I avoid redundancy between a function name and its package?"
  - "When should I use noun-like vs verb-like function names?"
---

# Quick Definition

Avoid repeating the package name, receiver type, parameter names, or return types in function and method names. Use noun-like names for functions that return values and verb-like names for functions that perform actions.

# Core Definition

When naming functions and methods, consider the context in which the name is read at the call site. The following can generally be omitted: the types of inputs and outputs (when no collision), the type of the method receiver, and whether an input or output is a pointer. Functions should not repeat the package name. Methods should not repeat the receiver name. Names should not repeat parameter variable names or return value types. When disambiguation is needed, extra information in the name is acceptable. Functions that return something use noun-like names (avoiding the `Get` prefix). Functions that do something use verb-like names. When identical functions differ only by type, include the type at the end of the name.

# Prerequisites

- **clarity-principle** -- Understanding that names should prioritize clarity for the reader

# Key Properties

1. Do not repeat the package name in function names (e.g., `yamlconfig.Parse` not `yamlconfig.ParseYAMLConfig`)
2. Do not repeat the receiver type in method names (e.g., `config.WriteTo` not `config.WriteConfigTo`)
3. Do not repeat parameter variable names in function names
4. Do not repeat return types in function names
5. Use noun-like names for functions returning values; avoid the `Get` prefix
6. Use verb-like names for functions performing actions
7. Append type name when disambiguating identical functions for different types

# Construction / Recognition

## To Apply:
1. Write the call site first to see how the name reads in context
2. Remove any part of the name that duplicates information already at the call site
3. Choose noun-like or verb-like form based on whether the function returns or acts
4. Add disambiguation only when truly needed (e.g., `WriteTextTo` vs `WriteBinaryTo`)

## To Recognize:
1. Call sites read naturally without redundant information
2. Function names are concise yet unambiguous at the call site
3. No `Get` prefix on value-returning functions

# Context & Application

This guidance applies broadly to all Go code. It is especially important for exported APIs where the call site readability matters most. The package name and receiver type are always visible at the call site, so repeating them in the function name wastes the reader's attention. When there is a clear "primary" version of a function, the type can be omitted (e.g., `Marshal` for bytes, `MarshalText` for string).

# Examples

**Example 1 -- Avoid repeating the package name**:

```go
// Bad:
package yamlconfig
func ParseYAMLConfig(input string) (*Config, error)

// Good:
package yamlconfig
func Parse(input string) (*Config, error)
```

**Example 2 -- Avoid repeating the receiver**:

```go
// Bad:
func (c *Config) WriteConfigTo(w io.Writer) (int64, error)

// Good:
func (c *Config) WriteTo(w io.Writer) (int64, error)
```

**Example 3 -- Noun-like names for return values**:

```go
// Good:
func (c *Config) JobName(key string) (value string, ok bool)

// Bad:
func (c *Config) GetJobName(key string) (value string, ok bool)
```

**Example 4 -- Type disambiguation**:

```go
// Good:
func ParseInt(input string) (int, error)
func ParseInt64(input string) (int64, error)
```

# Relationships

## Related
- **naming-principles** -- General naming guidance that this best practice extends
- **package-names** -- Package naming directly affects how function names read at call sites
- **repetition** -- The Decisions chapter section on avoiding repetition

## Contrasts With
(none)

# Common Errors

- **Error**: Prefixing getters with `Get` (e.g., `GetJobName`)
  **Correction**: Use a noun-like name instead (e.g., `JobName`)

- **Error**: Including the package name in the function (e.g., `yamlconfig.ParseYAMLConfig`)
  **Correction**: Remove the redundant package reference (e.g., `yamlconfig.Parse`)

# Common Confusions

- **Confusion**: Thinking shorter names are always better
  **Clarification**: When disambiguation is needed (e.g., `WriteTextTo` vs `WriteBinaryTo`), extra information is appropriate

- **Confusion**: Believing this rule means function names should always be one word
  **Clarification**: Multi-word names are fine when they add non-redundant information

# Source Reference

Chapter 4: Best Practices, Section "Naming" > "Function and method names".

# Verification Notes

- Definition source: Directly from "Function and method names" with "Avoid repetition" and "Naming conventions" subsections
- Confidence rationale: HIGH -- explicit guidance with clear good/bad examples
- Uncertainties: None
- Cross-reference status: References decisions#repetition, decisions#getters, decisions#repetitive-with-package
