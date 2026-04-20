# Tailwind CSS v4 Reference for Claude Code SKILL.md

> **Purpose:** This document distills the official Tailwind CSS v4.x documentation into a
> comprehensive reference that Claude Code can use as source material when building a
> Tailwind CSS SKILL.md. Everything here is verified v4 syntax. Do NOT mix with v3
> patterns (e.g. `tailwind.config.js` for theme, `@tailwind base/components/utilities`,
> the old `theme()` function as primary API, `@apply` inside `@layer utilities`, etc.).

---

## 1. CRITICAL v4 vs v3 Differences

### What Changed in v4

| Area | v3 (OLD — do NOT use) | v4 (CURRENT) |
|------|----------------------|--------------|
| **Entry point** | `@tailwind base; @tailwind components; @tailwind utilities;` | `@import "tailwindcss";` |
| **Config file** | `tailwind.config.js` (primary) | `@theme` directive in CSS (primary). JS config only via `@config` for legacy compat. |
| **Theme customization** | `theme.extend` in JS config | `@theme { --color-brand: ...; }` in your CSS file |
| **Custom utilities** | `@layer utilities { .foo { ... } }` | `@utility foo { ... }` directive |
| **Custom variants** | `addVariant()` in plugin JS | `@custom-variant name (selector);` in CSS |
| **Applying variants in CSS** | Nested `@screen` or manual media queries | `@variant dark { ... }` directive |
| **Content/source detection** | `content: [...]` array in JS config | Automatic scanning + `@source` directive for additions |
| **Color format** | hex/rgb/hsl | oklch (default palette), any CSS color works |
| **Spacing system** | Fixed scale (0, 0.5, 1, 1.5, 2, ...) | `--spacing` multiplier: `p-4` = `calc(var(--spacing) * 4)`. Default `--spacing: 0.25rem` |
| **Breakpoints** | `screens` in config | `--breakpoint-*` theme variables |
| **Dark mode config** | `darkMode: 'class'` in config | `@custom-variant dark (&:where(.dark, .dark *));` |
| **`theme()` function** | Primary way to reference tokens in CSS | **Deprecated.** Use CSS variables: `var(--color-red-500)` |
| **Plugin loading** | `plugins: [require('...')]` in config | `@plugin "...";` directive |
| **Important flag** | `important: true` in config | `@import "tailwindcss" important;` |
| **Prefix** | `prefix: 'tw-'` in config | `@import "tailwindcss" prefix(tw);` |
| **Source path** | `content` array in config | `@import "tailwindcss" source("../src");` |
| **`@apply`** | Works anywhere | Still works, but for Vue/Svelte `<style>` blocks use `@reference` first |
| **Opacity modifier** | `bg-red-500/50` | Same syntax, still works |
| **CSS variable shorthand** | `bg-[var(--my-color)]` | `bg-(--my-color)` (shorthand adds `var()` automatically) |
| **Important modifier** | `!bg-red-500` | `bg-red-500!` (suffix, not prefix) |
| **Container queries** | Plugin required | Built-in: `@container`, `@sm`, `@md`, etc. |
| **`text-shadow`** | Not available | New utility: `text-shadow-sm`, `text-shadow-md`, etc. |
| **`mask-*` utilities** | Not available | Full mask utilities: `mask-image`, `mask-clip`, etc. |
| **`field-sizing`** | Not available | New: `field-sizing-content`, `field-sizing-fixed` |

### v4 Import Statement

```css
/* The single import that replaces all three @tailwind directives */
@import "tailwindcss";

/* With options: */
@import "tailwindcss" prefix(tw);
@import "tailwindcss" important;
@import "tailwindcss" source("../src");
```

This single import provides the `theme`, `base`, `components`, and `utilities` layers.

---

## 2. Theme System (`@theme` directive)

### Defining Theme Variables

Theme variables are special CSS variables defined with `@theme` that create corresponding utility classes:

```css
@import "tailwindcss";

@theme {
  /* Colors — creates bg-brand, text-brand, border-brand, etc. */
  --color-brand: oklch(0.72 0.11 178);
  --color-brand-light: oklch(0.85 0.08 178);

  /* Fonts — creates font-display utility */
  --font-display: "Satoshi", sans-serif;

  /* Spacing is a single multiplier — p-4 = calc(var(--spacing) * 4) */
  --spacing: 0.25rem;

  /* Breakpoints — creates sm:, md:, etc. variants */
  --breakpoint-xs: 30rem;
  --breakpoint-sm: 40rem;
  --breakpoint-md: 48rem;
  --breakpoint-lg: 64rem;
  --breakpoint-xl: 80rem;
  --breakpoint-2xl: 96rem;

  /* Containers — creates @sm, @md, etc. container query variants */
  --container-sm: 24rem;

  /* Shadows — creates shadow-soft utility */
  --shadow-soft: 0 2px 8px rgba(0,0,0,0.08);

  /* Border radius — creates rounded-lg utility */
  --radius-lg: 0.5rem;

  /* Animations — creates animate-fade-in utility */
  --animate-fade-in: fade-in 0.3s ease-out;
  @keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  /* Typography scale — creates text-display utility */
  --text-display: 3rem;

  /* Font weights — creates font-heading utility */
  --font-weight-heading: 700;

  /* Letter spacing — creates tracking-wide utility */
  --tracking-wide: 0.025em;

  /* Line height — creates leading-relaxed utility */
  --leading-relaxed: 1.75;

  /* Blur — creates blur-heavy utility */
  --blur-heavy: 40px;

  /* Easing — creates ease-snappy utility */
  --ease-snappy: cubic-bezier(0.2, 0, 0, 1);

  /* Perspective — creates perspective-dramatic utility */
  --perspective-dramatic: 200px;

  /* Aspect ratio — creates aspect-golden utility */
  --aspect-golden: 1.618 / 1;

  /* Drop shadow — creates drop-shadow-hard utility */
  --drop-shadow-hard: 0 2px 4px rgba(0,0,0,0.3);

  /* Inset shadow — creates inset-shadow-deep utility */
  --inset-shadow-deep: inset 0 4px 8px rgba(0,0,0,0.15);
}
```

### Theme Variable Namespaces → Utility Classes

