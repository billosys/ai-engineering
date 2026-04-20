# Domain Taxonomy for Deep JavaScript

## Categories
- type-system (type coercion, conversion algorithms, equality)
- language-mechanics (destructuring, environments, scoping, operators)
- object-model (property descriptors, attributes, assignment, definition)
- object-protection (freeze, seal, preventExtensions, immutability)
- data-management (copying, mutation, shared state, defensive patterns)
- class-patterns (instantiation, cloning, wrapping, factory methods)
- regular-expressions (lookaround, composition, template tags)
- async-programming (promises, states, chaining, microtasks)
- metaprogramming (proxies, traps, handlers, membranes, reflection)
- functions (naming, .name property, binding)

## Tiers
- foundational: No prerequisites from this source (basic JS concepts assumed)
- intermediate: Requires foundational concepts from this source
- advanced: Requires intermediate concepts from this source

## Notation Conventions
- ECMAScript spec operations: ToPrimitive(), ToNumber(), ToString(), ToBoolean()
- Internal slots: [[Prototype]], [[Extensible]], [[Scope]]
- Property attributes: value, writable, get, set, configurable, enumerable
- Promise states: pending, fulfilled, rejected
- Regex assertions: (?=...), (?!...), (?<=...), (?<!...)
