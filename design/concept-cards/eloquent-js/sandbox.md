---
# === CORE IDENTIFICATION ===
concept: Sandbox
slug: sandbox

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
section: "In the sandbox"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - sandboxing
  - browser sandbox

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-in-browser
extends: []
related:
  - web-standards
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is sandboxing in the browser?"
---

# Quick Definition
Sandboxing is the practice of isolating a programming environment so that programs cannot access or modify anything outside their restricted scope, protecting users from malicious code.

# Core Definition
"Isolating a programming environment in this way is called *sandboxing*, the idea being that the program is harmlessly playing in a sandbox. But you should imagine this particular kind of sandbox as having a cage of thick steel bars over it so that the programs playing in it can't actually get out." (Eloquent JavaScript, Ch. 13, lines 409-413)

# Prerequisites
- **JavaScript in the browser**: Understanding that untrusted code runs in browsers

# Key Properties
1. Browsers severely limit what JavaScript can do
2. Scripts cannot read files on the user's computer
3. Scripts cannot modify anything unrelated to their web page
4. The sandbox must balance usefulness with security
5. Security vulnerabilities are discovered and patched continuously

# Construction / Recognition
The sandbox is enforced by the browser itself -- JavaScript running in a web page automatically operates within sandbox restrictions.

# Context & Application
Sandboxing is essential for web security, allowing users to visit untrusted websites without their computer being compromised.

# Examples
From the source: "Browsers severely limit the things a JavaScript program may do: it can't look at the files on your computer or modify anything not related to the web page it was embedded in." (lines 404-406)

"The hard part of sandboxing is allowing programs enough room to be useful while restricting them from doing anything dangerous." (lines 416-418)

# Relationships
## Builds Upon
- Browser security model
## Enables
- Safe browsing of untrusted websites
## Related
- Web standards (define what the sandbox allows)
## Contrasts With
- Unrestricted program execution (like native applications)

# Common Errors
- **Error**: Assuming the sandbox is impenetrable
  **Correction**: "Every now and then, someone comes up with a new way to circumvent the limitations of a browser and do something harmful." (lines 424-426)

# Common Confusions
- **Confusion**: All JavaScript code is sandboxed
  **Clarification**: Only browser JavaScript is sandboxed; Node.js JavaScript has full system access

# Source Reference
Chapter 13: JavaScript and the Browser, Section "In the sandbox", lines 392-431 of 13-javascript-and-the-browser.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with vivid metaphor
- Cross-reference status: verified
