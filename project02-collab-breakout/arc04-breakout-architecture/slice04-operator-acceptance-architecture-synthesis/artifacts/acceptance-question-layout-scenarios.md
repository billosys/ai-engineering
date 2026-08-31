# Acceptance Question Layout Scenarios

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice04-operator-acceptance-architecture-synthesis
status: supplemental-review-aid
operator-acceptance: pending
source-files-edited: false
```

## Purpose

This supplemental review aid expands AQ-01 through AQ-12 from
`operator-acceptance-packet.md` into filesystem-layout scenarios. The layouts
are intentionally conceptual. They are not accepted architecture, not Arc05
implementation instructions, and not source edits.

The examples show likely package/source shapes implied by each answer. Exact
source paths, package paths, Makefile targets, and generated zip contents
remain non-final until operator acceptance is recorded and Arc05 plans the
implementation work.

## Independence Notes

The acceptance questions are not fully independent.

Core spine choices:

- AQ-01 posture, AQ-02 methodology, and AQ-05 composer determine the top-level
  routing and dependency order.
- AQ-11 package/release gates constrain every accepted component path.

Mostly local component-boundary choices:

- AQ-03 project management, AQ-04 ledger, AQ-07 coverage, AQ-08 audit/coverage,
  and AQ-09 contribution can be decided mostly on their own, but their package
  layouts still inherit AQ-05 and AQ-11.

Cross-cutting placement choices:

- AQ-06 adapters, AQ-10 maintenance, and AQ-12 ontology critique affect many
  component entrypoints without necessarily creating their own packages.

## AQ-01: Collaborative Posture And Ethics

Question: accept `collaborative-posture-and-ethics` as a standalone component
plus dependency edge, with compact composer summary?

Default scenario: standalone posture component plus compact composer summary.

```text
collaboration-framework/
  SKILL.md                  # compact safety floor and route table
  guides/
    collaboration-floor.md  # short summary; routes to posture component

collaborative-posture-and-ethics/
  SKILL.md                  # direct-load posture/ethics entrypoint
  guides/
    posture-and-ethics.md   # derived from AI-CONSTITUTION-SUPPLEMENT.md
    structural-pulls.md
    collaborative-rights.md
```

Alternative scenario: composer-only posture.

```text
collaboration-framework/
  SKILL.md
  guides/
    posture-and-ethics.md
    structural-pulls.md
    collaborative-rights.md
```

Alternative scenario: methodology-owned posture.

```text
collaboration-framework/
  SKILL.md                  # routes to methodology for posture/process

engineering-methodology-and-process/
  SKILL.md
  guides/
    posture-and-ethics.md
    engineering-methodology.md
    process-rigour.md
```

Structural effect: AQ-01 is dependency-bearing. If posture is not standalone,
AQ-02 and AQ-05 must absorb more introductory safety-floor material.

## AQ-02: Engineering Methodology And Process

Question: accept `engineering-methodology-and-process` as the process
component/router rather than the owner of all operational practices?

Default scenario: methodology as process router.

```text
engineering-methodology-and-process/
  SKILL.md                    # direct-load process entrypoint/router
  guides/
    engineering-methodology.md
    knowledge-substrate.md
    process-rigour.md
    operational-routing.md    # routes to PM, ledger, audit, coverage, etc.

project-management/
ledger-verification-protocol/
code-audit-discipline/
coverage-hardening-discipline/
delegation-policy/
contribution-style-and-voice/
```

Alternative scenario: methodology monolith.

```text
engineering-methodology-and-process/
  SKILL.md
  guides/
    engineering-methodology.md
    project-management.md
    ledger-discipline.md
    code-audit.md
    coverage-hardening.md
    delegation-policy.md
    contribution-style.md
  templates/
    LEDGER-DISCIPLINE.md
    CONTRIBUTION-TICKET.md
```

Alternative scenario: link-only methodology.

```text
engineering-methodology-and-process/
  SKILL.md                  # route table only; no substantial guide body
