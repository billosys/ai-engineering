---
concept: Conditional Request
slug: conditional-request
category: server-side
subcategory: http-caching
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: Skill-Sharing Website"
chapter_number: 21
pdf_page: null
section: "HTTP interface"
extraction_confidence: high
aliases:
  - If-None-Match
  - 304 Not Modified
prerequisites:
  - etag
  - http-status-code
extends: []
related:
  - long-polling
contrasts_with: []
answers_questions:
  - "How do conditional HTTP requests work?"
---

# Quick Definition
A conditional request includes an `If-None-Match` header with a previously received ETag; the server responds with 304 "Not Modified" if the resource hasn't changed, avoiding unnecessary data transfer.

# Core Definition
"Clients, when they later request that resource again, may make a conditional request by including an `If-None-Match` header whose value holds that same string. If the resource hasn't changed, the server will respond with status code 304, which means 'not modified', telling the client that its cached version is still current" (Ch. 21).

# Prerequisites
- **ETag**: Conditional requests use ETag values
- **HTTP status codes**: 304 means "not modified"

# Key Properties
1. Client sends `If-None-Match: "etag"` header
2. Server compares with current ETag
3. Match → 304 response (no body)
4. No match → full response with new ETag
5. In long polling, server delays 304 instead of sending immediately

# Construction / Recognition
```javascript
router.add("GET", /^\/talks$/, async (server, request) => {
  let tag = /"(.*)"/.exec(request.headers["if-none-match"]);
  let wait = /\bwait=(\d+)/.exec(request.headers["prefer"]);
  if (!tag || tag[1] != server.version) {
    return server.talkResponse();
  } else if (!wait) {
    return {status: 304};
  } else {
    return server.waitForChanges(Number(wait[1]));
  }
});
```

# Context & Application
Reduces bandwidth and server load by avoiding retransmission of unchanged resources. Combined with long polling, enables efficient real-time updates.

# Examples
"When the tag does not match, the server responds as normal."

# Relationships
## Builds Upon
- etag, http-status-code
## Enables
- Efficient caching, long-polling, bandwidth savings
## Related
- long-polling, real-time-updates
## Contrasts With
- Unconditional requests (always fetch full resource)

# Common Errors
- **Error**: Comparing ETags without quotes
  **Correction**: ETags include quotes; parse them properly

# Common Confusions
- **Confusion**: 304 means an error
  **Clarification**: 304 is a success response meaning "your cached version is still valid"

# Source Reference
Chapter 21: Project: Skill-Sharing Website, Section "HTTP interface", lines 222-262, and "Long polling support", lines 550-636 of 21-project-skill-sharing-website.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Implementation shown in context
- Cross-reference status: verified
