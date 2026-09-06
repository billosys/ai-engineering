# Fixtures

Audit orientation is documented in `docs/audit-readiness.md`.

`tests/fixtures/valid/` contains accepted tiny-language programs.
`tests/fixtures/expected/` contains exact deterministic C++ stdout for valid
fixtures. `tests/fixtures/invalid/` contains rejected programs named by the
diagnostic behavior they exercise.

The CLI integration tests run fixture files through the binary instead of
duplicating long source strings. Generated C++ examples remain in `examples/`.