```

Structural effect: AQ-02 interacts strongly with AQ-03, AQ-04, AQ-07, AQ-08,
and AQ-09. The default keeps methodology from re-owning every operational
discipline.

## AQ-03: Project Management

Question: accept `project-management` as one component family with PM
wayfinder, PM examples, provenance/version notes, and anti-pattern support?

Default scenario: PM as one component family.

```text
project-management/
  SKILL.md
  guides/
    PROJECT-MANAGEMENT.md      # PM wayfinder
    pm/
      01-scales-of-work.md
      02-canonical-planning-worktree.md
      03-planning-top-down.md
      04-closing-slices.md
      05-closing-arcs.md
      06-confirmation-protocol.md
      07-anti-patterns.md
      08-maintenance.md
      09-worked-example-odm.md
      version-history.md
  examples/
    worked-example-odm.md
```

Alternative scenario: each PM guide becomes a package.

```text
project-management/
  SKILL.md                    # index/wayfinder only

pm-scales-of-work/
  SKILL.md
  guides/scales-of-work.md

pm-planning-worktree/
  SKILL.md
  guides/canonical-planning-worktree.md

pm-planning-top-down/
  SKILL.md
  guides/planning-top-down.md

pm-closing-slices/
  SKILL.md
  guides/closing-slices.md

pm-closing-arcs/
  SKILL.md
  guides/closing-arcs.md

pm-confirmation-protocol/
pm-anti-patterns/
pm-maintenance/
```

Structural effect: AQ-03 is mostly local, but it depends on AQ-04 because PM
close mechanics cite ledger evidence. Splitting PM into many packages creates
extra load decisions and more package-link surface.

## AQ-04: Ledger Verification Protocol

Question: accept `ledger-verification-protocol` as the evidence owner while PM
owns lifecycle mechanics?

Default scenario: ledger as direct-load evidence component.

```text
ledger-verification-protocol/
  SKILL.md
  guides/
    ledger-discipline.md
    evidence-strength.md
    row-closure.md
    silent-drop-checks.md
  templates/
    LEDGER-DISCIPLINE.md

project-management/
  SKILL.md                    # depends on ledger for close evidence
  guides/
    pm/04-closing-slices.md   # cites ledger-verification-protocol
    pm/05-closing-arcs.md
```

Alternative scenario: ledger as PM appendix.

```text
project-management/
  SKILL.md
  guides/
    PROJECT-MANAGEMENT.md
    pm/
      04-closing-slices.md
      05-closing-arcs.md
    ledger-discipline.md
  templates/
    LEDGER-DISCIPLINE.md
```

Alternative scenario: evidence vocabulary spread across components.

```text
engineering-methodology-and-process/
  guides/evidence-strength.md

project-management/
  guides/row-closure.md

code-audit-discipline/
  guides/audit-evidence.md

coverage-hardening-discipline/
  guides/coverage-evidence.md
```

Structural effect: AQ-04 touches PM, audit, coverage, and methodology. The
default creates a single evidence owner and reduces duplicate vocabulary.

## AQ-05: Top-Level Collaboration Framework Composer

Question: accept `collaboration-framework` as the top-level composer with
compact posture/process floor and route table?

Default scenario: compact but substantive composer.

```text
collaboration-framework/
  SKILL.md                    # broad session-start entrypoint
  guides/
    collaboration-floor.md    # compact posture/process floor
    component-route-table.md
    repository-orientation.md
  adapters/
    agent-role-language.md
```

Alternative scenario: keep current monolith.

```text
collaboration-framework/
  SKILL.md
  guides/
    ai-constitution-supplement.md
    ai-engineering-methodology.md
    project-management.md
    ledger-discipline.md
    code-audit.md
    coverage-hardening.md
    subagent-delegation-policy.md
    contribution-style.md
  templates/
    CONTRIBUTION-TICKET.md
    LEDGER-DISCIPLINE.md