| Namespace | What It Creates |
|-----------|----------------|
| `--color-*` | Color utilities: `bg-*`, `text-*`, `border-*`, `ring-*`, `fill-*`, `stroke-*`, `accent-*`, `caret-*`, `outline-*`, `shadow-*` (color), `decoration-*` |
| `--font-*` | `font-*` family utilities |
| `--text-*` | `text-*` size utilities |
| `--font-weight-*` | `font-*` weight utilities |
| `--tracking-*` | `tracking-*` letter-spacing utilities |
| `--leading-*` | `leading-*` line-height utilities |
| `--breakpoint-*` | Responsive variants: `sm:`, `md:`, `lg:`, etc. |
| `--container-*` | Container query variants: `@sm:`, `@md:`, and `max-w-*` size utilities |
| `--spacing-*` | Spacing utilities (padding, margin, gap, width, height, etc.) |
| `--radius-*` | `rounded-*` border-radius utilities |
| `--shadow-*` | `shadow-*` box-shadow utilities |
| `--inset-shadow-*` | `inset-shadow-*` utilities |
| `--drop-shadow-*` | `drop-shadow-*` filter utilities |
| `--blur-*` | `blur-*` filter utilities |
| `--perspective-*` | `perspective-*` utilities |
| `--aspect-*` | `aspect-*` aspect-ratio utilities |
| `--ease-*` | `ease-*` transition-timing utilities |
| `--animate-*` | `animate-*` animation utilities |

### Overriding & Removing Defaults

```css
@theme {
  /* Override a single value */
  --breakpoint-sm: 30rem;

  /* Remove an entire namespace — then redefine from scratch */
  --color-*: initial;
  --color-white: #fff;
  --color-black: #000;
  --color-primary: oklch(0.6 0.2 260);

  /* Remove a single value */
  --breakpoint-2xl: initial;
}
```

### Referencing Theme Variables in Custom CSS

```css
.my-element {
  /* Use the CSS variable directly */
  background-color: var(--color-brand);
  padding: var(--spacing);
  border-radius: var(--radius-lg);
}
```

### The `inline` Option

When theme variables reference other CSS variables, use `inline` to avoid resolution issues:

```css
@theme inline {
  --font-sans: var(--font-inter);
}
```

---

## 3. CSS Directives Reference (v4)

### `@import "tailwindcss"`
The single entry point. Replaces all v3 `@tailwind` directives.

### `@theme { ... }`
Define design tokens that generate utility classes. Must be top-level (not nested).

### `@source "path"`
Register additional source paths for class detection:
```css
@source "../node_modules/@my-company/ui-lib";
```

### `@utility name { ... }`
Register custom utility classes that work with all variants:
```css
@utility content-auto {
  content-visibility: auto;
}

/* Functional utilities with values */
@utility tab-* {
  tab-size: --value(--tab-size-*);
}

/* With bare value types */
@utility tab-* {
  tab-size: --value(integer);
}
```

### `@variant name { ... }`
Apply a Tailwind variant in custom CSS:
```css
.my-element {
  background: white;
  @variant dark {
    background: black;
  }
  @variant hover {
    background: gray;
  }
}
```

### `@custom-variant name (selector)`
Register a custom variant:
```css
@custom-variant dark (&:where(.dark, .dark *));
@custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

### `@apply`
Inline utility classes in custom CSS (still works in v4):
```css
.select2-dropdown {
  @apply rounded-b-lg shadow-md;
}
```

### `@reference "path"`
Import styles for reference only (no output). Required for `@apply` in Vue/Svelte `<style>` blocks:
```html
<style>
  @reference "../../app.css";
  h1 {
    @apply text-2xl font-bold text-red-500;
  }
</style>
```

### `@layer`
Place custom CSS in specific layers:
```css
@layer base {
  h1 { font-size: var(--text-2xl); }
}

@layer components {
  .card {
    background-color: var(--color-white);
    border-radius: var(--radius-lg);
    padding: calc(var(--spacing) * 6);
    box-shadow: var(--shadow-xl);
  }
}
```

### `@config` (legacy compatibility)
Load a v3-style JavaScript config:
```css
@config "../../tailwind.config.js";
```

### `@plugin` (legacy compatibility)
Load a JavaScript plugin:
```css
@plugin "@tailwindcss/typography";
```

---

## 4. CSS Functions Reference (v4)

### `--alpha(color / opacity)`
Adjust color opacity at build time:
```css
.my-element {
  color: --alpha(var(--color-lime-300) / 50%);
}
/* Compiles to: color: color-mix(in oklab, var(--color-lime-300) 50%, transparent); */
```

### `--spacing(multiplier)`
Generate spacing values from theme:
```css
.my-element {
  margin: --spacing(4);
}
/* Compiles to: margin: calc(var(--spacing) * 4); */
```

### `--value()` (inside `@utility`)
Resolve values for functional utilities:
```css
@utility tab-* {
  tab-size: --value(--tab-size-*);        /* Match theme keys */
  tab-size: --value(integer);              /* Bare integer value */
  tab-size: --value("inherit", "initial"); /* Literal strings */
}

