# v4.0 Verification Gate Matrix

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice05-implementation-plan-synthesis
artifact: v40-verification-gate-matrix
status: proposed-done
```

## Purpose

This verification gate matrix lists the checks a future implementation should
pass before claiming the v4.0 concept-card method skill is implemented or
release-ready. This matrix is not release evidence and does not claim release
readiness.

## Matrix

| Gate | Command or review | Applies to | Pass condition | Evidence class |
|------|-------------------|------------|----------------|----------------|
| source checkout clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | source checkout | No unintended tracked source changes outside the implementation commit boundary. | implementation hygiene |
| planning checkout hygiene | `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check` | planning checkout | No whitespace or patch hygiene defects in planning artifacts. | planning hygiene |
| skill metadata | `make check-skills` | `knowledge/concept-card-method/SKILL.md` via `ALL_SKILL_FILES` | Skill entrypoint passes repository skill-description checks. | source verification |
| package build | `make concept-card-method` | Makefile target and package list | `concept-card-method.zip` is generated from source. | package verification |
| generated zip listing | inspect `concept-card-method.zip` | generated zip | Archive contains `concept-card-method/SKILL.md` and `concept-card-method/guides/**`, including templates, examples, validation documentation, and support documents. | package verification |
| package-path check | `make check-package-paths` | generated archives | Package-context links resolve or have accepted package-path exceptions. | package verification |
| installability | `make install` and `make uninstall`, or narrower accepted install check | installed skill package | `concept-card-method/` installs under `$(INSTALL_DIR)` and uninstall removes it without touching source. | install verification |
| documentation-only validator scope | review and grep | validation documentation | Validation guidance does not claim executable validator-code; deferred validator-code is explicit. | overclaim check |
| README/library discoverability | review and grep | `README.md` and skill library text | README names reason to load, package expectation, adjacent routing, promise boundary, and verification commands. | discoverability check |
| version-history check | review and grep | changed source files | Source version-history entries exist for SKILL.md, guides, templates, examples, validation documentation, support documents, README, Makefile, and any package-path exception. | maintenance check |

## Release-Readiness Rule

Release readiness is a composition claim. A future implementation may claim
release readiness only when all applicable gates have evidence and the
evidence is consistent. A generated zip alone is not release evidence. A
clean source checkout alone is not release evidence. README/library
discoverability alone is not release evidence.

## Documentation-Only Validator Scope

The first implementation gate treats validator scope as documentation-only.
The gate can prove that the package documents deterministic structural
validation candidates, semantic audit boundaries, human/operator review
boundaries, and deferred runtime checks. It cannot prove executable
validator-code behavior because executable validator-code is deferred.

## Planning Boundary

This matrix is implementation planning. It does not edit source, does not run
future source checks, does not create generated zips, does not perform package
release, does not implement release gates, and does not claim release
readiness.

## Arc05 Composition Support

This matrix supports Arc05 composition rows A-6, A-7, A-8, and A-9 by tying
accepted Arc04 source layout and validation decisions to README, Makefile,
package list, package-path, generated zip, tests, release gates,
runtime systems deferral, and the source-edit boundary.
