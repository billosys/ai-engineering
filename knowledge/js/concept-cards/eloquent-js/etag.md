---
concept: ETag
slug: etag
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
  - entity tag
prerequisites:
  - request-headers
  - http-status-code
extends: []
related:
  - conditional-request
  - long-polling
contrasts_with: []
answers_questions:
  - "What is an ETag header?"
  - "How does HTTP caching work?"
---

# Quick Definition
An ETag (entity tag) is a response header containing a version identifier for a resource, enabling conditional requests where the client sends back the ETag to check if the resource has changed.

# Core Definition
"Servers may include an `ETag` ('entity tag') header in a response. Its value is a string that identifies the current version of the resource" (Ch. 21, "HTTP interface"). The skill-sharing server uses a version number as the ETag, incrementing it when talks change.

# Prerequisites
- **HTTP headers**: ETag is a response header
- **Status codes**: 304 "Not Modified" is the conditional response

# Key Properties
1. Server includes `ETag: "value"` in responses
2. Client sends `If-None-Match: "value"` in subsequent requests
3. If resource unchanged: server returns 304 (use cached version)
4. If changed: server returns new resource with new ETag
5. In skill-sharing app, ETag is the version counter as a string

# Construction / Recognition
```javascript
return {
  body: JSON.stringify(talks),
  headers: {"Content-Type": "application/json",
            "ETag": `"${this.version}"`,
            "Cache-Control": "no-store"}
};
```

# Context & Application
ETags are standard HTTP caching mechanism. The skill-sharing app repurposes them for long polling -- the client sends its known version, and the server responds only when the version changes.

# Examples
Client request with ETag:
```http
GET /talks HTTP/1.1
If-None-Match: "4"
Prefer: wait=90
```

# Relationships
## Builds Upon
- request-headers, http-status-code
## Enables
- Efficient caching, conditional-request, long-polling
## Related
- long-polling, real-time-updates
## Contrasts With
- Last-Modified header (date-based instead of tag-based)

# Common Errors
- **Error**: Using ETags without quotes
  **Correction**: ETag values must be quoted strings per the HTTP spec

# Common Confusions
- **Confusion**: ETags are only for caching
  **Clarification**: They can be repurposed for change detection, as in long polling

# Source Reference
Chapter 21: Project: Skill-Sharing Website, Section "HTTP interface", lines 218-262 of 21-project-skill-sharing-website.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explained with practical implementation
- Cross-reference status: verified
