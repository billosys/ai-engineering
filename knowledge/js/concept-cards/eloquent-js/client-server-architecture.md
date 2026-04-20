---
concept: Client-Server Architecture
slug: client-server-architecture
category: server-side
subcategory: web-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: Skill-Sharing Website"
chapter_number: 21
pdf_page: null
section: "Design"
extraction_confidence: high
aliases:
  - client-server model
  - full-stack architecture
prerequisites:
  - http
  - nodejs
extends: []
related:
  - rest-api
  - long-polling
  - fetch-api
contrasts_with: []
answers_questions:
  - "What is client-server architecture?"
  - "What must I know before building a web application?"
---

# Quick Definition
Client-server architecture separates an application into a server (Node.js) that stores data and handles API requests, and a client (browser JavaScript) that presents the UI and communicates with the server via HTTP.

# Core Definition
"There is a server part to this project, written for Node.js, and a client part, written for the browser. The server stores the system's data and provides it to the client. It also serves the files that implement the client-side system" (Ch. 21, "Design"). The client displays data, captures user actions, and sends HTTP requests to update server state.

# Prerequisites
- **HTTP**: Communication protocol between client and server
- **Node.js**: Server runtime

# Key Properties
1. Server stores and manages data (single source of truth)
2. Client renders UI and handles user interaction
3. Communication via HTTP requests (fetch on client, createServer on server)
4. Server serves both API endpoints and static files
5. Multiple clients can connect simultaneously

# Construction / Recognition
The skill-sharing project has:
- Server: `skillsharing_server.mjs` (Node.js, handles /talks API + serves static files)
- Client: `public/skillsharing_client.js` (browser, renders UI, uses fetch)
- Shared: JSON format for data exchange

# Context & Application
The standard architecture for web applications. Every website with dynamic data follows this pattern, from simple blogs to complex SaaS applications.

# Examples
"Each talk has a presenter name, a title, a summary, and an array of comments associated with it. The client allows users to propose new talks, delete talks, and comment on existing talks. Whenever the user makes such a change, the client makes an HTTP request to tell the server about it."

# Relationships
## Builds Upon
- http, nodejs
## Enables
- Multi-user applications, data sharing, web applications
## Related
- rest-api, long-polling, fetch-api, state-management
## Contrasts With
- Peer-to-peer architecture (no central server)

# Common Errors
- **Error**: Trusting client-side validation alone
  **Correction**: Always validate on the server; client validation is for UX only

# Common Confusions
- **Confusion**: The client and server must use the same language
  **Clarification**: They communicate via HTTP/JSON; either side can use any language (though JS on both is convenient)

# Source Reference
Chapter 21: Project: Skill-Sharing Website, Section "Design", lines 52-78 of 21-project-skill-sharing-website.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly described architecture
- Cross-reference status: verified
