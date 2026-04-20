---
name: tailwindcss
displayName: Tailwind CSS v4
description: >
  Tailwind CSS v4 utility-first styling with CSS-native configuration.
  Use when styling with Tailwind utility classes, configuring themes via @theme,
  building responsive/dark-mode layouts, creating custom utilities or variants,
  or working with container queries. Covers the complete v4 API including
  @theme, @utility, @custom-variant, @variant, @source, and all utility classes.
sources:
  - https://raw.githubusercontent.com/blencorp/claude-code-kit/refs/heads/main/cli/kits/tailwindcss/skills/tailwindcss/SKILL.md
  - https://raw.githubusercontent.com/einverne/dotfiles/refs/heads/master/claude/skills/tailwindcss/SKILL.md
version: 2.0.0
tailwind_version: ">=4.0"
---

# Tailwind CSS v4 — Claude Code Skill

> **Tailwind CSS v4** (released January 2025, current stable v4.2) uses a **CSS-first
> configuration** approach. This skill covers v4 exclusively. All theme customization
> happens in CSS via `@theme`, not in `tailwind.config.js`.

## Critical: v3 → v4 Breaking Changes

**Do NOT use these v3 patterns — they are wrong for v4:**

| ❌ v3 (WRONG) | ✅ v4 (CORRECT) |
|---|---|
| `@tailwind base; @tailwind components; @tailwind utilities;` | `@import "tailwindcss";` |
| `tailwind.config.js` theme/extend | `@theme { --color-brand: ...; }` in CSS |
| `content: ['./src/**/*.{js,tsx}']` in JS config | Automatic detection + `@source` directive |
| `theme()` function in CSS | `var(--color-red-500)` CSS variables |
| `!bg-red-500` (prefix `!` for important) | `bg-red-500!` (suffix `!`) |
| `darkMode: 'class'` in JS config | `@custom-variant dark (&:where(.dark, .dark *));` |
| `addUtility()` in plugin JS | `@utility name { ... }` in CSS |
| `addVariant()` in plugin JS | `@custom-variant name (selector);` in CSS |
| `@screen md { ... }` | `@variant md { ... }` or just use `md:` prefix |
| `@apply` in Vue/Svelte `<style>` (breaks) | Add `@reference "../../app.css";` first |
| `require('@tailwindcss/container-queries')` | Built-in: `@container` + `@sm:` / `@md:` etc. |
| `bg-[var(--my-color)]` | `bg-(--my-color)` (v4 shorthand) |

## Setup

### CSS Entry Point

```css
/* app.css — the single import replaces all v3 @tailwind directives */
@import "tailwindcss";

/* Optional modifiers: */
@import "tailwindcss" prefix(tw);        /* Prefix all classes: tw:flex */
@import "tailwindcss" important;          /* All utilities get !important */
@import "tailwindcss" source("../src");   /* Set source scanning root */
```

### Vite Setup

```bash
npm install -D tailwindcss @tailwindcss/vite
```

```javascript
// vite.config.ts
import tailwindcss from '@tailwindcss/vite'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [tailwindcss()],
})
```

### PostCSS Setup (Alternative)

```bash
npm install -D tailwindcss @tailwindcss/postcss autoprefixer
```

```javascript
// postcss.config.js
export default {
  plugins: {
    "@tailwindcss/postcss": {},
    autoprefixer: {},
  },
}
```

### CLI Setup (No Bundler)

```bash
npm install -D tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i app.css -o dist/app.css --watch
```

## Reference Material

A comprehensive Tailwind CSS v4.2 reference document is available at:
```
../../guides/tailwindcss-v4/reference.md
```

(Relative to this SKILL.md file.)

**When to consult the reference:**
- You need the exact list of values for a specific utility (e.g., all `blur-*` sizes, all `cursor-*` options)
- You're unsure whether a utility exists in v4 or was removed/renamed from v3
- You need the precise `@theme` namespace for a category (e.g., which variable prefix generates which utilities)
- You want to verify the correct syntax for a v4 directive (`@utility`, `@custom-variant`, `@source`, `@variant`)
- You encounter an unfamiliar v4 feature (container queries, `field-sizing`, `text-shadow`, mask utilities, `@reference`)

**When you don't need it:**
- Standard layout, spacing, typography, color, and responsive patterns are covered in this SKILL.md
- Common component patterns (cards, navs, forms, grids) are already here
- The v3→v4 migration table at the top of this file covers the most common pitfalls

Read the reference with the `view` tool if you need detail beyond what this skill file provides.

## Theme System (`@theme`)

Theme variables are special CSS variables defined with `@theme` that **create
corresponding utility classes**. They are not just CSS variables — they instruct
Tailwind to generate utilities.

### Defining Theme Variables

