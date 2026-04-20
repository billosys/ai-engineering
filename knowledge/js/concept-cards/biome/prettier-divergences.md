---
concept: Prettier Divergences
slug: prettier-divergences
category: compatibility
subcategory: formatting differences
tier: advanced
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "formatter/differences-with-prettier.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - Prettier differences
  - intentional divergences
prerequisites:
  - biome-formatter
  - prettier-compatibility
extends:
  - prettier-compatibility
related:
  - stricter-parsing
  - opinionated-formatting
contrasts_with: []
answers_questions:
  - "What should I understand before migrating from Prettier?"
  - "How does the Biome formatter relate to Prettier?"
  - "Where does Biome intentionally differ from Prettier's output?"
---

# Quick Definition

Biome intentionally diverges from Prettier's formatting output in several specific cases, including ES2015+ identifier unquoting, consistent parenthesization in computed keys, trailing commas on arrow function type parameters, and normalization of parenthesized non-null-asserted optional chains.

# Core Definition

While Biome aims for high Prettier compatibility, it has deliberately chosen to produce different output in cases where Prettier's behavior is considered inconsistent, overly conservative, or based on legacy constraints. These are not bugs but intentional design decisions documented as known divergences. Each divergence has a rationale grounded in consistency, correctness, or modernization.

# Prerequisites

- biome-formatter — understanding the Biome formatter
- prettier-compatibility — understanding the compatibility goal and its limits

# Key Properties

1. **ES2015+ identifier unquoting** — Biome unquotes all valid ES2015+ JavaScript identifiers in object/class properties, while Prettier only unquotes valid ES5 identifiers (a legacy restriction)
2. **Consistent parenthesization in computed keys** — Prettier inconsistently adds parentheses around assignments in computed keys of object properties but not class properties; Biome consistently omits them
3. **Trailing commas on arrow type parameters** — Prettier adds a trailing comma to type parameters of arrow functions even when a default type makes it unnecessary; Biome omits it when not required
4. **Non-null-asserted optional chains** — Prettier inconsistently handles parenthesized non-null assertions on optional chains; Biome normalizes by removing unnecessary parentheses
5. **TypeScript vs. Babel parser inconsistencies** — differences that only appear with Prettier's `typescript` parser (not `babel`/`babel-ts`) are considered Prettier bugs, not Biome incompatibilities

# Construction / Recognition

When migrating from Prettier, these divergences can be identified by running both formatters and diffing the output. Key patterns to look for:

- Properties like `"𐊧"` being unquoted to `𐊧` (ES2015+ identifiers)
- Parentheses around assignments in computed keys being removed: `[(x = 0)]` becomes `[x = 0]`
- Trailing commas removed from arrow function type parameters with defaults: `<T = unknown,>` becomes `<T = unknown>`
- Parentheses removed from non-null-asserted optional chains: `(a.?.b)!` becomes `a.?.b!`

# Context & Application

These divergences matter during migration from Prettier to Biome. Teams should review this list before switching to understand which formatting differences are expected and intentional. In most codebases, these cases are relatively rare and should not cause significant diff noise.

# Examples

From `formatter/differences-with-prettier.md`:

**Identifier unquoting** (ES2015+ vs. ES5):
```js
// Prettier keeps quotes on non-ES5 identifiers:
const obj = { "𐊧": true };
// Biome unquotes them:
const obj = { 𐊧: true };
```

**Computed key parenthesization** — Prettier adds parentheses for object but not class:
```js
// Prettier (inconsistent):
a = { [(x = 0)]: 1 };  // object: parenthesized
class C { [x = 0] = 1; }  // class: not parenthesized

// Biome (consistent):
a = { [x = 0]: 1 };  // both: not parenthesized
class C { [x = 0] = 1; }
```

**Arrow function type parameter trailing comma**:
```tsx
// Prettier: <T = unknown,>() => {};
// Biome:    <T = unknown>() => {};
```

# Relationships

## Builds Upon
- prettier-compatibility (these are the exceptions to the compatibility goal)

## Enables
- Informed decision-making during Prettier-to-Biome migration

## Related
- stricter-parsing (another category of Prettier differences, related to parser strictness)
- opinionated-formatting (divergences reflect Biome's own opinions)

## Contrasts With
None directly; these contrast with Prettier's specific behaviors.

# Common Errors

1. **Reporting divergences as bugs** — these differences are intentional and documented; they should not be filed as compatibility bugs.
2. **Blaming Biome for TypeScript parser differences** — formatting differences that appear only with Prettier's `typescript` parser setting are considered Prettier bugs.

# Common Confusions

1. **Divergences vs. bugs** — all items in this list are deliberate choices, not formatting errors.
2. **Divergences vs. parser strictness** — the divergences listed here are about formatting choices on valid code; stricter-parsing covers how invalid syntax is handled differently.

# Source Reference

- `sources-md/biome/formatter/differences-with-prettier.md` — all sections except "Prettier formats invalid syntaxes"

# Verification Notes

All divergence examples and rationales are taken directly from the source text with specific code examples preserved. Each divergence includes Biome's stated reasoning.
