# Exception Diff Scope

Implementation change:

- `package-path-exceptions.tsv` only.
- Five rows changed from `transitional-warning` with `expires=after-arc02` to ordinary `warning` rows with concrete later-maintenance expiry labels.
- No row was promoted to `explicit-exception`.
- No package-wide, class-wide, or document-wide suppression was added.
- Existing target patterns were preserved and remain limited to the affected packages/documents/target families.

No checker code, mature guide prose, staging transform, package target, or URL
policy changed in this slice.
