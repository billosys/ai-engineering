---
concept: Deno in Docker
slug: deno-in-docker
category: platform
subcategory: containerization
tier: advanced
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/docker.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Deno Docker"
  - "Deno containerization"
prerequisites:
  - deno-cli
  - deno-run
extends: []
related:
  - deno-serve
  - deno-in-ci
  - deno-compile
contrasts_with: []
answers_questions:
  - "How do I run Deno in Docker?"
  - "What Docker images does Deno provide?"
  - "How do I write a Dockerfile for a Deno application?"
---

# Quick Definition

Deno provides official Docker images (`denoland/deno`) in multiple variants (latest, alpine, distroless, ubuntu), supporting multi-stage builds, workspace containerization, development containers with hot-reload, and security best practices.

# Core Definition

"Deno provides official Docker files and images." The official images are published at `denoland/deno` on Docker Hub with several tag variants:

- `denoland/deno:latest` -- Latest stable release
- `denoland/deno:alpine` -- Alpine-based smaller image
- `denoland/deno:distroless` -- Google's distroless-based image
- `denoland/deno:ubuntu` -- Ubuntu-based image
- `denoland/deno:1.x` -- Specific version tags

Key Docker patterns include multi-stage builds for smaller production images, explicit permission flags in `CMD`, development containers with `--watch`, and workspace containerization for monorepos.

# Prerequisites

- **deno-cli** -- Understanding Deno commands and permission flags for Dockerfile CMD.
- **deno-run** -- Most Dockerfiles use `deno run` or `deno serve` as the entry command.

# Key Properties

1. **Official images** -- Multiple base variants (debian, alpine, distroless, ubuntu).
2. **Multi-stage builds** -- Separate build and production stages for smaller images.
3. **Permission flags in CMD** -- Explicit `--allow-*` flags enforce the principle of least privilege.
4. **Development containers** -- `--watch` flag for hot-reload during development.
5. **Environment variables** -- `DENO_DIR`, `DENO_INSTALL_ROOT`, `DENO_NO_UPDATE_CHECK`, `DENO_NO_PROMPT`.
6. **Workspace support** -- Full workspace or minimal workspace containerization strategies for monorepos.
7. **Health checks** -- `deno eval` with `fetch` for container health checking.
8. **Security** -- Run as non-root user; use `--deny-*` flags for additional restriction.

# Construction / Recognition

## Basic Dockerfile:
```dockerfile
FROM denoland/deno:latest
WORKDIR /app
COPY . .
RUN deno install --entrypoint main.ts
CMD ["deno", "run", "--allow-net", "main.ts"]
```

## Multi-stage build:
```dockerfile
FROM denoland/deno:latest AS builder
WORKDIR /app
COPY . .
RUN deno install --entrypoint main.ts

FROM denoland/deno:latest
WORKDIR /app
COPY --from=builder /app .
CMD ["deno", "run", "--allow-net", "main.ts"]
```

## Development container:
```dockerfile
FROM denoland/deno:latest
WORKDIR /app
COPY . .
CMD ["deno", "run", "--watch", "--allow-net", "main.ts"]
```

# Context & Application

- **Production deployment**: Multi-stage builds with explicit permissions for minimal, secure containers.
- **Development**: Volume-mounted containers with `--watch` for live development.
- **CI/CD**: Docker-based CI pipelines using official Deno images.
- **Monorepos**: Workspace containerization with selective copying of workspace members.

# Examples

**Example 1** (from source): Docker Compose for development.
```yaml
version: "3.8"
services:
  deno-app:
    build: .
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    command: ["deno", "run", "--watch", "--allow-net", "main.ts"]
```
(Section: "Using Docker Compose")

**Example 2** (from source): Health check.
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD deno eval "try { await fetch('http://localhost:8000/health'); } catch { Deno.exit(1); }"
```
(Section: "Health Checks")

**Example 3** (from source): Non-root user security.
```dockerfile
RUN addgroup --system deno && \
    adduser --system --ingroup deno deno
USER deno
```
(Section: "Security Considerations")

# Relationships

## Builds Upon
- **deno-cli** -- Docker CMD invokes Deno CLI commands.
- **deno-run** -- Most containers run `deno run` or `deno serve`.

## Enables
- Containerized Deno application deployment.
- Reproducible development environments.

## Related
- **deno-serve** -- Common CMD target for web server containers.
- **deno-in-ci** -- Docker images can be used in CI pipelines.
- **deno-compile** -- Compiled binaries can simplify Docker images (copy just the binary).

# Common Errors

- **Error**: Permission denied errors in Docker.
  **Correction**: Use appropriate `--allow-*` flags in the CMD instruction.

- **Error**: Large Docker image sizes.
  **Correction**: Use multi-stage builds, proper `.dockerignore`, and include only necessary files.

- **Error**: Cache invalidation on every build.
  **Correction**: Separate dependency installation (`deno install`) from source copying; use proper layer ordering.

# Common Confusions

- **Confusion**: The distroless image variant includes a shell for debugging.
  **Clarification**: Distroless images contain only the runtime; they have no shell, package manager, or other OS utilities.

# Source Reference

- runtime/reference/docker.md: Full Docker documentation including Dockerfiles, multi-stage builds, Docker Compose, health checks, security, workspace containerization.

# Verification Notes

- High confidence: Comprehensive documentation with Dockerfiles, Docker Compose, and security patterns directly from source.
- All image tag variants listed directly from source.
