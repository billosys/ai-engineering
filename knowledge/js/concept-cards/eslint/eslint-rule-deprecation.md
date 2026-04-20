---
# === CORE IDENTIFICATION ===
concept: ESLint Rule Deprecation
slug: eslint-rule-deprecation

# === CLASSIFICATION ===
category: usage
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/rule-deprecation.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "deprecated rules"
  - "frozen rules"
  - "rule lifecycle"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-getting-started
extends: []
related:
  - eslint-cli
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when an ESLint rule is deprecated?"
  - "Will deprecated rules be removed from ESLint?"
  - "Can I still use deprecated rules?"
---

# Quick Definition
ESLint's rule deprecation policy ensures rules are never removed unless replaced by another core rule or a functionally equivalent plugin rule. Deprecated rules receive no further maintenance but continue to work indefinitely.

# Core Definition
The ESLint team follows strict guidelines for rule deprecation to minimize disruption during upgrades. A rule will never be removed from ESLint unless: (1) it has been replaced by another core rule, or (2) a plugin exists with a functionally equivalent rule. Deprecated rules are marked as such in all documentation. Once deprecated, the team performs no further work on the rule -- no bug fixes, enhancements, or documentation updates. Issues and pull requests for deprecated rules are closed without action. Users can continue using deprecated rules indefinitely as long as they function correctly, but should be aware they are effectively unmaintained and may eventually be removed.

# Prerequisites
- eslint-getting-started -- Understanding of ESLint rules and configuration

# Key Properties
1. **Never removed without replacement** -- Rules are only removed if a core or plugin replacement exists
2. **Marked in documentation** -- All deprecated rules are clearly labeled
3. **No further maintenance** -- No bug fixes, enhancements, or doc updates after deprecation
4. **Issues/PRs closed** -- Related issues and pull requests are not accepted
5. **Indefinite usage** -- Deprecated rules continue to work and can be used as long as they function
6. **Effectively frozen** -- The rule's behavior is locked at the time of deprecation

# Construction / Recognition
Deprecated rules are identified by:
- Documentation marking them as deprecated
- The `usedDeprecatedRules` property in `LintResult` objects from the Node.js API
- Warnings in CLI output when deprecated rules are active

# Context & Application
Rule deprecation is a key aspect of ESLint's commitment to backward compatibility. When the team identifies that a rule's functionality is better served by a plugin (e.g., formatting rules moved to `@stylistic/eslint-plugin`), the core rule is deprecated rather than removed. This allows existing configurations to continue working without immediate changes while encouraging migration to the replacement.

# Examples
From use/rule-deprecation.md:
- A rule replaced by another core rule: the original is deprecated and documented
- A rule replaced by a plugin: the original is deprecated, the plugin equivalent is recommended

# Relationships
## Builds Upon
- eslint-getting-started (rules are part of ESLint configuration)
## Related
- eslint-cli (deprecated rule warnings appear in CLI output)

# Common Errors
1. Expecting bug fixes for deprecated rules -- they are effectively unmaintained
2. Filing issues for deprecated rules -- they will be closed without action

# Common Confusions
1. **Deprecated vs removed** -- Deprecated rules still work and can be used; they are not deleted
2. **Frozen behavior** -- A deprecated rule will not receive fixes even for incorrect behavior

# Source Reference
- use/rule-deprecation.md: Complete deprecation policy guidelines

# Verification Notes
Directly documented with clear policy statements. High confidence.
