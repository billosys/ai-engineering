---
concept: Real-Time Updates
slug: real-time-updates
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
  - live updates
  - push notifications
prerequisites:
  - long-polling
  - client-server-architecture
extends: []
related:
  - etag
  - conditional-request
contrasts_with: []
answers_questions:
  - "How do I show real-time updates in a web application?"
---

# Quick Definition
Real-time updates push changes to all connected clients immediately when data changes on the server, implemented in this project via long polling where pending requests are resolved when the server state is modified.

# Core Definition
"The application will be set up to show a live view of the current proposed talks and their comments. Whenever someone, somewhere, submits a new talk or adds a comment, all people who have the page open in their browsers should immediately see the change" (Ch. 21, "Design"). The `updated()` method resolves all waiting long-poll promises with the new data.

# Prerequisites
- **Long polling**: The transport mechanism for real-time updates
- **Client-server architecture**: Updates flow from server to all clients

# Key Properties
1. Server maintains list of waiting client connections
2. When state changes, all waiting clients receive updated data
3. Clients immediately re-poll after receiving an update
4. Version numbers (ETags) track what clients have seen
5. Timeout prevents stale connections

# Construction / Recognition
```javascript
SkillShareServer.prototype.updated = function() {
  this.version++;
  let response = this.talkResponse();
  this.waiting.forEach(resolve => resolve(response));
  this.waiting = [];
};
```

Client-side polling loop:
```javascript
async function pollTalks(update) {
  let response = await fetchOK("/talks", {
    headers: tag ? {"If-None-Match": tag, "Prefer": "wait=90"} : {}
  });
  if (response.status == 304) return;
  tag = response.headers.get("ETag");
  update(await response.json());
}
```

# Context & Application
Real-time features are expected in modern web apps: chat, collaborative editing, live dashboards, notifications. Long polling is one approach; WebSockets and Server-Sent Events are alternatives.

# Examples
"When Iman submits a talk on Extreme Downhill Unicycling, the server will notice that Fatma is waiting for updates and send a response containing the new talk to her pending request."

# Relationships
## Builds Upon
- long-polling, client-server-architecture
## Enables
- Live collaborative features, notifications, chat
## Related
- etag, conditional-request, server-state
## Contrasts With
- Manual refresh (user must reload page), WebSockets (persistent connection)

# Common Errors
- **Error**: Not reconnecting after a polling error
  **Correction**: Always restart the poll loop after errors or timeouts

# Common Confusions
- **Confusion**: All clients see updates at exactly the same instant
  **Clarification**: There's slight latency based on when each client's poll request is pending

# Source Reference
Chapter 21: Project: Skill-Sharing Website, Section "Design" and "Long polling", lines 72-135, and "Long polling support", lines 550-646 of 21-project-skill-sharing-website.md.

# Verification Notes
- Definition source: synthesized from design and implementation
- Confidence rationale: Core feature of the project
- Cross-reference status: verified
