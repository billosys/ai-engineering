---
concept: Stricter Parsing
slug: stricter-parsing
category: compatibility
subcategory: parser behavior
tier: advanced
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "formatter/differences-with-prettier.md"
chapter_number: null
pdf_page: null
section: "Prettier formats invalid syntaxes"
extraction_confidence: high
aliases:
  - bogus nodes
  - Biome parser strictness
prerequisites:
  - biome-formatter
  - prettier-compatibility
extends:
  - prettier-compatibility
related:
  - prettier-divergences
contrasts_with: []
answers_questions:
  - "What should I understand before migrating from Prettier?"
  - "How does Biome handle invalid syntax differently from Prettier?"
---

# Quick Definition

Biome's parser is intentionally stricter than Prettier's Babel-based parser, treating certain invalid syntax constructs as parse errors that produce "Bogus" nodes, which are printed verbatim without formatting rather than being silently normalized.

# Core Definition

Prettier's Babel-based JavaScript/TypeScript parser is permissive, allowing multiple syntax errors to be ignored and building an AST as if the code were valid. Biome's parser is stricter: it identifies genuine syntax errors and represents them as `Bogus` nodes in the syntax tree. When the formatter encounters a Bogus node, it prints the content verbatim without any formatting, since "attempting to format them could be incorrect and cause semantic changes."

# Prerequisites

- biome-formatter — understanding the Biome formatter
- prettier-compatibility — understanding the compatibility goal

# Key Properties

1. **Bogus nodes** — Biome's parser produces Bogus nodes for invalid syntax, which may contain valid nodes, invalid nodes, and raw characters
2. **Verbatim printing** — Bogus nodes are printed as plain text without formatting
3. **Semantic safety** — refusing to format invalid syntax prevents the formatter from introducing semantic changes
4. **Modifier handling** — Biome keeps a list of modifiers (preserving duplicates), while Prettier uses boolean fields (losing duplicates)
5. **Syntax errors detected** — duplicate modifiers, invalid modifier order, function declarations with bodies, abstract properties in non-abstract classes, assignment to optional chains, invalid `const` on interface type parameters, top-level return, erroneous self-increment/decrement

# Construction / Recognition

Invalid syntax that Biome detects but Prettier formats normally:

- `private public a = 1;` — duplicate accessibility modifiers (Prettier silently drops one)
- `declare function foo() {}` — declare function with body (Prettier formats it)
- `class C { abstract foo; }` — abstract in non-abstract class (Prettier formats it)
- `readonly readonly x: number;` — duplicate readonly (Prettier drops the duplicate)
- `(a?.b) = c;` — assignment to optional chain (Prettier removes parentheses)
- `(1)++;` — erroneous self-increment (Prettier removes parentheses)

In all these cases, Biome preserves the original text as-is because it cannot safely format invalid constructs.

# Context & Application

This difference is most visible when migrating codebases that contain invalid syntax. If Prettier was silently normalizing errors (e.g., removing duplicate modifiers), switching to Biome will surface those as un-formatted code. This can be beneficial for catching latent bugs, but it means the formatted output differs from Prettier's.

The source also notes that Prettier has inconsistencies between its TypeScript and Babel parsers. Biome uses a single unified parser, so there are no such inconsistencies. Differences that appear only with Prettier's `typescript` parser are considered Prettier bugs.

# Examples

From `formatter/differences-with-prettier.md`:

**Duplicate modifiers** — Prettier silently drops `public`, Biome preserves verbatim:
```ts
// Input:
class Foo { private public a = 1; }

// Prettier output:
class Foo { private a = 1; }

// Biome output (unformatted):
class Foo { private public a  = 1; }
```

**Top-level return** — Prettier formats as multi-line, Biome preserves verbatim:
```js
// Input:
return someVeryLongStringA && someVeryLongStringB && someVeryLongStringC && someVeryLongStringD

// Prettier wraps it; Biome keeps it on one line (verbatim)
```

**Assignment to optional chain** — Prettier removes parentheses (changing semantics), Biome preserves:
```js
// Input: (a?.b) = c;
// Prettier: a?.b = c;
// Biome: (a?.b) = c;
```

# Relationships

## Builds Upon
- prettier-compatibility (this is a category of known differences)

## Enables
- Detection of latent syntax errors in codebases that Prettier was silently normalizing

## Related
- prettier-divergences (intentional formatting differences on valid code)

## Contrasts With
Prettier's permissive parsing approach, which builds a valid AST even from syntactically invalid input.

# Common Errors

1. **Expecting formatted output for invalid syntax** — Biome intentionally does not format Bogus nodes; this is a feature, not a bug.
2. **Not recognizing parser strictness as the cause** — when code appears unformatted after migration, check if it contains syntax errors that Biome's parser detects.

# Common Confusions

1. **Strictness vs. incompatibility** — Biome's stricter parsing is not a compatibility failure; it is a deliberate design choice to avoid formatting invalid code.
2. **Bogus nodes vs. parse failure** — Bogus nodes do not prevent Biome from processing a file; the rest of the file is formatted normally, and only the invalid portions are preserved verbatim.
3. **Prettier "fixing" syntax** — Prettier does not fix syntax errors; it silently formats them as if they were valid, which can mask real problems (e.g., dropping duplicate modifiers without warning).

# Source Reference

- `sources-md/biome/formatter/differences-with-prettier.md` — "Prettier formats invalid syntaxes" section and all subsections (duplicate modifiers, assignment to optional chain, incorrect modifier for interface type parameters, top-level return, erroneous self-increment, abstract modifier in non-abstract classes)
- `sources-md/biome/formatter/differences-with-prettier.md` — "Prettier has inconsistencies between TypeScript and Babel parsing" section

# Verification Notes

All syntax error examples and the Bogus node mechanism description are taken directly from the source text. The list of detected errors comes from the enumerated list in the source.
