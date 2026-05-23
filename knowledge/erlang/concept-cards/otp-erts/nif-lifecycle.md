---
concept: NIF Lifecycle and Versioning
slug: nif-lifecycle
category: performance
subcategory: native-code-integration
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erl_nif"
chapter_number: null
pdf_page: null
section: "Initialization / Functionality"
extraction_confidence: high
aliases:
  - "NIF versioning"
  - "NIF load callback"
  - "NIF upgrade callback"
  - "NIF library lifecycle"
  - "ERL_NIF_INIT"
prerequisites:
  - erl-nif
extends:
  - erl-nif
related:
  - nif-resources
  - nif-thread-safety
contrasts_with: []
answers_questions:
  - "How does NIF library loading and upgrading work?"
  - "What happens when a module with NIFs is upgraded?"
  - "How does NIF version management work?"
---

# Quick Definition

NIF library lifecycle is managed through three callbacks -- `load`, `upgrade`, and `unload` -- passed to `ERL_NIF_INIT`. `load` is called when no previous NIF library exists for the module; `upgrade` when old code already has a loaded library. Private data can be maintained across NIF calls via `enif_priv_data`. Version management ensures binary compatibility between the NIF library and the runtime system through major/minor version checking.

# Core Definition

The ERTS documentation describes three lifecycle callbacks registered via `ERL_NIF_INIT(MODULE, funcs, load, NULL, upgrade, unload)`:

- **`load`**: "called when the NIF library is loaded and no previously loaded library exists for this module." It can set `*priv_data` to point to private data accessible via `enif_priv_data`. Returns 0 on success; any other value causes the library to fail to load. Can be NULL if no initialization is needed.

- **`upgrade`**: "called when the NIF library is loaded and there is old code of this module with a loaded NIF library." Works like `load` but receives `*old_priv_data` containing the value from the previous library's load/upgrade call. Both `*priv_data` and `*old_priv_data` can be written to. Returns 0 on success; the library fails to load if it returns non-zero OR if `upgrade` is NULL.

- **`unload`**: "called when the module instance that the NIF library belongs to is purged as old."

For module upgrade and static data, the source states: "A loaded NIF library is tied to the Erlang module instance that loaded it. If the module is upgraded, the new module instance needs to load its own NIF library (or maybe choose not to). The new module instance can, however, choose to load the exact same NIF library as the old code if it wants to. Sharing the dynamic library means that static data defined by the library is shared as well."

Version management uses `ERL_NIF_MAJOR_VERSION` and `ERL_NIF_MINOR_VERSION`, compiled into the library. The runtime refuses to load a library with a different major version or a minor version greater than the runtime's.

# Prerequisites

- **erl-nif** -- Lifecycle management is part of the NIF framework

# Key Properties

1. `load` is called for first-time loading; `upgrade` when old code already has a NIF library
2. `upgrade` being NULL causes module upgrade to fail -- this is a deliberate design point
3. Private data (`enif_priv_data`) persists across NIF calls within a module instance
4. Each module instance has its own private data, even when sharing the same .so file
5. `unload` is called when the module instance is purged (old code replaced)
6. A NIF library is persistent -- not unloaded until its module instance is purged
7. Resource types created via `enif_open_resource_type` support inheritance during upgrade
8. Major version changes require recompilation; minor version additions are backward compatible
9. Old NIF libraries with lower major versions are allowed during a transition period of two major releases
10. The `reload` callback (fourth argument to `ERL_NIF_INIT`) is deprecated and must be NULL since OTP 20

# Construction / Recognition

## To Construct/Create:

```c
static int load(ErlNifEnv* env, void** priv_data, ERL_NIF_TERM load_info) {
    MyPrivData* data = enif_alloc(sizeof(MyPrivData));
    /* initialize data... */
    *priv_data = data;
    return 0;
}

static int upgrade(ErlNifEnv* env, void** priv_data,
                   void** old_priv_data, ERL_NIF_TERM load_info) {
    MyPrivData* old = (MyPrivData*)*old_priv_data;
    MyPrivData* new = enif_alloc(sizeof(MyPrivData));
    /* migrate state from old to new... */
    *priv_data = new;
    return 0;
}

static void unload(ErlNifEnv* env, void* priv_data) {
    enif_free(priv_data);
}

ERL_NIF_INIT(my_module, nif_funcs, load, NULL, upgrade, unload)
```

