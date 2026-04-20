# Project Structure

How to organize a Deno JavaScript project for clarity, maintainability, and tooling compatibility: directory layout, file naming, module dependency flow, entry points, configuration, and test structure. This guide covers the *structural skeleton* — the decisions you make before writing application code. Module API design is in Guide 02; Deno runtime details are in Guide 12. Grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), *Eloquent JavaScript* (Haverbeke), and Deno documentation.

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: Flat-by-Feature, Not Nested-by-Type

**Strength**: SHOULD

**Summary**: Group files by feature/domain, not by technical role. Don't default to `controllers/`, `models/`, `services/`.

```
// Good — flat-by-feature: everything for a feature is together
project/
├── deno.json
├── mod.js
├── auth/
│   ├── mod.js              # public API: re-exports
│   ├── login.js            # login logic
│   ├── session.js          # session management
│   ├── password.js         # password hashing
│   └── auth_test.js        # tests for auth
├── users/
│   ├── mod.js
│   ├── repository.js       # data access
│   ├── validation.js       # input validation
│   └── users_test.js
└── shared/
    ├── http.js             # shared HTTP utilities
    └── constants.js        # shared constants

// Bad — nested-by-type: adding a feature touches every directory
project/
├── controllers/
│   ├── auth_controller.js
│   └── user_controller.js
├── models/
│   ├── auth_model.js
│   └── user_model.js
├── services/
│   ├── auth_service.js
│   └── user_service.js
└── utils/
    ├── http.js
    └── constants.js
```

**Why nested-by-type fails**: Adding or modifying a feature requires touching files in 3-4 directories (controller + model + service + test). This is "shotgun surgery" — a single logical change scattered across the project. Imports between layers create cross-directory dependency webs. Deleting a feature requires hunting through every directory.

**Why flat-by-feature works**: All files for `auth/` are in one directory. Adding a feature means adding a directory. Deleting it means deleting one directory. Imports stay local. Each feature directory has a clear public API via its `mod.js`.

**Rationale**: Haverbeke's module design principle: "modules that compute values are applicable in a wider range of programs than bigger modules that perform complicated actions with side effects." Feature cohesion maps to module cohesion (Eloquent JS Ch. 10).

---

## ID-02: Keep the Root Clean

**Strength**: SHOULD

**Summary**: The project root should contain only configuration files and the entry point. Source code goes in feature directories.

```
// Good — clean root
project/
├── deno.json               # config
├── deno.lock               # lockfile (auto-generated)
├── biome.json              # Biome config (if not using deno.json fmt/lint)
├── README.md
├── mod.js                  # library entry point
├── main.js                 # application entry point
├── auth/
│   └── ...
├── users/
│   └── ...
└── shared/
    └── ...

// Bad — cluttered root
project/
├── deno.json
├── auth.js
├── users.js
├── session.js
├── password.js
├── constants.js
├── http_utils.js
├── auth_test.js
├── users_test.js
└── ...  (20 more files)
```

**Rationale**: A developer opening the project should immediately see its structure — config at root, features as directories. A flat root with dozens of source files is as disorienting as a nested-by-type layout.

---

## ID-03: Reference Directory Structure for a Deno Project

**Strength**: SHOULD

**Summary**: A standard Deno project layout with feature directories, co-located tests, and centralized configuration.

```
my-project/
├── deno.json                # imports, tasks, lint, fmt, compilerOptions
├── deno.lock                # auto-generated lockfile
├── mod.js                   # library entry point (public API)
├── main.js                  # application entry point (CLI or server)
├── auth/
│   ├── mod.js               # re-exports: export { login } from "./login.js"
│   ├── login.js
│   ├── session.js
│   └── auth_test.js
├── users/
│   ├── mod.js
│   ├── repository.js
│   ├── validation.js
│   └── users_test.js
├── shared/
│   ├── http.js
│   ├── constants.js
│   └── types.js             # shared @typedef definitions
└── testing/
    └── helpers.js            # shared test utilities
```

**Conventions visible here**:
- `mod.js` for entry points (Deno convention, replaces `index.js`)
- `*_test.js` for tests (Deno test runner auto-discovery)
- Feature directories with internal `mod.js` barrel files
- `shared/` for cross-feature utilities
- `testing/` for test infrastructure (separate from `shared/`)

