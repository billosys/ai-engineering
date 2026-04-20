---
# === CORE IDENTIFICATION ===
concept: Deploy Framework Support
slug: deploy-framework-support

# === CLASSIFICATION ===
category: deploy
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/frameworks.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "framework presets"
  - "framework integrations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
  - deploy-builds
extends: []
related:
  - deploy-observability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What frameworks does Deno Deploy support?"
  - "How do I deploy Next.js / Astro / SvelteKit to Deno Deploy?"
---

# Quick Definition
Deno Deploy natively supports Next.js, Astro, Nuxt, SolidStart, TanStack Start, SvelteKit, Fresh, Lume, and Remix (experimental), with automatic detection, optimized build/runtime configuration, and zero-config deployment for most frameworks.

# Core Definition
Deno Deploy provides first-class framework presets that are automatically detected when creating an app. Each preset optimizes the build and runtime configuration for its framework. Most frameworks require no additional setup -- Deno Deploy auto-configures Nitro for Nuxt, SolidStart, and TanStack Start, and handles standalone mode for Next.js. Astro SSR requires the `@deno/astro-adapter` package. Frameworks not in the supported list can still work with manual configuration of install/build commands and runtime settings.

# Prerequisites
- deno-deploy -- Frameworks deploy on the Deno Deploy platform
- deploy-builds -- Framework presets configure the build pipeline

# Key Properties
1. **Auto-detection** -- Framework type detected from repository structure during app creation
2. **Zero-config for most** -- Next.js, Nuxt, SolidStart, SvelteKit, Fresh, Lume require no additional setup
3. **Next.js features** -- Pages and app router, ISR, SSG, SSR, PPR, `"use cache"`, `next/image`, built-in tracing
4. **Nitro auto-configuration** -- Nuxt, SolidStart, TanStack Start use Nitro; Deno Deploy configures it automatically
5. **Astro adapter required for SSR** -- Install `@deno/astro-adapter` and configure `astro.config.mjs`
6. **Static and dynamic** -- Both static site generators (Lume, static Astro) and dynamic SSR frameworks supported
7. **Preset slugs** -- `nextjs`, `astro`, `nuxt`, `solidstart`, `tanstackstart`, `sveltekit`, `fresh`, `lume`, `remix`
8. **Remix experimental** -- Not yet fully supported; some features may not work

# Construction / Recognition
- Select framework preset during app creation or in `deno.json`:
  ```json
  { "deploy": { "framework": "nextjs" } }
  ```
- Astro SSR requires adapter:
  ```javascript
  import deno from '@deno/astro-adapter';
  export default defineConfig({ output: 'server', adapter: deno() });
  ```

# Context & Application
Framework support enables teams to deploy their existing web applications to Deno Deploy with minimal configuration changes. The auto-detection and optimized presets reduce deployment friction. Next.js is particularly well-supported with ISR, PPR, and automatic tracing. For unsupported frameworks, manual build configuration provides a fallback path.

# Examples
From deploy/reference/frameworks.md:
- "Natively supported frameworks are tested to work with Deno Deploy and are automatically detected when you create a new app."
- "Next.js on Deno Deploy always builds in standalone mode."
- "Tracing is supported out of the box, and Next.js automatically emits some spans for incoming requests, routing, rendering, and other operations."

# Relationships
## Builds Upon
- deno-deploy (the hosting platform)
- deploy-builds (framework presets configure the build pipeline)

## Related
- deploy-observability (some frameworks emit automatic tracing spans)

# Common Errors
1. Missing Astro adapter for SSR -- static Astro works without it, but SSR requires `@deno/astro-adapter`
2. Using Remix in production without awareness of experimental status -- some features may not work

# Common Confusions
1. **Preset vs. manual config** -- A framework preset auto-configures everything; without a preset you must manually set install, build, and runtime configuration

# Source Reference
- deploy/reference/frameworks.md: Complete list of supported frameworks and configuration details

# Verification Notes
- High confidence: Each framework explicitly listed with its preset slug and setup requirements
