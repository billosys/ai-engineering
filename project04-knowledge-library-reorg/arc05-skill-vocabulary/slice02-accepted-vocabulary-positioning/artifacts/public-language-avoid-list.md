# public language avoid-list

## Purpose

This public language avoid-list records prohibited and risky claims for
README/docs/SKILL implementation. Slice03 should use it as a source-edit check.

## Prohibited Claims

| Prohibited or risky claims | Reason | Safer wording |
|---|---|---|
| "atomic means domain" or "Atomic means domain skill." | Collapses topology into kind. | Atomic means one bounded load reason; Rust is an example, not the rule. |
| "composite means framework" or "Composite means framework skill." | Collapses topology into kind. | Composite means composition is identity-defining; collaboration-framework is an example. |
| "method skills are composite" | Overclaims the method kind. | A method skill may be atomic or composite depending on its load reason and components. |
| "CCDP is a skill" | Contradicts current package behavior. | CCDP is a protocol distribution / protocol package. |
| "concept-card-method is available" | Overclaims planned Project03 work. | concept-card-method is a planned method skill until source and package support exist. |
| "source-root/package-root equivalence" | Current package behavior disproves this. | Source roots can be larger than package roots; package roots follow package behavior. |
| "`collaboration-framework` is deprecated" | Contradicts accepted Project02/Arc01 evidence. | collaboration-framework remains the top-level daily-driver composer. |
| "all knowledge lives in docs" | Contradicts Project04 boundary. | docs/ explains; knowledge/ stores source and derived substrate. |
| "all framework material is documentation" | Contradicts Arc03 source layout. | Framework material can be skill/source substrate under knowledge/. |
| "CCDP package is installed by make install" | Contradicts current Makefile behavior. | Use CCDP-specific package targets. |

## Risky Claims Requiring Caveats

- "domain/tooling skill" is accepted public vocabulary, but README may use
  "programming and tooling skill packages" for concise orientation.
- "framework/operational skill" is accepted, but a public page can often use
  "collaboration framework" or named component wording instead.
- "method skill" is accepted, but current examples must be marked planned if
  they are not live source.
- "bridge/integration layer" and "application/task bundle" are maintainer-
  facing unless a public edge-case explanation needs them.
- Metadata category values are current package metadata, not necessarily the
  accepted public skill-kind taxonomy.

## Slice03 Check

Slice03 should scan source wording for prohibited and risky claims before
committing. The expected safe output is not necessarily zero matches; the
check should inspect context and verify that any match appears only as an
avoid-list quote, caveat, or explicit "not this" explanation.
