---
# === CORE IDENTIFICATION ===
concept: Named Capture Groups in Composed Regexes
slug: named-capture-groups-composition

# === CLASSIFICATION ===
category: regular-expressions
subcategory: composition
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Composing regular expressions via re-template-tag (bonus)"
chapter_number: 18
section: "18.4 re and named capture groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - named groups in composed regex

# === TYPED RELATIONSHIPS ===
prerequisites:
  - re-template-tag
  - regex-fragment-reuse
  - named-capture-groups
extends:
  - regex-fragment-reuse
related:
  - regex-composition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compose regular expressions using template tags?"
---

# Quick Definition

Named capture groups make composed regex fragments more independent by allowing each fragment to define a self-describing named group, accessed via `match.groups.name` rather than positional indices that shift when fragments are added or reordered.

# Core Definition

As explained in "Deep JavaScript" (Ch 18, Section 18.4): "`re` profits from named capture groups because they make the fragments more independent." Without named groups, accessing captures requires knowing positional indices (`match[1]`, `match[2]`) that depend on fragment ordering. With named groups (`(?<year>...)`, `(?<month>...)`), captures are accessed via `match.groups.year`, making the code resilient to reordering or adding fragments.

# Prerequisites

- **`re` template tag** — The composition mechanism.
- **Regex fragment reuse** — The pattern this improves.
- **Named capture groups** — The `(?<name>...)` syntax (ES2018).

# Key Properties

1. Named groups use `(?<name>...)` syntax.
2. Captures accessed via `match.groups.name` instead of `match[N]`.
3. Fragments become **independent of ordering** — no positional index coupling.
4. Fragments can use `re` template tag themselves: `` re`(?<year>[0-9]{4})` ``.
5. Adding or removing fragments doesn't break existing group access.

# Construction / Recognition

## To Construct/Create:
1. Define each fragment with a named capture group: `` re`(?<year>[0-9]{4})` ``.
2. Compose fragments: `` re`/${RE_YEAR}-${RE_MONTH}-${RE_DAY}/u` ``.
3. Access captures: `match.groups.year`, `match.groups.month`, `match.groups.day`.

## To Identify/Recognize:
1. Regex fragments containing `(?<name>...)` syntax.
2. Match results accessed via `.groups` property instead of numeric indices.

# Context & Application

Named capture groups solve the fragility problem of composed regexes. In a monolithic regex, positional indices are manageable. In a composed regex where fragments can be added, removed, or reordered, positional indices become brittle. Named groups eliminate this coupling.

# Examples

**Example 1** (Ch 18): Without named groups (fragile indices):
```js
const RE_YEAR = /([0-9]{4})/;
const RE_MONTH = /([0-9]{2})/;
const RE_DAY = /([0-9]{2})/;
const RE_DATE = re`/^${RE_YEAR}-${RE_MONTH}-${RE_DAY}$/u`;

const match = RE_DATE.exec('2017-01-27');
assert.equal(match[1], '2017'); // positional — fragile
```

**Example 2** (Ch 18): With named groups (robust):
```js
const RE_YEAR = re`(?<year>[0-9]{4})`;
const RE_MONTH = re`(?<month>[0-9]{2})`;
const RE_DAY = re`(?<day>[0-9]{2})`;
const RE_DATE = re`/${RE_YEAR}-${RE_MONTH}-${RE_DAY}/u`;

const match = RE_DATE.exec('2017-01-27');
assert.equal(match.groups.year, '2017'); // named — robust
```

# Relationships

## Builds Upon
- **Regex fragment reuse** — Named groups improve the fragment reuse pattern.
- **Named capture groups (ES2018)** — The language feature enabling this.

## Enables
- **Robust composed regexes** — Fragment ordering doesn't affect capture access.
- **Self-documenting fragments** — The group name describes what it captures.

## Related
- **Regex composition** — The broader technique.

## Contrasts With
- **Positional capture groups** — Accessed by index, fragile to reordering.

# Common Errors

- **Error**: Duplicate named groups in composed fragments.
  **Correction**: Each named capture group must have a unique name across the entire composed regex. Choose distinct names for each fragment.

# Common Confusions

- **Confusion**: Thinking named groups and positional indices are mutually exclusive.
  **Clarification**: Named groups also have positional indices. You can access them either way, but `.groups.name` is preferred for clarity and robustness.

# Source Reference

Chapter 18: Composing regular expressions via re-template-tag, Section 18.4, lines 8427-8456.

# Verification Notes

- Definition source: direct (from source explanation and both examples)
- Confidence rationale: Explicitly contrasted with and without named groups
- Cross-reference status: verified against Section 18.2 basic composition
