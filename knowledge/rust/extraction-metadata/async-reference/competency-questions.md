# Competency Questions for Async Reference

## Definitional (What is X?)
1. What is pinning in Rust?
2. What is the `Pin` type?
3. What is the `Unpin` trait?
4. What is a place in Rust's memory model?
5. What is move semantics in Rust?
6. What is a self-referential type?
7. What is structural pinning (pin projection)?
8. What is address sensitivity?
9. What is `PhantomPinned`?
10. What is async cancellation?
11. What is cancellation safety?
12. What is structured concurrency?
13. What is a task tree?
14. What is temporal scope in structured concurrency?
15. What is async drop?

## Relational (How does X relate to Y?)
16. How does pinning relate to async/await implementation?
17. How does `Unpin` relate to `Pin`?
18. How does move semantics relate to self-referential types?
19. How does structural pinning relate to field access on pinned types?
20. How does `Drop` interact with pinning?
21. How does structured concurrency relate to error propagation?
22. How do scoped threads relate to structured concurrency?
23. How does cancellation propagation work in structured concurrency?

## Procedural (How do I do X?)
24. How do I pin a value on the heap?
25. How do I pin a value on the stack?
26. How do I implement pin projection for a struct?
27. How do I use `Pin<&mut Self>` in method signatures?
28. How do I apply structured concurrency principles to async Rust programs?
29. How do I implement `Drop` for a pinned type?

## Prerequisite (What before X?)
30. What must I understand before learning about `Pin`?
31. What must I understand before applying structured concurrency?

## Diagnostic (What distinguishes X from Y?)
32. What is the difference between `Pin<Box<T>>` and `Box<T>`?
33. What is the difference between `Unpin` and `!Unpin` types?
34. What is the difference between structured and unstructured concurrency?
35. What is the difference between cancellation and cancellation safety?
36. What distinguishes structural pinning from non-structural pinning of fields?
37. What is the difference between scoped threads and unscoped threads?
