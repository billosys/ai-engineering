---
concept: Server State
slug: server-state
category: server-side
subcategory: web-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: Skill-Sharing Website"
chapter_number: 21
pdf_page: null
section: "The server"
extraction_confidence: high
aliases:
  - server-side state
  - in-memory state
prerequisites:
  - http-createserver
extends: []
related:
  - rest-api
  - long-polling
contrasts_with: []
answers_questions:
  - "How does a server maintain application state?"
---

# Quick Definition
Server state is in-memory data (like the talks object and version counter) maintained by the server process, accessible to all request handlers, and updated through the API endpoints.

# Core Definition
The SkillShareServer keeps state as instance properties: `talks` (an object mapping titles to talk data), `version` (incremented on changes), and `waiting` (array of pending long-polling response callbacks). The `updated()` method increments version and resolves all waiting requests.

# Prerequisites
- **createServer**: Server state lives within the server process

# Key Properties
1. State is in-memory (lost when process restarts)
2. Shared across all request handlers via the server object
3. Version number tracks changes for conditional requests
4. `updated()` notifies all waiting long-poll clients

# Construction / Recognition
```javascript
class SkillShareServer {
  constructor(talks) {
    this.talks = talks;
    this.version = 0;
    this.waiting = [];
    // ... setup server
  }
}

SkillShareServer.prototype.updated = function() {
  this.version++;
  let response = this.talkResponse();
  this.waiting.forEach(resolve => resolve(response));
  this.waiting = [];
};
```

# Context & Application
Simple in-memory state works for prototypes and small applications. Production systems typically persist state to databases.

# Examples
```javascript
new SkillShareServer({}).start(8000);
```
"The talks that have been proposed are stored in the `talks` property of the server, an object whose property names are the talk titles."

# Relationships
## Builds Upon
- http-createserver
## Enables
- Data persistence (in memory), API responses, long-polling
## Related
- rest-api, long-polling, etag
## Contrasts With
- Database-backed state (persistent across restarts)

# Common Errors
- **Error**: Assuming server state persists across restarts
  **Correction**: In-memory state is lost when the process exits; use a database for persistence

# Common Confusions
- **Confusion**: Server state and client state are synchronized automatically
  **Clarification**: They must be explicitly synchronized via API calls and long polling

# Source Reference
Chapter 21: Project: Skill-Sharing Website, Section "The server" and "Long polling support", lines 270-646 of 21-project-skill-sharing-website.md.

# Verification Notes
- Definition source: synthesized from implementation
- Confidence rationale: Complete server implementation shown
- Cross-reference status: verified