```css
@import "tailwindcss";

@theme {
  /* Colors → bg-brand, text-brand, border-brand, ring-brand, etc. */
  --color-brand-50: oklch(0.97 0.02 264);
  --color-brand-500: oklch(0.55 0.22 264);
  --color-brand-900: oklch(0.25 0.15 264);

  /* Fonts → font-display, font-body utilities */
  --font-display: "Satoshi", "Inter", sans-serif;
  --font-body: "Inter", system-ui, sans-serif;

  /* Font sizes → text-display utility */
  --text-display: 3rem;

  /* Font weights → font-heading utility */
  --font-weight-heading: 700;

  /* Letter spacing → tracking-wide utility */
  --tracking-wide: 0.025em;

  /* Line height → leading-relaxed utility */
  --leading-relaxed: 1.75;

  /* Breakpoints → 3xl: responsive variant */
  --breakpoint-3xl: 120rem;

  /* Container sizes → @8xl: container query variant + max-w-8xl */
  --container-8xl: 96rem;

  /* Border radius → rounded-xl utility */
  --radius-xl: 0.75rem;

  /* Shadows → shadow-soft utility */
  --shadow-soft: 0 2px 8px rgba(0, 0, 0, 0.08);

  /* Inset shadows → inset-shadow-deep utility */
  --inset-shadow-deep: inset 0 4px 8px rgba(0, 0, 0, 0.15);

  /* Drop shadows → drop-shadow-hard utility */
  --drop-shadow-hard: 0 2px 4px rgba(0, 0, 0, 0.3);

  /* Blur → blur-heavy utility */
  --blur-heavy: 40px;

  /* Perspective → perspective-dramatic utility */
  --perspective-dramatic: 200px;

  /* Aspect ratio → aspect-golden utility */
  --aspect-golden: 1.618 / 1;

  /* Easing → ease-snappy utility */
  --ease-snappy: cubic-bezier(0.2, 0, 0, 1);

  /* Animations → animate-fade-in utility */
  --animate-fade-in: fade-in 0.3s ease-out;
  @keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
  }
}
```

### Namespace → Utility Mapping

| Theme Namespace | Creates |
|---|---|
| `--color-*` | `bg-*`, `text-*`, `border-*`, `ring-*`, `fill-*`, `stroke-*`, `accent-*`, `caret-*`, `outline-*`, `decoration-*`, `shadow-*` (color), `from-*`, `via-*`, `to-*` |
| `--font-*` | `font-*` (family) |
| `--text-*` | `text-*` (size) |
| `--font-weight-*` | `font-*` (weight) |
| `--tracking-*` | `tracking-*` (letter-spacing) |
| `--leading-*` | `leading-*` (line-height) |
| `--breakpoint-*` | `sm:`, `md:`, `lg:`, etc. responsive variants |
| `--container-*` | `@sm:`, `@md:`, etc. container query variants + `max-w-*` |
| `--spacing-*` | `p-*`, `m-*`, `gap-*`, `w-*`, `h-*`, and all spacing utilities |
| `--radius-*` | `rounded-*` |
| `--shadow-*` | `shadow-*` |
| `--inset-shadow-*` | `inset-shadow-*` |
| `--drop-shadow-*` | `drop-shadow-*` |
| `--blur-*` | `blur-*` |
| `--perspective-*` | `perspective-*` |
| `--aspect-*` | `aspect-*` |
| `--ease-*` | `ease-*` |
| `--animate-*` | `animate-*` |

### Overriding & Removing Defaults

```css
@theme {
  /* Override one value */
  --breakpoint-sm: 30rem;

  /* Remove entire namespace, then redefine */
  --color-*: initial;
  --color-white: #fff;
  --color-black: #000;
  --color-primary: oklch(0.6 0.2 260);

  /* Remove a single default */
  --breakpoint-2xl: initial;

  /* Reset everything (for fully custom themes) */
  --*: initial;
}
```

### Referencing Other Variables (use `inline`)

```css
@theme inline {
  --font-sans: var(--font-inter);
}
```

The `inline` option inlines the *value* rather than referencing the theme variable,
avoiding CSS variable resolution scope issues.

## CSS Directives

### `@source` — Register Additional Scan Paths

```css
@source "../node_modules/@my-company/ui-lib";
@source "../../packages/shared-components";
```

### `@source not()` — Ignore Paths

```css
@source not("./src/legacy");
```

### `@source inline()` — Safelist Classes

```css
@source inline("underline bg-red-500 lg:flex");
```

### `@utility` — Custom Utilities

```css
/* Simple utility */
@utility content-auto {
  content-visibility: auto;
}

/* With nesting */
@utility scrollbar-hidden {
  &::-webkit-scrollbar {
    display: none;
  }
}

/* Functional utility (accepts values) */
@utility tab-* {
  tab-size: --value(--tab-size-*);  /* Match theme keys */
}

@utility tab-* {
  tab-size: --value(integer);        /* Bare integer values: tab-4 */
}

/* Multiple resolvers (first match wins) */
@utility tab-* {
  tab-size: --value(--tab-size-*, integer, "inherit", "initial");
}
```

### `@custom-variant` — Custom Variants

```css
/* Class-based dark mode (replaces v3 darkMode: 'class') */
@custom-variant dark (&:where(.dark, .dark *));

/* Data attribute dark mode */
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));

/* Custom theme variant */
@custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

### `@variant` — Apply Variants in Custom CSS

```css
.my-element {
  background: white;
  @variant dark {
    background: black;
  }
  @variant hover {
    @variant dark {
      background: #333;
    }
  }
}
```

### `@layer` — Custom CSS in Layers

```css
@layer base {
  h1 { font-size: var(--text-2xl); }
  h2 { font-size: var(--text-xl); }
}

