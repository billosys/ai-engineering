# Biome Lint Rules

Biome's linter: rule groups, severity, domains, key rules for this project, safe vs unsafe fixes, suppression mechanisms, diagnostics, and advanced features. This chapter covers the *rule system* — 13-01 covers installation and config, 13-03 covers formatting. Grounded in Biome documentation concept cards.

Target environment: **Deno** + **Biome**, **ESM-only**, **no TypeScript** (plain JS with JSDoc where needed).

---

## ID-01: `recommended` Rules Are On by Default

**Strength**: MUST

**Summary**: Biome's `recommended` set is the sensible baseline. It includes stable rules across all groups that the Biome team considers universally valuable.

```jsonc
// biome.json — recommended is the default
{
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true   // this is the default; explicit for clarity
    }
  }
}
```

**What's included**: Stable, non-nursery rules from correctness, suspicious, style, complexity, performance, security, and a11y groups. Style rules default to `warn`; most others default to `error`.

**Rationale**: `recommended` provides a strong baseline without configuration. Start here and customize by enabling additional rules or disabling ones that don't fit your project. It is always on unless explicitly set to `false` (Biome lint rule groups docs).

---

## ID-02: `all` Enables Every Stable Rule

**Strength**: CONSIDER

**Summary**: `"all": true` activates every non-nursery rule — stricter than `recommended`.

```jsonc
{
  "linter": {
    "rules": {
      "all": true,
      "style": {
        "noNonNullAssertion": "off"   // disable individual rules you disagree with
      }
    }
  }
}
```

**Rationale**: `all` is for teams that want maximum strictness and are willing to suppress the rules they consciously disagree with. It is noisier than `recommended` but ensures no rule is missed. New rules added in Biome updates are automatically enabled (Biome lint rule groups docs).

---

## ID-03: `nursery` Rules Are Unstable — Opt In Explicitly

**Strength**: CONSIDER

**Summary**: Nursery rules are incubating and not subject to semver. They can change, be renamed, or be removed without a major version bump.

```jsonc
{
  "linter": {
    "rules": {
      "recommended": true,
      "nursery": {
        "noFloatingPromises": "error",
        "useExhaustiveSwitchCases": "warn"
      }
    }
  }
}
```

**Rationale**: Nursery rules require explicit opt-in on stable releases (they are enabled by default only on nightly builds). Many type-aware and domain-specific rules (e.g., `noFloatingPromises`, `useExhaustiveSwitchCases`) are currently in nursery. Expect breaking changes when upgrading Biome. See ID-09 for enabling types-domain nursery rules specifically (Biome nursery rules docs).

---

## ID-04: Severity Levels — `error`, `warn`, `info`, `off`

**Strength**: SHOULD

**Summary**: Severity controls whether a rule blocks CI, reports informally, or is disabled entirely.

| Level | `biome check` exit code | With `--error-on-warnings` | Notes |
|-------|------------------------|---------------------------|-------|
| `"error"` | Non-zero (fails) | N/A | Blocks CI unconditionally |
| `"warn"` | Zero (passes) | Non-zero (fails) | Advisory by default |
| `"info"` | Zero (passes) | Zero (passes) | Purely informational |
| `"off"` | Rule disabled | N/A | No diagnostic emitted |

`"on"` enables a rule at its **shipped default** severity (which varies by group — style defaults to `warn`, correctness defaults to `error`).

**Rationale**: Use `error` for rules that must block CI. Use `warn` for rules you're adopting gradually. Use `off` to disable rules you've consciously rejected. `--error-on-warnings` promotes all warnings to errors — useful for strict CI gates (Biome rule severity docs).

---

## ID-05: Configure Severity Per-Rule

**Strength**: SHOULD

**Summary**: Override any rule's severity in `biome.json` under its group.

```jsonc
{
  "linter": {
    "rules": {
      "suspicious": {
        "noDoubleEquals": "error"        // short form: severity only
      },
      "style": {
        "useConst": {
          "level": "warn",               // long form: severity + options
          "fix": "safe"
        },
        "noUselessElse": "off"           // disable this rule (example)
      },
      "correctness": {
        "noUnusedVariables": {
          "level": "error",
          "fix": "none"                  // keep diagnostic, suppress auto-fix
        }
      }
    }
  }
}
```

