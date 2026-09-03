# terminology decision question register

## Purpose

This register gives Slice02 answerable questions for accepted vocabulary and
positioning. It does not answer them here.

## Skill Kind Questions

1. Should public docs use "domain/tooling skill" or retain the current README
   phrase "programming and tooling skill packages"?
2. Should "framework/operational skill" be public-facing language, or should
   README/docs describe the collaboration framework and its components more
   concretely without the kind label?
3. Should "method skill" be an accepted public category before
   `concept-card-method` exists in source?
4. Should "protocol/package" be public vocabulary, or should docs simply say
   CCDP is a separate protocol distribution?
5. Should "support/template" be public vocabulary, or should templates be
   described as support material without adding another user-facing category?
6. Should "source/provenance" remain maintainer vocabulary rather than public
   skill-library vocabulary?

## Topology Questions

1. Should "atomic skill" be used publicly in README/docs now, or held for
   maintainer docs until users need the distinction?
2. Should Rust be the public example for atomic skill, or should Arc05 avoid
   publishing examples until package behavior is revalidated after edits?
3. Should "composite skill" be public vocabulary for the
   collaboration-framework daily-driver composer?
4. Should Biome's root/package split be explained as topology, package
   behavior, or simply as a current exception?
5. Should "bridge/integration layer" be a public topology term, or reserved
   for planning and maintainer-facing classification?
6. Should "application/task bundle" be public vocabulary, or too internal for
   end-user navigation?

## Examples

1. Should examples include only current source surfaces, or may they include
   planned surfaces with explicit planned status?
2. Should the accepted examples be Rust, collaboration-framework, CCDP, Biome,
   templates/GUIDE.md, and planned concept-card-method?
3. Should concept-card-method be named in public docs only as a planned method
   surface until implementation lands?
4. Should metadata categories such as systems-programming, web-frontend,
   linting, static-sites, and meta-skills be treated as examples, replaced
   later, or left as loader metadata only?

## Avoid-List

1. Should Slice02 formally prohibit "atomic means domain skill" and
   "composite means framework skill" in public docs?
2. Should Slice02 prohibit "CCDP is a skill" except when explicitly discussing
   why it is not an installable skill package?
3. Should Slice02 prohibit "concept-card-method is available" until source and
   package support exist?
4. Should Slice02 prohibit source-root/package-root equivalence claims?
5. Should Slice02 prohibit language implying `collaboration-framework` is
   deprecated by its component roots?

## Planned Surfaces

1. How should public docs talk about planned Project02 component surfaces now
   that their source material exists under knowledge/ component roots but the
   top-level composer remains the installable package?
2. How should public docs talk about planned Project03 concept-card-method
   without overclaiming availability?
3. Should public docs mention future Arc06 package/install validation work, or
   reserve that for planning artifacts?

## Re-Entry Conditions

1. Which source changes should reopen accepted vocabulary: entrypoint changes,
   package root changes, Makefile target changes, package-path exceptions,
   generated zip contents, or docs route changes?
2. Should CCDP vocabulary reopen if it gains an installable assistant-skill
   entrypoint?
3. Should Biome vocabulary reopen if source root and package roots are split?
4. Should atomic/composite examples reopen if future package checks show
   different load behavior?
5. Should current metadata categories be changed in Slice03, or deferred until
   package/install validation in Arc06?

## Slice02 Decision Inputs

Slice02 should turn this register into accepted vocabulary, examples,
avoid-list, source-edit authorization, and re-entry conditions. It should keep
kind, topology, examples, avoid-list, planned surfaces, and re-entry
conditions explicit rather than folding them into prose.
