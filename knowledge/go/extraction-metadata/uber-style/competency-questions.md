# Competency Questions for Uber Go Style Guide

## Definitional (What is X?)
1. What is the functional options pattern in Go?
2. What is a table-driven test?
3. What is an error sentinel in Go?
4. What is a custom error type?
5. What is error wrapping?
6. What is a zero-value mutex?
7. What is type embedding in Go structs?
8. What is a naked parameter?
9. What are predeclared identifiers in Go?
10. What is a fire-and-forget goroutine?

## Relational (How does X relate to Y?)
1. How do value receivers and pointer receivers differ for interface satisfaction?
2. How does `%w` differ from `%v` in error wrapping?
3. How does `strconv` compare to `fmt` for string conversion performance?
4. How does embedding in structs relate to avoiding embedding in public structs?
5. How does `init()` avoidance relate to the exit-in-main guideline?
6. How do error naming conventions differ for sentinel errors vs. custom error types?
7. How does reduce-nesting relate to unnecessary-else elimination?
8. How do map capacity hints differ from slice capacity specification?
9. How do local variable declarations differ from top-level variable declarations?
10. How does `time.Time` differ from `time.Duration` in external system interactions?

## Procedural (How do I do X?)
1. How do I verify interface compliance at compile time?
2. How do I safely copy slices and maps at API boundaries?
3. How do I properly wrap errors with context?
4. How do I implement the functional options pattern?
5. How do I write a table-driven test with subtests?
6. How do I properly handle type assertion failures?
7. How do I organize imports in a Go file?
8. How do I initialize structs idiomatically?
9. How do I initialize maps using make() vs. map literals?
10. How do I manage goroutine lifetimes properly?

## Prerequisite (What before X?)
1. What must I understand before using the functional options pattern?
2. What must I know before implementing error wrapping?
3. What Go fundamentals are needed before applying the style guidelines?
4. What must I understand about interfaces before using compile-time checks?
5. What must I know about goroutines before understanding lifetime management?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes a sentinel error (`var Err...`) from a custom error type?
2. What distinguishes `errors.Is` from `errors.As`?
3. What distinguishes embedding from composition via fields?
4. What distinguishes `make(map)` from map literal initialization?
5. What distinguishes common errors from common confusions in Go style?
6. What distinguishes `:=` from `var` for variable declarations?
7. What distinguishes `time.Add` from `time.AddDate`?
8. What distinguishes logging-and-returning from wrapping-and-returning errors?
