---
# === CORE IDENTIFICATION ===
concept: JSR Registry
slug: jsr-registry

# === CLASSIFICATION ===
category: modules
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/modules.md"
chapter_number: null
pdf_page: null
section: "Importing third party modules and libraries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - JSR
  - "JavaScript Registry"
  - "jsr: specifier"
  - "jsr.io"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ecmascript-modules
extends: []
related:
  - deno
  - deno-import-maps
contrasts_with:
  - deno-npm-specifiers

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes jsr: from npm: specifiers?"
  - "What is Deno's recommended package registry?"
---

# Quick Definition
JSR (JavaScript Registry) is the modern JavaScript registry at jsr.io, accessed via `jsr:` specifiers, that Deno recommends for third-party modules -- it supports TypeScript natively and auto-generates documentation.

# Core Definition
JSR (the JavaScript Registry, hosted at jsr.io) is the package registry that Deno recommends for publishing and consuming third-party modules. Packages are imported using the `jsr:` specifier prefix with the format `jsr:@<scope>/<package>@<version>`. JSR supports TypeScript natively (packages can be published as TypeScript source) and auto-generates documentation. The Deno Standard Library (`@std`) is hosted on JSR.

JSR packages can also be consumed from `package.json` using the `jsr:` scheme in the version field, making them accessible to projects using traditional Node.js dependency management.

# Prerequisites
- ecmascript-modules: Understanding of ESM import syntax

# Key Properties
1. **jsr: specifier** -- Import format: `jsr:@scope/package@version`
2. **Native TypeScript** -- Packages can be published as TypeScript; no compilation to JS required
3. **Auto-generated docs** -- Documentation is generated automatically from published code
4. **Deno Standard Library** -- The `@std` scope on JSR hosts Deno's standard library
5. **deno add support** -- `deno add jsr:@scope/package` adds the dependency to `deno.json`
6. **Semver versioning** -- Supports full semver range specifiers
7. **package.json compatible** -- Can be used from `package.json` dependencies with `"jsr:^version"` syntax

# Construction / Recognition
```ts
// Direct import with version
import { camelCase } from "jsr:@luca/cases@1.0.0";

// Via import map in deno.json
// { "imports": { "@luca/cases": "jsr:@luca/cases@^1.0.0" } }
import { camelCase } from "@luca/cases";
```

```sh
# Add JSR package
deno add jsr:@luca/cases
```

```json
// In package.json
{
  "dependencies": {
    "@std/path": "jsr:^1.0.9"
  }
}
```

# Context & Application
JSR is Deno's answer to the npm registry, designed from the ground up for modern JavaScript and TypeScript development. While npm remains the largest package ecosystem and is fully supported via `npm:` specifiers, JSR offers advantages for Deno-first development: native TypeScript support eliminates the need for a build step before publishing, and auto-generated documentation improves discoverability. The Deno Standard Library being hosted on JSR makes it the natural first choice for Deno projects.

JSR packages can be published using `deno publish` and consumed from any JavaScript runtime that supports the `jsr:` protocol.

# Examples
From runtime/fundamentals/modules.md:
- Import: `import { camelCase } from "jsr:@luca/cases@1.0.0";`
- Deno recommends JSR: "Deno recommends JSR, the modern JavaScript registry, for third party modules. There, you'll find plenty of well documented ES modules for your projects, including the Deno Standard Library."
- Standard library reference: `https://jsr.io/@std`
- From package.json: `{ "dependencies": { "@std/path": "jsr:^1.0.9" } }`

# Relationships
## Builds Upon
- ecmascript-modules (JSR packages are ESM)

## Related
- deno (JSR is the recommended registry for Deno)
- deno-import-maps (JSR packages are commonly mapped via import maps)

## Contrasts With
- deno-npm-specifiers / npm registry (`npm:` imports from npm; `jsr:` imports from JSR. JSR supports native TypeScript; npm generally requires compiled JS)

# Common Errors
1. Confusing `jsr:` and `npm:` specifiers -- they point to different registries
2. Not using `deno add` -- manually typing full specifiers is error-prone; `deno add` manages version resolution

# Common Confusions
1. **JSR vs. npm** -- JSR is a separate registry from npm; `jsr:` and `npm:` are not interchangeable. JSR supports TypeScript natively; npm packages typically require a build step
2. **JSR vs. deno.land/x** -- deno.land/x is the older HTTPS-based module hosting; JSR is the modern replacement with better tooling and discoverability

# Source Reference
- runtime/fundamentals/modules.md, section "Importing third party modules and libraries": JSR recommendation and import syntax
- runtime/contributing/architecture.md: Standard library hosted at jsr.io/@std

# Verification Notes
- High confidence: JSR is explicitly recommended and demonstrated in the module documentation
- Standard library hosting on JSR confirmed in both modules and architecture docs
