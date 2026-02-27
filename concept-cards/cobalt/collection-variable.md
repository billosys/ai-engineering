---
# === CORE IDENTIFICATION ===
concept: Collection Variable
slug: collection-variable

# === CLASSIFICATION ===
category: templating
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Variables"
chapter_number: null
pdf_page: null
section: "Collection Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "collections object"
  - "collection data"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - template-variables
extends: []
related:
  - site-variable
  - page-variable
  - cobalt-configuration-file
  - rss-feed
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Liquid template variables in my pages?"
---

# Quick Definition

The `collection` variable (accessed as `collections`) is a global Liquid object providing metadata about Cobalt's collections. The built-in `posts` collection exposes properties like `collections.posts.title`, `collections.posts.description`, `collections.posts.slug`, `collections.posts.rss`, and `collections.posts.jsonfeed`.

# Core Definition

The `collection` global variable provides access to collection-level metadata in Cobalt. Currently, the built-in collection is `posts`. Collection properties are configured in `_cobalt.yml` and include: `collections.posts.title` (String), `collections.posts.description` (String), `collections.posts.slug` (String), `collections.posts.rss` (String, permalink for the RSS feed), and `collections.posts.jsonfeed` (String, permalink for the JSON feed). The documentation notes that the built-in `posts` collection is the demonstrated example. (Source: Cobalt Variables documentation)

# Prerequisites

- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Understanding the variable system.

# Key Properties

1. **`collections.posts.title`** (String): The title of the posts collection.
2. **`collections.posts.description`** (String): The description of the posts collection.
3. **`collections.posts.slug`** (String): The identifier of the posts collection.
4. **`collections.posts.rss`** (String): The permalink for the posts' RSS feed.
5. **`collections.posts.jsonfeed`** (String): The permalink for the posts' JSON feed.

# Construction / Recognition

## To Construct/Create:
1. Configure collection properties in `_cobalt.yml`.
2. Access via the `collections` global in templates.

## To Identify/Recognize:
1. Any variable reference starting with `collections.` in a template.

# Context & Application

- **Typical contexts**: Templates that display collection-level metadata, RSS feed templates, site navigation.
- **Common applications**: Linking to RSS feeds, displaying collection titles and descriptions, building collection navigation.

# Examples

**Example 1** (source: Cobalt Variables documentation): Linking to the posts RSS feed:
```html
<a href="{{ collections.posts.rss }}">RSS Feed</a>
```

**Example 2** (source: Cobalt Variables documentation): Displaying the posts collection title:
```html
<h1>{{ collections.posts.title }}</h1>
<p>{{ collections.posts.description }}</p>
```

# Relationships

## Builds Upon
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Collection variables are one of three global objects.

## Enables
- **[RSS Feed](/concept-cards/cobalt/rss-feed.md)** -- Collection variables provide the RSS feed permalink.

## Related
- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- Another global variable object.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- Another global variable object.
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Collection properties are configured here.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `collection.posts` (singular) instead of `collections.posts` (plural).
  **Correction**: The global variable is `collections` (plural), though the Variables documentation lists the global as `collection` (Object).

# Common Confusions

- **Confusion**: Thinking collection variables contain the actual post data/list.
  **Clarification**: Collection variables provide metadata about the collection (title, description, RSS link). Individual posts are accessed through pagination or other mechanisms.

# Source Reference

Variables documentation, "Collection Variables" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Variables documentation
- Confidence rationale: All properties are explicitly documented in a table.
- Uncertainties: The documentation lists the global as `collection` (singular) but examples use `collections` (plural) -- the plural form is the correct access path.
- Cross-reference status: Verified against Variables documentation.
