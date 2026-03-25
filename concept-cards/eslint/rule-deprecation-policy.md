---
# === CORE IDENTIFICATION ===
concept: Rule Deprecation Policy
slug: rule-deprecation-policy

# === CLASSIFICATION ===
category: maintenance
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/rule-deprecation.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint rule deprecation"
  - "DeprecatedInfo"
  - "rule deprecation metadata"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - rules
extends: []
related:
  - core-rules-policy
  - plugins
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are ESLint rules deprecated?"
  - "What metadata describes a deprecated rule?"
  - "How do I specify a replacement for a deprecated rule?"
  - "What is the DeprecatedInfo type?"
  - "What is the difference between the old and new deprecation format?"
---

# Quick Definition
ESLint's rule deprecation system uses structured metadata (the `DeprecatedInfo` type) to describe why a rule is deprecated, when it was deprecated, when it may be removed, and what rules can replace it.

# Core Definition
The rule deprecation metadata in ESLint describes whether a rule is deprecated and how it can be replaced. The system has evolved from a legacy format where `deprecated` was a simple boolean and `replacedBy` was a top-level array, to a new format where `deprecated` is either a boolean or a `DeprecatedInfo` object that contains all deprecation information.

The `DeprecatedInfo` type includes: `message` (a user-facing explanation), `url` (a link to more information), `replacedBy` (an array of `ReplacedByInfo` objects), `deprecatedSince` (the semver version that deprecated the rule), and `availableUntil` (the semver version likely to remove the rule, or `null` to indicate the rule will be kept but not changed).

Each `ReplacedByInfo` object describes a single replacement option with: `message`, `url`, `plugin` (an `ExternalSpecifier` identifying which plugin has the replacement -- use "eslint" for core rules, omit for same-plugin), and `rule` (an `ExternalSpecifier` identifying the replacement rule).

The `ExternalSpecifier` type has `name` (package name or rule id) and `url` (documentation link).

# Prerequisites
- eslint: Basic ESLint knowledge
- rules: Understanding of ESLint rule structure

# Key Properties
1. **Structured deprecation** -- The new format uses `DeprecatedInfo` object instead of a simple boolean
2. **Replacement tracking** -- `replacedBy` is now nested inside `deprecated` rather than at the top level
3. **Version tracking** -- `deprecatedSince` and `availableUntil` track the deprecation lifecycle
4. **Null availableUntil** -- Special value `null` means the rule will no longer be changed but will be kept available indefinitely
5. **Cross-plugin replacements** -- Replacements can point to rules in other plugins using `ExternalSpecifier`
6. **All properties optional** -- Every property in `DeprecatedInfo`, `ReplacedByInfo`, and `ExternalSpecifier` is optional

# Construction / Recognition
New deprecation format in rule meta:
```javascript
meta: {
  deprecated: {
    message: "Use the `@stylistic/indent` rule instead.",
    url: "https://eslint.org/docs/rules/indent",
    replacedBy: [{
      plugin: { name: "@stylistic/eslint-plugin", url: "..." },
      rule: { name: "indent", url: "..." }
    }],
    deprecatedSince: "8.53.0",
    availableUntil: null
  }
}
```

Legacy format (still supported):
```javascript
meta: {
  deprecated: true,
  replacedBy: ["@stylistic/indent"]
}
```

# Context & Application
Understanding the deprecation metadata is important for plugin authors who need to deprecate their own rules, tool authors who display deprecation information, and ESLint users who need to understand why rules are being phased out and what to use instead. The structured format enables tooling to automatically suggest replacements.

# Examples
From extend/rule-deprecation.md:
- "The legacy format used the two top-level rule meta properties `deprecated` (as a boolean only) and `replacedBy`."
- "In the new format, `deprecated` is a boolean or an object of type `DeprecatedInfo`, and `replacedBy` should be defined inside `deprecated` instead of at the top-level."
- "`availableUntil` -- The special value `null` means the rule will no longer be changed but will be kept available."

# Relationships
## Part Of
- rules (metadata component)

## Related
- core-rules-policy
- plugins

## Contrasts With
- Frozen rules (still active and maintained; deprecated rules are being phased out)

# Common Errors
1. Using the legacy top-level `replacedBy` format -- should now be nested inside `deprecated`
2. Forgetting to specify `plugin` in `ReplacedByInfo` when the replacement is in a different plugin
3. Setting `availableUntil` to `null` when the rule will actually be removed (null means "kept forever")

# Common Confusions
1. **Deprecated vs. frozen** -- Deprecated rules are being phased out; frozen rules are maintained but won't get new features
2. **`availableUntil: null` vs. omitted** -- `null` explicitly means "kept available indefinitely"; omitted means unknown

# Source Reference
- extend/rule-deprecation.md: Complete deprecation metadata type definitions and format documentation

# Verification Notes
- High confidence: Type definitions and format rules are explicitly documented
- All type properties taken directly from the source documentation
