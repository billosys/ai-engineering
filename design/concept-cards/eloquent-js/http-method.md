---
concept: HTTP Method
slug: http-method
category: http-forms
subcategory: protocol
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "The protocol"
extraction_confidence: high
aliases:
  - HTTP verb
  - request method
  - GET POST PUT DELETE
prerequisites:
  - http
extends: []
related:
  - fetch-api
  - rest-api
contrasts_with: []
answers_questions:
  - "What are HTTP methods?"
  - "What is the difference between GET, POST, PUT, and DELETE?"
---

# Quick Definition
HTTP methods (GET, POST, PUT, DELETE) indicate the intended action for a request: GET retrieves data, POST sends data, PUT creates or replaces a resource, and DELETE removes one.

# Core Definition
"The first word is the method of the request. `GET` means that we want to get the specified resource. Other common methods are `DELETE` to delete a resource, `PUT` to create or replace it, and `POST` to send information to it" (Ch. 18, "The protocol"). GET requests should have no side effects; POST, PUT, and DELETE may modify server state.

# Prerequisites
- **HTTP**: Methods are part of the HTTP protocol

# Key Properties
1. GET -- retrieve a resource (no side effects, no body)
2. POST -- send data to a resource (has body)
3. PUT -- create or replace a resource (has body)
4. DELETE -- remove a resource (no body)
5. GET and DELETE don't send bodies; PUT and POST do

# Construction / Recognition
```http
GET /18_http.html HTTP/1.1
Host: eloquentjavascript.net
```

```http
POST /example/message.html HTTP/1.1
Content-type: application/x-www-form-urlencoded

name=Jean&message=Yes%3F
```

# Context & Application
Fundamental to web development and API design. REST APIs use HTTP methods to indicate operations on resources.

# Examples
Using methods with fetch:
```javascript
fetch("example/data.txt", {method: "DELETE"}).then(resp => {
  console.log(resp.status); // → 405
});
```

# Relationships
## Builds Upon
- http
## Enables
- fetch-api, rest-api, form-element
## Related
- http-status-code, request-headers, response-object
## Contrasts With
- Remote procedure calls (function-name-based instead of method-based)

# Common Errors
- **Error**: Using GET for requests that modify data
  **Correction**: Use POST, PUT, or DELETE for state-changing operations

# Common Confusions
- **Confusion**: POST and PUT are interchangeable
  **Clarification**: PUT creates/replaces a resource at a specific URL; POST sends data to be processed

# Source Reference
Chapter 18: HTTP and Forms, Section "The protocol", lines 80-164 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: All four methods explicitly defined
- Cross-reference status: verified
