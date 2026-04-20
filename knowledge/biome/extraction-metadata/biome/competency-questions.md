# Competency Questions for Biome Documentation

## Definitional (What is X?)
1. What is Biome?
2. What is the Biome formatter?
3. What is the Biome linter?
4. What is Biome Assist?
5. What is a CST (Concrete Syntax Tree)?
6. What is trivia in the context of Biome's parser?
7. What is a bogus node?
8. What is GritQL?
9. What is a linter domain?
10. What is a diagnostic in Biome?
11. What is a suppression comment?
12. What is the Biome Scanner?
13. What is a safe fix vs. an unsafe fix?
14. What is the Biome daemon?
15. What are lint rule groups?

## Relational (How does X relate to Y?)
1. How does the Biome formatter relate to Prettier?
2. How do lint rule groups relate to individual rules?
3. How do linter domains relate to rule groups?
4. How does the Scanner relate to project-domain rules?
5. How does biome.json configuration relate to CLI options?
6. How does VCS integration relate to file processing?
7. How do safe fixes and unsafe fixes relate to code actions?
8. How does the CST relate to error-resilient parsing?
9. How does GritQL relate to linter plugins?
10. How do nested configurations relate to monorepo support?

## Procedural (How do I do X?)
1. How do I install and set up Biome?
2. How do I configure the Biome formatter?
3. How do I enable or disable a lint rule?
4. How do I suppress a lint rule for a line, range, or file?
5. How do I set up Biome in a monorepo?
6. How do I integrate Biome with Git hooks?
7. How do I set up Biome in CI?
8. How do I migrate from ESLint/Prettier to Biome?
9. How do I write a GritQL linter plugin?
10. How do I configure Biome to process only changed files?

## Prerequisite (What before X?)
1. What must I understand before configuring lint domains?
2. What must I know before writing GritQL plugins?
3. What must I understand before using project-domain rules?
4. What must I know before setting up monorepo configuration?
5. What should I understand before migrating from Prettier?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes `biome check` from `biome ci`?
2. What distinguishes safe fixes from unsafe fixes?
3. What distinguishes lint rule groups from domains?
4. What distinguishes inline, top-level, and range suppressions?
5. What distinguishes `biome format`, `biome lint`, and `biome check`?
6. What distinguishes error, warning, and info severity?
7. What distinguishes Biome Assist from the Biome Linter?
8. What distinguishes the formatter's opinionated approach from configurable formatters?
