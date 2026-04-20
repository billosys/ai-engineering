# Biome Setup

Installation, configuration, CLI commands, editor integration, Deno coexistence, VCS integration, and migration from ESLint/Prettier. Biome is a unified linter + formatter in a single Rust-based binary — it replaces ESLint + Prettier with one tool. This chapter covers the setup you do once; lint rules are in 13-02, formatting options in 13-03. Grounded in Biome documentation concept cards.

Target environment: **Deno** + **Biome**, **ESM-only**, **no TypeScript** (plain JS with JSDoc where needed).

---

## ID-01: Biome Replaces ESLint + Prettier — One Tool for Lint and Format

**Strength**: SHOULD

**Summary**: Biome combines linting, formatting, and import organization in a single binary. It is significantly faster than ESLint + Prettier and produces 97%+ Prettier-compatible output.

**What Biome does**:
- Lints JS, TS, JSX, TSX, JSON, CSS, GraphQL (200+ rules)
- Formats JS, TS, JSX, TSX, JSON, CSS, GraphQL, HTML
- Organizes imports
- All in one `biome check` command

**What Biome does NOT do**:
- Type checking — use `deno check` for that
- Test running — use `deno test`
- Module resolution — use Deno's runtime

**Rationale**: Running ESLint + Prettier requires two tools, two configs, two sets of plugins, and careful coordination to avoid conflicts. Biome eliminates this complexity. It is built in Rust and is an order of magnitude faster than Prettier on most workloads (Biome docs).

---

## ID-02: Biome Alongside Deno — The Division of Labor

**Strength**: SHOULD

**Summary**: Use Biome for linting and formatting. Use Deno for type-checking, testing, and running. They complement each other.

| Concern | Tool | Config |
|---------|------|--------|
| Linting | **Biome** | `biome.json` |
| Formatting | **Biome** | `biome.json` |
| Type checking | **Deno** | `deno.json` (`compilerOptions.checkJs`) |
| Testing | **Deno** | `deno test` |
| Running | **Deno** | `deno run` |
| Import resolution | **Deno** | `deno.json` (`imports`) |
| Tasks | **Deno** | `deno.json` (`tasks`) |

**The rule**: Omit `lint` and `fmt` from `deno.json` when using Biome. Having both Deno and Biome lint/format the same files creates conflicts and confusion about which tool "wins."

**Rationale**: Deno's built-in `deno lint` and `deno fmt` are good defaults for projects that want zero additional tools. When you want Biome's broader rule set, unified `check` command, or Prettier-compatible formatting, use Biome for lint/fmt and Deno for everything else (Deno configuration docs; Biome docs).

**See also**: `12-deno/01-runtime-basics.md` ID-13, `12-deno/03-task-runner.md` ID-08

---

## ID-03: When to Use Deno's Built-In Tools vs Biome

**Strength**: SHOULD

**Summary**: Use Deno's built-in lint/fmt if you want zero extra tools. Use Biome if you want broader rules, Prettier compat, or unified lint+format.

| Factor | Deno built-in | Biome |
|--------|--------------|-------|
| Installation | None (ships with Deno) | Separate binary |
| Config | `deno.json` | `biome.json` |
| Lint rules | ESLint-subset (~100) | 200+ rules, multiple domains |
| Formatter | dprint engine | Prettier-compatible (97%+) |
| Speed | Fast | Faster |
| CSS/GraphQL | No | Yes |
| Import organizing | No | Yes |
| Editor extension | Deno LSP (built-in) | `biomejs.biome` (separate) |

**This project uses Biome** because the lykn project benefits from Biome's broader rule set and Prettier-compatible output. Both are legitimate choices — pick one and be consistent.

---

## ID-04: Install Biome — Standalone Binary, No npm Required

**Strength**: MUST

**Summary**: Install Biome as a standalone binary. No Node.js or npm required.

