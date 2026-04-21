# Gio UI Framework

Guidelines for building desktop and embedded UIs with Gio (`gioui.org`), an immediate-mode retained-op GPU-accelerated UI framework for Go. Covers window construction, widget state lifecycle, theme allocation, platform-specific threading (notably macOS Cocoa), keyboard and pointer input routing, scroll event bounds, and overlay event propagation.

These patterns fall outside the scope of Uber and Google's Go style guides (which do not address UI frameworks) and are collected from the `claude-skill-golang` workbench repo (darrenoakey). Gio's API is deliberately small, but its immediate-mode/retained-op hybrid has non-obvious event-routing rules that show up only at runtime — this chapter captures the recurring surprises.


## GI-01: Construct Windows with new(app.Window) + Option(), Not app.NewWindow()

**Strength**: MUST

**Summary**: A Gio window is a zero-value struct configured post-construction. There is no `app.NewWindow(...)` factory; code that calls it fails to compile.

```go
// Bad — app.NewWindow does not exist in Gio
win := app.NewWindow(app.Title("My App"), app.Size(unit.Dp(800), unit.Dp(600)))

// Good — new() the struct, then Option() to configure
win := new(app.Window)
win.Option(app.Title("My App"), app.Size(unit.Dp(800), unit.Dp(600)))
```

**Rationale**: Gio exposes `app.Window` as a zero-value struct that is configured by calling `Option()` on the instance. The commonly-assumed `app.NewWindow()` factory that other UI toolkits (and LLM-generated boilerplate) suggest does not exist in Gio's public API (paraphrased from `claude-skill-golang/skills/GIO_UI.md`).

**See also**: GI-03

---

## GI-02: Persist Widgets as Struct Fields, Not Per-Frame Locals

**Strength**: MUST

**Summary**: Gio's event system routes by pointer identity of the registered target; a fresh `widget.Clickable{}` each frame is a new tag, and all events for it are silently dropped.

```go
// Bad — new Clickable each frame; clicks never register
func (w *Window) layout(gtx layout.Context) layout.Dimensions {
    btn := widget.Clickable{}
    return material.Button(th, &btn, "Click").Layout(gtx)
}

// Good — persistent field on the containing struct
type Window struct {
    btn widget.Clickable
}
func (w *Window) layout(gtx layout.Context) layout.Dimensions {
    return material.Button(th, &w.btn, "Click").Layout(gtx)
}
```

For dynamic collections, use a persistent map keyed by a stable ID (e.g. `map[string]*widget.Clickable`) and prune stale entries to avoid unbounded growth.

**Rationale**: Although Gio's rendering model is immediate-mode, event routing is retained — each registered target's pointer identity must survive across frames. A widget allocated inside the frame handler has a fresh address that was never registered, so click, hover, and edit events for it have nowhere to go (paraphrased from `claude-skill-golang/skills/GIO_GOTCHAS.md`).

**See also**: GI-03, GI-07

---

## GI-03: Allocate material.NewTheme() Once at Construction, Never Per Frame

**Strength**: MUST

**Summary**: A theme owns a text shaper and a font cache. Creating a new one inside the frame handler rebuilds those structures on every repaint.

```go
// Bad — allocates on every frame
func (w *Window) layout(gtx layout.Context) layout.Dimensions {
    th := material.NewTheme()
    // ... build widgets from th
}

// Good — constructed once, stored as a field
type Window struct {
    theme *material.Theme
}
func NewWindow() *Window {
    return &Window{theme: material.NewTheme()}
}
```

**Rationale**: `material.NewTheme()` allocates a text shaper and font cache. Since the frame handler re-runs on every repaint in an immediate-mode loop, per-frame allocation rebuilds these heavy structures continuously and degrades performance noticeably on content-heavy UIs (paraphrased from `claude-skill-golang/skills/GIO_GOTCHAS.md`).

**See also**: GI-01, GI-02

---

## GI-04: On macOS, Run Blocking Work in a Goroutine + Invalidate()

**Strength**: MUST

**Summary**: The Gio frame handler owns the Cocoa main thread on macOS. Any operation that re-dispatches to the main thread — subprocesses, cross-window `Option()` calls, blocking I/O — deadlocks unless offloaded.

