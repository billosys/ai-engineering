---
# === CORE IDENTIFICATION ===
concept: Repetition in Naming
slug: repetition-in-naming

# === CLASSIFICATION ===
category: naming
subcategory: redundancy
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Repetition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "naming redundancy"
  - "stutter in naming"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - package-names
extends: []
related:
  - variable-names
  - getters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is widget.NewWidget considered bad naming in Go?"
  - "Should variable names include their type?"
  - "How do I avoid redundancy between package name and symbol name?"
---

# Quick Definition

Avoid unnecessary repetition in names. Do not repeat the package name in exported symbols, the type in variable names, or external context (package, method, type) in local names. Evaluate repetition from the caller's perspective.

# Core Definition

Go source code should avoid unnecessary repetition in names. This manifests in three common forms: (1) Package vs. exported symbol -- when a package exports a type named after the package itself, the constructor should be `New`, not `NewWidget` in package `widget`. (2) Variable name vs. type -- the compiler knows the type, so `users int` is better than `numUsers int`, and `name string` is better than `nameString`. (3) External context vs. local names -- the package name, method name, type name, and function name all provide context that should not be repeated in local identifiers. Repetition should be evaluated from the perspective of the user of the symbol, not in isolation (Google Go Style Guide, "Style Decisions", "Repetition").

# Prerequisites

- **package-names** -- Understanding Go packages is needed to recognize package-vs-symbol repetition

# Key Properties

1. Package name should not repeat in exported symbol names: `widget.New` not `widget.NewWidget`
2. Type should not repeat in variable names: `users int` not `numUsers int`
3. Surrounding context should not repeat in local names: `Name()` not `ProjectName()` on `*Project`
4. Type qualifiers OK when disambiguating two forms: `limitStr` and `limit`
5. Evaluate from the user's (caller's) perspective

# Construction / Recognition

## To Apply:
1. Check if the exported name repeats the package name -- remove the redundant portion
2. Check if variable names encode their type -- remove the type encoding
3. Check if local names repeat information from the enclosing function, method, type, or package
4. When in doubt, read the fully qualified name from the caller's perspective

## To Recognize:
1. `widget.NewWidget` -- package name repeated in symbol
2. `numUsers int` -- type encoded in variable name
3. `func (p *Project) ProjectName()` -- type name repeated in method
4. `AdsTargetingRevenueReport` in package `ads/targeting/revenue/reporting` -- package path repeated in type

# Context & Application

Because Go uses qualified names (package.Symbol), there is always context available at the call site. The caller writes `widget.New()` which reads as "new widget" -- adding Widget to the constructor name would make it `widget.NewWidget()` which reads as "new widget widget." This redundancy adds length without information. The principle extends to variables and method names where surrounding context already provides the necessary qualification.

# Examples

**Example 1 -- Good: reducing package-symbol repetition** (Decisions, "Repetition"):

> Repetitive Name -> Better Name:
> - `widget.NewWidget` -> `widget.New`
> - `widget.NewWidgetWithName` -> `widget.NewWithName`
> - `db.LoadFromDatabase` -> `db.Load`
> - `goatteleportutil.CountGoatsTeleported` -> `gtutil.CountGoatsTeleported` or `goatteleport.Count`

**Example 2 -- Good: omitting type from variable names** (Decisions, "Repetition"):

Repetitive Name               | Better Name
----------------------------- | ----------------------
`var numUsers int`             | `var users int`
`var nameString string`        | `var name string`
`var primaryProject *Project`  | `var primary *Project`

**Example 3 -- Good: omitting context from local names** (Decisions, "Repetition"):

```go
// Good:
// In package "ads/targeting/revenue/reporting"
type Report struct{}

func (p *Project) Name() string
```

```go
// Bad:
// In package "ads/targeting/revenue/reporting"
type AdsTargetingRevenueReport struct{}

func (p *Project) ProjectName() string
```

**Example 4 -- Good vs Bad: context-aware naming** (Decisions, "Repetition"):

```go
// Bad:
func (db *DB) UserCount() (userCount int, err error) {
    var userCountInt64 int64
    if dbLoadError := db.LoadFromDatabase("count(distinct users)", &userCountInt64); dbLoadError != nil {
        return 0, fmt.Errorf("failed to load user count: %s", dbLoadError)
    }
    userCount = int(userCountInt64)
    return userCount, nil
}
```

```go
// Good:
func (db *DB) UserCount() (int, error) {
    var count int64
    if err := db.Load("count(distinct users)", &count); err != nil {
        return 0, fmt.Errorf("failed to load user count: %s", err)
    }
    return int(count), nil
}
```

# Relationships

## Related
- **variable-names** -- Variable naming guidelines complement repetition avoidance
- **getters** -- Dropping `Get` prefix is related to avoiding redundancy
- **package-names** -- Good package names reduce the need for verbose symbol names

# Common Errors

- **Error**: Naming a constructor `NewWidget` in package `widget`
  **Correction**: Use `New` -- the package name already provides "widget" context

- **Error**: Encoding the type in every variable name (`nameString`, `countInt`)
  **Correction**: Omit the type; use `name` and `count`

# Common Confusions

- **Confusion**: Thinking `type Report struct{}` is too generic in package `reporting`
  **Clarification**: The fully qualified name `reporting.Report` is perfectly clear to callers

- **Confusion**: Believing you should never include type information in a variable name
  **Clarification**: Type qualifiers are acceptable when disambiguating two forms of the same value (e.g., `limitStr` and `limit`)

# Source Reference

Chapter 3: Style Decisions, Section "Repetition" (including subsections on package vs. symbol, variable vs. type, and external context vs. local names).

# Verification Notes

- Definition source: Directly from the "Repetition" section and its three subsections in Google Go Style Decisions
- Confidence rationale: HIGH -- extensive examples with before/after patterns
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