---

## ID-04: kebab-case for File and Directory Names

**Strength**: SHOULD

**Summary**: Use `kebab-case` (lowercase with hyphens) for all file and directory names. Reserve PascalCase for class names inside files.

```
// Good
auth/
  password-hash.js
  session-store.js
  auth_test.js

// Bad — PascalCase, camelCase, or mixed
Auth/
  PasswordHash.js
  sessionStore.js
  AuthTest.js
```

**Exception**: Test files use `*_test.js` (underscore) per Deno convention (ID-07). The underscore separates the module name from the `test` suffix and matches Deno's test runner auto-discovery pattern.

**Rationale**: kebab-case is the Deno and web ecosystem convention for file names. It avoids case-sensitivity issues across operating systems (macOS is case-insensitive by default, Linux is not). Class names are PascalCase inside the file, not in the filename (Exploring JS Ch. 9).

**See also**: `01-core-idioms.md` ID-12

---

## ID-05: One Module, One Purpose

**Strength**: SHOULD

**Summary**: Each file should have a single clear responsibility. If you can't describe what a file does in one sentence, split it.

```js
// Good — focused modules
// password.js — password hashing and verification
export function hashPassword(plain) { /* ... */ }
export function verifyPassword(plain, hash) { /* ... */ }

// Bad — kitchen-sink utility
// utils.js — "various helpers"
export function hashPassword(plain) { /* ... */ }
export function formatDate(d) { /* ... */ }
export function slugify(s) { /* ... */ }
export function debounce(fn, ms) { /* ... */ }
```

**Rationale**: Haverbeke: modules that "compute values are applicable in a wider range of programs than bigger modules that perform complicated actions with side effects." Focused modules are independently testable, tree-shakeable, and easier to find via filename (Eloquent JS Ch. 10).

**See also**: `02-api-design.md` ID-06

---

## ID-06: Name Files After Their Primary Export

**Strength**: SHOULD

**Summary**: A file named `session.js` should export session-related functions. Don't name files after their role in a framework.

```
// Good — file name matches content
auth/
  login.js          # export function login() {}
  session.js        # export function createSession() {}
  password.js       # export function hashPassword() {}

// Bad — generic role-based naming
auth/
  controller.js     # what does it control? auth? users? both?
  service.js        # service for what?
  helper.js         # helper for... everything?
```

**Rationale**: When you see `import { createSession } from "./auth/session.js"`, both the import and the file name communicate the same thing. Generic names like `helper.js` or `utils.js` accumulate unrelated code over time.

---

## ID-07: Test Files Use `*_test.js` for Deno Auto-Discovery

**Strength**: SHOULD

**Summary**: Deno's test runner auto-discovers files matching `*_test.js`, `*.test.js`, and `test.js`. Use `*_test.js` as the primary convention.

```
// Good — Deno discovers these automatically
auth/
  login.js
  login_test.js       # deno test finds this
users/
  repository.js
  repository_test.js   # deno test finds this

// Also valid — dot-separated
auth/
  login.test.js

// Bad — tests hidden in a non-standard location
__tests__/
  auth/
    login.spec.js      # Deno doesn't discover .spec.js by default
```

**Rationale**: `deno test` discovers files matching `{*_,*.,}test.{ts,tsx,mts,js,mjs,jsx}` by default. Using the convention eliminates configuration and ensures `deno test` works out of the box. The `*_test.js` pattern (underscore) is the Deno standard library convention.

---

## ID-08: Explicit Entry Point — `mod.js` for Libraries, `main.js` for Applications

**Strength**: SHOULD

**Summary**: Use `mod.js` as the library entry point (Deno convention). Use `main.js` for application entry points (CLI, server).

```
// Library — mod.js is the public API
my-lib/
├── deno.json        # "exports": "./mod.js"
├── mod.js           # export { create } from "./create.js"; export { parse } from "./parse.js"
├── create.js
└── parse.js

// Application — main.js is the entry point
my-app/
├── deno.json        # tasks: { "start": "deno run --allow-net main.js" }
├── main.js          # Deno.serve(...) or CLI logic
├── auth/
│   └── ...
└── users/
    └── ...
```

