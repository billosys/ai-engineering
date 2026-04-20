---
# === CORE IDENTIFICATION ===
concept: Sandbox Security
slug: sandbox-security

# === CLASSIFICATION ===
category: sandbox
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "sandbox/security.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sandbox isolation"
  - "network policies"
  - "secret redaction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-sandbox
extends: []
related:
  - deploy-observability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Deno Sandbox protect against untrusted code?"
  - "How do secrets work in Deno Sandbox?"
  - "How do I restrict network access in Deno Sandbox?"
---

# Quick Definition
Deno Sandbox employs a defense-in-depth security model with hypervisor-level VM isolation, outbound network allowlists (`allowNet`), secret redaction with host-scoped substitution, filesystem cleanup on teardown, and full audit trails via observability integration.

# Core Definition
Deno Sandbox is designed for untrusted and AI-generated workloads. Every VM is ephemeral, isolated at the hypervisor level (not container-level), and governed by strict outbound policies. The security model has four pillars: (1) network control via `allowNet` host allowlists that block outbound requests to unapproved hosts, (2) secret redaction where real credential values never enter sandbox environment variables -- placeholders are substituted only on outbound requests to approved hosts, (3) filesystem isolation where VMs boot from clean disk images and are wiped on destruction, and (4) auditing where every command, HTTP request, and SSH session is traceable in the Deploy dashboard.

# Prerequisites
- deno-sandbox -- Security features are part of the sandbox platform

# Key Properties
1. **Hypervisor-level isolation** -- Each sandbox is a dedicated microVM, not a shared-kernel container
2. **Secret redaction** -- Environment variables hold placeholders; real values substituted only on approved outbound requests
3. **Host-scoped secrets** -- Each secret specifies which hosts it can be sent to: `{ hosts: ["api.openai.com"], value: "sk-..." }`
4. **Network allowlist** -- `allowNet: ["api.openai.com", "*.anthropic.com"]` blocks all other outbound traffic
5. **Pattern matching** -- Exact hostname, hostname:port, wildcard subdomain (`*.example.com`), IPv4, IPv6
6. **Default: unrestricted** -- When `allowNet` is omitted, all outbound requests are allowed
7. **Filesystem cleanup** -- VM destroyed and disk wiped when sandbox ends; no lingering state
8. **Volume isolation** -- Volume access is explicit per sandbox; can be mounted read-only
9. **Audit trail** -- All activity traceable in Deploy dashboard; attach metadata for agent attribution

# Construction / Recognition
```typescript
await using sandbox = await Sandbox.create({
  allowNet: ["api.openai.com", "*.anthropic.com"],
  secrets: {
    OPENAI_API_KEY: {
      hosts: ["api.openai.com"],
      value: process.env.OPENAI_API_KEY,
    },
  },
});
// Inside sandbox: echo $OPENAI_API_KEY => <placeholder>
// Outbound request to api.openai.com substitutes real key
// Outbound request to evil.com is blocked (not in allowNet)
```

# Context & Application
Sandbox security is critical for AI agent workflows where LLM-generated code may attempt prompt injection attacks to exfiltrate secrets. The secret substitution model blocks the most common attack path: code reading an environment variable and sending its value to an attacker-controlled endpoint. Even if the code reads the variable, it only sees a placeholder, and even if it makes an outbound request, the real secret is only injected for approved hosts. This enables running arbitrary code while safely calling third-party APIs.

# Examples
From sandbox/security.md:
- "Secrets never enter the sandbox environment variables. Instead, Deno Deploy substitutes them only when the sandbox makes outbound requests to an approved host."
- Inside sandbox: `echo $ANTHROPIC_API_KEY` outputs `<placeholder>`
- "This blocks the most common AI attack path of prompt injection followed by secret exfiltration while allowing your automation to call third-party APIs securely."
- Network patterns: `example.com` (any port), `example.com:443` (port 443 only), `*.example.com` (subdomains), `192.0.2.1` (IPv4)

# Relationships
## Builds Upon
- deno-sandbox (security is a core sandbox feature)

## Related
- deploy-observability (sandbox activity logged and traceable in dashboard)

# Common Errors
1. Omitting `allowNet` when running untrusted code -- without it, all outbound traffic is allowed, defeating network isolation
2. Not scoping secrets to specific hosts -- a secret without `hosts` restriction could theoretically be sent anywhere it is substituted

# Common Confusions
1. **Placeholder vs. null** -- The sandbox env var holds a placeholder string, not null; code that checks for its existence will find it "set"
2. **allowNet vs. Deno permissions** -- `allowNet` is a platform-level firewall on the VM's network; it is separate from Deno's `--allow-net` permission flag

# Source Reference
- sandbox/security.md: Defense-in-depth model, secret redaction, network control, filesystem isolation, auditing

# Verification Notes
- High confidence: Security model explicitly documented with attack vector analysis and configuration examples
