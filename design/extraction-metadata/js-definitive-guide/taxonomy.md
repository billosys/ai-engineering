# Domain Taxonomy for JavaScript: The Definitive Guide

## Categories
- language-fundamentals (lexical structure, types, variables, literals, operators, statements)
- type-system (primitive types, type coercion, type conversion, equality semantics)
- objects (object creation, properties, prototypes, property descriptors, serialization)
- arrays (array creation, methods, iteration, typed arrays, array-like objects)
- functions (declarations, expressions, closures, invocation, this binding, functional patterns)
- classes (class syntax, constructors, inheritance, subclasses, private fields, prototypes)
- modules (CommonJS, ES6 modules, import/export, dynamic imports, bundling)
- iterators-generators (iterator protocol, generator functions, yield, async iteration)
- async-programming (callbacks, promises, async/await, event loop, error handling)
- metaprogramming (property attributes, proxies, reflect, well-known symbols, object protection)
- standard-library (Set, Map, RegExp, Date, Error, JSON, Intl, Console, URL, timers)
- browser-apis (DOM, events, CSS scripting, canvas, web components, networking, storage, workers)
- node-apis (streams, buffers, EventEmitter, file system, HTTP, child processes, worker threads)
- tooling (linting, formatting, testing, package management, bundling, transpilation, type checking)

## Tiers
- foundational: No prerequisites from this source (basic programming assumed)
- intermediate: Requires foundational concepts from this source
- advanced: Requires intermediate concepts from this source

## Notation Conventions
- ECMAScript versions: ES5, ES6/ES2015, ES2016-ES2020
- Type coercion functions: Number(), String(), Boolean(), Symbol()
- Internal operations: [[Prototype]], [[Extensible]], [[Get]], [[Set]]
- Property attributes: value, writable, enumerable, configurable, get, set
- Promise states: pending, fulfilled, rejected
- Iterator protocol: Symbol.iterator, next(), {value, done}
- Well-known symbols: Symbol.iterator, Symbol.toPrimitive, Symbol.hasInstance, Symbol.species, Symbol.toStringTag
- DOM methods: querySelector(), getElementById(), addEventListener()
- Node patterns: error-first callbacks, EventEmitter.on()/emit()
