---
# === CORE IDENTIFICATION ===
concept: Types Domain
slug: types-domain

# === CLASSIFICATION ===
category: linter-domains
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "linter/domains.mdx"
chapter_number: null
pdf_page: null
section: "Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "type-aware rules"
  - "type inference rules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linter-domains
  - project-domain
extends:
  - linter-domains
related:
  - nursery-rules
contrasts_with:
  - project-domain

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the types domain?"
  - "How does Biome use type inference for linting?"
  - "What must I understand before configuring lint domains?"
---

# Quick Definition
The types domain contains lint rules powered by Biome's type inference engine, enabling analysis that requires knowledge of expression types, such as detecting floating promises or unnecessary conditions.

# Core Definition
The types domain contains rules that perform project-level analysis using Biome's module graph for dependency resolution and its inference engine to resolve and flatten types. When rules belonging to this domain are enabled, Biome scans the entire project and enables the inference engine. This has a performance impact on the linting process, similar to the project domain but with the additional cost of type resolution.

# Prerequisites
- linter-domains
- project-domain (understanding of Scanner behavior)

# Key Properties
1. **Type inference** -- Rules use Biome's built-in inference engine, not TypeScript's compiler
2. **Scanner + inference** -- Enables both the project Scanner and the type inference engine
3. **All rules currently in nursery** -- As of the current documentation, all types-domain rules are in the nursery group
4. **No recommended rules yet** -- Enabling with "recommended" activates nothing; individual rules must be enabled explicitly
5. **Performance cost** -- Includes the Scanner overhead plus type resolution overhead

# Construction / Recognition
Since all rules are in nursery, "recommended" activates nothing. Enable individual rules:
```json
{
  "linter": {
    "domains": {
      "types": "all"
    }
  }
}
```

Types-domain rules include:
- `noFloatingPromises` (nursery)
- `noMisusedPromises` (nursery)
- `noUnnecessaryConditions` (nursery)
- `useArraySortCompare` (nursery)
- `useAwaitThenable` (nursery)
- `useConsistentEnumValueType` (nursery)
- `useExhaustiveSwitchCases` (nursery)
- `useFind` (nursery)
- `useNullishCoalescing` (nursery)
- `useRegexpExec` (nursery)

# Context & Application
The types domain represents Biome's move toward TypeScript-aware linting without requiring the TypeScript compiler. Rules like `noFloatingPromises` detect unhandled promises by inferring the return type of expressions -- functionality previously only available through `typescript-eslint` with its full type-checking integration. Since Biome v2, the toolchain uses TypeScript type definitions to infer types, scanning `.d.ts` files including those of transitive dependencies.

# Examples
From linter/domains.mdx, "Types" section:
- "This domain contains rules that perform project-level analysis. This includes our module graph for dependency resolution. When enabling rules that belong to this domain, Biome will scan the entire project, and it will enable the inference engine to resolve and flat types."

From linter/index.mdx, FAQ:
- "Since Biome v2, the toolchain is now able to use TypeScript to infer types and provide more powerful rules."
- "Biome scans .d.ts files inside the node_modules folder, including those of transitive dependencies."

# Relationships
## Builds Upon
- linter-domains
- project-domain (shares Scanner infrastructure)

## Enables
- Type-aware linting without the TypeScript compiler

## Related
- nursery-rules (all types-domain rules are currently nursery)

## Contrasts With
- project-domain -- Project domain focuses on module graph and import resolution; types domain adds type inference on top of the module graph

# Common Errors
1. Enabling `"types": "recommended"` and expecting rules to activate -- all rules are currently nursery, so nothing is enabled
2. Not anticipating the memory cost of scanning `.d.ts` files from transitive dependencies

# Common Confusions
1. **Types domain vs. TypeScript compiler** -- Biome uses its own inference engine, not `tsc`
2. **Types vs. project domain** -- Both trigger the Scanner, but the types domain additionally enables the inference engine for type resolution

# Source Reference
- linter/domains.mdx: "Types" section
- linter/index.mdx: FAQ on memory usage and TypeScript inference

# Verification Notes
- High confidence: Types domain is explicitly described in domains.mdx
- All rules verified as nursery from the source listing