**Short form**: `"ruleName": "error"` — just the severity.
**Long form**: `"ruleName": { "level": "error", "fix": "safe", "options": {...} }` — severity + fix behavior + rule-specific options.

**Rationale**: Per-rule severity lets you adopt rules incrementally — start at `warn`, promote to `error` once the codebase is clean. The `fix` option controls whether auto-fix is `"safe"`, `"unsafe"`, or `"none"` (diagnostic only) (Biome rule severity docs; Biome code fix configuration docs).

---

## ID-06: Rule Groups — Organized by Problem Type

**Strength**: SHOULD

**Summary**: Biome organizes rules into groups by the type of problem they detect.

| Group | Purpose | Default severity |
|-------|---------|-----------------|
| `correctness` | Code guaranteed to be incorrect or useless | `error` |
| `suspicious` | Code likely to be incorrect (softer than correctness) | `error` |
| `style` | Idiomatic, consistent code | `warn` |
| `complexity` | Code that could be simplified | `warn` |
| `performance` | Code that could run faster or use less memory | `error` |
| `security` | Potential security flaws | `error` |
| `a11y` | Accessibility problems | `error` |
| `nursery` | Unstable/incubating rules | varies |

**Configure at group level**:
```jsonc
{
  "linter": {
    "rules": {
      "a11y": "off",           // disable entire group
      "style": "error"         // promote style warnings to errors
    }
  }
}
```

Individual rule config overrides group config.

**Rationale**: Groups let you tune strictness by problem category. Disable `a11y` if you're not building accessible HTML. Promote `style` to `error` for strict code consistency. The group names appear in diagnostic output (e.g., `lint/suspicious/noDebugger`) for quick identification (Biome lint rule groups docs).

---

## ID-07: Rule Naming — `use*` Enforces, `no*` Denies

**Strength**: SHOULD

**Summary**: `use*` rules say "do this." `no*` rules say "don't do this." The prefix signals intent at a glance.

| Prefix | Meaning | Example |
|--------|---------|---------|
| `use*` | Enforce/suggest a pattern | `useConst`, `useExhaustiveSwitchCases` |
| `no*` | Deny/prevent a pattern | `noVar`, `noDoubleEquals`, `noDebugger` |

**Rationale**: Consistent naming makes rules discoverable. When you see `noDoubleEquals` in a diagnostic, you immediately know the fix is to use `===`. When you see `useConst`, you know to change `let` to `const` (Biome lint rules docs).

---

## ID-08: Domains — Rules Grouped by Analysis Capability

**Strength**: SHOULD

**Summary**: Domains group rules by the technology or analysis engine they require, not by problem type.

```jsonc
{
  "linter": {
    "domains": {
      "types": "all",        // type-aware rules (requires JSDoc + checkJs)
      "project": "all"       // project-wide analysis rules (import graph)
    }
  }
}
```

**Available domains**: `types`, `project`, `react`, `solid`, `next`, `vue`, `test`, `drizzle`, `playwright`, `qwik`, `turborepo`.

**A rule belongs to one group but zero or more domains.** Domains can be auto-detected (e.g., `react` from `package.json`).

**Rationale**: Domains separate *what* a rule checks (the group) from *what analysis it needs* (the domain). Most rules need only the source file; `types` rules need type information; `project` rules need the import graph (Biome linter domains docs).

---

## ID-09: `types` Domain — Rules Requiring Type Information

**Strength**: SHOULD

**Summary**: The `types` domain enables rules powered by Biome's type inference engine. For plain JS projects, this requires `checkJs` and JSDoc annotations.

```jsonc
// biome.json
{
  "linter": {
    "domains": {
      "types": "all"    // currently most types-domain rules are nursery; use "all" to enable them
    }
  }
}
```

**Key types-domain rules** (all currently nursery):
- `noFloatingPromises` — unhandled Promise return values
- `noMisusedPromises` — Promises in non-async contexts
- `useAwaitThenable` — `await` on non-Promise values
- `useExhaustiveSwitchCases` — switch missing cases for union discriminants
- `noUnnecessaryConditions` — conditions always true/false by type

**Performance note**: Enabling types-domain rules triggers Biome's Scanner and type inference engine, adding measurable overhead. Only enable if the project has sufficient JSDoc type coverage.

