---
concept: Web Framework Support
slug: deno-web-framework-support
category: development
subcategory: web frameworks
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/web_dev.md"
chapter_number: null
pdf_page: null
section: "Web development"
extraction_confidence: high
aliases:
  - "Deno web frameworks"
  - "Fresh"
  - "Deno web development"
prerequisites:
  - deno-configuration
  - deno-http-server
extends: []
related:
  - deno-http-server
  - deno-package-json-support
contrasts_with: []
answers_questions:
  - "Which web frameworks work with Deno?"
  - "How do I use Next.js with Deno?"
  - "What is Fresh?"
---

# Quick Definition

Deno supports a wide range of web frameworks including Fresh (Deno-native, server-rendered with islands architecture), Next.js, Astro, Vite, Hono, Oak, Lume, and Docusaurus — all runnable via `deno run` or `deno task` with minimal or no configuration changes.

# Core Definition

Deno provides a developer-friendly environment for building web applications with its secure defaults, built-in TypeScript support, and standard library. While simple applications can use `Deno.serve` directly, complex applications typically use a framework.

Supported frameworks include:

- **Fresh** — The most popular Deno-native framework. Uses server-side rendering with an islands architecture (no JS sent to client by default). Create with `deno run -A -r https://fresh.deno.dev`.
- **Next.js** — React framework, runnable with `deno run -A npm:create-next-app@latest`.
- **Astro** — Static site generator, runnable with `deno run -A npm:create-astro`.
- **Vite** — Build tool serving native ES modules, runnable with `deno run -A npm:create-vite@latest`.
- **Hono** — Lightweight web framework in the Express/Sinatra tradition.
- **Oak** — Middleware framework for Deno's HTTP server with routing, JSON parsing, and plugin support. Available from `jsr:@oak/oak`.
- **Lume** — Deno-native static site generator inspired by Jekyll/Eleventy.
- **Docusaurus** — Documentation-optimized static site generator.

Additionally, existing Node.js projects run with Deno out of the box.

# Prerequisites

- `deno-configuration` — framework projects use `deno.json` for configuration
- `deno-http-server` — frameworks build on Deno's HTTP server capabilities

# Key Properties

1. **npm compatibility**: Most frameworks are installed via `npm:` specifiers (e.g., `npm:create-next-app@latest`), leveraging Deno's Node.js compatibility.
2. **Fresh is Deno-native**: Fresh is purpose-built for Deno, using server-side rendering and selective client-side hydration via islands.
3. **Oak is Deno-native**: Oak is available from JSR (`jsr:@oak/oak`) and provides Express-like middleware for Deno's HTTP server.
4. **Task-based workflows**: All frameworks integrate with `deno task` for dev, build, and start commands.
5. **No migration needed for Node projects**: Deno runs Node.js projects directly.

# Construction / Recognition

Fresh (Deno-native):
```sh
deno run -A -r https://fresh.deno.dev
cd my-fresh-app
deno task start
```

Next.js:
```sh
deno run -A npm:create-next-app@latest my-next-app
cd my-next-app
deno task dev
```

Oak server:
```ts
import { Application } from "jsr:@oak/oak/application";
import { Router } from "jsr:@oak/oak/router";

const router = new Router();
router.get("/", (ctx) => {
  ctx.response.body = "<h1>Hello oak!</h1>";
});

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());
app.listen({ port: 8080 });
```

# Context & Application

Framework support is central to Deno's web development story. By supporting both Deno-native frameworks (Fresh, Oak, Lume) and Node.js frameworks (Next.js, Astro, Vite), Deno provides a migration path for existing Node.js projects while offering Deno-optimized alternatives for new projects.

# Examples

All framework creation commands from `runtime/fundamentals/web_dev.md`:

```sh
# Fresh
deno run -A -r https://fresh.deno.dev

# Next.js
deno run -A npm:create-next-app@latest my-next-app

# Astro
deno run -A npm:create-astro my-astro-site

# Vite
deno run -A npm:create-vite@latest

# Hono
deno run -A npm:create-hono@latest

# Lume
deno run -A https://lume.land/init.ts

# Docusaurus
deno run -A npm:create-docusaurus@latest my-website classic
```

# Relationships

- **Related**: `deno-http-server` — `Deno.serve` is the foundation that frameworks build upon
- **Related**: `deno-package-json-support` — npm-based frameworks use `package.json` dependencies

# Common Errors

1. **Forgetting `deno install` for npm frameworks**: Frameworks using `package.json` dependencies need `deno install` to set up `node_modules`.

# Common Confusions

- **Fresh vs Next.js**: Fresh is Deno-native with server-rendered islands (no client JS by default), while Next.js is a React framework that requires npm compatibility.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/web_dev.md`, all sections.

# Verification Notes

All framework listings and setup commands are explicitly documented in the source file. Extraction confidence is high.