/* Combining multiple resolvers — first match wins */
@utility tab-* {
  tab-size: --value(--tab-size-*, integer);
}
```

---

## 5. Variants Reference (All v4 Variants)

### Pseudo-class Variants
| Variant | CSS | Notes |
|---------|-----|-------|
| `hover:` | `&:hover` | Wrapped in `@media (hover: hover)` |
| `focus:` | `&:focus` | |
| `focus-within:` | `&:focus-within` | |
| `focus-visible:` | `&:focus-visible` | |
| `active:` | `&:active` | |
| `visited:` | `&:visited` | |
| `target:` | `&:target` | |
| `first:` | `&:first-child` | |
| `last:` | `&:last-child` | |
| `only:` | `&:only-child` | |
| `odd:` | `&:nth-child(odd)` | |
| `even:` | `&:nth-child(even)` | |
| `first-of-type:` | `&:first-of-type` | |
| `last-of-type:` | `&:last-of-type` | |
| `only-of-type:` | `&:only-of-type` | |
| `empty:` | `&:empty` | |
| `disabled:` | `&:disabled` | |
| `enabled:` | `&:enabled` | |
| `checked:` | `&:checked` | |
| `indeterminate:` | `&:indeterminate` | |
| `default:` | `&:default` | |
| `required:` | `&:required` | |
| `valid:` | `&:valid` | |
| `invalid:` | `&:invalid` | |
| `in-range:` | `&:in-range` | |
| `out-of-range:` | `&:out-of-range` | |
| `placeholder-shown:` | `&:placeholder-shown` | |
| `autofill:` | `&:autofill` | |
| `read-only:` | `&:read-only` | |
| `nth-*:` | `&:nth-child(*)` | e.g. `nth-3:`, `nth-[2n+1]:` |
| `nth-last-*:` | `&:nth-last-child(*)` | |
| `nth-of-type-*:` | `&:nth-of-type(*)` | |
| `has-*:` | `&:has(*)` | e.g. `has-checked:`, `has-[:focus]:`, `has-[img]:` |
| `not-*:` | `&:not(*)` | e.g. `not-focus:`, `not-last:` |

### Pseudo-element Variants
| Variant | CSS |
|---------|-----|
| `before:` | `&::before` (auto-adds `content: ''`) |
| `after:` | `&::after` (auto-adds `content: ''`) |
| `placeholder:` | `&::placeholder` |
| `file:` | `&::file-selector-button` |
| `marker:` | `&::marker` |
| `selection:` | `&::selection` |
| `first-line:` | `&::first-line` |
| `first-letter:` | `&::first-letter` |
| `backdrop:` | `&::backdrop` |

### Responsive Breakpoint Variants (default)
| Variant | Min-width | CSS |
|---------|-----------|-----|
| `sm:` | 40rem (640px) | `@media (width >= 40rem)` |
| `md:` | 48rem (768px) | `@media (width >= 48rem)` |
| `lg:` | 64rem (1024px) | `@media (width >= 64rem)` |
| `xl:` | 80rem (1280px) | `@media (width >= 80rem)` |
| `2xl:` | 96rem (1536px) | `@media (width >= 96rem)` |
| `max-sm:` | < 40rem | `@media (width < 40rem)` |
| `max-md:` | < 48rem | `@media (width < 48rem)` |
| `max-lg:` | < 64rem | `@media (width < 64rem)` |
| `max-xl:` | < 80rem | `@media (width < 80rem)` |
| `max-2xl:` | < 96rem | `@media (width < 96rem)` |
| `min-[value]:` | Arbitrary | `@media (width >= value)` |
| `max-[value]:` | Arbitrary | `@media (width < value)` |

**Breakpoint ranges:** `md:max-xl:flex` = apply only between md and xl.

### Dark Mode
| Variant | Default behavior |
|---------|-----------------|
| `dark:` | `@media (prefers-color-scheme: dark)` |

Override for class-based: `@custom-variant dark (&:where(.dark, .dark *));`
Override for data attribute: `@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));`

### Container Query Variants
| Variant | Container size |
|---------|---------------|
| `@container` | Mark parent as container |
| `@sm:` | Container ≥ size |
| `@md:`, `@lg:`, etc. | Ascending sizes |
| `@max-sm:` | Container < size |
| `@container/{name}` | Named container |
| `@sm/{name}:` | Query named container |
| `@min-[value]:` | Arbitrary container query |

### Group & Peer Variants
| Pattern | Usage |
|---------|-------|
| `group-hover:` | Style child when parent `.group` is hovered |
| `group-focus:` | Style child when parent `.group` is focused |
| `group/{name}` | Named groups for nesting: `group/card` |
| `group-hover/{name}:` | Target specific named group |
| `group-has-*:` | Style based on group's descendants |
| `group-[.is-active]:` | Arbitrary group selector |
| `peer-invalid:` | Style element based on sibling `.peer` state |
| `peer/{name}` | Named peers |
| `peer-checked/{name}:` | Target specific named peer |
| `peer-has-*:` | Style based on peer's descendants |
| `in-*:` | Implicit group (no `group` class needed on parent) |

### Media & Feature Query Variants
| Variant | CSS |
|---------|-----|
| `motion-safe:` | `@media (prefers-reduced-motion: no-preference)` |
| `motion-reduce:` | `@media (prefers-reduced-motion: reduce)` |
| `contrast-more:` | `@media (prefers-contrast: more)` |
| `contrast-less:` | `@media (prefers-contrast: less)` |
| `forced-colors:` | `@media (forced-colors: active)` |
| `portrait:` | `@media (orientation: portrait)` |
| `landscape:` | `@media (orientation: landscape)` |
| `print:` | `@media print` |
| `supports-[...]:` | `@supports (...)` |

### Data & ARIA Attribute Variants
| Pattern | CSS |
|---------|-----|
| `data-[active]:` | `&[data-active]` |
| `data-[state=open]:` | `&[data-state=open]` |
| `aria-[expanded=true]:` | `&[aria-expanded=true]` |
| `aria-busy:` | `&[aria-busy=true]` |
| `aria-checked:` | `&[aria-checked=true]` |
| `aria-disabled:` | `&[aria-disabled=true]` |
| `aria-hidden:` | `&[aria-hidden=true]` |
| `aria-pressed:` | `&[aria-pressed=true]` |
| `aria-readonly:` | `&[aria-readonly=true]` |
| `aria-required:` | `&[aria-required=true]` |
| `aria-selected:` | `&[aria-selected=true]` |
| `open:` | `&[open]` |

### Stacking Variants
Variants can be stacked: `dark:md:hover:bg-indigo-600`
Order doesn't matter semantically but conventionally: responsive → feature → state → pseudo-element.

### Arbitrary Variants
```html
<div class="[&>p]:mt-4">            <!-- Direct child p tags -->
<div class="[&_p]:mt-4">             <!-- Any descendant p tags -->
<div class="[@supports(display:grid)]:grid"> <!-- Arbitrary @supports -->
<div class="[@media(width>=900px)]:flex">    <!-- Arbitrary media query -->
```

---

## 6. Complete Utility Class Reference (v4)

### Layout

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `aspect-*` | `aspect-ratio` | `aspect-auto`, `aspect-square`, `aspect-video`, `aspect-[4/3]` |
| `columns-*` | `columns` | `columns-1` to `columns-12`, `columns-auto`, `columns-3xs` to `columns-7xl`, `columns-[value]` |
| `break-after-*` | `break-after` | `break-after-auto`, `break-after-avoid`, `break-after-all`, `break-after-avoid-page`, `break-after-page`, `break-after-column` |
| `break-before-*` | `break-before` | Same patterns as break-after |
| `break-inside-*` | `break-inside` | `break-inside-auto`, `break-inside-avoid`, `break-inside-avoid-page`, `break-inside-avoid-column` |
| `box-decoration-*` | `box-decoration-break` | `box-decoration-clone`, `box-decoration-slice` |
| `box-*` | `box-sizing` | `box-border`, `box-content` |
| Display | `display` | `block`, `inline-block`, `inline`, `flex`, `inline-flex`, `table`, `inline-table`, `table-caption`, `table-cell`, `table-column`, `table-column-group`, `table-footer-group`, `table-header-group`, `table-row-group`, `table-row`, `flow-root`, `grid`, `inline-grid`, `contents`, `list-item`, `hidden` (display:none) |
| `float-*` | `float` | `float-start`, `float-end`, `float-right`, `float-left`, `float-none` |
| `clear-*` | `clear` | `clear-start`, `clear-end`, `clear-right`, `clear-left`, `clear-both`, `clear-none` |
| `isolation-*` | `isolation` | `isolate`, `isolation-auto` |
| `object-*` | `object-fit` | `object-contain`, `object-cover`, `object-fill`, `object-none`, `object-scale-down` |
| `object-*` | `object-position` | `object-bottom`, `object-center`, `object-left`, `object-left-bottom`, `object-left-top`, `object-right`, `object-right-bottom`, `object-right-top`, `object-top` |
| `overflow-*` | `overflow` | `overflow-auto`, `overflow-hidden`, `overflow-clip`, `overflow-visible`, `overflow-scroll`, `overflow-x-*`, `overflow-y-*` |
| `overscroll-*` | `overscroll-behavior` | `overscroll-auto`, `overscroll-contain`, `overscroll-none`, `overscroll-x-*`, `overscroll-y-*` |
| Position | `position` | `static`, `fixed`, `absolute`, `relative`, `sticky` |
| Inset / TRBL | `top/right/bottom/left/inset` | `inset-*`, `inset-x-*`, `inset-y-*`, `start-*`, `end-*`, `top-*`, `right-*`, `bottom-*`, `left-*`. Values: numbers (spacing scale), `auto`, `px`, `full`, `1/2`, `1/3`, `2/3`, `1/4`, `3/4` |
| `visible`/`invisible`/`collapse` | `visibility` | |
| `z-*` | `z-index` | `z-0`, `z-10`, `z-20`, `z-30`, `z-40`, `z-50`, `z-auto`, `z-[value]` |

### Flexbox & Grid

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `basis-*` | `flex-basis` | `basis-0` through numbers, `basis-auto`, `basis-full`, fractions, `basis-[value]` |
| `flex-row`, `flex-col`, etc. | `flex-direction` | `flex-row`, `flex-row-reverse`, `flex-col`, `flex-col-reverse` |
| `flex-wrap`, etc. | `flex-wrap` | `flex-wrap`, `flex-wrap-reverse`, `flex-nowrap` |
| `flex-*` | `flex` shorthand | `flex-1` (1 1 0%), `flex-auto` (1 1 auto), `flex-initial` (0 1 auto), `flex-none` (none) |
| `grow-*` | `flex-grow` | `grow` (1), `grow-0` |
| `shrink-*` | `flex-shrink` | `shrink` (1), `shrink-0` |
| `order-*` | `order` | `order-1` to `order-12`, `order-first` (-9999), `order-last` (9999), `order-none` (0) |
| `grid-cols-*` | `grid-template-columns` | `grid-cols-1` to `grid-cols-12`, `grid-cols-none`, `grid-cols-subgrid`, `grid-cols-[value]` |
| `col-span-*` | `grid-column` | `col-auto`, `col-span-1` to `col-span-12`, `col-span-full`, `col-start-*`, `col-end-*` |
| `grid-rows-*` | `grid-template-rows` | `grid-rows-1` to `grid-rows-12`, `grid-rows-none`, `grid-rows-subgrid` |
| `row-span-*` | `grid-row` | `row-auto`, `row-span-1` to `row-span-12`, `row-span-full`, `row-start-*`, `row-end-*` |
| `grid-flow-*` | `grid-auto-flow` | `grid-flow-row`, `grid-flow-col`, `grid-flow-dense`, `grid-flow-row-dense`, `grid-flow-col-dense` |
| `auto-cols-*` | `grid-auto-columns` | `auto-cols-auto`, `auto-cols-min`, `auto-cols-max`, `auto-cols-fr` |
| `auto-rows-*` | `grid-auto-rows` | `auto-rows-auto`, `auto-rows-min`, `auto-rows-max`, `auto-rows-fr` |
| `gap-*` | `gap` | `gap-0` to numbers, `gap-px`, `gap-x-*`, `gap-y-*` |
| `justify-*` | `justify-content` | `justify-normal`, `justify-start`, `justify-end`, `justify-center`, `justify-between`, `justify-around`, `justify-evenly`, `justify-stretch` |
| `justify-items-*` | `justify-items` | `justify-items-start`, `justify-items-end`, `justify-items-center`, `justify-items-stretch`, `justify-items-normal` |
| `justify-self-*` | `justify-self` | `justify-self-auto`, `justify-self-start`, `justify-self-end`, `justify-self-center`, `justify-self-stretch` |
| `content-*` | `align-content` | `content-normal`, `content-center`, `content-start`, `content-end`, `content-between`, `content-around`, `content-evenly`, `content-baseline`, `content-stretch` |
| `items-*` | `align-items` | `items-start`, `items-end`, `items-center`, `items-baseline`, `items-stretch` |
| `self-*` | `align-self` | `self-auto`, `self-start`, `self-end`, `self-center`, `self-stretch`, `self-baseline` |
| `place-content-*` | `place-content` | `place-content-center`, `place-content-start`, `place-content-end`, `place-content-between`, `place-content-around`, `place-content-evenly`, `place-content-baseline`, `place-content-stretch` |
| `place-items-*` | `place-items` | `place-items-start`, `place-items-end`, `place-items-center`, `place-items-baseline`, `place-items-stretch` |
| `place-self-*` | `place-self` | `place-self-auto`, `place-self-start`, `place-self-end`, `place-self-center`, `place-self-stretch` |

### Spacing

| Utility Pattern | CSS Property | Value System |
|----------------|-------------|-------------|
| `p-*`, `px-*`, `py-*`, `ps-*`, `pe-*`, `pt-*`, `pr-*`, `pb-*`, `pl-*` | `padding` | Number (spacing scale): `p-4` = `calc(var(--spacing) * 4)`. Also: `p-px` (1px), `p-[value]` |
| `m-*`, `mx-*`, `my-*`, `ms-*`, `me-*`, `mt-*`, `mr-*`, `mb-*`, `ml-*` | `margin` | Same as padding, plus `m-auto`, negative values with `-m-4` |
| `space-x-*`, `space-y-*` | Margin between children | `space-x-4`, `space-y-2`, `space-x-reverse` |

### Sizing

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `w-*` | `width` | Numbers, `w-auto`, `w-full` (100%), `w-screen` (100vw), `w-dvw`, `w-svw`, `w-lvw`, `w-min`, `w-max`, `w-fit`, fractions (`w-1/2`, `w-1/3`, etc.), `w-[value]` |
| `min-w-*` | `min-width` | `min-w-0`, `min-w-full`, `min-w-min`, `min-w-max`, `min-w-fit`, numbers |
| `max-w-*` | `max-width` | `max-w-none`, `max-w-full`, `max-w-min`, `max-w-max`, `max-w-fit`, `max-w-prose` (65ch), `max-w-screen-sm/md/lg/xl/2xl`, named sizes from `--container-*` |
| `h-*` | `height` | Same pattern as width: numbers, `h-auto`, `h-full`, `h-screen`, `h-dvh`, `h-svh`, `h-lvh`, `h-min`, `h-max`, `h-fit` |
| `min-h-*` | `min-height` | `min-h-0`, `min-h-full`, `min-h-screen`, `min-h-dvh`, `min-h-svh`, `min-h-lvh`, `min-h-min`, `min-h-max`, `min-h-fit` |
| `max-h-*` | `max-height` | Same patterns |
| `size-*` | `width` + `height` | Shorthand: `size-12` sets both width and height. Same values as width. |
| Logical properties | `inline-size`, `block-size`, `min-inline-size`, `max-inline-size`, `min-block-size`, `max-block-size` | Same patterns using logical direction names |

### Typography

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `font-*` | `font-family` | `font-sans`, `font-serif`, `font-mono`, custom via `--font-*` |
| `text-*` | `font-size` | `text-xs` (0.75rem), `text-sm` (0.875rem), `text-base` (1rem), `text-lg` (1.125rem), `text-xl` (1.25rem), `text-2xl` to `text-9xl`. **Combined line-height:** `text-sm/6` = font-size 0.875rem + line-height 1.5rem |
| `antialiased` / `subpixel-antialiased` | `font-smoothing` | |
| `italic` / `not-italic` | `font-style` | |
| `font-*` | `font-weight` | `font-thin` (100), `font-extralight` (200), `font-light` (300), `font-normal` (400), `font-medium` (500), `font-semibold` (600), `font-bold` (700), `font-extrabold` (800), `font-black` (900) |
| `font-stretch-*` | `font-stretch` | `font-stretch-ultra-condensed` to `font-stretch-ultra-expanded`, percentages |
| `tabular-nums`, `oldstyle-nums`, etc. | `font-variant-numeric` | `normal-nums`, `ordinal`, `slashed-zero`, `lining-nums`, `oldstyle-nums`, `proportional-nums`, `tabular-nums`, `diagonal-fractions`, `stacked-fractions` |
| `tracking-*` | `letter-spacing` | `tracking-tighter`, `tracking-tight`, `tracking-normal`, `tracking-wide`, `tracking-wider`, `tracking-widest` |
| `line-clamp-*` | Line clamping | `line-clamp-1` to `line-clamp-6`, `line-clamp-none` |
| `leading-*` | `line-height` | `leading-none` (1), `leading-tight` (1.25), `leading-snug` (1.375), `leading-normal` (1.5), `leading-relaxed` (1.625), `leading-loose` (2), numbers |
| `list-*` | `list-style-type` | `list-none`, `list-disc`, `list-decimal`, `list-[value]` |
| `list-inside` / `list-outside` | `list-style-position` | |
| `text-left`, `text-center`, etc. | `text-align` | `text-left`, `text-center`, `text-right`, `text-justify`, `text-start`, `text-end` |
| `text-*` | `color` | `text-inherit`, `text-current`, `text-transparent`, `text-black`, `text-white`, color scale: `text-red-500`, etc. Opacity: `text-red-500/50` |
| `underline`, `overline`, `line-through`, `no-underline` | `text-decoration-line` | |
| `decoration-*` | `text-decoration-color` | `decoration-inherit`, `decoration-current`, `decoration-transparent`, color scale |
| `decoration-*` | `text-decoration-style` | `decoration-solid`, `decoration-double`, `decoration-dotted`, `decoration-dashed`, `decoration-wavy` |
| `decoration-*` | `text-decoration-thickness` | `decoration-auto`, `decoration-from-font`, `decoration-0` to `decoration-8` |
| `underline-offset-*` | `text-underline-offset` | `underline-offset-auto`, `underline-offset-0` to `underline-offset-8` |
| `uppercase`, `lowercase`, `capitalize`, `normal-case` | `text-transform` | |
| `truncate`, `text-ellipsis`, `text-clip` | `text-overflow` | |
| `text-wrap`, `text-nowrap`, `text-balance`, `text-pretty` | `text-wrap` | |
| `indent-*` | `text-indent` | Numbers (spacing scale) |
| `align-*` | `vertical-align` | `align-baseline`, `align-top`, `align-middle`, `align-bottom`, `align-text-top`, `align-text-bottom`, `align-sub`, `align-super` |
| `whitespace-*` | `white-space` | `whitespace-normal`, `whitespace-nowrap`, `whitespace-pre`, `whitespace-pre-line`, `whitespace-pre-wrap`, `whitespace-break-spaces` |
| `break-*` | `word-break` | `break-normal`, `break-words`, `break-all`, `break-keep` |
| `wrap-*` | `overflow-wrap` | `wrap-break-word`, `wrap-anywhere`, `wrap-normal` |
| `hyphens-*` | `hyphens` | `hyphens-none`, `hyphens-manual`, `hyphens-auto` |
| `content-*` | `content` | `content-none`, `content-[value]` |

### Backgrounds

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `bg-fixed`, `bg-local`, `bg-scroll` | `background-attachment` | |
| `bg-clip-*` | `background-clip` | `bg-clip-border`, `bg-clip-padding`, `bg-clip-content`, `bg-clip-text` |
| `bg-*` | `background-color` | `bg-inherit`, `bg-current`, `bg-transparent`, `bg-black`, `bg-white`, color scale. Opacity: `bg-red-500/50` |
| `bg-*` | `background-image` | `bg-none`, `bg-linear-to-t/tr/r/br/b/bl/l/tl` (linear gradients), `bg-radial-*`, `bg-conic-*`, `bg-[url('...')]` |
| Gradient color stops | | `from-*`, `via-*`, `to-*` with colors and positions: `from-red-500`, `from-10%`, `via-blue-500`, `via-50%`, `to-green-500` |
| `bg-origin-*` | `background-origin` | `bg-origin-border`, `bg-origin-padding`, `bg-origin-content` |
| `bg-*` | `background-position` | `bg-bottom`, `bg-center`, `bg-left`, `bg-left-bottom`, `bg-left-top`, `bg-right`, `bg-right-bottom`, `bg-right-top`, `bg-top` |
| `bg-repeat`, `bg-no-repeat`, etc. | `background-repeat` | `bg-repeat`, `bg-no-repeat`, `bg-repeat-x`, `bg-repeat-y`, `bg-repeat-round`, `bg-repeat-space` |
| `bg-*` | `background-size` | `bg-auto`, `bg-cover`, `bg-contain` |

### Borders

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `rounded-*` | `border-radius` | `rounded-none` (0), `rounded-sm`, `rounded` (default), `rounded-md`, `rounded-lg`, `rounded-xl`, `rounded-2xl`, `rounded-3xl`, `rounded-full` (9999px). Per-side: `rounded-t-*`, `rounded-r-*`, `rounded-b-*`, `rounded-l-*`, `rounded-tl-*`, `rounded-tr-*`, `rounded-br-*`, `rounded-bl-*`, `rounded-s-*`, `rounded-e-*`, `rounded-ss-*`, `rounded-se-*`, `rounded-es-*`, `rounded-ee-*` |
| `border-*` | `border-width` | `border` (1px), `border-0`, `border-2`, `border-4`, `border-8`. Per-side: `border-t-*`, `border-r-*`, `border-b-*`, `border-l-*`, `border-s-*`, `border-e-*`, `border-x-*`, `border-y-*` |
| `border-*` | `border-color` | `border-inherit`, `border-current`, `border-transparent`, color scale. Per-side: `border-t-red-500`, etc. |
| `border-*` | `border-style` | `border-solid`, `border-dashed`, `border-dotted`, `border-double`, `border-hidden`, `border-none` |
| `outline-*` | `outline-width` | `outline`, `outline-0`, `outline-1`, `outline-2`, `outline-4`, `outline-8` |
| `outline-*` | `outline-color` | Color scale |
| `outline-*` | `outline-style` | `outline`, `outline-none`, `outline-dashed`, `outline-dotted`, `outline-double` |
| `outline-offset-*` | `outline-offset` | `outline-offset-0`, `outline-offset-1`, `outline-offset-2`, `outline-offset-4`, `outline-offset-8` |
| `ring-*` | `box-shadow` (ring) | `ring` (3px), `ring-0`, `ring-1`, `ring-2`, `ring-4`, `ring-8`, `ring-inset`. Color: `ring-blue-500` |
| `divide-*` | Border between children | `divide-x-*`, `divide-y-*`, `divide-*` (color), `divide-solid/dashed/dotted/double/none`, `divide-x-reverse`, `divide-y-reverse` |

### Effects

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `shadow-*` | `box-shadow` | `shadow-2xs`, `shadow-xs`, `shadow-sm`, `shadow` (default), `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`, `shadow-none`, `shadow-inner` (inset). Color: `shadow-red-500/50` |
| `text-shadow-*` | `text-shadow` | `text-shadow-2xs`, `text-shadow-xs`, `text-shadow-sm`, `text-shadow` (default), `text-shadow-md`, `text-shadow-lg`, `text-shadow-none` |
| `opacity-*` | `opacity` | `opacity-0` to `opacity-100` (in steps of 5), `opacity-[value]` |
| `mix-blend-*` | `mix-blend-mode` | `mix-blend-normal`, `mix-blend-multiply`, `mix-blend-screen`, `mix-blend-overlay`, `mix-blend-darken`, `mix-blend-lighten`, `mix-blend-color-dodge`, `mix-blend-color-burn`, `mix-blend-hard-light`, `mix-blend-soft-light`, `mix-blend-difference`, `mix-blend-exclusion`, `mix-blend-hue`, `mix-blend-saturation`, `mix-blend-color`, `mix-blend-luminosity`, `mix-blend-plus-lighter` |
| `bg-blend-*` | `background-blend-mode` | Same modes as mix-blend |
| `mask-*` | Mask utilities | `mask-clip-*`, `mask-composite-*`, `mask-image-*`, `mask-mode-*`, `mask-origin-*`, `mask-position-*`, `mask-repeat-*`, `mask-size-*`, `mask-type-*` |

### Filters

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `blur-*` | `filter: blur()` | `blur-none`, `blur-xs` (2px), `blur-sm` (4px), `blur` (8px), `blur-md` (12px), `blur-lg` (16px), `blur-xl` (24px), `blur-2xl` (40px), `blur-3xl` (64px) |
| `brightness-*` | `filter: brightness()` | `brightness-0` to `brightness-200` |
| `contrast-*` | `filter: contrast()` | `contrast-0` to `contrast-200` |
| `drop-shadow-*` | `filter: drop-shadow()` | `drop-shadow-none`, `drop-shadow-xs`, `drop-shadow-sm`, `drop-shadow` (default), `drop-shadow-md`, `drop-shadow-lg`, `drop-shadow-xl`, `drop-shadow-2xl` |
| `grayscale` / `grayscale-0` | `filter: grayscale()` | |
| `hue-rotate-*` | `filter: hue-rotate()` | `hue-rotate-0` to `hue-rotate-180` |
| `invert` / `invert-0` | `filter: invert()` | |
| `saturate-*` | `filter: saturate()` | `saturate-0` to `saturate-200` |
| `sepia` / `sepia-0` | `filter: sepia()` | |
| `backdrop-blur-*` | `backdrop-filter: blur()` | Same scale as blur |
| `backdrop-brightness-*` | `backdrop-filter: brightness()` | |
| `backdrop-contrast-*` | `backdrop-filter: contrast()` | |
| `backdrop-grayscale` | `backdrop-filter: grayscale()` | |
| `backdrop-hue-rotate-*` | `backdrop-filter: hue-rotate()` | |
| `backdrop-invert` | `backdrop-filter: invert()` | |
| `backdrop-opacity-*` | `backdrop-filter: opacity()` | |
| `backdrop-saturate-*` | `backdrop-filter: saturate()` | |
| `backdrop-sepia` | `backdrop-filter: sepia()` | |

### Tables

| Utility | CSS |
|---------|-----|
| `border-collapse` | `border-collapse: collapse` |
| `border-separate` | `border-collapse: separate` |
| `border-spacing-*` | `border-spacing`. Per-axis: `border-spacing-x-*`, `border-spacing-y-*` |
| `table-auto` | `table-layout: auto` |
| `table-fixed` | `table-layout: fixed` |
| `caption-top` | `caption-side: top` |
| `caption-bottom` | `caption-side: bottom` |

### Transitions & Animations

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `transition-*` | `transition-property` | `transition` (default set), `transition-all`, `transition-colors`, `transition-opacity`, `transition-shadow`, `transition-transform`, `transition-none` |
| `transition-*` | `transition-behavior` | `transition-normal`, `transition-discrete` |
| `duration-*` | `transition-duration` | `duration-0`, `duration-75`, `duration-100`, `duration-150`, `duration-200`, `duration-300`, `duration-500`, `duration-700`, `duration-1000` |
| `ease-*` | `transition-timing-function` | `ease-linear`, `ease-in`, `ease-out`, `ease-in-out`, custom via `--ease-*` |
| `delay-*` | `transition-delay` | Same values as duration |
| `animate-*` | `animation` | `animate-spin`, `animate-ping`, `animate-pulse`, `animate-bounce`, `animate-none`, custom via `--animate-*` |

### Transforms

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `backface-visible` / `backface-hidden` | `backface-visibility` | |
| `perspective-*` | `perspective` | `perspective-none`, `perspective-near` (100px), `perspective-normal` (500px), `perspective-midrange` (800px), `perspective-far` (1000px), `perspective-distant` (1200px), `perspective-[value]` |
| `perspective-origin-*` | `perspective-origin` | `perspective-origin-center`, `perspective-origin-top`, etc. |
| `rotate-*` | `rotate` | `rotate-0`, `rotate-1`, `rotate-2`, `rotate-3`, `rotate-6`, `rotate-12`, `rotate-45`, `rotate-90`, `rotate-180`. Negative: `-rotate-45`. 3D: `rotate-x-*`, `rotate-y-*`, `rotate-z-*` |
| `scale-*` | `scale` | `scale-0`, `scale-50`, `scale-75`, `scale-90`, `scale-95`, `scale-100`, `scale-105`, `scale-110`, `scale-125`, `scale-150`, `scale-200`. Per-axis: `scale-x-*`, `scale-y-*`, `scale-z-*` |
| `skew-*` | `skew` | `skew-x-*`, `skew-y-*` with degree values |
| `transform-*` | `transform` (combined) | `transform-gpu` (translateZ(0)), `transform-none` |
| `origin-*` | `transform-origin` | `origin-center`, `origin-top`, `origin-top-right`, `origin-right`, `origin-bottom-right`, `origin-bottom`, `origin-bottom-left`, `origin-left`, `origin-top-left` |
| `transform-flat` / `transform-3d` | `transform-style` | |
| `translate-*` | `translate` | Numbers (spacing scale), fractions, `translate-x-*`, `translate-y-*`, `translate-z-*`. Negative: `-translate-x-4` |

### Interactivity

| Utility Pattern | CSS Property | Key Classes |
|----------------|-------------|-------------|
| `accent-*` | `accent-color` | `accent-auto`, color scale |
| `appearance-none` / `appearance-auto` | `appearance` | |
| `caret-*` | `caret-color` | Color scale |
| `color-scheme-*` | `color-scheme` | `color-scheme-normal`, `color-scheme-dark`, `color-scheme-light`, `color-scheme-light-dark` |
| `cursor-*` | `cursor` | `cursor-auto`, `cursor-default`, `cursor-pointer`, `cursor-wait`, `cursor-text`, `cursor-move`, `cursor-help`, `cursor-not-allowed`, `cursor-none`, `cursor-context-menu`, `cursor-progress`, `cursor-cell`, `cursor-crosshair`, `cursor-vertical-text`, `cursor-alias`, `cursor-copy`, `cursor-no-drop`, `cursor-grab`, `cursor-grabbing`, `cursor-all-scroll`, `cursor-col-resize`, `cursor-row-resize`, `cursor-n-resize`, `cursor-e-resize`, `cursor-s-resize`, `cursor-w-resize`, `cursor-ne-resize`, `cursor-nw-resize`, `cursor-se-resize`, `cursor-sw-resize`, `cursor-ew-resize`, `cursor-ns-resize`, `cursor-nesw-resize`, `cursor-nwse-resize`, `cursor-zoom-in`, `cursor-zoom-out` |
| `field-sizing-*` | `field-sizing` | `field-sizing-content`, `field-sizing-fixed` |
| `pointer-events-*` | `pointer-events` | `pointer-events-none`, `pointer-events-auto` |
| `resize-*` | `resize` | `resize-none`, `resize`, `resize-y`, `resize-x` |
| `scroll-auto` / `scroll-smooth` | `scroll-behavior` | |
| `scroll-m-*` | `scroll-margin` | Same values as margin, per-side variants |
| `scroll-p-*` | `scroll-padding` | Same values as padding, per-side variants |
| `snap-*` | `scroll-snap-align` | `snap-start`, `snap-end`, `snap-center`, `snap-align-none` |
| `snap-*` | `scroll-snap-stop` | `snap-normal`, `snap-always` |
| `snap-*` | `scroll-snap-type` | `snap-none`, `snap-x`, `snap-y`, `snap-both`, `snap-mandatory`, `snap-proximity` |
| `touch-*` | `touch-action` | `touch-auto`, `touch-none`, `touch-pan-x`, `touch-pan-left`, `touch-pan-right`, `touch-pan-y`, `touch-pan-up`, `touch-pan-down`, `touch-pinch-zoom`, `touch-manipulation` |
| `select-*` | `user-select` | `select-none`, `select-text`, `select-all`, `select-auto` |
| `will-change-*` | `will-change` | `will-change-auto`, `will-change-scroll`, `will-change-contents`, `will-change-transform` |

### SVG

| Utility | CSS Property |
|---------|-------------|
| `fill-*` | `fill` — color scale, `fill-none`, `fill-current` |
| `stroke-*` | `stroke` — color scale, `stroke-none`, `stroke-current` |
| `stroke-*` | `stroke-width` — `stroke-0`, `stroke-1`, `stroke-2` |

### Accessibility

| Utility | CSS |
|---------|-----|
| `sr-only` | Screen-reader only (position: absolute, clip, etc.) |
| `not-sr-only` | Reset sr-only |
| `forced-color-adjust-auto` | `forced-color-adjust: auto` |
| `forced-color-adjust-none` | `forced-color-adjust: none` |

---

## 7. Arbitrary Values & Modifiers

### Arbitrary Values (Square Bracket Syntax)
```html
<div class="top-[117px]">                     <!-- Any CSS value -->
<div class="bg-[#bada55]">                    <!-- Hex color -->
<div class="text-[22px]">                     <!-- Font size -->
<div class="grid-cols-[1fr_500px_2fr]">       <!-- Underscores = spaces -->
<div class="bg-[url('/image.png')]">           <!-- URLs -->
<div class="before:content-['Hello']">        <!-- Content strings -->
<div class="max-h-[calc(100dvh-4rem)]">       <!-- calc() expressions -->
<div class="[mask-type:luminance]">           <!-- Arbitrary properties -->
<div class="[--my-var:1rem]">                 <!-- CSS custom properties -->
```

### CSS Variable Shorthand
```html
<!-- These are equivalent: -->
<div class="fill-[var(--my-color)]">
<div class="fill-(--my-color)">               <!-- v4 shorthand, adds var() -->

