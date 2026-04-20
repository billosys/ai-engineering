# Deno Publishing

Everything you need to publish a Deno package to JSR: package metadata, the `exports` map, `deno publish`, JSR requirements for plain JS, versioning, documentation, the pre-publish checklist, and workspace publishing. This is the capstone of the Deno series — it ties together runtime basics (12-01), testing (12-02), task runner (12-03), API design (02), project structure (10), and documentation (11). Grounded in Deno documentation concept cards.

Target environment: **Deno**, **JSR** (not npm), **ESM-only**, **no TypeScript** (plain JS with JSDoc where needed).

---

## ID-01: `name` Field — Scoped Package Identifier

**Strength**: MUST

**Summary**: Every publishable package requires a scoped `name` in `@scope/package` format.

```jsonc
// deno.json (workspace member or standalone package)
{
  "name": "@myorg/http-utils",
  "version": "0.1.0",
  "exports": "./mod.js"
}
```

**Rules**:
- Format: `@scope/package-name` — always scoped
- Create your scope on [jsr.io](https://jsr.io) before publishing
- In a workspace, `name` goes in the **member** `deno.json`, not the root

**Rationale**: JSR uses scoped packages exclusively — there are no unscoped packages. The scope is your organization or username. All `@std/*` packages follow this pattern (JSR registry docs).

---

## ID-02: `version` Field — Semantic Versioning

**Strength**: MUST

**Summary**: Every publishable package requires a semver `version` string.

```jsonc
{
  "name": "@myorg/http-utils",
  "version": "1.2.3",
  "exports": "./mod.js"
}
```

**Semver contract**:
- **Major** (`2.0.0`): Breaking changes to the public API
- **Minor** (`1.3.0`): New features, backwards-compatible
- **Patch** (`1.2.4`): Bug fixes, backwards-compatible
- **`0.x.y`**: Unstable — breaking changes allowed at minor bumps (see ID-14)
- **Pre-release**: `1.0.0-alpha.1`, `1.0.0-rc.1` for pre-release versions

Consumers depend on semver ranges (`^1.0.0`). Breaking the semver contract causes unexpected breakage for downstream users. The `@std` standard library tracks stability per-package — `1.0.0+` packages are stable; `0.x` packages are experimental.

**Rationale**: Once published, a version is **immutable** — it cannot be changed, replaced, or deleted. If you publish a mistake, you must bump the version and publish again. Use `--dry-run` (ID-08) to catch issues before committing to a version number (JSR registry docs; Deno standard library docs).

---

## ID-03: `exports` Field — The Public API Map

**Strength**: MUST

**Summary**: The `exports` field declares which files consumers can import. Paths not in `exports` are private.

```jsonc
// Single export (shorthand) — one entry point
{
  "name": "@myorg/parser",
  "version": "1.0.0",
  "exports": "./mod.js"
}
// Consumer: import { parse } from "@myorg/parser"

// Multiple exports (object form) — multiple entry points
{
  "name": "@myorg/toolkit",
  "version": "1.0.0",
  "exports": {
    ".": "./mod.js",
    "./http": "./http/mod.js",
    "./crypto": "./crypto/mod.js",
    "./testing": "./testing/mod.js"
  }
}
// Consumer: import { serve } from "@myorg/toolkit/http"
// Consumer: import { hash } from "@myorg/toolkit/crypto"
```

**Rationale**: The `exports` map is the most important field for publishing. It is the mechanism that enforces the public API boundary — consumers can **only** import paths that appear as keys in `exports`. Files not in `exports` are private to the package, even though they exist on JSR. This is the runtime-enforced version of the barrel-file convention (JSR registry docs; Exploring JS Ch. 29).

**See also**: `02-api-design.md` ID-08, `10-project-structure.md` ID-09

---

## ID-04: `exports` Enforces the Public API Boundary

**Strength**: SHOULD

**Summary**: Internal modules not listed in `exports` cannot be imported by consumers. Use this to separate public from internal code.

```
my-package/
├── deno.json            # exports: { ".": "./mod.js", "./http": "./http/mod.js" }
├── mod.js               # public: re-exports from internal modules
├── http/
│   ├── mod.js           # public: listed in exports as "./http"
│   ├── server.js        # PRIVATE: not in exports, consumers cannot import
│   └── router.js        # PRIVATE: not in exports
└── internal/
    ├── cache.js          # PRIVATE: entire directory is private
    └── utils.js          # PRIVATE
```

```js
// Consumer code:
import { serve } from "@myorg/toolkit/http";       // ✓ listed in exports
import { router } from "@myorg/toolkit/http/router.js"; // ✗ NOT in exports — error
import { cache } from "@myorg/toolkit/internal/cache.js"; // ✗ NOT in exports — error
```

**Rationale**: `exports` is the contractual boundary between package author and consumer. Internal files can be renamed, reorganized, or deleted without breaking consumers — as long as the `exports` map stays stable. This is stronger than the barrel-file convention (which is organizational) because it is enforced by the module resolver (JSR registry docs).

---

## ID-05: Subpath Exports for Multi-Entrypoint Packages

**Strength**: SHOULD

**Summary**: Use subpath exports when a package has multiple logical modules that consumers import independently.

```jsonc
{
  "name": "@myorg/std-toolkit",
  "version": "1.0.0",
  "exports": {
    ".": "./mod.js",
    "./assert": "./assert/mod.js",
    "./http": "./http/mod.js",
    "./path": "./path/mod.js",
    "./testing": "./testing/mod.js"
  }
}
```

```js
// Consumers import only what they need
import { assertEquals } from "@myorg/std-toolkit/assert";
import { serve } from "@myorg/std-toolkit/http";
// Tree-shaking and code-splitting work naturally with subpath imports
```

**Rationale**: The `@std` standard library uses this pattern extensively — each `@std/*` package is a separate JSR package, but within a package, subpath exports provide further granularity. Subpath exports enable consumers to import only the functionality they need, enabling better tree-shaking at the package level (JSR registry docs; Deno standard library docs).

---

## ID-06: `exclude` Field — Keep Dev Files Out of the Package

**Strength**: SHOULD

**Summary**: Use `exclude` to prevent test files, benchmarks, and development artifacts from being included in the published package.

```jsonc
{
  "name": "@myorg/http-utils",
  "version": "1.0.0",
  "exports": "./mod.js",
  "exclude": [
    "**/*_test.js",
    "**/*.test.js",
    "testing/",
    "benchmarks/",
    "examples/",
    "*.md",
    "!README.md"
  ]
}
```

**Rationale**: Test files, benchmarks, and examples are development artifacts that consumers don't need. Excluding them reduces package size and prevents consumers from accidentally importing test utilities. The `!` prefix re-includes a file that would otherwise be excluded (Deno configuration docs).

---

## ID-07: `deno publish` — Authenticate, Validate, Upload

**Strength**: MUST

**Summary**: `deno publish` is the single command that validates and uploads your package to JSR.

```sh
# Publish (prompts for browser-based authentication on first use)
deno publish

# Publish a specific workspace member
deno publish --cwd packages/http-utils

# Publish all workspace members from the root
deno publish
```

**What `deno publish` validates before uploading**:
1. `name` and `version` are present and valid
2. `exports` is declared and all referenced files exist
3. Type information is complete on all exported symbols (the "slow types" check — see ID-10)
4. No type errors in exported code

**Authentication**: First publish prompts for OAuth via browser. In CI, use `JSR_TOKEN` or `DENO_AUTH_TOKENS` environment variable.

**Rationale**: `deno publish` handles validation, type-checking, and upload in one step. It refuses to publish if the package doesn't meet JSR's requirements — fix the issues, then try again (JSR registry docs).

---

## ID-08: `deno publish --dry-run` — Validate Without Publishing

**Strength**: SHOULD

**Summary**: `--dry-run` runs all validation checks without actually uploading. Use it to catch issues before committing to a version.

```sh
# Validate everything, publish nothing
deno publish --dry-run

# Typical workflow
deno publish --dry-run   # fix any issues
deno publish --dry-run   # verify fixes
deno publish             # ship it
```

**Rationale**: Published versions are immutable — you cannot fix a mistake in `1.0.0`, only publish `1.0.1`. `--dry-run` lets you iterate on validation errors (missing types, missing exports, unresolved modules) without burning a version number. Make it a habit before every publish (JSR registry docs).

---

## ID-09: `--allow-dirty` for Publishing with Uncommitted Changes

**Strength**: CONSIDER

**Summary**: By default, `deno publish` refuses to publish if there are uncommitted git changes. `--allow-dirty` overrides this.

```sh
# Publish with uncommitted changes (not recommended for releases)
deno publish --allow-dirty
```

**Rationale**: The uncommitted-changes check is a safety net — it prevents publishing code that differs from what's in version control. Use `--allow-dirty` only during development iteration, never for actual releases.

---

## ID-10: JSR Requires Type Information — The "Slow Types" Rule for Plain JS

**Strength**: MUST

**Summary**: JSR requires complete type information on all exported symbols. For plain JS, this means comprehensive JSDoc with `@param` and `@returns` on every export.

```js
// Good — JSDoc provides the type information JSR needs
/**
 * Parse a port number from a string.
 *
 * @param {string} input - The string to parse.
 * @returns {number} The parsed port number.
 * @throws {RangeError} If the port is out of range.
 */
export function parsePort(input) {
  const port = Number(input);
  if (!Number.isFinite(port) || port < 0 || port > 65535) {
    throw new RangeError(`Invalid port: ${input}`);
  }
  return port;
}

// Bad — no JSDoc, JSR cannot generate type declarations
export function parsePort(input) {
  const port = Number(input);
  if (!Number.isFinite(port) || port < 0 || port > 65535) {
    throw new RangeError(`Invalid port: ${input}`);
  }
  return port;
}
```

**What "slow types" means**: JSR needs to generate `.d.ts` type declarations for consumers. Without explicit type annotations, JSR would have to run the full TypeScript compiler's type inference engine to figure out the types — which is slow (hence "slow types"). With explicit annotations (`@param`, `@returns` in JSDoc, or type annotations in TypeScript), JSR can extract types quickly ("fast types") without running inference. For plain JS, this means JSDoc annotations are mandatory on all exports. If an exported function lacks `@param`/`@returns`, the type cannot be fully resolved, and `deno publish` will flag it.

**What to annotate**: Every exported function, class, constant, and type alias needs JSDoc type annotations. Internal (non-exported) code does not need annotations for JSR — but it may still benefit from them for `deno check`.

**Rationale**: JSR auto-generates documentation and type declarations from published source. Without type information, the generated docs are incomplete and consumers lose autocomplete and type safety. This connects Guide 05 (type annotation syntax) and Guide 11 (documentation prose) — both are required for publishable packages (JSR registry docs).

**See also**: `05-type-discipline.md` ID-16–20, `11-documentation.md` ID-05–09

---

## ID-11: JSR Auto-Generates Documentation from JSDoc

**Strength**: SHOULD

**Summary**: Your JSDoc comments become the package's documentation page on JSR. Write for the registry, not just for editors.

```js
/**
 * HTTP utilities for Deno applications.
 *
 * @example
 * ```js
 * import { createRouter } from "@myorg/http-utils";
 * const router = createRouter();
 * router.get("/", () => new Response("Hello!"));
 * ```
 *
 * @module
 */

/**
 * Create an HTTP router with type-safe route handlers.
 *
 * @param {{ prefix?: string }} [options] - Router configuration.
 * @returns {Router} A new router instance.
 *
 * @example
 * ```js
 * import { createRouter } from "@myorg/http-utils";
 * const router = createRouter({ prefix: "/api" });
 * ```
 */
export function createRouter(options = {}) { /* ... */ }
```

**What renders on JSR**:
- Module-level `@module` JSDoc → package overview page
- Function/class JSDoc → per-symbol documentation
- `@example` code blocks → rendered as examples and testable with `deno test --doc`

**Rationale**: JSR documentation is auto-generated, not manually written. The quality of your JSDoc directly determines the quality of your package's documentation on the registry. The `@std` standard library sets the bar (JSR registry docs).

**See also**: `11-documentation.md` ID-10, ID-11, ID-12

---

## ID-12: Scoped Packages — Create a Scope First

**Strength**: MUST

**Summary**: Create your scope on jsr.io before publishing. All JSR packages are scoped.

```
1. Go to jsr.io and sign in
2. Create a scope (e.g., @myorg)
3. Add your deno.json: "name": "@myorg/my-package"
4. Run: deno publish
```

**Rationale**: JSR has no unscoped packages. The scope is your organization or username, and it controls who can publish under it. Creating the scope is a one-time setup (JSR registry docs).

---

## ID-13: Immutable Versions — Once Published, Cannot Be Changed

**Strength**: SHOULD

**Summary**: A published version is permanent. To fix a mistake, publish a new version.

```sh
# Published 1.0.0 with a bug? Can't fix it in place.
# Must publish 1.0.1
# version in deno.json: "1.0.1"
deno publish
```

**Rationale**: Immutability is a fundamental registry guarantee — consumers who depend on `1.0.0` always get the exact same code. This prevents the left-pad problem (npm, 2016) where unpublishing broke the ecosystem. Always use `--dry-run` before publishing to avoid burning a version number on a mistake (JSR registry docs).

---

## ID-14: `0.x.y` Versions — Breaking Changes at Minor Bumps

**Strength**: SHOULD

**Summary**: During early development, use `0.x.y`. The semver spec allows breaking changes in minor bumps when major is `0`.

```jsonc
// 0.1.0 → 0.2.0: breaking API change (allowed by semver)
// 0.2.0 → 0.2.1: bug fix
// 0.2.1 → 1.0.0: API is stable, first stable release
```

**Rationale**: `0.x.y` signals "this API is not yet stable" to consumers. Semver explicitly states: "Major version zero (0.y.z) is for initial development. Anything MAY change at any time." Use this for all packages until the API is proven stable through real usage.

---

## ID-15: Module-Level JSDoc for JSR Pages

**Strength**: SHOULD

**Summary**: A `@module` JSDoc block at the top of each exported file becomes the module's description on JSR.

```js
/**
 * Cryptographic hashing utilities for Deno.
 *
 * Supports SHA-256, SHA-384, and SHA-512 via the Web Crypto API.
 * All functions are async because they delegate to `crypto.subtle`.
 *
 * @module
 */

export async function sha256(data) { /* ... */ }
export async function sha512(data) { /* ... */ }
```

**Rationale**: JSR renders the `@module` JSDoc as the module's overview on its documentation page. Without it, the page shows a bare list of exports with no context. This connects to Guide 11 (ID-11): "Every module gets a top-of-file JSDoc block" (JSR registry docs).

**See also**: `11-documentation.md` ID-11

---

## ID-16: `@example` Blocks Render on JSR and Are Testable

**Strength**: SHOULD

**Summary**: JSDoc `@example` blocks with fenced code render as examples on JSR and can be verified with `deno test --doc`. The `@example` tag labels the block for JSR rendering; the fenced code block is what `deno test --doc` extracts and executes.

```js
/**
 * Hash a string using SHA-256.
 *
 * @param {string} input - The string to hash.
 * @returns {Promise<string>} Hex-encoded hash.
 *
 * @example
 * ```js
 * import { sha256 } from "@myorg/crypto-utils";
 * import { assertEquals } from "@std/assert";
 * const hash = await sha256("hello");
 * assertEquals(typeof hash, "string");
 * assertEquals(hash.length, 64);
 * ```
 */
export async function sha256(input) { /* ... */ }
```

```sh
# Verify examples compile and pass
deno test --doc crypto.js
```

**Rationale**: Examples that are also tests cannot silently become stale. JSR renders them on the documentation page, and `deno test --doc` runs them in CI. Use fenced code blocks (triple backticks) inside `@example` — this is the format Deno extracts and executes (JSR registry docs; Deno test runner docs).

**See also**: `11-documentation.md` ID-10, `12-deno/02-testing.md` ID-20

---

## ID-17: The Pre-Publish Pipeline — Checklist as a Task

**Strength**: SHOULD

**Summary**: Define a `publish` task that runs the full quality pipeline before publishing. One command, checks always run.

```jsonc
// deno.json
{
  "tasks": {
    "prepublish": "biome ci && deno check **/*.js && deno test --allow-all --doc && deno publish --dry-run",
    "publish": "deno task prepublish && deno publish"
  }
}
```

```sh
# One command to verify everything and publish
deno task publish
```

**The pipeline, step by step**:

| Step | Command | What it catches |
|------|---------|----------------|
| 1. Lint + fmt | `biome ci` | Style violations, lint errors |
| 2. Type-check | `deno check **/*.js` | Type errors in JSDoc annotations |
| 3. Test + doc-test | `deno test --allow-all --doc` | Broken tests, stale examples |
| 4. Dry-run | `deno publish --dry-run` | Missing exports, slow types, metadata issues |
| 5. Publish | `deno publish` | Upload to JSR |

**Why a task, not manual steps**: Making `publish` a task ensures the pre-publish checks always run — nobody can accidentally skip them by running `deno publish` directly. The pipeline uses `&&` so it stops at the first failure. Each step catches a different class of issue.

**Rationale**: `biome ci` catches formatting/lint. `deno check` catches type errors. `deno test --doc` catches stale examples. `--dry-run` catches JSR-specific issues (missing types on exports, bad metadata). The task is the single source of truth for the release process.

**See also**: `12-deno/03-task-runner.md` ID-07, ID-19

---

## ID-18: Workspace Publishing — Members Publish Independently

**Strength**: CONSIDER

**Summary**: In a workspace, each member with `name` and `version` publishes independently to JSR.

```jsonc
// Root deno.json
{
  "workspace": ["./packages/core", "./packages/cli"]
}

// packages/core/deno.json
{
  "name": "@myorg/core",
  "version": "1.0.0",
  "exports": "./mod.js"
}

// packages/cli/deno.json
{
  "name": "@myorg/cli",
  "version": "0.3.0",
  "exports": "./mod.js"
}
```

```sh
# Publish all workspace members
deno publish

# Publish a single member
deno publish --cwd packages/core
```

**Cross-member imports**: During development, `import { x } from "@myorg/core"` resolves via the workspace. When published, workspace references are automatically rewritten to registry specifiers (`jsr:@myorg/core@1.0.0`).

**Rationale**: Each workspace member has its own version and publishes independently. This enables the `@std` pattern: a monorepo of independently versioned packages under one scope. Members can depend on each other, and the workspace handles resolution locally while the registry handles it for consumers (Deno workspace docs).

**See also**: `10-project-structure.md` ID-25

---

## ID-19: `license` Field

**Strength**: SHOULD

**Summary**: Include a `license` field in `deno.json` to declare the package's license.

```jsonc
{
  "name": "@myorg/http-utils",
  "version": "1.0.0",
  "exports": "./mod.js",
  "license": "MIT"
}
```

**Rationale**: The license is displayed on the JSR package page and is checked by consumers' compliance tools. Use a standard SPDX identifier (MIT, Apache-2.0, ISC, etc.).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `name` — scoped identifier | MUST | `@scope/package` format required |
| 02 | `version` — semver | MUST | Immutable once published; full semver contract |
| 03 | `exports` — public API map | MUST | Only exported paths are importable |
| 04 | `exports` enforces boundary | SHOULD | Internal files are truly private |
| 05 | Subpath exports | SHOULD | Multi-entrypoint packages |
| 06 | `exclude` dev files | SHOULD | Tests, benchmarks out of package |
| 07 | `deno publish` | MUST | Validates, type-checks, uploads |
| 08 | `--dry-run` | SHOULD | Validate before committing a version |
| 09 | `--allow-dirty` | CONSIDER | Dev only; never for releases |
| 10 | JSDoc for "slow types" | MUST | Plain JS needs `@param`/`@returns` on all exports |
| 11 | JSDoc → JSR docs | SHOULD | Auto-generated; write for the registry |
| 12 | Create scope first | MUST | All JSR packages are scoped |
| 13 | Immutable versions | SHOULD | Can't fix in place; must bump version |
| 14 | `0.x.y` for unstable | SHOULD | Breaking changes at minor bumps allowed |
| 15 | Module-level `@module` JSDoc | SHOULD | Becomes module overview on JSR |
| 16 | `@example` blocks | SHOULD | Render on JSR + testable with `--doc` |
| 17 | Pre-publish pipeline as task | SHOULD | lint → typecheck → test → dry-run → publish |
| 18 | Workspace publishing | CONSIDER | Members publish independently |
| 19 | `license` field | SHOULD | Displayed on JSR; SPDX identifier |

### Publishing Quick Reference

```sh
# Validate without publishing
deno publish --dry-run

# Publish to JSR
deno publish

# Publish specific workspace member
deno publish --cwd packages/core

# Full pipeline (define as deno task)
biome ci && deno check **/*.js && deno test --allow-all --doc && deno publish
```

### Required `deno.json` Fields for Publishing

```jsonc
{
  "name": "@scope/package",    // REQUIRED — scoped identifier
  "version": "1.0.0",          // REQUIRED — semver
  "exports": "./mod.js",       // REQUIRED — public API entry point(s)
  "license": "MIT",            // RECOMMENDED — SPDX identifier
  "exclude": ["**/*_test.js"]  // RECOMMENDED — keep dev files out
}
```

---

## Related Guidelines

- **API Design**: See `02-api-design.md` for module design (ID-06), named exports (ID-07), barrel files (ID-08), no side effects (ID-09)
- **Type Discipline**: See `05-type-discipline.md` for JSDoc annotations (ID-16–20) required for "slow types" compliance
- **Project Structure**: See `10-project-structure.md` for `mod.js` entry point (ID-08), barrel files (ID-09), workspaces (ID-25), `deno.json` (ID-15)
- **Documentation**: See `11-documentation.md` for JSDoc prose (ID-05–09), module-level docs (ID-11), `@example` (ID-10), writing for tooling (ID-12)
- **Runtime Basics**: See `12-deno/01-runtime-basics.md` for `deno.json` config (ID-13), `jsr:` specifiers (ID-17), `@std/*` (ID-25)
- **Testing**: See `12-deno/02-testing.md` for `deno test --doc` (ID-20), test coverage (ID-21)
- **Task Runner**: See `12-deno/03-task-runner.md` for `check` task (ID-07), CI pipeline (ID-19), task composition (ID-18)

---

## External References

- [JSR Registry](https://jsr.io/)
- [JSR — Publishing Packages](https://jsr.io/docs/publishing-packages)
- [Deno — Configuration (`deno.json`)](https://docs.deno.com/runtime/fundamentals/configuration/)
- [Deno — Workspaces](https://docs.deno.com/runtime/fundamentals/workspaces/)
- [Semver Specification](https://semver.org/)
