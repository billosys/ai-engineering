# Staged colour-conversion proof

## Scope and model

This proof uses the pinned prepared Oklab article at SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`, local source SHA-256 `ffe5494da6f0d040fb341d8e1f03d3e396600f6787088b6d57e32613798375f4`. The article’s 2021-01-25 linear-sRGB generation defines `A` (combined linear-sRGB→LMS coefficients) and `B` (LMS-prime→Oklab coefficients). For a linear RGB vector `v`,

`F_linear(v) = B · cbrt_signed(A · v)`,

where the root is applied componentwise as the real signed cube root. For encoded sRGB `c`, `F_encoded(c)=F_linear(d(c))`, with `d` the piecewise sRGB decoding function. The reverse operation applies the published inverse LMS-prime transform, componentwise cubes, the published inverse A, and, for encoded return values, the sRGB encoding function. The actual coefficients and all case values are recorded in [numerical-reconciliation.md](numerical-reconciliation.md).

The distinct XYZ generation uses its separately printed matrix `M1`: `F_XYZ(x)=B·cbrt_signed(M1·x)`. It is not the combined RGB matrix A. The article says the sRGB coefficients were updated on 2021-01-25 and cautions that applications may use their own sRGB matrices. This proof does not assert exact equivalence across matrix generations.

## Why the whole operation is not one matrix

For any positive scalar `λ`, linearity of A gives `A(λv)=λAv`. The signed real cube root is homogeneous for positive `λ`, so componentwise `cbrt(λx)=λ^(1/3)cbrt(x)`. B is linear. Therefore:

`F_linear(λv)=B·cbrt(λAv)=λ^(1/3) B·cbrt(Av)=λ^(1/3)F_linear(v)`.

A linear map `M` would instead satisfy `M(λv)=λM(v)`. Choose nonzero white `v=(1,1,1)` and `λ=1/8`: the staged output’s lightness changes from approximately `0.999999993474` to `0.499999996737`, a factor of one half; a single linear map would scale every output component by one eighth. Thus the whole pipeline is not one constant 3×3 linear matrix. Adjacent linear stages can be multiplied together, which explains the article’s combined RGB→LMS coefficients; that composition cannot cross the componentwise nonlinear root.

For encoded sRGB, decoding is another required nonlinear stage before A. The numerical control in [numerical-reconciliation.md](numerical-reconciliation.md) shows that omitting it changes middle-gray L from approximately `0.598180726623` to `0.793700520804`. The signed root also matters: the XYZ Z-basis produces negative first LMS, and a naive fractional power is non-real in ordinary real arithmetic. No clipping is part of these identities.

## Rectangular and polar coordinates

For Oklab `(L,a,b)`, the analytic polar representation is `C=hypot(a,b)` and `H=atan2(b,a)` converted to degrees modulo 360. Reconstruction is `(L,C cos H,C sin H)`. Hue is undefined only when `C` is exactly zero in this mathematical diagnostic. Rounded coefficients leave small nonzero chroma for nominally neutral cases, so their calculated hue is unstable and not meaningful. The 20-case reconstruction results are recorded in the numerical artifact.

CSS Color 4 separately defines powerless hue using a chroma epsilon and handles missing hue in its conversion rules. That implementation convention is not substituted into the analytic round-trip predicate. Parsing, missing-component interpolation, gamut mapping, clipping, alpha/compositing, and browser behavior are separate concerns.

## Claim boundary

The identities establish the structure and scaling behavior of this specified mathematical model. They do not establish equal perceived brightness for every hue, observer, or context; a uniquely best design space; universal contrast; palette quality; or an identity between colour conversion and equal temperament. “Approximately perceptual under the identified model” is a scoped characterization. The musical comparison can remain an analogy without claiming identical mechanisms. CSS’s dated draft discussion describes relative perceptual advantages, not a universal brightness guarantee. Practical colour decisions still depend on source space and white point, target gamut, alpha and background compositing, and review of actual foreground/background/state pairs. This slice supplies no palette defaults or accessibility certification.

## Reproduction pointer

The standard-library binary64 extraction and full 13 encoded, 3 linear, 4 XYZ, 16 inverse, 20 polar and 3 contrary-control reconciliation are in [numerical-reconciliation.md](numerical-reconciliation.md). Exact pinned local spans and dated public source observations are in [execution-notes.md](execution-notes.md).
