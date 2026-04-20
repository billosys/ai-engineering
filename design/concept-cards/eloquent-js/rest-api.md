---
concept: REST API
slug: rest-api
category: server-side
subcategory: web-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "Appreciating HTTP"
extraction_confidence: high
aliases:
  - RESTful API
  - resource-based API
prerequisites:
  - http-method
  - http
  - url
extends: []
related:
  - json-in-http
  - server-routing
  - fetch-api
contrasts_with: []
answers_questions:
  - "What is a REST API?"
  - "How do I design an HTTP API?"
---

# Quick Definition
A REST API organizes communication around resources identified by URLs, using HTTP methods (GET, PUT, POST, DELETE) to perform operations, with JSON as the typical data format.

# Core Definition
"Another approach is to build your communication around the concept of resources and HTTP methods. Instead of a remote procedure called `addUser`, you use a `PUT` request to `/users/larry`. [...] you define a JSON document format that represents a user. The body of the `PUT` request to create a new resource is then such a document" (Ch. 18, "Appreciating HTTP"). The skill-sharing project implements this: GET /talks retrieves talks, PUT /talks/Title creates one, DELETE removes one.

# Prerequisites
- **HTTP methods**: REST uses methods semantically
- **HTTP**: REST is built on HTTP
- **URLs**: Resources are identified by URLs

# Key Properties
1. Resources identified by URLs (/talks, /talks/Title)
2. HTTP methods indicate operations (GET read, PUT create/replace, DELETE remove)
3. JSON documents represent resources
4. Leverages HTTP features (caching, status codes, headers)
5. Stateless -- each request contains all necessary information

# Construction / Recognition
```http
PUT /talks/How%20to%20Idle HTTP/1.1
Content-Type: application/json

{"presenter": "Maureen", "summary": "Standing still on a unicycle"}
```

```http
GET /talks HTTP/1.1
```

# Context & Application
REST is the dominant API design style for web services. It maps naturally to HTTP and is simple to implement with any server framework.

# Examples
From Ch. 18: "This second approach makes it easier to use some of the features that HTTP provides, such as support for caching resources. The concepts used in HTTP, which are well designed, can provide a helpful set of principles to design your server interface around."

# Relationships
## Builds Upon
- http-method, http, url
## Enables
- Web APIs, client-server communication, microservices
## Related
- json-in-http, server-routing, fetch-api
## Contrasts With
- Remote procedure calls (RPC) -- function-name-based

# Common Errors
- **Error**: Using GET for operations that modify data
  **Correction**: GET should be idempotent and side-effect-free; use POST/PUT/DELETE for modifications

# Common Confusions
- **Confusion**: REST requires a specific framework
  **Clarification**: REST is an architectural style using standard HTTP; any HTTP server can implement it

# Source Reference
Chapter 18: HTTP and Forms, Section "Appreciating HTTP", lines 391-428 of 18-http-and-forms.md; Chapter 21, Section "HTTP interface", lines 137-262 of 21-project-skill-sharing-website.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly described and implemented
- Cross-reference status: verified (Ch. 18 theory, Ch. 21 practice)
