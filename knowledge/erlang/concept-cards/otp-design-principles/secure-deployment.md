---
# === CORE IDENTIFICATION ===
concept: Secure Deployment
slug: secure-deployment

# === CLASSIFICATION ===
category: production-ops
subcategory: deployment
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Rules / Secure Coding Standard"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Erlang deployment hardening"
  - "DEP-002 through DEP-006"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
extends: []
related:
  - distribution-security
  - crypto-application-security
  - application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should Erlang/OTP be built for production use?"
  - "Why should you build Erlang/OTP yourself instead of using prebuilt images?"
  - "What is interactive vs embedded mode and which should be used in production?"
  - "How should the code path be protected?"
  - "What privileges should the Erlang VM run with?"
  - "Why should maintained OTP versions be used?"
---

# Quick Definition

Secure deployment of Erlang/OTP systems requires building Erlang yourself (not relying on external tools), using actively maintained versions, protecting the code path, running in `embedded` mode (not `interactive`), minimizing VM privileges, and avoiding debug functionality in production. These rules range from Critical to Medium priority.

# Core Definition

The Secure Coding Guidelines define five deployment rules (DEP-002 through DEP-006) covering the secure build and deployment of Erlang/OTP systems. DEP-002 (priority: High) states that Erlang/OTP should be built by the user themselves because "tools like kerl and asdf or prebuilt docker images are convenient, they sometimes patch Erlang/OTP or set CFLAGS/LDFLAGS themselves, which has caused problems." DEP-003 (priority: Critical) requires using an actively maintained version. DEP-004 (priority: Medium) addresses code path protection. DEP-005 (priority: Critical) warns against `interactive` mode in production. DEP-006 (priority: Medium) requires minimizing VM privileges.

# Prerequisites

- **Erlang Threat Model** -- understanding that all loaded code is trusted motivates securing the code path and build process.

# Key Properties

1. **Build Erlang/OTP yourself** (DEP-002, High) -- external build tools sometimes patch OTP or set problematic CFLAGS/LDFLAGS. The `--enable-pie` configure argument should be used instead of passing `pie` options in CFLAGS/LDFLAGS (which conflicts with `pic` for shared libraries).
2. **C/C++ hardening flags** -- as of Erlang/OTP 28.0, the configure script enables most hardening flags recommended by the Open Source Security Foundation. Use `V=1` during build to verify.
3. **Up-to-date OpenSSL** -- use `--with-ssl=PATH` to specify the OpenSSL installation and `--disable-dynamic-ssl-lib` to statically link `libcrypto`.
4. **Use maintained versions** (DEP-003, Critical) -- the OTP Versions Tree page has maintenance status and CVE information. VEX documents are regularly updated. Patches announced on `erlang-announce` mailing list and erlang forums.
5. **Protect the code path** (DEP-004, Medium) -- code path folders should only be writable by a dedicated user separate from the user running the VM (CWE-427).
6. **Avoid interactive mode** (DEP-005, Critical) -- `interactive` mode loads code on demand, making it easy to trigger code loading. Use `embedded` mode in production.
7. **Minimize VM privileges** (DEP-006, Medium) -- run under a dedicated user; further restrict through SELinux/AppArmor, containerization, etc.
8. **Avoid debug functionality** (MSC-007, Critical) -- functions like `erlang:list_to_pid/1` and the `keep_secrets` ssl option should not be used in production; debug functionality may be unstable and have adverse scheduling effects.
9. **Do not use undocumented functionality** (DSG-004, Critical) -- undocumented functions "can cause the system to behave in unexpected ways" and may change without notice.
10. **Do not use deprecated functionality** (DSG-005, Medium) -- deprecation may be for security reasons; always check for and migrate to replacement functionality.

# Construction / Recognition

## Build Configuration:
```bash
# Build with proper hardening
./configure --enable-pie --with-ssl=/path/to/openssl --disable-dynamic-ssl-lib

# Verify hardening flags during build
make V=1

# Do NOT set pie in CFLAGS (conflicts with shared libraries)
# WRONG: CFLAGS="-fpie" LDFLAGS="-pie" ./configure
```

## Runtime Configuration:
```bash
# Use embedded mode in production
erl -mode embedded

# Disable EPMD if not needed
erl -start_epmd false
```

