---
# === CORE IDENTIFICATION ===
concept: Clippy Lint Naming
slug: clippy-lint-naming

# === CLASSIFICATION ===
category: lint-development
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "03-lint-basics"
chapter_number: 3
pdf_page: null
section: "Lint name"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "lint naming conventions"
  - "lint naming guidelines"
  - "Clippy lint name rules"
  - "naming a lint"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
extends: []
related:
  - adding-a-lint
  - lint-declaration
  - clippy-lint-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I name a new Clippy lint?"
  - "What are the lint naming conventions?"
  - "What makes a good lint name?"
  - "How does a lint name relate to allow/warn/deny usage?"
---

# Quick Definition

Clippy lint names follow snake_case convention and must describe the thing being checked for, reading naturally when used with `allow`/`warn`/`deny` attributes. The name should state what the code pattern is, not what should be done instead. Names are validated during the PR review process.

# Core Definition

The source emphasizes naming as an important early decision: "A good lint name is important, make sure to check the lint naming guidelines." The chapter references RFC 0344 ("Conventions Galore") for the authoritative naming rules.

Key principles from the source:

1. **Snake_case**: Lint names use snake_case (e.g., `foo_functions`, not `FooFunctions` or `fooFunctions`)
2. **State the checked thing**: "The name should state the thing that is being checked for"
3. **Read well with attributes**: The name should "read well when used with `allow`/`warn`/`deny`"
4. **ALL_CAPS constant**: In code, the lint name is an ALL_CAPS constant (e.g., `FOO_FUNCTIONS`), but users reference it in snake_case with the `clippy::` prefix (e.g., `clippy::foo_functions`)

The source illustrates with the `foo_functions` example: this name describes what is being detected (functions named `foo`), and `#[allow(clippy::foo_functions)]` reads naturally as "allow functions named foo."

The PR process includes a review of the lint name. The source reassures: "Don't worry, if the lint name doesn't fit, a Clippy team member will alert you in the PR process."

# Prerequisites

- **clippy** -- Understanding Clippy and its lint system is needed to name lints appropriately.

# Key Properties

1. Lint names use snake_case (e.g., `foo_functions`, `manual_strip`, `range_plus_one`)
2. The name should describe the pattern being detected, not the fix
3. The name should read naturally when prefixed with `clippy::` in `allow`/`warn`/`deny`
4. In declaration code, the name is ALL_CAPS (e.g., `FOO_FUNCTIONS`)
5. Users reference the name as `clippy::foo_functions` in attributes and CLI flags
6. The name is reviewed during the PR process -- Clippy team members will suggest changes if needed
7. The authoritative reference is RFC 0344 (Conventions Galore, lints section)
8. `cargo dev new_lint --name=<name>` takes the name in snake_case

# Construction / Recognition

## To Choose a Good Lint Name:
1. Identify the code pattern the lint detects (e.g., "functions named foo")
2. Describe that pattern in snake_case (e.g., `foo_functions`)
3. Test readability: does `#[allow(clippy::your_name)]` make sense?
4. Test readability: does `#[deny(clippy::your_name)]` make sense?
5. Avoid describing the fix -- describe the problem
6. Check existing lints for naming patterns in similar categories
7. Consult RFC 0344 lint naming guidelines if uncertain

## To Recognize the Name Convention in Existing Lints:
1. Look for patterns like `needless_return` (describes the problem: a return that is needless)
2. Look for patterns like `manual_strip` (describes the problem: manual implementation of strip)
3. Look for patterns like `range_plus_one` (describes the code pattern: range plus one)
4. Avoid patterns like `use_inclusive_range` (describes the fix, not the problem)

## Naming Patterns by Category:
- **Correctness/suspicious**: Name the bug or suspicious pattern (e.g., `drop_forget_ref`)
- **Style**: Name the style violation (e.g., `needless_return`)
- **Complexity**: Name the unnecessarily complex pattern (e.g., `manual_strip`)
- **Pedantic**: Name the imprecise or non-idiomatic pattern (e.g., `range_plus_one`)
- **Restriction**: Name the restricted construct (e.g., `implicit_return`)

# Context & Application

