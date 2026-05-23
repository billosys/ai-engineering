---
concept: tty Command-Line Interface
slug: tty-interface
category: tooling
subcategory: shell
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "tty - A Command-Line Interface"
chapter_number: null
pdf_page: null
section: "Normal Mode"
extraction_confidence: high
aliases:
  - tty
  - "Erlang shell CLI"
  - "Erlang terminal interface"
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is the Erlang tty interface?"
  - "What key bindings are available in the Erlang shell?"
  - "What modes does the Erlang shell support?"
---

# Quick Definition

`tty` is the command-line interface program for the Erlang shell, started by running `erl`. It collects and interprets keystrokes, sends completed lines to the shell, and provides Emacs-style line editing, command history, search mode, shell break mode, and autocompletion.

# Core Definition

`tty` is a "simple command-line interface program where keystrokes are collected and interpreted. Completed lines are sent to the shell for interpretation. A simple history mechanism saves previous lines, which can be edited before sending them to the shell" (Ericsson AB, "tty - A Command-Line Interface").

`tty` operates in three modes:

1. **Normal mode**: Text lines can be edited and sent to the shell using Emacs-style key bindings
2. **Search mode**: The user can search backward and forward through the history buffer for previous commands
3. **Shell break mode**: Allows killing/suspending the current shell, connecting to a suspended shell, or starting a new shell

# Prerequisites

- Basic familiarity with the Erlang shell (`erl`)

# Key Properties

1. Started automatically when Erlang is started with the `erl` command
2. Most Emacs line-editing commands are supported
3. Key notation: `C-a` = Ctrl+a, `M-f` = Esc then f (or Alt+f), `C-S-a` = Ctrl+Shift+a
4. Supports multi-line editing with `M-Enter` to insert new lines and `C-Up`/`C-Down` to navigate rows
5. `C-g` enters shell break mode for shell management
6. `C-r` enters search mode for backward history search; `C-s` searches forward
7. `Tab` or `C-i` triggers autocompletion
8. `C-o` or `M-o` opens the current line in an external editor (set via `VISUAL` or `EDITOR` environment variables)
9. `M-h` displays help for the module or function nearest to the cursor
10. `PageUp`/`PageDown` scroll the expand, search, or help buffer

# Construction / Recognition

## Essential Key Bindings (Normal Mode)

| Key | Function |
| --- | --- |
| `C-a` / `Home` | Beginning of line |
| `C-e` / `End` | End of line |
| `C-f` | Forward character |
| `C-b` | Backward character |
| `M-f` / `C-Right` | Forward word |
| `M-b` / `C-Left` | Backward word |
| `C-p` / `Up` | Previous history line |
| `C-n` / `Down` | Next history line |
| `C-d` | Delete character |
| `M-d` | Delete word |
| `C-k` | Kill to end of line |
| `C-u` | Kill to beginning of line |
| `C-w` | Backward kill word |
| `C-y` | Yank (paste) killed text |
| `C-t` | Transpose characters |
| `C-l` | Clear screen |
| `M-c` | Clear current expression |
| `M-l` | Redraw line |
| `C-]` | Insert matching closing bracket |
| `M-r` | Format current expression |
| `Tab` / `C-i` | Autocomplete |
| `M-h` | Show help for module/function at cursor |
| `M-Enter` | Insert new line at cursor |
| `C-Up` / `M-Up` | Navigate up in multi-line edit |
| `C-Down` / `M-Down` | Navigate down in multi-line edit |
| `M-<` / `M-S-Up` | Go to start of expression |
| `M->` / `M-S-Down` | Go to end of expression |

## Shell Break Mode (`C-g`)

In shell break mode, the user can:
- Kill or suspend the current shell
- Connect to a suspended shell
- Start a new shell

## Search Mode (`C-r`)

- `C-r` enters search mode and searches backward through shell history
- `C-s` searches forward in the shell history
- Type characters to refine the search

# Context & Application

The `tty` interface is the primary interactive development tool for Erlang programmers. Key productivity features:

- **Multi-line editing**: `M-Enter` inserts a new line, allowing complex expressions to be composed interactively with `C-Up`/`C-Down` navigation
- **External editor integration**: `C-o` opens the current expression in `$VISUAL` or `$EDITOR` for complex editing (on Windows, the editor cannot be console-based)
- **Inline help**: `M-h` shows documentation for the function at the cursor position
- **Expression formatting**: `M-r` formats the current expression using `shell:format_shell_func/1`
- **Multiple shells**: Shell break mode (`C-g`) allows running multiple concurrent shell sessions within the same node

# Examples

**Entering and using search mode** (source: "tty - A Command-Line Interface"):

1. Press `C-r` to enter search mode
2. Type part of a previous command to search backward
3. Press `C-s` to search forward
4. Press Enter to execute the found command

**Using an external editor** (source: same):

Set the environment variable before starting the shell:
```bash
export VISUAL="emacs -nw"
erl
```
Then press `C-o` to edit the current line in Emacs.

**Shell break mode** (source: section "Shell Break Mode"):

Press `C-g` to enter break mode, where you can start new shells, kill existing ones, or connect to suspended shells.

# Relationships

(No closely related concept cards in this extraction set.)

# Common Errors

- **Error**: Trying to use a console-based editor with `C-o` on Windows
  **Correction**: On Windows, the `VISUAL`/`EDITOR` editor cannot be a console-based editor

- **Error**: Not knowing how to exit a stuck shell
  **Correction**: Press `C-g` to enter shell break mode, then use the menu options to kill the current shell or start a new one

# Common Confusions

- **Confusion**: `tty` is a separate program from the Erlang shell
  **Clarification**: `tty` is the input/editing layer that feeds into the Erlang shell; it starts automatically with `erl` and provides the line editing and history features

- **Confusion**: `C-s` freezes the terminal (XON/XOFF flow control)
  **Clarification**: In modern terminal emulators, `C-s` in the Erlang shell enters forward search mode; if the terminal intercepts it for flow control, this is a terminal configuration issue, not an Erlang issue

# Source Reference

"tty - A Command-Line Interface," sections "Normal Mode" and "Shell Break Mode." The source provides a complete table of key bindings for normal mode editing, describes the three operating modes (normal, search, shell break), and notes the external editor integration via `VISUAL`/`EDITOR` environment variables.

# Verification Notes

- All key bindings: Directly from source table "tty Text Editing"
- Three operating modes: Directly listed in source introduction
- External editor feature: Directly from source `C-o` entry, including Windows limitation
- Shell break mode capabilities: Directly from source section "Shell Break Mode"
- Emacs key binding heritage: Directly stated -- "Most of the Emacs line-editing commands are supported"
- Key notation conventions (C-a, M-f, C-S-a): Directly from source typographic conventions
- Confidence: HIGH -- all content directly from official ERTS documentation
