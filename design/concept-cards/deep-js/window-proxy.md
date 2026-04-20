---
# === CORE IDENTIFICATION ===
concept: WindowProxy
slug: window-proxy

# === CLASSIFICATION ===
category: language-mechanics
subcategory: scoping
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "A detailed look at global variables"
chapter_number: 5
section: "5.4 In browsers, globalThis does not point directly to the global object"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - global-object
  - global-this
extends: []
related:
  - global-environment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

`WindowProxy` is a browser-specific exotic object that forwards all property accesses to the current `Window` object, ensuring that `globalThis` remains stable even when an iframe's document (and thus its `Window`) changes.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.4): Browsers "internally distinguish two objects: `Window` is the global object. It changes whenever the location changes. `WindowProxy` is an object that forwards all accesses to the current `Window`. This object never changes." In browsers, `globalThis` refers to `WindowProxy`, not directly to `Window`. "everywhere else, it directly refers to the global object."

# Prerequisites

- **Global object** — WindowProxy proxies access to the global object (Window).
- **globalThis** — In browsers, `globalThis` is `WindowProxy`.

# Key Properties

1. Browser-specific mechanism.
2. **Forwards** all accesses to the current `Window` object.
3. **Never changes** — maintains identity even when `Window` changes.
4. `Window` (the actual global object) changes when iframe location changes.
5. `globalThis` points to `WindowProxy`, not `Window`.
6. Not relevant in Node.js or other non-browser environments.

# Construction / Recognition

## To Construct/Create:
1. Created automatically by the browser for each browsing context.

## To Identify/Recognize:
1. In browsers, `globalThis` is a `WindowProxy`. Cross-iframe identity checks reveal this behavior.

# Context & Application

WindowProxy exists to solve a specific browser problem: iframes get new `Window` objects when their source changes, but external code holding a reference to `globalThis` of the iframe needs a stable reference. WindowProxy provides that stability.

# Examples

**Example 1** (Ch 5): Demonstrating WindowProxy stability across iframe navigation:
```html
<!-- parent.html -->
<iframe src="iframe.html?first"></iframe>
<script>
  const iframe = document.querySelector('iframe');
  const icw = iframe.contentWindow; // globalThis of iframe

  iframe.onload = () => {
    const firstGlobalThis = icw.globalThis;
    const firstArray = icw.Array;
    console.log(icw.iframeName); // 'first'

    iframe.onload = () => {
      const secondGlobalThis = icw.globalThis;
      const secondArray = icw.Array;

      // The global object (Window) is different:
      console.log(icw.iframeName); // 'second'
      console.log(secondArray === firstArray); // false

      // But globalThis (WindowProxy) is still the same:
      console.log(firstGlobalThis === secondGlobalThis); // true
    };
    iframe.src = 'iframe.html?second';
  };
</script>
```

# Relationships

## Builds Upon
- **Global object** — WindowProxy proxies the Window (global object).
- **globalThis** — `globalThis` is `WindowProxy` in browsers.

## Enables
- **Stable cross-frame references** — External code can hold a stable reference to an iframe's global.

## Related
- **Global environment** — WindowProxy interacts with the global environment in browsers.

## Contrasts With
- None directly (unique browser mechanism).

# Common Errors

- **Error**: Assuming `globalThis === window` means they are the same underlying object.
  **Correction**: `globalThis` is `WindowProxy`, which forwards to `Window`. They appear the same but have different identities internally when frames navigate.

# Common Confusions

- **Confusion**: WindowProxy is relevant in Node.js.
  **Clarification**: WindowProxy is a browser-only concept. In Node.js, `globalThis` directly references the global object.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.4, lines 103-164.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Detailed explanation with browser example
- Cross-reference status: verified against WHATWG spec references in source
