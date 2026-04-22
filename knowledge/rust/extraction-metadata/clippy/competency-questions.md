# Competency Questions for Clippy

## Definitional (What is X?)
1. What is Clippy?
2. What is a Clippy lint group?
3. What is a lint level (allow/warn/deny/forbid)?
4. What is the clippy.toml configuration file?
5. What is a lint pass (EarlyLintPass vs LateLintPass)?
6. What is LateContext?
7. What is TypeckResults?
8. What is Ty and TyKind in Clippy lint development?
9. What is a diagnostic item?
10. What is clippy-driver?
11. What is lintcheck?

## Relational (How does X relate to Y?)
12. How do lint groups relate to individual lints?
13. How does LateContext relate to TypeckResults?
14. How does Ty relate to TyKind?
15. How do EarlyLintPass and LateLintPass differ?

## Procedural (How do I do X?)
16. How do I run Clippy on a project?
17. How do I configure which Clippy lints are enabled?
18. How do I set up Clippy in CI/CD?
19. How do I use cargo clippy --fix?
20. How do I create a new Clippy lint?
21. How do I register a lint with Clippy?
22. How do I emit a lint diagnostic?
23. How do I check the type of an expression in a lint?
24. How do I check if a type implements a specific trait?
25. How do I deal with macros when writing lints?

## Prerequisite (What before X?)
26. What must I understand before writing a Clippy lint?

## Diagnostic (What distinguishes X from Y?)
27. What is the difference between clippy::pedantic and clippy::restriction?
28. What is the difference between EarlyLintPass and LateLintPass?
29. What is the difference between allow, warn, deny, and forbid?
30. What is the difference between clippy::all, clippy::pedantic, and clippy::nursery?
