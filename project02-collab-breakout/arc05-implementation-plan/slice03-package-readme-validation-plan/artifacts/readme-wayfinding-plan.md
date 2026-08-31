# README Wayfinding Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice03-package-readme-validation-plan
status: proposed-done
artifact-status: readme wayfinding plan
source-files-edited: false
```

## Grounding

This README plan consumes verified Slice01 release validation evidence,
verified Slice02 component contract and file layout evidence, and
`operator-accepted-architecture`. It preserves the daily-driver composer while
making standalone use of every accepted component visible. It is not final
README prose.

## README Information Architecture

Recommended README changes:

- Keep a top-level "The collaboration framework" section, but make the first
  route the composed use case: load the daily-driver composer
  `collaboration-framework` when a session needs the full posture and route
  table.
- Add a compact component table that explains usefulness and standalone use
  for `engineering-methods`, `project-management`, `work-verification`,
  `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`.
- Add a "Reader modes" subsection that distinguishes source checkout,
  generated zip, unzipped/install, and installed skill use.
- Keep the build/install section as the release command home, updated after
  Makefile planning closes.
- Keep CCDP in its separate README section with explicit CCDP separation.

## Component Usefulness Table

| Component | README usefulness | composed use | standalone use |
|-----------|-------------------|--------------|----------------|
| `collaboration-framework` | Daily-driver composer for sustained, high-stakes work. | The default composed use route; it points to all specialist components. | Useful alone when the operator wants posture plus route selection without loading a specialist yet. |
| `engineering-methods` | Methodology, LLM-centric SDLC, operational routing, and source/package/release gates. | Supplies process/gate language to the composer and specialist components. | Useful alone for planning process, gate design, or component-boundary work. |
| `project-management` | Project/arc/slice planning and close lifecycle. | Used when the composer routes into planning or closure. | Useful alone when opening, checking, or closing planning work. |
| `work-verification` | Ledgers, evidence strength, independent verification, and silent-drop prevention. | Supplies closure discipline to PM, audits, tests, and the composer. | Useful alone for ledgered work or CDC-style verification. |
| `testing` | Testing discipline, coverage hardening, and validation gates. | Receives hardening handoffs from auditing and route decisions from methodology. | Useful alone when a task is mainly about tests, coverage, or validation. |
| `code-auditing` | Diagnosis-only audit discipline with severity and stage/scale guidance. | Can hand findings to testing and PM/verification workflows. | Useful alone for review/audit work that should not edit code. |
| `agent-coordination` | CC/CDC/operator terms, delegation decisions, context packets, and result integration. | Supports multi-agent or multi-surface workflows from the composer. | Useful alone when delegation, handoff, or integration quality is the task. |
| `contribution-style` | Upstream contribution voice, ticket shape, and ticket template use. | Uses collaboration posture and can consume audit findings. | Useful alone when drafting an issue, PR note, or upstream question. |

## Reader Modes

| Reader mode | README route |
|-------------|--------------|
| source checkout | Point to component roots such as `collaboration-framework/SKILL.md`, `engineering-methods/SKILL.md`, and package-local source paths. Source checkout links may use repository-relative paths when the target is expected to exist in the repo. |
| generated zip | Explain that each generated zip has one package root matching the component name, and that readers start at `<component>/SKILL.md` after unzipping. |
| unzipped/install | Explain that `make install` unpacks skill packages into the install directory, preserving component roots. |
| installed skill | Use installed skill route wording such as `/collaboration-framework`, `/engineering-methods`, `/project-management`, `/work-verification`, `/testing`, `/code-auditing`, `/agent-coordination`, and `/contribution-style`. |

## Migration Notes

- Do not make the daily-driver composer look deprecated. The README should say
  the composer remains the default for broad sustained work, while specialists
  are useful when the task has a narrower reason to load.
- Explicitly name the old monolithic source shape as historical during the
  migration, especially top-level `SKILL.md`, `docs/CLAUDE-CODE-COVERAGE.md`,
  `docs/SUBAGENT-DELEGATION-POLICY.md`, `docs/CODE-AUDIT.md`, and
  `docs/CONTRIBUTION-STYLE.md`.
- Preserve source provenance while guiding new readers to component roots.
- Keep CCDP separation in the README: CCDP is a protocol distribution with
  `ccdp.zip`, not a collaboration-framework component skill package.
