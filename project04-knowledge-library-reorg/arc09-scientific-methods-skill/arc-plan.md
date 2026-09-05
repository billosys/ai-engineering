# Arc 09: Scientific Methods Skill

```yaml
project: project04-knowledge-library-reorg
arc: arc09-scientific-methods-skill
status: closed
opened-by: CDC
opened-on: 2026-09-05
closed-on: 2026-09-05
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
execution-mode: cdc-direct-operator-override
source-commit: a2122abbe75b42f87e550c87ba1150b51d7abb38
```

## Capability

Arc09 adds `scientific-methods` as a live method skill that generalizes the
experiment-design pattern used for the framework-version comparison prompt:
pin the independent variable, control contamination, bound the task,
predeclare outputs and measures, preserve evidence, compare against a rubric,
and report threats to validity.

The arc also adds light collaboration-framework wayfinding so a session that
has already loaded the collaboration framework can recognize when a
conversation has become a controlled inquiry and should load
`scientific-methods` separately.

## Operator Override

The operator explicitly requested this work be recorded under Project04 but did
not require the formal CDC-to-CC handoff loop. CDC performed the implementation
directly and recorded validation evidence. The verification evidence is
same-context CDC validation, not independent CC/CDC verification.

## Slice Breakdown

Arc09 is intentionally one slice:

1. `slice01-scientific-methods-skill-implementation` - create the
   `knowledge/scientific-methods/` method skill, guides, templates,
   version-history, Makefile package target, README/docs mentions,
   collaboration-framework wayfinding, release-note reconciliation, and
   validation evidence.

This is one slice because the source change is cohesive and small enough to
hold in one context with validation headroom.

## Boundaries

In scope:

- `knowledge/scientific-methods/SKILL.md`
- `knowledge/scientific-methods/version-history.md`
- focused guides under `knowledge/scientific-methods/guides/`
- reusable templates under `knowledge/scientific-methods/templates/`
- Makefile packaging and install target wiring
- top-level README and `docs/skill-library.md` discoverability
- `docs/building-and-installing.md` target description
- `docs/collaboration-framework.md` and collaboration-framework source
  wayfinding to load `scientific-methods` separately
- release-note reconciliation for `RELEASE-0.5.0.md`

Out of scope:

- Bundling `scientific-methods` inside `collaboration-framework.zip`
- Recasting scientific-methods as a framework component
- Changing Project04 Arc08 closure status
- Implementing `concept-card-method`
- Adding a runtime experiment runner, database, or metrics service

## Validation

Arc09 validates through source and package evidence:

- source commit with explicit file set;
- `git diff --check`;
- `git diff --cached --check`;
- `make check-skills`;
- focused local Markdown link validation;
- `make scientific-methods`;
- `make check-package-paths`;
- `scientific-methods.zip` inspection;
- isolated install smoke.

## Version History

### v1.0 - 2026-09-05

Opened and closed Arc09 by operator-approved CDC-direct execution. Added the
scientific-methods method skill and collaboration-framework wayfinding as a
Project04 scope expansion after Arc08 review surfaced the general reusable
pattern.