**Note**: `mod.js` is the convention, but the `exports` field in `deno.json` is the actual mechanism that controls what consumers can import. The entry point can technically be any filename — `exports` is what the package registry and runtime resolve. `mod.js` is conventional because it is self-documenting and widely recognized in the Deno ecosystem.

**Rationale**: Deno uses `mod.js` (or `mod.ts`) as the conventional entry point for libraries, replacing Node.js's `index.js`. The `exports` field in `deno.json` makes this explicit for the package registry. `main.js` is the conventional name for application entry points — the file you pass to `deno run`.

---

## ID-09: Barrel Files for Public API Surfaces — Selective Re-Exports Only

**Strength**: SHOULD

**Summary**: Use selective re-exports in `mod.js` to define the public API. Avoid wildcard `export *`.

```js
// Good — selective re-exports (explicit, tree-shakeable)
// auth/mod.js
export { login, logout } from "./login.js";
export { createSession, destroySession } from "./session.js";
export { hashPassword } from "./password.js";

// Bad — wildcard re-export (opaque, name conflicts silently drop exports)
// auth/mod.js
export * from "./login.js";
export * from "./session.js";   // if session.js also exports "login", it vanishes
export * from "./password.js";
```

**Rationale**: Wildcard `export *` does NOT re-export default exports, can silently suppress conflicting names, and makes the public API invisible without reading every sub-module. Selective re-exports make the API explicit and stable. Tree-shaking works better with selective re-exports because bundlers can trace exact names (Exploring JS Ch. 29; JS Definitive Guide, §10.3.4).

**See also**: `02-api-design.md` ID-08

---

## ID-10: Avoid Deep Imports into Internal Modules

**Strength**: SHOULD

**Summary**: Consumers should import from a feature's `mod.js`, not from its internal files.

```js
// Good — import from the public API
import { login, createSession } from "./auth/mod.js";

// Bad — reaching into internals
import { hashPassword } from "./auth/password.js";
import { validateToken } from "./auth/session.js";
```

**Enforcement levels**: For published packages, the `exports` field in `deno.json` controls what's importable — deep imports into unexported paths are rejected by the runtime. For internal project code (not published), this is an organizational convention enforced by code review, not by tooling.

**Rationale**: Deep imports create tight coupling to internal file structure. Renaming or reorganizing internal files breaks every consumer. A barrel file (`mod.js`) provides a stable public API that can be refactored behind without breaking imports. The exception is within the feature directory itself, where direct imports between sibling files are expected.

---

## ID-11: Dependency Direction — Depend Inward, Not Outward

**Strength**: MUST

**Summary**: Inner/core modules should not import from outer/feature modules. Dependencies flow inward toward shared abstractions.

```
// Good — dependency flows inward
auth/login.js       → imports from shared/http.js     ✓ (inward)
users/repository.js → imports from shared/http.js     ✓ (inward)
shared/http.js      → imports from nothing outside     ✓ (leaf)

// Bad — shared module depends on a feature
shared/http.js      → imports from auth/session.js    ✗ (outward!)
auth/login.js       → imports from users/repository.js ✗ (cross-feature)
```

**The dependency rule**:
- Feature modules may import from `shared/`
- `shared/` modules must not import from feature modules
- Feature modules should not import from other feature modules directly — if they need to share, extract to `shared/`

**Rationale**: Outward dependencies create circular dependency risks and make modules impossible to use independently. Haverbeke: "explicitly declare all dependencies via `import`" — hidden dependencies through shared state or outward imports make the graph invisible (Eloquent JS Ch. 10).

---

## ID-12: No Circular Imports

**Strength**: MUST

**Summary**: ESM circular imports cause bindings to be `undefined` at access time. They are a signal of poor module decomposition.

```js
// Anti-pattern — circular import with const (throws ReferenceError)
// a.js
import { b } from "./b.js";
export const a = `a-${b}`;

// b.js
import { a } from "./a.js";
export const b = `b-${a}`;  // ReferenceError: Cannot access 'a' before initialization

// With var instead of const — silently produces wrong values (no error)
// a.js
import { b } from "./b.js";
export var a = `a-${b}`;

// b.js
import { a } from "./a.js";
export var b = `b-${a}`;    // a is undefined — b becomes "b-undefined"
// Then a becomes "a-b-undefined" — silently wrong
```

