<div class="container is-max-desktop" role="main">

<div class="content is-medium">

> # From personal project to industry standard
>
> *Introduction added in 2025*
>
> When introduced Oklab in 2020, I never expected it to reach as far as it has. In a few years Oklab has, among other things, found its way into:
>
> - Photoshop – Now the default interpolation method for gradients
> - Web browsers – Part of CSS Color Level 4 and 5, supported by major browsers
> - Game engines – Used in Unity’s gradients and Godot’s color picker
> - Open source libraries – Too many to list! For python, I recommend [colour](https://github.com/colour-science/colour).
>
> I developed Oklab in my free time and the results are freely available and open source. Want to support my work? Here are some options:
>
> - I’m available for contracting work in color science, computer graphics, game dev and more.
> - I’m an indie game developer making [Island Architect](https://store.steampowered.com/app/3079100/Island_Architect), a cozy town building game. Consider sharing and wishlisting. It is of course using Oklab here and there!
>
> Below you find the original blog post introducing Oklab, from 2020.

# A perceptual color space for image processing <a href="#a-perceptual-color-space-for-image-processing" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

A perceptual color space is desirable when doing many kinds of image processing. It is useful for things like:

- Turning an image grayscale, while keeping the perceived lightness the same
- Increasing the saturation of colors, while maintaining perceived hue and lightness
- Creating smooth and uniform looking transitions between colors

Unfortunately, as far as I am aware, while there are color spaces that aim to be perceptually uniform, none are without significant drawbacks when used for image processing.

For this reason I have designed a new perceptual color space, designed to be simple to use, while doing a good job at predicting perceived lightness, [chroma](https://en.wikipedia.org/wiki/Colorfulness) and hue. It is called the **Oklab color space**, because it is an OK Lab color space.

Before diving into the details of why a new color space is needed and how it was derived, here is the everything needed to use the color space:

# The Oklab color space <a href="#the-oklab-color-space" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

A color in Oklab is represented with three coordinates, similar to how [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space) works, but with better perceptual properties. Oklab uses a D65 whitepoint, since this is what sRGB and other common color spaces use. The three coordinates are:

- <span class="katex"><span class="katex-mathml">$`L`$</span></span> – perceived lightness
- <span class="katex"><span class="katex-mathml">$`a`$</span></span> – how green/red the color is
- <span class="katex"><span class="katex-mathml">$`b`$</span></span> – how blue/yellow the color is

For many operations, <span class="katex"><span class="katex-mathml">$`Lab`$</span></span>-coordinates can be used directly, but they can also be transformed into polar form, with the coordinates lightness, chroma and hue, <span class="katex"><span class="katex-mathml">$`LCh`$</span></span>:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`C={\sqrt {a^2+b^2}}, \qquad h^{\circ}=\text{atan2}(b,a)`$</span></span></span>

From <span class="katex"><span class="katex-mathml">$`C`$</span></span> and <span class="katex"><span class="katex-mathml">$`h^{\circ}`$</span></span>, <span class="katex"><span class="katex-mathml">$`a`$</span></span> and <span class="katex"><span class="katex-mathml">$`b`$</span></span> can be computed like this:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`a=C\cos(h^{\circ}),\qquad b=C\sin(h^{\circ})`$</span></span></span>

Lets look at a practical example to see how Oklab performs, before looking at how the <span class="katex"><span class="katex-mathml">$`Lab`$</span></span> coordinates are computed.

> #### Comparing Oklab to HSV <a href="#comparing-oklab-to-hsv" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>
>
> Here’s an Oklab color gradient with varying hue and constant lightness and chroma.
>
> <img src="/img/oklab/hue_oklab.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 1130px) min(calc(var(--main-width) * 0.1495575221238938), 169px);" decoding="async" loading="lazy" width="1130" height="169" alt="Oklab varying hue plot" />
>
> Compare this to a similar plot of a HSV color gradient with varying hue and constant value and saturation (HSV using the sRGB color space).
>
> <img src="/img/oklab/hue_hsv.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 1130px) min(calc(var(--main-width) * 0.1495575221238938), 169px);" decoding="async" loading="lazy" width="1130" height="169" alt="HSV varying hue plot" />
>
> The gradient is quite uneven and there are clear differences in lightness for different hues. Yellow, magenta and cyan appear much lighter than red and blue.
>
> Here is lightness of the HSV plot, as predicted by Oklab:
>
> <img src="/img/oklab/hue_hsv_lightness.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 1130px) min(calc(var(--main-width) * 0.1495575221238938), 169px);" decoding="async" loading="lazy" width="1130" height="169" alt="HSV varying hue plot lightness" />

### Implementation <a href="#implementation" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

#### Converting from XYZ to Oklab <a href="#converting-from-xyz-to-oklab" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Given a color in <span class="katex"><span class="katex-mathml">$`XYZ`$</span></span> coordinates, with a D65 whitepoint and white as Y=1, Oklab coordinates can be computed like this:

First the <span class="katex"><span class="katex-mathml">$`XYZ`$</span></span> coordinates are converted to an approximate cone responses:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`\begin{pmatrix} l \\ m \\ s \end{pmatrix} = \mathbf{M_1} \times \begin{pmatrix} X \\ Y \\ Z \end{pmatrix}`$</span></span></span>

A non-linearity is applied:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`\begin{pmatrix} l' \\ m' \\ s' \end{pmatrix} = \begin{pmatrix} l^{\frac 1 3} \\ m^{\frac 1 3} \\ s^{\frac 1 3} \end{pmatrix}`$</span></span></span>

Finally, this is transformed into the <span class="katex"><span class="katex-mathml">$`Lab`$</span></span>-coordinates:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`\begin{pmatrix} L \\ a \\ b \end{pmatrix} = \mathbf{M_2} \times \begin{pmatrix} l' \\ m' \\ s' \end{pmatrix}`$</span></span></span>

with the following values for <span class="katex"><span class="katex-mathml">$`\mathbf{M_1}`$</span></span> and <span class="katex"><span class="katex-mathml">$`\mathbf{M_2}`$</span></span>:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`\mathbf{M_1} = \begin{pmatrix} +0.8189330101 & +0.3618667424 & -0.1288597137 \\ +0.0329845436 & +0.9293118715 & +0.0361456387 \\ +0.0482003018 & +0.2643662691 & +0.6338517070 \end{pmatrix}`$</span></span></span>

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`\mathbf{M_2} = \begin{pmatrix} +0.2104542553 & +0.7936177850 & -0.0040720468 \\ +1.9779984951 & -2.4285922050 & +0.4505937099 \\ +0.0259040371 & +0.7827717662 & -0.8086757660 \end{pmatrix}`$</span></span></span>

The inverse operation, going from Oklab to XYZ is done with the following steps:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`\begin{pmatrix} l' \\ m' \\ s' \end{pmatrix} = \mathbf{M_2}^{-1} \times \begin{pmatrix} L \\ a \\ b \end{pmatrix},\qquad \begin{pmatrix} l \\ m \\ s \end{pmatrix} = \begin{pmatrix} {(l')}^{3} \\ {(m')}^{3} \\ {(s')}^{3} \end{pmatrix},\qquad \begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = \mathbf{M_1}^{-1} \times \begin{pmatrix} l \\ m \\ s \end{pmatrix}`$</span></span></span>

  

> ##### Table of example XYZ and Oklab pairs <a href="#table-of-example-xyz-and-oklab-pairs" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>
>
> Provided to test Oklab implementations. Computed by transforming the XYZ coordinates to Oklab and rounding to three decimals.
>
> | X     | Y     | Z     | L     | a      | b      |
> |-------|-------|-------|-------|--------|--------|
> | 0.950 | 1.000 | 1.089 | 1.000 | 0.000  | 0.000  |
> | 1.000 | 0.000 | 0.000 | 0.450 | 1.236  | -0.019 |
> | 0.000 | 1.000 | 0.000 | 0.922 | -0.671 | 0.263  |
> | 0.000 | 0.000 | 1.000 | 0.153 | -1.415 | -0.449 |

  

#### Converting from linear sRGB to Oklab <a href="#converting-from-linear-srgb-to-oklab" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Since this will be a common use case, here is the code to convert linear sRGB values to Oklab and back. To compute linear sRGB values, see [my previous post](https://bottosson.github.io/posts/colorwrong/#what-can-we-do%3F).

The code is in C++, but without any fancy features so should be easy to translate. The code is available in public domain, feel free to use it any way you please. It is also available under an MIT licensee if you for some reason can’t or don’t want to use public domain software. The license text [is available here](https://bottosson.github.io/misc/License.txt)

``` language-cpp
struct Lab {float L; float a; float b;};
struct RGB {float r; float g; float b;};

Lab linear_srgb_to_oklab(RGB c) 
{
    float l = 0.4122214708f * c.r + 0.5363325363f * c.g + 0.0514459929f * c.b;
   float m = 0.2119034982f * c.r + 0.6806995451f * c.g + 0.1073969566f * c.b;
 float s = 0.0883024619f * c.r + 0.2817188376f * c.g + 0.6299787005f * c.b;

    float l_ = cbrtf(l);
    float m_ = cbrtf(m);
    float s_ = cbrtf(s);

    return {
        0.2104542553f*l_ + 0.7936177850f*m_ - 0.0040720468f*s_,
        1.9779984951f*l_ - 2.4285922050f*m_ + 0.4505937099f*s_,
        0.0259040371f*l_ + 0.7827717662f*m_ - 0.8086757660f*s_,
    };
}

RGB oklab_to_linear_srgb(Lab c) 
{
    float l_ = c.L + 0.3963377774f * c.a + 0.2158037573f * c.b;
    float m_ = c.L - 0.1055613458f * c.a - 0.0638541728f * c.b;
    float s_ = c.L - 0.0894841775f * c.a - 1.2914855480f * c.b;

    float l = l_*l_*l_;
    float m = m_*m_*m_;
    float s = s_*s_*s_;

    return {
      +4.0767416621f * l - 3.3077115913f * m + 0.2309699292f * s,
        -1.2684380046f * l + 2.6097574011f * m - 0.3413193965f * s,
        -0.0041960863f * l - 0.7034186147f * m + 1.7076147010f * s,
    };
}
```

> The matrices were updated 2021-01-25. The new matrices have been derived using a higher precision sRGB matrix and with exactly matching D65 values. The old matrices are available [here](https://bottosson.github.io/misc/srgb_to_oklab_old.txt) for reference. The values only differ after the first three decimals.
>
> Depending on use case you might want to use the sRGB matrices your application uses directly instead of the ones provided here.

This is everything you need to use the Oklab color space! If you need a simple perceptual color space, try it out.

The rest of the post will go into why a new color space was needed, how it has been constructed and how it compares with existing color spaces.

------------------------------------------------------------------------

# Motivation and derivation of Oklab <a href="#motivation-and-derivation-of-oklab" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

What properties does a perceptual color space need to satisfy to be useful for image processing? The answer to this is always going to be a bit subjective, but based on my experience, these are a good set of requirements:

> - **Should be an opponent color space**, similar to for example [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space).
> - **Should predict lightness, chroma and hue well**. <span class="katex"><span class="katex-mathml">$`L`$</span></span>, <span class="katex"><span class="katex-mathml">$`C`$</span></span> and <span class="katex"><span class="katex-mathml">$`h`$</span></span> should be perceived as orthogonal, so one can be altered without affecting the other two. This is useful for things like turning an image black and white and increasing colorfulness without introducing hue shifts etc.
> - **Blending two colors should result in even transitions**. The transition colors should appear to be in between the blended colors (e.g. passing through a warmer color than either original color is not good).
> - **Should assume a D65 whitepoint**. This is what common color spaces like sRGB, rec2020 and Display P3 uses.
> - **Should behave well numerically**. The model should be easy to compute, numerically stable and differentiable.
> - **Should assume normal well lit viewing conditions**. The complexity of supporting different viewing conditions is not practical in most applications. Information about absolute luminance and background luminance adaptation does not normally exist and the viewing conditions can vary.
> - **If the scale/exposure of colors are changed, the perceptual coordinates should just be scaled by a factor**. To handle a large dynamic range without requiring knowledge of viewing conditions all colors should be modelled as if viewed under normal viewing conditions and as if the eye is adapted to roughly the luminance of the color. This avoids a dependence on scaling.

### What about existing models? <a href="#what-about-existing-models%3F" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Let’s look at existing models and how they stack up against these requirements. Further down there are graphs that illustrate some of these issues.

> - **[CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space) and [CIELUV](https://en.wikipedia.org/wiki/CIELUV)** – Largest issue is their inability to predict hue. In particular blue hues are predicted badly. Other smaller issues exist as well
> - **[CIECAM02-UCS](https://en.wikipedia.org/wiki/CIECAM02) and the newer CAM16-UCS** – Does a good job at being perceptually uniform overall, but doesn’t meet other requirements: Bad numerical behavior, it is not scale invariant and blending does not behave well because of its compression of chroma. Hue uniformity is decent, but other models predict it more accurately.
> - **[OSA-UCS](https://en.wikipedia.org/wiki/OSA-UCS)** – Overall does a good job. The transformation to OSA-UCS lacks an analytical inverse unfortunately which makes it impractical.
> - **[IPT](https://scholarworks.rit.edu/theses/2858/)** – Does a great job modelling hue uniformity. Doesn’t predict lightness and chroma well unfortunately, but meets all other requirements. Is simple computationally and does not depend on the scale/exposure.
> - **[JzAzBz](https://www.osapublishing.org/oe/fulltext.cfm?uri=oe-25-13-15131&id=368272)** – Overall does a fairly good job. Designed to have uniform scaling of lightness for HDR data. While useful in some cases this introduces a dependence on the scale/exposure that makes it hard to use in general cases.
> - **[HSV](https://en.wikipedia.org/wiki/HSL_and_HSV) representation of sRGB** – Only on this list because it is widely used. Does not meet any of the requirements except having a D65 whitepoint.

So, all in all, all these existing models have drawbacks.

Out of all of these, two models stand out: CAM16-UCS, for being the model with best properties of perceptual uniformity overall, and IPT for having a simple computational structure that meets all the requirements besides predicting lightness and chroma well.

For this reason it is reasonable to try to make a new color space, with the same computational structure as IPT, but that performs closer to CAM16-UCS in terms of predicting lightness and chroma. This exploration resulted in Oklab.

### How Oklab was derived <a href="#how-oklab-was-derived" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

To derive Oklab, three datasets were used:

- A generated data set of pairs of colors with the same lightness but random hue and chroma, generated using CAM16 and normal viewing conditions. Colors were limited to be within Pointer’s Gamut – the set of possible surface colors.
- A generated data set of pairs of colors with the same chroma but random hue and lightness, generated using CAM16 and normal viewing conditions. Colors were limited to be within Pointer’s Gamut
- The [uniform perceived hue](https://github.com/nschloe/colorio/blob/master/colorio/data/ebner_fairchild.yaml) data used to derive IPT. From this data, colors were combined into pairs of colors with equal perceived hue.

These datasets can be used to test prediction of lightness, chroma and hue respectively. If a color space accurately models <span class="katex"><span class="katex-mathml">$`L`$</span></span>, <span class="katex"><span class="katex-mathml">$`C`$</span></span> and <span class="katex"><span class="katex-mathml">$`h`$</span></span>, then all pairs in lightness dataset should have the same value for <span class="katex"><span class="katex-mathml">$`L`$</span></span>, all pairs in the chroma dataset the same value for <span class="katex"><span class="katex-mathml">$`C`$</span></span> and all pairs in the hue dataset the same values for <span class="katex"><span class="katex-mathml">$`h`$</span></span>.

To test a color space it is not possible to simply check the distance in predictions in the tested color space however, since that will depend on the scaling of the color space. It is also not desirable to exactly predict ground truth values for <span class="katex"><span class="katex-mathml">$`L`$</span></span>, <span class="katex"><span class="katex-mathml">$`C`$</span></span> and <span class="katex"><span class="katex-mathml">$`h`$</span></span>, since it is more important that our model has perceptually orthogonal coordinates, than that the model has the same spacing within each coordinate.

Instead the following approach was used to create an error metric independent of the color space:

- For each dataset all the pairs are converted to the tested color space.
- Coordinates that are supposed to be the same within a pair are swapped to generate a new set of altered pairs:
  - For the lightness dataset, the L coordinates are swapped between the pairs, and so on.
  - These altered pair would be equal to the original pair if the model predicts the datasets perfectly.
- The perceived distance between the original colors and the altered colors are are computed using [CIEDE2000](https://en.wikipedia.org/wiki/Color_difference).
- The error for each pair is given as the minimum of the two color differences.
- The error for the entire dataset is the root mean squared error of the color differences.

Oklab was derived by optimizing the parameters of a color space with the same structure as IPT, to get a low error on all the datasets. For completeness, here is the structure of the color space – the parameters to optimize are the 3x3 matrices <span class="katex"><span class="katex-mathml">$`\mathbf{M_1}`$</span></span> and <span class="katex"><span class="katex-mathml">$`\mathbf{M_2}`$</span></span> and the positive number <span class="katex"><span class="katex-mathml">$`\gamma`$</span></span>.

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`\begin{pmatrix} l \\ m \\ s \end{pmatrix} = \mathbf{M_1} \times \begin{pmatrix} X \\ Y \\ Z \end{pmatrix}`$</span></span></span>

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`\begin{pmatrix} L \\ a \\ b \end{pmatrix} = \mathbf{M_2} \times \begin{pmatrix} l^\gamma \\ m^\gamma \\ s^\gamma \end{pmatrix}`$</span></span></span>

A couple of extra constraints were also added, since this error doesn’t alone determine the scale and orientation of the color model.

- Positive b is oriented to the same yellow color as CAM16
- D65 (normalized with <span class="katex"><span class="katex-mathml">$`Y=1`$</span></span>) should transform to <span class="katex"><span class="katex-mathml">$`L=1, a=0, b=0`$</span></span> and
- The <span class="katex"><span class="katex-mathml">$`a`$</span></span> and <span class="katex"><span class="katex-mathml">$`b`$</span></span> plane is scaled so that around 50% gray the ratio of color differences along the lightness axis and the <span class="katex"><span class="katex-mathml">$`a`$</span></span> and <span class="katex"><span class="katex-mathml">$`b`$</span></span> plane is the same as the ratio for color differences predicted by CIEDE2000.

Using these constraints a fairly good model was found, but based on the results two more changes was made. The <span class="katex"><span class="katex-mathml">$`\gamma`$</span></span> value ended up very close to 1/3, 0.323, and when looking at the sRGB gamut, the blue colors folded in on themselves slightly, resulting in a non-convex sRGB gamut. By forcing the value of <span class="katex"><span class="katex-mathml">$`\gamma`$</span></span> to 1/3 and adding a constraint the blue colors to not fold inwards, the final Oklab model was derived. The error was not noticeably affected by these restrictions.

### Comparison with other color spaces <a href="#comparison-with-other-color-spaces" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Here are the errors for the three different datasets across color spaces, given both as root mean square error and as the 95th percentile. The best performing result is highlighted in *bold* in each row (ignoring CAM16 since it is the origin of the test data). Since the lightness and chroma data was generated using CAM16 rather than being data from experiments, this data can’t be used to say which model best matches human perception. What can be said is that Oklab does a good job at predicting hue and its predictions for chroma and lightness are close to those of CAM16-UCS.

|       | Oklab    | CIELAB | CIELUV | OSA-UCS | IPT  | JzAzBz   | HSV   | CAM16-UCS |
|-------|----------|--------|--------|---------|------|----------|-------|-----------|
| L RMS | **0.20** | 1.70   | 1.72   | 2.05    | 4.92 | 2.38     | 11.59 | *0.00*    |
| C RMS | **0.81** | 1.84   | 2.32   | 1.28    | 2.18 | 1.79     | 3.38  | *0.00*    |
| H RMS | 0.49     | 0.69   | 0.68   | 0.49    | 0.48 | **0.43** | 1.10  | 0.59      |
| L 95  | **0.44** | 3.16   | 3.23   | 4.04    | 9.89 | 4.55     | 23.17 | *0.00*    |
| C 95  | **1.78** | 3.96   | 5.03   | 2.73    | 4.64 | 3.77     | 7.51  | *0.00*    |
| H 95  | 1.06     | 1.56   | 1.51   | 1.08    | 1.02 | **0.92** | 2.42  | 1.31      |

> To be able to include HSV in these comparisons, a Lab-like color space has been defined based on it, by interpreting HSV as a cylindrical color space and converting to a regular grid.
>
> JzAzBz has been used with white scaled so that Y=100. This matches the graphs in the original paper, but it is unclear if this is how it is intended to be used. (See [this colorio Github issue](https://github.com/nschloe/colorio/issues/41) for a discussion of the topic)

#### Munsell data <a href="#munsell-data" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Here is [Munsell color chart data](https://www.rit.edu/cos/colorscience/rc_munsell_renotation.php) (with V=5) plotted in the various color spaces. If a color space has a chroma prediction that matches that of the Munsell data, the rings formed by the data should appear as perfect circles. The quality of this data is a bit hard to assess, since it isn’t directly using experimental data, it is a color chart created from experimental data back in the 1940s.

Oklab and CAM16-UCS seem to predict the Munsell data well, while other spaces squash the circles in the dataset in various ways, which would indicate that Oklab does a better job than most of the color spaces of predicting chroma.

<div class="columns has-background-white-ter">

<div class="column">

**Oklab**  
<img src="/img/oklab/oklab_munsell.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 394px) min(calc(var(--main-width) * 0.7055837563451777), 278px);" decoding="async" loading="lazy" width="394" height="278" alt="Munsell plot" />

</div>

<div class="column">

**CIELAB**  
<img src="/img/oklab/cielab_munsell.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 391px) min(calc(var(--main-width) * 0.710997442455243), 278px);" decoding="async" loading="lazy" width="391" height="278" alt="Munsell plot" />

</div>

</div>

<div class="columns has-background-white-ter">

<div class="column">

**CIELUV**  
<img src="/img/oklab/cieluv_munsell.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 391px) min(calc(var(--main-width) * 0.710997442455243), 278px);" decoding="async" loading="lazy" width="391" height="278" alt="Munsell plot" />

</div>

<div class="column">

**OSA-UCS**  
<img src="/img/oklab/osa_munsell.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 391px) min(calc(var(--main-width) * 0.710997442455243), 278px);" decoding="async" loading="lazy" width="391" height="278" alt="Munsell plot" />

</div>

</div>

<div class="columns has-background-white-ter">

<div class="column">

**IPT**  
<img src="/img/oklab/ipt_munsell.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 384px) min(calc(var(--main-width) * 0.7239583333333334), 278px);" decoding="async" loading="lazy" width="384" height="278" alt="Munsell plot" />

</div>

<div class="column">

**JzAzBz**  
<img src="/img/oklab/jzazbz_munsell.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 401px) min(calc(var(--main-width) * 0.6932668329177057), 278px);" decoding="async" loading="lazy" width="401" height="278" alt="Munsell plot" />

</div>

</div>

<div class="columns has-background-white-ter">

<div class="column">

**HSV**  
<img src="/img/oklab/hsv_munsell.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 394px) min(calc(var(--main-width) * 0.7055837563451777), 278px);" decoding="async" loading="lazy" width="394" height="278" alt="Munsell plot" />

</div>

<div class="column">

**CAM16-UCS**  
<img src="/img/oklab/cam16_munsell.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 391px) min(calc(var(--main-width) * 0.710997442455243), 278px);" decoding="async" loading="lazy" width="391" height="278" alt="Munsell plot" />

</div>

</div>

#### Luo-Rigg dataset and full gamut <a href="#luo-rigg-dataset-and-full-gamut" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

These plots show three things, ellipses, scaled based on perception of color differences from the [Luo-Rigg](https://github.com/nschloe/colorio/tree/master/colorio/data/luo-rigg) dataset, the shape of the full visible gamut (the black line corresponds to pure single wavelength lights) and a slice of the sRGB gamut.

A few interesting observations are:

- The shape of the full gamut is quite odd in CIELAB and OSA-UCS, which likely means that their predictions are quite bad for highly saturated colors
- Except for CAM16-UCS the ellipses are stretched out as chroma increases. CAM16 explicitly compresses chroma to better match experimental data, which makes this data look good, but makes color blending worse

<div class="columns has-background-white-ter">

<div class="column">

**Oklab**  
<img src="/img/oklab/oklab_luo_rigg.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 394px) min(calc(var(--main-width) * 0.7055837563451777), 278px);" decoding="async" loading="lazy" width="394" height="278" alt="Luo-Rigg plot" />

</div>

<div class="column">

**CIELAB**  
<img src="/img/oklab/cielab_luo_rigg.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 397px) min(calc(var(--main-width) * 0.7002518891687658), 278px);" decoding="async" loading="lazy" width="397" height="278" alt="Luo-Rigg plot" />

</div>

</div>

<div class="columns has-background-white-ter">

<div class="column">

**CIELUV**  
<img src="/img/oklab/cieluv_luo_rigg.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 397px) min(calc(var(--main-width) * 0.7002518891687658), 278px);" decoding="async" loading="lazy" width="397" height="278" alt="Luo-Rigg plot" />

</div>

<div class="column">

**OSA-UCS**  
<img src="/img/oklab/osa_luo_rigg.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 391px) min(calc(var(--main-width) * 0.710997442455243), 278px);" decoding="async" loading="lazy" width="391" height="278" alt="Luo-Rigg plot" />

</div>

</div>

<div class="columns has-background-white-ter">

<div class="column">

**IPT**  
<img src="/img/oklab/ipt_luo_rigg.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 391px) min(calc(var(--main-width) * 0.710997442455243), 278px);" decoding="async" loading="lazy" width="391" height="278" alt="Luo-Rigg plot" />

</div>

<div class="column">

**JzAzBz**  
<img src="/img/oklab/jzazbz_luo_rigg.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 401px) min(calc(var(--main-width) * 0.6932668329177057), 278px);" decoding="async" loading="lazy" width="401" height="278" alt="Luo-Rigg plot" />

</div>

</div>

<div class="columns has-background-white-ter">

<div class="column">

**HSV**  
*Data missing. Plot broken since HSV does not handle colors outside sRGB gamut*

</div>

<div class="column">

**CAM16-UCS**  
<img src="/img/oklab/cam16_luo_rigg.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 393px) min(calc(var(--main-width) * 0.7073791348600509), 278px);" decoding="async" loading="lazy" width="393" height="278" alt="Luo-Rigg plot" />

</div>

</div>

#### Blending colors <a href="#blending-colors" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Here are plots of white blended with a blue color, using the various color spaces tested. The blue color has been picked since it is the hue with the most variation between spaces. CIELAB, CIELUV and HSV all show hue shifts towards purple. CAM16 has a different issue, with the color becoming desaturated quickly, resulting in a transition that doesn’t look as even as some of the other ones.

<div class="columns has-background-white-ter">

<div class="column">

**Oklab**  
<img src="/img/oklab/oklab_blend.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 349px) min(calc(var(--main-width) * 0.4584527220630373), 160px);" decoding="async" loading="lazy" width="349" height="160" alt="Blend plot" />

</div>

<div class="column">

**CIELAB**  
<img src="/img/oklab/cielab_blend.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 349px) min(calc(var(--main-width) * 0.4584527220630373), 160px);" decoding="async" loading="lazy" width="349" height="160" alt="Blend plot" />

</div>

<div class="column">

**CIELUV**  
<img src="/img/oklab/cieluv_blend.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 349px) min(calc(var(--main-width) * 0.4584527220630373), 160px);" decoding="async" loading="lazy" width="349" height="160" alt="Blend plot" />

</div>

<div class="column">

**OSA-UCS**  
<img src="/img/oklab/osa_blend.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 349px) min(calc(var(--main-width) * 0.4584527220630373), 160px);" decoding="async" loading="lazy" width="349" height="160" alt="Blend plot" />

</div>

</div>

<div class="columns has-background-white-ter">

<div class="column">

**IPT**  
<img src="/img/oklab/ipt_blend.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 349px) min(calc(var(--main-width) * 0.4584527220630373), 160px);" decoding="async" loading="lazy" width="349" height="160" alt="Blend plot" />

</div>

<div class="column">

**JzAzBz**  
<img src="/img/oklab/jzazbz_blend.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 349px) min(calc(var(--main-width) * 0.4584527220630373), 160px);" decoding="async" loading="lazy" width="349" height="160" alt="Blend plot" />

</div>

<div class="column">

**HSV**  
<img src="/img/oklab/hsv_blend.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 349px) min(calc(var(--main-width) * 0.4584527220630373), 160px);" decoding="async" loading="lazy" width="349" height="160" alt="Blend plot" />

</div>

<div class="column">

**CAM16-UCS**  
<img src="/img/oklab/cam16_blend.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 349px) min(calc(var(--main-width) * 0.4584527220630373), 160px);" decoding="async" loading="lazy" width="349" height="160" alt="Blend plot" />

</div>

</div>

## Conclusion <a href="#conclusion" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

This post has introduced the Oklab color space, a perceptual color space for image processing. Oklab is able to predict perceived lightness, chroma and hue well, while being simple and well-behaved numerically and easy to adopt.

In future posts I want to look into using Oklab to build a better perceptual color picker and more.

------------------------------------------------------------------------

> *Oklab and the images in this post have been made using [python](https://www.python.org/), [jupyter](https://jupyter.org/), [numpy](https://numpy.org/), [scipy](https://www.scipy.org/) [matplotlib](https://matplotlib.org/), [colorio](https://github.com/nschloe/colorio) and [colour](https://github.com/colour-science/colour).*

------------------------------------------------------------------------

If you liked this article, it would be great if you considered sharing it:

<div class="buttons">

<a href="https://twitter.com/intent/tweet/?text=A%20perceptual%20color%20space%20for%20image%20processing&amp;url=https%3A%2F%2Fbottosson.github.io%2Fposts%2Foklab%2F" class="is-small button resp-sharing-button--twitter" rel="noopener" target="_blank" aria-label="Share on Twitter"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNMjMuNDQgNC44M2MtLjguMzctMS41LjM4LTIuMjIuMDIuOTMtLjU2Ljk4LS45NiAxLjMyLTIuMDItLjg4LjUyLTEuODYuOS0yLjkgMS4xLS44Mi0uODgtMi0xLjQzLTMuMy0xLjQzLTIuNSAwLTQuNTUgMi4wNC00LjU1IDQuNTQgMCAuMzYuMDMuNy4xIDEuMDQtMy43Ny0uMi03LjEyLTItOS4zNi00Ljc1LS40LjY3LS42IDEuNDUtLjYgMi4zIDAgMS41Ni44IDIuOTUgMiAzLjc3LS43NC0uMDMtMS40NC0uMjMtMi4wNS0uNTd2LjA2YzAgMi4yIDEuNTYgNC4wMyAzLjY0IDQuNDQtLjY3LjItMS4zNy4yLTIuMDYuMDguNTggMS44IDIuMjYgMy4xMiA0LjI1IDMuMTZDNS43OCAxOC4xIDMuMzcgMTguNzQgMSAxOC40NmMyIDEuMyA0LjQgMi4wNCA2Ljk3IDIuMDQgOC4zNSAwIDEyLjkyLTYuOTIgMTIuOTItMTIuOTMgMC0uMiAwLS40LS4wMi0uNi45LS42MyAxLjk2LTEuMjIgMi41Ni0yLjE0eiIgLz48L3N2Zz4=" /> </span></a><a href="mailto:?subject=A%20perceptual%20color%20space%20for%20image%20processing&amp;body=https%3A%2F%2Fbottosson.github.io%2Fposts%2Foklab%2F" class="is-small button resp-sharing-button--email" rel="noopener" target="_self" aria-label="Share by E-Mail"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNMjIgNEgyQy45IDQgMCA0LjkgMCA2djEyYzAgMS4xLjkgMiAyIDJoMjBjMS4xIDAgMi0uOSAyLTJWNmMwLTEuMS0uOS0yLTItMnpNNy4yNSAxNC40M2wtMy41IDJjLS4wOC4wNS0uMTcuMDctLjI1LjA3LS4xNyAwLS4zNC0uMS0uNDMtLjI1LS4xNC0uMjQtLjA2LS41NS4xOC0uNjhsMy41LTJjLjI0LS4xNC41NS0uMDYuNjguMTguMTQuMjQuMDYuNTUtLjE4LjY4em00Ljc1LjA3Yy0uMSAwLS4yLS4wMy0uMjctLjA4bC04LjUtNS41Yy0uMjMtLjE1LS4zLS40Ni0uMTUtLjcuMTUtLjIyLjQ2LS4zLjctLjE0TDEyIDEzLjRsOC4yMy01LjMyYy4yMy0uMTUuNTQtLjA4LjcuMTUuMTQuMjMuMDcuNTQtLjE2LjdsLTguNSA1LjVjLS4wOC4wNC0uMTcuMDctLjI3LjA3em04LjkzIDEuNzVjLS4xLjE2LS4yNi4yNS0uNDMuMjUtLjA4IDAtLjE3LS4wMi0uMjUtLjA3bC0zLjUtMmMtLjI0LS4xMy0uMzItLjQ0LS4xOC0uNjhzLjQ0LS4zMi42OC0uMThsMy41IDJjLjI0LjEzLjMyLjQ0LjE4LjY4eiIgLz48L3N2Zz4=" /> </span></a><a href="https://reddit.com/submit/?url=https%3A%2F%2Fbottosson.github.io%2Fposts%2Foklab%2F&amp;resubmit=true&amp;title=A%20perceptual%20color%20space%20for%20image%20processing" class="is-small button resp-sharing-button--reddit" rel="noopener" target="_blank" aria-label="Share on Reddit"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNMjQgMTEuNWMwLTEuNjUtMS4zNS0zLTMtMy0uOTYgMC0xLjg2LjQ4LTIuNDIgMS4yNC0xLjY0LTEtMy43NS0xLjY0LTYuMDctMS43Mi4wOC0xLjEuNC0zLjA1IDEuNTItMy43LjcyLS40IDEuNzMtLjI0IDMgLjVDMTcuMiA2LjMgMTguNDYgNy41IDIwIDcuNWMxLjY1IDAgMy0xLjM1IDMtM3MtMS4zNS0zLTMtM2MtMS4zOCAwLTIuNTQuOTQtMi44OCAyLjIyLTEuNDMtLjcyLTIuNjQtLjgtMy42LS4yNS0xLjY0Ljk0LTEuOTUgMy40Ny0yIDQuNTUtMi4zMy4wOC00LjQ1LjctNi4xIDEuNzJDNC44NiA4Ljk4IDMuOTYgOC41IDMgOC41Yy0xLjY1IDAtMyAxLjM1LTMgMyAwIDEuMzIuODQgMi40NCAyLjA1IDIuODQtLjAzLjIyLS4wNS40NC0uMDUuNjYgMCAzLjg2IDQuNSA3IDEwIDdzMTAtMy4xNCAxMC03YzAtLjIyLS4wMi0uNDQtLjA1LS42NiAxLjItLjQgMi4wNS0xLjU0IDIuMDUtMi44NHpNMi4zIDEzLjM3QzEuNSAxMy4wNyAxIDEyLjM1IDEgMTEuNWMwLTEuMS45LTIgMi0yIC42NCAwIDEuMjIuMzIgMS42LjgyLTEuMS44NS0xLjkyIDEuOS0yLjMgMy4wNXptMy43LjEzYzAtMS4xLjktMiAyLTJzMiAuOSAyIDItLjkgMi0yIDItMi0uOS0yLTJ6bTkuOCA0LjhjLTEuMDguNjMtMi40Mi45Ni0zLjguOTYtMS40IDAtMi43NC0uMzQtMy44LS45NS0uMjQtLjEzLS4zMi0uNDQtLjItLjY4LjE1LS4yNC40Ni0uMzIuNy0uMTggMS44MyAxLjA2IDQuNzYgMS4wNiA2LjYgMCAuMjMtLjEzLjUzLS4wNS42Ny4yLjE0LjIzLjA2LjU0LS4xOC42N3ptLjItMi44Yy0xLjEgMC0yLS45LTItMnMuOS0yIDItMiAyIC45IDIgMi0uOSAyLTIgMnptNS43LTIuMTNjLS4zOC0xLjE2LTEuMi0yLjItMi4zLTMuMDUuMzgtLjUuOTctLjgyIDEuNi0uODIgMS4xIDAgMiAuOSAyIDIgMCAuODQtLjUzIDEuNTctMS4zIDEuODd6IiAvPjwvc3ZnPg==" /> </span></a><a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbottosson.github.io%2Fposts%2Foklab%2F&amp;t=A%20perceptual%20color%20space%20for%20image%20processing" class="is-small button resp-sharing-button--hackernews" rel="noopener" target="_blank" aria-label="Share on Hacker News"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQwIDE0MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBoZWlnaHQ9IjI0IiB3aWR0aD0iMjQiPjxwYXRoIGQ9Ik02MC45NCA4Mi4zMTRMMTcgMGgyMC4wOGwyNS44NSA1Mi4wOTNjLjM5Ny45MjcuODYgMS44ODggMS4zOSAyLjg4My41My45OTQuOTk1IDIuMDIgMS4zOTMgMy4wOC4yNjUuNC40NjMuNzY0LjU5NiAxLjA5NS4xMy4zMzQuMjYyLjYzLjM5NS44OTguNjYyIDEuMzI1IDEuMjYgMi42MTggMS43OSAzLjg3Ny41MyAxLjI2Ljk5MyAyLjQyIDEuMzkgMy40OCAxLjA2LTIuMjU0IDIuMjItNC42NzMgMy40OC03LjI1OCAxLjI2LTIuNTg1IDIuNTUyLTUuMjcgMy44NzctOC4wNTJMMTAzLjQ5IDBoMTguNjlMNzcuODQgODMuMzA4djUzLjA4N2gtMTYuOXYtNTQuMDh6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+PC9zdmc+" /> </span></a><a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fbottosson.github.io%2Fposts%2Foklab%2F&amp;title=A%20perceptual%20color%20space%20for%20image%20processing&amp;source=https%3A%2F%2Fbottosson.github.io%2Fposts%2Foklab%2F" class="is-small button resp-sharing-button--linkedin" rel="noopener" target="_blank" aria-label="Share on LinkedIn"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNNi41IDIxLjVoLTV2LTEzaDV2MTN6TTQgNi41QzIuNSA2LjUgMS41IDUuMyAxLjUgNHMxLTIuNCAyLjUtMi40YzEuNiAwIDIuNSAxIDIuNiAyLjUgMCAxLjQtMSAyLjUtMi42IDIuNXptMTEuNSA2Yy0xIDAtMiAxLTIgMnY3aC01di0xM2g1VjEwczEuNi0xLjUgNC0xLjVjMyAwIDUgMi4yIDUgNi4zdjYuN2gtNXYtN2MwLTEtMS0yLTItMnoiIC8+PC9zdmc+" /> </span></a><a href="https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbottosson.github.io%2Fposts%2Foklab%2F" class="is-small button resp-sharing-button--facebook" rel="noopener" target="_blank" aria-label="Share on Facebook"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNMTguNzcgNy40NkgxNC41di0xLjljMC0uOS42LTEuMSAxLTEuMWgzVi41aC00LjMzQzEwLjI0LjUgOS41IDMuNDQgOS41IDUuMzJ2Mi4xNWgtM3Y0aDN2MTJoNXYtMTJoMy44NWwuNDItNHoiIC8+PC9zdmc+" /></span></a>

</div>

For discussions and feedback, <a href="https://twitter.com/bjornornorn" rel="noopener" target="_blank">ping me on Twitter.</a>

Published 23 Dec 2020

</div>

</div>
