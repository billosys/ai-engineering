---
# === CORE IDENTIFICATION ===
concept: Nursery Rules
slug: nursery-rules

# === CLASSIFICATION ===
category: linter
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "linter/index.mdx"
chapter_number: null
pdf_page: null
section: "Nursery"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "nursery group"
  - "unstable rules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-rules
  - lint-rule-groups
extends:
  - lint-rule-groups
related:
  - rule-severity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are nursery rules?"
  - "Why do some rules require explicit opt-in?"
  - "What happens to nursery rules over time?"
---

# Quick Definition
Nursery rules are new Biome lint rules still under development that require explicit opt-in on stable versions because they may have bugs or performance problems.

# Core Definition
Nursery is a special rule group for new rules that are still under development. Nursery rules require explicit opt-in via configuration on stable versions because they may still have bugs or performance problems, even if they are marked as recommended. On nightly builds, nursery rules are enabled by default. Their diagnostic severity may be set to either error or warning depending on whether the team intends the rule to be recommended when stabilized. Nursery rules get promoted to other groups once they become stable, or may be removed entirely.

# Prerequisites
- lint-rules
- lint-rule-groups

# Key Properties
1. **Explicit opt-in required** -- Not enabled by default on stable versions, even if marked recommended
2. **Enabled on nightly** -- Automatically enabled on nightly builds for testing
3. **May have bugs** -- Explicitly acknowledged to potentially contain bugs or performance issues
4. **Promotion path** -- Rules graduate to other groups once stable, or get removed
5. **No semver guarantees** -- Rules in the nursery group are not subject to semantic versioning
6. **Variable severity** -- May be error or warning depending on intended future recommendation status

# Construction / Recognition
- Enable a nursery rule explicitly in configuration:
```json
{
  "linter": {
    "rules": {
      "nursery": {
        "someNewRule": "error"
      }
    }
  }
}
```
- Nursery rules are identifiable in the domains documentation by the "(nursery)" annotation next to the rule name

# Context & Application
The nursery group serves as an incubation area for new rules. It allows the Biome team to ship rules early for feedback while protecting stable users from potential issues. This is particularly relevant for domain-specific rules -- many domain rules (e.g., in the types, playwright, and turborepo domains) are currently in nursery, meaning enabling the domain with "recommended" may activate fewer rules than expected.

# Examples
From linter/index.mdx, "Nursery" section:
- "New rules that are still under development."
- "Nursery rules require explicit opt-in via configuration on stable versions because they may still have bugs or performance problems."
- "Nursery rules get promoted to other groups once they become stable or may be removed."

From linter/domains.mdx:
- The Types domain currently has all rules in nursery: `noFloatingPromises`, `noMisusedPromises`, `noUnnecessaryConditions`, etc.
- Several domains note: "Since all rules in this domain are nursery rules, no rules will be activated when enabling the domain."

# Relationships
## Builds Upon
- lint-rule-groups (nursery is a specific group)

## Enables
- Early testing and feedback on new rules

## Related
- rule-severity (nursery rules have variable default severity)
- linter-domains (many domain rules are nursery)

## Contrasts With
- Stable groups (correctness, style, etc.) that are subject to semver

# Common Errors
1. Enabling a domain and expecting all its rules to activate -- many domain rules are in nursery and require individual opt-in
2. Relying on nursery rule behavior in CI -- rules may change or be removed without semver notice

# Common Confusions
1. **"Recommended" nursery rules** -- Even if a nursery rule is marked recommended, it still requires explicit opt-in on stable versions
2. **Domain activation vs. nursery** -- Enabling a domain with "recommended" only activates non-nursery recommended rules

# Source Reference
- linter/index.mdx: "Nursery" subsection under "Linter Groups"
- linter/domains.mdx: Multiple domain sections noting nursery status

# Verification Notes
- High confidence: Nursery behavior is explicitly documented
- Cross-referenced with domains.mdx for practical implications
