---
concept: Progressive Web Apps
slug: progressive-web-apps
category: web-development
subcategory: null
tier: foundational
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Next steps: overview of web development"
chapter_number: 49
pdf_page: null
section: "49.2 Things worth learning for web development"
extraction_confidence: high
aliases:
  - PWA
  - PWAs
prerequisites: []
extends: []
related:
  - web-development-overview
contrasts_with: []
answers_questions:
  - "What should I learn next for web development?"
---

# Quick Definition

Progressive Web Apps (PWAs) are web applications enhanced with native-app-like features -- native installation, offline operation, and push notifications -- achieved through HTTPS, a web app manifest file, and a service worker.

# Core Definition

"Exploring JavaScript" Ch. 49: "The driving idea behind progressive web apps is to give web apps features that, traditionally, only native apps had -- for example: native installation on mobile and desktop operating systems; offline operation; showing notifications to users." Minimum requirements: HTTPS, Web App Manifest file, and a service worker.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Served over HTTPS (not HTTP)
2. Web App Manifest: metadata (app name, icons)
3. Service worker: background process for offline support, caching, push notifications
4. Service worker acts as local proxy for web resource requests
5. Can be installed on mobile and desktop OS

# Construction / Recognition

Not demonstrated with code. PWAs are identified by their manifest file, service worker registration, and HTTPS deployment.

# Context & Application

PWAs bridge the gap between web and native apps, providing native-like experience through web technologies.

# Examples

From the source, service worker capabilities: "a base layer of the app that runs in the background, in a separate process... One of its responsibilities is to keep the app functioning when there is no internet connection."

(Ch. 49, Section 49.2, lines 124-146)

# Relationships

## Related
- **Web development overview** -- PWAs are part of the web ecosystem

# Common Errors

- **Error**: Deploying a PWA without HTTPS
  **Correction**: HTTPS is a minimum requirement for PWAs

# Common Confusions

- **Confusion**: PWAs require a specific framework
  **Clarification**: PWAs are built on web standards (manifest, service workers, HTTPS) and can use any framework

# Source Reference

Chapter 49: Next steps: overview of web development, Section 49.2, lines 124-148.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with minimum requirements
- Cross-reference status: verified
