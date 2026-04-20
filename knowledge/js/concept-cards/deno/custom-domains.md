---
# === CORE IDENTIFICATION ===
concept: Custom Domains
slug: custom-domains

# === CLASSIFICATION ===
category: infrastructure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/domains.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "domain management"
  - "organization domains"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - deploy-timelines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use a custom domain with Deno Deploy?"
  - "How does TLS work on Deno Deploy?"
---

# Quick Definition
Deno Deploy provides default domains (`<app>.<org>.deno.net`) for all applications and supports custom domains with automatic TLS provisioning via Let's Encrypt, wildcard support, and flexible DNS configuration methods.

# Core Definition
Every Deno Deploy organization receives a default domain (`<org-slug>.deno.net`), and each application gets a production domain at `<app-slug>.<org-slug>.deno.net`. Custom domains can be added at the organization level and assigned to applications. Domains can be base domains or wildcards (`*.example.com`), with wildcard domains assignable to one app entirely or partially to multiple apps. TLS certificates are automatically provisioned via Let's Encrypt or can be uploaded manually (RSA 2048-4096 or ECDSA P-256/P-384/P-521). DNS configuration supports ANAME/ALIAS (preferred), CNAME, or A record methods.

# Prerequisites
- deno-deploy -- Custom domains are configured within Deno Deploy organizations

# Key Properties
1. **Default domains** -- Automatic `<app>.<org>.deno.net` for every application
2. **Wildcard support** -- `*.example.com` assignable to one or multiple apps
3. **Three DNS methods** -- ANAME/ALIAS (preferred), CNAME (not for apex), A record (most compatible)
4. **Automatic TLS** -- Let's Encrypt provisioning with auto-renewal
5. **Bring your own certificate** -- Upload PEM certificate and private key; manual renewal required
6. **Organization-level management** -- Domains belong to organizations, assigned to apps
7. **Renewal notifications** -- Email sent 14 days before certificate expiry

# Construction / Recognition
- Add domain via organization Domains tab
- Configure DNS records as shown in the configuration drawer
- Verify domain ownership (automatic or manual trigger)
- Provision TLS certificate (automatic Let's Encrypt or manual upload)
- Assign to application(s)

# Context & Application
Custom domains are essential for production applications that need branded URLs. The wildcard domain feature enables multi-tenant architectures where different subdomains route to different applications. The ANAME/ALIAS method is preferred because it supports apex domains and other DNS record types simultaneously. Cloudflare users must disable proxy (orange cloud) for `_acme-challenge` CNAME records.

# Examples
From deploy/reference/domains.md:
- Default domain: organization `acme-inc` gets `acme-inc.deno.net`; app `my-app` gets `my-app.acme-inc.deno.net`
- Wildcard partial assignment: different subdomains of `*.example.com` to different apps
- "Deno Deploy does not currently support IPv6" with the A record method

# Relationships
## Builds Upon
- deno-deploy (domains are a platform feature)

## Related
- deploy-timelines (custom domains map to the production timeline)

# Common Errors
1. Using Cloudflare proxy on `_acme-challenge` CNAME -- verification and certificate provisioning will fail
2. Renaming an app breaks `deno.net` URLs -- previous URLs stop working (custom domains unaffected)

# Common Confusions
1. **CNAME for apex domains** -- CNAME records cannot be used for apex/root domains; use ANAME/ALIAS or A record instead

# Source Reference
- deploy/reference/domains.md: Complete domain management documentation

# Verification Notes
- High confidence: Explicitly documented with DNS configuration methods, TLS options, and step-by-step instructions
