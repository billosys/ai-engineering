---
# === CORE IDENTIFICATION ===
concept: Linter Domains
slug: linter-domains

# === CLASSIFICATION ===
category: linter-domains
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "linter/index.mdx"
chapter_number: null
pdf_page: null
section: "Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Biome domains"
  - "lint domains"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-linter
  - lint-rules
  - lint-rule-groups
extends: []
related:
  - project-domain
  - types-domain
  - nursery-rules
contrasts_with:
  - lint-rule-groups

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a linter domain?"
  - "What distinguishes lint rule groups from domains?"
  - "How do linter domains relate to rule groups?"
  - "What must I understand before configuring lint domains?"
---

# Quick Definition
Linter domains are a Biome feature that groups lint rules by technology or framework -- such as React, Solid, Next.js, or test -- rather than by problem type.

# Core Definition
Domains are a Biome feature that allow for grouping rules by technology, or domain. Examples include "react", "solid", "test", "next", "project", and "types". A domain has its own set of recommended rules, can be automatically enabled when Biome detects certain dependencies in the project's `package.json`, and can define additional global variables. Domains are configured under `linter.domains` in `biome.json` with values of `"recommended"`, `"all"`, or `"off"`.

# Prerequisites
- biome-linter
- lint-rules
- lint-rule-groups (to understand the distinction)

# Key Properties
1. **Technology-based grouping** -- Rules grouped by framework or technology, not problem type
2. **Auto-detection** -- Domains can be automatically enabled based on `package.json` dependencies
3. **Own recommended set** -- Each domain has its own recommended rules, separate from group-level recommendations
4. **Global variable definitions** -- Some domains define additional global bindings (e.g., test domain defines `describe`, `it`, `expect`)
5. **Three activation levels** -- `"recommended"` (non-nursery recommended rules), `"all"` (all rules), `"off"` (disabled)
6. **Available domains** -- drizzle, next, playwright, project, qwik, react, solid, test, turborepo, types, vue

# Construction / Recognition
- Enable recommended rules: `"test": "recommended"`
- Enable all rules: `"test": "all"`
- Disable: `"test": "off"`

```json
{
  "linter": {
    "domains": {
      "react": "recommended",
      "test": "all"
    }
  }
}
```

- Auto-detection example: if `mocha` dependency is detected, the `test` domain's recommended rules are enabled automatically

# Context & Application
Domains solve the problem of framework-specific rules that do not fit neatly into problem-type groups. They allow Biome to be intelligent about the project context -- a React project gets React-specific rules automatically without explicit configuration. Domains complement groups: a rule belongs to one group (e.g., correctness) and may also belong to one or more domains (e.g., react).

# Examples
From linter/index.mdx, "Domains" section:
- "Domains are a Biome feature that allow for grouping rules by technology, or well, domain. Examples of domains are 'react', 'solid', and 'test'."
- "Biome's linter will automatically enable the rules that belong to a domain when it detects certain dependencies in the nearest package.json."
- Auto-detection: "if the mocha dependency is detected, Biome will enable the recommended rules of the test domain"

From linter/domains.mdx:
- The test domain is activated by dependencies: jest >=26.0.0, mocha >=8.0.0, ava >=2.0.0, vitest >=1.0.0
- The react domain is activated by: react >=16.0.0
- The next domain is activated by: next >=14.0.0

# Relationships
## Builds Upon
- lint-rule-groups

## Enables
- project-domain
- types-domain
- Framework-specific linting without manual configuration

## Related
- nursery-rules (many domain rules are in nursery)

## Contrasts With
- lint-rule-groups -- Groups categorize by problem type (correctness, style, security); domains categorize by technology (react, test, project). A rule belongs to exactly one group but may belong to zero or more domains.

# Common Errors
1. Expecting "recommended" to enable nursery rules -- it only enables non-nursery recommended rules
2. Not understanding that auto-detection requires a `package.json` with the relevant dependency

# Common Confusions
1. **Groups vs. domains** -- Groups classify by what kind of problem the rule catches; domains classify by what technology the rule applies to
2. **"recommended" vs. "all"** -- Some domains have all rules in nursery, so "recommended" activates nothing; "all" is needed to enable nursery rules
3. **Conflicts between domains** -- React and Solid domains may enable conflicting rules; only one should be active

# Source Reference
- linter/index.mdx: "Domains" subsection
- linter/domains.mdx: Full domain listing with activation, dependencies, and rules

# Verification Notes
- High confidence: Domains are explicitly defined with clear semantics
- Domain list and auto-detection behavior verified against domains.mdx