```sh
# Homebrew (macOS/Linux)
brew install biome

# Standalone binary (any platform)
curl -fsSL https://biomejs.dev/install.sh | sh

# Verify installation
biome --version
```

**Alternative** (if the project already uses npm for some dependencies):
```sh
npm i -D -E @biomejs/biome
npx @biomejs/biome --version
```

**In Deno projects** (via npm specifier):
```sh
deno run npm:@biomejs/biome -- --version
```

**Always pin the version** (`-E` / `--save-exact` for npm) to ensure consistent behavior across the team.

**Rationale**: Biome is a single binary with no runtime dependencies. The standalone installation keeps the Deno project free of `node_modules`. Use `brew` or the install script for the cleanest setup (Biome docs).

---

## ID-05: Initialize Config — `biome init`

**Strength**: SHOULD

**Summary**: Run `biome init` once to generate a starter `biome.json` at the project root.

```sh
biome init
# Creates biome.json with formatter, linter, and assist enabled
```

**Rationale**: `biome init` generates a minimal, correct starting config. All three tools (formatter, linter, assist/import organizer) are enabled by default. Customize from here rather than writing `biome.json` from scratch (Biome docs).

---

## ID-06: `biome.json` — The Config File

**Strength**: MUST

**Summary**: `biome.json` at the project root configures all Biome behavior. One file replaces `.eslintrc` + `.prettierrc`.

```jsonc
// biome.json — recommended starter for a Deno plain-JS project
{
  "$schema": "https://biomejs.dev/schemas/2.0.0/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true,
    "defaultBranch": "main"
  },
  "files": {
    "includes": ["**", "!!**/dist", "!!**/vendor"]
  },
  "formatter": {
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  },
  "javascript": {
    "formatter": {
      // These match both the project's conventions and Biome's defaults.
      // Shown explicitly for clarity; omitting them produces the same output.
      "quoteStyle": "double",
      "semicolons": "always",
      "trailingCommas": "all"
    }
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true
    }
  }
}
```

**Key structure**:
- `formatter` — global formatting options (indent, line width)
- `javascript.formatter` — JS/TS-specific overrides (quotes, semicolons)
- `linter` — linting options and rules
- `files` — which files to process
- `vcs` — Git integration
- `$schema` — enables editor autocompletion

**File formats**: `biome.json` (strict JSON) or `biome.jsonc` (JSON with comments).

**Rationale**: The `$schema` field enables autocomplete in VS Code. The `vcs` section enables `.gitignore` respect and VCS-aware commands. The `files` section excludes build output and vendored code (Biome configuration docs).

---

## ID-07: `files.includes` and `files.ignore` — Control Which Files Biome Processes

**Strength**: SHOULD

**Summary**: Use glob patterns to include/exclude files from Biome processing.

```jsonc
{
  "files": {
    "includes": [
      "**",
      "!**/*.generated.js",
      "!!**/dist",
      "!!**/vendor",
      "!!**/node_modules"
    ]
  }
}
```

**Negation semantics** (differs from `.gitignore` where `!` means re-include):
- `!pattern` — excludes from lint/format but keeps the file indexed (for import resolution and type inference)
- `!!pattern` — fully excludes from all operations including indexing

**Rationale**: `!!` double-negation fully excludes build output and vendored code. Single `!` is for files you don't want to lint/format but that other files import from. Biome always ignores `package-lock.json`, `yarn.lock`, and similar lock files automatically (Biome file inclusion docs).

---

## ID-08: Configuration File Resolution

**Strength**: SHOULD

**Summary**: Biome searches for `biome.json` starting from the working directory, walking up to the root.

**Search order**:
1. `biome.json` → `biome.jsonc` → `.biome.json` → `.biome.jsonc`
2. Starting from CWD, then parent directories upward
3. Falls back to built-in defaults if nothing found

**Override**: `biome check --config-path=./custom/biome.json`

