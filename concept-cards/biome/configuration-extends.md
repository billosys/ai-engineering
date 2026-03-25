---
# === CORE IDENTIFICATION ===
concept: Configuration Extends
slug: configuration-extends

# === CLASSIFICATION ===
category: configuration
subcategory: configuration sharing
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/big-projects.mdx"
chapter_number: null
pdf_page: null
section: "Other ways to share a configuration file"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "extends field"
  - "configuration inheritance"
  - "shared configuration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-configuration
extends:
  - monorepo-support
related:
  - shared-configuration-via-npm
  - configuration-file-resolution
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set up Biome in a monorepo?"
  - "How does biome.json configuration relate to CLI options?"
---

# Quick Definition
The `extends` field in `biome.json` allows a configuration to inherit settings from other configuration files or NPM packages, with later entries overriding earlier ones.

# Core Definition
The `extends` field accepts either the special `"//"` microsyntax (for root configuration inheritance in monorepos) or an array of paths to other configuration files. Paths are resolved relative to the extending configuration file's directory. Entries are processed in order, with later entries overriding earlier ones. Extended files cannot themselves extend other files (no chaining). Critically, paths referenced inside an extended configuration (such as `files.includes` globs) are resolved from the location of the file doing the extending, not from the extended file's own location.

# Prerequisites
- biome-configuration: Must understand the structure of biome.json.

# Key Properties
1. Accepts `"//"` (root config) or an array of relative/NPM paths.
2. Array entries are processed in order; later entries override earlier ones.
3. Extended files cannot extend other files (single level of inheritance only).
4. Paths inside extended configs resolve from the extending file's directory.
5. Paths starting with `.` or ending with `.json`/`.jsonc` are treated as relative paths.
6. Other paths are resolved from `node_modules/` using the Node.js resolution algorithm.

# Construction / Recognition
To use configuration extends:
1. For monorepo root inheritance: `"extends": "//"`.
2. For shared local file: `"extends": ["../common.json"]`.
3. For NPM package: `"extends": ["@org/shared-configs/biome"]`.
4. Multiple extends: `"extends": ["./base.json", "./overrides.json"]`.

# Context & Application
Used to share common configuration across multiple projects or subdirectories. Especially useful for organizations that want to maintain a single set of standards across repositories while allowing per-project overrides.

# Examples
From the source, a project with shared configuration:

```
backend/
  biome.json      # extends: ["../common.json"]
frontend/
  biome.json      # extends: ["../common.json"]
common.json
```

```json
// common.json
{
  "files": { "includes": ["src/**/*.js", "test/**/*.js"] },
  "linter": { "includes": ["**", "!test"] }
}
```

```json
// frontend/biome.json
{ "extends": ["../common.json"] }
```

When Biome runs from `frontend/`, the paths `src/**/*.js` and `test/**/*.js` from `common.json` resolve relative to `frontend/`, not relative to the root where `common.json` lives.

(From guides/big-projects.mdx, "Other ways to share a configuration file" section)

# Relationships
## Builds Upon
- biome-configuration
- monorepo-support
## Enables
- shared-configuration-via-npm
## Related
- configuration-file-resolution
## Contrasts With
None.

# Common Errors
1. Expecting extended config paths to resolve from the extended file's location -- they resolve from the extending file's location.
2. Trying to chain extends (A extends B, B extends C) -- this is not supported.
3. Using a relative path for an NPM package specifier (paths starting with `.` are always treated as file paths).

# Common Confusions
1. Confusing path resolution semantics: globs in an extended file are interpreted from the directory of the extending file.
2. Thinking `extends` deeply merges objects -- later settings override at the field level.

# Source Reference
- guides/big-projects.mdx, "Other ways to share a configuration file" section

# Verification Notes
Explicitly documented with path resolution examples. High confidence.