**Why it happens**: ESM resolves the module graph before execution. When A imports B and B imports A, the engine creates binding slots for all exports during the linking phase. But when B's top-level code runs and reads `a`, A's code hasn't executed yet. The behavior depends on the declaration:
- **`const`/`let`/`class`**: The binding is in the Temporal Dead Zone — accessing it throws `ReferenceError`
- **`var`/`function`**: The binding exists and is hoisted to `undefined` (for `var`) or the function body (for `function`) — producing silently wrong values instead of throwing

The `const` case is actually safer because it throws immediately. The `var` case is more dangerous because it silently produces `undefined`-contaminated values.

**How to fix**: Extract the shared dependency into a third module.

```js
// Fix — extract shared code
// shared.js
export const shared = "value";

// a.js
import { shared } from "./shared.js";
export const a = `a-${shared}`;

// b.js
import { shared } from "./shared.js";
export const b = `b-${shared}`;
```

**Common accidental cycle**: A sub-module imports from its own barrel file (`import { foo } from "../mod.js"` where `mod.js` re-exports from that sub-module). Always import sibling files directly within a feature directory.

**Rationale**: Rauschmayer explicitly notes that ESM supports cyclic imports but bindings may be uninitialized. Haverbeke warns they "can cause problems." The safe approach is to avoid them entirely through structural discipline (Exploring JS Ch. 29; Eloquent JS Ch. 10; JS Definitive Guide, §10.3).

---

## ID-13: Limit Import Depth — Restructure If Imports Are Deep

**Strength**: SHOULD

**Summary**: If you're writing `../../utils/helpers/strings.js`, the project structure needs work.

```js
// Bad — deep relative imports signal structural problems
import { slugify } from "../../utils/helpers/strings.js";
import { validate } from "../../../shared/validation/schema.js";

// Good — shallow imports via feature barrels or import map
import { slugify } from "../../shared/strings.js";

// Better — import map alias for frequently used shared modules
// deno.json: { "imports": { "@shared/": "./shared/" } }
import { slugify } from "@shared/strings.js";
```

**Rationale**: Deep relative imports are fragile (any directory rename breaks them) and hard to read. If imports consistently reach 3+ levels up, it means the module is in the wrong directory or the shared code needs a shorter path. Import map aliases (`@shared/`, `@/`) solve this for cross-cutting utilities.

---

## ID-14: Separate Pure Logic from I/O

**Strength**: SHOULD

**Summary**: Keep core business logic in pure modules that import nothing with side effects. Push I/O to the edges.

```
// Good — pure core, I/O at edges
shared/
  transform.js       # pure: export function transform(data) { ... }
  validate.js        # pure: export function validate(input) { ... }
auth/
  login.js           # I/O: reads from database, calls transform/validate
main.js              # I/O: Deno.serve(), reads config

// Bad — I/O mixed into core logic
shared/
  transform.js       # import { readFile } from "..."; — now has side effects
                     # cannot be imported without triggering I/O
```

**Rationale**: Pure modules (no I/O, no side effects at import time) are tree-shakeable, independently testable, and safe to import from anywhere. Modules with top-level side effects defeat tree shaking and create import-order dependencies (Exploring JS Ch. 29; Eloquent JS Ch. 10).

**See also**: `02-api-design.md` ID-09, `08-performance.md` ID-31

---

## ID-15: `deno.json` as the Single Config Source

**Strength**: SHOULD

**Summary**: Centralize imports, tasks, lint, fmt, and compiler options in `deno.json`. Don't scatter config across multiple files.

```json
{
  "imports": {
    "@std/assert": "jsr:@std/assert@^1.0.0",
    "@std/path": "jsr:@std/path@^1.0.0",
    "chalk": "npm:chalk@5",
    "@shared/": "./shared/"
  },
  "tasks": {
    "dev": "deno run --watch --allow-net --allow-read main.js",
    "test": "deno test --allow-all",
    "check": "deno test --allow-all",
    "bench": "deno bench"
  },
  "compilerOptions": {
    "checkJs": true,
    "strict": true
  }
}
```

**Note on lint/fmt**: This example omits `lint` and `fmt` fields because the lykn project uses **Biome** for linting and formatting (configured in `biome.json`), not Deno's built-in tools. If your project uses Deno's built-in linter/formatter instead of Biome, add `lint` and `fmt` sections here. See `13-biome/01-setup.md` for Biome configuration.

