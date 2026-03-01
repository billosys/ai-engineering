---
title: "Tables"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/tables.html"
---

<div id="content">

<div id="doc">

tablesThe best tool for gridded or complex layouts

The good news: tables are one of the handiest tools in your word processor and web browser. A table is usually the right solution for layout problems where <a href="white-space-characters.html" class="xref">white-space characters</a> aren’t up to the <span class="no-hyphens">task.</span>

The bad news: tables can be difficult to use. The user interface for editing them is complex and finicky. While I can’t give you a full tutorial on using tables in your word processor—refer to your manual or help file—I can give you a few directional <span class="no-hyphens">tips.</span>

I’ve already pointed out the ways in which <a href="typewriter-habits.html" class="xref">typewriter habits</a> have endured. But an unfortunate truth about word processors and web browsers is that their basic model for page layout is similar to that of a typewriter of a hundred years ago: the document is treated as one big column of text. That’s great when all you need is one big column of text. It’s not so great <span class="no-hyphens">otherwise.</span>

Tables are <span class="no-hyphens">useful—</span>

1.  For spreadsheet-style <a href="grids-of-numbers.html" class="xref">grids of numbers</a> or other data. In the typewriter era, grids like this would’ve been made with <a href="tabs-and-tab-stops.html" class="xref">tabs and tab stops</a>. These days, you’d use a <span class="no-hyphens">table.</span>

2.  For layouts where text needs to be positioned side-by-side or floating at specific locations on the page. If making these is frustrating with the usual layout tools, try using a <span class="no-hyphens">table.</span>

<div class="howto">

<div class="howto-name">

How to insert a table

</div>

WordInsert → Tables panel → Table → drag your cursor around the grid to set the number of rows and <span class="no-hyphens">columns.</span>

Mac OS Word Insert tab → Table → drag your cursor to set the number of rows and <span class="no-hyphens">columns.</span>

PagesInsert → Table → Basic. Pages will insert a small table, and open the table editor in the Inspector to allow further <span class="no-hyphens">adjustments.</span>

HTMLThe three basic tags are `<table>`, `<tr>` (for each row), and `<td>` (for each cell). HTML also supports optional tags for certain other table <span class="no-hyphens">elements.</span>

</div>

There are many ways to format a table. But default tables have two formatting defects you should always fix: cell borders and cell margins.

Web browsers used to turn on cell borders by default, but these days, they <span class="no-hyphens">don’t.</span>

Cell borders are the lines around each cell in the table. Cell borders are helpful as guides when you’re loading information into the table. They’re less useful once the table is full. The text in the cells will create an implied grid. Cell borders can make the grid cluttered and difficult to read, especially in tables with many small <span class="no-hyphens">cells.</span>

<div class="gap" style="height:0.7em">

</div>

<div class="indented">

| Cluttered   | Athos | Porthos | Aramis |
|-------------|-------|---------|--------|
| Priors?     | Yes   | No      | Yes    |
| Alibi?      | No    | Yes     | Yes    |
| Confession? | No    | No      | No     |

</div>

<div class="indented">

| Clean       | Athos | Porthos | Aramis |
|-------------|-------|---------|--------|
| Priors?     | Yes   | No      | Yes    |
| Alibi?      | No    | Yes     | Yes    |
| Confession? | No    | No      | No     |

</div>

In this example, cell borders are unnecessary. In other cases, they can be useful. The goal is to improve the legibility of the table. When you’re ready to format your table, I recommend turning off all the cell borders to start, and then turning them back on as needed. (See <a href="rules-and-borders.html" class="xref">rules and borders</a> for more <span class="no-hyphens">tips.)</span>

<div class="howto">

<div class="howto-name">

How to turn off cell borders

</div>

WordRight-click in the table to display menu → Borders and Shading → Borders tab. In the column on the left labeled Setting, click the button next to None. Click OK.

PagesClick the table to select it. Go to View → Show Toolbar (or option + ⌘ + t) → Format button → Table pane. Under Table Outline, select None, and under Gridlines, deselect the two buttons on the left (that control horizontal and vertical cell borders, <span class="no-hyphens">respectively)</span>

CSS`border: none` (though be careful: tables, table rows, and table cells can all have separate border <span class="no-hyphens">settings)</span>

</div>

Cell margins create space between the cell borders and the text of the cell. Increasing the cell margins is the best way to improve the legibility of a dense <span class="no-hyphens">table.</span>

<div class="gap" style="height:0.7em">

</div>

<div class="indented">

| Dense | Athos          | Porthos        | Aramis         |
|-------|----------------|----------------|----------------|
| Phone | (617) 555 1453 | (508) 555 3232 | (603) 555 8490 |
| Cell  | (617) 555 3145 | (508) 555 2323 | (603) 555 8491 |
| Fax   | (617) 555 5413 | (508) 555 4545 | (603) 555 8492 |

</div>

<div class="indented">

| Not   | Athos          | Porthos        | Aramis         |
|-------|----------------|----------------|----------------|
| Phone | (617) 555 1453 | (508) 555 3232 | (603) 555 8490 |
| Cell  | (617) 555 3145 | (508) 555 2323 | (603) 555 8491 |
| Fax   | (617) 555 5413 | (508) 555 4545 | (603) 555 8492 |

</div>

The default cell margins, especially in Word, are too tight. But add space gingerly— a little goes a long way—start around 0.03″ and increase by increments of 0.01″. Also, there’s no need to make the cell margins the same on all sides. The top and bottom margins can be bigger than the side margins, if that looks <span class="no-hyphens">right.</span>

<div class="howto">

<div class="howto-name">

How to set cell margins

</div>

WordRight-click in the table to display menu → Table Properties → Table tab → Options. Under Default cell margins, enter the values. You can also use the up and down arrow keys to change the values in increments of <span class="no-hyphens">0.01″.</span>

PagesClick inside the table and press ⌘ + a to select all cells. Then do View → Show Toolbar (or option + ⌘ + t) → Format button → Text pane → Layout pane → enter the measurement in Text <span class="no-hyphens">Inset</span>

CSSAdd `padding` to your `td` (table cell) <span class="no-hyphens">selector.</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- In HTML/CSS, you can still use the traditional `table` markup to make a table. But you can also use the newer CSS *grid layout*, which is now [well supported](http://caniuse.com/#search=grid) in web browsers. Its syntax is knottier than `table`. But by moving the table markup out of the HTML and into CSS, it’s ultimately more <span class="no-hyphens">flexible.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="bulleted-and-numbered-lists.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="rules-and-borders.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="page-layout.html" class="box-link">chapter</a>

</div>

</div>

</div>