```

Alternative scenario: link-only index.

```text
collaboration-framework/
  SKILL.md                    # route table only
```

Alternative scenario: remove composer.

```text
collaborative-posture-and-ethics/
engineering-methodology-and-process/
ledger-verification-protocol/
project-management/
code-audit-discipline/
coverage-hardening-discipline/
delegation-policy/
contribution-style-and-voice/
```

Structural effect: AQ-05 is a spine decision. It determines whether broad
session start still has a single stable entrypoint.

## AQ-06: Agent Adapter And Routing

Question: accept central plus local notes for the agent adapter and defer
standalone `agent-adapter-and-routing` package status?

Default scenario: central adapter plus local notes.

```text
collaboration-framework/
  SKILL.md
  adapters/
    agent-role-language.md      # CC/CDC/Codex/Claude translation

project-management/
  SKILL.md
  guides/
    local-agent-note.md

delegation-policy/
  SKILL.md
  guides/
    local-agent-note.md

code-audit-discipline/
coverage-hardening-discipline/
contribution-style-and-voice/
  guides/
    local-agent-note.md         # only where role language affects use
```

Alternative scenario: central-only adapter.

```text
collaboration-framework/
  adapters/
    agent-role-language.md

project-management/
ledger-verification-protocol/
code-audit-discipline/
coverage-hardening-discipline/
delegation-policy/
contribution-style-and-voice/
  SKILL.md                      # all rely on cross-package adapter route
```

Alternative scenario: local-only adapter notes.

```text
project-management/guides/local-agent-note.md
ledger-verification-protocol/guides/local-agent-note.md
code-audit-discipline/guides/local-agent-note.md
coverage-hardening-discipline/guides/local-agent-note.md
delegation-policy/guides/local-agent-note.md
contribution-style-and-voice/guides/local-agent-note.md
```

Alternative scenario: standalone adapter package now.

```text
agent-adapter-and-routing/
  SKILL.md
  guides/
    agent-role-language.md
    codex-desktop-routing.md
    codex-cli-routing.md
    legacy-claude-language.md

collaboration-framework/
project-management/
ledger-verification-protocol/
  SKILL.md                      # depend on adapter package
```

Structural effect: AQ-06 is cross-cutting. It can change every entrypoint's
introductory text even if no new package is created.

## AQ-07: Coverage Hardening

Question: accept `coverage-hardening-discipline` with compatibility treatment
for the historical `CLAUDE-CODE-COVERAGE.md` surface?

Default scenario: coverage component plus compatibility route.

```text
coverage-hardening-discipline/
  SKILL.md
  guides/
    coverage-hardening.md       # derived from CLAUDE-CODE-COVERAGE.md
    compatibility.md            # old name and route explained
    validation-gates.md
```

Alternative scenario: hard rename without compatibility.

```text
coverage-hardening-discipline/
  SKILL.md
  guides/
    coverage-hardening.md
```

Alternative scenario: merge coverage into audit.

```text
code-audit-discipline/
  SKILL.md
  guides/
    code-audit.md
    coverage-hardening.md
    audit-to-hardening-handoff.md
```

Structural effect: AQ-07 is local unless merged into audit. The default
preserves history while giving coverage a direct-load package.

## AQ-08: Audit And Coverage Relationship

Question: accept audit and coverage as sibling operational components, with
audit remaining diagnosis-only?

Default scenario: sibling components with audit diagnosis-only.

```text
code-audit-discipline/
  SKILL.md
  guides/
    code-audit.md
    findings-format.md
    modernization-synthesis.md

coverage-hardening-discipline/
  SKILL.md
  guides/
    coverage-hardening.md
    validation-gates.md
```

Alternative scenario: broad quality wrapper.

```text
quality-discipline/
  SKILL.md
  guides/
    code-audit.md
    coverage-hardening.md
    verification.md
    audit-to-hardening-handoff.md