## To Identify/Recognize:

1. `ERL_NIF_INIT` macro with load/upgrade/unload function pointers
2. Functions matching the `load`, `upgrade`, or `unload` callback signatures
3. Use of `enif_priv_data` to access per-module-instance state

# Context & Application

The lifecycle system supports Erlang's hot code upgrade mechanism. When a module is upgraded:

1. The new module instance loads its NIF library, calling `upgrade`
2. The `upgrade` callback can access the old private data to migrate state
3. Resource types can be "inherited" -- the new library takes ownership of existing resource objects, and its destructor is used for inherited objects
4. Once the old module instance is purged, `unload` is called for the old library
5. The old library's unloading is postponed as long as resource objects with destructors from that library exist

This enables seamless upgrades of NIF libraries in long-running systems without losing state or orphaning native resources.

# Examples

**Example 1** (erl_nif, Initialization): The `ERL_NIF_INIT` macro:

```c
ERL_NIF_INIT(MODULE, ErlNifFunc funcs[], load, NULL, upgrade, unload)
```

The source states: "`MODULE` is the name of the Erlang module as an identifier without string quotations. It is stringified by the macro." The fourth argument `NULL` replaces the deprecated `reload` callback.

**Example 2** (erl_nif, Functionality, Module upgrade and static data):

The source explains: "To avoid unintentionally shared static data between module instances, each Erlang module version can keep its own private data. This private data can be set when the NIF library is loaded and later retrieved by calling `enif_priv_data`."

**Example 3** (erl_nif, Functionality, Resource objects): Resource type upgrade:

"Resource types support upgrade in runtime by allowing a loaded NIF library to take over an already existing resource type and by that 'inherit' all existing objects of that type. The destructor of the new library is thereafter called for the inherited objects and the library with the old destructor function can be safely unloaded."

# Relationships

## Builds Upon

- **erl-nif** -- Lifecycle is part of the NIF framework

## Related

- **nif-resources** -- Resource types are created during load/upgrade and can be inherited
- **nif-thread-safety** -- load/upgrade callbacks are thread-safe for shared state

# Common Errors

- **Error**: Setting `upgrade` to NULL and then trying to hot-upgrade the module
  **Correction**: If `upgrade` is NULL, loading the NIF library during module upgrade will fail; always provide an `upgrade` callback if hot code upgrade is expected

- **Error**: Not handling resource type inheritance during upgrade
  **Correction**: Call `enif_open_resource_type` with `ERL_NIF_RT_TAKEOVER` flag in the `upgrade` callback to inherit existing resource objects

- **Error**: Passing a non-NULL value for the fourth argument to `ERL_NIF_INIT` (the deprecated reload callback)
  **Correction**: The reload callback is no longer supported since OTP 20; always pass NULL

# Common Confusions

- **Confusion**: Thinking `load` and `upgrade` are interchangeable
  **Clarification**: `load` is called only when no previous NIF library exists; `upgrade` is called when old code has a library. If the wrong one fires, the library fails to load.

- **Confusion**: Believing static C variables are isolated between module instances
  **Clarification**: If the same .so file is loaded by both old and new module instances, static data is shared; use `enif_priv_data` for per-instance state

- **Confusion**: Thinking `unload` is called when `load_nif/2` is called again
  **Clarification**: `unload` is called when the module instance is purged as old, not when a new version loads

# Source Reference

- "erl_nif" reference (Initialization section: ERL_NIF_INIT, load, upgrade, unload)
- "erl_nif" reference (Functionality section: "Module upgrade and static data," "Version Management," "Resource objects" upgrade behavior)

# Verification Notes

- Callback descriptions: Directly from erl_nif.md Initialization section
- Module upgrade quote: From erl_nif.md Functionality section
- Resource type upgrade: Quoted from erl_nif.md Resource objects section
- Version management: From erl_nif.md Version Management section
- Confidence: HIGH -- lifecycle callbacks are explicitly documented with clear semantics
