---
# === CORE IDENTIFICATION ===
concept: npm Registry
slug: npm-registry

# === CLASSIFICATION ===
category: language-background
subcategory: ecosystem
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Why JavaScript?"
chapter_number: 3
pdf_page: null
section: "3.2.3 Language"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - npm
  - npm software registry

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - javascript-ecosystem
  - node-js-platform
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are JavaScript libraries and tools distributed?"
---

# Quick Definition

npm (Node Package Manager) is the de-facto standard software registry for JavaScript, used to install libraries, tools, and frameworks for both client-side and server-side development.

# Core Definition

npm is "the de-facto standard in the JavaScript ecosystem" for distributing libraries (Ch. 3, &sect;3.2.3). "Node's software registry, npm, has become the dominant way of installing tools (such as compilers and build tools) and libraries -- even for client-side development." (Ch. 8, &sect;8.1). Most JavaScript tools, including native tools, are installed via npm.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. De-facto standard package registry for JavaScript
2. Used for both server-side and client-side packages
3. Installs tools (compilers, build tools) and libraries
4. Available at npmjs.com
5. Even native tools are installed via npm-based package managers

# Construction / Recognition

Packages are installed via `npm install` or similar commands. Package dependencies are listed in `package.json`.

# Context & Application

Nearly all JavaScript development relies on npm for dependency management. Understanding npm is essential for any JavaScript project setup.

# Examples

From the source text (Ch. 3, &sect;3.2.3; Ch. 8, &sect;8.1):
- "Many libraries are available, via the de-facto standard in the JavaScript ecosystem, the npm software registry."
- npm is used for installing tools like compilers and build tools

# Relationships

## Builds Upon
- No prerequisites

## Enables
- JavaScript library and tool distribution

## Related
- **javascript-ecosystem** -- npm is a core part of the ecosystem
- **node-js-platform** -- npm originated from Node.js

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Thinking npm is only for Node.js server-side code.
  **Correction**: npm is used for client-side tools and libraries too.

# Common Confusions

- **Confusion**: Confusing npm (the registry) with npm (the CLI tool).
  **Clarification**: "npm" refers to both the online registry (npmjs.com) and the command-line tool used to interact with it.

# Source Reference

Chapter 3: Why JavaScript?, Section 3.2.3, lines 126-128. Chapter 8: Section 8.1, lines 48-50.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly mentioned in multiple chapters
- Cross-reference status: verified across Ch. 3 and Ch. 8