```

Alternative scenario: merged audit/coverage ownership under audit.

```text
code-audit-discipline/
  SKILL.md
  guides/
    code-audit.md
    coverage-hardening.md
    remediation-loop.md
```

Structural effect: AQ-08 interacts with AQ-07. The default keeps diagnosis and
implementation hardening separate, which reduces accidental audit scope creep.

## AQ-09: Contribution Style And Ticket Template

Question: accept `contribution-style-and-voice` with
`CONTRIBUTION-TICKET.md` as a package-local support asset?

Default scenario: contribution component plus package-local template.

```text
contribution-style-and-voice/
  SKILL.md
  guides/
    contribution-style.md
    upstream-ticket-workflow.md
  templates/
    CONTRIBUTION-TICKET.md
```

Alternative scenario: template-only package.

```text
contribution-ticket-template/
  SKILL.md
  templates/
    CONTRIBUTION-TICKET.md
```

Alternative scenario: guide without bundled template.

```text
contribution-style-and-voice/
  SKILL.md
  guides/
    contribution-style.md
    upstream-ticket-workflow.md
```

Structural effect: AQ-09 is mostly local. The default keeps voice, workflow,
and the reusable ticket shape together.

## AQ-10: Maintenance And Version History

Question: accept maintenance owner and version-history responsibility as
mandatory component contract fields, while deferring standalone maintenance
component status?

Default scenario: maintenance fields embedded in every component contract.

```text
collaboration-framework/SKILL.md
collaborative-posture-and-ethics/SKILL.md
engineering-methodology-and-process/SKILL.md
ledger-verification-protocol/SKILL.md
project-management/SKILL.md
code-audit-discipline/SKILL.md
coverage-hardening-discipline/SKILL.md
delegation-policy/SKILL.md
contribution-style-and-voice/SKILL.md
  # each entrypoint carries maintenance owner and version-history duty
```

Alternative scenario: no explicit owner field.

```text
collaboration-framework/
collaborative-posture-and-ethics/
engineering-methodology-and-process/
ledger-verification-protocol/
project-management/
code-audit-discipline/
coverage-hardening-discipline/
delegation-policy/
contribution-style-and-voice/
  # no common maintenance metadata requirement
```

Alternative scenario: standalone maintenance package now.

```text
component-maintenance-discipline/
  SKILL.md
  guides/
    maintenance-owners.md
    version-history.md
    package-surface-synchronization.md

collaboration-framework/
project-management/
ledger-verification-protocol/
  SKILL.md                      # depend on maintenance package
```

Structural effect: AQ-10 is cross-cutting. It does not necessarily create a
package, but it changes the contract for every accepted package.

## AQ-11: Source/Package And Release Gates

Question: accept the source/package and release gate strategy, including
README, `SKILL.md`, Makefile, package list, generated zip, validation, and
CCDP separation fields?

Default scenario: gate-first package/release strategy.

```text
README.md                       # source-clone and package-reader routes
SKILL.md                        # top-level composer source entrypoint
Makefile                        # package targets and zip lists
package-path-exceptions.tsv     # only justified exceptions

collaboration-framework/
collaborative-posture-and-ethics/
engineering-methodology-and-process/
ledger-verification-protocol/
project-management/
code-audit-discipline/
coverage-hardening-discipline/
delegation-policy/
contribution-style-and-voice/
  SKILL.md
  guides/

protocols/ccdp/                 # separate protocol distribution
ccdp.zip                        # separate package surface
```

Alternative scenario: pick package paths first and repair gates later.

```text
collaboration-framework/
collaborative-posture-and-ethics/
engineering-methodology-and-process/
ledger-verification-protocol/
project-management/
code-audit-discipline/
coverage-hardening-discipline/
delegation-policy/
contribution-style-and-voice/
  # paths chosen before README/Makefile/package-link gates are reconciled
```

Alternative scenario: prose-only gates.

```text
README.md
SKILL.md
component-packages/
  # package expectations documented in prose but not tied to validation rows
