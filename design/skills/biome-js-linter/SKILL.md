---
name: biome-js-linter
displayName: Biome JS Linter
description: >
  Pure JavaScript/ECMAScript linting guidance based on Biome's lint rules,
  filtered to language-level concerns only. No React, Node.js, JSX, CSS, or
  framework-specific rules. Use when writing, reviewing, or refactoring vanilla
  JavaScript to catch bugs, avoid pitfalls, enforce idiomatic style, simplify
  code, and prevent performance or security issues.
metadata:
  version: "1.0.0"
  domain: linting
  triggers: biome, lint, javascript, ecmascript, JS style, code quality, code review, vanilla JS
  role: reviewer
  scope: review
  output-format: guidance
  related-skills: javascript-pro, biome-web-linter
---

# Biome JS Linter — Claude Code Skill

> Pure JavaScript/ECMAScript linting guidance distilled from Biome's rules.
> Framework-free — no React, Node.js, JSX, CSS, or TypeScript type-system rules.
> 257 rules organized by concern, with do/don't code examples.

## When to Use This Skill

- Writing or reviewing vanilla JavaScript / ECMAScript code
- Catching language-level bugs before they reach production
- Enforcing consistent JS idioms and style
- Simplifying overly complex code
- Identifying performance anti-patterns in pure JS
- Reviewing code for security issues (eval, secrets)

## Core Workflow

1. **Identify context** — What kind of JS work? Data processing (load performance, simplification), business logic (bugs, pitfalls), library code (style, all categories)
2. **Load references** — Pull in relevant category files from the table below
3. **Apply rules** — Use the do/don't examples to guide code or review
4. **Cite rules** — Reference the Biome rule name (e.g., `noAccumulatingSpread`) when flagging issues

## Reference Guide

| Category | Reference | Rules | Load When |
|----------|-----------|-------|-----------|
| Bugs & Correctness | `references/bugs.md` | 37 | Wrong assignments, unreachable code, broken control flow |
| Pitfalls | `references/pitfalls.md` | 63 | Likely-wrong patterns, dubious comparisons, typos |
| Style & Idioms | `references/style.md` | 49 | Naming, syntax preferences, modern idioms |
| Simplification | `references/simplification.md` | 42 | Redundant wrappers, verbose patterns, over-engineering |
| Performance | `references/performance.md` | 8 | O(n^2) patterns, blocking operations |
| Security | `references/security.md` | 1 | Hardcoded secrets |
| Experimental | `references/experimental.md` | 57 | Biome nursery rules, not yet recommended |

## Critical Rules (Always Apply)

The highest-impact pure JS rules — keep these in mind at all times.

### Bugs — Catch Real Mistakes

| Don't | Do | Rule |
|-------|-----|------|
| Reassign `const` variables | Use `let` if reassignment needed | `noConstAssign` |
| Leave variables unused | Remove or prefix with `_` | `noUnusedVariables` |
| Write code after `return` | Remove unreachable code | `noUnreachable` |
| Use `new` on `Symbol` or `BigInt` | Call without `new`: `Symbol()`, `BigInt()` | `noInvalidNewBuiltin` |
| Return a value from setters | Setters must not return | `noSetterReturn` |
| Assign in `switch` discriminant | Compute before the `switch` | `noSwitchDeclarations` |

### Pitfalls — Probably Wrong

| Don't | Do | Rule |
|-------|-----|------|
| `typeof x === "strnig"` | Use valid type strings | `noInvalidTypeofComparison` |
| `x == null` (loose equality) | `x === null \|\| x === undefined` | `noDoubleEquals` |
| Duplicate object keys | Use unique keys | `noDuplicateObjectKeys` |
| `debugger` in committed code | Remove before committing | `noDebugger` |
| Assign inside expressions | Separate assignment from condition | `noAssignInExpressions` |
| Confusing `void` expressions | Separate into two statements | `noConfusingVoidExpression` |

### Style — Write Idiomatic JS

| Don't | Do | Rule |
|-------|-----|------|
| `var x = 1` | `const x = 1` or `let x = 1` | `noVar` |
| `x === -0` | `Object.is(x, -0)` | `noCompareNegZero` |
| `new Object()` / `new Array()` | `{}` / `[]` | `noNewSymbol` |
| Comma operator `(a, b)` | Separate statements | `noCommaOperator` |
| `arguments` keyword | Use rest parameters `...args` | `noArguments` |

### Performance — Avoid Slowdowns

| Don't | Do | Rule |
|-------|-----|------|
| `[...acc, val]` in `.reduce()` | `acc.push(val); return acc` | `noAccumulatingSpread` |
| `delete obj.key` | `obj.key = undefined` or restructure | `noDelete` |
| `for...in` on arrays | `for...of` or `.forEach()` | `noForEach` |

### Security

| Don't | Do | Rule |
|-------|-----|------|
| `const key = "AKIA1234..."` | Use environment variables | `noSecrets` |

## Constraints

### MUST DO
- Reference the specific Biome rule name when flagging issues
- Prioritize recommended rules (enabled by default) over optional ones
- Load category reference files for detailed examples before reviewing
- Consider that some rules may be intentionally disabled in the project's biome.json

### MUST NOT DO
- Apply experimental/nursery rules as errors — they may change
- Include React, Node.js, JSX, CSS, or framework-specific guidance (use `biome-web-linter` for that)
- Override project-specific rule configurations without discussion
