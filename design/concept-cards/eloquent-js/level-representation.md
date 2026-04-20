---
concept: Level Representation
slug: level-representation
category: application-architecture
subcategory: game-design
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Levels"
extraction_confidence: high
aliases:
  - level plan
  - tile map
prerequisites:
  - array
  - string
extends: []
related:
  - actor-pattern
  - game-state
contrasts_with: []
answers_questions:
  - "How can game levels be defined in a human-readable format?"
  - "How do you parse a text-based level into a data structure?"
---

# Quick Definition
A level representation uses a multiline string where each character maps to a grid element (wall, empty space, lava) or a moving actor (player, coin), which is then parsed into arrays of tile types and actor objects.

# Core Definition
Haverbeke describes the approach: "We'll want a human-readable, human-editable way to specify levels. Since it is okay for everything to start out on a grid, we could use big strings in which each character represents an element -- either a part of the background grid or a moving element" (Ch. 16, "Levels"). The `Level` class parses these plans into a `rows` array of background types and a `startActors` array of moving entities.

# Prerequisites
- **Strings**: Level plans are multiline strings
- **Arrays**: Parsed into 2D arrays of tile types

# Key Properties
1. Characters map to background types or actor classes via `levelChars`
2. Background grid is stored as a 2D array of strings ("empty", "wall", "lava")
3. Actors are extracted and stored separately from the grid
4. Width and height are derived from the plan dimensions

# Construction / Recognition
```javascript
let simpleLevelPlan = `
......................
..#................#..
..#..............=.#..
..#.........o.o....#..
..#.@......#####...#..
..#####............#..
......#++++++++++++#..
......##############..
......................`;
```
Characters: `.` = empty, `#` = wall, `+` = lava, `@` = player, `o` = coin, `=` `|` `v` = moving lava.

# Context & Application
Text-based level representation is common in 2D games. It makes levels easy to create and edit without specialized tools, and maps naturally to grid-based game worlds.

# Examples
The Level constructor parses the plan:
```javascript
class Level {
  constructor(plan) {
    let rows = plan.trim().split("\n").map(l => [...l]);
    this.height = rows.length;
    this.width = rows[0].length;
    this.startActors = [];
    this.rows = rows.map((row, y) => {
      return row.map((ch, x) => {
        let type = levelChars[ch];
        if (typeof type != "string") {
          let pos = new Vec(x, y);
          this.startActors.push(type.create(pos, ch));
          type = "empty";
        }
        return type;
      });
    });
  }
}
```

# Relationships
## Builds Upon
- string, array, class-declaration
## Enables
- game-state, collision-detection, display rendering
## Related
- actor-pattern, vector
## Contrasts With
- Binary level formats, JSON-based level editors

# Common Errors
- **Error**: Forgetting that actor positions replace their grid cell with "empty"
  **Correction**: When a character maps to an actor class, the background cell becomes "empty"

# Common Confusions
- **Confusion**: The level plan string IS the runtime level data
  **Clarification**: The string is parsed once into structured data (rows + actors); the game operates on the parsed data

# Source Reference
Chapter 16: Project: A Platform Game, Section "Levels" and "Reading a level", lines 116-213 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Full code and explanation provided
- Cross-reference status: verified
