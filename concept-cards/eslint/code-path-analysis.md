---
# === CORE IDENTIFICATION ===
concept: Code Path Analysis
slug: code-path-analysis

# === CLASSIFICATION ===
category: ast-analysis
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/code-path-analysis.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "code path"
  - "CodePath"
  - "CodePathSegment"
  - "execution path analysis"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - custom-rules
extends:
  - custom-rules
related:
  - ast-selectors
  - rule-context-object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does ESLint model execution paths through code?"
  - "What are CodePath and CodePathSegment objects?"
  - "What events are available for tracking code paths in rules?"
  - "How do you detect unreachable code using code path analysis?"
---

# Quick Definition
Code path analysis is ESLint's system for modeling execution routes through a program, using `CodePath` objects (representing whole execution paths per function/global) and `CodePathSegment` objects (representing individual segments that fork and merge at control flow points).

# Core Definition
ESLint models program execution as code paths that fork and join at control flow structures like `if`, `while`, `try/catch`, and `switch`. A program has multiple code paths -- one per function and one for the global scope.

**CodePath** represents an entire code path with properties:
- `id` (string): unique identifier
- `origin` (string): `"program"`, `"function"`, `"class-field-initializer"`, or `"class-static-block"`
- `initialSegment`: the starting segment
- `finalSegments`: all final segments (returned and thrown)
- `returnedSegments` / `thrownSegments`: subsets of final segments
- `upper`: parent code path (or null for global)
- `childCodePaths`: nested function code paths

**CodePathSegment** represents a portion of a code path (similar to a doubly linked list with forking/merging):
- `id` (string): unique identifier
- `nextSegments` / `prevSegments`: arrays of connected segments
- `reachable` (boolean): false after `return`, `throw`, `break`, `continue`

# Prerequisites
- Understanding of custom rules and AST traversal

# Key Properties
1. **Seven events** -- onCodePathStart, onCodePathEnd, onCodePathSegmentStart, onCodePathSegmentEnd, onUnreachableCodePathSegmentStart, onUnreachableCodePathSegmentEnd, onCodePathSegmentLoop
2. **CodePath** -- Represents whole execution path for a function or global scope
3. **CodePathSegment** -- Individual segment with reachability flag and prev/next connections
4. **Forking/merging** -- Segments fork at conditionals and merge at join points
5. **Loop event** -- onCodePathSegmentLoop fires when a looping path connects to an existing segment
6. **Shared instances** -- CodePath and CodePathSegment are shared across rules and must not be modified

# Construction / Recognition
```js
create(context) {
    let currentSegments;
    const allCurrentSegments = [];
    return {
        onCodePathStart(codePath) {
            allCurrentSegments.push(currentSegments);
            currentSegments = new Set();
        },
        onCodePathEnd(codePath) {
            currentSegments = allCurrentSegments.pop();
        },
        onCodePathSegmentStart(segment) { currentSegments.add(segment); },
        onCodePathSegmentEnd(segment) { currentSegments.delete(segment); },
        onUnreachableCodePathSegmentStart(segment) { currentSegments.add(segment); },
        onUnreachableCodePathSegmentEnd(segment) { currentSegments.delete(segment); },
        ExpressionStatement(node) {
            if (!areAnySegmentsReachable(currentSegments)) {
                context.report({ message: "Unreachable!", node });
            }
        }
    };
}
```

# Context & Application
Code path analysis powers rules like `no-unreachable`, `no-fallthrough`, and `consistent-return`. It enables detecting whether a callback is called in every execution path, whether all branches return a value, or whether code after a `throw`/`return` is reachable. The analysis handles all JavaScript control flow: if/else, switch, while, do-while, for, for-in, try-catch-finally.

# Examples
From extend/code-path-analysis.md:
- Finding unreachable nodes: check `segment.reachable` for all current segments at any node
- Verifying callback called in every path: use `codePath.finalSegments.every()` at `onCodePathEnd`
- Loop handling: `onCodePathSegmentLoop(fromSegment, toSegment, node)` fires when looping back to existing segments

# Relationships
## Part Of
- custom-rules (code path events are defined alongside visitor methods in create())

## Related
- ast-selectors
- scope-manager

# Common Errors
1. Modifying CodePath or CodePathSegment instances -- these are shared across all rules
2. Only tracking reachable segments -- must also handle unreachable segments via the unreachable events
3. Forgetting to manage a stack for nested code paths -- each function creates a new code path

# Source Reference
- extend/code-path-analysis.md: CodePath/CodePathSegment interfaces, seven events, usage examples with loops, if/else, try/catch

# Verification Notes
- High confidence: all events and properties enumerated directly from the documentation
