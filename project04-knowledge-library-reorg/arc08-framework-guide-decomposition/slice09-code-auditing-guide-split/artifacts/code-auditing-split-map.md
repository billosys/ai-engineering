# Code-Auditing Split Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice09-code-auditing-guide-split
artifact: code-auditing-split-map
source_commit: 1eb10d789734d9cca5c2c0f7cdedb4257dfab1e6
```

## Accepted Guide Set

Slice09 implemented the five accepted numbered code-auditing guides:

- `knowledge/code-auditing/guides/01-audit-scope-and-map.md`
- `knowledge/code-auditing/guides/02-findings-and-severity.md`
- `knowledge/code-auditing/guides/03-scale-aware-auditing.md`
- `knowledge/code-auditing/guides/04-modernization-synthesis.md`
- `knowledge/code-auditing/guides/05-audit-to-hardening-handoff.md`

The split is semantic, not heading-only. Each guide is independently loadable
and contains cross-links to the companion guide needed for the next audit
stage.

## Semantic Preservation Map

| Former `CODE-AUDIT.md` material | New owner | Preservation claim |
|---------------------------------|-----------|--------------------|
| Diagnosis-only audit posture; "context window is not the scope" guardrail | `01-audit-scope-and-map.md` and `05-audit-to-hardening-handoff.md` | Preserved as the opening audit contract and the handoff boundary. |
| Date capture, project context reading, architecture-doc gap handling | `01-audit-scope-and-map.md` | Preserved in the preparation section. |
| Language/tool detection by manifests, config files, extensions, and Tailwind CSS content | `01-audit-scope-and-map.md` | Preserved as language/tool detection rules. |
| Matching detected languages to `knowledge/<slug>/` skills and loading `SKILL*.md` plus guides | `01-audit-scope-and-map.md` | Preserved as required skill loading. |
| Audit-map construction across source, tests, generated/vendor boundaries, packages, entrypoints, and cross-cutting contracts | `01-audit-scope-and-map.md` | Preserved as "Build The Audit Map". |
| Output files for per-language reports, top-level index, and modernization synthesis | `01-audit-scope-and-map.md` and `04-modernization-synthesis.md` | Preserved with the same `workbench/<DATE>-...` output homes. |
| Per-language report structure | `02-findings-and-severity.md` | Preserved as the report contract. |
| Severity classes and stable finding format with file:line evidence | `02-findings-and-severity.md` | Preserved with Blocker, High, Medium, Low and required file:line locations. |
| Coherence observations and cross-cutting findings | `02-findings-and-severity.md` | Preserved with escalation rules for concrete failure modes. |
| Negative findings | `02-findings-and-severity.md` | Preserved as "Things I looked for and did not find". |
| Required scale coverage from line/function through workspace/monorepo | `03-scale-aware-auditing.md` | Preserved as required scales and evidence section. |
| Cross-language and per-language hunt lists | `03-scale-aware-auditing.md` | Preserved as the hunt-list contract. |
| Modernization synthesis structure and evidence rules | `04-modernization-synthesis.md` | Preserved with compatibility classification and deferral rules. |
| Final verification checklist and audit-to-hardening boundary | `05-audit-to-hardening-handoff.md` | Preserved and made explicit as the handoff gate. |

## Selective Loading

The new load paths reduce required context for common tasks:

- Starting or scoping an audit loads `01-audit-scope-and-map.md`.
- Writing or reviewing findings loads `02-findings-and-severity.md`.
- Checking audit breadth loads `03-scale-aware-auditing.md`.
- Producing the modernization synthesis loads `04-modernization-synthesis.md`.
- Turning findings into follow-up testing or hardening work loads
  `05-audit-to-hardening-handoff.md`.

## Quality-Floor Preservation

The split preserves the required audit floor:

- diagnosis-only, no code changes during audit;
- language/tool detection and skill-backed review;
- audit map before findings;
- all-scale review, not context-window sampling;
- severity classes from Blocker through Low;
- stable finding IDs and file:line evidence;
- per-language reports and top-level index;
- modernization synthesis grounded in finding IDs;
- negative findings;
- final verification checklist;
- handoff to testing and validation without softening root-cause repair.