@layer components {
  .card {
    background-color: var(--color-white);
    border-radius: var(--radius-lg);
    padding: calc(var(--spacing) * 6);
    box-shadow: var(--shadow-xl);
  }
  .btn-primary {
    @apply rounded-lg bg-blue-600 px-4 py-2 font-semibold text-white;
    @apply hover:bg-blue-700 active:bg-blue-800;
    @apply focus:outline-2 focus:outline-offset-2 focus:outline-blue-500;
  }
}
```

### `@reference` — For Vue/Svelte `<style>` Blocks

```html
<style>
  @reference "../../app.css";
  h1 {
    @apply text-2xl font-bold text-red-500;
  }
</style>
```

### `@apply` — Inline Utility Classes in CSS

```css
.select2-dropdown {
  @apply rounded-b-lg shadow-md;
}
```

### Legacy Compatibility

```css
@config "../../tailwind.config.js";   /* Load v3 JS config */
@plugin "@tailwindcss/typography";     /* Load JS plugin */
```

## CSS Functions

```css
/* Adjust color opacity at build time */
.element { color: --alpha(var(--color-lime-300) / 50%); }

/* Generate spacing from theme multiplier */
.element { margin: --spacing(4); }  /* = calc(var(--spacing) * 4) */

/* In arbitrary values: */
<div class="py-[calc(--spacing(4)-1px)]">
```

## Responsive Design

### Default Breakpoints (Mobile-First)

| Prefix | Min Width | CSS |
|---|---|---|
| *(none)* | 0 | Base styles — apply to ALL sizes |
| `sm:` | 40rem (640px) | `@media (width >= 40rem)` |
| `md:` | 48rem (768px) | `@media (width >= 48rem)` |
| `lg:` | 64rem (1024px) | `@media (width >= 64rem)` |
| `xl:` | 80rem (1280px) | `@media (width >= 80rem)` |
| `2xl:` | 96rem (1536px) | `@media (width >= 96rem)` |

### Max-Width & Range Queries

```html
<div class="max-md:flex">          <!-- Below 768px only -->
<div class="md:max-xl:flex">       <!-- Between 768px and 1280px -->
<div class="min-[900px]:flex">     <!-- Arbitrary min-width -->
<div class="max-[600px]:hidden">   <!-- Arbitrary max-width -->
```

### Mobile-First Pattern

```html
<!-- CORRECT: style mobile first, override upward -->
<div class="text-center sm:text-left">

<!-- WRONG: don't use sm: to "target mobile" -->
<div class="sm:text-center">  <!-- This only applies at 640px+ -->
```

### Responsive Example

```html
<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
  <div class="rounded-lg bg-white p-4 shadow">Item</div>
  <!-- ... -->
</div>

<h1 class="text-2xl font-bold md:text-4xl lg:text-6xl">
  Responsive heading
</h1>

<div class="hidden lg:block">Desktop only</div>
<div class="lg:hidden">Mobile/tablet only</div>
```

## Container Queries (Built-In)

```html
<!-- Mark parent as container -->
<div class="@container">
  <!-- Style based on container width, not viewport -->
  <div class="flex flex-col @md:flex-row @md:items-center gap-4">
    <img class="w-full @md:w-48 rounded-lg" src="..." alt="">
    <div>
      <h3 class="text-lg font-bold">Title</h3>
      <p class="text-sm text-gray-500">Description</p>
    </div>
  </div>
</div>

<!-- Named containers for nested queries -->
<div class="@container/main">
  <div class="@sm/main:flex-row flex flex-col">...</div>
</div>

<!-- Max-width container queries -->
<div class="@container">
  <div class="flex flex-row @max-md:flex-col">...</div>
</div>

<!-- Range queries -->
<div class="@container">
  <div class="@sm:@max-md:flex-col">Between sm and md container</div>
</div>
```

## Dark Mode

### Automatic (System Preference — Default)

```html
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
  Switches with OS setting
</div>
```

### Manual Toggle (Class-Based)

```css
/* In your CSS */
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```

```html
<html class="dark">
  <body>
    <div class="bg-white dark:bg-gray-900">Now class-controlled</div>
  </body>