**Rationale**: The upward search means you can place `biome.json` at the project root and it will be found from any subdirectory. In monorepos, nested `biome.json` files override the root for their directory subtree (Biome configuration resolution docs).

---

## ID-09: `extends` for Shared Configuration

**Strength**: CONSIDER

**Summary**: Inherit base configuration from a parent config or an npm package.

```jsonc
// Inherit from monorepo root
{ "extends": "//" }

// Inherit from a shared npm package
{ "extends": ["@myorg/biome-config/biome"] }

// Inherit from a relative file
{ "extends": ["../base-biome.json"] }
```

**Rules**:
- Array entries processed in order; later entries override earlier ones
- Extended configs cannot themselves extend further (no chaining)
- `"//"` is the monorepo microsyntax — inherits from the nearest ancestor config

**Rationale**: Shared configs enforce consistency across multiple projects or workspace members. The `"//"` syntax is Biome's built-in monorepo inheritance pattern (Biome extends docs).

---

## ID-10: `biome check` — Lint + Format in One Pass

**Strength**: MUST

**Summary**: `biome check` runs linting, formatting, and import organization together. This is the primary command.

```sh
# Check all files (report violations, don't modify)
biome check

# Check a specific directory
biome check ./src

# Check and auto-fix + format in one pass
biome check --write

# Check only staged files (for pre-commit hooks)
biome check --staged

# Check only files changed from the default branch
biome check --changed
```

**Rationale**: `biome check` replaces running `eslint` and `prettier --check` separately. One command, one pass, one set of diagnostics. Use `--write` during development to auto-fix; use without `--write` (or use `biome ci`) in CI to report violations (Biome check command docs).

---

## ID-11: `biome check --write` — Auto-Fix and Format

**Strength**: SHOULD

**Summary**: `--write` applies safe lint fixes and formatting to files in place.

```sh
# Fix everything Biome can fix safely
biome check --write

# Fix + apply unsafe fixes too (may change semantics)
biome check --write --unsafe
```

**Safe vs unsafe fixes**: Safe fixes never change program behavior (formatting, removing unused imports). Unsafe fixes may change semantics (e.g., simplifying a boolean expression). `--write` applies only safe fixes; `--write --unsafe` applies both.

**Rationale**: `--write` is the development workflow command — format and fix as you go. For CI, use `biome ci` (ID-12) which is read-only (Biome check command docs).

**See also**: `13-biome/02-lint-rules.md` for safe vs unsafe fix classification

---

## ID-12: `biome ci` — CI Mode

**Strength**: SHOULD

**Summary**: `biome ci` is the CI-optimized read-only check. It reports violations as errors (including format violations).

```sh
# CI mode — errors on any violation, no fixes applied
biome ci

# CI mode with specific directory
biome ci ./src
```

**CI-specific features**:
- Reports formatting violations as errors (not just warnings)
- Outputs GitHub PR annotations automatically
- Supports `--reporter=gitlab` for GitLab code quality reports
- With VCS enabled, `--changed` is automatic (not `--staged`, which has no meaning in CI)
- Controls thread count for resource management

**GitHub Actions**:
```yaml
- uses: biomejs/setup-biome@v2
  with:
    version: latest
- run: biome ci .
```

**Rationale**: `biome ci` is distinct from `biome check` because it treats formatting violations as errors and never modifies files. It is the correct command for CI pipelines — `biome check` without `--write` would also work but `biome ci` is optimized for the CI context (Biome CI command docs).

**See also**: `12-deno/03-task-runner.md` ID-07, ID-19

---

## ID-13: `biome format` — Format Only

**Strength**: SHOULD

**Summary**: Run only the formatter, without linting. Useful when you want to format without triggering lint diagnostics.

```sh
# Format and write
biome format --write

# Format a specific directory
biome format --write ./src

# Check formatting without writing (CI mode)
biome format ./src
```

