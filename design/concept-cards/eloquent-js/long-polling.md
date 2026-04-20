---
concept: Long Polling
slug: long-polling
category: server-side
subcategory: real-time
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: Skill-Sharing Website"
chapter_number: 21
pdf_page: null
section: "Long polling"
extraction_confidence: high
aliases:
  - HTTP long polling
  - polling
prerequisites:
  - fetch-api
  - http-createserver
  - promise
extends: []
related:
  - real-time-updates
  - etag
  - conditional-request
contrasts_with: []
answers_questions:
  - "How do I push updates to the browser without WebSockets?"
  - "What is long polling?"
---

# Quick Definition
Long polling is a technique where the client makes an HTTP request that the server holds open until new data is available (or a timeout elapses), enabling near-real-time updates over regular HTTP.

# Core Definition
"Long polling, where clients continuously ask the server for new information using regular HTTP requests, and the server stalls its answer when it has nothing new to report" (Ch. 21, "Long polling"). "As long as the client makes sure it constantly has a polling request open, it will receive information from the server quickly after it becomes available."

# Prerequisites
- **Fetch API**: Client uses fetch for polling requests
- **createServer**: Server holds response open
- **Promises**: Server uses promises to delay responses

# Key Properties
1. Client sends request; server delays response until data available
2. Timeout prevents connections from dying (e.g., 90 seconds)
3. Client immediately opens new request after receiving response
4. Uses regular HTTP, no special protocol needed
5. Node is well-suited (manages many connections without threads)

# Construction / Recognition
Server side:
```javascript
SkillShareServer.prototype.waitForChanges = function(time) {
  return new Promise(resolve => {
    this.waiting.push(resolve);
    setTimeout(() => {
      if (!this.waiting.includes(resolve)) return;
      this.waiting = this.waiting.filter(r => r != resolve);
      resolve({status: 304});
    }, time * 1000);
  });
};
```

# Context & Application
Used for real-time features (chat, notifications, live data) when WebSockets are overkill or unavailable. The skill-sharing website uses it to show live updates of new talks and comments.

# Examples
Request with long polling headers:
```http
GET /talks HTTP/1.1
If-None-Match: "4"
Prefer: wait=90
```
"The server will keep a version number that it updates every time the talks change and will use that as the `ETag` value."

# Relationships
## Builds Upon
- fetch-api, http-createserver, promise
## Enables
- real-time-updates without WebSockets
## Related
- etag, conditional-request, client-server-architecture
## Contrasts With
- WebSockets (full-duplex, persistent connection), regular polling (constant requests)

# Common Errors
- **Error**: Not setting a timeout on long-polling requests
  **Correction**: Always set a maximum wait time to handle connection drops and proxy timeouts

# Common Confusions
- **Confusion**: Long polling uses a persistent WebSocket-like connection
  **Clarification**: It uses regular HTTP requests; the server just delays the response

# Source Reference
Chapter 21: Project: Skill-Sharing Website, Section "Long polling", lines 85-135 of 21-project-skill-sharing-website.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thoroughly explained with implementation
- Cross-reference status: verified
