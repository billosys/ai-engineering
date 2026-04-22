# Competency Questions for Rust Design Patterns

## Definitional (What is X?)
1. What is the borrowed types idiom?
2. What is the constructor idiom in Rust?
3. What is the Default trait pattern?
4. What is the newtype pattern?
5. What is the builder pattern in Rust?
6. What is RAII with guards?
7. What is the command pattern in Rust?
8. What is the strategy pattern in Rust?
9. What is the visitor pattern in Rust?
10. What is the interpreter pattern?
11. What is the fold pattern?
12. What is on-stack dynamic dispatch?
13. What is the Deref polymorphism anti-pattern?
14. What are functional optics?
15. What is the generics-as-type-classes pattern?

## Relational (How does X relate to Y?)
16. How do Rust idioms relate to the borrow checker?
17. How does the newtype pattern relate to type safety?
18. How does RAII relate to Rust's Drop trait?
19. How does the strategy pattern differ in Rust vs OOP languages?

## Procedural (How do I do X?)
20. How do I use borrowed types for function arguments?
21. How do I implement the builder pattern?
22. How do I handle FFI string passing idiomatically?
23. How do I use mem::take and mem::replace?
24. How do I use #[non_exhaustive] for API extensibility?
25. How do I implement object-based FFI APIs?

## Diagnostic (What distinguishes X from Y?)
26. What is the difference between idioms, patterns, and anti-patterns?
27. What is the difference between cloning to satisfy the borrow checker vs legitimate cloning?
28. What is the difference between #![deny(warnings)] in library vs binary crates?
29. What is the difference between imperative and declarative style in Rust?
30. What is the difference between the builder pattern and constructor functions?
