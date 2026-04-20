# Competency Questions for Google Go Style Guide

## Definitional (What is X?)
1. What are the five style principles in the Google Go Style Guide?
2. What does "canonical" mean in the context of Google's Go style documents?
3. What does "normative" mean in the context of Google's Go style documents?
4. What does "idiomatic" mean in the context of Go code?
5. What is the least mechanism principle?
6. What are Must functions in Go?
7. What are in-band errors?
8. What is signal boosting in Go documentation?
9. What is a test helper vs. an assertion library?
10. What is a test double package?
11. What are sentinel errors in Go?
12. What are variadic options in Go function design?

## Relational (How does X relate to Y?)
1. How does clarity relate to simplicity in Go style?
2. How do the three Google Go style documents (Guide, Decisions, Best Practices) relate to each other?
3. How does repetition in naming relate to package names?
4. How does `errors.Is` relate to `errors.As` for error matching?
5. How does `%w` relate to `%v` for error wrapping context?
6. How do receiver names relate to variable name length guidelines?
7. How does `t.Error` relate to `t.Fatal` in test design?
8. How does global state relate to dependency injection?
9. How do option structs relate to variadic options?
10. How does import renaming relate to package naming?

## Procedural (How do I do X?)
1. How do I name variables according to scope size in Go?
2. How do I write effective doc comments in Go?
3. How do I organize imports at Google?
4. How do I handle errors effectively in Go?
5. How do I structure error types for programmatic matching?
6. How do I add context to wrapped errors without redundancy?
7. How do I format composite literals properly?
8. How do I write useful test failure messages?
9. How do I design effective interfaces in Go?
10. How do I manage goroutine lifetimes properly?
11. How do I use contexts correctly in Go?
12. How do I declare variables using zero values vs composite literals?

## Prerequisite (What before X?)
1. What must I understand before applying the least mechanism principle?
2. What must I know before designing Go error types?
3. What must I understand before using Must functions?
4. What must I know before using generics in Go?
5. What Go fundamentals are needed before understanding receiver type choices?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes clarity from concision in Go?
2. What distinguishes doc comments from regular comments?
3. What distinguishes `import _` from `import .`?
4. What distinguishes in-band errors from returned errors?
5. What distinguishes value receivers from pointer receivers?
6. What distinguishes `t.Error` from `t.Fatal`?
7. What distinguishes test helpers from assertion libraries?
8. What distinguishes option structs from variadic options?
9. What distinguishes package-level global state from instance-based state?
10. What distinguishes MixedCaps from snake_case in Go naming?
