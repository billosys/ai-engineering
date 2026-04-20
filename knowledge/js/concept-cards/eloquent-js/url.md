---
# === CORE IDENTIFICATION ===
concept: URL (Uniform Resource Locator)
slug: url

# === CLASSIFICATION ===
category: web-platform
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "JavaScript and the Browser"
chapter_number: 13
pdf_page: null
section: "The Web"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - uniform resource locator
  - web address

# === TYPED RELATIONSHIPS ===
prerequisites:
  - http
extends: []
related:
  - world-wide-web
  - html
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a URL?"
---

# Quick Definition
A URL (uniform resource locator) is an address that names a document on the web, specifying the protocol, server, and path to a resource.

# Core Definition
"Each document on the web is named by a *uniform resource locator* (URL)." A URL has three main parts: the protocol, the server, and the path. (Eloquent JavaScript, Ch. 13, lines 158-166)

# Prerequisites
- **HTTP**: URLs commonly use HTTP/HTTPS as their protocol

# Key Properties
1. Specifies the protocol (http, https, etc.)
2. Identifies the server (domain name or IP address)
3. Contains a path to the specific resource
4. Domain names map to IP addresses via DNS

# Construction / Recognition
```
  http://eloquentjavascript.net/13_browser.html
 |      |                      |               |
 protocol       server               path
```
(lines 162-166)

# Context & Application
URLs are the primary way to identify and locate resources on the web. They are used in browser address bars, links, API endpoints, and any web resource reference.

# Examples
From the source: "The first part tells us that this URL uses the HTTP protocol (as opposed to, for example, encrypted HTTP, which would be *https://*). Then comes the part that identifies which server we are requesting the document from. Last is a path string that identifies the document (or *resource*) we are interested in." (lines 169-173)

# Relationships
## Builds Upon
- HTTP protocol
- Domain Name System (DNS)
## Enables
- Linking between web pages
- Resource identification and retrieval
## Related
- World Wide Web (URLs make the web addressable)
## Contrasts With
- IP addresses (numeric, less human-friendly)

# Common Errors
- **Error**: Omitting the protocol scheme from URLs
  **Correction**: URLs need a protocol prefix (http:// or https://)

# Common Confusions
- **Confusion**: URLs and domain names are the same thing
  **Clarification**: The domain name is just one part of a URL; the URL also includes the protocol and path

# Source Reference
Chapter 13: JavaScript and the Browser, Section "The Web", lines 158-192 of 13-javascript-and-the-browser.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with visual breakdown
- Cross-reference status: verified