<!-- Type hints for ambiguous variables: -->
<div class="text-(length:--my-var)">          <!-- Force font-size -->
<div class="text-(color:--my-var)">           <!-- Force color -->
```

### Important Modifier
```html
<!-- v4: suffix with ! -->
<div class="bg-red-500!">                     <!-- !important -->

<!-- v3 (DEPRECATED): prefix with ! -->
<!-- <div class="!bg-red-500"> -->
```

### Opacity Modifier
```html
<div class="bg-red-500/50">                   <!-- 50% opacity -->
<div class="bg-red-500/[.15]">               <!-- Arbitrary opacity -->
<div class="text-black/75">                   <!-- 75% opacity -->
```

### Negative Values
```html
<div class="-mt-4">                           <!-- Negative margin -->
<div class="-translate-x-1/2">               <!-- Negative translate -->
<div class="-rotate-45">                      <!-- Negative rotation -->
```

---

## 8. Color System (v4)

### Default Palette (oklch-based)
Colors: `slate`, `gray`, `zinc`, `neutral`, `stone`, `red`, `orange`, `amber`, `yellow`, `lime`, `green`, `emerald`, `teal`, `cyan`, `sky`, `blue`, `indigo`, `violet`, `purple`, `fuchsia`, `pink`, `rose`.

Each has shades: `50`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `950`.

Special: `black`, `white`, `transparent`, `current`, `inherit`.

### Color Utility Prefixes
Colors work with: `bg-*`, `text-*`, `border-*`, `ring-*`, `outline-*`, `divide-*`, `accent-*`, `caret-*`, `fill-*`, `stroke-*`, `shadow-*`, `decoration-*`, `from-*`, `via-*`, `to-*`, `placeholder-*` (via `placeholder:text-*`).

### Custom Colors
```css
@theme {
  --color-brand: oklch(0.72 0.11 178);
  --color-brand-50: oklch(0.97 0.02 178);
  --color-brand-100: oklch(0.94 0.04 178);
  /* ... full scale ... */
  --color-brand-900: oklch(0.25 0.05 178);
  --color-brand-950: oklch(0.15 0.03 178);
}
```

---

## 9. Spacing System (v4)

In v4, spacing is based on a single `--spacing` variable (default `0.25rem`):

- `p-0` = `padding: 0`
- `p-px` = `padding: 1px`
- `p-0.5` = `padding: calc(var(--spacing) * 0.5)` = 0.125rem
- `p-1` = `padding: calc(var(--spacing) * 1)` = 0.25rem
- `p-4` = `padding: calc(var(--spacing) * 4)` = 1rem
- `p-8` = `padding: calc(var(--spacing) * 8)` = 2rem
- `p-12` = 3rem, `p-16` = 4rem, etc.
- Any integer or decimal works: `p-3.5`, `p-7`, `p-72`, `p-96`

This same scale applies to: margin, padding, gap, width, height, min/max sizes, inset (top/right/bottom/left), translate, space-between, scroll-margin, scroll-padding, text-indent, border-spacing, and more.

---

## 10. Source Detection & Safelisting

### Automatic Detection
Tailwind scans all project files (except `.gitignore`d, `node_modules`, binary files, CSS files, lock files).

### Explicit Sources
```css
@source "../node_modules/@my-company/ui-lib";
@source "../../packages/shared-components";
```

### Setting Base Path
```css
@import "tailwindcss" source("../src");
```

### Safelisting Classes
```css
@source inline("underline bg-red-500 lg:flex");
```

### Ignoring Paths
```css
@source not("./src/legacy");
```

### Dynamic Class Name Rules
NEVER construct class names dynamically:
```jsx
// BAD — will not be detected:
<div className={`bg-${color}-500`}>

