---
# === CORE IDENTIFICATION ===
concept: Variable Names
slug: variable-names

# === CLASSIFICATION ===
category: naming
subcategory: variables
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Variable names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "variable naming conventions"
  - "Go variable naming"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mixed-caps
extends: []
related:
  - single-letter-variable-names
  - repetition-in-naming
  - constant-names
contrasts_with:
  - reduce-scope-of-variables

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How long should variable names be in Go?"
  - "Should variable names include the type?"
  - "How does scope affect variable name length in Go?"
---

# Quick Definition

Variable name length should be proportional to scope size and inversely proportional to usage frequency. Avoid including the type in the name. Name by role in current context, not by origin.

# Core Definition

The general rule for Go variable naming is that name length should be proportional to the size of the scope and inversely proportional to the number of times the variable is used within that scope. A file-scope variable may need multiple words, while a variable in a single inner block may need only one word or a character or two. Names should reflect what the variable contains and how it is used in the current context, rather than where the value originated. Types and type-like words should be omitted from most variable names -- `userCount` is better than `numUsers` or `usersInt`, and `users` is better than `userSlice` (Google Go Style Guide, "Style Decisions", "Variable names").

# Prerequisites

- **mixed-caps** -- All variable names follow Go's MixedCaps convention
- **Go scoping rules** -- Understanding block scope, function scope, and file scope

# Key Properties

1. Name length proportional to scope size (small scope = short name)
2. Name length inversely proportional to usage frequency (more uses = shorter name is OK)
3. Omit types from names: `users` not `userSlice`, `count` not `countInt`
4. Name by role in current context, not by origin
5. Omit words clear from surrounding context
6. Scope guidelines: small (1-7 lines), medium (8-15), large (15-25), very large (25+)

# Construction / Recognition

## To Apply:
1. Assess the scope size where the variable lives
2. Choose a name length appropriate to that scope
3. Use a name that describes the variable's role, not its type or origin
4. Drop type suffixes (`Int`, `String`, `Slice`) unless disambiguating two forms of same value
5. Drop context already provided by the enclosing function, method, or package name

## To Recognize:
1. Look for very long names in small scopes -- they add noise
2. Look for very short names in large scopes -- they may be unclear
3. Look for type-encoding in names (`numUsers`, `nameString`) -- these should be simplified
4. Look for names that repeat information from the enclosing context

# Context & Application

This principle balances readability with conciseness. In a 3-line loop, `i` is perfectly clear. In a 50-line function, `i` becomes ambiguous. The advice to omit types reflects Go's strong typing: the compiler knows the type, and in most cases the reader can infer it from usage. Including types in names is redundant noise. The exception is when two representations of the same value coexist (e.g., `ageString` and `age` for raw and parsed forms).

# Examples

**Example 1 -- Good: scope-appropriate naming** (Decisions, "Variable names"):

```go
// Small scope: short name is fine
for i, v := range items {
    process(v)
}

// Large scope: more descriptive name needed
var primaryProject *Project
```

**Example 2 -- Good: omit types from names** (Decisions, "Variable names"):

```go
// Good:
var users int       // not numUsers or usersInt
var name string     // not nameString
var primary *Project // not primaryProject
```

**Example 3 -- Good: disambiguating two forms of same value** (Decisions, "Variable names"):

```go
// Good: type qualifier acceptable when two versions coexist
limitRaw := r.FormValue("limit")
limit, err := strconv.Atoi(limitRaw)
```

```go
// Also good:
limitStr := r.FormValue("limit")
limit, err := strconv.Atoi(limitStr)
```

**Example 4 -- Good: name by context, not origin** (Decisions, "Variable names"):

```go
// Good: single-word starting point, add words to disambiguate
count := db.UserCount()
userCount := db.UserCount()
projectCount := db.ProjectCount()
```

# Relationships

## Related
- **single-letter-variable-names** -- The extreme short end of variable naming
- **repetition-in-naming** -- Avoiding redundancy between name and its context
- **constant-names** -- Constants follow similar role-based naming principles

## Contrasts With
- **reduce-scope-of-variables** (Uber style) -- Uber focuses on reducing scope; Google focuses on matching name length to scope

# Common Errors

- **Error**: Using `numUsers` or `usersInt` instead of `users`
  **Correction**: Omit the type -- `users` is sufficient since the type is known from context

- **Error**: Using `Sbx` as an abbreviation for `Sandbox` to save typing
  **Correction**: Do not simply drop letters; `Sandbox` is preferred, especially for exported names

# Common Confusions

- **Confusion**: Thinking all short variable names are bad
  **Clarification**: Short names are preferred in small scopes. `db` is fine even in large scopes when there is only one database.

- **Confusion**: Believing the local variable name should match the struct field name
  **Clarification**: The best local name reflects the current context, which may differ from the field or proto name

# Source Reference

Chapter 3: Style Decisions, Section "Variable names".

# Verification Notes

- Definition source: Directly from the "Variable names" section of Google Go Style Decisions
- Confidence rationale: HIGH -- detailed guidelines with examples and scope size definitions
- Uncertainties: Scope size ranges are described as rough baselines, not strict rules
- Cross-reference status: Related slugs verified against planned extractions
