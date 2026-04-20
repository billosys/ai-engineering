---
name: biome-linter
displayName: Biome Linter
description: >
  JavaScript/TypeScript/JSX/CSS linting guidance based on Biome's 394 lint rules.
  Use when writing, reviewing, or refactoring JS/TS/JSX/CSS code to catch bugs,
  enforce style consistency, improve accessibility, avoid performance pitfalls,
  and prevent security vulnerabilities. Covers correctness, suspicious patterns,
  style, complexity, a11y, performance, and security categories.
metadata:
  version: "1.0.0"
  domain: linting
  triggers: biome, lint, linter, code review, JS style, code quality, a11y, accessibility
  role: reviewer
  scope: review
  output-format: guidance
  related-skills: javascript-pro
---

# Biome Linter — Claude Code Skill

> **Biome** is a fast formatter and linter for JavaScript, TypeScript, JSX, and CSS.
> This skill distills 394 lint rules into actionable do/don't guidance, organized
> by category. Rules marked **recommended** are enabled by default in Biome.

## When to Use This Skill

- Writing or reviewing JavaScript, TypeScript, JSX, or CSS code
- Catching bugs before they reach production
- Enforcing consistent code style across a codebase
- Improving accessibility of HTML/JSX output
- Identifying performance anti-patterns
- Preventing common security vulnerabilities

## Core Workflow

1. **Identify context** — Determine which categories are relevant (e.g., a11y for UI components, performance for data processing, security for user-facing code)
2. **Load references** — Load the relevant category reference files (see table below)
3. **Apply rules** — Use the do/don't patterns to guide code writing or review
4. **Cite rules** — When flagging issues, reference the Biome rule name (e.g., `noAccumulatingSpread`) so developers can configure or look up the rule

## Reference Guide

Load detailed do/don't guidance based on context:

| Category | Reference | Load When |
|----------|-----------|-----------|
| Correctness | `references/correctness.md` | Catching bugs: wrong assignments, unreachable code, broken control flow |
| Suspicious | `references/suspicious.md` | Likely-wrong patterns: typos, dubious comparisons, debug leftovers |
| Style | `references/style.md` | Code style: naming, syntax preferences, idiomatic patterns |
| Complexity | `references/complexity.md` | Simplification: unnecessary wrappers, redundant logic, over-engineering |
| Accessibility | `references/a11y.md` | HTML/JSX a11y: ARIA, semantic elements, keyboard navigation |
| Performance | `references/performance.md` | Performance: O(n^2) patterns, blocking operations, unnecessary work |
| Security | `references/security.md` | Security: eval(), target=_blank, secrets in code |
| Nursery | `references/nursery.md` | Experimental rules under evaluation, not yet recommended |

## Critical Rules (Always Apply)

These are the highest-impact rules you should always keep in mind. For the full
set with examples, load the category reference files above.

### Correctness — Catch Real Bugs

| Don't | Do | Rule |
|-------|-----|------|
| Reassign `const` variables | Use `let` if reassignment needed | `noConstAssign` |
| Leave variables unused | Remove or prefix with `_` | `noUnusedVariables` |
| Use `==` or `!=` | Use `===` or `!==` | `noDoubleEquals` |
| Write unreachable code after `return` | Remove dead code | `noUnreachable` |
| Call `new` on non-constructors | Only `new` on classes/constructors | `noInvalidNewBuiltin` |
| Return in setters | Setters should not return values | `noSetterReturn` |

### Suspicious — Probably Wrong

| Don't | Do | Rule |
|-------|-----|------|
| Use `console.log()` in production | Remove or use proper logging | `noConsole` |
| Compare with `typeof foo === "strnig"` | Use valid type strings | `noInvalidTypeofComparison` |
| Duplicate keys in objects | Use unique keys | `noDuplicateObjectKeys` |
| Use `debugger` statement | Remove before committing | `noDebugger` |
| Reassign function parameters | Copy to local variable | `noAssignInExpressions` |

### Performance — Avoid Slowdowns

| Don't | Do | Rule |
|-------|-----|------|
| `[...acc, val]` in `.reduce()` | `acc.push(val); return acc` | `noAccumulatingSpread` |
| `await` inside loops | Collect promises, `await Promise.all()` | `noAwaitInLoops` |
| `delete obj.key` | `obj.key = undefined` or restructure | `noDelete` |

### Security — Prevent Vulnerabilities

| Don't | Do | Rule |
|-------|-----|------|
| `eval("code")` | Avoid eval entirely | `noGlobalEval` |
| `<a target="_blank">` | Add `rel="noopener"` | `noBlankTarget` |
| Hardcode API keys/tokens | Use environment variables | `noSecrets` |

### Accessibility — Include Everyone

| Don't | Do | Rule |
|-------|-----|------|
| `<div role="button">` | Use `<button>` | `useSemanticElements` |
| `<img>` without `alt` | Always provide `alt` text | `useAltText` |
| `aria-hidden="true"` on focusable elements | Remove from tab order first | `noAriaHiddenOnFocusable` |
| `tabIndex > 0` | Use `tabIndex={0}` or `tabIndex={-1}` | `noPositiveTabindex` |
| Missing `<label>` for inputs | Associate labels with controls | `noLabelWithoutControl` |

## Constraints

### MUST DO
- Always reference the specific Biome rule name when flagging issues
- Prioritize recommended rules (enabled by default) over optional ones
- Consider the project's biome.json configuration — some rules may be intentionally disabled
- Load category reference files for detailed examples before reviewing domain-specific code

### MUST NOT DO
- Flag nursery rules as errors — they are experimental and may change
- Assume all rules apply — check whether the project uses Biome at all
- Override project-specific rule configurations without discussion
- Apply CSS or GraphQL rules when reviewing pure JavaScript/TypeScript
