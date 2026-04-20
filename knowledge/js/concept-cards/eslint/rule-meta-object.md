---
# === CORE IDENTIFICATION ===
concept: Rule Meta Object
slug: rule-meta-object

# === CLASSIFICATION ===
category: extending
subcategory: custom rule internals
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/custom-rules.md"
chapter_number: null
pdf_page: null
section: "Rule Structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rule metadata"
  - "meta property"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - custom-rules
extends:
  - custom-rules
related:
  - rule-context-object
  - creating-plugins
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What metadata does an ESLint rule need?"
  - "What is the difference between problem, suggestion, and layout rule types?"
  - "How do you declare a rule as fixable?"
  - "What is the messages object used for?"
---

# Quick Definition
The `meta` object is the metadata section of an ESLint rule that declares its type, documentation, fixability, option schema, messages, and other properties that ESLint and tooling use to manage the rule.

# Core Definition
Every ESLint rule exports an object with a `meta` property. This object communicates to ESLint how the rule behaves and what capabilities it has. The `meta` object contains the following properties:

- **type** (`string`): One of `"problem"`, `"suggestion"`, or `"layout"`, indicating the rule's purpose. Used with `--fix-type` CLI option.
- **docs** (`object`): Properties for documentation, including `description` (string), `recommended` (boolean for core rules), and `url` (link to full documentation).
- **messages** (`object`): Key-value pairs mapping `messageId` strings to message templates with `{{ placeholder }}` syntax. Required for core rules.
- **fixable** (`string`): Either `"code"` or `"whitespace"`. Mandatory if the rule implements a `fix` function.
- **hasSuggestions** (`boolean`): Must be `true` if the rule provides suggestions. ESLint throws if a rule produces suggestions without this property.
- **schema** (`object | array | false`): JSON Schema for validating rule options. Mandatory when the rule has options.
- **defaultOptions** (`array`): Default options merged recursively with user-provided options.
- **deprecated** (`boolean | DeprecatedInfo`): Indicates whether the rule is deprecated.

# Prerequisites
- Understanding of custom rules structure

# Key Properties
1. **type** -- Classifies the rule's purpose: `"problem"` (likely error), `"suggestion"` (improvement), `"layout"` (formatting)
2. **fixable** -- Mandatory for fixable rules; without it, ESLint throws when a fix is attempted
3. **hasSuggestions** -- Mandatory for rules providing suggestions
4. **messages** -- Central repository for violation messages, referenced by `messageId` in `context.report()`
5. **schema** -- Validates rule configuration options against JSON Schema
6. **defaultOptions** -- Provides fallback values when users do not specify all options

# Construction / Recognition
```js
meta: {
    type: "problem",
    docs: {
        description: "Enforce that const foo equals 'bar'.",
    },
    fixable: "code",
    hasSuggestions: false,
    schema: [],
    messages: {
        avoidName: "Avoid using variables named '{{ name }}'"
    }
}
```

# Context & Application
The meta object is read by ESLint core, editor integrations, documentation generators, and the `--fix-type` CLI filter. Messages defined here enable `messageId`-based reporting, which reduces duplication between rule files and test files and lowers the barrier for improving messages.

# Examples
From extend/custom-rules.md:
- `"problem"`: "The rule is identifying code that either will cause an error or may cause a confusing behavior."
- `"suggestion"`: "The rule is identifying something that could be done in a better way but no errors will occur if the code isn't changed."
- `"layout"`: "The rule cares primarily about whitespace, semicolons, commas, and parentheses."

# Relationships
## Part Of
- custom-rules

## Related
- rule-context-object

# Common Errors
1. Omitting `fixable` on a rule that provides fixes -- causes an ESLint runtime error
2. Omitting `hasSuggestions` on a rule that provides suggestions -- causes an ESLint runtime error
3. Forgetting `schema` when the rule accepts options -- ESLint cannot validate user config

# Source Reference
- extend/custom-rules.md: Rule Structure section detailing all meta properties

# Verification Notes
- High confidence: all properties enumerated directly from the documentation