**Rationale**: `biome format` is a subset of `biome check`. Use it when you want to format code without seeing lint violations — for example, when formatting generated code that you don't lint (Biome docs).

---

## ID-14: `biome lint` — Lint Only

**Strength**: CONSIDER

**Summary**: Run only the linter, without formatting. `--write` applies safe fixes.

```sh
# Lint with safe auto-fixes
biome lint --write

# Lint without fixing (report only)
biome lint

# Lint with unsafe fixes too
biome lint --write --unsafe
```

**Rationale**: `biome lint` is the other subset of `biome check`. Use it when you want to see lint violations without reformatting — for example, when reviewing code that is already formatted (Biome docs).

---

## ID-15: VS Code — Biome Extension + Deno LSP Coexistence

**Strength**: SHOULD

**Summary**: Install the `biomejs.biome` extension and configure VS Code so Biome handles formatting/linting and Deno LSP handles type intelligence.

```jsonc
// .vscode/settings.json — complete Biome + Deno setup
{
  // Deno LSP — type-checking, autocomplete, hover, go-to-definition
  "deno.enable": true,
  "deno.lint": false,           // Biome handles linting, not Deno

  // Biome — formatting, linting, import organization
  "editor.defaultFormatter": "biomejs.biome",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.biome": "explicit",
    "source.organizeImports.biome": "explicit"
  },

  // Per-language formatter overrides (ensures Biome for all file types)
  "[javascript]": {
    "editor.defaultFormatter": "biomejs.biome"
  },
  "[json]": {
    "editor.defaultFormatter": "biomejs.biome"
  }
}
```

**Division of labor in the editor**:
- **Biome extension** (`biomejs.biome`): formatting on save, lint diagnostics, quick fixes, import organization
- **Deno extension** (`denoland.vscode-deno`): autocomplete, hover types, go-to-definition, type error diagnostics

**Critical setting**: `"deno.lint": false` — without this, both Deno and Biome produce lint diagnostics, some overlapping and some conflicting. Disabling Deno's linter defers all lint work to Biome while preserving Deno's type intelligence.

**Rationale**: Both extensions communicate with their respective daemons (Biome daemon, Deno LSP). They handle different concerns and do not conflict when configured correctly (Biome docs; Deno docs).

---

## ID-16: Omit `lint` and `fmt` from `deno.json` When Using Biome

**Strength**: MUST

**Summary**: When Biome handles linting and formatting, remove the `lint` and `fmt` fields from `deno.json` to avoid confusion.

```jsonc
// Good — deno.json when using Biome
{
  "imports": { "@std/assert": "jsr:@std/assert@^1.0.0" },
  "tasks": {
    "check": "biome ci && deno check **/*.js && deno test --allow-all"
  },
  "compilerOptions": { "checkJs": true, "strict": true }
  // No "lint" or "fmt" fields — Biome handles those
}

// Bad — lint/fmt in deno.json AND biome.json
{
  "lint": { "rules": { "tags": ["recommended"] } },  // conflicts with biome.json
  "fmt": { "lineWidth": 100 }                         // conflicts with biome.json
}
```

**Rationale**: Having both `deno.json` lint/fmt and `biome.json` creates ambiguity — which tool's rules apply? Which formatter wins on save? Remove the source of conflict entirely (Deno configuration docs).

**See also**: `12-deno/01-runtime-basics.md` ID-13, `12-deno/03-task-runner.md` ID-08

---

## ID-17: Wire Biome into `deno task`

**Strength**: SHOULD

**Summary**: Call Biome from `deno task` definitions for the development and CI workflows.

```jsonc
// deno.json
{
  "tasks": {
    "lint": "biome check",
    "lint:fix": "biome check --write",
    "fmt": "biome format --write",
    "check": "biome ci && deno check **/*.js && deno test --allow-all",
    "ci": "biome ci && deno check **/*.js && deno test --allow-all --parallel"
  }
}
```

