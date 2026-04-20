---
concept: JSX Syntax
slug: jsx-syntax
category: tooling
subcategory: transpilation
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 662
section: "17.7 JSX: Markup Expressions in JavaScript"
extraction_confidence: high
aliases:
  - JSX
  - React JSX
prerequisites:
  - babel-transpilation
extends: []
related:
  - flow-type-annotations
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

JSX is a JavaScript language extension that allows HTML-like syntax in JavaScript expressions, compiled by Babel into `React.createElement()` calls, with curly braces `{}` embedding JavaScript expressions within the markup.

# Core Definition

JSX is an extension of core JavaScript most closely associated with React. JSX expressions are delimited by angle brackets and compile to `React.createElement()` calls. Attributes become properties of the second argument object. Children become additional arguments. Curly braces `{}` embed JavaScript expressions within JSX. Lowercase tag names are passed as strings; uppercase names are passed as identifiers (enabling components). Babel transforms JSX into standard JavaScript function calls (Flanagan, Ch. 17, pp. 662-667).

# Prerequisites

- **babel-transpilation** — JSX requires Babel (or similar) for compilation.

# Key Properties

1. HTML-like syntax that compiles to function calls.
2. Attributes map to a props object.
3. `{}` embeds JavaScript expressions.
4. Lowercase tags become string arguments; uppercase become component references.
5. The `&&` operator is an idiom for conditional rendering.
6. Spread syntax `{...obj}` distributes props from an object.

# Construction / Recognition

```jsx
let sidebar = (
  <div className="sidebar">
    <h1>{title}</h1>
    { drawLine && <hr/> }
    <p>{content}</p>
  </div>
);
// Compiles to:
let sidebar = React.createElement("div", {className: "sidebar"},
  React.createElement("h1", null, title),
  drawLine && React.createElement("hr", null),
  React.createElement("p", null, content));
```

# Context & Application

The dominant syntax for React UI development. Understanding JSX is essential for reading React code, even if you do not use React yourself.

# Examples

From the source (p. 663): A `sidebar()` function returns a JSX element with dynamic class, title, conditional `<hr/>`, and content. Also, a `list()` function using `items.map()` to generate `<li>` elements with `onClick` handlers and `key` props.

# Relationships

## Builds Upon
- **babel-transpilation** — Babel compiles JSX to JavaScript

## Enables
- React component development

## Related
- **flow-type-annotations** — Both are language extensions requiring Babel

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `class` instead of `className` in JSX.
  **Correction**: Since `class` is a JavaScript reserved word, JSX uses `className` for the HTML class attribute.

# Common Confusions

- **Confusion**: JSX is part of the JavaScript language standard.
  **Clarification**: JSX is a non-standard language extension that requires a build tool (Babel) to compile into standard JavaScript.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.7, pages 662-667.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Detailed compilation examples shown
- Uncertainties: None
- Cross-reference status: Verified