```

Alternative scenario: CCDP bundled into skill packages.

```text
collaboration-framework/
  SKILL.md
  protocols/
    ccdp/

ccdp/
  # duplicated or ambiguous package ownership
```

Structural effect: AQ-11 constrains every other AQ. The default prevents
source/package path drift and keeps CCDP separate from skill packages.

## AQ-12: Ontology Critique

Question: accept ontology critique as a deferred non-component and method
evidence, not a package now?

Default scenario: ontology critique remains deferred method evidence.

```text
project02-collab-breakout/
  arc02-conceptual-analysis/
    slice03-ontology-decision-synthesis/
      artifacts/
        arc02-conceptual-model.md
        boundary-and-naming-findings.md
  arc04-breakout-architecture/
    slice04-operator-acceptance-architecture-synthesis/
      artifacts/
        decision-risk-disposition-record.md

collaboration-framework/
engineering-methodology-and-process/
  SKILL.md                      # may cite method evidence, not own package
```

Alternative scenario: package ontology critique now.

```text
ontology-critique-and-boundary-analysis/
  SKILL.md
  guides/
    ontology-critique.md
    component-boundary-analysis.md
    merge-split-diagnostics.md
```

Alternative scenario: drop the concern.

```text
collaboration-framework/
engineering-methodology-and-process/
project-management/
ledger-verification-protocol/
  # no visible ontology critique component, package, or re-entry trail
```

Structural effect: AQ-12 is a deferral decision. The default preserves the
evidence trail and re-entry condition without promoting a package before there
is direct-load evidence.

## All-Defaults Composite View

If AQ-01 through AQ-12 all take their recommended defaults, the resulting
conceptual package/source layout is expected to converge toward this shape:

```text
collaboration-framework/
  SKILL.md
  guides/
    collaboration-floor.md
    component-route-table.md
    repository-orientation.md
  adapters/
    agent-role-language.md

collaborative-posture-and-ethics/
  SKILL.md
  guides/
    posture-and-ethics.md
    structural-pulls.md
    collaborative-rights.md

engineering-methodology-and-process/
  SKILL.md
  guides/
    engineering-methodology.md
    knowledge-substrate.md
    process-rigour.md
    operational-routing.md

ledger-verification-protocol/
  SKILL.md
  guides/
    ledger-discipline.md
    evidence-strength.md
    row-closure.md
    silent-drop-checks.md
  templates/
    LEDGER-DISCIPLINE.md

project-management/
  SKILL.md
  guides/
    PROJECT-MANAGEMENT.md
    pm/
      01-scales-of-work.md
      02-canonical-planning-worktree.md
      03-planning-top-down.md
      04-closing-slices.md
      05-closing-arcs.md
      06-confirmation-protocol.md
      07-anti-patterns.md
      08-maintenance.md
      09-worked-example-odm.md
      version-history.md
  examples/
    worked-example-odm.md

code-audit-discipline/
  SKILL.md
  guides/
    code-audit.md
    findings-format.md
    modernization-synthesis.md

coverage-hardening-discipline/
  SKILL.md
  guides/
    coverage-hardening.md
    compatibility.md
    validation-gates.md

delegation-policy/
  SKILL.md
  guides/
    subagent-delegation-policy.md
    local-agent-note.md

contribution-style-and-voice/
  SKILL.md
  guides/
    contribution-style.md
    upstream-ticket-workflow.md
  templates/
    CONTRIBUTION-TICKET.md
```

Non-package rows under the all-defaults scenario:

```text
agent-adapter-and-routing              # central adapter plus local notes
repository-orientation-and-distribution # adapter/constraint, not package
verification-methodology               # dependency edge/non-component
ontology-critique                      # deferred non-component
component-maintenance-discipline        # mandatory fields, not package
evidence-strength-memory-admission      # non-component/deferred evidence row
CCDP                                   # separate protocol distribution
```
