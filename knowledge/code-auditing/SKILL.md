---
name: code-auditing
description: |
  Component framework/operational skill for commissioning evidence-based code
  audits. Use when a repository, language surface, package, or body of work
  needs severity-graded findings grounded in actual files and verification
  evidence, without making code changes during the audit.
version: 1.0.0
license: MIT
metadata:
  hermes:
    tags: [ai-engineering, audit, code-review, verification]
    category: meta-skills
---

# Code Auditing

Use this component for diagnosis-only audits. It routes to the audit guide,
which defines the evidence map, severity classes, finding format, and
multi-scale review expectations.

Read the guide:

- [Code Audit](./guides/CODE-AUDIT.md)

This is a component entrypoint for the collaboration framework. It is included
inside `collaboration-framework.zip` as routed dependency material, not as a
separate installable package.
