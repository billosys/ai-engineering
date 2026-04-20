---
# === CORE IDENTIFICATION ===
concept: HTTP (HyperText Transfer Protocol)
slug: http

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
section: "Networks and the Internet"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - HyperText Transfer Protocol

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tcp
  - network-protocol
extends:
  - network-protocol
related:
  - url
  - html
  - world-wide-web
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is HTTP?"
---

# Quick Definition
HTTP is a protocol for retrieving named resources (such as web pages or images) from servers, forming the foundation of web communication.

# Core Definition
"The *HyperText Transfer Protocol* (HTTP) is a protocol for retrieving named resources (chunks of information, such as web pages or pictures). It specifies that the side making the request should start with a line like this, naming the resource and the version of the protocol that it is trying to use." (Eloquent JavaScript, Ch. 13, lines 86-90)

# Prerequisites
- **TCP**: HTTP is built on top of TCP
- **Network protocol**: Understanding protocol concepts

# Key Properties
1. Request-response model: client requests, server responds
2. Uses port 80 by default (443 for HTTPS)
3. Requests specify a method (GET, POST, etc.) and a resource path
4. Built on top of TCP for reliable delivery
5. Stateless -- each request is independent

# Construction / Recognition
```
GET /index.html HTTP/1.1
```
(line 93)

# Context & Application
HTTP is the protocol that powers the World Wide Web. Browsers use it to request web pages, images, scripts, and other resources from servers.

# Examples
From the source: "If you type this URL into your browser's address bar, the browser will try to retrieve and display the document at that URL. First, your browser has to find out what address *eloquentjavascript.net* refers to. Then, using the HTTP protocol, it will make a connection to the server at that address and ask for the resource */13_browser.html*." (lines 187-192)

# Relationships
## Builds Upon
- TCP (reliable transport)
## Enables
- The World Wide Web
- Web page retrieval and API communication
## Related
- URL (identifies resources)
- HTML (common content type returned by HTTP)
## Contrasts With
- Other application protocols (SMTP for email, FTP for files)

# Common Errors
- **Error**: Confusing HTTP with HTTPS
  **Correction**: HTTPS is HTTP with encryption (TLS); the protocol semantics are the same

# Common Confusions
- **Confusion**: HTTP and the web are the same thing
  **Clarification**: HTTP is one protocol used by the web; the web also relies on HTML, CSS, JavaScript, and DNS

# Source Reference
Chapter 13: JavaScript and the Browser, Section "Networks and the Internet", lines 86-101 of 13-javascript-and-the-browser.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified
