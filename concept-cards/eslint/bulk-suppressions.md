---
# === CORE IDENTIFICATION ===
concept: Bulk Suppressions
slug: bulk-suppressions

# === CLASSIFICATION ===
category: suppression
subcategory: project-wide suppression
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/suppressions.md"
chapter_number: null
pdf_page: null
section: "Bulk Suppressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - eslint suppressions
  - suppress-all
  - eslint-suppressions.json
  - prune-suppressions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rule-configuration
extends: []
related:
  - disable-directives
contrasts_with:
  - disable-directives

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I enable a new ESLint rule without fixing all existing violations?"
  - "What is eslint-suppressions.json?"
  - "How do I gradually adopt strict ESLint rules in a large codebase?"
  - "How do I remove suppressions after fixing violations?"
---

# Quick Definition
Bulk suppressions allow enabling new ESLint rules as `"error"` while automatically suppressing all existing violations, tracked in an `eslint-suppressions.json` file that can be gradually pruned as violations are fixed.

# Core Definition
Bulk suppressions solve the problem of adopting new lint rules in large codebases. When a rule is enabled as `"error"`, the `--suppress-all` CLI flag generates an `eslint-suppressions.json` file that records all existing violations, preventing them from being reported. New code is still held to the rule. As violations are fixed, `--prune-suppressions` removes resolved entries from the file. Only rules configured as `"error"` are suppressed (not `"warn"`). The suppressions file should be committed to version control.

# Prerequisites
- rule-configuration (rules must be configured as "error" for suppression)

# Key Properties
1. `--suppress-all`: suppress all existing violations of all error-level rules
2. `--suppress-rule <name>`: suppress violations of a specific rule
3. Multiple rules: `--suppress-rule rule1 --suppress-rule rule2`
4. `eslint-suppressions.json`: generated file tracking suppressed violations (commit to VCS)
5. `--prune-suppressions`: remove entries for violations that no longer exist
6. `--suppressions-location <path>`: custom location for the suppressions file
7. `--pass-on-unpruned-suppressions`: ignore unused suppressions in exit code
8. Recommended to use with `--fix` to avoid suppressing auto-fixable violations
9. ESLint exits with error when suppressions exist for resolved violations (prompts pruning)
10. Node.js API: `applySuppressions: true` in ESLint constructor; `suppressionsLocation` for custom path

# Construction / Recognition
Initial suppression workflow:
```bash
# Enable rule in config, then suppress existing violations
eslint --fix --suppress-all

# After fixing some violations, prune resolved suppressions
eslint --prune-suppressions
```

Suppress a specific rule:
```bash
eslint --fix --suppress-rule no-unused-expressions
```

Custom suppressions file location:
```bash
eslint --suppressions-location .github/.eslint-suppressions
```

Node.js API usage:
```js
const eslint = new ESLint({
  applySuppressions: true,
  suppressionsLocation: "./config/my-suppressions.json",
});
```

# Context & Application
Bulk suppressions are designed for teams adopting stricter rules incrementally. The workflow is: (1) enable the rule as `"error"` in config, (2) run with `--fix --suppress-all` to auto-fix what's possible and suppress the rest, (3) commit the suppressions file, (4) fix violations over time, (5) run `--prune-suppressions` periodically. This prevents new violations while allowing gradual cleanup.

# Examples
From `use/suppressions.md`: When using `lintText()` via the Node.js API, `filePath` must be provided for suppressions to work since suppressions are matched by file path.

The Node.js API only supports applying existing suppressions. Creating new suppressions (`--suppress-all`, `--suppress-rule`) and pruning (`--prune-suppressions`) are CLI-only operations.

# Relationships
## Builds Upon
- rule-configuration (only "error"-level rules can be suppressed)

## Enables
- Incremental adoption of strict lint rules in large codebases
- Zero-violation CI enforcement for new code while allowing legacy exceptions

## Related
- disable-directives (per-location suppression, complementary approach)

## Contrasts With
- disable-directives: Disable directives are manual, per-location comments in source code. Bulk suppressions are automated, project-wide, tracked in a separate JSON file, and designed for gradual cleanup.

# Common Errors
1. Not using `--fix` with `--suppress-all`, resulting in suppressing auto-fixable violations
2. Forgetting to commit `eslint-suppressions.json` to version control
3. Not providing `--suppressions-location` consistently between suppression and lint runs
4. Using with `"warn"`-level rules (only `"error"` rules are suppressed)

# Common Confusions
1. Thinking suppressions apply to warnings -- they only apply to errors
2. Not realizing that ESLint will error when suppressions exist for resolved violations (need to prune)
3. Assuming the Node.js API can create suppressions (it can only apply existing ones)

# Source Reference
- `sources-md/eslint/use/suppressions.md`, all sections

# Verification Notes
Extracted from the bulk suppressions documentation. CLI flags, workflow, and API limitations verified against source.
