---
# === CORE IDENTIFICATION ===
concept: Rule Pillars
slug: rule-pillars

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
section: "Rule pillars"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Biome rule pillars"
  - "lint rule design principles"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-rules
extends: []
related:
  - biome-linter
  - rule-severity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What design principles guide Biome lint rules?"
  - "What should a Biome rule diagnostic communicate?"
---

# Quick Definition
The rule pillars are three design principles that every Biome lint rule should follow: explain the error, explain why the error is triggered, and tell the user what to do to fix it.

# Core Definition
In Biome, rules should be informative and explain to the user why a rule is triggered and tell them what they should do to fix the error. Every rule should follow three pillars:
1. Explain to the user the error -- generally implemented as the diagnostic message.
2. Explain to the user why the error is triggered -- generally implemented with an additional note.
3. Tell the user what they should do -- generally implemented using a code action; if a code action is not applicable, a note should tell the user what to do.

# Prerequisites
- lint-rules

# Key Properties
1. **Pillar 1: What** -- The diagnostic message explains what the error is
2. **Pillar 2: Why** -- An additional note explains why the error matters
3. **Pillar 3: How** -- A code action or note tells the user how to fix the error
4. **User-centric design** -- Rules are designed to educate, not just flag violations

# Construction / Recognition
- When evaluating a rule's diagnostic output, check for all three pillars
- A diagnostic message alone (Pillar 1) is insufficient -- it should also include the reason (Pillar 2) and remediation guidance (Pillar 3)
- If a rule lacks any pillar, an issue can be filed against the Biome repository

# Context & Application
The rule pillars distinguish Biome's approach to linting from tools that simply flag violations. By requiring rules to explain the "why" and provide actionable guidance, Biome aims to be educational rather than merely prescriptive. This design philosophy applies to all rules across all groups and domains.

# Examples
From linter/index.mdx, "Rule pillars" section:
- "1. Explain to the user the error. Generally, this is the message of the diagnostic."
- "2. Explain to the user **why** the error is triggered. Generally, this is implemented with an additional note."
- "3. Tell the user what they should do. Generally, this is implemented using a code action. If a code action is not applicable a note should tell the user what they should do to fix the error."

# Relationships
## Builds Upon
- lint-rules

## Enables
- Better diagnostic quality across all rules

## Related
- biome-linter
- rule-severity

## Contrasts With
- Linters that only report the violation without explaining why or how to fix it

# Common Errors
1. Submitting a rule contribution that only flags the violation without explaining why or how to fix it

# Common Confusions
1. **Pillars vs. severity** -- Pillars govern what a diagnostic communicates; severity governs how serious it is

# Source Reference
- linter/index.mdx: "Rule pillars" subsection

# Verification Notes
- High confidence: The three pillars are explicitly enumerated in the source
- All three pillar descriptions quoted from source
