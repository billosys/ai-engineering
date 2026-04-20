---
# === CORE IDENTIFICATION ===
concept: Rule Context Object
slug: rule-context-object

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
section: "The Context Object"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "context object"
  - "rule context"
  - "context.report()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - custom-rules
extends:
  - custom-rules
related:
  - rule-meta-object
  - scope-manager
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What information does the context object provide to a rule?"
  - "How does context.report() work?"
  - "How does a rule access the source code and options?"
  - "How do you apply automatic fixes or provide suggestions?"
---

# Quick Definition
The `context` object is the sole argument to a rule's `create` function, providing access to the source code, rule options, language settings, and the `report()` method for flagging problems.

# Core Definition
The context object provides the runtime environment for a rule. Its properties include:

- **id** (`string`): The rule ID.
- **filename** / **physicalFilename** (`string`): The file being linted.
- **cwd** (`string`): Current working directory.
- **options** (`array`): Configured options for this rule (excluding severity level).
- **sourceCode** (`object`): A `SourceCode` object for accessing tokens, comments, scopes, and AST information.
- **settings** (`object`): Shared settings from the configuration.
- **languageOptions** (`object`): Includes `sourceType`, `ecmaVersion`, `parser`, `parserOptions`, and `globals`.

The primary method is `context.report(descriptor)`, which publishes a warning or error. The descriptor object accepts: `node` or `loc` (at least one required), `message` or `messageId`, optional `data` for placeholders, an optional `fix(fixer)` function for automatic fixes, and an optional `suggest` array for manual suggestions.

# Prerequisites
- Understanding of custom rule structure and the meta object

# Key Properties
1. **context.report()** -- Primary method for reporting problems; accepts node, message/messageId, data, fix, and suggest
2. **context.sourceCode** -- Access to SourceCode with methods like getText(), getTokens(), getScope(), getAncestors()
3. **context.options** -- Array of user-configured rule options
4. **Fixer methods** -- insertTextAfter, insertTextBefore, remove, removeRange, replaceText, replaceTextRange
5. **Suggestions** -- Array of objects with `desc`/`messageId` and a `fix` function for editor-assisted fixes

# Construction / Recognition
```js
create(context) {
    return {
        Identifier(node) {
            if (node.name === "foo") {
                context.report({
                    node,
                    messageId: "avoidName",
                    data: { name: "foo" },
                    fix(fixer) {
                        return fixer.replaceText(node, "bar");
                    }
                });
            }
        }
    };
}
```

# Context & Application
The context object is the primary API surface for rule authors. The `sourceCode` property provides rich AST querying capabilities including token navigation, scope analysis via `getScope(node)`, variable tracking via `getDeclaredVariables(node)`, and ancestor traversal. The fixer API enables automatic code corrections that are applied iteratively (up to 10 rounds).

# Examples
From extend/custom-rules.md:
- `context.report({ node, message: "Unexpected identifier" })` -- simplest form
- `context.report({ node, messageId: "avoidName", data: { name: "foo" } })` -- with messageId and placeholders
- Fixer methods: `fixer.insertTextAfter(node, ";")`, `fixer.replaceText(node, '"bar"')`, `fixer.removeRange(range)`

# Relationships
## Part Of
- custom-rules

## Uses
- scope-manager (via `context.sourceCode.getScope()`)

## Related
- rule-meta-object

# Common Errors
1. Returning multiple independent fixes from a single `fix()` -- the fixer objects must not have overlapping ranges
2. Trying to access `context.options` without defining a schema in meta -- ESLint cannot validate the options
3. Making fixes that change runtime behavior -- fixes should preserve functionality

# Common Confusions
1. **fix vs. suggest** -- `fix` is applied automatically with `--fix`; `suggest` is presented to users in editors for manual application

# Source Reference
- extend/custom-rules.md: "The Context Object" section, "Report Problems" section, "Applying Fixes" section, "Providing Suggestions" section

# Verification Notes
- High confidence: all properties and methods enumerated directly from the documentation