## Privilege Minimization:
```bash
# Run under dedicated user
sudo -u erlang_app erl -mode embedded ...

# Consider additional restrictions:
# - SELinux/AppArmor profiles
# - Container isolation
# - Read-only code path mounts
```

# Context & Application

These deployment rules collectively address the supply chain security concern (OWASP A03:2025, A08:2025) and the trusted-code assumption in the Erlang threat model. Since all loaded BEAM code is fully trusted, securing the build pipeline, code path, and runtime environment is essential. The `interactive` mode is particularly dangerous because it loads code on demand, lowering the bar for an attacker who has write access to the code path. The emphasis on building Erlang/OTP yourself (rather than using third-party tools) reflects a security-conscious approach to the software supply chain where even well-intentioned modifications can introduce vulnerabilities.

# Examples

**Example 1** (secure_coding.md, DEP-002): "Some guides recommend passing the pie options (position independent executables), which should not be passed in CFLAGS and LDFLAGS since it might conflict with the pic (position independent code) options used when building shared libraries. In order to build position independent executables, you instead want to pass the --enable-pie configure argument."

**Example 2** (secure_coding.md, DEP-004): "If a malicious actor can write to a folder in the code path used by the Erlang VM (either the Erlang code path or the host system's shared library load path), and they have the capability to coerce the system into loading that code (made worse by interactive mode, see DEP-005), then it is possible for an attacker to load malicious code."

**Example 3** (secure_coding.md, DEP-005): "interactive mode loads code on demand, making it easy to trigger code loading. There is generally little reason to use this mode outside of development, so consider using embedded mode instead."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- the trusted-code assumption motivates all deployment security measures

## Enables
- No concepts directly enabled.

## Related
- **Distribution Security** -- distribution hardening (DEP-001) is the most critical deployment rule, covered in its own card
- **Crypto Application Security** -- the build process must ensure proper OpenSSL linkage
- **application** -- embedded vs interactive mode affects how OTP applications load code

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Using `kerl`, `asdf`, or prebuilt Docker images without verifying the build configuration.
  **Correction**: Build Erlang/OTP yourself following the official installation guide. External tools "sometimes patch Erlang/OTP or set CFLAGS/LDFLAGS themselves, which has caused problems in some cases."

- **Error**: Running an Erlang production system in `interactive` mode.
  **Correction**: Use `embedded` mode (`erl -mode embedded`). Interactive mode "loads code on demand, making it easy to trigger code loading" and is a Critical-priority security concern.

- **Error**: Running the VM as root or with more privileges than necessary.
  **Correction**: "The virtual machine should run with the fewest possible privileges your system needs." Use a dedicated user and consider SELinux/AppArmor, containerization.

- **Error**: Passing `-fpie` and `-pie` in CFLAGS/LDFLAGS.
  **Correction**: Use `--enable-pie` as a configure argument instead. CFLAGS/LDFLAGS apply to both executables and shared libraries, and `pie` conflicts with `pic` options for shared libraries.

# Common Confusions

- **Confusion**: Thinking that using a recent OTP version means it is secure.
  **Clarification**: The version must be actively maintained. Check the OTP Versions Tree page for maintenance status and CVEs. Even recent releases may have known vulnerabilities if they are no longer maintained.

- **Confusion**: Believing that containerization alone provides sufficient security.
  **Clarification**: Containerization is one layer of defense. The code path, build configuration, code loading mode, and VM privileges must all be addressed. Defense in depth is required.

# Source Reference

OTP Design Principles, Secure Coding Guidelines: DEP-002 (secure_coding.md, lines 603-656), DEP-003 (lines 658-675), DEP-004 (lines 677-693), DEP-005 (lines 695-704), DEP-006 (lines 706-718), DSG-004 (lines 855-875), DSG-005 (lines 877-890), DSG-006 (lines 892-901), MSC-007 (lines 1338-1358).

# Verification Notes

- Definition source: Synthesized from DEP-002 through DEP-006, DSG-004, DSG-005, DSG-006, and MSC-007 rules.
- Confidence rationale: High -- multiple rules with explicit priority ratings and clear guidance.
- Uncertainties: None.
- Cross-reference status: References OWASP A03:2025, A08:2025, A06:2025, CWE-242, CWE-427, CWE-477, CWE-489, CWE-676.