// GOOD — use complete class names:
const colors = {
  red: "bg-red-500 text-white",
  blue: "bg-blue-500 text-white",
};
<div className={colors[color]}>
```

---

## 11. Key Patterns for Claude Code

### Standard HTML Setup
```html
<!DOCTYPE html>
<html lang="en" class="bg-white text-gray-900 dark:bg-gray-950 dark:text-gray-100">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="/app.css">
</head>
```

### Standard CSS Setup
```css
@import "tailwindcss";

@theme {
  --color-primary: oklch(0.6 0.2 260);
  --color-primary-light: oklch(0.8 0.15 260);
  --font-heading: "Inter", sans-serif;
}
```

### Responsive Card Component
```html
<div class="mx-auto max-w-sm rounded-xl bg-white p-6 shadow-lg
            sm:max-w-md sm:p-8
            dark:bg-gray-800 dark:shadow-none">
  <h2 class="text-xl font-bold text-gray-900 dark:text-white">Title</h2>
  <p class="mt-2 text-gray-600 dark:text-gray-400">Description text.</p>
  <button class="mt-4 rounded-lg bg-blue-600 px-4 py-2 text-white
                  hover:bg-blue-700 active:bg-blue-800
                  focus:outline-2 focus:outline-offset-2 focus:outline-blue-500
                  disabled:opacity-50 disabled:cursor-not-allowed">
    Action
  </button>
