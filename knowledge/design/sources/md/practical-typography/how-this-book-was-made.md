---
title: "How This Book Was Made"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/how-this-book-was-made.html"
---

<div id="content">

<div id="doc">

How this book was made

When I started *Practical Typography*, my key question was this: how could I adapt the material from my paperback *Typography for Lawyers* into a digital version, while keeping it a peaceful, book-like reading <span class="no-hyphens">experience?</span>

At the time, my most recent adventure in e-books had been unsatisfying. When I released the first edition of *Typography for Lawyers*, readers begged for a Kindle version. So I made one. It was awful. Because the Kindle is awful. From Amazon’s perspective, this is probably a feature. From mine, it was a bug. Why do we need a typographically ruinous version of a book making the case for good typography? When the time came to make a second edition, I pulled the <span class="no-hyphens">plug.</span>

Pages from the Kindle version of Typography for Lawyers <span class="no-hyphens">(RIP)</span>

It seemed to me then—and even more so today, now that makers of e-book readers have had years to make improvements—that these devices prioritized convenience over all else. I predict they’ll never have the typographic capabilities or standards of print <span class="no-hyphens">publishing.</span>

I don’t mean that as a put-down. In publishing, convenience sometimes should win, and does win. In <a href="billionaires-typewriter.html" class="xref">The Billionaire’s Typewriter</a>, I reflect on how the original manual typewriter offered writers convenience at the cost of typographic freedom. Compared to the productivity of pencil and paper, it was a worthy <span class="no-hyphens">trade-off.</span>

Still, at the time, I was dispirited. Wealthy tech companies were taking over the book market in a manner that made convenience the \#1 consideration. Tied for last place: everything <span class="no-hyphens">else.</span>

For instance, had it been worth Apple’s time to provide nice e-book developer tools for the iPad, those tools would’ve existed. Instead, Apple provided developer tools for making flashy games, because these were more likely to sell iPads. In turn, it’s no surprise that these games have taken over the iPad <span class="no-hyphens">economy.</span>

The iPad is much better at simulating vintage pinball than simulating a vintage <span class="no-hyphens">book.</span>

Either I had to give up on the idea of a well designed e-book. Or find a way around the <span class="no-hyphens">roadblock.</span>

<div id="what-about-pdf" class="subhead">

