# Framework 0.4.1 / Pre-0.5.0 A/B Experiment

Preserved on 2026-09-05 under Project04 at the operator's request.

This archive contains the prompts, planning, Rust implementations, fixtures,
generated C++ examples, verification records, read-only audits, project close
reports and assessments from the framework comparison. Both experimental
projects completed their scoped implementation-and-audit work. Audit findings
were deliberately left unrepaired as evidence.

## Start Here

- [Final framework regression assessment](B/lykn-cpp-transpiler-trial/final-framework-regression-assessment.md)
  compares the completed projects and audits, records the
  `main-slightly-improved` verdict and preserves the limitations and misses.
- [Arc01 comparison](B/lykn-cpp-transpiler-trial/arc01-framework-comparison.md)
  captures the first planning/implementation checkpoint.
- [Post-Arc02 comparison](B/lykn-cpp-transpiler-trial/phase2a-post-arc02-framework-comparison.md)
  captures the next checkpoint, including different slice allocation and the
  limits of comparing arc numbers rather than equivalent capability.
- [Shared read-only self-audit prompt](B/lykn-cpp-transpiler-trial/read-only-self-audit-prompt.md)
  and [assessor rubric](B/lykn-cpp-transpiler-trial/read-only-self-audit-assessment-rubric.md)
  define the final audit phase and assessment expectations.
- [Article source notes](B/lykn-cpp-transpiler-trial/article-source-notes.md)
  connect this evidence to the draft Billo article, including the later syntax
  examples. The article itself remains in the website repository.

The shared assessment and editorial files remain under B because that is where
they were originally written. Their location does not make them B's self-audit
or evidence from a blind assessor.

## Conditions

A and B are archive labels assigned at preservation time; the original run
labels inside the evidence are unchanged.

| | A | B |
| --- | --- | --- |
| Framework | 0.4.1 baseline | main / pre-0.5.0 candidate |
| Original run label | `framework-0.4.1` | `framework-main-pre-0.5.0` |
| Framework checkout HEAD at preservation | `306dfb69d6b893e8928e57d65f8c886afb5474a6` | `9d8bbe2f95ceff7fc90acfb8c45c3f3a52c7a2f0` |
| Initial prompt | [cdc-project-prompt.md](A/cdc-project-prompt.md) | [cdc-project-prompt.md](B/cdc-project-prompt.md) |
| Complete trial directory | [A trial](A/lykn-cpp-transpiler-trial/) | [B trial](B/lykn-cpp-transpiler-trial/) |
| Project plan | [A plan](A/lykn-cpp-transpiler-trial/project-plan.md) | [B plan](B/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md) |
| Project closing report | [A close](A/lykn-cpp-transpiler-trial/closing-report.md) | [B close](B/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/closing-report.md) |
| Rust self-audit | [A audit](A/lykn-cpp-transpiler-trial/rust-self-audit-report.md) | [B audit](B/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/rust-self-audit-report.md) |
| Rust crate | [A Cargo.toml](A/lykn-cpp-transpiler-trial/Cargo.toml) | [B Cargo.toml](B/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/Cargo.toml) |
| Fixtures | [A fixtures](A/lykn-cpp-transpiler-trial/tests/fixtures/) | [B fixtures](B/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/fixtures/) |
| Generated C++ examples | [A examples](A/lykn-cpp-transpiler-trial/examples/) | [B examples](B/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/examples/generated/) |

These hashes identify framework checkouts at preservation time, not Git
commits containing the formerly ignored trial implementations. Consult the
original prompts and reports for references actually loaded and deviations.
This archive does not newly freeze installed domain skills, Lykn reference
material, external sources or the original toolchain.

## Arc and Slice Evidence

Each linked arc retains its original plans, prompts, iterations where present,
ledgers, closing reports, verification records and supporting artifacts.

| Checkpoint | A | B |
| --- | --- | --- |
| Arc01 | [Foundation](A/lykn-cpp-transpiler-trial/arc01-foundation/) | [Minimum language core](B/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/) |
| Arc02 | [Expressions and semantics](A/lykn-cpp-transpiler-trial/arc02-expressions-and-semantics/) | [Diagnostics and negative coverage](B/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/) |
| Arc03 | [Examples and audit readiness](A/lykn-cpp-transpiler-trial/arc03-examples-and-audit-readiness/) | [CLI, examples and audit readiness](B/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/) |

The different layouts and decomposition choices are part of the evidence.
They have not been normalised to the current framework's preferred shape.

## Relocation Map

Paths below are relative to the main ai-engineering checkout. The destinations
are relative to this README.

| Original location | Archive location |
| --- | --- |
| `.worktrees/0.4.1/workbench/cdc-project-prompt.md` | `A/cdc-project-prompt.md` |
| `.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/` | `A/lykn-cpp-transpiler-trial/` |
| `workbench/cdc-project-prompt.md` | `B/cdc-project-prompt.md` |
| `workbench/lykn-cpp-transpiler-trial/` | `B/lykn-cpp-transpiler-trial/` |

The original files and directories were moved, not left as duplicate working
copies. Other workbench contents, including release notes, remain in place.

Historical absolute paths and command text inside the archived material are
preserved verbatim. Use this map to locate relocated trial artifacts. Framework
paths still refer to their original versioned checkouts. Archived prompts are
historical evidence, not new instructions to execute or authority to resume a
closed trial. Re-running commands may require path adjustments in a separate
working copy; this preservation operation does not claim a hermetic replay.

## Preservation and Verification

[preservation-manifest.json](preservation-manifest.json) records each relocation,
checkout identities, SHA-256 digests, sizes and permission modes for the 153
durable evidence files. All 3,881 regular files, including build caches, were
checked for byte and permission-mode equality before and after the move.
No trial prose, source code, test, fixture or reported finding was changed.

The two Cargo `target/` directories were moved with their workspaces and remain
available locally. The arc's [.gitignore](.gitignore) excludes them from Git;
the manifest records their aggregate inventory hashes, file counts and sizes.
They are disposable compiled output, not part of the committed evidence set.
Cargo manifests, lockfiles, source, tests and generated C++ evidence are kept
in Git. A fresh checkout will not contain the ignored build caches.

Verification for this archival operation checks preservation, completeness,
README links, former-location removal and explicit Git scope. It does not
rerun or repair the experiment or independently re-score its findings.

The default staged whitespace check reports existing blank lines at EOF in
some archived B files. Their pre/post SHA-256 checks match: these are retained
source bytes, not archival edits. The new README, ignore file, manifest and
project-plan changes pass the default check; the full archive passes with only
the `blank-at-eof` whitespace rule disabled for that check. No repository-wide
whitespace configuration was changed.

## Project04 Status and Layout Override

The operator explicitly requested an arbitrary `arc10-ab-experiment` archive
with A/B homes and a README. This is the accepted exception to the usual new
arc/slice planning packet: no retrospective CC assignment or fabricated
independent verification is introduced. The archived experimental projects
retain their own real planning and verification records.

This preservation is CDC-direct. It does not close Arc08, lift its operator
review pause, or formally close Project04. The [project plan](../project-plan.md)
records this archive in the roadmap.