**Rationale**: `deno.json` replaces `package.json` and `tsconfig.json` in a single file. When using Biome, it also eliminates `.eslintrc` and `.prettierrc` — Biome handles those in `biome.json`. Accepts `.jsonc` (comments allowed). Auto-detected by walking up the directory tree. Centralizing config eliminates the "which of these 7 config files controls X?" problem.

---

## ID-16: Import Maps for Dependency Aliases

**Strength**: SHOULD

**Summary**: Use the `imports` field in `deno.json` for bare specifier mapping. Versions are declared once, used everywhere.

```json
{
  "imports": {
    "@std/assert": "jsr:@std/assert@^1.0.0",
    "@std/path": "jsr:@std/path@^1.0.0",
    "@shared/": "./shared/",
    "@auth/": "./auth/"
  }
}
```

```js
// Source files use clean bare specifiers
import { assertEquals } from "@std/assert";
import { join } from "@std/path";
import { slugify } from "@shared/strings.js";
```

**Rationale**: Import maps centralize version declarations — update once in `deno.json`, not in every source file. Directory aliases (`@shared/`) eliminate deep relative paths. `deno add jsr:@pkg/name` manages the import map automatically.

---

## ID-17: Environment-Specific Config via Environment Variables

**Strength**: SHOULD

**Summary**: Use environment variables for runtime configuration. Don't use conditional imports or compile-time flags.

```js
// Good — environment variables
const PORT = Number(Deno.env.get("PORT") ?? "8080");
const DB_URL = Deno.env.get("DATABASE_URL") ?? "sqlite:./dev.db";

Deno.serve({ port: PORT }, handler);

// Bad — conditional imports based on environment
const config = Deno.env.get("ENV") === "prod"
  ? await import("./config.prod.js")   // dynamic import for config
  : await import("./config.dev.js");    // defeats static analysis
```

**Rationale**: Environment variables are the standard mechanism for runtime configuration across all platforms. Conditional imports create code paths that are hard to test and defeat static analysis. Configuration modules (if needed) should read environment variables internally, not be swapped via dynamic import.

---

## ID-18: Centralize Shared Constants

**Strength**: SHOULD

**Summary**: Put constants used across feature modules in a dedicated `shared/constants.js` file.

```js
// shared/constants.js
export const MAX_RETRIES = 3;
export const DEFAULT_TIMEOUT = 5000;
export const API_VERSION = "v2";

// Feature module imports what it needs
import { MAX_RETRIES, DEFAULT_TIMEOUT } from "@shared/constants.js";
```

**Rationale**: Scattered magic values are hard to find and change. A dedicated constants module is searchable, changeable in one place, and self-documenting. Use `Object.freeze()` for constant objects.

**See also**: `01-core-idioms.md` ID-11, `04-values-references.md` ID-19

---

## ID-19: JSDoc Types — Co-Locate or Centralize

**Strength**: CONSIDER

**Summary**: For types used in one module, define them inline. For types shared across features, centralize in `shared/types.js`.

```js
// Good — inline for local use
/**
 * @typedef {{ host: string, port: number, tls?: boolean }} ServerConfig
 */

/** @param {ServerConfig} config */
export function createServer(config) { /* ... */ }

// Good — centralized for shared use
// shared/types.js
/**
 * @typedef {{ id: string, name: string, email: string }} User
 * @typedef {{ status: "ok", data: unknown } | { status: "error", message: string }} ApiResult
 */

// Feature modules reference the shared types
/** @type {import("@shared/types.js").User} */
const user = await getUser(id);
```

**Rationale**: Co-locating types keeps them close to the code that uses them, reducing indirection. Centralizing shared types prevents duplication. The `import()` syntax in JSDoc references types across files without a runtime import.

**See also**: `05-type-discipline.md` ID-17

---

## ID-20: Co-Locate Tests with Source

**Strength**: SHOULD

**Summary**: Place test files next to the source files they test. This is the default for Deno's test runner.

```
// Good — co-located tests
auth/
  login.js
  login_test.js       # tests for login.js
  session.js
  session_test.js     # tests for session.js

// Also acceptable — mirrored test directory (pick one, be consistent)
auth/
  login.js
  session.js
tests/
  auth/
    login_test.js
    session_test.js
```

