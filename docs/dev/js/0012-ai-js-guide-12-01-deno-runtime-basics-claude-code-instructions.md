# ai-js Guide 12-01: Deno Runtime Basics — Claude Code Instructions

## Context

We're building `ai-js`, a repo of curated JavaScript guides that Claude
Code reads via a SKILL.md entry point to produce consistently high-quality
JS code. This is modeled on our `ai-rust` repo.

Guides 01–11 are complete. Now we're writing the Deno sub-guide series
(Guide 12), which has four chapters:

| Chapter | Slug | Scope |
|---------|------|-------|
| 12-01 | `12-deno/01-runtime-basics.md` | Runtime model, permissions, APIs, config |
| 12-02 | `12-deno/02-testing.md` | `Deno.test()`, assertions, async tests, mocking |
| 12-03 | `12-deno/03-task-runner.md` | `deno task`, scripts, dev workflows |
| 12-04 | `12-deno/04-publishing.md` | JSR, `deno publish`, package metadata |

This prompt is for **12-01: Runtime Basics** — the foundational chapter
that the other three build on. It covers everything a developer needs
to know about Deno as a runtime: the security model, the permission
system, the Deno namespace APIs, Web Platform API support, `deno.json`
configuration, module resolution, `deno check` for type checking,
`deno doc` for documentation, and the key differences from Node.js
that affect how you write code.

Multiple existing guides reference this chapter:
- Guide 02: "Deno-specific API patterns"
- Guide 03: "Deno-specific error handling and permissions"
- Guide 05: "`deno check`, LSP configuration, and `.d.ts` wiring"
- Guide 07: "Deno-specific async APIs"
- Guide 10: "runtime details, permissions, and `deno.json` deep dive"

This chapter must deliver on all of those promises.

The target environment is:
- **Deno** (not Node.js — no `require()`, no `node_modules`, no npm scripts)
- **Biome** for linting and formatting (not ESLint, not Prettier)
- **ESM-only** (`import`/`export`, no CommonJS)
- **No TypeScript** (plain JS with JSDoc where needed)
- This is the JS used in the **lykn** project (s-expression syntax for JS)

## The full ai-js guide list

Use these numbers and slugs for all cross-references.

| # | Slug | Title |
|---|------|-------|
| 01 | `01-core-idioms.md` | Core Idioms |
| 02 | `02-api-design.md` | API Design |
| 03 | `03-error-handling.md` | Error Handling |
| 04 | `04-values-references.md` | Values & References |
| 05 | `05-type-discipline.md` | Type Discipline (without TypeScript) |
| 06 | `06-functions-closures.md` | Functions & Closures |
| 07 | `07-async-concurrency.md` | Async & Concurrency |
| 08 | `08-performance.md` | Performance |
| 09 | `09-anti-patterns.md` | Anti-Patterns |
| 10 | `10-project-structure.md` | Project Structure |
| 11 | `11-documentation.md` | Documentation |
| 12 | `12-deno/` | Deno (multi-part sub-guide) |
|    | `12-deno/01-runtime-basics.md` | Runtime Basics |
|    | `12-deno/02-testing.md` | Testing |
|    | `12-deno/03-task-runner.md` | Task Runner |
|    | `12-deno/04-publishing.md` | Publishing |
| 13 | `13-biome/` | Biome (multi-part sub-guide) |
|    | `13-biome/01-setup.md` | Setup |
|    | `13-biome/02-lint-rules.md` | Lint Rules |
|    | `13-biome/03-formatting.md` | Formatting |
| 14 | `14-no-node-boundary.md` | No-Node Boundary |

## Reference material

You have a concept card library under `concept-cards/`. These are your
authoritative references — the guide must be grounded in what the cards
say, not in general knowledge.

### Source priority

For this guide, the **Deno concept cards are the primary authority**.
The JS language cards are secondary — use them only for language
semantics that interact with Deno's runtime (e.g., ESM module
resolution, strict mode).

1. `concept-cards/deno/` — **PRIMARY**. Deno-specific behavior,
   APIs, configuration, and conventions.
2. `concept-cards/exploring-js/` — Secondary. ESM module system,
   strict mode, and language semantics that Deno relies on.
3. `concept-cards/js-definitive-guide/` — Secondary. Web Platform
   APIs that Deno implements.
4. Other sources as needed for specific language interactions.

### Concept cards to read for this guide

Read these cards before writing. This is not exhaustive — if you find
related cards while reading, use them too.

**Deno overview and architecture**:
- `deno/deno.md`
- `deno/deno-architecture.md`
- `deno/deno-stability-and-releases.md`
- `deno/deno-cli.md`
- `deno/deno-run.md`

**Security and permissions**:
- `deno/deno-security-model.md`
- `deno/deno-permissions-system.md`
- `deno/deno-sandbox.md`
- `deno/sandbox-security.md`