```sh
# Development workflow
deno task lint:fix   # fix + format
deno task check      # full quality gate

# CI workflow
deno task ci
```

**Rationale**: Wrapping Biome in `deno task` keeps the developer workflow unified under one command runner. The `check` task chains `biome ci` (lint + fmt) → `deno check` (types) → `deno test` (tests) — the complete quality gate (Biome docs; Deno task docs).

**See also**: `12-deno/03-task-runner.md` ID-07, ID-08

---

## ID-18: VCS-Aware Processing — Only Lint/Format Changed Files

**Strength**: CONSIDER

**Summary**: With VCS integration enabled, Biome can process only files that have changed from the default branch.

```jsonc
// biome.json — enable VCS integration
{
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true,
    "defaultBranch": "main"
  }
}
```

```sh
# Only files changed from main
biome check --changed

# Only staged files (for pre-commit)
biome check --staged

# Override the comparison branch
biome check --since=develop
```

**Rationale**: VCS-aware processing speeds up large projects by skipping unchanged files. `--staged` is essential for pre-commit hooks — only check what's about to be committed. `useIgnoreFile: true` makes Biome respect `.gitignore` patterns (Biome VCS integration docs).

---

## ID-19: Git Hooks — Pre-Commit Lint and Format

**Strength**: CONSIDER

**Summary**: Run Biome on staged files before every commit to catch issues early.

```sh
# Simple pre-commit hook (.git/hooks/pre-commit)
#!/bin/sh
biome check --staged --write --files-ignore-unknown=true --no-errors-on-unmatched
git add -u  # re-stage any files that were fixed
```

**For more robust setups**, use Lefthook, Husky + lint-staged, or the `pre-commit` Python tool — all of which have Biome integrations. See the Biome git hooks documentation for configuration examples.

**Key flags for hooks**:
- `--staged` — only process staged files
- `--files-ignore-unknown=true` — skip file types Biome doesn't support
- `--no-errors-on-unmatched` — don't fail if no files match

**Rationale**: Pre-commit hooks prevent un-linted/unformatted code from entering the repository. `--staged` ensures only the files being committed are checked, not the entire project (Biome git hooks docs).

---

## ID-20: Migrate from ESLint — `biome migrate eslint`

**Strength**: CONSIDER

**Summary**: Biome can automatically convert ESLint configuration to equivalent Biome rules.

```sh
# Read .eslintrc and write equivalent biome.json rules
biome migrate eslint --write

# Also migrate "inspired" rules (Biome's intentional deviations)
biome migrate eslint --write --include-inspired
```

**What it migrates**: `.eslintrc` (legacy and flat config), `.eslintignore`, TypeScript ESLint, ESLint React, JSX A11y, ESLint Unicorn plugins.

**Limitations**: Output sets `recommended: false` and enables individual rules explicitly. YAML/TOML configs are not supported. Some rules have intentional behavioral differences.

**Rationale**: Migration automates the tedious rule-by-rule translation. Review the output — some Biome rules are stricter or broader than their ESLint equivalents. Biome uses `camelCaseRuleName` vs ESLint's `kebab-case-rule-name` (Biome ESLint migration docs).

---

## ID-21: Migrate from Prettier — `biome migrate prettier`

**Strength**: CONSIDER

**Summary**: Biome can convert Prettier configuration to equivalent Biome formatter options.

```sh
# Read .prettierrc and write equivalent biome.json formatter settings
biome migrate prettier --write
```

**Compatibility**: 97%+ output compatibility with Prettier, verified through the formal Prettier Challenge. A small set of intentional divergences remain — see `13-biome/03-formatting.md` for details.

