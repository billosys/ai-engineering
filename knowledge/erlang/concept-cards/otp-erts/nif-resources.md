---
concept: NIF Resource Objects
slug: nif-resources
category: performance
subcategory: native-code-integration
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erl_nif"
chapter_number: null
pdf_page: null
section: "Functionality / Resource objects"
extraction_confidence: high
aliases:
  - "NIF resources"
  - "resource objects"
  - "enif_alloc_resource"
  - "ErlNifResourceType"
prerequisites:
  - erl-nif
extends:
  - erl-nif
related:
  - nif-lifecycle
  - dirty-nif-schedulers
contrasts_with: []
answers_questions:
  - "How do I safely pass C data structures through Erlang terms?"
  - "How does NIF resource garbage collection work?"
  - "What are NIF resource types?"
---

# Quick Definition

NIF resource objects are a safe mechanism for wrapping pointers to native C data structures as opaque Erlang terms. A resource is a block of memory allocated with `enif_alloc_resource`, turned into an opaque term with `enif_make_resource`, and automatically garbage collected by the VM when the last reference is gone and `enif_release_resource` has been called.

# Core Definition

The ERTS documentation states: "The use of resource objects is a safe way to return pointers to native data structures from a NIF. A resource object is only a block of memory allocated with `enif_alloc_resource`. A handle ('safe pointer') to this memory block can then be returned to Erlang by the use of `enif_make_resource`. The term returned by `enif_make_resource` is opaque in nature. It can be stored and passed between processes, but the only real end usage is to pass it back as an argument to a NIF." (erl_nif, Functionality, Resource objects).

Resource objects have a dual ownership model: "A resource object is not deallocated until the last handle term is garbage collected by the VM and the resource is released with `enif_release_resource` (not necessarily in that order)."

All resources are created as instances of a **resource type**, which is created by calling `enif_open_resource_type` during library loading. Resource types are uniquely identified by a name string and the implementing module name. Each type can have a user-supplied destructor function that is automatically called when resources of that type are released.

# Prerequisites

- **erl-nif** -- Resource objects are a feature of the NIF API

# Key Properties

1. Resources are allocated with `enif_alloc_resource`, which takes a resource type and size
2. `enif_make_resource` creates an opaque Erlang term (handle) from a resource pointer
3. `enif_get_resource` retrieves the C pointer from a handle term, verifying the resource type
4. Resources are reference counted with dual ownership: Erlang terms (GC) and native code (`enif_release_resource`)
5. Resource types are created during `load`/`upgrade` callbacks via `enif_open_resource_type`
6. Each resource type has an optional destructor (`ErlNifResourceDtor`) called automatically on deallocation
7. Resource types support runtime upgrade -- a new NIF library can "inherit" existing resource objects
8. Resources can also be used to create binary terms with custom memory management via `enif_make_resource_binary`
9. Opaque resource terms can be stored in ETS, passed between processes, but only meaningfully used by passing back to a NIF

# Construction / Recognition

## To Construct/Create:

1. During `load`/`upgrade`, create a resource type:
   ```c
   my_resource_type = enif_open_resource_type(env, NULL, "my_resource",
                                               my_destructor,
                                               ERL_NIF_RT_CREATE, NULL);
   ```

2. In a NIF, allocate and return a resource:
   ```c
   MyStruct* obj = enif_alloc_resource(my_resource_type, sizeof(MyStruct));
   /* initialize obj... */
   ERL_NIF_TERM term = enif_make_resource(env, obj);
   enif_release_resource(obj);  /* Erlang now owns it */
   return term;
   ```

3. In another NIF, retrieve the resource:
   ```c
   MyStruct* obj;
   if (!enif_get_resource(env, argv[0], my_resource_type, (void**)&obj))
       return enif_make_badarg(env);
   /* use obj... */
   ```

## To Identify/Recognize:

1. Code using `enif_alloc_resource`, `enif_make_resource`, `enif_get_resource`
2. `ErlNifResourceType*` variables, typically stored as module-level static pointers
3. Resource destructor functions with the `ErlNifResourceDtor` signature

# Context & Application

