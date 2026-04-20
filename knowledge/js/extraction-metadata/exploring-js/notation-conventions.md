# Notation Conventions for Exploring JavaScript

## Code Examples

- Use fenced code blocks with `javascript` language tag
- Preserve the book's assertion-based example style: `assert.equal(x, y)`
- Use `>` for console output in examples

## Type Annotations

- The book uses TypeScript-style type signatures for documentation
- Format: `functionName(param: Type): ReturnType`
- These are descriptive, not executable TypeScript

## ES Version Markers

- The book marks features with superscript version tags: ^ES6^, ^ES2017^, ^ES2020^, etc.
- In concept cards, note the ES version in the Key Properties section
- Use format: "Introduced in ES2015 (ES6)" for the first major revision, then "ES20XX" for subsequent

## Special Values

- Wrap JavaScript values in backticks: `undefined`, `null`, `true`, `false`, `NaN`, `Infinity`
- Wrap operators in backticks: `===`, `==`, `typeof`, `instanceof`, `??`, `?.`
- Wrap keywords in backticks: `let`, `const`, `var`, `class`, `function`, `async`, `await`

## Source Citations

- This is an EPUB-converted source — no PDF page numbers
- Use markdown line numbers from the chapter metadata headers (`book_md_line` field)
- Citation format: "(Ch. N, line NNN)" or "(Rauschmayer, Ch. N)"
- Section references: use the book's numbered section format (e.g., "§13.1", "§27.3.2")

## Advanced Content Markers

- The book marks some chapters/sections as "(advanced)"
- Concept cards from advanced sections should be tier: advanced
- Note the advanced marker in the card's Context & Application section
