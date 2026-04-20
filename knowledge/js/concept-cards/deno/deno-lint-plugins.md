---
concept: Lint Plugins
slug: deno-lint-plugins
category: toolchain
subcategory: code quality
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/lint_plugins.md"
chapter_number: null
pdf_page: null
section: "Lint Plugins"
extraction_confidence: high
aliases:
  - "Deno lint plugin"
  - "custom lint rules"
  - "Deno.lint.Plugin"
prerequisites:
  - deno-linter
  - deno-configuration
extends:
  - deno-linter
related:
  - deno-test-runner
contrasts_with: []
answers_questions:
  - "What is a lint plugin in Deno?"
  - "How do I write a lint plugin?"
  - "How do I create custom lint rules in Deno?"
---

# Quick Definition

Deno lint plugins extend the built-in linter with custom rules using an ESLint-like API, where plugins define AST visitor objects with CSS-like selectors to match nodes and report diagnostics, configured via the `lint.plugins` array in `deno.json`.

# Core Definition

The lint plugin API (experimental, requires Deno 2.2.0+) allows extending Deno's built-in linter with custom rules. The API is intentionally modeled after the ESLint plugin API, so existing ESLint knowledge is largely transferable.

A plugin is a module with a default export conforming to `Deno.lint.Plugin`. Each plugin has a `name` and a `rules` object where each rule defines a `create(context)` method that returns an AST visitor object. The visitor's property names can be AST node types (e.g., `Identifier`) or CSS-like selectors (e.g., `'CallExpression[callee.name="require"]'`).

Plugins are loaded via the `lint.plugins` setting in `deno.json`:
```json
{
  "lint": {
    "plugins": ["./my-plugin.ts"]
  }
}
```

Plugin specifiers can be local paths, `npm:`, or `jsr:` specifiers.

# Prerequisites

- `deno-linter` — the plugin system extends the built-in linter
- `deno-configuration` — plugins are configured in `deno.json`

# Key Properties

1. **ESLint-compatible API**: The `create(context)` / visitor pattern mirrors ESLint, enabling knowledge reuse.
2. **CSS-like selectors**: Visitor keys support selectors like `'CallExpression[callee.name="require"]'`, descendant combinators, pseudo-classes (`:first-child`, `:not()`, `:has()`), and field selectors.
3. **Auto-fixable**: Rules can provide `fix(fixer)` functions with methods like `replaceText`, `insertTextBefore`, `remove`, etc., applied via `deno lint --fix`.
4. **Testable**: `Deno.lint.runPlugin()` API allows testing plugins in `deno test` by asserting on diagnostics produced for given input.
5. **Cleanup hooks**: `destroy()` method runs after a file is linted for resource cleanup.
6. **Excludable**: Custom rules can be disabled via `lint.rules.exclude` using the format `<plugin-name>/<rule-name>`.
7. **Ignorable inline**: `// deno-lint-ignore <plugin>/<rule>` suppresses specific reports.

# Construction / Recognition

A complete plugin example:

```ts
const plugin: Deno.lint.Plugin = {
  name: "my-plugin",
  rules: {
    "my-rule": {
      create(context) {
        return {
          Identifier(node) {
            if (node.name === "_a") {
              context.report({
                node,
                message: "should be _b",
                fix(fixer) {
                  return fixer.replaceText(node, "_b");
                },
              });
            }
          },
        };
      },
    },
  },
};
export default plugin;
```

Selector-based matching:

```ts
return {
  'CallExpression[callee.name="require"]'(node) {
    context.report({
      node,
      message: "Don't use require() calls to load modules",
    });
  },
};
```

# Context & Application

Lint plugins fill the gap between Deno's built-in rules and project-specific needs. They are useful for enforcing company-wide conventions, catching context-specific problems, or porting existing ESLint rules. The selector system reduces boilerplate compared to manual AST traversal.

# Examples

**Testing a plugin** (from `runtime/reference/lint_plugins.md`):
```ts
Deno.test("my-plugin", () => {
  const diagnostics = Deno.lint.runPlugin(
    myPlugin,
    "main.ts",
    "const _a = 'a';",
  );
  assertEquals(diagnostics.length, 1);
  assertEquals(diagnostics[0].id, "my-plugin/my-rule");
  assertEquals(diagnostics[0].message, "should be _b");
});
```

**Supported selectors** include: `Foo + Foo` (sibling), `Foo > Bar` (child), `Foo[attr]` (attribute), `Foo[attr.length < 2]` (comparison), `:first-child`, `:nth-child(2n+1)`, `:not()`, `:has()`, `:exit` (upward traversal), and `IfStatement.test` (field).

# Relationships

- **Extends**: `deno-linter` — adds custom rules to the built-in linter
- **Related**: `deno-test-runner` — `Deno.lint.runPlugin` is only available in `deno test`

# Common Errors

1. **Keeping global state**: Plugin instances may be reused across files. Avoid global state; use the `destroy()` hook for cleanup.
2. **Forgetting `export default`**: The plugin must be the default export of the module.
3. **Missing `--unstable` flag**: The plugin API is experimental and currently marked unstable.

# Common Confusions

- **Plugin rules vs built-in rules**: Custom rule names are prefixed with the plugin name (`my-plugin/my-rule`), unlike built-in rules which have no prefix.
- **`Deno.lint.runPlugin` scope**: This testing API only works inside `deno test` and `deno bench`; it throws in other subcommands.

# Source Reference

Source: "Deno Documentation", file `runtime/reference/lint_plugins.md`, all sections.

# Verification Notes

All API details, selector syntax, and testing patterns are explicitly documented in the source file. Extraction confidence is high.