**Rationale**: Co-located tests are discovered by `deno test` automatically, require shorter import paths, and are visible alongside the code they test — you see immediately if a module lacks tests. A mirrored `tests/` directory is acceptable for larger projects but requires more navigation.

---

## ID-21: Separate Test Utilities

**Strength**: CONSIDER

**Summary**: Shared test helpers (fixtures, mocks, custom assertions) go in a `testing/` directory, not in `shared/`.

```
testing/
  helpers.js          # createMockUser(), setupTestDb(), etc.
  fixtures/
    sample-config.json
    test-data.csv
```

```js
// In a test file
import { createMockUser } from "../testing/helpers.js";
```

**Rationale**: Test utilities are dependencies of tests, not of production code. Placing them in `shared/` risks accidental import into production modules. A dedicated `testing/` directory makes the boundary clear.

---

## ID-22: Pin Dependency Versions — Use `deno.lock`

**Strength**: SHOULD

**Summary**: Commit `deno.lock` to version control for reproducible builds. The lock file records cryptographic hashes of all resolved dependencies.

```json
// deno.json — versions in import map
{
  "imports": {
    "@std/assert": "jsr:@std/assert@^1.0.0",
    "chalk": "npm:chalk@5"
  }
}
// deno.lock is auto-generated and records exact resolved versions + hashes
```

**Rationale**: Without a lock file, `jsr:@std/assert@^1.0.0` could resolve to different patch versions on different machines or CI runs. `deno.lock` ensures every developer and CI run uses the exact same dependency versions. Deno automatically creates and updates it.

---

## ID-23: Prefer `jsr:` Specifiers over `npm:`

**Strength**: CONSIDER

**Summary**: Use `jsr:` for Deno standard library and packages published to JSR. Use `npm:` for npm-only packages.

```json
{
  "imports": {
    "@std/assert": "jsr:@std/assert@^1.0.0",
    "@std/path": "jsr:@std/path@^1.0.0",
    "@luca/cases": "jsr:@luca/cases@1.0.0",
    "chalk": "npm:chalk@5"
  }
}
```

**Rationale**: JSR is Deno's native registry. `jsr:` packages support TypeScript natively, publish source directly, and are designed for the Deno ecosystem. Use `npm:` only for packages that have no JSR equivalent. Both are resolved on import — no install step required.

---

## ID-24: Vendor Dependencies for Offline/CI Stability

**Strength**: CONSIDER

**Summary**: Use `"vendor": true` in `deno.json` to download all remote dependencies locally for air-gapped or reproducible builds.

```json
// deno.json — enable vendoring
{
  "vendor": true
}
```

```sh
# With "vendor": true, Deno downloads dependencies to vendor/ automatically
# Subsequent runs use vendor/ — no network needed
deno test --allow-all
```

**Rationale**: Vendoring creates a self-contained project that builds without network access. Setting `"vendor": true` in `deno.json` is the recommended approach in Deno 2.x — it automatically manages the `vendor/` directory on module resolution. Useful for air-gapped environments, auditing third-party code, and CI pipelines where registry availability is unreliable. The trade-off is repository size.

---

## ID-25: Deno Workspaces for Multi-Package Projects

**Strength**: CONSIDER

**Summary**: Use the `workspace` field in the root `deno.json` for monorepos with multiple packages.

```json
// Root deno.json
{
  "workspace": ["./core", "./cli", "./web"],
  "imports": {
    "@std/assert": "jsr:@std/assert@^1.0.0"
  }
}
```

```
project/
├── deno.json              # workspace root
├── deno.lock
├── core/
│   ├── deno.json          # { "name": "@myapp/core", "version": "0.1.0", "exports": "./mod.js" }
│   └── mod.js
├── cli/
│   ├── deno.json          # { "name": "@myapp/cli", "exports": "./main.js" }
│   └── main.js            # import { something } from "@myapp/core"
└── web/
    ├── deno.json
    └── main.js
```

**Key mechanics**:
- Members inherit root `imports`, `compilerOptions`, and lint/fmt rules
- Cross-member imports use the member `name` as a bare specifier
- Root-only fields: `workspace`, `lock`, `vendor`, `nodeModulesDir`
- Member-only fields: `name`, `version`, `exports`
- `deno test`, `deno lint`, `deno fmt` run across all members from the root

