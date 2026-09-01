# v4.0 Release Gate Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice04-packaging-release-plan
artifact: v40-release-gate-plan
status: proposed-done
release-claim: none
```

## Purpose

This artifact plans release gates and evidence required before a future
implementation can claim release readiness for the v4.0 concept-card method
skill. It is not release evidence and not a release.

This plan does not edit source, does not create generated zips, does not
perform package release, does not claim release readiness, does not implement
executable validator-code, and does not create runtime services, GraphRAG,
graph database, ontology database, memory runtime, CCDP service, or live
extraction behavior.

## Planned Release Gate Sequence

Future implementation must pass these planned release gate checks before
claiming release readiness:

1. Source checkout cleanliness: `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet`.
2. Planning checkout hygiene: `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`.
3. Skill checks: `make check-skills` after adding
   `knowledge/concept-card-method/SKILL.md` to `ALL_SKILL_FILES`.
4. Package build: `make concept-card-method` creates
   `concept-card-method.zip`.
5. Generated zip checks: inspect `concept-card-method.zip` and confirm it
   contains `concept-card-method/SKILL.md` and
   `concept-card-method/guides/**`.
6. Package-path checks: `make check-package-paths` validates package-local
   Markdown links inside generated archives.
7. Package installability: `make install` unpacks `concept-card-method/` into
   `$(INSTALL_DIR)` and `make uninstall` removes it without touching source.
8. Documentation-only validator scope check: confirm validation guidance is
   packaged as documentation and no executable validator-code is claimed.
9. README/library discoverability check: confirm README and skill library text
   name the reason to load, package expectation, adjacent routing, and promise
   boundary.
10. Source version-history check: confirm required source version history
    entries exist for changed source surfaces.

## Release-Readiness Evidence

Evidence required before claiming release readiness:

- command transcript for `make check-skills`;
- command transcript for `make concept-card-method`;
- generated zip listing for `concept-card-method.zip`;
- command transcript for `make check-package-paths`;
- installability transcript for `make install` and `make uninstall`, or a
  documented narrower install check accepted by the implementation owner;
- source checkout clean result;
- planning checkout hygiene result;
- README/library discoverability review result;
- source version-history review result;
- documentation-only validator scope review result.

This planned release gate list is not release evidence. It describes evidence
required before claiming readiness in a future implementation. Slice04 does
not claim release readiness.

Exact overclaim boundary: evidence required before claiming release readiness
must be produced by a future implementation; this Slice04 artifact is not a
release and is not release evidence.

## Gate Boundaries

| Gate | Can prove | Cannot prove |
|------|-----------|--------------|
| `make check-skills` | SKILL.md description length and entrypoint check coverage. | Semantic method correctness, package-path correctness, or release readiness alone. |
| package build | Generated zip can be built from source. | Installability, package-local link correctness, or semantic validity. |
| generated zip checks | Archive root and expected package contents exist. | Runtime behavior, source support warrant, or memory admission correctness. |
| package-path checks | Package-context Markdown links resolve or have accepted exceptions. | Source semantic correctness, executable validator behavior, or release readiness alone. |
| installability | Package can be unpacked into the skill install directory and removed. | That every operator workflow is correct or semantically verified. |
| documentation-only validator scope | The package does not overclaim executable validator-code. | That a validator exists or that deterministic checks are executed. |

## Future Implementation Requirements

Future implementation should treat release readiness as a composition claim:
all gate evidence must be present and consistent before release readiness is
claimed. A generated zip alone is not enough. A clean source checkout alone is
not enough. README prose alone is not enough.

Generated zips remain build artifacts under the current ignore policy. Package
release requires a later owner and explicit evidence.

## Later-Slice Routing

Slice05 owns implementation-plan synthesis, implementation slice
recommendations, deferral register, source edit sequence, and Project03 close
input.

Slice04 found no release-gate, generated-artifact, or package-path fact that
requires Arc05 re-sequencing, a new slice, or a scope correction.
