---
title: "The Infinite Pixel Screen"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/the-infinite-pixel-screen.html"
---

<div id="content">

<div id="doc">

The infinite-pixel screen

Last week I upgraded my desktop monitors. I retired my trusty [Apple Cinema Displays](http://www.everymac.com/monitors/apple/studio_cinema/specs/apple_cinema_display_23.html) in favor of two 4K [Dell monitors.](https://www.dell.com/en-us/work/shop/dell-24-ultra-hd-4k-monitor-p2415q/apd/210-agnk/monitors-monitor-accessories) As a typographer, the upgrade from black & white to grayscale fonts in the ’90s was pretty good. But 4K is much <span class="no-hyphens">better.</span>

High-resolution displays like these have already taken over phones and tablets. It’s nice to see that they’re spreading into laptops and desktops <span class="no-hyphens">too.</span>

The monitors are mounted on a [Humanscale](https://www.humanscale.com/products/category_detail.cfm?category=monitorarms) stand. As of 2020, the Dell monitors have been replaced with two [LG Ultrafine 4K](https://www.apple.com/shop/product/HMUA2VC/A/lg-ultrafine-4k-display) <span class="no-hyphens">monitors.</span>

The keyboard pictured is the excellent [Matias Tactile Pro,](http://matias.ca/tactilepro4/) though I’ve since switched to an original [Apple Extended Keyboard <span class="no-hyphens">II.</span>](https://macclack.com/reviewed-apple-extended-keyboard-ii/)

Fonts look <span class="no-hyphens">fantastic.</span>

Well, that’s not entirely true. Good fonts look fantastic. Bad fonts look worse, because they can no longer hide behind the indistinct edges of coarser pixels. But if you work with type—as a reader, writer, programmer, or designer (which I guess covers just about everyone)—then upgrading to 4K is completely <span class="no-hyphens">worthwhile.</span>

But what is “4K”? In the <span style="text-decoration:line-through">false advertising</span> optimistic math of the display industry, 4K is the [common name](http://en.wikipedia.org/wiki/4K_resolution) for a screen that’s 3840 pixels wide by 2160 pixels high. (Because 3840 is, I guess, 4000-ish.) It has twice the resolution in each direction as a [standard HDTV screen,](http://en.wikipedia.org/wiki/High-definition_television) which is 1920 pixels wide by 1080 <span class="no-hyphens">high.</span>

When 4K screens first appeared, it wasn’t uncommon for people to describe them as having “twice as many” pixels. But that’s wrong. If you double the pixel resolution horizontally and vertically, it’s like cutting each pixel in half in two directions. So a 4K screen has *four* times as many pixels as an HDTV. (Skeptics are invited to multiply the numbers above and see that this is <span class="no-hyphens">so.)</span>

To the surprise of no one, the display industry plans to keep dividing pixels. Farther on the horizon is the 7680 × 4320 screen, [known as 8K.](http://en.wikipedia.org/wiki/8K_resolution) Of course, at desktop sizes, one rapidly approaches diminishing returns, because the human eye has its own [resolution limit.](http://gizmodo.com/what-is-the-resolution-of-the-human-eye-1541242269) The jump to 4K is a very noticeable improvement. The jump to 8K will be less so. At some point, manufacturers will stop dividing <span class="no-hyphens">pixels.</span>

But what if they didn’t? What if they divided the pixels on the screen an infinite number of times? How many pixels would the resulting screen <span class="no-hyphens">have?</span>

a\) As many pixels as positive integers.  
b) Fewer.  
c) <span class="no-hyphens">More.</span>

As a fan of math, I like thinking about questions like this. (If you don’t, you can bail out now. In sum: buy a 4K monitor, and you’re <span class="no-hyphens">welcome.)</span>

<div id="comparing-infinities" class="subhead">

[Comparing infinities](#comparing-infinities)

</div>

The first thing that might give you pause is the implication in option (c) that we can have a quantity of pixels that’s greater than the number of positive integers. Aren’t the integers infinite? And isn’t infinity, like, as far as you can <span class="no-hyphens">go?</span>

Georg Cantor  
1845–1918

Turns out the answer is no. For this result, we can thank the German mathematician Georg Cantor. When Cantor started his work in the 1860s, infinite numbers had been used in mathematics for hundreds of years. But there was always a bit of mystery and handwaving about what they really were. Cantor cleared away the <span class="no-hyphens">fog.</span>

One question Cantor studied is whether all infinite sets are the same size, or if some are bigger. But how do you compare infinite sets? If we had finite sets, we’d know how to compare them: just count the elements. Whichever set has more elements is bigger. But with infinite sets, counting takes too <span class="no-hyphens">long.</span>

So what do we do? We can’t count infinite sets directly. But suppose further that we couldn’t count *finite* sets directly. In that case, how could we represent, say, the quantity five? We could raise our hand and say “this many fingers”. In so doing, we’d be defining a quantity by referring to the number of elements in an existing set—namely, the set of fingers on our <span class="no-hyphens">hand.</span>

This quantity of elements in a set is also called the *cardinality* of the set. How is cardinality useful? If we have a set with a certain cardinality, we can use it to measure other sets by matching up the elements of one set to the elements of the other. If the two sets have a *one-to-one correspondence* between elements, then they must have the same <span class="no-hyphens">cardinality.</span>

For instance, suppose we want to measure the cardinality of the set of toes on our foot. We notice that we can touch each finger on our hand to each toe on our foot. Thus we can conclude that fingers and toes have the same <span class="no-hyphens">cardinality.</span>

That’s a rudimentary example. What if I gave you two bags of objects and asked whether they contained the same number of objects? Again, without counting. You could take an item out of both bags until you exhausted the supply of one bag. If the other bag was simultaneously empty, then you’d know they had the same cardinality. This would work regardless of how many items were in the <span class="no-hyphens">bag.</span>

Which brings us to Cantor’s insight: even though you can’t count infinite sets directly, you can compare them by cardinality. If two infinite sets are the same size, then you’ll be able to put them into a one-to-one correspondence. Or, if you can prove that no such correspondence exists, then one of the infinite sets must be bigger. “Finding a one-to-one correspondence” is a lot of typing, so this technique is more compactly known as *bijection*.

Bijection is a simple idea. But it’s an important tool because it helps keep us out of the counterintuitive weeds when working with infinite sets. For instance, we can now figure this out: are there more positive integers {1, 2, 3, ...} or even integers {2, 4, 6, ...}? The naive answer would be that there must be more positive integers, because the set of positive integers includes both the even and odd <span class="no-hyphens">integers.</span>

But this is wrong. Using bijection, we see that we can put the positive integers and even integers into a one-to-one correspondence like <span class="no-hyphens">so:</span>

`1, 2, 3, 4, ...`  
`2, 4, 6, 8, ...`

No matter how far we go, we can always find the element in one set that corresponds to the element in the other. That’s the bijection. Thus, the cardinality of these two infinite sets is the same. There are just as many positive integers as even integers. It sounds a little weird at first, but we just proved <span class="no-hyphens">it.</span>

<div id="a-bigger-infinity" class="subhead">

[A bigger infinity](#a-bigger-infinity)

</div>

To show that two infinite sets are the same size, you have to find a bijection. But to show that one infinite set is bigger than the other, you have to prove something more difficult: that no bijection can <span class="no-hyphens">exist.</span>

But Cantor proved this was possible too. One of his methods, the *diagonalization* argument, is singularly lovely, and goes like <span class="no-hyphens">this.</span>

Cantor started by considering an infinite string of binary digits like <span class="no-hyphens">so:</span>

`10010101001011101010 ...`

Then he thought about the set of all such <span class="no-hyphens">strings:</span>

`10010101001010101010 ...`  
`01001010100101001001 ...`  
`10010011110001001000 ...`  
`...`

Then he asked: how many of these strings exist? Clearly, it’s an infinite number. And it looks like we might be able to find a bijection with the positive integers by just listing them all out in some systematic <span class="no-hyphens">way:</span>

`1: 10010101001010101010 ...`  
`2: 01001010100101001001 ...`  
`3: 10010011110001001000 ...`  
`4: ...`

If that bijection works, then the set of infinite binary strings has the same cardinality as the positive <span class="no-hyphens">integers.</span>

But here comes Cantor’s jiu-jitsu move. He points out that if you take the nth digit from each string and flip it (from 0 to 1 or 1 to 0), you’ll end up with a new <span class="no-hyphens">string:</span>

1: <span style="background:#fdd">1</span>0010101001010101010 ...  
2: 0<span style="background:#fdd">1</span>001010100101001001 ...  
3: 10<span style="background:#fdd">0</span>10011110001001000 ...  
4: ...

<span style="background:#dfd">001</span> ...

Obviously, this new string is itself an infinite binary string. So it belongs to our set. **But it’s not in the bijection**. How do we know this? Because of how we constructed it: the new string differs from every string already in the bijection by at least one <span class="no-hyphens">digit.</span>

In other words, given any attempt to match up these infinite binary strings with the positive integers, you can always construct another string that’s not in the bijection. Therefore, there can be no bijection between the positive integers and these infinite binary strings. Though both sets are infinite, the set of infinite binary strings is really, truly <span class="no-hyphens">bigger.</span>

Cantor also showed, to the surprise of many, that the set of rational numbers is only countably <span class="no-hyphens">infinite.</span>

To be more precise, the *cardinality* of the set of infinite binary strings is greater than the cardinality of the set of positive integers. These two infinite cardinalities surface often enough that they have their own names. Sets that share the cardinality of the positive integers are called *countably* infinite; sets that share the cardinality of the infinite binary strings are called *uncountably* <span class="no-hyphens">infinite.</span>

<div id="back-to-the-infinite-pixel-screen" class="subhead">

[Back to the infinite-pixel screen](#back-to-the-infinite-pixel-screen)

</div>

Recall that our screen is constructed by dividing the pixels in half an infinite number of times. We can now see that the word “infinite” in that sentence refers to a *countably* infinite number of pixel divisions. Why? Because we can create a bijection between the positive integers and the pixel <span class="no-hyphens">divisions.</span>

Suppose we start with a screen that’s one giant <span class="no-hyphens">pixel:</span>

|     |
|-----|
|     |

In step 1, we cut the pixel in half <span class="no-hyphens">horizontally:</span>

|     |
|-----|
|     |
|     |

In step 2, we cut it in half <span class="no-hyphens">vertically:</span>

 
</div>

</div>

 
In step 3, we cut each new pixel <span class="no-hyphens">horizontally:</span>

 
In step 4, we cut them <span class="no-hyphens">vertically:</span>

 
And so on. You can see that each round of cutting will correspond to a positive integer, creating a bijection with a countably infinite <span class="no-hyphens">set.</span>

So how many pixels remain at the end? It should be clear that we have infinite pixels. Moreover, having made countably infinite rounds of cuts, the intuitive answer might be that we also have a countably infinite number of <span class="no-hyphens">pixels.</span>

Or do we? Is it possible that we have more pixels—an *uncountably* infinite set of pixels? As before, we can figure this out by asking whether we can create a bijection betweeen our pixels and some uncountably infinite <span class="no-hyphens">set.</span>

We have such a set. We already established that Cantor’s infinite binary strings were uncountably <span class="no-hyphens">infinite:</span>

`10010101001010101010 ...`  
`01001010100101001001 ...`  
`10010011110001001000 ...`  
`...`

So can we create a bijection between these strings and the pixels? I propose we can. Recall that we constructed our panel by making alternating horizontal and vertical cuts. We can match up any of these binary strings to a certain pixel on the screen by using the digits in the string to “steer” <span class="no-hyphens">us.</span>

In step 1, we made a horizontal cut. So if the first digit in our string is 0, we’ll choose the top half of the pixel. If 1, we’ll choose the bottom <span class="no-hyphens">half.</span>

|              |
|--------------|
| **`0`**`...` |
| **`1`**`...` |

In step 2, we made a vertical cut. So if our second digit is 0, we’ll choose the left half of the pixel. If 1, we’ll choose the right <span class="no-hyphens">half.</span>

`0`**`0`**`...`

`0`**`1`**`...`

`1`**`0`**`...`

`1`**`1`**`...`

Now we just repeat this process: letting alternating numbers in the string indicate top vs. bottom, then left vs. right. After step <span class="no-hyphens">4:</span>

`000`**`0`**`...`

`000`**`1`**`...`

`010`**`0`**`...`

`010`**`1`**`...`

`001`**`0`**`...`

`001`**`1`**`...`

`011`**`0`**`...`

`011`**`1`**`...`

`100`**`0`**`...`

`100`**`1`**`...`

`110`**`0`**`...`

`110`**`1`**`...`

`101`**`0`**`...`

`101`**`1`**`...`

`111`**`0`**`...`

`111`**`1`**`...`

As we continue, the cells will get smaller, and the binary strings will get longer. Eventually—meaning, at the end of this countably infinite process—we’ll have a one-to-one correspondence between every pixel and every infinite binary string. In other words, we will have defined a bijection. And since the infinite binary strings are uncountably infinite, so are the pixels. Therefore, we have more pixels than positive <span class="no-hyphens">integers.</span>

<div id="the-internet-demands-a-recount" class="subhead">

[The internet demands a recount](#the-internet-demands-a-recount)

</div>

The first release of this article ended here. In an impressively efficient display of [Cunningham’s Law,](http://meta.wikimedia.org/wiki/Cunningham%27s_Law) several readers wrote to say that my reasoning was faulty. The infinite-pixel screen contains only a countably infinite number of <span class="no-hyphens">pixels.</span>

I’ll concede that this is <span class="no-hyphens">so.</span>

To see why, let’s first find the flaw in my previous demonstration. I claimed that my pixel-cutting technique would let us associate any infinite binary string with a <span class="no-hyphens">pixel.</span>

A couple readers tried to find a contradiction using Cantor’s diagonalization argument, saying that there should be a way to construct a new infinite binary string that doesn’t map to a particular pixel. But there’s no way to do <span class="no-hyphens">this.</span>

Why? Because the problem with my proposed bijection is not that it fails to map every infinite binary string, but that it fails to map *any* of <span class="no-hyphens">them.</span>

Even though each of our binary strings is infinite in length, it represents an exact number—a specific point on the screen. This shouldn’t alarm you. For instance, recall from seventh-grade math that the exact fraction one-third can be found on the number line between 0 and 1. But the decimal expansion of this fraction is the infinite decimal 0.333... As we add digits to the decimal—0.3, 0.33, 0.333, 0.3333—we get ever closer to one-third. And though one-third is certainly the *limit* of this series of decimals, one-third itself never appears within the series. In a sense, the limit is information that’s “outside” this series of <span class="no-hyphens">approximations.</span>

Likewise, the pixels in my construction represent approximations of infinite binary strings, which are the limits of these approximations. But just as there’s no way to follow 0.333... until you reach exactly one-third, there’s no way to carve a pixel until you get to the exact point represented by a certain infinite binary string. So the premise behind my proposed bijection was faulty. I tried to fudge that which could not be <span class="no-hyphens">fudged.</span>

Having adopted the idea that every pixel is an approximation, we can use the construction to recount the pixels. This time, let’s label our original pixel with the digit `1`:

|     |
|-----|
| `1` |

Then we’ll append a binary digit each time we split the current pixels, the same way as <span class="no-hyphens">before:</span>

|      |
|------|
| `10` |
| `11` |

`100`

`101`

`110`

`111`

Skipping to step <span class="no-hyphens">4:</span>

We need the prepended 1 so that we don’t end up with ambiguous indexes like 01, 001, and 0001. Instead they become 101, 1001, and <span class="no-hyphens">10001.</span>

`10000`

`10001`

`10100`

`10101`

`10010`

`10011`

`10110`

`10111`

`11000`

`11001`

`11100`

`11101`

`11010`

`11011`

`11110`

`11111`

In so doing, we can associate every pixel at every level of the construction with a unique integer. (You can interpret the numbers above as binary or decimal—same result.) Of course, the total number of pixels is still infinite, since the doubling goes on forever. But any infinite subset of the positive integers can be [put into bijection](http://math.stackexchange.com/questions/107617/an-infinite-subset-of-a-countable-set-is-countable) with the positive integers (like the example of even integers vs. positive integers earlier). So there are only as many pixels as <span class="no-hyphens">integers.</span>

<div id="extra-credit" class="subhead">

[Extra credit](#extra-credit)

</div>

What about those infinite binary strings? We now see that there are more of those (because they’re uncountably infinite) than pixels in our screen (because those are countably infinite). But is there a way to relate these two kinds of infinite cardinality within this pixel construction? I say yes. (OK, I’ve been wrong <span class="no-hyphens">before.)</span>

[Cantor’s Theorem](http://en.wikipedia.org/wiki/Cantor%27s_theorem)—he discovered several theorems, but this is the eponymous one—says that for any set of items, the set of *subsets* of items is always bigger (i.e., has greater cardinality). With a small set, this is easy to see. The three-element set {x, y, z} has eight subsets: {x}, {y}, {z}, {x, y}, {x, z}, {y, z}, {x, y, z} itself, and {}, the empty set. This set of subsets is also known as a *power set*.

In general, how big is a power set? When we create any subset, we’re essentially making a series of decisions whether to include each element. So for the set {x, y, z}, we have three elements, and hence three decisions to make. And because each decision can have two outcomes (include vs. exclude), the number of possible subsets is 2 × 2 × 2 = 8. Thus, for a finite set, the size of the power set is 2 raised to a power equal to the number of elements in the <span class="no-hyphens">set.</span>

The neat part of Cantor’s Theorem is that it also applies to infinite sets. Consider the power set of positive integers—meaning, all possible subsets of the positive integers. This power set is itself an infinite set, but by Cantor’s Theorem, also has greater cardinality than the positive <span class="no-hyphens">integers.</span>

This idea of a bigger infinite set is still weird and abstract. So let’s try bringing it back to our infinite-pixel <span class="no-hyphens">screen.</span>

First, let’s ask how could we notate those subsets. Since every subset is a series of include–exclude decisions, we could adopt a numerical scheme—say, “1” for include and “0” for exclude. Then we’d just need to write one digit for every positive integer, maybe like <span class="no-hyphens">so:</span>

`10010101001011101010 ...`

Then the full power set for the positive integers would look something like <span class="no-hyphens">this:</span>

`10010101001010101010 ...`  
`01001010100101001001 ...`  
`10010011110001001000 ...`  
`...`

That should look familiar—we’ve come full circle, back to Cantor’s set of infinite binary strings. Recall that Cantor’s diagonalization argument showed that this set had greater cardinality than the integers. Cantor’s Theorem says the same thing, but through the idea of the power <span class="no-hyphens">set.</span>

<div id="thats-a-lot-of-bitmaps" class="subhead">

[That’s a lot of bitmaps](#thats-a-lot-of-bitmaps)

</div>

*Bit* is a contraction of “binary digit”. *Byte* is a pun on bit (with a “y” to further distinguish the <span class="no-hyphens">words).</span>

When we see a row of zeroes and ones, it suggests a stream of bits—a *bit* being the smallest unit of digital information. Having noticed that a power set can be written as a set of bit strings, it is possible to recharacterize the power set in terms of <span class="no-hyphens">information?</span>

Why not? Let’s see what happens if we treat the power set as a measure of the *information capacity* of a set. We saw how a three-element set {x, y, z} could be used to express eight different subsets. That’s like saying that three bits in a computer can express eight numbers (and indeed they can). This equivalence will be true for any finite set. By Cantor’s Theorem, it should remain true for infinite <span class="no-hyphens">sets.</span>

Let’s test it out. We now have a screen of countably infinite pixels. But pixels are the perfect items for our example, since their reason for existence is to display information. To make things simple, we’ll assume that our screen is installed in a vintage Mac Plus Infinite, so all the pixels can be either white (on) or black <span class="no-hyphens">(off).</span>

Now turn the computer on. What can we say about the screen image? It’s a bitmap, which we can intuitively understand as way of storing and displaying information. The bitmap is defined as a set of pixels turned white, which is a subset of the whole screen. Of course, any pixel in the screen can be white or black, so as we use the computer, and the bitmap changes, we’re seeing different subsets turned <span class="no-hyphens">white.</span>

So the final question: how many bitmaps are possible on our infinite-pixel screen? Or equivalently: what is the information capacity of this <span class="no-hyphens">screen?</span>

Since any particular bitmap is represented by a subset of screen pixels, then the set of all possible bitmaps is the set of all possible pixel subsets—otherwise known as the power set. Furthermore, we have countably infinite pixels in the screen to begin with. And the power set of a countably infinite set—as Cantor showed in several ways—is uncountably <span class="no-hyphens">infinite.</span>

Therefore, though it turned out our screen could only hold a countably infinite number of pixels, it can still display an *uncountably* infinite number of <span class="no-hyphens">bitmaps.</span>

If you need to make a slide presentation of Cantor’s infinite binary strings, this is the screen to get, because it can display all of <span class="no-hyphens">them.</span>

Otherwise, however, my advice remains the same—just upgrade to 4K. It’s got plenty of pixels. <span class="no-hyphens">Really.</span>

—Matthew Butterick  
15–18 March <span class="no-hyphens">2015</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- William Dunham’s [*Journey Through Genius*](http://www.amazon.com/Journey-through-Genius-Theorems-Mathematics/dp/014014739X) is a terrific, approachable book about famous math theorems through history, and includes discussions of Cantor’s work. (Did you know that Archimedes had a day job designing military weapons? I <span class="no-hyphens">didn’t.)</span>

- If you’re already sure you enjoy math, don’t miss [*Infinity and the Mind*](http://www.amazon.com/Infinity-Mind-Philosophy-Infinite-Princeton/dp/0691121273) by Rudy <span class="no-hyphens">Rucker.</span>

- Suppose we constructed our infinite screen a different way: by taking a pixel of a certain dimension and tiling it indefinitely in both directions, to form an endless grid. Compared to our first infinite screen, how many pixels would be in the new one—the same? More? Fewer? (Left as an exercise to the <span class="no-hyphens">reader.)</span>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

<a href="billionaires-typewriter.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="effluents-influence-affluence.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="commentary.html" class="box-link">chapter</a>

</div>

</div>

</div>
