# Known Extraction Gaps

Concepts referenced by existing cards' typed relationships but not yet extracted as
cards of their own. The references are kept intact (they encode real relationships);
these are candidates for a future extraction pass. Each maps to a real Erlang/OTP
topic, so they are legitimate cards-to-be, not noise.

| missing slug | referenced by | likely home (source / chapter) |
|--------------|---------------|--------------------------------|
| `bif-name-clash-resolution` | otp-reference-manual/auto-imported-bifs | Reference Manual → 01 core-idioms / 05 functions |
| `changing-a-supervisor` | otp-design-principles/synchronized-code-replacement | Design Principles (release handling) → 08 supervision |
| `expressions-in-patterns` | otp-reference-manual/patterns-in-expressions | Reference Manual → 05 functions-pattern-matching |
| `function-calls` | auto-imported-bifs, built-in-functions, function-evaluation | Reference Manual → 05 functions-pattern-matching |
| `module-dependencies` | otp-design-principles/application-upgrade-file | Design Principles (appup/relup) → 12 project-structure |
| `string-prefix-in-patterns` | otp-reference-manual/patterns-in-expressions | Reference Manual (`"prefix" ++ Rest`) → 05 functions-pattern-matching |

Resolved (were typos, now fixed):
- `binary-comprehensions` → `binary-comprehension`
- `escape-sequence` → `escape-sequences`
- `error-handling-processes` → `error-handling-between-processes`
