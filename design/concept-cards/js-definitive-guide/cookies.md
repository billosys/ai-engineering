---
concept: Cookies
slug: cookies
category: browser-apis
subcategory: storage
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 556
section: "15.12.2 Cookies"
extraction_confidence: high
aliases:
  - HTTP cookies
  - document.cookie
prerequisites: []
extends: []
related:
  - localstorage-and-sessionstorage
contrasts_with:
  - localstorage-and-sessionstorage
answers_questions:
  - "How do localStorage and sessionStorage differ?"
---

# Quick Definition

Cookies are small named data strings stored by the browser and automatically transmitted with every HTTP request to the associated server, managed through the cryptic `document.cookie` string property with attributes controlling lifetime, path, domain, and security.

# Core Definition

A cookie is a small amount of named data stored by the web browser and associated with a particular web page or website. Cookie data is automatically transmitted between browser and server with every HTTP request. The JavaScript API uses `document.cookie` for reading (returns all cookies as a semicolon-separated string) and setting (assigning a name=value string). Cookie attributes include `max-age` (lifetime in seconds), `path` (URL scope), `domain` (subdomain sharing), and `secure` (HTTPS only). The 4KB size limit per cookie still applies (Flanagan, Ch. 15, pp. 556-560).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Automatically sent with every HTTP request to the matching server.
2. Transient by default; use `max-age` to persist across sessions.
3. Scoped by origin and path; `domain` attribute enables subdomain sharing.
4. 4KB size limit per cookie.
5. Delete by setting `max-age=0`.

# Construction / Recognition

```javascript
document.cookie = `version=${encodeURIComponent(document.lastModified)}`;
document.cookie = `name=value; max-age=${60*60*24*365}; path=/`;
```

# Context & Application

Primarily designed for server-side session management. For client-only storage, `localStorage` is easier and does not add HTTP overhead.

# Examples

From the source (p. 559): A `setCookie()` function that encodes the value and optionally sets `max-age`:
```javascript
function setCookie(name, value, daysToLive=null) {
  let cookie = `${name}=${encodeURIComponent(value)}`;
  if (daysToLive !== null) {
    cookie += `; max-age=${daysToLive*60*60*24}`;
  }
  document.cookie = cookie;
}
```

# Relationships

## Builds Upon
- (None - foundational)

## Enables
- Server-side session management

## Related
- **localstorage-and-sessionstorage** — Modern, simpler alternative for client-side storage

## Contrasts With
- **localstorage-and-sessionstorage** — Cookies are sent with every HTTP request; Web Storage is not

# Common Errors

- **Error**: Expecting `document.cookie = "name=value"` to overwrite all cookies.
  **Correction**: Setting `document.cookie` adds or updates a single cookie; it does not replace all cookies.

# Common Confusions

- **Confusion**: Cookies are a good choice for large client-side data.
  **Clarification**: Cookies have a 4KB limit and add HTTP overhead. Use `localStorage` or `IndexedDB` for larger data.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.12.2, pages 556-560.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Comprehensive coverage of attributes and limitations
- Uncertainties: None
- Cross-reference status: Verified
