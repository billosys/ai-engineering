---
# === CORE IDENTIFICATION ===
concept: JavaScript Platforms
slug: javascript-platforms

# === CLASSIFICATION ===
category: language-background
subcategory: ecosystem
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Using JavaScript: the big picture"
chapter_number: 8
pdf_page: null
section: "8.2 The structure of browsers and Node.js"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - JavaScript runtime environments
  - JS platforms

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - node-js-platform
  - javascript-ecosystem
  - global-object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where does JavaScript run and what is the platform architecture?"
---

# Quick Definition

JavaScript runs on two main platforms -- web browsers and Node.js -- which share a common architecture: a JavaScript engine with platform-specific core, topped by the JavaScript standard library and a platform API.

# Core Definition

The two JavaScript platforms (web browser and Node.js) have similar structures (Ch. 8, &sect;8.2): a foundational layer consisting of the JavaScript engine and platform-specific core, with two APIs on top: the JavaScript standard library (part of JavaScript proper, runs on the engine) and the platform API (provides platform-specific functionality). In browsers, the platform API handles UI, mouse clicks, sounds; in Node.js, it handles file I/O, HTTP, etc.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Two main platforms: web browsers and Node.js
2. Common architecture: engine + core, standard library, platform API
3. JavaScript standard library is platform-independent
4. Platform APIs differ: browser (DOM, events, UI) vs. Node.js (fs, http, child_process)
5. Node.js serves three roles: server software, command-line tools, development tooling

# Construction / Recognition

Platform differences become visible when using APIs: `document` and `window` are browser-only; `fs` and `process` are Node.js-only.

# Context & Application

Understanding the platform architecture helps distinguish language features (available everywhere) from platform features (browser-only or Node-only).

# Examples

From the source text (Ch. 8, &sect;8.2):
- Browser platform API: react to mouse clicks, play sounds
- Node.js platform API: read and write files, download data via HTTP
- Node.js roles: server software, command-line tools, development tool platform

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **node-js-platform** -- one of the two main platforms

## Related
- **javascript-ecosystem** -- platforms are part of the broader ecosystem
- **global-object** -- differs between platforms

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming all JavaScript APIs work in all environments.
  **Correction**: Platform APIs differ; `window` is browser-only, `process` is Node-only.

# Common Confusions

- **Confusion**: Thinking "JavaScript" only means browser JavaScript.
  **Clarification**: JavaScript runs on many platforms; the language itself is platform-independent.

# Source Reference

Chapter 8: Using JavaScript: the big picture, Section 8.2, lines 52-81.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit architecture description with diagram reference
- Cross-reference status: verified
