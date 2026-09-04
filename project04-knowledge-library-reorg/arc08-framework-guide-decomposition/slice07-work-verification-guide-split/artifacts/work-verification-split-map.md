# Work-Verification Split Map

## Source Commit

Source commit:
`2a092d76090387a12e34d08e895084ee5389dbb2`

## Accepted Guide Set

The five accepted numbered guides now exist:

- `knowledge/work-verification/guides/01-ledger-discipline.md`
- `knowledge/work-verification/guides/02-evidence-strength.md`
- `knowledge/work-verification/guides/03-row-closure.md`
- `knowledge/work-verification/guides/04-silent-drop-checks.md`
- `knowledge/work-verification/guides/05-independent-verification.md`

## Semantic Mapping

| New guide | Source material preserved | Independent load reason |
|---|---|---|
| `01-ledger-discipline.md` | Overview, invariant spine, ledger format, rules, scale adaptation, slice/arc/project recomposition. | Start any ledgered project, arc, or slice without loading copyable templates. |
| `02-evidence-strength.md` | Asserted/attested/reproduced/reconciled vocabulary, proposed-done distinction, package evidence boundary. | Decide whether evidence is only doer-attested or independently reproduced/reconciled. |
| `03-row-closure.md` | Final statuses, CC close protocol, CDC row review, close-report shape, copyable-template route. | Update ledgers, write close reports, or verify row dispositions. |
| `04-silent-drop-checks.md` | Silent drop, spec-softening, partial adoption, vacuous checks, compliance theatre, inherited composition, wrong-scale iteration. | Compare scope-as-specified against scope-as-delivered and find missing/weakened rows. |
| `05-independent-verification.md` | Closer/verifier separation, CDC review, higher-scale gate review, sandbox/approval caveats, known limits. | Assign or perform independent verification, including CDC/fresh-context/operator review. |

## Semantic Preservation

The split is not heading-only. Each guide carries enough standalone context to
be useful in its narrow load moment:

- `01-ledger-discipline.md` defines the ledger format, rules, and all three
  scales.
- `02-evidence-strength.md` defines `asserted`, `attested`, `reproduced`, and
  `reconciled`, including the closure threshold and package/release evidence
  implications.
- `03-row-closure.md` preserves the final statuses, CC and CDC row protocols,
  close-report requirements, artifact inventory, and higher-scale row classes.
- `04-silent-drop-checks.md` preserves the anti-drop failure modes and turns
  them into a direct scope-diff checklist.
- `05-independent-verification.md` preserves the structural separation rule,
  same-surface mitigation, CDC slice review, higher-scale gate review, and
  sandbox/approval caveat.

The retained `templates/LEDGER-DISCIPLINE.md` remains the complete protocol
and copyable table source. It now cross-routes to the focused guide set.

## Selective Loading

The new entrypoint route supports selective loading:

- start with `01-ledger-discipline.md` for any ledgered unit;
- load `02-evidence-strength.md` when evidence strength is contested;
- load `03-row-closure.md` when closing or verifying rows;
- load `04-silent-drop-checks.md` when doing scope-diff review;
- load `05-independent-verification.md` when performing CDC or gate review;
- load `templates/LEDGER-DISCIPLINE.md` only when the full protocol or
  copyable table material is needed.
