# Competency Questions for Rust Macros (The Little Book of Rust Macros)

## Definitional (What is X?)
1. What is macro_rules! in Rust?
2. What is a token tree?
3. What is a metavariable (capture) in a macro?
4. What are fragment specifiers?
5. What is macro expansion?
6. What is macro hygiene?
7. What is a syntax extension?
8. What is the TT muncher pattern?
9. What is push-down accumulation?
10. What is the callback pattern in macros?
11. What is AST coercion?
12. What is an internal rules pattern?

## Relational (How does X relate to Y?)
13. How do token trees relate to the AST?
14. How does macro hygiene relate to variable scoping?
15. How do fragment specifiers relate to macro matching?
16. How does repetition relate to metavariable captures?

## Procedural (How do I do X?)
17. How do I write a macro_rules! macro?
18. How do I capture expressions, types, and identifiers in macros?
19. How do I use repetition patterns in macros?
20. How do I debug macro expansion?
21. How do I count items in a macro?
22. How do I parse complex input in a macro?
23. How do I design a macro invocation syntax?

## Prerequisite (What before X?)
24. What must I understand before writing declarative macros?

## Diagnostic (What distinguishes X from Y?)
25. What is the difference between tokens and token trees?
26. What is the difference between EarlyLintPass-level and macro-level processing?
27. What is the difference between the callback pattern and direct macro expansion?
28. What is the difference between declarative macros and procedural macros?
