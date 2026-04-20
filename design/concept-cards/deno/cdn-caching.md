---
# === CORE IDENTIFICATION ===
concept: CDN Caching
slug: cdn-caching

# === CLASSIFICATION ===
category: infrastructure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/caching.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "edge caching"
  - "HTTP caching"
  - "Deno Deploy CDN"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - deploy-builds
  - deploy-timelines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does CDN caching work in Deno Deploy?"
  - "How do I invalidate cached content on Deno Deploy?"
---

# Quick Definition
Deno Deploy includes a built-in HTTP caching layer at the edge that automatically caches eligible responses, supports tag-based invalidation, and follows RFC 9110/9111 semantics.

# Core Definition
Deno Deploy's CDN caching layer intercepts responses at the edge, storing cacheable content to reduce latency and origin load. It follows standard HTTP caching semantics (RFC 9110, RFC 9111) and adds Deno-specific headers for fine-grained control. Responses are cached based on `Cache-Control` directives, with a priority chain of `Deno-CDN-Cache-Control` > `CDN-Cache-Control` > `Cache-Control`. Cache tags (`Deno-Cache-Tag`) enable targeted invalidation via a local API endpoint. By default, all cached responses are automatically invalidated on new deployments unless opted out with `Deno-Cache-Id`.

# Prerequisites
- deno-deploy -- CDN caching is a built-in feature of the Deno Deploy platform

# Key Properties
1. **RFC-compliant** -- Follows RFC 9110 and RFC 9111 HTTP caching semantics
2. **Deno-CDN-Cache-Control** -- Highest-priority cache directive, overrides both CDN-Cache-Control and Cache-Control
3. **Cache tags** -- `Deno-Cache-Tag` / `Cache-Tag` headers associate responses with tags; up to 500 tags per response, 1024 chars per tag
4. **Deno-Cache-Id** -- Opts responses out of automatic deployment invalidation; persists across redeployments
5. **Tag-based invalidation** -- POST to `http://cache.localhost/invalidate/http` with tags array; wildcard `"*"` purges all
6. **Cross-region propagation** -- Cache invalidation synchronizes across all Deploy regions within seconds
7. **Automatic deployment invalidation** -- Responses without `Deno-Cache-Id` are purged on new deployments
8. **Cache-Status header** -- Response header indicating hit/miss/bypass status with detailed reason codes

# Construction / Recognition
- Set caching: `"Cache-Control": "public, s-maxage=3600"`
- Deploy-specific control: `"Deno-CDN-Cache-Control": "public, s-maxage=3600"`
- Tag responses: `"Deno-Cache-Tag": "product-123,products,catalog"`
- Invalidate:
  ```typescript
  await fetch("http://cache.localhost/invalidate/http", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tags: ["products"] }),
  });
  ```

# Context & Application
CDN caching is essential for reducing latency and origin load on Deno Deploy applications. It is particularly useful for content-heavy sites, API responses that change infrequently, and static assets. The tag-based invalidation system supports CMS webhook integration, enabling selective cache purges when content changes. `Deno-Cache-Id` is ideal for content-addressed static assets that should survive redeployments.

# Examples
From deploy/reference/caching.md:
- Cache for 1 hour at edge: `"Cache-Control": "public, s-maxage=3600"`
- Different browser vs CDN TTL: browser 60s via `max-age=60`, CDN 1 hour via `Deno-CDN-Cache-Control: public, s-maxage=3600`
- Stale-while-revalidate: `"Cache-Control": "public, s-maxage=60, stale-while-revalidate=300"`
- Cache status values: `deno; hit`, `deno; fwd=uri-miss; stored`, `deno; fwd=bypass` with detail codes

# Relationships
## Builds Upon
- deno-deploy (caching is a platform feature)

## Related
- deploy-builds (new deployments trigger automatic cache invalidation)
- deploy-timelines (cache is per-deployment unless Deno-Cache-Id is used)

# Common Errors
1. Forgetting that `Set-Cookie` headers prevent caching -- responses with `Set-Cookie` bypass the cache entirely
2. Using `Vary: *` -- this prevents caching entirely

# Common Confusions
1. **Automatic vs. explicit invalidation** -- Without `Deno-Cache-Id`, all cache is wiped on each deploy; with it, content persists across deploys
2. **s-maxage vs. max-age** -- `s-maxage` controls CDN/shared cache duration; `max-age` controls browser cache duration

# Source Reference
- deploy/reference/caching.md: Complete caching documentation including headers, invalidation API, best practices

# Verification Notes
- High confidence: Comprehensive source documentation with explicit header definitions and API specifications