```go
// Bad — deadlock on macOS inside a frame handler
func (w *Window) layout(gtx layout.Context) layout.Dimensions {
    if w.btn.Clicked(gtx) {
        exec.Command("open", url).Run() // blocks the main thread
    }
}

// Good — goroutine for anything blocking, then Invalidate to trigger repaint
func (w *Window) layout(gtx layout.Context) layout.Dimensions {
    if w.btn.Clicked(gtx) {
        go func() {
            exec.Command("open", url).Run()
            w.win.Invalidate()
        }()
    }
}
```

**Rationale**: Because Cocoa serializes all GUI work on the main thread and the frame handler holds that thread during layout, any call that itself requires the main thread waits forever. Offloading to a goroutine frees the frame handler; `window.Invalidate()` then schedules a follow-up repaint safely (paraphrased from `claude-skill-golang/skills/GIO_GOTCHAS.md`).

---

## GI-05: Register key.Filter{Name: key.NameTab} Explicitly Alongside the Catch-All

**Strength**: MUST

**Summary**: Tab is delivered as a system event that the empty-name catch-all filter does not match; without an explicit Tab filter, Gio's focus navigation consumes the key silently.

```go
// Bad — Tab silently consumed by focus navigation
key.Filter{Name: "", Optional: key.ModShift | key.ModCtrl}

// Good — register both filters
key.Filter{Name: key.NameTab}                                // explicit Tab
key.Filter{Name: "", Optional: key.ModShift | key.ModCtrl}   // everything else
```

**Rationale**: Gio reserves Tab for focus navigation and emits it as a `key.Event` with `Modifiers` set to `key.ModFunction`. The empty-name catch-all filter does not match these system events, so Tab never reaches the consumer unless a named filter is also registered (paraphrased from `claude-skill-golang/skills/GIO_GOTCHAS.md`).

**See also**: GI-09

---

## GI-06: Give pointer.InputOp Non-Zero ScrollY/ScrollX Bounds

**Strength**: MUST

**Summary**: `pointer.InputOp{Types: pointer.Scroll}` with default (zero) scroll bounds drops every scroll event. Always set a non-empty `ScrollRange`.

```go
// Bad — scroll events silently dropped
pointer.InputOp{Tag: w, Types: pointer.Scroll}

// Good — bounds matching the scrollable content range (or a wide sentinel)
pointer.InputOp{
    Tag:     w,
    Types:   pointer.Scroll,
    ScrollY: pointer.ScrollRange{Min: -1e6, Max: 1e6},
}
```

**Rationale**: Gio's pointer filter silently rejects scroll events when `ScrollY` or `ScrollX` bounds equal `{Min: 0, Max: 0}` (the zero value). Providing a wide range — or one calibrated to the actual content — ensures scroll deltas are delivered (paraphrased from `claude-skill-golang/skills/GIO_GOTCHAS.md`).

---

## GI-07: Combine Pointer Event Types into One InputOp — Later Calls Replace, Not Merge

**Strength**: MUST

**Summary**: Multiple `pointer.InputOp` calls for the same tag do not accumulate; only the last registration wins. OR-combine event types into a single call.

```go
// Bad — only the last registration wins, Press never arrives
pointer.InputOp{Tag: w, Types: pointer.Press}
pointer.InputOp{Tag: w, Types: pointer.Release}

// Good — combine with bitwise OR
pointer.InputOp{
    Tag:   w,
    Types: pointer.Press | pointer.Drag | pointer.Release | pointer.Scroll,
}
```

**Rationale**: A later `pointer.InputOp` for a given tag replaces the earlier one rather than composing with it. Splitting types across multiple calls discards all but the final registration (paraphrased from `claude-skill-golang/skills/GIO_GOTCHAS.md`).

**See also**: GI-02, GI-08

---

## GI-08: Wrap Full-Window Dismiss Overlays in pointer.PassOp

**Strength**: MUST

**Summary**: A full-screen overlay (e.g. click-outside-to-dismiss for a context menu) sits on top of the op tree and consumes every pointer event unless wrapped in `pointer.PassOp`.

