# Project 03: Concept Card Method

## Project Ledger

Definition of done: the v3.2 concept-card methodology is assessed as the
source baseline, and a v4.0 concept-card method is planned as a repo knowledge
skill that supports concept extraction, ontology critique, provenance-bearing
memory consolidation, and CCDP-compatible evidence grading.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| P-1 | Arc 01 closes with a Project02 boundary aid accepted as input to Project02 Arc02 | `test -f arc01-method-positioning/closing-report.md && rg -n "Composition verdict: delivered|Project02 Arc02" arc01-method-positioning/closing-report.md` | serious | project-plan | done | Attested by pointer to `arc01-method-positioning/closing-report.md`; spot-checked during Project03 Arc01 close on 2026-08-30. | Child-arc closure evidence. |
| P-2 | Arc 02 closes with a source-backed inventory and gap analysis of the v3.2 baseline docs for the v4.0 method | `test -f arc02-method-inventory/closing-report.md && rg -n "Composition verdict: delivered|v3.2 baseline|v4.0|gap analysis" arc02-method-inventory/closing-report.md` | serious | project-plan | open | | |
| P-3 | Arc 03 closes with an accepted v4.0 conceptual model for cards, claims, evidence, relations, CQs, extraction runs, and memory admission | `test -f arc03-conceptual-model/closing-report.md && rg -n "Composition verdict: delivered|v4.0|concept card|evidence grade|memory admission" arc03-conceptual-model/closing-report.md` | serious | project-plan | open | | |
| P-4 | Arc 04 closes with an accepted v4.0 skill architecture and package shape | `test -f arc04-skill-architecture/closing-report.md && rg -n "Composition verdict: delivered|v4.0|SKILL.md|guides|templates|package" arc04-skill-architecture/closing-report.md` | serious | project-plan | open | | |
| P-5 | Arc 05 closes with an implementation plan covering source edits, README, Makefile/package updates, and validation gates | `test -f arc05-implementation-plan/closing-report.md && rg -n "Composition verdict: delivered|README|Makefile|check-package-paths|check-skills" arc05-implementation-plan/closing-report.md` | correctness-grade | project-plan | open | | |
| P-6 | Project03 planning keeps source edits out of scope until an accepted implementation plan exists | `rg -n "Out of scope until an accepted implementation plan|Editing source" project-plan.md arc*/arc-plan.md` | serious | operator constraint | open | | |

## Closure

Project remains open.
