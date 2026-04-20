---
# === CORE IDENTIFICATION ===
concept: Sandbox Volumes
slug: sandbox-volumes

# === CLASSIFICATION ===
category: sandbox
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "sandbox/volumes.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "persistent storage"
  - "snapshots"
  - "block storage"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-sandbox
extends: []
related:
  - sandbox-security
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I persist data across sandbox sessions?"
  - "What are sandbox volumes and snapshots?"
---

# Quick Definition
Deno Sandbox provides two storage primitives: volumes (read-write regional block storage, 300 MB to 20 GB, for caches/databases/artifacts) and snapshots (read-only images created from volumes for pre-installed software, enabling instant boot with toolchains ready).

# Core Definition
Volumes are persistent read-write block storage that can be mounted into sandboxes, allowing data to survive process restarts and new connections. Snapshots are read-only images created from volumes; when used as a sandbox's root filesystem, they replace the default disk image, enabling sandboxes to boot instantly with pre-installed software. Volumes and snapshots are region-specific -- they must be in the same region as the sandbox mounting them. Volumes support one concurrent sandbox at a time; snapshots can be used by many sandboxes simultaneously.

# Prerequisites
- deno-sandbox -- Volumes and snapshots are storage primitives for the sandbox platform

# Key Properties
1. **Volumes: read-write** -- Regional block storage, 300 MB to 20 GB capacity
2. **Snapshots: read-only** -- Created from volumes; many sandboxes can boot from the same snapshot simultaneously
3. **Region-locked** -- Volume/snapshot must match sandbox region (`ord` or `ams`)
4. **Mount at any path** -- Volumes mount to arbitrary paths (e.g., `/data/dataset`); snapshots replace root filesystem
5. **Bootable volumes** -- Created with `from: "builtin:debian-13"` for custom root filesystems
6. **Snapshot workflow** -- Create bootable volume, boot sandbox with it as root, install software, snapshot the volume
7. **Volume from snapshot** -- Create new writable volumes from existing snapshots
8. **Deletion grace period** -- Volumes marked deleted immediately but underlying storage removed after 24 hours
9. **One volume per sandbox** -- Volumes can only be mounted by one sandbox at a time
10. **Slug-based addressing** -- Volumes and snapshots identified by slug or UUID

# Construction / Recognition
```typescript
import { Client, Sandbox } from "@deno/sandbox";
const client = new Client();

// Create a volume
const volume = await client.volumes.create({
  slug: "training-cache", region: "ord", capacity: "2GB",
});

// Mount in sandbox
await using sandbox = await Sandbox.create({
  region: "ord",
  volumes: { "/data/cache": volume.slug },
});
await sandbox.fs.writeTextFile("/data/cache/data.txt", "Persisted!\n");

// Snapshot workflow for pre-installed toolchains
const bootVol = await client.volumes.create({
  slug: "my-toolchain", region: "ord", capacity: "10GiB",
  from: "builtin:debian-13",
});
await using setup = await client.sandboxes.create({ region: "ord", root: bootVol.slug });
await setup.sh`apt-get update && apt-get install -y nodejs npm`;
const snapshot = await client.volumes.snapshot(bootVol.id, { slug: "my-toolchain-snapshot" });

// Boot from snapshot (instant with everything installed)
await using fast = await client.sandboxes.create({ region: "ord", root: "my-toolchain-snapshot" });
await fast.sh`node --version`; // already installed
```

# Context & Application
Volumes are ideal for package caches, build artifacts, SQLite databases, and any workflow needing durable storage without promoting to a full Deploy app. Snapshots solve the cold-start problem for toolchain-heavy sandboxes: install once, snapshot, and every future sandbox starts instantly with everything ready. This is particularly valuable for CI runners and AI agent workflows that need specific toolchains.

# Examples
From sandbox/volumes.md:
- Volume fields: slug (required, unique per org), region (required, must match sandbox), capacity (required, 300 MB - 20 GB)
- "Deletion is a two-step process: The API marks the volume as deleted immediately... A background job waits 24 hours before removing the underlying block storage."
- Volumes vs Snapshots table: volumes are read-write, one sandbox at a time; snapshots are read-only, many sandboxes simultaneously
- Currently only `builtin:debian-13` base image available for bootable volumes

# Relationships
## Builds Upon
- deno-sandbox (volumes/snapshots are sandbox storage primitives)

## Related
- sandbox-security (volume access is explicit per sandbox; can be mounted read-only)

# Common Errors
1. Trying to mount a volume from a different region -- volumes and sandboxes must be in the same region
2. Trying to mount a volume in two sandboxes simultaneously -- only one sandbox can use a volume at a time (snapshots allow concurrent use)

# Common Confusions
1. **Volume vs. snapshot** -- Volumes are writable and single-use; snapshots are read-only and shareable. Use volumes for mutable data, snapshots for immutable toolchains.
2. **Bootable volume vs. regular volume** -- Only volumes created with `from` can be used as root filesystems

# Source Reference
- sandbox/volumes.md: Complete volumes and snapshots documentation with provisioning, mounting, snapshotting, and deletion

# Verification Notes
- High confidence: Storage primitives explicitly documented with API examples, comparison table, and lifecycle details
