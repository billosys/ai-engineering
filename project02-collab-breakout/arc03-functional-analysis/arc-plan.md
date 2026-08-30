# Arc 03: Functional Analysis

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
status: placeholder
depends-on:
  - arc02-conceptual-analysis
blocks:
  - arc04-breakout-architecture
```

## Capability

Arc 03 will analyze the framework as a working system. It will examine how
humans and LLMs use the current framework in direct source-clone reading,
packaged skill reading, session startup, planning, execution, review,
auditing, coverage work, delegation decisions, and upstream contribution.

The output should identify inefficiencies, deficiencies, context-load costs,
unclear routing, missing entry points, packaging mismatches, and cases where
current behavior misses functional goals.

## Deferred Planning Notes

Detailed slice planning is deferred until Arc 02 closes.

Expected analysis themes:

- Expected load paths and minimum useful load sets.
- Standalone component use cases.
- Composition use cases involving two or more components.
- Human-reader versus LLM-reader ergonomics.
- Source tree versus packaged zip behavior.
- Naming/discovery problems.
- Inefficiencies caused by the current monolithic entry point.
- Functional goals not yet served by any current document.

## Version History

### v1.0 - 2026-08-29

Placeholder opened with dependency on Arc 02.
