---
name: work-verification
description: |
  Component framework/operational skill for ledger discipline and evidence
  strength. Use at the start of any ledgered project, arc, or slice; when
  closing work; or when distinguishing proposed-done attestation from
  independent reproduced verification.
version: 1.1.1
license: MIT
metadata:
  hermes:
    tags: [ai-engineering, ledger, verification, evidence]
    category: meta-skills
---

# Work Verification

Use this component when the unit of work has a ledger or when evidence strength
matters. It owns the closure discipline, row-by-row verification, evidence
levels, and proposed-done versus independently verified distinction.

Read only the guide needed for the work:

- [Ledger Discipline](./guides/01-ledger-discipline.md) - scale-free ledger
  format, rows, and slice/arc/project adaptation.
- [Evidence Strength](./guides/02-evidence-strength.md) - asserted,
  attested, reproduced, and reconciled evidence.
- [Row Closure](./guides/03-row-closure.md) - final statuses, row walks,
  closure evidence, and templates.
- [Silent-Drop Checks](./guides/04-silent-drop-checks.md) - missing-row,
  spec-softening, partial-adoption, and inherited-composition checks.
- [Independent Verification](./guides/05-independent-verification.md) -
  closer/verifier separation, CDC review, gate review, and sandbox caveats.

Use [LEDGER-DISCIPLINE.md](./templates/LEDGER-DISCIPLINE.md) as the retained
full protocol and copyable ledger-template support asset when a project needs
the complete pre-split text in one file.

This is a component entrypoint for the collaboration framework. It is included
inside `collaboration-framework.zip` as routed dependency material, not as a
separate installable package.

Component history lives in [version-history.md](./version-history.md).
