---
name: laboratory-recordkeeping
description: |
  Organize and preserve laboratory notebooks, experiment records, runs, and
  research collections. Use when establishing a lab repository, recording
  exploratory or experimental work, handling unexpected artifacts, preserving
  provenance, or preparing results for reconstruction and reuse. Complements
  scientific-methods, which owns inquiry design and evidence interpretation.
license: MIT
metadata:
  version: "0.1.0"
  hermes:
    tags: [laboratory, notebooks, recordkeeping, provenance, preservation]
    category: method-skills
---

# Laboratory Recordkeeping

Keep research understandable beyond the session that produced it. Preserve
the question, the work actually performed, the observations, and the path
from those observations to a conclusion. Future readers should be able to
inspect results, reconstruct the work, challenge the interpretation, and see
what remains unexamined.

Use this skill for both active notebooks and retained research collections.
It supports exploratory work, controlled experiments, replications, symbolic
derivations, numerical studies, and equipment or software commissioning.

## Boundaries

- **This skill:** record organization, identity, chronology, provenance,
  storage, corrections, retention, and navigation.
- **Scientific-methods:** questions, controls, measures, protocols, comparisons,
  interpretation, and threats to validity. Load that skill when designing or
  evaluating an inquiry; its [source entrypoint](https://github.com/billosys/ai-engineering/blob/main/knowledge/scientific-methods/SKILL.md)
  and [protocol template](https://github.com/billosys/ai-engineering/blob/main/knowledge/scientific-methods/templates/experiment-protocol.md)
  are available separately.
- **Collaboration-framework:** engineering commitments, implementation handoffs,
  and independent acceptance when the work uses that framework. A research
  record does not replace an existing plan or acceptance gate.
- **Repository conventions:** the repository selects its root, naming profile,
  custodians, and storage arrangements. Preserve established layouts unless
  the user authorizes a migration.

## Start here

Read the repository instructions and nearest index before creating records.
For a new collection, read guides 01–03. For an existing session, load the
guide matching the action below. Apply the smallest record set that preserves
meaning; a useful notebook entry does not require an experiment directory.

| Action | Guide |
| --- | --- |
| Define a collection and its responsibilities | [Collections and stewardship](./guides/01-collections-and-stewardship.md) |
| Choose names, scopes, and entrypoints | [Layout and identifiers](./guides/02-layout-and-identifiers.md) |
| Decide what to create or handle an unexpected file | [Creation and routing](./guides/03-creation-and-routing.md) |
| Record thinking, observations, and corrections | [Journals and notebooks](./guides/04-journals-and-notebooks.md) |
| Prepare, execute, and finish an attempt | [Run records](./guides/05-run-records.md) |
| Preserve inputs, native files, and external evidence | [Storage and preservation](./guides/06-storage-and-preservation.md) |
| Publish a finding or revisit someone else's work | [Reports and reconstruction](./guides/07-reports-and-reconstruction.md) |

## Essential practice

Give each attempt a stable identity. Record what actually happened, including
failures, deviations, interruptions, and missing evidence. Keep source inputs
and raw observations distinguishable from transformations and interpretation.
Never replace an earlier observation with a later result under the same name.

Link findings to analysis, analysis to attempts, and attempts to the exact
inputs, method, code, configuration, and environment used. A link or checksum
helps locate or identify evidence; neither proves that an experiment ran or
that its conclusion is correct.

For LLM-assisted work, inspect required linked files using the available tools.
Record unresolved access rather than inferring their contents from filenames.
When file access itself is being evaluated, retain tool calls, returned
contents, and behavior that depends on those contents.

## Reusable material

- [Lab entrypoint](./templates/lab-readme.md)
- [Experiment entrypoint](./templates/experiment-readme.md)
- [Journal entry](./templates/journal-entry.md)
- [Run record](./templates/run-record.md)
- [Evidence inventory](./templates/evidence-inventory.md)
- [Report](./templates/report.md)
- [Worked routing examples](./examples/recordkeeping-decisions.md)
- [Sources and adaptations](./references/sources-and-adaptations.md)
- [Version history](./version-history.md)

Templates are starting points. Remove irrelevant optional fields; state why a
material field is unknown or inapplicable. Do not fill gaps with invented facts.