**Deno namespace APIs**:
- `deno/deno-namespace-apis.md`
- `deno/deno-api-overview.md`
- `deno/deno-resources.md`

**Web Platform APIs in Deno**:
- `deno/deno-web-platform-apis.md`
- `deno/web-platform-apis.md`

**HTTP server**:
- `deno/deno-http-server.md`
- `deno/deno-serve.md`

**Configuration**:
- `deno/deno-configuration.md`
- `deno/deno-import-maps.md`
- `deno/deno-import-attributes.md`
- `deno/deno-workspaces.md`
- `deno/environment-variables-and-contexts.md`

**Module system and resolution**:
- `deno/ecmascript-modules.md`
- `deno/deno-npm-specifiers.md`
- `deno/deno-package-json-support.md`

**TypeScript/JSDoc/type checking**:
- `deno/deno-typescript-support.md`

**Node.js compatibility**:
- `deno/deno-node-api-compatibility.md`
- `deno/deno-node-compatibility.md`

**Standard library**:
- `deno/deno-standard-library.md`

**Compilation and deployment**:
- `deno/deno-compile.md`
- `deno/deno-debugging.md`

**FFI and WebAssembly**:
- `deno/deno-ffi.md`
- `deno/webassembly-support.md`

**ESM semantics (from JS language cards)**:
- `exploring-js/ecmascript-module.md`
- `exploring-js/module-characteristics.md`
- `exploring-js/scripts-vs-modules.md`
- `exploring-js/import-meta.md`
- `exploring-js/dynamic-import.md`
- `exploring-js/top-level-await.md`
- `js-definitive-guide/es6-module-system.md`

## Structural template

Follow the same format as the existing guides (01–11):

Each idiom entry has:
```
## ID-XX: [Title]

**Strength**: MUST | SHOULD | CONSIDER

**Summary**: One sentence.

[Code examples with // Good and // Bad labels]

**Rationale**: Why this matters. Cite concept card sources.

**See also**: Cross-references to other IDs or guides
```

End with:
- Quick Reference Table
- Related Guidelines — use the format from Guide 09: list specific
  ID numbers per guide for direct navigation.
- External References

## Proposed idiom list

This is a starting outline — adjust based on what the concept cards
emphasize. Add idioms if the cards reveal important patterns. Remove
or merge if redundant. Aim for 25-35 idioms.

### Security model and permissions

1. Deno is secure by default — no file, network, or env access
   without explicit permission (MUST)
2. Use granular permissions — `--allow-read=./data` not
   `--allow-read` (SHOULD)
3. Permission flags for common operations: `--allow-net`,
   `--allow-read`, `--allow-write`, `--allow-env`, `--allow-run`
   (MUST)
4. Request permissions at runtime with `Deno.permissions.request()`
   (CONSIDER)
5. `--allow-all` / `-A` only for development — never in production
   (MUST)

### Deno namespace APIs

6. File I/O: `Deno.readTextFile`, `Deno.writeTextFile`,
   `Deno.readFile`, `Deno.open` — async by default (SHOULD)
7. `Deno.serve()` for HTTP servers — the modern replacement for
   `Deno.listen` + manual request handling (SHOULD)
8. `Deno.Command` for subprocesses — replaces `Deno.run` (deprecated)
   (SHOULD)
9. `Deno.env` for environment variables (SHOULD)
10. `Deno.cwd()`, `Deno.execPath()`, `Deno.mainModule` — runtime
    introspection (CONSIDER)
11. `Deno.exit()` — prefer letting the event loop drain naturally
    (SHOULD)

### Web Platform APIs

12. `fetch()` is built-in — no import needed (MUST)
13. Web APIs available: `URL`, `URLSearchParams`, `Headers`,
    `Request`, `Response`, `AbortController`, `crypto`,
    `TextEncoder`/`TextDecoder`, `structuredClone`, `performance`,
    `WebSocket`, `console`, `setTimeout`/`setInterval` (SHOULD)
14. `import.meta.url` and `import.meta.main` — URL-based module
    identity (SHOULD)

### Configuration — `deno.json`

15. `deno.json` is auto-detected — one file replaces
    `package.json` + `tsconfig.json` + `.eslintrc` + `.prettierrc`
    (SHOULD — references 10 ID-15)
16. `imports` field for import maps — bare specifier resolution
    (SHOULD — references 10 ID-16)
17. `compilerOptions` for JSDoc type checking — `checkJs`, `strict`
    (SHOULD — references 05 ID-20)
18. `tasks` field for scripts — `deno task dev`, `deno task test`
    (SHOULD — forward-references 12-03)

### Module resolution

19. File extensions are required on local imports (MUST)
20. `jsr:` specifiers for JSR packages, `npm:` for npm packages —
    no install step (SHOULD)