[What about PDF?](#what-about-pdf)

</div>

True, PDF supports a lot of typographic & design flexibility. But PDF is a paper simulator. It’s great for making digital versions of works originally designed for print. For natively digital works, it imposes unnecessary complexity and <span class="no-hyphens">limitations.</span>

For a longer answer, see <a href="why-theres-no-e-book-or-pdf.html" class="xref">why there’s no e-book or PDF</a>.

<div id="back-to-the-web" class="subhead">

[Back to the web](#back-to-the-web)

</div>

Having eliminated the other options, I started thinking about publishing *Practical Typography* on the <span class="no-hyphens">web.</span>

In principle, I wasn’t opposed. After all, *Typography for Lawyers* itself had started in 2008 [as a web-based book,](http://web.archive.org/web/20080913080848/http://www.typographyforlawyers.com:80/) which is what led to the paperback deal. I had made that version in WordPress. WordPress made basic publishing tasks easy, but ambitious layouts remained <span class="no-hyphens">difficult.</span>

By the time I was thinking about *Practical Typography*, there had been valuable developments in web design—most notably browser support for webfonts. It occurred to me that what I wanted was not a simple but regimented system like WordPress—it just wouldn’t let me work with the sophistication and detail I needed. Instead, I wanted a flexible tool for describing complex HTML & CSS layouts with simpler, high-level <span class="no-hyphens">notation.</span>

In short: I wanted my own programming <span class="no-hyphens">language.</span>

<div id="enter-racket" class="subhead">

[Enter Racket](#enter-racket)

</div>

Inventing a language to solve a problem is an established technique called *language-oriented programming*. The language that results is sometimes known as a *domain-specific language* (or *DSL*).

I didn’t know this at the time, however. So, in typical fashion, I just blundered into the project with optimism. Let’s see what happens! I designed my notation—which involved programming commands embedded in plain text—and prototyped an interpreter in Python. The language worked—barely. It was reminiscent of the first act of *Iron Man*, where Tony Stark, trapped in a cave, builds his first flying suit out of toaster parts and car batteries. Not beautiful. But better than the <span class="no-hyphens">alternative.</span>

My Python skills, however, were not sufficient to get me where I needed to go. That’s when some internet spelunking led me to [Racket,](https://racket-lang.org) a programming language that had a text-based dialect called [Scribble.](http://docs.racket-lang.org/scribble/) Originally, I’d only intended to use Scribble to add a few features to my language. But as I studied it, I realized that the Racket guys had gone down the path I was traveling, and already sorted out the thorniest <span class="no-hyphens">problems.</span>

See also <a href="why-racket-why-lisp.html" class="xref">Why Racket? Why <span class="no-hyphens">Lisp?</span></a>

Moreover, I learned that Scribble itself was made possible by Racket’s orientation toward language-oriented programming. Then the light bulb went on: I shouldn’t be using Python at all. I should rewrite the whole project in <span class="no-hyphens">Racket.</span>

<div id="pollen-is-born" class="subhead">

[Pollen is born](#pollen-is-born)

</div>

So I did. I named the resulting language [Pollen.](https://pollenpub.com) I used Pollen to make the first version of *Practical Typography*. I’ve used it nearly every day since, on everything I publish on the <span class="no-hyphens">web.</span>

The difference between WordPress and <span class="no-hyphens">Pollen?</span>

- WordPress relies on a cloud-based interface—you log into a remote website and make your edits through a web interface. After you click a button, the site is <span class="no-hyphens">updated.</span>

- Pollen, by contrast, adopts the idioms of programming. There is no cloud interface. A website is a collection of source files in a local directory (written in the Pollen language). To refresh the site, you recompile these source files to produce output files. Then you copy these output files to your web <span class="no-hyphens">server.</span>

If this sounds more complicated, it is, a little. But the benefit of adopting a programming model is that within a Pollen project, I can use programming tools. For instance, I can consolidate complicated formatting tasks into functions that automatically handle them. Whereas in WordPress, I’d have to do these by hand, which in many cases would be impractical. So though the floor is higher, so is the ceiling. With Pollen, I can accomplish things that would otherwise be too <span class="no-hyphens">expensive.</span>

<div id="in-sum" class="subhead">

[In sum](#in-sum)

</div>

I’m satisfied with web publishing. The web offers plenty of typographic and layout capability. Certainly more than any e-book format, and on par with <span class="no-hyphens">PDF.</span>

But to fully harness this capability, I had to create better tools. Writing Pollen wasn’t cheap. But over its first five years, it’s already repaid my <span class="no-hyphens">investment.</span>

Readers have occasionally asked if I’ll ever publish *Practical Typography* as a paperback. Early on, I said yes. These days, no. As a reader, I prefer printed books. As a typographer, I miss working on print layouts. Eventually I’ll find other some pretext for making printed <span class="no-hyphens">things.</span>

But as a self-published writer, I’ve come to prefer the plasticity, immediacy, and reach of the web. At this point, a printed version of *Practical Typography* strikes me as a dilution of the concept. That is not a result I would’ve predicted when I started this <span class="no-hyphens">project.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- [Pollen](https://pollenpub.com) is open-source software and can be downloaded and used by <span class="no-hyphens">anyone.</span>

- My other online book, [*Beautiful Racket*,](https://beautifulracket.com) teaches language-oriented programming using <span class="no-hyphens">Racket.</span>

- PDF and print typesetting is the topic of my next software project, the slowly gestating [Quad.](https://docs.racket-lang.org/quad)

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="the-copyright-status-of-fonts.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="typographic-humor.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="appendix.html" class="box-link">chapter</a>

</div>

</div>

</div>
