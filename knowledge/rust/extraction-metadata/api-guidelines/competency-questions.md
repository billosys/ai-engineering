# Competency Questions for Rust API Guidelines

## Definitional (What is X?)
1. What are the Rust API Guidelines?
2. What are the naming conventions for Rust APIs (C-CASE, C-CONV, C-GETTER, C-ITER)?
3. What common traits should Rust types implement (C-COMMON-TRAITS)?
4. What are the macro design guidelines?
5. What are the documentation guidelines for Rust APIs?
6. What are the predictability guidelines?
7. What are the type safety guidelines (C-NEWTYPE, C-CUSTOM-TYPE, C-BUILDER)?
8. What is a sealed trait (C-SEALED)?

## Procedural (How do I do X?)
9. How should I name conversion methods (as_, to_, into_)?
10. How should I implement interoperability traits (From, AsRef, Serde)?
11. How should I document a Rust crate?
12. How should I design for future compatibility?
13. How should I use newtypes for type safety?
14. How should I minimize assumptions about function parameters?

## Diagnostic (What distinguishes X from Y?)
15. What is the difference between as_, to_, and into_ conversions?
16. When should I use generics vs concrete types in API design?
17. When should I seal a trait vs leave it open?