</div>
```

### Grid Layout
```html
<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
  <!-- Cards -->
</div>
```

### Flex Navigation
```html
<nav class="flex items-center justify-between px-4 py-3">
  <div class="flex items-center gap-4">
    <img class="h-8 w-8" src="/logo.svg" alt="Logo">
    <span class="text-lg font-semibold">Brand</span>
  </div>
  <div class="hidden gap-6 sm:flex">
    <a href="#" class="text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white">Home</a>
    <a href="#" class="text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white">About</a>
  </div>
</nav>
```

### Container Queries
```html
<div class="@container">
  <div class="flex flex-col @md:flex-row @md:items-center gap-4">
    <img class="w-full @md:w-48 rounded-lg" src="..." alt="">
    <div>
      <h3 class="text-lg font-bold">Title</h3>
      <p class="text-sm text-gray-500">Description</p>
    </div>
  </div>
</div>
```

### Group & Peer Patterns
```html
<!-- Group hover -->
<a href="#" class="group block rounded-lg p-6 hover:bg-gray-50">
  <h3 class="font-semibold group-hover:text-blue-600">Title</h3>
  <p class="text-gray-500 group-hover:text-gray-700">Description</p>
</a>

<!-- Peer validation -->
<label class="block">
  <input type="email" class="peer rounded border px-3 py-2" placeholder="Email">
  <p class="invisible mt-1 text-sm text-red-500 peer-invalid:visible">
    Please enter a valid email.
  </p>