</html>
```

```javascript
// Toggle in JS
document.documentElement.classList.toggle('dark',
  localStorage.theme === 'dark' ||
  (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
);
```

### Data Attribute Approach

```css
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

```html
<html data-theme="dark">...</html>
```

## State Variants

### Interactive States

```html
<button class="bg-blue-600 hover:bg-blue-700 active:bg-blue-800
               focus:outline-2 focus:outline-offset-2 focus:outline-blue-500
               disabled:opacity-50 disabled:cursor-not-allowed
               transition-colors">
  Button
</button>

<a class="text-blue-600 hover:text-blue-800 hover:underline
          focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-500
          visited:text-purple-600">
  Link
</a>
```

### Form States

```html
<input class="border border-gray-300 rounded-lg px-3 py-2
              focus:border-blue-500 focus:ring-2 focus:ring-blue-200
              invalid:border-red-500 focus:invalid:ring-red-200
              disabled:bg-gray-100 disabled:cursor-not-allowed
              placeholder:text-gray-400 placeholder:italic
              read-only:bg-gray-50"
       required />

<input type="checkbox" class="checked:bg-blue-500 indeterminate:bg-gray-300" />
```

### Structural (Children)

```html
<ul>
  {items.map(item => (
    <li class="py-4 first:pt-0 last:pb-0 odd:bg-gray-50 even:bg-white">
      {item.name}
    </li>
  ))}
</ul>

<div class="nth-3:underline">3rd child underlined</div>
<div class="empty:hidden">Hidden when empty</div>
```

### Group (Parent State)

```html
<a href="#" class="group block rounded-lg p-6 hover:bg-gray-50">
  <h3 class="font-semibold group-hover:text-blue-600">Title</h3>
  <p class="text-gray-500 group-hover:text-gray-700">Description</p>
  <svg class="hidden group-has-[a]:block">...</svg>
</a>

<!-- Named groups for nesting -->
<div class="group/card">
  <div class="group/button">
    <span class="group-hover/card:text-blue-500
                 group-hover/button:underline">Text</span>
  </div>
</div>
```

### Peer (Sibling State)

```html
<label class="block">
  <input type="email" class="peer rounded border px-3 py-2" required />
  <p class="invisible mt-1 text-sm text-red-500 peer-invalid:visible">
    Please enter a valid email.
  </p>
</label>

<!-- Named peers -->
<input id="draft" class="peer/draft" type="radio" name="status" checked />
<div class="hidden peer-checked/draft:block">Draft selected</div>
```

### Implicit Group (`in-*`)

```html
<!-- No need to add "group" class to parent -->
<div tabindex="0">
  <div class="opacity-50 in-focus:opacity-100">
    Responds to any parent's focus
  </div>
</div>
```

### Has (Descendant State)

```html
<label class="has-checked:bg-indigo-50 has-checked:ring-indigo-200">
  <input type="radio" class="checked:border-indigo-500" />
  Google Pay
</label>
```

### Not

```html
<button class="bg-indigo-600 hover:not-focus:bg-indigo-700">
  Only hover styles when NOT focused
</button>
```

### Pseudo-Elements

```html
<div class="before:content-[''] before:absolute before:inset-0 before:bg-black/50">
  Overlay
</div>
<blockquote class="after:content-[attr(data-cite)]">Quote</blockquote>
<input class="placeholder:text-gray-400" placeholder="Search..." />
<li class="marker:text-blue-500">List item</li>
<p class="selection:bg-yellow-200">Selectable text</p>
<input type="file" class="file:mr-4 file:rounded-lg file:border-0 file:bg-blue-50 file:px-4 file:py-2" />
```

### Media & Feature Queries

```html
<div class="motion-safe:animate-bounce">Respects reduced motion</div>
<div class="motion-reduce:transition-none">No transitions if reduced motion</div>
<div class="contrast-more:border-2">Higher contrast borders</div>
<div class="print:hidden">Hidden when printing</div>
<div class="portrait:flex-col landscape:flex-row">Orientation-aware</div>
<div class="supports-[display:grid]:grid">Feature detection</div>
<div class="forced-colors:border">Forced colors mode</div>
```

### Data & ARIA Attributes

```html
<div class="data-[state=open]:bg-blue-50" data-state="open">Open</div>
<div class="aria-expanded:rotate-180" aria-expanded="true">Chevron</div>
<div class="aria-busy:opacity-50" aria-busy="true">Loading</div>
<details class="open:bg-gray-50" open>Expandable</details>
```

### Stacking Variants

```html
<button class="dark:md:hover:bg-indigo-600">
  Dark mode + medium screen + hover
</button>

<div class="dark:lg:data-[active]:hover:bg-fuchsia-600">
  Four stacked variants
</div>
```

### Arbitrary Variants

```html
<div class="[&>p]:mt-4">Direct child p tags</div>
<div class="[&_p]:mt-4">Any descendant p tags</div>
<div class="lg:[&:nth-child(-n+3)]:hover:underline">Complex selector</div>
<div class="[@supports(display:grid)]:grid">@supports</div>
```

## Spacing System

In v4, spacing uses a single `--spacing` multiplier (default `0.25rem`):

```
p-0    → padding: 0
p-px   → padding: 1px
p-0.5  → padding: calc(var(--spacing) * 0.5)  = 0.125rem
p-1    → padding: calc(var(--spacing) * 1)    = 0.25rem
p-2    → padding: calc(var(--spacing) * 2)    = 0.5rem
p-4    → padding: calc(var(--spacing) * 4)    = 1rem
p-8    → padding: calc(var(--spacing) * 8)    = 2rem
p-16   → 4rem, p-24 → 6rem, p-32 → 8rem, p-64 → 16rem, p-96 → 24rem
```

Any number works: `p-3.5`, `p-7`, `p-18`, `p-72`. The same scale applies to
margin, gap, width, height, inset, translate, scroll-margin, scroll-padding,
space-between, text-indent, border-spacing, and all spacing-based utilities.

## Arbitrary Values

```html
<div class="top-[117px]">               <!-- Any CSS value -->
<div class="bg-[#bada55]">              <!-- Hex color -->
<div class="text-[22px]">               <!-- Font size -->
<div class="grid-cols-[1fr_500px_2fr]"> <!-- Underscores = spaces -->
<div class="bg-[url('/img.png')]">      <!-- URLs -->
<div class="before:content-['Hello']">  <!-- Content strings -->
<div class="max-h-[calc(100dvh-4rem)]"> <!-- calc() -->
<div class="[mask-type:luminance]">     <!-- Arbitrary CSS property -->
<div class="[--my-var:1rem]">           <!-- CSS variable -->

<!-- CSS variable shorthand (v4): adds var() automatically -->
<div class="fill-(--my-brand-color)">   <!-- = fill-[var(--my-brand-color)] -->

<!-- Type hints for ambiguous variables -->
<div class="text-(length:--my-var)">    <!-- Force font-size interpretation -->
<div class="text-(color:--my-var)">     <!-- Force color interpretation -->
```

### Important Modifier

```html
<!-- v4: suffix ! -->
<div class="bg-red-500!">

<!-- v3 (WRONG in v4): prefix ! -->
<!-- <div class="!bg-red-500"> -->
```

### Opacity Modifier

```html
<div class="bg-red-500/50">        <!-- 50% opacity -->
<div class="bg-red-500/[.15]">    <!-- Arbitrary opacity -->
<div class="text-black/75">        <!-- 75% opacity text -->
```

### Negative Values

```html
<div class="-mt-4">                <!-- Negative margin -->
<div class="-translate-x-1/2">    <!-- Negative translate -->
<div class="-rotate-45">           <!-- Negative rotation -->
```

## Color System

### Default Palette

22 color families, each with shades 50–950:
`slate`, `gray`, `zinc`, `neutral`, `stone`, `red`, `orange`, `amber`,
`yellow`, `lime`, `green`, `emerald`, `teal`, `cyan`, `sky`, `blue`,
`indigo`, `violet`, `purple`, `fuchsia`, `pink`, `rose`.

Plus: `black`, `white`, `transparent`, `current`, `inherit`.

All default colors use **oklch** color space.

### Custom Colors

```css
@theme {
  --color-brand-50: oklch(0.97 0.02 264);
  --color-brand-500: oklch(0.55 0.22 264);
  --color-brand-900: oklch(0.25 0.15 264);
}
```

Now `bg-brand-500`, `text-brand-50`, `border-brand-900`, etc. all work.

## Complete Utility Reference

### Layout

| Classes | CSS Property |
|---|---|
| `block`, `inline-block`, `inline`, `flex`, `inline-flex`, `grid`, `inline-grid`, `table`, `contents`, `flow-root`, `list-item`, `hidden` | `display` |
| `aspect-auto`, `aspect-square`, `aspect-video`, `aspect-[4/3]` | `aspect-ratio` |
| `columns-1`–`columns-12`, `columns-auto`, `columns-3xs`–`columns-7xl` | `columns` |
| `box-border`, `box-content` | `box-sizing` |
| `float-start`, `float-end`, `float-right`, `float-left`, `float-none` | `float` |
| `clear-start`, `clear-end`, `clear-both`, `clear-none` | `clear` |
| `isolate`, `isolation-auto` | `isolation` |
| `object-contain`, `object-cover`, `object-fill`, `object-none`, `object-scale-down` | `object-fit` |
| `object-bottom`, `object-center`, `object-left`, `object-top`, etc. | `object-position` |
| `overflow-auto`, `overflow-hidden`, `overflow-clip`, `overflow-visible`, `overflow-scroll`, `overflow-x-*`, `overflow-y-*` | `overflow` |
| `overscroll-auto`, `overscroll-contain`, `overscroll-none` | `overscroll-behavior` |
| `static`, `fixed`, `absolute`, `relative`, `sticky` | `position` |
| `inset-*`, `inset-x-*`, `inset-y-*`, `top-*`, `right-*`, `bottom-*`, `left-*`, `start-*`, `end-*` | `inset` / TRBL |
| `visible`, `invisible`, `collapse` | `visibility` |
| `z-0`, `z-10`, `z-20`, `z-30`, `z-40`, `z-50`, `z-auto` | `z-index` |

### Flexbox & Grid

| Classes | CSS Property |
|---|---|
| `flex-row`, `flex-row-reverse`, `flex-col`, `flex-col-reverse` | `flex-direction` |
| `flex-wrap`, `flex-wrap-reverse`, `flex-nowrap` | `flex-wrap` |
| `flex-1`, `flex-auto`, `flex-initial`, `flex-none` | `flex` shorthand |
| `grow`, `grow-0` | `flex-grow` |
| `shrink`, `shrink-0` | `flex-shrink` |
| `basis-*` (numbers, `auto`, `full`, fractions) | `flex-basis` |
| `order-*` (1–12, `first`, `last`, `none`) | `order` |
| `grid-cols-*` (1–12, `none`, `subgrid`) | `grid-template-columns` |
| `grid-rows-*` (1–12, `none`, `subgrid`) | `grid-template-rows` |
| `col-span-*`, `col-start-*`, `col-end-*` | `grid-column` |
| `row-span-*`, `row-start-*`, `row-end-*` | `grid-row` |
| `grid-flow-row`, `grid-flow-col`, `grid-flow-dense` | `grid-auto-flow` |
| `auto-cols-auto`, `auto-cols-min`, `auto-cols-max`, `auto-cols-fr` | `grid-auto-columns` |
| `auto-rows-auto`, `auto-rows-min`, `auto-rows-max`, `auto-rows-fr` | `grid-auto-rows` |
| `gap-*`, `gap-x-*`, `gap-y-*` | `gap` |
| `justify-start`, `justify-end`, `justify-center`, `justify-between`, `justify-around`, `justify-evenly` | `justify-content` |
| `justify-items-start`, `justify-items-end`, `justify-items-center`, `justify-items-stretch` | `justify-items` |
| `justify-self-auto`, `justify-self-start`, `justify-self-end`, `justify-self-center` | `justify-self` |
| `items-start`, `items-end`, `items-center`, `items-baseline`, `items-stretch` | `align-items` |
| `content-center`, `content-start`, `content-end`, `content-between`, `content-around` | `align-content` |
| `self-auto`, `self-start`, `self-end`, `self-center`, `self-stretch` | `align-self` |
| `place-content-*`, `place-items-*`, `place-self-*` | Place shorthands |

### Sizing

| Classes | CSS Property |
|---|---|
| `w-*` (numbers, `auto`, `full`, `screen`, `dvw`, `svw`, `lvw`, `min`, `max`, `fit`, fractions) | `width` |
| `h-*` (numbers, `auto`, `full`, `screen`, `dvh`, `svh`, `lvh`, `min`, `max`, `fit`) | `height` |
| `size-*` (sets both width and height) | `width` + `height` |
| `min-w-*`, `max-w-*` (`none`, `full`, `min`, `max`, `fit`, `prose`, `screen-*`, container sizes) | `min/max-width` |
| `min-h-*`, `max-h-*` | `min/max-height` |

### Typography

| Classes | CSS Property |
|---|---|
| `font-sans`, `font-serif`, `font-mono` | `font-family` |
| `text-xs`–`text-9xl`, `text-sm/6` (combined size/line-height) | `font-size` |
| `font-thin`(100)–`font-black`(900) | `font-weight` |
| `italic`, `not-italic` | `font-style` |
| `antialiased`, `subpixel-antialiased` | `font-smoothing` |
| `tracking-tighter`–`tracking-widest` | `letter-spacing` |
| `leading-none`(1)–`leading-loose`(2) | `line-height` |
| `text-left`, `text-center`, `text-right`, `text-justify`, `text-start`, `text-end` | `text-align` |
| `text-*` (colors: `text-gray-900`, `text-blue-500/50`) | `color` |
| `underline`, `overline`, `line-through`, `no-underline` | `text-decoration-line` |
| `decoration-*` (color, style, thickness) | `text-decoration-*` |
| `uppercase`, `lowercase`, `capitalize`, `normal-case` | `text-transform` |
| `truncate`, `text-ellipsis`, `text-clip` | `text-overflow` |
| `text-wrap`, `text-nowrap`, `text-balance`, `text-pretty` | `text-wrap` |
| `line-clamp-1`–`line-clamp-6`, `line-clamp-none` | Line clamping |
| `whitespace-normal`, `whitespace-nowrap`, `whitespace-pre`, `whitespace-pre-line`, `whitespace-pre-wrap` | `white-space` |
| `break-normal`, `break-words`, `break-all`, `break-keep` | `word-break` |
| `list-none`, `list-disc`, `list-decimal`, `list-inside`, `list-outside` | `list-style` |
| `tabular-nums`, `oldstyle-nums`, `lining-nums`, `proportional-nums`, `slashed-zero`, `ordinal`, `diagonal-fractions`, `stacked-fractions` | `font-variant-numeric` |
| `indent-*` | `text-indent` |
| `align-baseline`, `align-top`, `align-middle`, `align-bottom` | `vertical-align` |
| `content-none`, `content-[value]` | `content` |

### Backgrounds

| Classes | CSS Property |
|---|---|
| `bg-*` (colors, opacity: `bg-red-500/50`) | `background-color` |
| `bg-none`, `bg-linear-to-t/tr/r/br/b/bl/l/tl`, `bg-radial-*`, `bg-conic-*` | `background-image` |
| `from-*`, `via-*`, `to-*` (gradient stops with colors + positions) | Gradient color stops |
| `bg-fixed`, `bg-local`, `bg-scroll` | `background-attachment` |
| `bg-clip-border`, `bg-clip-padding`, `bg-clip-content`, `bg-clip-text` | `background-clip` |
| `bg-auto`, `bg-cover`, `bg-contain` | `background-size` |
| `bg-center`, `bg-top`, `bg-bottom`, `bg-left`, `bg-right`, etc. | `background-position` |
| `bg-repeat`, `bg-no-repeat`, `bg-repeat-x`, `bg-repeat-y` | `background-repeat` |

### Borders

| Classes | CSS Property |
|---|---|
| `rounded-none`–`rounded-full`, per-side: `rounded-t-*`, `rounded-tl-*`, `rounded-s-*`, `rounded-ss-*` | `border-radius` |
| `border`, `border-0`, `border-2`, `border-4`, `border-8`, per-side: `border-t-*`, `border-x-*`, `border-y-*` | `border-width` |
| `border-*` (colors), per-side: `border-t-red-500` | `border-color` |
| `border-solid`, `border-dashed`, `border-dotted`, `border-double`, `border-hidden`, `border-none` | `border-style` |
| `outline`, `outline-0`–`outline-8` | `outline-width` |
| `outline-*` (colors) | `outline-color` |
| `outline-none`, `outline-dashed`, `outline-dotted`, `outline-double` | `outline-style` |
| `outline-offset-*` (0, 1, 2, 4, 8) | `outline-offset` |
| `ring`, `ring-0`–`ring-8`, `ring-inset`, `ring-*` (color) | Ring (box-shadow) |
| `divide-x-*`, `divide-y-*`, `divide-*` (color/style), `divide-x-reverse` | Border between children |

### Effects

| Classes | CSS Property |
|---|---|
| `shadow-2xs`–`shadow-2xl`, `shadow-inner`, `shadow-none`, `shadow-*` (color) | `box-shadow` |
| `text-shadow-2xs`–`text-shadow-lg`, `text-shadow-none` | `text-shadow` (**new in v4**) |
| `opacity-0`–`opacity-100` | `opacity` |
| `mix-blend-*` (normal, multiply, screen, overlay, etc.) | `mix-blend-mode` |
| `bg-blend-*` | `background-blend-mode` |
| `mask-*` (clip, composite, image, mode, origin, position, repeat, size, type) | CSS masks (**new in v4**) |
| `inset-shadow-*` | Inset box shadows (**new in v4**) |

### Filters

| Classes | CSS Property |
|---|---|
| `blur-none`, `blur-xs`–`blur-3xl` | `filter: blur()` |
| `brightness-0`–`brightness-200` | `filter: brightness()` |
| `contrast-0`–`contrast-200` | `filter: contrast()` |
| `grayscale`, `grayscale-0` | `filter: grayscale()` |
| `hue-rotate-0`–`hue-rotate-180` | `filter: hue-rotate()` |
| `invert`, `invert-0` | `filter: invert()` |
| `saturate-0`–`saturate-200` | `filter: saturate()` |
| `sepia`, `sepia-0` | `filter: sepia()` |
| `drop-shadow-none`–`drop-shadow-2xl` | `filter: drop-shadow()` |
| `backdrop-blur-*`, `backdrop-brightness-*`, `backdrop-contrast-*`, `backdrop-grayscale`, `backdrop-hue-rotate-*`, `backdrop-invert`, `backdrop-opacity-*`, `backdrop-saturate-*`, `backdrop-sepia` | `backdrop-filter` |

### Tables

| Classes | CSS Property |
|---|---|
| `border-collapse`, `border-separate` | `border-collapse` |
| `border-spacing-*`, `border-spacing-x-*`, `border-spacing-y-*` | `border-spacing` |
| `table-auto`, `table-fixed` | `table-layout` |
| `caption-top`, `caption-bottom` | `caption-side` |

### Transitions & Animations

| Classes | CSS Property |
|---|---|
| `transition` (default), `transition-all`, `transition-colors`, `transition-opacity`, `transition-shadow`, `transition-transform`, `transition-none` | `transition-property` |
| `transition-normal`, `transition-discrete` | `transition-behavior` |
| `duration-0`, `duration-75`, `duration-100`, `duration-150`, `duration-200`, `duration-300`, `duration-500`, `duration-700`, `duration-1000` | `transition-duration` |
| `ease-linear`, `ease-in`, `ease-out`, `ease-in-out` | `transition-timing-function` |
| `delay-*` (same as duration values) | `transition-delay` |
| `animate-spin`, `animate-ping`, `animate-pulse`, `animate-bounce`, `animate-none` | `animation` |

### Transforms

| Classes | CSS Property |
|---|---|
| `rotate-0`, `rotate-1`, `rotate-2`, `rotate-3`, `rotate-6`, `rotate-12`, `rotate-45`, `rotate-90`, `rotate-180`, `-rotate-*`, `rotate-x-*`, `rotate-y-*` | `rotate` |
| `scale-0`, `scale-50`, `scale-75`, `scale-90`, `scale-95`, `scale-100`, `scale-105`, `scale-110`, `scale-125`, `scale-150`, `scale-200`, `scale-x-*`, `scale-y-*` | `scale` |
| `skew-x-*`, `skew-y-*` | `skew` |
| `translate-x-*`, `translate-y-*`, `translate-z-*` (spacing scale + fractions) | `translate` |
| `origin-center`, `origin-top`, `origin-top-right`, etc. | `transform-origin` |
| `transform-gpu`, `transform-none` | `transform` |
| `transform-flat`, `transform-3d` | `transform-style` |
| `backface-visible`, `backface-hidden` | `backface-visibility` |
| `perspective-none`, `perspective-near`–`perspective-distant` | `perspective` |
| `perspective-origin-*` | `perspective-origin` |

### Interactivity

| Classes | CSS Property |
|---|---|
| `accent-*` (colors), `accent-auto` | `accent-color` |
| `appearance-none`, `appearance-auto` | `appearance` |
| `caret-*` (colors) | `caret-color` |
| `color-scheme-normal`, `color-scheme-dark`, `color-scheme-light`, `color-scheme-light-dark` | `color-scheme` |
| `cursor-auto`, `cursor-default`, `cursor-pointer`, `cursor-wait`, `cursor-text`, `cursor-move`, `cursor-help`, `cursor-not-allowed`, `cursor-none`, `cursor-grab`, `cursor-grabbing`, `cursor-col-resize`, `cursor-row-resize`, `cursor-zoom-in`, `cursor-zoom-out`, etc. | `cursor` |
| `field-sizing-content`, `field-sizing-fixed` | `field-sizing` (**new in v4**) |
| `pointer-events-none`, `pointer-events-auto` | `pointer-events` |
| `resize-none`, `resize`, `resize-x`, `resize-y` | `resize` |
| `scroll-auto`, `scroll-smooth` | `scroll-behavior` |
| `scroll-m-*`, `scroll-p-*` (all sides) | `scroll-margin`, `scroll-padding` |
| `snap-start`, `snap-end`, `snap-center`, `snap-align-none` | `scroll-snap-align` |
| `snap-normal`, `snap-always` | `scroll-snap-stop` |
| `snap-none`, `snap-x`, `snap-y`, `snap-both`, `snap-mandatory`, `snap-proximity` | `scroll-snap-type` |
| `touch-auto`, `touch-none`, `touch-pan-x`, `touch-pan-y`, `touch-pinch-zoom`, `touch-manipulation` | `touch-action` |
| `select-none`, `select-text`, `select-all`, `select-auto` | `user-select` |
| `will-change-auto`, `will-change-scroll`, `will-change-contents`, `will-change-transform` | `will-change` |

### SVG

| Classes | CSS Property |
|---|---|
| `fill-none`, `fill-current`, `fill-*` (colors) | `fill` |
| `stroke-none`, `stroke-current`, `stroke-*` (colors) | `stroke` |
| `stroke-0`, `stroke-1`, `stroke-2` | `stroke-width` |

### Accessibility

| Classes | Effect |
|---|---|
| `sr-only` | Screen-reader only (visually hidden, accessible) |
| `not-sr-only` | Reset sr-only |
| `forced-color-adjust-auto` | `forced-color-adjust: auto` |
| `forced-color-adjust-none` | `forced-color-adjust: none` |

## Source Detection Rules

**Never construct class names dynamically:**

```jsx
// ❌ WRONG — Tailwind cannot detect these
<div className={`bg-${color}-500`} />
<div className={`text-${size}`} />

// ✅ CORRECT — use complete class name strings
const colorMap = {
  red: "bg-red-500 text-white",
  blue: "bg-blue-500 text-white",
  green: "bg-green-500 text-white",
};
<div className={colorMap[color]} />

// ✅ CORRECT — ternary with complete strings
<div className={isActive ? "bg-blue-600 text-white" : "bg-gray-100 text-gray-700"} />
```

## Component Patterns

### Responsive Card

```html
<div class="mx-auto max-w-sm rounded-xl bg-white p-6 shadow-lg
            sm:max-w-md sm:p-8
            dark:bg-gray-800 dark:shadow-none
            dark:ring-1 dark:ring-white/10">
  <h2 class="text-xl font-bold text-gray-900 dark:text-white">Title</h2>
  <p class="mt-2 text-gray-600 dark:text-gray-400">Description.</p>
  <button class="mt-4 rounded-lg bg-blue-600 px-4 py-2 text-sm font-semibold text-white
                  hover:bg-blue-700 active:bg-blue-800
                  focus:outline-2 focus:outline-offset-2 focus:outline-blue-500
                  disabled:opacity-50 disabled:cursor-not-allowed
                  transition-colors">
    Action
  </button>
</div>
```

### Navigation Bar

```html
<nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200
            dark:bg-gray-900/80 dark:border-gray-800">
  <div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">
    <a href="/" class="text-xl font-bold text-gray-900 dark:text-white">Logo</a>
    <div class="hidden gap-6 sm:flex">
      <a href="#" class="text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white transition-colors">Home</a>
      <a href="#" class="text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white transition-colors">About</a>
    </div>
    <button class="sm:hidden rounded-md p-2 hover:bg-gray-100 dark:hover:bg-gray-800">
      <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
      </svg>
    </button>
  </div>
</nav>
```

### Form with Validation States

```html
<form class="mx-auto max-w-md space-y-6 rounded-xl bg-white p-8 shadow-lg dark:bg-gray-800">
  <div>
    <label class="mb-2 block text-sm font-medium text-gray-700 dark:text-gray-300" for="email">Email</label>
    <input type="email" id="email" required
           class="w-full rounded-lg border border-gray-300 px-4 py-2
                  focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:outline-none
                  invalid:border-red-500 focus:invalid:ring-red-200
                  disabled:bg-gray-100 disabled:cursor-not-allowed
                  placeholder:text-gray-400
                  dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-500"
           placeholder="you@example.com" />
  </div>
  <button type="submit"
          class="w-full rounded-lg bg-blue-600 py-3 font-bold text-white
                 hover:bg-blue-700 active:bg-blue-800 transition-colors
                 disabled:opacity-50 disabled:cursor-not-allowed">
    Sign In
  </button>
</form>
```

### Responsive Grid

```html
<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
  {items.map(item => (
    <div class="rounded-lg bg-white p-6 shadow-md hover:shadow-lg transition-shadow
                dark:bg-gray-800">
      {item.name}
    </div>
  ))}
</div>
```

## Best Practices

1. **Use `@theme` for all design tokens** — don't scatter arbitrary values; define them as theme variables
2. **Mobile-first always** — base styles are mobile, add `sm:`, `md:`, `lg:` for larger screens
3. **Dark mode from the start** — add `dark:` variants as you go, not as an afterthought
4. **Complete class strings only** — never interpolate partial class names
5. **Prefer utility classes over `@apply`** — extract components in your framework, not in CSS
6. **Use semantic color names** — `--color-primary`, `--color-danger` over raw palette references
7. **Keep spacing consistent** — use the spacing scale, reach for arbitrary values sparingly
8. **Accessibility always** — add `focus:`, `focus-visible:`, `sr-only`, `forced-color-adjust` as needed
9. **Use `@layer components`** for complex reusable styles — maintains proper specificity ordering
10. **Use container queries** for truly portable components that respond to their parent, not the viewport