Resource objects solve the fundamental problem of safely passing native pointers through the Erlang world. Without resources, a NIF would have to return a raw pointer as an integer, which is unsafe -- the pointer could be used after free, cast to the wrong type, or manipulated arbitrarily by Erlang code.

With resources, the VM guarantees:
- Type safety: `enif_get_resource` verifies the resource type
- Memory safety: the destructor is called exactly once, after both the Erlang GC and native code have released their references
- Upgrade safety: resource types can be inherited by new library versions

A secondary use case is `enif_make_resource_binary`, which creates a binary term backed by resource memory. The destructor is called when the binary is garbage collected, enabling patterns like memory-mapped file access where `munmap` is called in the destructor.

# Examples

**Example 1** (erl_nif, Functionality, Resource objects): The template pattern for creating and returning a resource:

```c
ERL_NIF_TERM term;
MyStruct* obj = enif_alloc_resource(my_resource_type, sizeof(MyStruct));

/* initialize struct ... */

term = enif_make_resource(env, obj);

if (keep_a_reference_of_our_own) {
    /* store 'obj' in static variable, private data
       or other resource object */
}
else {
    enif_release_resource(obj);
    /* resource now only owned by "Erlang" */
}
return term;
```

The source explains: "once `enif_make_resource` creates the term to return to Erlang, the code can choose to either keep its own native pointer to the allocated struct and release it later, or release it immediately and rely only on the garbage collector to deallocate the resource object eventually when it collects the term."

**Example 2** (erl_nif, Functionality, Resource objects): The `ErlNifResourceTypeInit` struct for advanced resource types:

```c
typedef struct {
    ErlNifResourceDtor* dtor;       // Destructor
    ErlNifResourceStop* stop;       // Select stop callback
    ErlNifResourceDown* down;       // Monitor down callback
    int members;
    ErlNifResourceDynCall* dyncall; // Dynamic call
} ErlNifResourceTypeInit;
```

Resources can integrate with the I/O select mechanism (via `stop`) and process monitoring (via `down`), enabling resource objects to react to external events.

# Relationships

## Builds Upon

- **erl-nif** -- Resource objects are part of the NIF API

## Related

- **nif-lifecycle** -- Resource types are created during load/upgrade and inherited during upgrades
- **dirty-nif-schedulers** -- Resource access in dirty NIFs requires the same synchronization as in regular NIFs

# Common Errors

- **Error**: Not calling `enif_release_resource` after `enif_make_resource`, keeping the native reference alive forever
  **Correction**: If you do not need to keep a native reference, call `enif_release_resource` immediately after `enif_make_resource`; the Erlang GC will then manage the lifetime

- **Error**: Accessing a resource after its destructor has been called
  **Correction**: The destructor is the last valid access point; once called, the memory is deallocated

- **Error**: Creating resource types outside of `load`/`upgrade` callbacks
  **Correction**: `enif_open_resource_type` can only be called during library initialization (from `load` or `upgrade` callbacks)

# Common Confusions

- **Confusion**: Thinking resource terms carry meaningful data that Erlang code can inspect
  **Clarification**: Resource terms are fully opaque; they can be stored and passed around but the only useful operation is passing them back to a NIF that calls `enif_get_resource`

- **Confusion**: Believing `enif_release_resource` immediately frees the resource
  **Clarification**: It only decrements the native reference count; the resource is not freed until both the Erlang GC has collected all handle terms AND `enif_release_resource` has been called

- **Confusion**: Thinking resource types from different modules can share resources
  **Clarification**: Resource types are uniquely identified by their name string AND the implementing module name; `enif_get_resource` will fail if the type does not match

# Source Reference

- "erl_nif" reference (Functionality section, "Resource objects" subsection)
- "erl_nif" reference (Data Types: ErlNifResourceType, ErlNifResourceTypeInit, ErlNifResourceDtor, ErlNifResourceDown, ErlNifResourceStop, ErlNifResourceDynCall)

# Verification Notes

- Definition: Directly quoted from erl_nif.md, Functionality, "Resource objects"
- Dual ownership: Directly quoted from source
- Template example: Verbatim from source
- Confidence: HIGH -- resource objects are thoroughly documented with explicit examples
