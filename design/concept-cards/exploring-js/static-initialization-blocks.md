---
concept: Static Initialization Blocks
slug: static-initialization-blocks
category: classes
subcategory: static
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.6.4 Static initialization blocks in classes"
extraction_confidence: high
aliases:
  - "static block"
  - "class static block"
prerequisites:
  - static-members
extends: []
related:
  - constructor-method
contrasts_with: []
answers_questions:
  - "How do I run complex initialization code when a class is created?"
---

# Quick Definition

Static initialization blocks (ES2022) are `static { ... }` blocks inside class bodies that execute when the class is created, with access to private slots.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, static blocks are the static counterpart of constructors: they run once when the class is created, not per instance. Multiple static blocks per class are allowed. Their execution is interleaved with static field initializers. Superclass static members execute before subclass static members. They have access to private slots.

# Prerequisites

- Static members

# Key Properties

1. Introduced in ES2022.
2. Executed once when the class is created.
3. Multiple blocks allowed per class.
4. Interleaved with static field initializers.
5. Superclass static members run before subclass.
6. Has access to private slots.

# Construction / Recognition

```js
class Translator {
  static translations = { yes: 'ja', no: 'nein' };
  static englishWords = [];
  static {
    for (const [en, de] of Object.entries(this.translations)) {
      this.englishWords.push(en);
    }
  }
}
```

# Context & Application

Use for complex static initialization that requires multiple statements or access to private slots.

# Examples

From the source text (Ch. 31, section 31.6.4):

```js
class Translator {
  static translations = { yes: 'ja', no: 'nein', maybe: 'vielleicht' };
  static englishWords = [];
  static germanWords = [];
  static {
    for (const [english, german] of Object.entries(this.translations)) {
      this.englishWords.push(english);
      this.germanWords.push(german);
    }
  }
}
```

# Relationships

## Builds Upon
- **Static Members** -- static blocks are a kind of static member

## Related
- **Constructor Method** -- instance-level equivalent

# Source Reference

Chapter 31: Classes, Section 31.6.4, lines 1986-2077.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit rules and execution order
- Cross-reference status: verified
