---
# === CORE IDENTIFICATION ===
concept: World Wide Web
slug: world-wide-web

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
  - the web
  - WWW

# === TYPED RELATIONSHIPS ===
prerequisites:
  - http
extends: []
related:
  - url
  - html
  - javascript-in-browser
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the World Wide Web?"
---

# Quick Definition
The World Wide Web is a set of protocols and formats that allow users to visit linked web pages in a browser, forming a mesh of interconnected documents.

# Core Definition
"The *World Wide Web* (not to be confused with the internet as a whole) is a set of protocols and formats that allow us to visit web pages in a browser. The word *Web* refers to the fact that such pages can easily link to each other, thus connecting into a huge mesh that users can move through." (Eloquent JavaScript, Ch. 13, lines 145-149)

# Prerequisites
- **HTTP**: The primary protocol used by the web

# Key Properties
1. Distinct from "the internet" -- the web is one application built on the internet
2. Based on HTTP, HTML, URLs, and browsers
3. Pages link to each other, forming a web/mesh structure
4. To join the web, a machine needs internet connectivity and an HTTP server on port 80
5. Decentralized -- no central authority controls it

# Construction / Recognition
"To become part of the web, all you need to do is connect a machine to the internet and have it listen on port 80 with the HTTP protocol so that other computers can ask it for documents." (lines 152-155)

# Context & Application
The web is the platform on which JavaScript and web development operate. Understanding the web's architecture is foundational for web development.

# Examples
From the source: "Web technology has been decentralized from the start, not just technically but also in terms of the way it evolved. Various browser vendors have added new functionality in ad hoc and sometimes poorly thought-out ways." (lines 41-44)

# Relationships
## Builds Upon
- The internet, HTTP, HTML
## Enables
- Web applications, online communication, information sharing
## Related
- URLs (addresses on the web), browsers (clients for the web)
## Contrasts With
- The internet as a whole (email, FTP, etc. are not part of the web)

# Common Errors
- **Error**: Confusing "the internet" with "the web"
  **Correction**: The internet is the network infrastructure; the web is one application built on it

# Common Confusions
- **Confusion**: The web has always been standardized
  **Clarification**: "The haphazard way in which the web was developed means that the resulting system is not exactly a shining example of internal consistency." (lines 51-54)

# Source Reference
Chapter 13: JavaScript and the Browser, Section "The Web", lines 142-192 of 13-javascript-and-the-browser.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified
