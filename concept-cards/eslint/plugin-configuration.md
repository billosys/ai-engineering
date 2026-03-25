---
# === CORE IDENTIFICATION ===
concept: Plugin Configuration
slug: plugin-configuration

# === CLASSIFICATION ===
category: configuration
subcategory: plugins
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/plugins.md"
chapter_number: null
pdf_page: null
section: "Configure Plugins"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - configuring plugins
  - eslint plugins
  - plugin setup

# === TYPED RELATIONSHIPS ===
prerequisites:
  - configuration-objects
  - rule-configuration
extends: []
related:
  - combining-configurations
  - language-options
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add a plugin to ESLint flat config?"
  - "How do I use plugin rules, processors, and configurations?"
  - "What is a virtual plugin in ESLint?"
  - "How do I use a local (unpublished) plugin?"
---

# Quick Definition
Plugin configuration in ESLint flat config uses the `plugins` property to map namespace names to plugin objects, enabling the use of plugin-provided rules, processors, configurations, and languages.

# Core Definition
Plugins in ESLint's flat config are objects conforming to a specific interface, registered via the `plugins` property. The key is the namespace (conventionally the npm name without `eslint-plugin-`), and the value is the imported plugin object. Plugin rules are referenced as `namespace/rule-name` in the `rules` property. Plugins can also export predefined configurations (used via `extends`), processors (used via `processor`), and languages (used via `language`). Plugins can be npm packages, local files, or virtual (inline) definitions.

# Prerequisites
- configuration-objects (plugins are a property of config objects)
- rule-configuration (plugin rules are configured the same way)

# Key Properties
1. Namespace convention: npm package name without `eslint-plugin-` prefix (e.g., `eslint-plugin-jsdoc` becomes `jsdoc`)
2. Plugin rules referenced as `namespace/rule-name` in `rules` property
3. Plugin configurations used via `extends: ["namespace/configName"]`
4. Processors specified as `processor: "namespace/processorName"`
5. Languages specified as `language: "namespace/languageName"`
6. Local plugins loaded from files: `import local from "./my-plugin.js"`
7. Virtual plugins defined inline with a `rules` object containing rule implementations
8. Custom namespaces allowed -- not required to match plugin's prescribed name

# Construction / Recognition
Standard plugin usage:
```js
import jsdoc from "eslint-plugin-jsdoc";
import { defineConfig } from "eslint/config";

export default defineConfig([{
  files: ["**/*.js"],
  plugins: { jsdoc },
  rules: {
    "jsdoc/require-description": "error",
  },
}]);
```

Virtual plugin:
```js
import myRule from "./rules/my-rule.js";

export default defineConfig([{
  plugins: {
    local: { rules: { "my-rule": myRule } },
  },
  rules: { "local/my-rule": "warn" },
}]);
```

Using a plugin's predefined config:
```js
import examplePlugin from "eslint-plugin-example";

export default defineConfig([{
  files: ["**/*.js"],
  plugins: { example: examplePlugin },
  extends: ["example/recommended"],
}]);
```

Using a processor:
```js
import markdown from "@eslint/markdown";

export default defineConfig([{
  files: ["**/*.md"],
  plugins: { markdown },
  processor: "markdown/markdown",
}]);
```

# Context & Application
Plugin configuration is how ESLint gains capabilities beyond its built-in rules: TypeScript linting (`@typescript-eslint`), React-specific rules (`eslint-plugin-react`), JSON/Markdown linting, and custom project rules. The flat config format treats plugins as first-class JavaScript objects rather than resolved strings.

# Examples
From `use/configure/plugins.md`: Processors can create named code blocks (e.g., `0.js` inside Markdown). Additional config objects with patterns like `**/*.md/*.js` can target these code blocks specifically.

From `use/configure/plugins.md`: The `language` key enables non-JavaScript linting. For example, `@eslint/json` with `language: "json/jsonc"` enables JSON linting.

# Relationships
## Builds Upon
- configuration-objects (plugins property)
- rule-configuration (plugin rules configured the same way)

## Enables
- Extended linting for TypeScript, React, JSON, Markdown, etc.
- Custom rule integration without publishing to npm

## Related
- combining-configurations (plugin configs used via extends)
- language-options (languageOptions become language-specific when a plugin language is set)

# Common Errors
1. Forgetting to add the plugin to `plugins` before referencing its rules
2. Using wrong namespace prefix in rule names
3. Expecting configuration comments to load plugins (they cannot)

# Common Confusions
1. Thinking plugins must be npm packages -- local and virtual plugins work too
2. Confusing `plugins` (registering the plugin) with `extends` (applying the plugin's predefined config)

# Source Reference
- `sources-md/eslint/use/configure/plugins.md`, all sections

# Verification Notes
Extracted from the plugins configuration documentation. Virtual plugins, local plugins, processors, and languages all verified against source.
