---
# === CORE IDENTIFICATION ===
concept: Faceted Search
slug: faceted-search

# === CLASSIFICATION ===
category: performance
subcategory: text-analysis
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Sherlock's Last Case"
chapter_number: 27
pdf_page: null
section: "Searching Mails for a Specific Author, Date, or Subject"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - faceted search
  - facet

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record
extends: []
related:
  - cosine-similarity
  - tf-idf-weight
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a faceted search?"
  - "How do I search documents by a specific field such as author or subject?"
---

# Quick Definition

A faceted search is a search restricted to a specific field (facet) of a document — such as its author, date, or subject — rather than its full content.

# Core Definition

"A facet of a document is, for example, the username or the subject in a document. A faceted search is a search within a specific field or set of fields." In Sherlock, "parsed documents are represented as Erlang records," and "we can perform a specific search of all documents on any of these fields" ("Searching Mails for a Specific Author, Date, or Subject"). The search iterates over the stored documents and applies a regular-expression match to each chosen field of the record.

# Prerequisites

- **Record** — Parsed documents are stored as Erlang records; a faceted search matches against the record's individual fields.

# Key Properties

1. A *facet* is a single field of a document (author, date, subject, etc.).
2. A faceted search restricts matching to one or more named fields rather than the whole document.
3. Documents are stored as Erlang records, one field per facet.
4. The search iterates over the stored records and applies a regular-expression match to the chosen fields.
5. Multiple facets can be constrained at once (e.g., author AND subject AND content).

# Construction / Recognition

## To Construct/Create:
1. Parse each document into an Erlang record with one field per facet (author, date, subject, content).
2. Accept a regular-expression pattern for each facet to constrain (use `"*"` to match anything).
3. Iterate over the stored records and keep those whose fields all match their respective patterns.
4. Return the matching document indices.

## To Identify/Recognize:
1. A query that takes per-field patterns and matches against record fields is a faceted search.

# Context & Application

- **Typical contexts**: Searching a corpus by structured metadata rather than free text.
- **Common applications**: Sherlock's `sherlock_mail:search_mails_regexp/4` iterates over a year's parsed `#post` records, matching regular expressions against individual fields.
- **Historical/stylistic notes**: Faceted search complements similarity search (cosine similarity) — one finds documents by structured fields, the other by content similarity.

# Examples

**Example 1** ("Searching Mails for a Specific Author, Date, or Subject"): A faceted search over the 2009 mails for an author matching `*Armstrong*`, a subject matching `*Protocol*`, and any content:

```
1> sherlock:search_mails_regexprs("2009", "*Armstrong*", "*Protocol*", "*").
946: UBF and JSON Protocols
5994: Message protocol vs. Function call API
Query took:23 ms #results=2
[946,5994]
```

**Example 2** ("Overview of the Implementation"): `sherlock_mail:search_mails_regexp/4` "iterates over the entries `MAIL/Year/mails.bin` and performs regular expression searches on the individual elements in the `#post` records."

# Relationships

## Builds Upon
- This card builds on the record concept; it has no elaborating prerequisite card.

## Enables
- Targeted retrieval of documents by structured metadata.

## Related
- **Cosine similarity** — The content-similarity counterpart to faceted (field) search.
- **TF*IDF weight** — Both query mechanisms operate over the same parsed mail corpus.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Searching the whole document body when only a specific field is meant.
  **Correction**: Constrain the regular-expression match to the named facet (record field).

- **Error**: Forgetting that an unconstrained facet still needs a pattern.
  **Correction**: Pass a wildcard such as `"*"` for facets you do not want to constrain.

# Common Confusions

- **Confusion**: Thinking faceted search and similarity search are the same thing.
  **Clarification**: Faceted search matches structured fields with regular expressions; similarity search (cosine similarity) compares content keyword vectors.

# Source Reference

Chapter 27: Sherlock's Last Case, Sections "Searching Mails for a Specific Author, Date, or Subject" and "Overview of the Implementation."

# Verification Notes

- Definition source: Direct quote and adaptation from "Searching Mails for a Specific Author, Date, or Subject."
- Confidence rationale: HIGH — the source defines facet and faceted search and gives a worked query.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