21. `node:` specifiers for Node.js built-in API compatibility
    (CONSIDER)
22. Remote imports via HTTPS URLs — cached locally (CONSIDER)

### Type checking and documentation

23. `deno check` for type checking JS with JSDoc annotations
    (SHOULD — references 05 ID-20)
24. `deno doc` generates API documentation from JSDoc (SHOULD)
25. Deno LSP provides autocomplete, hover docs, and type errors
    in editors (SHOULD)

### Node.js compatibility layer

26. `npm:` specifier for using npm packages without `node_modules`
    (SHOULD)
27. Node.js built-in API shims — `node:fs`, `node:path`, etc. —
    available but prefer Deno/Web APIs (CONSIDER)
28. `--node-modules-dir` for packages that need it (rare)
    (CONSIDER)

### Compilation and single-binary output

29. `deno compile` for standalone executables — embed dependencies
    into a single binary (CONSIDER)

### Standard library

30. `@std/` packages on JSR — assert, path, fs, http, testing,
    etc. (SHOULD)
31. Import via `jsr:@std/assert` — no vendoring needed (SHOULD)

### Key differences from Node.js

32. No `require()`, no `module.exports`, no `__dirname`, no
    `__filename` — ESM only (MUST — references 09 ID-33)
33. `import.meta.dirname` and `import.meta.filename` replace
    `__dirname` and `__filename` (SHOULD)
34. No `process` global — use `Deno.env`, `Deno.args`, `Deno.exit()`
    (SHOULD)
35. No `Buffer` — use `Uint8Array` and `TextEncoder`/`TextDecoder`
    (SHOULD)

## Boundaries with other chapters and guides

**Guide 10 (Project Structure)** already covers:
- `deno.json` layout and placement (10 ID-15)
- Import maps for aliases (10 ID-16)
- Workspaces (10 ID-25)
- Lock files (10 ID-22)
- Vendoring (10 ID-24)

This chapter covers the **runtime behavior and API surface** of these
features, not the project organization aspects. Guide 10 says *where*
`deno.json` goes and what fields exist; this chapter says *how* each
field affects runtime behavior.

**Guide 05 (Type Discipline)** already covers:
- JSDoc annotation syntax (05 ID-16–19)
- `// @ts-check` and `deno check` integration (05 ID-20)

This chapter covers `deno check` as a command and `deno doc` as a
tool, not the JSDoc syntax itself.

**12-02 (Testing)** will cover:
- `Deno.test()` API, assertion library, async tests, mocking, BDD

**12-03 (Task Runner)** will cover:
- `deno task` in depth, script patterns, watch mode, dev workflows

**12-04 (Publishing)** will cover:
- JSR publishing, `deno publish`, package metadata, versioning

**Do NOT cover testing, task runner, or publishing in this chapter.**
This chapter is the runtime foundation. Cross-reference the other
chapters for those topics.

## Output

Save as: `guides/12-deno/01-runtime-basics.md` in the `ai-js` repo.

## Quality bar

- The Deno concept cards are the primary source for this guide.
  Cite them specifically.
- Code examples must use Deno APIs correctly — `Deno.readTextFile`
  not `fs.readFile`, `Deno.serve()` not `http.createServer()`.
- Permission examples should show realistic, granular permissions
  — not just `--allow-all`.
- The `Deno.serve()` entry should show the modern API (the simple
  callback pattern), not the older `Deno.listen()` approach.
- The Node.js compatibility section should be honest: Deno supports
  Node.js APIs but prefers Web Platform APIs. Show both when
  relevant, recommend the Deno/Web way.
- `deno.json` coverage should complement Guide 10, not duplicate
  it. Focus on runtime behavior: "what does `compilerOptions.checkJs`
  actually do?" rather than "where does `deno.json` go?"
- This guide should be comprehensive enough that a developer new
  to Deno (but experienced in JS) can use it as a reference for
  all common Deno operations. It's the "Deno cheat sheet" chapter.
- Match the existing guides' terse, direct style.

## What NOT to do

- Don't include `Deno.test()` details — that's 12-02
- Don't include `deno task` patterns — that's 12-03
- Don't include JSR publishing — that's 12-04
- Don't include Biome configuration — that's Guide 13
- Don't include Deno Deploy, Deno KV, or Deno Cron — those are
  hosting/infrastructure features beyond the scope of a JS
  quality guide
- Don't include JSX/TSX support — the target environment is plain JS
- Don't include FFI or WebAssembly beyond a brief mention — these
  are niche use cases
- Don't include Docker or CI/CD patterns — those are operational
- Don't write a Deno tutorial — this is a reference guide for
  developers who already know JS and need Deno-specific patterns
- Don't compare Deno to Node.js extensively — a brief "key
  differences" section is fine, but don't turn the guide into a
  migration document (that's closer to Guide 14's territory)
