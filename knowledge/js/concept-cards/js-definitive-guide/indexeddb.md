---
concept: IndexedDB
slug: indexeddb
category: browser-apis
subcategory: storage
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 560
section: "15.12.3 IndexedDB"
extraction_confidence: high
aliases:
  - IndexedDB API
  - client-side database
prerequisites:
  - localstorage-and-sessionstorage
extends: []
related: []
contrasts_with:
  - localstorage-and-sessionstorage
answers_questions:
  - "How do localStorage and sessionStorage differ?"
---

# Quick Definition

IndexedDB is an asynchronous, transactional object database built into the browser that stores structured JavaScript objects with indexes for efficient querying, scoped to the document origin.

# Core Definition

IndexedDB is an object database that stores JavaScript objects (serialized via the structured clone algorithm) in named object stores, each with a key path for the primary key and optional secondary indexes. It provides atomicity via transactions and is asynchronous with an event-based (not Promise-based) API. Databases are opened with `indexedDB.open(name, version)`, and schema changes (creating object stores and indexes) can only occur in the "upgradeneeded" event handler (Flanagan, Ch. 15, pp. 560-564).

# Prerequisites

- **localstorage-and-sessionstorage** — Understanding simpler storage helps contextualize IndexedDB.

# Key Properties

1. Asynchronous, event-based API (not Promise-based).
2. Transactional: all operations are atomic within a transaction.
3. Object stores hold structured objects, not just strings.
4. Supports primary keys and secondary indexes for efficient queries.
5. Schema changes only allowed in "upgradeneeded" event handlers.
6. Scoped to document origin.

# Construction / Recognition

```javascript
let request = indexedDB.open("zipcodes", 1);
request.onsuccess = () => { let db = request.result; };
request.onupgradeneeded = () => { /* create object stores */ };
```

# Context & Application

Used when `localStorage` is insufficient: for large datasets, complex queries, or structured data. Common in progressive web apps for offline data.

# Examples

From the source (p. 562): A zip code database with an object store keyed on "zipcode" and an index on city name, demonstrating open, upgradeneeded, transaction creation, and get/put operations.

# Relationships

## Builds Upon
- **localstorage-and-sessionstorage** — A more powerful storage alternative

## Enables
- Offline-capable web applications

## Related
- (None)

## Contrasts With
- **localstorage-and-sessionstorage** — localStorage is simpler but limited to string key-value pairs; IndexedDB handles structured objects with indexes

# Common Errors

- **Error**: Trying to create object stores outside of the "upgradeneeded" event handler.
  **Correction**: Object stores and indexes can only be created/modified during the "upgradeneeded" event.

# Common Confusions

- **Confusion**: IndexedDB is a relational database with SQL.
  **Clarification**: IndexedDB is an object database. There is no SQL; queries use key lookups and cursors.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.12.3, pages 560-564.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Detailed explanation of API pattern
- Uncertainties: None
- Cross-reference status: Verified
