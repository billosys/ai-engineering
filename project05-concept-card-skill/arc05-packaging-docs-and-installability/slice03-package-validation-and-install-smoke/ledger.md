# Slice03 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S3-1 | Package-path validation covers both new skills. | Run `make check-package-paths`; inspect output for hard failures and warnings relevant to `document-extraction.zip` and `concept-cards.zip`. | serious | arc plan | open | | Accepted warnings must be named, not hand-waved. |
| S3-2 | Generated packages contain the documented support shape after package-path validation rebuilds them. | Inspect `target/skills/document-extraction.zip` and `target/skills/concept-cards.zip` for entrypoint, sibling `version-history.md`, `guides/`, `templates/`, `examples/`, and `concept-cards/references/`. | serious | Slice01/Slice02 | open | | |
| S3-3 | Isolated install smoke proves both skills unpack into an install destination. | Run `INSTALL_DIR=<temp> make install`; inspect installed `document-extraction/` and `concept-cards/` directories. | serious | project DoD | open | | Use an isolated temporary directory, not the operator's live skill install. |
| S3-4 | Installed contents match public docs and package claims. | Compare installed trees against README, `docs/skill-library.md`, `docs/building-and-installing.md`, and `docs/knowledge-library-anatomy.md` package/support-directory claims. | correctness-grade | docs/package reconciliation | open | | |
| S3-5 | Package-local Markdown links for the two new skills are validated or explicitly dispositioned. | Use `make check-package-paths` output plus targeted archive/source inspection for `document-extraction` and `concept-cards` package-local links. | serious | repository gate | open | | |
| S3-6 | Package/install work preserves runtime and old-root exclusions. | Inspect source diff and public docs for no executable validators, JSON Schema, runtime services, live-corpus extraction, graph/ontology databases, GraphRAG, CCDP services, memory runtime work, `knowledge/concept-card-method/`, or `knowledge/source-preparation/`. | serious | project boundary | open | | |
| S3-7 | Arc06 closure inputs are explicit. | Record any remaining project-level gates, accepted package warnings, no-op/deferred items, and final validation evidence needed by Arc06. | serious | project close handoff | open | | |
| S3-8 | Focused validation and repository hygiene pass. | Run `make check-skills`, `make check-skill-versions`, `make -s print-skill-zips`, `git diff --check`, and status checks. | serious | repository gate | open | | |

Rows: 8. Open: 8. Done: 0. Deferred: 0. No-op: 0.