Lint naming matters because users interact with lint names constantly -- in `#[allow(...)]` attributes, in `clippy.toml` configuration, in CLI flags, and in lint list documentation. A well-named lint is self-documenting: seeing `clippy::foo_functions` in an `allow` attribute immediately communicates what is being suppressed.

**Conflicting lints** illustrate naming well. The source discusses lints that oppose each other (e.g., `implicit_return` in restriction vs. `needless_return` in style). Both names describe what they detect, not what they want you to do. This is essential because opposing lints cannot both say "use X" -- they must each name the pattern they flag.

The source also notes that conflicting lints should generally be in different categories (with at least one in `restriction`) unless both are in `restriction` (e.g., `semicolon_inside_block` and `semicolon_outside_block`).

# Examples

**Example 1**: Good lint name -- `foo_functions`:
- Describes: functions named `foo`
- Usage: `#[allow(clippy::foo_functions)]` -- "allow functions named foo"
- In code: `pub FOO_FUNCTIONS`

**Example 2**: Good naming pattern for conflicting lints:
- `implicit_return` (restriction, allow) -- names the pattern: implicit returns
- `needless_return` (style, warn) -- names the pattern: needless explicit returns
- Both describe what they detect, not what to do

**Example 3**: Scaffolding with the name:
```bash
cargo dev new_lint --name=foo_functions --pass=early --category=pedantic
```
The `--name` flag accepts the snake_case lint name.

# Relationships

## Builds Upon
- **clippy** -- Naming conventions are specific to the Clippy project

## Enables
- **lint-declaration** -- The chosen name becomes the ALL_CAPS constant in `declare_clippy_lint!`
- **adding-a-lint** -- Naming is the first decision when creating a new lint

## Related
- **clippy-lint-groups** -- The category choice (which affects the user-visible group) should complement the name
- **clippy-lint-levels** -- The name must read naturally with `allow`/`warn`/`deny`

# Common Errors

- **Error**: Naming the lint after the fix instead of the problem (e.g., `use_inclusive_range` instead of `range_plus_one`).
  **Correction**: Describe the detected pattern, not the suggested alternative. The fix goes in the lint documentation and help message.

- **Error**: Using camelCase or PascalCase for the lint name.
  **Correction**: Lint names use snake_case. The ALL_CAPS version is only for the constant in code.

- **Error**: Choosing an overly generic name (e.g., `bad_code` or `style_issue`).
  **Correction**: Be specific about the pattern. The name should identify what makes the code worth linting.

# Common Confusions

- **Confusion**: Thinking the ALL_CAPS constant name and the user-facing name are different things.
  **Clarification**: They are the same name in different cases. `FOO_FUNCTIONS` in code becomes `clippy::foo_functions` for users. The conversion is automatic.

- **Confusion**: Believing a lint name cannot be changed after submission.
  **Clarification**: Lint names can be changed during PR review. The source says a "Clippy team member will alert you" if the name does not fit. Name changes are handled through deprecation of the old name.

- **Confusion**: Wondering whether the `clippy::` prefix is part of the lint name.
  **Clarification**: The `clippy::` prefix is the namespace, not part of the name. In declarations and registration, only the bare name is used (`FOO_FUNCTIONS`). The prefix is added automatically for user-facing contexts.

# Source Reference

Chapter 3: Lint Basics, sections "Getting Started" (where `foo_functions` naming is discussed), "Lint name" (in the "Define New Lints" chapter), "Lint declaration" (where naming rules are stated), and "Conflicting lints" (where opposing lint names are discussed). The authoritative reference is RFC 0344.

# Verification Notes

- Snake_case: Demonstrated throughout with `foo_functions` example
- "State the thing being checked for": Directly quoted from the "Lint declaration" section
- "Read well when used with allow/warn/deny": Directly quoted from the "Lint declaration" section
- PR review: Source states "a Clippy team member will alert you in the PR process"
- RFC reference: Source links to RFC 0344 for lint naming guidelines
- Conflicting lints examples: `implicit_return`/`needless_return` and `semicolon_inside_block`/`semicolon_outside_block` from source
- Confidence: MEDIUM -- the source references external RFC 0344 for detailed rules rather than listing them inline; the chapter provides principles and examples but defers to the RFC for comprehensive guidelines
- Cross-references: All slugs verified against planned extractions across agents
