---
concept: Server Routing
slug: server-routing
category: server-side
subcategory: web-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: Skill-Sharing Website"
chapter_number: 21
pdf_page: null
section: "Routing"
extraction_confidence: high
aliases:
  - URL routing
  - router
  - route handler
prerequisites:
  - http-createserver
  - request-handling
extends: []
related:
  - rest-api
  - http-method
contrasts_with: []
answers_questions:
  - "How do you route HTTP requests to different handlers?"
  - "What must I know before building a web application?"
---

# Quick Definition
A router dispatches incoming HTTP requests to handler functions based on the request's method and URL pattern, using regular expressions to match paths and extract parameters.

# Core Definition
"A router is a component that helps dispatch a request to the function that can handle it" (Ch. 21, "Routing"). Handlers are registered with `add(method, urlPattern, handler)`. The `resolve` method matches incoming requests against registered routes, extracting URL parameters from regex groups.

# Prerequisites
- **createServer**: Router works within Node HTTP servers
- **Request handling**: Routes dispatch to request handlers

# Key Properties
1. Routes are triples: (method, URL pattern, handler)
2. URL patterns are regular expressions
3. Regex capture groups become handler arguments
4. First matching route wins
5. Returns undefined if no route matches (fall through to static files)

# Construction / Recognition
```javascript
class Router {
  constructor() { this.routes = []; }
  add(method, url, handler) {
    this.routes.push({method, url, handler});
  }
  async resolve(request, context) {
    let {pathname} = new URL(request.url, "http://d");
    for (let {method, url, handler} of this.routes) {
      let match = url.exec(pathname);
      if (!match || request.method != method) continue;
      let parts = match.slice(1).map(decodeURIComponent);
      return handler(context, ...parts, request);
    }
  }
}
```

# Context & Application
Every web framework includes a router. This chapter shows the fundamental concept: mapping (method, path) pairs to handlers. Express, Koa, and Hapi all provide more feature-rich versions.

# Examples
Registering routes:
```javascript
router.add("GET", /^\/talks\/([^\/]+)$/, async (server, title) => {
  if (Object.hasOwn(server.talks, title)) {
    return {body: JSON.stringify(server.talks[title]),
            headers: {"Content-Type": "application/json"}};
  } else {
    return {status: 404, body: `No talk '${title}' found`};
  }
});
```

# Relationships
## Builds Upon
- http-createserver, request-handling
## Enables
- REST APIs, organized server code, resource-based handlers
## Related
- rest-api, http-method
## Contrasts With
- Single handler with if/else chain

# Common Errors
- **Error**: Forgetting to decode URI components from regex matches
  **Correction**: Always decodeURIComponent on URL parts (spaces become %20, etc.)

# Common Confusions
- **Confusion**: Route order doesn't matter
  **Clarification**: First match wins; more specific routes should be registered before general ones

# Source Reference
Chapter 21: Project: Skill-Sharing Website, Section "Routing", lines 277-340 of 21-project-skill-sharing-website.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete Router implementation shown
- Cross-reference status: verified
