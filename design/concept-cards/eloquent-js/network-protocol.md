---
# === CORE IDENTIFICATION ===
concept: Network Protocol
slug: network-protocol

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
  - protocol

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - tcp
  - http
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a protocol in networking?"
---

# Quick Definition
A network protocol describes a style of communication over a network, defining how computers exchange data for a specific purpose.

# Core Definition
"A *network protocol* describes a style of communication over a network. There are protocols for sending email, for fetching email, for sharing files, and even for controlling computers that happen to be infected by malicious software." (Eloquent JavaScript, Ch. 13, lines 80-83)

# Prerequisites
None required -- this is a foundational networking concept.

# Key Properties
1. Defines rules for how data is formatted and exchanged
2. Different protocols serve different purposes
3. Protocols are often layered on top of each other
4. Both sides of the communication must follow the same protocol

# Construction / Recognition
Recognized by standardized request/response patterns, like HTTP:
```
GET /index.html HTTP/1.1
```
(line 93)

# Context & Application
Protocols are the foundation of all networked communication, from web browsing (HTTP) to email (SMTP) to file transfer.

# Examples
From the source: HTTP "specifies that the side making the request should start with a line like this, naming the resource and the version of the protocol that it is trying to use" (lines 88-90).

"Most protocols are built on top of other protocols. HTTP treats the network as a streamlike device... Providing those guarantees on top of the primitive data-sending that the network gives you is already a rather tricky problem." (lines 104-109)

# Relationships
## Builds Upon
- Basic networking (cables, data transmission)
## Enables
- Structured communication between computers
## Related
- TCP, HTTP (specific protocols)
## Contrasts With
- Unstructured data transmission

# Common Errors
- **Error**: Confusing the protocol with the data being sent
  **Correction**: The protocol defines the rules; the data is what flows through those rules

# Common Confusions
- **Confusion**: All internet communication uses the same protocol
  **Clarification**: Different purposes use different protocols, often layered

# Source Reference
Chapter 13: JavaScript and the Browser, Section "Networks and the Internet", lines 80-115 of 13-javascript-and-the-browser.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified
