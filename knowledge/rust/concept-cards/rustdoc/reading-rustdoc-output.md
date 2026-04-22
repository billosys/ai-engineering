---
# === CORE IDENTIFICATION ===
concept: Reading Rustdoc Output
slug: reading-rustdoc-output

# === CLASSIFICATION ===
category: documentation
subcategory: navigation
tier: foundational

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "How to read rustdoc output"
chapter_number: 3
pdf_page: null
section: "Structure, Item Documentation, Navigation Bar, In-doc settings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "navigating rustdoc"
  - "rustdoc page structure"
  - "rustdoc UI"
  - "rustdoc in-doc settings"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rustdoc
extends: []
related:
  - rustdoc-search
  - doc-comments
  - doc-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is a rustdoc page structured?"
  - "What are the three main sections of rustdoc output?"
  - "What information appears in the navigation bar?"
  - "How do I find the source code link for an item?"
  - "What keyboard shortcuts are available in rustdoc?"
  - "What settings can I configure in rustdoc's in-doc settings menu?"
  - "How do I deep-link to a specific section of documentation?"
  - "What does the aliased type section show?"
  - "How do I auto-collapse large trait implementation lists?"
---

# Quick Definition

Rustdoc's HTML output is organized into three sections: a navigation sidebar on the left showing contextual links, a search interface at the top, and the main item documentation below. The output includes a settings menu for customizing display behavior (auto-hide, themes, line numbers) and keyboard shortcuts for efficient navigation.

# Core Definition

As described in the source: "The `rustdoc` output is divided into three sections. Along the left side of each page is a quick navigation bar, which shows contextual information about the current entry. The rest of the page is taken up by the search interface at the top and the documentation for the current item below that." (Ch. 3: How to read rustdoc output).

The item documentation section displays the type and name (e.g., "Struct `std::time::Duration`"), a clipboard button for copying the item path, expand/collapse controls, a link to source code (`[src]`), and the stabilization version for standard library items. Below this header appears the main documentation text, followed by the definition or function signature, fields or variants for types, and then associated functions and trait implementations (including automatic and blanket implementations).

The navigation sidebar shows all crates in the documentation bundle at the crate root, with quick links to modules, structs, traits, functions, and macros. It displays a configurable logo alongside the crate name and version.

Rustdoc also provides an in-doc settings menu (accessed via the gear icon) with options for theme selection (including system-preference-aware light/dark modes), auto-hiding large items (those with more than 12 fields/variants), auto-hiding method documentation, auto-hiding trait implementation documentation, direct navigation on single search results, code example line numbers, and disabling keyboard shortcuts.

# Prerequisites

- **rustdoc** -- Understanding what rustdoc produces

# Key Properties

1. **Three-section layout**: Left navigation bar, top search interface, main item documentation area
2. **Item header controls**: Type/name display, clipboard copy, expand/collapse (`[+]`/`[-]`), source link (`[src]`), stabilization version
3. **Deep linking**: Subheadings, variants, fields, and other elements are anchors; the section symbol "SS" appears on hover/focus to indicate linkable elements
4. **Aliased type expansion**: Type aliases show the compile-time expansion result, including substituted type parameters in public fields and variants
5. **Keyboard shortcuts**: `S` focuses search, `?` opens help, arrow keys navigate search results, `+`/`-` expand/collapse all sections
6. **Theme system**: Supports light (default) and dark themes, plus system-preference-aware mode with separate preferred light and dark theme selections
7. **Auto-hide settings**: Items with more than 12 sub-items collapse by default (configurable); method documentation and trait implementations can be collapsed separately
8. **Single-result navigation**: Optional setting to bypass the results page when search returns exactly one match

# Construction / Recognition

## Navigating Item Documentation:
- Click the type/name header to navigate to an item
- Click `[src]` to view the source code (if available; may be absent with `cargo doc --no-deps`)
- Click `[+]`/`[-]` to expand or collapse documentation sections
- Click the clipboard icon to copy the item's full path
- Hover over headings to reveal the "SS" anchor symbol for deep-linking

## Using Keyboard Shortcuts:
- Press `S` to focus the search bar from anywhere on the page
- Press `?` to open the help screen showing all shortcuts
- Use arrow keys in search results: left/right for tabs, up/down for results, Enter to open
- Press `+` or `-` to expand or collapse all sections on the current page