```go
// Bad — bg overlay blocks all events to handlers underneath
bgArea := clip.Rect{Max: gtx.Constraints.Max}.Push(gtx.Ops)
event.Op(gtx.Ops, &m.bgTag)
bgArea.Pop()

// Good — PassOp lets events pass through to underlying handlers
passStack := pointer.PassOp{}.Push(gtx.Ops)
bgArea := clip.Rect{Max: gtx.Constraints.Max}.Push(gtx.Ops)
event.Op(gtx.Ops, &m.bgTag)
bgArea.Pop()
passStack.Pop()
```

**Rationale**: Without `PassOp`, the overlay produces the classic "click-to-dismiss, next-click-does-nothing" bug because the row underneath never sees the follow-up click. `pointer.PassOp` lets events propagate through the overlay to handlers below while still allowing the overlay's own tag to receive the dismiss click (paraphrased from `claude-skill-golang/skills/GIO_PATTERNS.md`).

**See also**: GI-07

---

## GI-09: Switch on Both key.Event (for Shortcuts) and key.EditEvent (for Text)

**Strength**: MUST

**Summary**: `key.Event.Name` is always uppercase and ignores shift/dead-keys/IME. Use it for shortcuts; use `key.EditEvent.Text` for correctly composed text input.

```go
// Bad — only reading key.Event; typed text is wrong for shift/dead-keys/IME
for {
    e, ok := gtx.Event(
        key.Filter{Name: "", Optional: key.ModShift | key.ModCtrl | key.ModCommand},
    )
    if !ok { break }
    if ev, ok := e.(key.Event); ok && ev.State == key.Press {
        insert(ev.Name) // wrong: always uppercase, ignores IME / dead keys
    }
}

// Good — dispatch to the right event type
for {
    e, ok := gtx.Event(
        key.Filter{Name: key.NameTab},
        key.Filter{Name: "", Optional: key.ModShift | key.ModCtrl | key.ModCommand},
    )
    if !ok { break }
    switch e := e.(type) {
    case key.Event:
        if e.State != key.Press { continue }
        // e.Name is UPPERCASE: "A", "Return", "Escape", "Tab"
        // Handle shortcuts here; apply e.Modifiers for case/shift logic if needed.
    case key.EditEvent:
        // e.Text is the correctly composed character — use for text insertion.
    }
}
```

**Rationale**: `key.Event.Name` reflects the raw keyboard key rather than the typed character, so relying on it for text input produces wrong case and breaks dead-key and IME composition. `key.EditEvent.Text` carries the composed character. Shortcuts and navigation still belong on `key.Event`, so both must be switched on inside the event loop (paraphrased from `claude-skill-golang/skills/GIO_GOTCHAS.md`).

**See also**: GI-05

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `new(app.Window)` + `Option()` | MUST | No `app.NewWindow()` constructor exists |
| 02 | Persistent widget fields | MUST | Event routing matches by pointer identity |
| 03 | Theme allocated once | MUST | Text shaper + font cache are heavy |
| 04 | macOS: goroutine + Invalidate | MUST | Frame handler holds the Cocoa main thread |
| 05 | Explicit `key.NameTab` filter | MUST | Catch-all filter misses system events |
| 06 | Non-zero scroll bounds | MUST | Zero `ScrollRange` drops scroll events |
| 07 | One `pointer.InputOp` per tag | MUST | Later calls replace, not merge |
| 08 | `PassOp` around dismiss overlays | MUST | Otherwise the overlay steals every click |
| 09 | Handle both `key.Event` and `key.EditEvent` | MUST | Shortcuts vs composed text |

### When to Reach for Each Pattern

- **Starting a new Gio app**: GI-01, GI-02, GI-03 are the three that bite first.
- **Cross-platform support** (macOS in particular): GI-04 will save hours.
- **Keyboard-heavy UIs** (editors, terminals): GI-05 and GI-09 together.
- **Pointer-driven interactions** (drag, menu, scroll): GI-06, GI-07, GI-08.

## Related Guidelines

- Chapter 06 (Concurrency) — for the goroutine spawn in GI-04.
- Chapter 02 (API Design) — for functional options, which contrasts with Gio's `Option()` method style in GI-01.
- Chapter 04 (Type Design) — for the persistent-field discipline in GI-02.

## External References

- Gio documentation: https://gioui.org
- Gio source repository: https://git.sr.ht/~eliasnaur/gio
- `claude-skill-golang` workbench repo (darrenoakey): skill bundle this chapter is distilled from.
