---
name: deno-js-linter
displayName: Deno JS Linter
description: >
  Pure JavaScript/ECMAScript linting guidance based on Deno's lint rules,
  filtered to language-level concerns only. No React, JSX, Fresh, Deno-specific,
  Node.js-specific, or TypeScript type-system rules. Use when writing, reviewing,
  or refactoring vanilla JavaScript to catch bugs, avoid pitfalls, and enforce
  idiomatic style.
metadata:
  version: "1.0.0"
  domain: linting
  triggers: deno lint, javascript, ecmascript, JS style, code quality, code review, vanilla JS
  role: reviewer
  scope: review
  output-format: guidance
  related-skills: javascript-pro, biome-js-linter
---

# Deno JS Linter — Claude Code Skill

> Pure JavaScript/ECMAScript linting guidance distilled from Deno's lint rules.
> Framework-free — no React, JSX, Fresh, Deno runtime APIs, Node.js, or
> TypeScript type-system rules. 70 rules organized by concern, with do/don't
> code examples.

## When to Use This Skill

- Writing or reviewing vanilla JavaScript / ECMAScript code
- Catching language-level bugs before they reach production
- Avoiding common JS pitfalls (loose equality, misused async, eval)
- Enforcing consistent style and modern idioms (const, camelCase, etc.)

## Core Workflow

1. **Identify context** — What kind of JS work? Logic-heavy (load bugs), async code (load pitfalls), new code (load style)
2. **Load references** — Pull in relevant category files from the table below
3. **Apply rules** — Use the do/don't examples to guide code or review
4. **Cite rules** — Reference the Deno lint rule name (e.g., `no-const-assign`) when flagging issues

## Reference Guide

| Category | Reference | Rules | Load When |
|----------|-----------|-------|-----------|
| Bugs & Correctness | `references/bugs.md` | 41 | Wrong assignments, unreachable code, broken control flow, invalid regex |
| Pitfalls | `references/pitfalls.md` | 18 | Dubious comparisons, misused async, eval, debug leftovers, empty blocks |
| Style & Idioms | `references/style.md` | 11 | const vs let vs var, naming, cleaner declarations |

## Critical Rules (Always Apply)

The highest-impact pure JS rules — keep these in mind at all times.

### Bugs — Catch Real Mistakes

| Don't | Do | Rule |
|-------|-----|------|
| Reassign `const` variables | Use `let` if reassignment needed | `no-const-assign` |
| Write code after `return` | Remove unreachable code | `no-unreachable` |
| Duplicate keys in objects | Use unique keys | `no-dupe-keys` |
| Duplicate `case` labels | Use unique case values | `no-duplicate-case` |
| Reassign function declarations | Use `const fn = ...` if needed | `no-func-assign` |
| Return from setters | Setters must not return | `no-setter-return` |
| Omit `return` from getters | Getters must return a value | `getter-return` |
| Use `new Symbol()` | Call `Symbol()` without `new` | `no-new-symbol` |
| Forget `super()` in subclass constructor | Always call `super()` in extending classes | `constructor-super` |
| Assign in conditions `if (x = 1)` | Use `===` for comparison | `no-cond-assign` |
| Use `hasOwnProperty` directly | Use `Object.hasOwn()` or `Object.prototype.hasOwnProperty.call()` | `no-prototype-builtins` |

### Pitfalls — Probably Wrong

| Don't | Do | Rule |
|-------|-----|------|
| `x == y` (loose equality) | `x === y` (strict equality) | `eqeqeq` |
| `eval("code")` | Avoid eval entirely | `no-eval` |
| `debugger` in committed code | Remove before committing | `no-debugger` |
| `throw "error"` (string literal) | `throw new Error("error")` | `no-throw-literal` |
| `await` in a loop body | Collect promises, use `Promise.all()` | `no-await-in-loop` |
| `await` in a non-async function | Mark the function `async` | `no-await-in-sync-fn` |
| `async function` with no `await` | Remove `async` or add `await` | `require-await` |
| Leave empty `catch {}` blocks | Handle or comment the error | `no-empty` |

### Style — Write Idiomatic JS

| Don't | Do | Rule |
|-------|-----|------|
| `var x = 1` | `const x = 1` or `let x = 1` | `no-var` |
| `let x = 1` (never reassigned) | `const x = 1` | `prefer-const` |
| `let a = 1, b = 2` | `let a = 1; let b = 2;` | `single-var-declarator` |
| `!!someValue` (double negation) | `Boolean(someValue)` | `no-extra-boolean-cast` |
| Unused variables left in code | Remove or prefix with `_` | `no-unused-vars` |

## Constraints

### MUST DO
- Reference the specific Deno lint rule name when flagging issues
- Prioritize recommended rules (enabled by default) over optional ones
- Load category reference files for detailed examples before reviewing

### MUST NOT DO
- Include React, JSX, Fresh, Deno runtime, Node.js, or TypeScript type-system guidance (use other skills for those)
- Assume Deno lint is in use — check the project first
- Override project-specific lint configurations without discussion
