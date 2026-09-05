---
name: code-auditing
description: |
  Component framework/operational skill for commissioning evidence-based code
  audits. Use when a repository, language surface, package, or body of work
  needs severity-graded findings grounded in actual files and verification
  evidence, without making code changes during the audit.
version: 1.1.0
license: MIT
metadata:
  hermes:
    tags: [ai-engineering, audit, code-review, verification]
    category: meta-skills
---

# Code Auditing

Use this component for diagnosis-only audits. It routes to focused audit guides
for scope mapping, severity/file-line findings, scale-aware review,
modernization synthesis, and the audit-to-hardening handoff.

Read only the guide needed for the work:

- [Audit Scope And Map](./guides/01-audit-scope-and-map.md) - audit stance,
  source discovery, language/tool detection, skill loading, audit map, and
  output files.
- [Findings And Severity](./guides/02-findings-and-severity.md) - report
  structure, finding format, severity classes, coherence observations,
  cross-cutting findings, and negative findings.
- [Scale-Aware Auditing](./guides/03-scale-aware-auditing.md) - required review
  scales and cross-language/per-language hunt lists.
- [Modernization Synthesis](./guides/04-modernization-synthesis.md) -
  evidence-backed modernization themes, moves, compatibility classification,
  and deferrals.
- [Audit To Hardening Handoff](./guides/05-audit-to-hardening-handoff.md) -
  diagnosis-only boundary, follow-up work packet, testing/validation routing,
  and final verification checklist.

This is a component entrypoint for the collaboration framework. It is included
inside `collaboration-framework.zip` as routed dependency material, not as a
separate installable package.

Component history lives in [version-history.md](./version-history.md).
