---
# === CORE IDENTIFICATION ===
concept: CommonJS Module
slug: commonjs-module

# === CLASSIFICATION ===
category: modularity
subcategory: module-systems
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Modules"
chapter_number: 10
pdf_page: null
section: "CommonJS modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - CJS
  - require/exports

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module
  - function
extends:
  - module
related:
  - es-module
  - npm
  - dependency
contrasts_with:
  - es-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is CommonJS?"
  - "What must I know before writing a module system?"
---

# Quick Definition
CommonJS is an older module system where modules use `require()` to load dependencies and `exports` to define their interface, with `require` being a runtime function call rather than a static declaration.

# Core Definition
Haverbeke explains: "A CommonJS module looks like a regular script, but it has access to two bindings that it uses to interact with other modules. The first is a function called `require`. When you call this with the module name of your dependency, it makes sure the module is loaded and returns its interface. The second is an object named `exports`, which is the interface object for the module." (Ch 10, "CommonJS modules")

# Prerequisites
- **Modules**: Understanding the module concept
- **Functions**: `require` is a function; modules are wrapped in functions

# Key Properties
1. Uses `require()` function to load dependencies
2. Uses `exports` object to define interface
3. `require` is a runtime call (can appear in conditionals, loops)
4. Module code is wrapped in a function for scope isolation
5. Modules are cached after first load
6. Node.js originally used CommonJS (now also supports ES modules)

# Construction / Recognition
```javascript
const ordinal = require("ordinal");
const {days, months} = require("date-names");

exports.formatDate = function(date, format) { ... };
```

# Context & Application
CommonJS was the community solution before ES modules existed. While still encountered in older code, "there is no real reason to write new programs in this style anymore." (Ch 10)

# Examples
```javascript
const ordinal = require("ordinal");
const {days, months} = require("date-names");

exports.formatDate = function(date, format) {
  return format.replace(/YYYY|M(MMM)?|Do?|dddd/g, tag => {
    if (tag == "YYYY") return date.getFullYear();
    if (tag == "MMMM") return months[date.getMonth()];
    if (tag == "Do") return ordinal(date.getDate());
    if (tag == "dddd") return days[date.getDay()];
  });
};
```
(Ch 10, "CommonJS modules", lines 377-391)

# Relationships
## Builds Upon
- module, function
## Enables
- Understanding of legacy Node.js code
## Related
- npm, dependency
## Contrasts With
- es-module (ES module imports are static; CommonJS require is dynamic)

# Common Errors
- **Error**: Writing new code using CommonJS when ES modules are available
  **Correction**: Prefer ES modules for new code; CommonJS is legacy

# Common Confusions
- **Confusion**: CommonJS and ES modules are interchangeable
  **Clarification**: "ES module imports happen before a module's script starts running, whereas `require` is a normal function, invoked when the module is already running." (Ch 10)

# Source Reference
Chapter 10: Modules, Section "CommonJS modules", lines 307-481.

# Verification Notes
- Definition source: direct
- Confidence rationale: Extensively explained with implementation details
- Cross-reference status: verified