**Rationale**: Workspaces enable shared configuration, independent versioning, and cross-member imports without path gymnastics. Use them when a project has distinct publishable packages or clearly separated concerns that benefit from independent dependency management.

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Flat-by-feature layout | SHOULD | Group by domain, not by type; avoid shotgun surgery |
| 02 | Clean root | SHOULD | Config at root, source in feature directories |
| 03 | Reference directory structure | SHOULD | mod.js, *_test.js, feature dirs, shared/ |
| 04 | kebab-case file names | SHOULD | Cross-OS safe; PascalCase inside files only |
| 05 | One module, one purpose | SHOULD | Focused modules are testable and tree-shakeable |
| 06 | Name files after primary export | SHOULD | login.js exports login(), not "controller" |
| 07 | `*_test.js` for tests | SHOULD | Deno auto-discovery; no config needed |
| 08 | `mod.js` / `main.js` entry points | SHOULD | Deno convention; `exports` in deno.json |
| 09 | Selective re-exports in barrels | SHOULD | Wildcard `export *` hides conflicts |
| 10 | No deep imports into internals | SHOULD | Import from `mod.js`, not internal files |
| 11 | Depend inward, not outward | MUST | shared/ doesn't import from features |
| 12 | No circular imports | MUST | Bindings exist but may be uninitialized |
| 13 | Limit import depth | SHOULD | Deep paths signal wrong structure; use import maps |
| 14 | Separate pure logic from I/O | SHOULD | Pure modules are testable and tree-shakeable |
| 15 | `deno.json` as single config | SHOULD | Replaces package.json + tsconfig + eslintrc + prettierrc |
| 16 | Import maps for aliases | SHOULD | Centralized versions, clean bare specifiers |
| 17 | Env vars for runtime config | SHOULD | Don't use conditional imports |
| 18 | Centralize shared constants | SHOULD | One place to find and change |
| 19 | JSDoc types: co-locate or centralize | CONSIDER | Inline for local; shared/types.js for cross-feature |
| 20 | Co-locate tests with source | SHOULD | Visible alongside code; short imports |
| 21 | Test utilities in `testing/` | CONSIDER | Keep test deps out of production code |
| 22 | `deno.lock` for reproducibility | SHOULD | Exact versions + hashes; commit to VCS |
| 23 | `jsr:` over `npm:` | CONSIDER | Native registry; TypeScript support |
| 24 | Vendor for offline builds | CONSIDER | Self-contained; no network needed |
| 25 | Workspaces for monorepos | CONSIDER | Shared config; independent packages |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for ESM-only (ID-08), named exports (ID-07), `const`/`let` (ID-01), magic values (ID-11)
- **API Design**: See `02-api-design.md` for module responsibility (ID-06), barrel files (ID-08), no side effects (ID-09), export at declaration (ID-10)
- **Error Handling**: See `03-error-handling.md` for validation at boundaries (ID-23, ID-24)
- **Values & References**: See `04-values-references.md` for `Object.freeze()` for constants (ID-19)
- **Type Discipline**: See `05-type-discipline.md` for JSDoc `@typedef` (ID-17), `@enum` (ID-18), Deno LSP (ID-20)
- **Functions & Closures**: See `06-functions-closures.md` for module scope (ID-15), pure functions (ID-28–29)
- **Performance**: See `08-performance.md` for tree shaking (ID-30), side-effect-free modules (ID-31)
- **Anti-Patterns**: See `09-anti-patterns.md` for ID-29 (`for...in`), ID-33 (CommonJS), ID-32 (IIFEs in ESM)
- **Deno**: See `12-deno/01-runtime-basics.md` for runtime details, permissions, and `deno.json` deep dive
- **No-Node Boundary**: See `14-no-node-boundary.md` for why no `package.json`, `node_modules`, or npm scripts

---

## External References

- [Deno Manual — Configuration](https://docs.deno.com/runtime/fundamentals/configuration/)
- [Deno Manual — Workspaces](https://docs.deno.com/runtime/fundamentals/workspaces/)
- [Deno Manual — Testing](https://docs.deno.com/runtime/fundamentals/testing/)
- [JSR Registry](https://jsr.io/)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