**Rationale**: Since this project uses `checkJs: true` and comprehensive JSDoc (Guide 05), the types domain should be enabled — it catches async bugs and exhaustiveness issues that syntax-only rules cannot. Use `"all"` since all types-domain rules are currently in nursery (Biome types domain docs).

**See also**: `05-type-discipline.md` ID-20, ID-24, ID-25

---

## ID-10: `project` Domain — Cross-File Analysis

**Strength**: CONSIDER

**Summary**: The `project` domain enables rules that analyze the full import graph — unused exports, circular imports, undeclared dependencies.

```jsonc
{
  "linter": {
    "domains": {
      "project": "all"
    }
  }
}
```

**Key project-domain rules**:
- `noUnresolvedImports` — imports pointing to nonexistent modules
- `noUndeclaredDependencies` — imports from packages not in `deno.json`
- `noImportCycles` — circular import detection
- `noPrivateImports` — accessing non-exported internals

**Performance note**: Triggers a full project crawl via the Scanner. Roughly ~2s for ~2k files, ~8s for ~5k files (vs. ~1s without Scanner).

**Rationale**: Project-domain rules catch structural issues that per-file linting misses. The performance cost is acceptable for CI but may slow interactive editing in large projects (Biome project domain docs).

**See also**: `10-project-structure.md` ID-11, ID-12

---

## ID-11: Key Rules — `noDoubleEquals`

**Strength**: MUST

**Summary**: Enforces `===` and `!==` over `==` and `!=`.

```js
// Diagnostic: Use === instead of ==. Unsafe fix available.
if (x == 0) { } // biome: lint/suspicious/noDoubleEquals
// Fix:
if (x === 0) { }
```

**Rationale**: The `==` coercion cascade produces surprising results (09 ID-01). This is the automated safety net for `01-core-idioms.md` ID-02.

---

## ID-12: Key Rules — `noVar`

**Strength**: MUST

**Summary**: Bans `var` declarations. Enforces `const` and `let`.

```js
// Diagnostic: Use let or const instead of var.
var x = 1; // biome: lint/style/noVar
// Fix:
const x = 1;
```

**Rationale**: `var` is function-scoped, hoists to `undefined`, and creates global properties (09 ID-28). This is the automated safety net for `01-core-idioms.md` ID-01.

---

## ID-13: Key Rules — `useConst`

**Strength**: SHOULD

**Summary**: Prefers `const` over `let` when no reassignment occurs.

```js
// Diagnostic: Use const instead of let.
let x = 5;    // x is never reassigned
// Fix:
const x = 5;
```

**Rationale**: `const` communicates intent — this binding will not change (01 ID-01). The fix is safe and automated.

---

## ID-14: Key Rules — `noUnusedVariables` / `noUnusedImports`

**Strength**: SHOULD

**Summary**: Detects variables and imports that are declared but never read.

```js
// Diagnostic: This variable is unused.
const unused = computeExpensive(); // biome: lint/correctness/noUnusedVariables

// Diagnostic: This import is unused.
import { unused } from "./utils.js"; // biome: lint/correctness/noUnusedImports
```

**Rationale**: Unused code is dead weight — it adds confusion, increases bundle size, and may mask bugs where a value was supposed to be used but wasn't. The fix for unused imports is safe (remove them); for unused variables, it's often unsafe (the variable may have side effects) so Biome defaults to `"fix": "none"` for `noUnusedVariables`.

---

## ID-15: Key Rules — Additional High-Value Rules for Plain JS

**Strength**: SHOULD

**Summary**: Curated rules beyond the basics that are particularly valuable for Deno plain-JS projects.

| Rule | Group | What it catches | Guide reference |
|------|-------|----------------|-----------------|
| `noShadowRestrictedNames` | `suspicious` | Shadowing `undefined`, `NaN`, `Infinity`, etc. | 09 ID-12 |
| `useArraySortCompare` | `nursery`* | `.sort()` without comparator (lexicographic trap) | 09 ID-17 |
| `noDebugger` | `suspicious` | `debugger` statements left in code | — |
| `useIsNan` | `correctness` | `x === NaN` (always false) vs `Number.isNaN()` | 05 ID-11 |
| `noCompareNegZero` | `correctness` | `x === -0` vs `Object.is()` | 05 ID-12 |
| `useValidTypeof` | `correctness` | `typeof x === "undefined"` typos | 05 ID-01 |
| `noConsole` | `suspicious` | `console.log` left in production code | — |
| `useNamingConvention` | `style` | Enforces camelCase/PascalCase/UPPER_CASE | 01 ID-12 |

