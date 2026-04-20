---
# === CORE IDENTIFICATION ===
concept: Lint Rules
slug: lint-rules

# === CLASSIFICATION ===
category: linter
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "linter/index.mdx"
chapter_number: null
pdf_page: null
section: "Rules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "linter rules"
  - "Biome rules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-linter
extends: []
related:
  - lint-rule-groups
  - rule-severity
  - safe-fixes
  - unsafe-fixes
  - rule-pillars
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lint rule in Biome?"
  - "How do I enable or disable a lint rule?"
  - "What is the naming convention for Biome rules?"
---

# Quick Definition
A lint rule is a single unit of static analysis in Biome that enforces or denies a specific code pattern, emitting a diagnostic when it encounters a violation.

# Core Definition
A rule enforces or denies a code style, the use of something that could lead to a bug, or other code quality concerns. Rules follow a naming convention: rules starting with `use*` enforce or suggest something, while rules starting with `no*` deny something. When a rule encounters a violation, it emits a diagnostic. Each rule ships with a default severity and belongs to a group. Many rules provide automatic code fixes. Biome supports language-agnostic rules that work across more than one language.

# Prerequisites
- biome-linter

# Key Properties
1. **Naming convention** -- `use*` rules enforce/suggest; `no*` rules deny
2. **Diagnostics** -- Each violation produces a diagnostic with a message
3. **Default severity** -- Every rule ships with a default severity level
4. **Group membership** -- Each rule belongs to a group (e.g., suspicious, style, correctness)
5. **Recommended set** -- A subset of rules are recommended and enabled by default
6. **Language-agnostic capability** -- Some rules work across multiple languages (e.g., `noUselessEscapeInString` for both JavaScript and CSS)
7. **Code fixes** -- Many rules provide safe or unsafe automatic fixes

# Construction / Recognition
- Disable a rule: set it to `"off"` in `biome.json` under its group
- Enable with default severity: set it to `"on"`
- Change severity: set to `"error"`, `"warn"`, or `"info"`
- Configure options: use an object with `level` and `options` keys
- Disable all recommended rules: set `"recommended": false` at the rules level

Example configuration to disable a rule:
```json
{
  "linter": {
    "rules": {
      "suspicious": {
        "noDebugger": "off"
      }
    }
  }
}
```

Example configuration with options:
```json
{
  "linter": {
    "rules": {
      "style": {
        "useNamingConvention": {
          "level": "error",
          "options": {
            "strictCase": false
          }
        }
      }
    }
  }
}
```

# Context & Application
Rules are the fundamental building block of the Biome linter. Users configure them in `biome.json` to match project and organizational requirements. Rules can also be selectively run or skipped via CLI flags (`--only`, `--skip`).

# Examples
From linter/index.mdx, "Rules" section:
- `noDebugger` denies the use of `debugger` statements in JavaScript code
- `noUselessEscapeInString` is a language-agnostic rule that reports useless escape sequences in both JavaScript and CSS
- `noShoutyConstants` is a non-recommended rule that emits an information-level diagnostic by default

# Relationships
## Builds Upon
- biome-linter

## Enables
- rule-severity
- safe-fixes
- unsafe-fixes
- code-fix-configuration

## Related
- lint-rule-groups
- nursery-rules
- rule-pillars

## Contrasts With
- Formatting rules (Biome explicitly excludes formatting from linting)

# Common Errors
1. Expecting rules to handle formatting -- Biome separates linting and formatting
2. Assuming all rules are enabled by default -- only recommended rules are enabled; others require explicit opt-in

# Common Confusions
1. **"on" vs. severity values** -- `"on"` enables a rule with its default severity, while `"error"`/`"warn"`/`"info"` override the default
2. **Rule vs. group configuration** -- A rule can be configured individually or at the group level; individual settings override group settings

# Source Reference
- linter/index.mdx: "Rules" section and "Configure the linter" section

# Verification Notes
- High confidence: Rules are explicitly defined and documented in linter/index.mdx
- Naming convention and configuration syntax taken directly from source
