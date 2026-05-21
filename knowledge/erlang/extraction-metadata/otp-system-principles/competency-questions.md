# Competency Questions for OTP System Principles (System Documentation)

> Source: "OTP System Principles" — Ericsson/OTP Team
> Canonical extraction input: `knowledge/erlang/sources/md/otp-system-principles/`

## Definitional (What is X?)
1. What is a boot script in Erlang/OTP?
2. What is a target system?
3. What is embedded mode vs interactive mode for code loading?
4. What is the OTP version scheme?
5. What is a release in the context of OTP versioning?
6. What is the Logger in Erlang/OTP?
7. What is a release upgrade file (relup)?
8. What is an application upgrade file (.appup)?
9. What is the code path in Erlang/OTP?
10. What is start_erl?
11. What is the OTP deprecation policy?

## Relational (How does X relate to Y?)
1. How do boot scripts relate to release resource files (.rel)?
2. How does embedded mode differ from interactive mode?
3. How does a basic target system differ from a simple or embedded target system?
4. How does the OTP version relate to application versions?
5. How does restart_new_emulator differ from restart_emulator?
6. How does Logger relate to SASL error logging?
7. How do maintenance patches relate to emergency patches?
8. How does the code path relate to code loading strategy?

## Procedural (How do I do X?)
1. How do I start/stop/restart an Erlang runtime system?
2. How do I create a target system?
3. How do I install a target system?
4. How do I upgrade a target system to a new version?
5. How do I create a user-defined boot script?
6. How do I retrieve the current OTP version?
7. How do I configure system parameters with sys.config?
8. How do I enable progress reports from OTP behaviours?
9. How do I create a release upgrade file?
10. How do I determine which OTP version includes a specific application version?

## Prerequisite (What before X?)
1. What must I understand before creating a target system?
2. What must I know before performing a release upgrade?
3. What must I understand before choosing embedded vs interactive mode?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes a .script file from a .boot file?
2. What distinguishes start_clean.boot from start_sasl.boot?
3. What distinguishes deprecation from removal in OTP?
4. What distinguishes a major version bump from a minor or patch bump?
5. What distinguishes branched versions from normal versions?
6. What distinguishes core application upgrades from other application upgrades?
7. What distinguishes run_erl from to_erl?