</label>
```

---

## 12. Things That Commonly Trip Up AI Code Generators

1. **Don't use `tailwind.config.js` for theming** — use `@theme` in CSS
2. **Don't use `@tailwind base/components/utilities`** — use `@import "tailwindcss"`
3. **Don't use `theme()` function** — use `var(--color-red-500)` etc.
4. **Don't use `!` prefix for important** — use `!` suffix: `bg-red-500!`
5. **Don't use `@screen`** — use `@variant` or responsive variants in classes
6. **Don't forget `@reference`** in Vue/Svelte `<style>` blocks
7. **Don't dynamically construct class names** — always use complete strings
8. **Spacing is a multiplier** — `p-4` = `calc(var(--spacing) * 4)`, not a fixed value from a lookup table
9. **Colors are oklch by default** — the palette uses oklch color space
10. **Container queries are built-in** — no plugin needed, use `@container` and `@sm:`/`@md:` etc.
11. **`text-shadow` is new** — v4 has native text-shadow utilities
12. **`mask-*` utilities are new** — full CSS mask support
13. **`field-sizing` is new** — for auto-sizing form fields
14. **The `in-*` variant is new** — implicit group without adding `group` class
15. **`@custom-variant` replaces JS `addVariant()`** — define custom variants in CSS
16. **`@utility` replaces adding utilities via plugins** — define in CSS