*`useArraySortCompare` may have graduated from nursery in recent Biome versions — verify with `biome lint --list-rules` or the [Biome rules page](https://biomejs.dev/linter/rules/). If it's now in a stable group, no nursery opt-in is needed.

**Configuration example**:
```jsonc
{
  "linter": {
    "rules": {
      "recommended": true,
      "nursery": {
        "useArraySortCompare": "error"
      },
      "suspicious": {
        "noConsole": "warn"
      }
    }
  }
}
```

**Rationale**: These rules automate patterns taught across guides 01, 05, and 09. Enabling them turns manual discipline into automated enforcement (Biome lint rules docs).

---

## ID-16: Safe Fixes — Applied by `biome check --write`

**Strength**: SHOULD

**Summary**: Safe fixes are guaranteed to not change program semantics. They are applied automatically by `--write`.

```sh
# Apply safe fixes only
biome check --write

# In editor: source.fixAll.biome applies safe fixes on save
```

**Examples of safe fixes**: Removing unused imports, replacing `==` with `===`, removing `debugger` statements, adding missing semicolons. Note: `var` → `const`/`let` conversion is classified as safe because Biome only applies it when it can verify that the TDZ behavior change won't affect the code (the `var` was never accessed before its declaration).

**Rationale**: Safe fixes can be applied automatically in CI and on save without human review. They never change what the program does — only how it looks or how it avoids obvious bugs (Biome safe fixes docs).

---

## ID-17: Unsafe Fixes — Applied Only by `--write --unsafe`

**Strength**: SHOULD

**Summary**: Unsafe fixes may change program semantics. They require explicit `--unsafe` and should be reviewed.

```sh
# Apply safe + unsafe fixes
biome check --write --unsafe

# In editor: unsafe fixes appear as individual code actions (not on save)
```

**Examples of unsafe fixes**: Simplifying boolean expressions, adding `_` prefix to unused variables, converting `function` to arrow functions.

**Why a fix is "unsafe"**: It may change runtime behavior (e.g., simplifying `!!x` to `Boolean(x)` when `x` is a Symbol), or it may be harmful during active typing (e.g., adding `_` to a variable you just declared).

**Rationale**: The safe/unsafe split ensures `biome check --write` is always safe for automation. Unsafe fixes require conscious review — they appear in editors as individual code actions, not bulk save-on-type operations (Biome unsafe fixes docs).

---

## ID-18: Inline Suppression — `biome-ignore` with Mandatory Reason

**Strength**: MUST

**Summary**: Suppress a rule for the next line with `// biome-ignore`. A reason is required — bare suppressions are rejected.

```js
// Good — reason explains why the suppression is needed
// biome-ignore lint/suspicious/noDoubleEquals: API returns mixed types, == null is intentional
if (value == null) { /* ... */ }

// Good — suppress all lint for one line (less specific, use sparingly)
// biome-ignore lint: generated code, not worth fixing
eval(generatedCode);

// Bad — no reason (Biome rejects this)
// biome-ignore lint/suspicious/noDebugger
debugger;  // ERROR: suppression must include an explanation
```

**Specificity levels**:
- `biome-ignore lint` — all lint rules
- `biome-ignore lint/suspicious` — all rules in the suspicious group
- `biome-ignore lint/suspicious/noDebugger` — one specific rule

**Rationale**: The mandatory reason enforces documentation discipline — every suppression explains *why* the rule doesn't apply here. This connects to Guide 11's principle: comments explain why, not what. Bare suppressions that say "I know better" without explanation are rejected by Biome (Biome suppression comments docs).

**See also**: `11-documentation.md` ID-01

---

## ID-19: Range Suppressions — Suppress for a Block of Code

**Strength**: CONSIDER

**Summary**: Use `biome-ignore-start` / `biome-ignore-end` to suppress a rule across multiple lines.

```js
// biome-ignore-start lint/suspicious/noDoubleEquals: legacy comparison logic, migration pending
if (a == b) { /* ... */ }
if (c == d) { /* ... */ }
if (e == f) { /* ... */ }
// biome-ignore-end lint/suspicious/noDoubleEquals

if (g == h) { /* ... */ } // this line IS checked — outside the range
```

**Rules**:
- Every `start` must have a matching `end` with the same rule — unmatched pairs are errors
- The reason is required on both `start` and `end`
- Multiple ranges for different rules can overlap independently

**Rationale**: Range suppressions are for blocks of legacy code being migrated incrementally. Prefer fixing the code; use range suppressions when fixing is not yet feasible (Biome range suppression docs).

---

## ID-20: File-Wide Suppression — `biome-ignore-all`

**Strength**: CONSIDER

**Summary**: Suppress a rule for an entire file by placing `biome-ignore-all` at the top of the file.

```js
// biome-ignore-all lint/suspicious/noConsole: this is a logging utility module
// biome-ignore-all lint/style/noVar: generated code, do not modify

export function log(msg) {
  console.log(msg);  // no diagnostic
}
```

**Rules**: Must appear at the very top of the file (before any code). If placed elsewhere, Biome flags it as unused.

**Rationale**: File-wide suppressions are for generated files, vendor code, or files with known intentional patterns throughout. Prefer `files.includes` exclusion in `biome.json` for entire directories of generated code (Biome suppression docs).

---

## ID-21: Reading Diagnostic Output

**Strength**: SHOULD

**Summary**: Every Biome diagnostic contains the severity, rule name, location, explanation, and fix suggestion — following the rule pillars (What, Why, How).

```
/src/auth/login.js:42:5 lint/suspicious/noDoubleEquals ━━━━━━━━━━━━━━━━

  ✖ Use === instead of ==.
    == is only allowed when comparing against null.

  > 42 │ if (status == 200) {
       │     ^^^^^^^^^^^^^^

  ℹ Using == may lead to unexpected type coercion.

  ℹ Unsafe fix: Use ===
```

**Reading the output**:
- **File:line:col** — clickable in terminals/IDEs
- **Category** — `lint/suspicious/noDoubleEquals` (group/rule)
- **✖** — the "what" (what's wrong)
- **ℹ** — the "why" and "how" (advices)
- **Unsafe fix** — indicates a code action is available (tagged as unsafe in this case)

**Rationale**: Biome follows three rule pillars: every diagnostic must explain *what* is wrong, *why* it matters, and *how* to fix it. If a diagnostic is missing any pillar, that's a Biome bug worth reporting (Biome diagnostics docs; Biome rule pillars docs).

---

## ID-22: Biome Assist — Code Actions Beyond Lint

**Strength**: CONSIDER

**Summary**: Biome Assist provides code improvements (like import sorting) without being lint violations. Assist actions always have an automated fix.

```jsonc
{
  "assist": {
    "enabled": true,
    "actions": {
      "source": {
        "useSortedKeys": "on"     // sort object literal keys (JS) and JSON keys
      }
    }
  }
}
```

**In editors**: `source.organizeImports.biome` (import organization) and `source.fixAll.biome` (lint fixes) run on save when configured in VS Code settings.

**Rationale**: Assist is separate from lint — it suggests improvements without calling code "wrong." Import organization is the most common assist action. Configure via `biome.json` or editor settings (Biome assist docs).

---

## ID-23: Biome Scanner — Project-Level Indexing

**Strength**: CONSIDER

**Summary**: The Scanner crawls the project to collect metadata needed by types-domain and project-domain rules.

**When it runs**: Automatically triggered when any types-domain or project-domain rule is enabled. Does not run for syntax-only rules.

**Performance impact**: ~2s for ~2k files, ~8s for ~5k files. Without Scanner, linting takes ~1s regardless of project size.

**Rationale**: The Scanner enables cross-file analysis (unused exports, circular imports, type-aware checks) at the cost of a project crawl. Only runs when needed — syntax-only rules skip it entirely (Biome scanner docs).

---

## ID-24: GritQL — Custom Lint Rules via Pattern Matching

**Strength**: CONSIDER

**Summary**: Write custom lint rules using GritQL, a structural search language. Rules are `.grit` files registered in `biome.json`.

```grit
// no-object-assign.grit — flag Object.assign usage
`$fn($args)` where {
    $fn <: `Object.assign`,
    register_diagnostic(
        span = $fn,
        message = "Prefer object spread instead of Object.assign()"
    )
}
```

```jsonc
// biome.json
{ "plugins": ["./no-object-assign.grit"] }
```

**Limitations**: Plugins can only produce diagnostics (no auto-fixes). Supports JS/TS, CSS, and JSON.

**Rationale**: GritQL enables project-specific rules without forking Biome. It matches code by structure, not text — whitespace and quote style are ignored. Useful for enforcing project conventions that no built-in rule covers (Biome GritQL docs; Biome linter plugins docs).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `recommended` baseline | MUST | Stable, sensible default rules |
| 02 | `all` for maximum strictness | CONSIDER | Every stable rule; disable what you reject |
| 03 | `nursery` — opt-in only | CONSIDER | Not semver-stable; expect breaking changes |
| 04 | Severity: error/warn/info/off | SHOULD | Controls CI blocking behavior |
| 05 | Per-rule severity config | SHOULD | Short form or long form with fix/options |
| 06 | Rule groups by problem type | SHOULD | correctness, suspicious, style, complexity, etc. |
| 07 | `use*` vs `no*` naming | SHOULD | Enforce vs deny at a glance |
| 08 | Domains by analysis capability | SHOULD | types, project, react, etc. |
| 09 | `types` domain for type-aware rules | SHOULD | Requires JSDoc + checkJs; all rules currently nursery |
| 10 | `project` domain for cross-file | CONSIDER | Import graph analysis; Scanner performance cost |
| 11 | `noDoubleEquals` | MUST | Automated `===` enforcement → 01 ID-02 |
| 12 | `noVar` | MUST | Automated `var` ban → 01 ID-01 |
| 13 | `useConst` | SHOULD | Automated `const` preference → 01 ID-01 |
| 14 | `noUnusedVariables/Imports` | SHOULD | Dead code detection |
| 15 | Curated high-value rules | SHOULD | noShadow, useArraySortCompare, useIsNan, etc. |
| 16 | Safe fixes (`--write`) | SHOULD | Never change semantics; auto-apply safely |
| 17 | Unsafe fixes (`--write --unsafe`) | SHOULD | May change semantics; review required |
| 18 | Inline suppression with reason | MUST | `biome-ignore`: reason is mandatory |
| 19 | Range suppression | CONSIDER | `biome-ignore-start`/`-end` for legacy blocks |
| 20 | File-wide `biome-ignore-all` | CONSIDER | Top of file; for generated/vendor code |
| 21 | Reading diagnostic output | SHOULD | What, Why, How — three rule pillars |
| 22 | Biome Assist | CONSIDER | Import sorting, code improvements beyond lint |
| 23 | Scanner for cross-file analysis | CONSIDER | Triggered by types/project domain rules |
| 24 | GritQL custom rules | CONSIDER | Structural search; diagnostic only, no auto-fix |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `===` (ID-02), `const`/`let` (ID-01), naming (ID-12) — patterns that Biome enforces
- **Type Discipline**: See `05-type-discipline.md` for discriminated unions (ID-24–25), `deno check` (ID-20) — connects to types domain
- **Anti-Patterns**: See `09-anti-patterns.md` for `==` (ID-01), `var` (ID-28), shadowing (ID-12), `.sort()` (ID-17) — patterns Biome catches
- **Documentation**: See `11-documentation.md` for "comments explain why" (ID-01) — connects to mandatory suppression reasons
- **Biome Setup**: See `13-biome/01-setup.md` for installation (ID-04), `biome.json` (ID-06), CLI commands (ID-10–14)
- **Biome Formatting**: See `13-biome/03-formatting.md` for formatter options, Prettier compat

---

## External References

- [Biome — Lint Rules](https://biomejs.dev/linter/rules/)
- [Biome — Rule Groups](https://biomejs.dev/linter/#rule-groups)
- [Biome — Domains](https://biomejs.dev/linter/domains/)
- [Biome — Suppressions](https://biomejs.dev/linter/suppression/)
- [Biome — GritQL Plugins](https://biomejs.dev/linter/plugins/)