**Rationale**: For most codebases, migrating from Prettier produces identical output. Run `biome format --write` after migration and compare the diff — minimal or no changes are expected (Biome Prettier compatibility docs).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Biome replaces ESLint + Prettier | SHOULD | One tool, one binary, one config |
| 02 | Biome + Deno division of labor | SHOULD | Biome: lint/fmt. Deno: types/test/run |
| 03 | Deno built-in vs Biome | SHOULD | Zero-tool vs broader rules — pick one |
| 04 | Standalone binary install | MUST | No npm required; brew, curl, or binary |
| 05 | `biome init` | SHOULD | Generate starter config |
| 06 | `biome.json` config | MUST | $schema, formatter, linter, vcs, files |
| 07 | `files.includes` / `!` / `!!` | SHOULD | `!` = skip lint/fmt; `!!` = fully exclude |
| 08 | Config file resolution | SHOULD | Walks up from CWD; `--config-path` override |
| 09 | `extends` for shared config | CONSIDER | `"//"` for monorepo; npm packages for cross-project |
| 10 | `biome check` | MUST | Lint + format + organize in one pass |
| 11 | `biome check --write` | SHOULD | Auto-fix + format; `--unsafe` for semantic fixes |
| 12 | `biome ci` | SHOULD | CI-optimized; format violations = errors |
| 13 | `biome format` | SHOULD | Format only, no lint |
| 14 | `biome lint` | CONSIDER | Lint only, no format |
| 15 | VS Code Biome + Deno LSP | SHOULD | `deno.lint: false`; per-language formatter overrides |
| 16 | No lint/fmt in `deno.json` | MUST | Remove to avoid conflicts with biome.json |
| 17 | Biome in `deno task` | SHOULD | `biome ci` in the `check` and `ci` tasks |
| 18 | VCS-aware `--changed`/`--staged` | CONSIDER | Skip unchanged files; essential for hooks |
| 19 | Git pre-commit hooks | CONSIDER | `--staged --write` catches issues early |
| 20 | `biome migrate eslint` | CONSIDER | Auto-converts ESLint rules to Biome |
| 21 | `biome migrate prettier` | CONSIDER | 97%+ compat; minimal diff expected |

### CLI Quick Reference

| Command | Purpose |
|---------|---------|
| `biome init` | Generate starter `biome.json` |
| `biome check` | Lint + format check (report only) |
| `biome check --write` | Lint fix + format (modify files) |
| `biome check --staged` | Check staged files only |
| `biome check --changed` | Check files changed from default branch |
| `biome ci` | CI mode (errors on all violations) |
| `biome format --write` | Format only |
| `biome lint --write` | Lint + safe fixes only |
| `biome migrate eslint --write` | Convert ESLint config |
| `biome migrate prettier --write` | Convert Prettier config |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for naming (ID-12), `===` (ID-02), `const`/`let` (ID-01) — rules Biome enforces
- **Type Discipline**: See `05-type-discipline.md` for `deno check` integration (ID-20) — the type-checking that Biome does not do
- **Project Structure**: See `10-project-structure.md` for `deno.json` placement (ID-15), `biome.json` in root (ID-02)
- **Runtime Basics**: See `12-deno/01-runtime-basics.md` for `deno.json` config (ID-13), Deno lint/fmt as alternatives
- **Task Runner**: See `12-deno/03-task-runner.md` for `biome ci` in tasks (ID-07, ID-08), the `check` quality gate (ID-07)
- **Lint Rules**: See `13-biome/02-lint-rules.md` for rule groups, domains, severity, suppressions
- **Formatting**: See `13-biome/03-formatting.md` for formatter options, Prettier compat, divergences

---

## External References

- [Biome — Getting Started](https://biomejs.dev/guides/getting-started/)
- [Biome — Configuration](https://biomejs.dev/reference/configuration/)
- [Biome — CLI Reference](https://biomejs.dev/reference/cli/)
- [Biome — VS Code Extension](https://biomejs.dev/reference/vscode/)
- [Biome — ESLint Migration](https://biomejs.dev/guides/migrate-eslint-prettier/)
- [Biome — Git Hooks](https://biomejs.dev/guides/integrate-in-vcs/)
