---
# === CORE IDENTIFICATION ===
concept: KV Data Modeling
slug: kv-data-modeling

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/data_modeling_typescript.md"
chapter_number: null
pdf_page: null
section: "Data Modeling in TypeScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "KV data modeling patterns"
  - "TypeScript data modeling for KV"
  - "KV DTOs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-kv
  - kv-operations
  - kv-secondary-indexes
extends: []
related:
  - kv-key-space
  - kv-atomic-transactions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I model data in Deno KV with TypeScript?"
  - "How do I get strongly typed objects from Deno KV?"
---

# Quick Definition
Data modeling in Deno KV uses TypeScript interfaces as data transfer objects (DTOs) combined with type assertions or generic type parameters to achieve strongly typed storage and retrieval, with a service layer encapsulating business logic and cross-index lookups.

# Core Definition
Deno KV stores and retrieves untyped JavaScript objects. To work with strongly typed data in TypeScript, you define interfaces describing the shape of your data and use them as data transfer objects (DTOs). When storing data, TypeScript interfaces guide the shape of what you pass to `kv.set()`. When retrieving data, you apply type assertions (`as Author`) or use the generic type parameter on `kv.get<Author>()` to inform the TypeScript compiler of the expected shape.

For complex domain objects with relationships (e.g., a blog post referencing an author), a service layer of pure functions wraps `kv.get()` and `kv.set()` to handle serialization, hydration, and cross-index lookups. A common pattern is to extend the DTO with a "raw" interface that includes foreign key references (e.g., `authorUsername`), storing this raw form in KV and resolving references when reading.

# Prerequisites
- Understanding of Deno KV operations (kv-operations)
- Familiarity with TypeScript interfaces and type assertions
- Understanding of secondary indexes for cross-entity references (kv-secondary-indexes)

# Key Properties
1. **Interface-based DTOs** -- Define TypeScript interfaces for domain objects; use them to type data going into and out of KV
2. **Type assertions** -- Use `as Type` or generic parameter `kv.get<Type>(key)` for typed retrieval
3. **Service layer pattern** -- Wrap KV operations in functions that handle serialization, hydration, and cross-reference resolution
4. **Raw/extended interfaces** -- Extend DTOs with foreign key fields for storage; strip them during hydration
5. **Separation of persistence and domain logic** -- Service functions replace direct `kv.get()`/`kv.set()` calls with typed, validated operations

# Construction / Recognition
- Define a DTO interface:
  ```
  interface Author { username: string; fullName: string; }
  ```
- Store with type: `await kv.set(["authors", a.username], a);`
- Retrieve with type parameter: `const r = await kv.get<Author>(["authors", "acdoyle"]);`
- Retrieve with type assertion: `const ac = r.value as Author;`
- Service function with cross-reference:
  ```
  interface RawPost extends Post { authorUsername: string; }
  async function getPost(slug: string): Promise<Post> {
    const rawPost = (await kv.get(["posts", slug])).value as RawPost;
    const author = (await kv.get(["authors", rawPost.authorUsername])).value as Author;
    return Object.assign({}, rawPost, { author }) as Post;
  }
  ```

# Context & Application
This pattern is essential for any non-trivial Deno KV application where domain objects have relationships or require validation. The service layer acts as a mini repository pattern, keeping KV access details out of business logic. It is the natural progression from simple key-value storage to structured application data management.

# Examples
From deploy/kv/data_modeling_typescript.md:
- Blog system with `Author` and `Post` interfaces
- `RawPost` extends `Post` with `authorUsername` field for storage
- `savePost` function serializes a Post with the author reference
- `getPost` function hydrates a Post by resolving the author from a separate KV read

# Relationships
## Builds Upon
- kv-operations (get, set)
- kv-secondary-indexes (cross-entity references)
- kv-key-space (key design for entities)

## Enables
- Complex application data architectures on Deno KV

## Related
- kv-atomic-transactions (service functions may use atomic operations for consistency)

## Contrasts With
- ORM patterns (ORMs auto-map objects to database rows; KV data modeling is manual)

# Common Errors
1. Forgetting that `kv.get()` returns untyped data -- without type assertions or generics, the value is `unknown`
2. Storing class instances instead of plain objects -- KV uses structured clone, which does not preserve class prototypes
3. Not handling `null` values -- `kv.get()` returns `null` value when key does not exist; the type assertion does not prevent this

# Common Confusions
1. **Type safety at runtime** -- TypeScript type assertions are compile-time only; they do not validate the actual shape of data at runtime
2. **Raw vs. domain interfaces** -- The raw interface is what gets stored in KV (with foreign keys); the domain interface is what the application works with (with resolved references)

# Source Reference
- deploy/kv/data_modeling_typescript.md: Guide covering interface-based DTOs, type assertions, generic type parameters, and service layer patterns with a blog system example

# Verification Notes
- High confidence: Patterns are explicitly documented with complete code examples
- Blog system example (Author, Post, RawPost) taken directly from source
