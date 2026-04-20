---
concept: JSX Support
slug: jsx-support
category: platform
subcategory: language support
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/jsx.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "JSX in Deno"
  - "TSX in Deno"
  - "JSX configuration"
prerequisites:
  - deno
  - deno-cli
extends: []
related:
  - web-platform-apis
  - deno-bundle
  - deno-serve
contrasts_with: []
answers_questions:
  - "How do I use JSX in Deno?"
  - "How do I configure Deno for React or Preact JSX?"
  - "What is the JSX precompile transform?"
---

# Quick Definition

Deno has built-in JSX/TSX support in `.jsx` and `.tsx` files, configurable via `deno.json` compiler options for React, Preact, or the Deno-specific precompile transform that is 7-20x faster for server-side rendering.

# Core Definition

"Deno has built-in support for JSX in both `.jsx` files and `.tsx` files. JSX in Deno can be handy for server-side rendering or generating code for browser consumption."

Deno supports four JSX modes configured via the `"jsx"` compiler option in `deno.json`:

1. **`"react"`** (default) -- Classic `React.createElement` transform. Requires `jsxFactory` and `jsxFragmentFactory`.
2. **`"react-jsx"`** (recommended) -- Automatic runtime transform (React 17+). Auto-imports from `jsxImportSource/jsx-runtime`.
3. **`"react-jsxdev"`** -- Development transform with file/line/column debug information. Only for development.
4. **`"precompile"`** -- Deno-specific transform that pre-renders static HTML strings, "up to 7-20x faster than the other JSX transform options." Works best with Preact and Hono; not supported in React.

The `jsxImportSource` setting controls which library provides the JSX runtime (e.g., `"react"`, `"preact"`). Per-file overrides are supported via the `@jsxImportSource` pragma in leading comments.

# Prerequisites

- **Deno** -- JSX support is built into the Deno runtime.
- **deno-cli** -- Configuration is via `deno.json` and the CLI runs JSX files.

# Key Properties

1. **Zero-config default** -- Default is classic React transform; no configuration needed for basic React JSX.
2. **Automatic imports** -- `"react-jsx"` mode auto-inserts JSX runtime imports.
3. **Precompile transform** -- Deno-exclusive optimization that stores pre-compiled HTML strings for static elements.
4. **Per-file pragma** -- `@jsxImportSource` pragma overrides project-level settings per file.
5. **Type support** -- `jsxImportSourceTypes` setting (or `@jsxImportSourceTypes` pragma) provides type definitions when the JSX library doesn't include them.
6. **Skip elements** -- `jsxPrecompileSkipElements` prevents specific HTML elements from being precompiled.

# Construction / Recognition

## To Configure (recommended React setup):
```json
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "jsxImportSource": "react"
  },
  "imports": {
    "react": "npm:react",
    "@types/react": "npm:@types/react"
  }
}
```

## To Configure (Preact with precompile):
```json
{
  "compilerOptions": {
    "jsx": "precompile",
    "jsxImportSource": "preact"
  },
  "imports": {
    "preact": "npm:preact"
  }
}
```

## Per-file override:
```jsx
/** @jsxImportSource https://esm.sh/preact */
export function App() {
  return <div><h1>Hello, world!</h1></div>;
}
```

# Context & Application

- **Server-side rendering**: JSX combined with `renderToString` and `Deno.serve()` for SSR.
- **Browser code generation**: Bundle JSX for browser consumption via `deno bundle --platform=browser`.
- **Preact/Hono applications**: The precompile transform provides significant SSR performance gains.

# Examples

**Example 1** (from source): JSX automatic runtime output.
```jsx
// input
const jsx = (
  <div className="foo">
    <MyComponent value={2} />
  </div>
);

// output
import { jsx as _jsx } from "react/jsx-runtime";
const jsx = _jsx("div", {
  className: "foo",
  children: _jsx(MyComponent, { value: 2 }),
});
```
(Section: "JSX automatic runtime")

**Example 2** (from source): Preact SSR with precompile transform.
```tsx
import { renderToString } from "preact-render-to-string";

const App = () => <h1>Hello world</h1>;

Deno.serve(() => {
  const html = `<!DOCTYPE html>${renderToString(<App />)}`;
  return new Response(html, {
    headers: { "Content-Type": "text/html; charset=utf-8" },
  });
});
```
(Section: "Rendering JSX in server responses")

**Example 3** (from source): Precompile transform output showing pre-rendered HTML template.
```jsx
// output of precompile transform:
const $$_tpl_1 = ['<div class="foo">', "</div>"];
const jsx = _jsxTemplate($$_tpl_1, _jsx(MyComponent, { value: 2 }));
```
(Section: "JSX precompile transform")

# Relationships

## Builds Upon
- React/Preact JSX transform specifications.
- TypeScript compiler JSX options.

## Enables
- Server-side rendering in Deno.
- Isomorphic React/Preact applications.

## Related
- **deno-bundle** -- Bundles JSX/TSX for browser distribution.
- **deno-serve** -- Commonly used to serve SSR output.
- **web-platform-apis** -- SSR responses use Web Platform Request/Response.

# Common Errors

- **Error**: Using `"react-jsxdev"` in production.
  **Correction**: The dev transform adds file/line/column metadata for debugging. Use `"react-jsx"` or `"precompile"` in production.

- **Error**: Using the precompile transform with React.
  **Correction**: The precompile transform "works best with Preact or Hono. It is not supported in React."

# Common Confusions

- **Confusion**: Deno requires a separate JSX/TSX compiler.
  **Clarification**: JSX/TSX support is built into the Deno CLI; configuration is via `deno.json` compiler options.

- **Confusion**: The precompile transform works with all frameworks.
  **Clarification**: It is designed for Preact and Hono; React does not support it.

# Source Reference

- runtime/reference/jsx.md: Full JSX configuration documentation, all four modes, pragma support, precompile transform, SSR examples.

# Verification Notes

- High confidence: Comprehensive documentation with configuration examples, transform output, and SSR patterns directly from source.
- Performance claim ("7-20x faster") quoted directly from source.