## Configuring In-Doc Settings:
- Click the gear icon in the upper right to open settings
- Select theme: light, dark, ayu, or system preference (with sub-preferences for light and dark)
- Toggle auto-hide for large items, method docs, or trait implementation docs
- Enable "Directly go to item in search if there is only one result"
- Enable line numbers on code examples

# Context & Application

Understanding rustdoc's output structure is essential for efficiently navigating Rust library documentation, whether on docs.rs, the standard library docs, or locally generated documentation. The settings are stored in the browser, so preferences persist across sessions. The deep-linking capability is particularly valuable for sharing precise references to specific fields, variants, or trait implementations in code reviews and discussions. The auto-hide settings are crucial for working with large types like `Iterator` that have dozens of methods and trait implementations.

# Examples

**Example 1** (Ch. 3): At-a-glance controls for an item page:
> "At the top is some at-a-glance info and controls: the type and name of the item, such as 'Struct `std::time::Duration`', a button to copy the item's path to the clipboard... a button to collapse or expand the top-level documentation for that item (`[+]` or `[-]`), a link to the source code (`[src]`)... and the version in which the item became stable."

**Example 2** (Ch. 3): The navigation bar at the crate root:
> "When looking at documentation for the crate root, it shows all the crates documented in the documentation bundle, and quick links to the modules, structs, traits, functions, and macros available from the current crate."

**Example 3** (Ch. 3): Auto-hide for large items:
> "If the type definition contains more than 12 items, and this setting is enabled, it'll collapse them by default. You can see them by clicking on the `[+]` button to expand them."

The `Iterator` trait page is given as an example where this is useful due to its many associated methods.

**Example 4** (Ch. 3): System-preference-aware theming:
> "If you pick the 'system preference', you will be able to see two new sub-menus: 'Preferred light theme' and 'Preferred dark theme'. It means that if your system preference is set to 'light', then rustdoc will use the theme you selected in 'Preferred light theme'."

# Relationships

## Builds Upon
- **rustdoc** -- this describes how to read the output rustdoc generates

## Enables
- **rustdoc-search** -- the search interface is one of the three main sections of the output

## Related
- **doc-comments** -- the documentation text displayed in the item documentation section comes from doc comments
- **doc-attribute** -- attributes like `html_logo_url` and `html_no_source` control aspects of the output

## Contrasts With
- None within this source

# Common Errors

- **Error**: Looking for an item's source code link and not finding it.
  **Correction**: The `[src]` link may be absent if documentation was generated with `cargo doc --no-deps` or if `html_no_source` is configured. The source is not always available.

- **Error**: Expecting keyboard shortcuts to work when they have been disabled.
  **Correction**: Check the in-doc settings -- the "Disable keyboard shortcuts" option may be enabled, particularly if a browser extension conflicts with the default shortcuts.

- **Error**: Thinking auto-hide settings are per-crate or per-session.
  **Correction**: Settings are stored in the browser and persist across all rustdoc pages and sessions until changed.

# Common Confusions

- **Confusion**: Thinking all items on a page are always visible.
  **Clarification**: With auto-hide enabled, items with more than 12 sub-items are collapsed by default, method documentation may be hidden, and trait implementation sections may be collapsed. Use `[+]` or the `+` key to expand.

- **Confusion**: Thinking deep-link anchors are only on section headings.
  **Clarification**: "Subheadings, variants, fields, and many other things in this documentation are anchors and can be clicked on and deep-linked to." The "SS" symbol appears next to any linkable element on hover or keyboard focus.

- **Confusion**: Thinking the navigation bar only shows the current crate.
  **Clarification**: At the crate root, the sidebar shows all crates in the documentation bundle, not just the current one. Within a specific item, it shows contextual navigation for that item's crate.

# Source Reference

Chapter 3: How to read rustdoc output -- sections "Structure," "The Item Documentation," "The Navigation Bar," "The Theme Picker and Search Interface," "Shortcuts," and the in-doc settings subsections. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 3 -- "The `rustdoc` output is divided into three sections."
- Confidence rationale: HIGH -- the source provides detailed descriptions of each UI element
- Uncertainties: The exact appearance of UI elements may vary across rustdoc versions; the source notes themes are not stable between versions
- Cross-reference status: rustdoc, rustdoc-search are in this extraction set; doc-comments, doc-attribute from Agent B
