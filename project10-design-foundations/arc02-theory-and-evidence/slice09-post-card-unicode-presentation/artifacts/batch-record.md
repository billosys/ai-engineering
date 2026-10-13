# Arc02 Slice09 — batch record

## Intake and source-cited contract readback

Assignment: the initial [Slice09 prompt](../cc-prompt.md), issued by planning
commit `58d7502116ce00c26dbeb03796dd24cca01de872` (predecessor `eac665f569d269b6a913e2f9349ef3e73656781e`), against source input
`c4cc74279ac845003b0c80f55907981241c58a99`. The planning worktree was clean at intake; main was at the
pinned source revision with only the pre-existing untracked `knowledge/lfe/`
directory. No source or planning writes occurred before preflight completed.

**Required-text coverage.** Read the prompt, Slice09 plan and four-row ledger
completely. Read the named Project10 sections and all thirteen criterion rows;
read Arc02's capability, accepted-inputs, slice-breakdown and workflow sections
and all ten criterion rows. Read Arc06's hosted CDC return completely, the
specified Slice02 plan sections, six-row ledger and closing report completely,
and the batch record's hosted-boundary and postpublication sections completely.
Read current `knowledge/design/SKILL.md`, sibling history and source
`AGENTS.md` completely. Read concept-cards guide08's review definition,
structural validation, recoverability and false-upgrade sections;
work-verification independent-review, ledger-discipline, row-closure and
evidence-strength guidance; project-management SKILL/README and Expedited Mode;
and engineering-methods guide07 CC intake. No conditional input was missing.

**Required-data coverage.** Loaded the immutable Arc06 bridge from `eac665f569d269b6a913e2f9349ef3e73656781e`
and verified SHA-256 `3b990a637074cf19dfcecd8709e2712ccaefb394d0e85c44b20ed36e34f9041b`. It contains 233 unique card records and 46
post-card paths. Resolved every final source hash at `c4cc74279ac845003b0c80f55907981241c58a99`. Projected
all 46 bodies' complete `\uXXXX` matches with full matching-line contexts and
per-token frequencies; the 23 whitelisted tokens occur 1,062 times exactly as
prescribed, with no other `\uXXXX` token. Inspected the code-bearing witnesses:
Matrix's `3×3` and inverse formulas, feColorMatrix's illustrative SVG ellipsis,
and mix-blend-mode's multiplication/division/subtraction formulas. The
feColorMatrix ellipsis is display punctuation, as the prompt specifies. This
inspection establishes the representation scope, not formula validity or a
five-dimension semantic review.

**Contract readback.** Only the 23 listed six-byte ASCII tokens after each
existing YAML closing delimiter become their specified Unicode characters in
the 46 post bodies. The complete frontmatter prefixes and all 187 other card
files stay byte-identical; every other body byte, newline, number, claim,
reference, Markdown construct and existing Unicode character stays exact.
Only the design skill's owning metadata version and paired sibling-history
entry change. The equality oracle is original prefix plus exact whitelisted body
replacements; count-only or converter-owned output is insufficient. We exercised
the same oracle against a remaining active Matrix escape, a changed metadata
field and a changed unrelated body number. This is a display correction only.

### Per-token frequency projection

| Input token | Display character | Occurrences |
|---|---:|---:|
| `\u00b0` | ° | 5 |
| `\u00b2` | ² | 10 |
| `\u00b3` | ³ | 2 |
| `\u00b7` | · | 29 |
| `\u00b9` | ¹ | 10 |
| `\u00d7` | × | 53 |
| `\u00e9` | é | 1 |
| `\u00f6` | ö | 13 |
| `\u00f7` | ÷ | 2 |
| `\u03b3` | γ | 5 |
| `\u03c6` | φ | 21 |
| `\u2013` | – | 40 |
| `\u2014` | — | 734 |
| `\u2026` | … | 1 |
| `\u207b` | ⁻ | 10 |
| `\u207f` | ⁿ | 1 |
| `\u2192` | → | 90 |
| `\u2194` | ↔ | 5 |
| `\u2208` | ∈ | 5 |
| `\u2212` | − | 11 |
| `\u221a` | √ | 2 |
| `\u2248` | ≈ | 11 |
| `\u2260` | ≠ | 1 |

Totals: 23 tokens, 1,062 matches; the frequencies equal the prompt's per-token
input expectations exactly.

## Prewrite reconciliation and source mutation

The pinned bridge is the sole source roster. All 233 current whole-file hashes
match its `revisions.final.sha256`; the 46 post-card sources also match the
recorded body hashes, byte offsets and closing-delimiter lines. The complete
source allowlist is the 46 bridge post paths plus `knowledge/design/SKILL.md`
and `knowledge/design/version-history.md` (48 paths). The entrypoint/history
input hashes match their pins; metadata was1.0.5 with a paired 1.0.5 history
entry. No other source drift or unlisted token was found.

The source commit is `589d7c21bd6c9a415b921b80479822561861fa79` (parent `c4cc74279ac845003b0c80f55907981241c58a99`), with exactly
those 48 paths and both required co-author trailers. All 233 metadata prefixes
remain byte-exact; all 187 non-post card files remain whole-file identical. The
46 body transforms replace 1,062 occurrences across 23 tokens and reduce body
bytes by 3,337 total. All 46 remain valid UTF-8 and preserve input line counts;
reapplying the whitelist changes no bytes. The paired skill version is now 1.0.6.

| Post-card path | Input whole (SHA-256 / bytes) | Corrected whole (SHA-256 / bytes) | Input body (SHA-256 / bytes) | Corrected body (SHA-256 / bytes) | Unchanged header SHA-256 | Closing delimiter line / body offset | Replacements |
|---|---|---|---|---|---|---:|---:|
| `knowledge/design/concept-cards/posts/additive-colour-mixing.md` | `31ce444f48f7b9340d285e6ce21925c8a59c41be3a54732e2139839fb58d575a` / 5547 | `2d3ed53e668a6e39d0d1e8c7d6712f994db25e55f705f93f437ada45d82fbc3f` / 5502 | `afb287818f82160c3075d25bd9ed8ec7b0884e9ce059566aa3c6fcfe17bf4d48` / 4533 | `d11ce7093c516ba1e5c9f2165c551e19eb3975d27355446485651cb41b489491` / 4488 | `57c3f9a2b1120d296e317ea9313fbf8203501e3caa0260df2b05561661962b82` | 37 / 1014 | 15 |
| `knowledge/design/concept-cards/posts/chroma-perceptual.md` | `b6f051b831c2c82e245c4d161bce59203b6b6f3e674841a175f7285a740b25c9` / 6635 | `743720854a5b6a2df5f07c1dcd0ecd2fe63b3ba48c577aeaf4747d2b6c298507` / 6567 | `2f9219c65e5ad494ffe43974493f4933ab8aadaec88a4c79463e42a32d08a683` / 5733 | `2fc06f9e78a0d018f12168f8666819cca57399181b08ca17032b3d167c32bde9` / 5665 | `f78ac275cf8ba40b012672e3518be9d6c7583f4f9fc174597c38f93f52c76656` | 35 / 902 | 20 |
| `knowledge/design/concept-cards/posts/chroma-vs-saturation.md` | `2ee5b9608d9203de94894721fdd99d2a65300df3ffd6f228acc105c5bf3707a2` / 6159 | `59d598326c6e2c8c0b89134e671eba0254c168eddaaca1ac7b7e788f09572c77` / 6107 | `2530fc9fe968c89d0570ab8f520e38d66b53dc6e0866dda9beea27b53e5ae618` / 5387 | `c9e5d1d737b508ee989d0927a9c9001888503c1ae02fcbc28b9cd9c83aa3726c` / 5335 | `608c51ffdd4e590108be3cad70ae4e4f2cc57d5b07bde27de771bfe20f23193f` | 34 / 772 | 17 |
| `knowledge/design/concept-cards/posts/colour-bit-depth.md` | `5a2890c0348a211191bb3a7eb812de9b393d54300d5fc5da9e7fb399bc2b5c01` / 5117 | `3c31d8821a094f07fa88ca4a43d2bade008da201eeb5ab23807db854dc2af74d` / 5061 | `8d46d07a4436e13fdbbf2086ae458cfaf019fb494aa15f0145c3c65f7ddf20bc` / 4168 | `e5d0081c4f4f51c73f32e042fea294d97d295d78cfa400c8bcb64c974037f21d` / 4112 | `a45ae27aed774d739a81b18c77ae184d1b016e8f49e9020e1cb3d54de07a9abb` | 36 / 949 | 18 |
| `knowledge/design/concept-cards/posts/colour-contrast.md` | `0ade13b60e02e13fcdd279560232fd2a649f628b6a16fbb702b2bf0b8e1df6c6` / 6422 | `18db7bf0f2759888994bf69c03710c355414601e878f156985fffe299644f194` / 6386 | `7ab8bc132d7826f34a49c2f3cd4bca098059c718389eba826f1de153aa8eb24a` / 5507 | `414a406ba83c3ab81d0e8ec665d1e01e60269811e4fd75d79e6366904327e2f4` / 5471 | `167772e6cdb66476ceee20f4a36797213c2bdfbd4e00765903d1982291c2898d` | 38 / 915 | 12 |
| `knowledge/design/concept-cards/posts/colour-gamut.md` | `8cd71ebf7b63945a3957b4caeb8f6a911dce7b372f40f425cfeacfedf21041a9` / 5358 | `3a6bb3b37ffd7000b8698a783561f3b4ab7f44442c3cdfc07072445c9fc818a6` / 5316 | `298b7c90f000f892a0f19446991238ecd62f777076be1e6e49b02e7a2c52cae5` / 4726 | `21fb0d92ba049fa65c2a50beb9eecf37b9a6a66353f98942f52caf177930241a` / 4684 | `2f86d6b54badb158f671452ad248a5c9f781d84b103df7bae29d2ee0183ec7ef` | 33 / 632 | 13 |
| `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | `6dcdad24222445e500d29ccc5e6c8fc0f7e25045d3599f007f0739c49ed520ea` / 8246 | `e0d02a1d8dc63eea7f5dc86761696e500079d60e477b0c008d6ab8a2ce7bde2c` / 8135 | `adf085f8087d93ce5344882a18252157bd9357a3f7ab6abc7a86ee569adb4bfc` / 6771 | `b4fbfe07aab947f0bef5eb1848e4b0cc4aa6dbcbeea64e653596ab8cbace3245` / 6660 | `08d84ead655d77a97103de1ce1ad7b18b796610e72ca533894370c0b77397531` | 46 / 1475 | 34 |
| `knowledge/design/concept-cards/posts/colour-picker-design-principles.md` | `2be6583ba3605b1b243aba56264762ca562934d480dc2dc9147526f233f8b497` / 6612 | `4ceabe9e2123d075f22ed489cad8f383eaf6e07b53f93cfff5a58107598e6fa1` / 6539 | `3bdb8630d1f459d1d82241f8b722f086dcaf69ab7699be709dc27e907969bcfd` / 5835 | `d18df1f82b179d8f288fcee34178bdc37fed617d629f163a2671ed018e632834` / 5762 | `c4ead415998d972b0de2371e225ed4506a98d104483b6a84428f737a279b17a4` | 36 / 777 | 24 |
| `knowledge/design/concept-cards/posts/colour-picker.md` | `90a4e6cbb445615ca26b6a95b929e6f237c99d4894ee6e7bc3c902dbd4c41b2c` / 5706 | `a81924852555d07b93c09dc3612f4820e535149c06f0cb4918d7fc7d504dfbf6` / 5664 | `e09f49a5a090188d53fed28aa9d8f0c43d870c85602ace5f08716aa727e133c2` / 4879 | `978b851b6650da7d24f2b039e1ff7b724af74e498972234e0f8a22e2509fc46e` / 4837 | `056bca8fb41c53af32d8bbf9379992b960ea04c9e2377d8ffdd8623a8c07995f` | 39 / 827 | 13 |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `3fc525d46cfe4f658c2133795295349f331c668255cf40f0d2831b74d07d3a5e` / 7538 | `3a66f268239f22e89c52e111fbe8e9a5a7b5b54f88ae416184951a1e174f9b74` / 7493 | `a53cf63003113ed176aae89975bb1fc39a10f6267d04169ad33cf08e41223c06` / 6442 | `0fd9e7ad8fea6266e4d3c4f48c733a126678ede85f3cf323661becce089fe5b2` / 6397 | `c646de27225dba250e219ec7ce28dc8db001bf4d40fa17dd8afc971fb4a8942a` | 42 / 1096 | 15 |
| `knowledge/design/concept-cards/posts/colour-space.md` | `98a71235a8ec662db69652663c9fbd3280984b3aff35914c3337fee1e8d992ec` / 5694 | `6540c99331d77c09d09770f562aa3b239604f0f75fd7f026e8d2d10da379e9ca` / 5655 | `c59a6bd6a167460d192cf205f4f69b63d41795a0fc1d6c14c24af3afe4e70d88` / 5019 | `b87a393f12edbec72782e8a3937c13a8b42e63e8d2b0241b314bb19b104c171a` / 4980 | `798b42f84f19c25facee2f2fee54a265cc889b4c54052f4ec4127a85469e0485` | 28 / 675 | 13 |
| `knowledge/design/concept-cards/posts/css-colour-custom-properties.md` | `8e94ee62f4570d27ba65162b8cce4061f4765787207201d4604b01fac3d0a5f3` / 7171 | `96c88a186ddb8b1d64e96be34a9a03b4ca083adea8b1672611f0787fd877bbcd` / 7114 | `587865c09db390256b41250e05966aea202ac8a3b33224686fad54a82091354c` / 5926 | `3ec4e2bc7f222b716b27345e0c1d2e07b714191d0abfeb2185b5520e94a97833` / 5869 | `4c05ad58ce005bd4282670d42e6cbab52d7adbd0605207690dc149b1291ce8a0` | 38 / 1245 | 19 |
| `knowledge/design/concept-cards/posts/css-rgba.md` | `ecf456b30896bc0b0e0c092eb892ade948290fcd43f97fdb7f3ddc763b01f859` / 4451 | `35722317b25a8a84af13e64508ea7ba7c5ec38ab8cd8ea433a26c0d567f70e77` / 4421 | `c528b95a69249e335189239ee96a5ef91ea25a1061bd499f086311b1bb03c2c0` / 3575 | `de9931dc306b9e9bba29f09be39ab7e5df468b5062d40a5948b8448bc1b60621` / 3545 | `c002f5253077c2a539e14a41cee7406a8071d04eafa87734ca1d10866cced3ae` | 41 / 876 | 10 |
| `knowledge/design/concept-cards/posts/d65-whitepoint.md` | `3427c25e857536fcac86f784cc7f454e8179767b0207970ccafceb776bf563a4` / 4926 | `0574b5f1f95029efc5d0c8690c7483e94fb0b09071c4f364c900335b7434b6c7` / 4890 | `6148f6b3fc20c6faace088c600c88b1805f01e2cf2c08eb97928ad498c966e79` / 4272 | `13a55209e765b03af15b69c92c09457e2e170da2c388b0538fa2b7cfc60a5da9` / 4236 | `37865d764993ec3dddab6ba1ac6a5ca1c753cba9d730dd0b16adec95496fe699` | 29 / 654 | 12 |
| `knowledge/design/concept-cards/posts/fecolormatrix.md` | `d3f67496299c65293c354255a1cd4d6c4eb4e64a852027b5512d7a8fd2513dde` / 7439 | `605a00f8b3461353d61fda60b082d8cc5fd24306401289bba87432d7bbee48d0` / 7376 | `af92d57e6a83c0a406d8407fdbae2e6ff7d8c532f03c0fa99abe5092cc993165` / 6420 | `d9d77ea515848531864467ace75b266f4c8ce4a9df0e7704ec2bd60144f80bfb` / 6357 | `45fd3c9fa76281b636506bb7cbbc988d7886ef1eb33c397eeec8e161a39ec092` | 36 / 1019 | 19 |
| `knowledge/design/concept-cards/posts/gamut-srgb.md` | `549793726e78a1554f96ed7adde564d55be1c7fa167f11f167641f671e940d73` / 6539 | `b99f8827f7f62582da7663a80b503b9c98c52f57a3e4b827770fd4e22e465560` / 6483 | `d4a8cc0dca8139d9c6be9331a16d3dce4505f93cc9517631bf7ff3d1f1be7e4b` / 5731 | `1fb8dfea8516e71b346f53da35cb847356fff58ea3dec9e20f44dc0846b2f245` / 5675 | `47e4d2142ac69af2dd328d0ea41660b2b1caeff5ecdfabb9386b9f28ad576501` | 35 / 808 | 18 |
| `knowledge/design/concept-cards/posts/golden-ratio.md` | `fdbd4a60b4d6e4d92cb56dc6fc85267d7f4520d282b01705cab514f945f755d1` / 9472 | `d4c6b251f4c3f64e707f0a5c5e221ce5cc0364f13da310857283a7d99bcdbef3` / 9337 | `c90d97499fa66cdf0116a9bcfe8709bddf2e92994167c0d4f7c141a427fe2280` / 7718 | `539dcda7acc264bf73bb1ce36c2872f046ff4c3a9614d5ed912fdd3837e84900` / 7583 | `5040bc5398c57834ce947cd5c4df09c9971c1ba540ece473760a16cd10db3474` | 48 / 1754 | 39 |
| `knowledge/design/concept-cards/posts/gradient-colour-interpolation.md` | `e4d9cdc9f3f8d962ce339599a92412dde6b6937bfa2103b4d68efe46972c8fef` / 6545 | `c6632af80fbcaf53ca0251837379ac73be858bc4e00beef2e14461e3a6865de5` / 6500 | `8d63ae4d5ff3ac36077819339068021f3d5f75132d61b6f11cb43af47d79abd9` / 5448 | `bb3c7d86dc13ee2c2427a3b0d154308ae57cecc9ac1890996d0f6b03ca3324a0` / 5403 | `8f8521b89cb892e6c1a6f37d826e3c68bc36af5e6d7aef80847779e0abbc258f` | 38 / 1097 | 15 |
| `knowledge/design/concept-cards/posts/hex-colour-notation.md` | `7901e1bf53cadb70dd31a931d389c3434cc76d41fae82c55113cf9ab12a2e59e` / 5934 | `b1d3f79a64d8add23da24550f3661a3adf65c2cd20ce59bb83cf36eba5d99f89` / 5864 | `fe259bffbcfada93761bae65c600a6f18fd74d898d4a31b559c31acc48656524` / 4897 | `52ee3efcf1a58990fb93020f83be8f10c4c72665023429f923bd358a24c97818` / 4827 | `b47de58cf966eda7a72a38116ceeb53e38e9f613104eb1255cd1c1f6235f6b2d` | 39 / 1037 | 23 |
| `knowledge/design/concept-cards/posts/hsl-css-syntax.md` | `ae2e9827058f0aed181daa102fa4af8904948eec2c4421836d2c686d96126557` / 5295 | `57b63d3753be742b1b4b2fb4c06f8fd600e4e936ca6d14aa526e8a1c896dc1ac` / 5232 | `873c9d1f0e2f2fb1aa1f5d1ff5d7a8dbd8b956f8f3805ce87bdefb256aef5126` / 4356 | `8abf97c5d3dbc133dfa08baecf35246021be9ce0ddd64a9af2959c1041762dde` / 4293 | `59c9fe38d6a5aeaecea1d609996032f6529be9f3badaf6aeedb35d1b088d51cc` | 44 / 939 | 21 |
| `knowledge/design/concept-cards/posts/hsl.md` | `a9a805e446de2a4c6eab647e4c41e89184015d95c93e2a9f82223c3586123cb1` / 6326 | `51233bb126106409fd85fcd01abc47addd447ad7b3aed0772381126c7a08ddfe` / 6263 | `18061fcec58e3a914b689f132043d179d294c1fc99d2d30ce88534987b6400af` / 5466 | `b6195dfea3986c3df2db29e7d9ea91c791912ed5ab0f4d26fce71cad37a69e52` / 5403 | `3b3ddeb3d5de4ac29d32eb87b0918678578c1cab85a090dfb7566e2dd445e1e8` | 41 / 860 | 21 |
| `knowledge/design/concept-cards/posts/hsv.md` | `4acf5b8d0a0733be7c9926f8de2c46481668aada41c9fb381f1357e15dbe63d2` / 5863 | `48460e04f3b4ac21d0497a7c30f1c6d508c4d547ceed7b5c9533c41e8716c347` / 5823 | `5040d3c0fd3140ac0f12b27da17258b51a72639613931e88651ed7c4030509e3` / 5187 | `ed1af7e99a636a21314cad56be305219370e0304a5ca7e6666cbeff0cf7ca534` / 5147 | `ca312c3672821658dfe232b3f4c3e3fd0ad855008cd8708b8a56912457a61547` | 34 / 676 | 13 |
| `knowledge/design/concept-cards/posts/lightness-perceptual.md` | `d3dc753562179211f48fd7ec09686a77c281842cc70f8404884789333c191d2e` / 6614 | `6a028a21d3f774d75287497e961fc396e671fa18a4edc12b20892cc4246263fd` / 6553 | `68256f306b7a6af6f5f4520d5a48c071281e68a189de59d4874e6338942022b2` / 5681 | `a99e4d93c442ef90f32be3bfb7f12e4fbedd798c69a28ab765b6b0fd1f250f7b` / 5620 | `7090ff090635b06216a79969e1c357eb29ae109ad1fa035a55e2ac7cc07e724a` | 35 / 933 | 20 |
| `knowledge/design/concept-cards/posts/lms-cone-responses.md` | `e058141bf3bf62b662c0f9a65d801e85c51d285c672e021185afc5ff8f948f73` / 6178 | `fd95de6da64b319cc83824e4e113f5666bc6dea7c3c7d2938f64efd7ce05f9b3` / 6111 | `6159917a87b5a88a5e7cb57c65bbdb263d1de54684764a8dedbf1d6dd3df124f` / 5490 | `319b22614606c17261107e3292c1dd0321eb7106257184c6126b8e4b81ecfc7d` / 5423 | `01ec582608f6540f6c755f1cac39b8be90fc14b2023727ad7d6ad6441c50d33c` | 29 / 688 | 21 |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `44fcaef7a83759aef6c6a80a7b3e492ddf798da0df0a47bc3d5b7e7922776df7` / 7300 | `b2a63456d88ffa70537fe98b0cd3d36be75b40036da6a24c86546d8dbd2db1e4` / 7092 | `5aeddf6cc349a3ee84be031ebb36dc3859232c79eb9e62de57b510d820c93f57` / 6291 | `df3b3f04b65f3ef04d8b77c1fdb48ebf147f0e11dc6e89d3e67670fd4ad22754` / 6083 | `1e4654d8c20a3020ddf28b8a15394b25465ec8bdb41b22c6ca56e49c9493ca71` | 36 / 1009 | 60 |
| `knowledge/design/concept-cards/posts/mix-blend-mode.md` | `41707130d6177daced5f5d79392259d1e870d3274e2913ff7656a588fb4e1fbb` / 6241 | `6881abe6ec3533959febf4bfb7f34a826a87ddadcb4033169d20c302369178a8` / 6145 | `d33287cec1e7e42890e59e25e1bd9e4933f33dee269de1d87fb4597c5e523537` / 5071 | `a49fbbac46289c6770c3aedc0f5a3b8e26908748243c27586948252062e86d75` / 4975 | `e8321e54fa82a61bb39b9241400cdc92af196054b8ae408a643100e3cf8c4340` | 37 / 1170 | 30 |
| `knowledge/design/concept-cards/posts/modular-scale-construction.md` | `eb54832a713afc3a8ec3c862170f19cd9937f3684279ae4ebbcbb203c98fc8cf` / 11208 | `823cf6bd23cec2dd05927bfd99df6d155befa32ef266ad4fee886d5340f64526` / 11090 | `e38d32beabb285c82034c3383d6cb29541106a19ec750c5bed7d09110654cf67` / 9672 | `60b228306f5798e9342711d381d50205acd2a586eafd803ded838e94a46d1e2d` / 9554 | `4995eacddee46534e029668da4df44dd76f854b24ff57ce17958b72b83de7695` | 46 / 1536 | 38 |
| `knowledge/design/concept-cards/posts/modular-scale.md` | `55dee48f182cb70c6794ba0c75bebad43229226960f642ed404ba0adfbe426e4` / 12497 | `10c5e1b10f6301e3c13d85ea86e8bd6656f7e10904e9384f3b02d309d027b677` / 12392 | `5b93499e9ed20a830839561e9c23b51de29bfc14da264f19845b5693d9684297` / 10526 | `093fdefaf1b5643d40a39f5066bc9e0644dcdf73528708848ac859049400e425` / 10421 | `cc2e67001fde7c45a98c66cc609aee713964602088ba4642eba5d7e3a59f5899` | 52 / 1971 | 34 |
| `knowledge/design/concept-cards/posts/munsell-colour-system.md` | `b380d20365a1aeb9028accade943762c96ffaa9aa51437276e84b40d29cda7da` / 5435 | `457a6baaf6ff5ccd9e9921c3af6d7fce209b9bbf68a6b90f94038908bab53f25` / 5380 | `f2addeff80801bebf588a5906bc99bd65d878c3f9d852360990c2963b94646a0` / 4752 | `fca0b5ac72be90c49dfd67966a424fd00f8c167d9feb6c17be1d8be8db6d9e75` / 4697 | `c456f6bf81d69c62d0a15425d09811ab276014923865f2c1bbdea4906be5d48c` | 32 / 683 | 18 |
| `knowledge/design/concept-cards/posts/musical-interval-typographic-ratio.md` | `42d1cb3c5fd4cade0900de38250d9d203d9036e21b31668cc6f33e29adc59953` / 13367 | `18dab1df3df19984542a5f60615b37f41d9faedfb4b84edb310935217fb2c020` / 13248 | `141a8aee84331f814e3d230ca60fc71309b8cffebc6e3538b9dac38d4867d387` / 10854 | `a56f7af01deb8ef56b5cbecca05b433b76322db9f9b2953e1fa281da9fa7bdfd` / 10735 | `5cd34a4f41e828da7f3bb5bf67c79c518836e1edce032db9b44d91162c32c776` | 52 / 2513 | 39 |
| `knowledge/design/concept-cards/posts/natural-colour-system.md` | `bdcbd9ba870809c3c1ba364553fcf4a0b1227f16ec0ff123c0179bdbf527c0b5` / 6059 | `db5eca37b8a86415c952d629f29252bf756c97f5692468a783aeba5a2f203b7a` / 6028 | `bf39f13298bcca5c0bd727a6bf1b592c0bfb8fab16d9f83616e4fbae776f7c5f` / 5331 | `169425788e6b32da7d9c7f90913681338ac3de18b86100b1c1be2bffc3f191f2` / 5300 | `295d2f72d249ada134a59ea8195149b9538c42bc06be3c918a860049355e07c3` | 34 / 728 | 10 |
| `knowledge/design/concept-cards/posts/okhsl.md` | `239c0f8be4383cfd27f8f28d80f879f923efb4bcad518045dd52a3012024c848` / 7740 | `c1b68b39a592cbcc5911694fad66c0200a407e02484d7b393c09c476393d168f` / 7672 | `bdcda3feb45ffd77c130d39249ff744df211ba91195da99002c047ccced4cdbd` / 6650 | `4e39acf6e75e2349a822c1cc78b0a0790d77ab3af9137f02a204f757d512839b` / 6582 | `88acc1413fa8a3078fab1fd2265e07953c6c46133dd5d92d2fc2bd60bbcfc87d` | 40 / 1090 | 22 |
| `knowledge/design/concept-cards/posts/okhsv.md` | `14ccad9bf131a6ee71dc725d30e2ed968c43fcff75d8e7321fb70128bf47a894` / 6918 | `5e3b31a90ca88e05745b31d76c1a5e8d2d97bf32430464036be2e4af1ca7a054` / 6847 | `7e9364d2b0a275ac07a4549a1570c95b11daed5647cf7e0c893656ac94c89c56` / 5894 | `ec825357c3a48d92b63cecf2889208a0909b9053183d14f271982af20cfebacd` / 5823 | `575ea055838000fd2f9732086e9afebdbd71cacf9a0c3e61fc6f7cbb00858617` | 40 / 1024 | 23 |
| `knowledge/design/concept-cards/posts/oklab-conversion.md` | `11fff91aeb2418e89578640552bc4cd0035106df41634a0e721034944672e1a9` / 7950 | `15f9f8d0c4c64a34255a1eb8c6f29fc419cbe879fed16e31ac2dfe1c42a7e172` / 7757 | `3b7827f08447b95879dbfa2a5b10b1fcbd715dc12c74758d6bbd98c5a14ec253` / 6830 | `cbfac72e15d2f7f80e0bde3c75686da0fcc896d0cf266af65b8594914e4b2933` / 6637 | `eba7a783b64800bf7b2f1880297c25f83f8ba332876b25a0d3b03d514de2cf85` | 41 / 1120 | 57 |
| `knowledge/design/concept-cards/posts/oklab.md` | `57b6eca1c05281053222249f584b9b30900ef51902169330be4218b0fe6d1fb9` / 8803 | `b57d056abf550a3eeef19d0ec63267b1ecda70bbd4d641b8b684a73e25f6b4c2` / 8668 | `f540ca3846f7ef1bbb9970c11a99d0cdd730c59ccd8a50e235f50407f0e5026c` / 7568 | `4f509d9eabe795b244c7005091d8e8a53664ea8f0ab19795def9f419d545a831` / 7433 | `405aa8e259e2975039b048a70a0384c42910d0e9d3bb89b12dcb9188a8b2161c` | 47 / 1235 | 41 |
| `knowledge/design/concept-cards/posts/orthogonal-colour-properties.md` | `cc94e6ed42015d279096c2d99b64570d250585db064492da553850a13ebf658b` / 6190 | `56c6937ec0b41e74c3ff3c08b33c1483b9f237b7d19ff6e6bfe46ef85a8a566c` / 6132 | `fd64c0414622e7087605972768d03e2d39a798ad1e029f89b2d8da2c3f696d78` / 5054 | `7c5002e430c5dc446d11f13b2ffac6f46827cc9c23f922c87dd88e0e5de24c6d` / 4996 | `6c3389653649f459b44689081f77afd1298230289ae2ed0833c707f2ebeaddd0` | 40 / 1136 | 19 |
| `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | `9729492574a5eb16d72b78b351e9004f215dc99b2f9243ee0bec447a7ec78816` / 8814 | `e7074db7c7a1de290caa8be5db5e9a2cd306c4e7868141a2a7d7d3888eff0a24` / 8763 | `d29fa8499acf234667fda8e10249c614f5e0d8184ae58ccb270371876aeba922` / 7341 | `2245fde5e1ea4471044244f9c2909931223d7bc4237e8e7e6b753de76a69aeb9` / 7290 | `35b2c72172bc7e8d7fecd659917ee724c608597d53999afeef57e7b0f9bb12f1` | 43 / 1473 | 17 |
| `knowledge/design/concept-cards/posts/ratio-selection-criteria.md` | `4529b43e4e670aeb5b007bc42c1c6e2ddeb448151078255fee28d83c8990f53f` / 9019 | `d283070f6efe964b3ab1a9021fa7384a3af232a5d466d7830ec96fa024b20ce2` / 8947 | `8f1809c24a600f5d1cc001b4f1ce160660f874797cd8e93706387372ac5f71e8` / 8143 | `05ff75f6ee75df98bc9216831f2e39ed7123a84f36d4d1b36f17f73f16198875` / 8071 | `618427ad668287d14ffdefa69bf8a7daa335d06d5b4e10a4ac7039c88490c087` | 36 / 876 | 23 |
| `knowledge/design/concept-cards/posts/responsive-type-modular-scale.md` | `1cd198b08e28decec073971ae38b7b7e5f5134ba372417415ec6d0f2f73f328d` / 7254 | `de5673e9d03bd978a0622cb232b29fea575432aa1d631c1fa59e83e2ae17f965` / 7202 | `cf6b5995434a182a1a7e4a35632df8ad1e4a712048122e19c27bf945fad72326` / 6189 | `1f527ad8467054467fe4c67bfa60baa6a1b675766136bafe6b6bdba4b2b72227` / 6137 | `b5d19d0f12de2345ed88dfa4768ee62b0e4057e6b714efe53c9d31c85cd032f0` | 38 / 1065 | 17 |
| `knowledge/design/concept-cards/posts/rgb-colour-model.md` | `9d5deea23a9c666b47596b4aa927d78720be6628583699adb7aa17d08200710f` / 4849 | `02f29f3f8d57afa9593977a2e7b961ad85255f2ea6dedd21fe7b2cb4d90d0b12` / 4774 | `04e615c280677db51fc8be26f6ed1cf167ed66b83c3abd2adf40b65971f51509` / 3823 | `6f336797bb29c575d66603cabe0200e8baf47328bd56a94b6a7affb097b5e488` / 3748 | `8e637a76b135b48ea6d43213252655ead979f763ffb4e61e88a17830d1fb80b6` | 44 / 1026 | 25 |
| `knowledge/design/concept-cards/posts/scale-application-typographic-hierarchy.md` | `cc42c6931288c8313f7e6b5707bd06bda2d3c7199ed22826f02cc90b95ff4d23` / 10587 | `edd720a521c7736cf54002d7221f0114f2e2a5bcf010e62df98afeac6b5a44d8` / 10484 | `6c0eb79125db75eef155bee29132a1c867d77696673882a5fe8e1cbd1bd659a7` / 8788 | `89b49bc0d58b3466acea63b6abb7eb5f6c93652c40e60c8af74bab129ab6568a` / 8685 | `cb73b03ff4129c3d4a71e0a3724c250bbdac2e48dc1ea13b3b13f167af7c046c` | 53 / 1799 | 34 |
| `knowledge/design/concept-cards/posts/scale-base-unit.md` | `835bdb75151021f422125617fa3c74352f427f1bd4ac268b6edba8f3b334cbfb` / 8517 | `1b6d4187b89ce2eaa2c051a45c997cddf65ab549c4d977f9d62272bf5f4b4e42` / 8442 | `ea6eeef0171f483f0526230a79952f9d3bc4c6bddf15a847080f85a79b287042` / 7603 | `b82ecb88069b20930c09c27d8ac46fce330491b6cdd88a97c841e0310c3218e9` / 7528 | `bd7493548f57ecec552d77c7943a6e4e2cccc0da988cac4adef63c0740e624ce` | 37 / 914 | 25 |
| `knowledge/design/concept-cards/posts/scale-ratio.md` | `afea99af5a70069d9c770024bc5fa2dc6e90c3062e8b42c6e8d68573834802b8` / 9451 | `346fe1650fe48b1bc671e7bec9eb5ad1734b8a63697ec456a5b78b87812d0e63` / 9381 | `a2a0c82b69bb25541e3d303535d670dac69ed59796a2274cf5fe4ff2fbdc76f1` / 7672 | `eb71f552a2b599c980c94cf70007cfd419d632025afecb03f1387c4cc1ecfaa7` / 7602 | `a6cc85c2658364fbdeb04980dce72ee4673ca7dfeda1958ab51f30171a709b8d` | 49 / 1779 | 23 |
| `knowledge/design/concept-cards/posts/subtractive-colour-mixing.md` | `37340039478f0a08bff230cc55b38382ff57ecf5ac28cba1458513d92a01dd31` / 4039 | `9c8881f09d4297fc88f9873a7e7cfaa7e51869a235f662c7e6d36ceab3b65faa` / 4012 | `493950a5ad2e33470a8bd22ea4e59deccbe2d2be10d58bb90b8ea083f7af4e5a` / 3319 | `fba2adce22dc79e12ad45a63c1ca19e6af09462abb6d36ee7b9b272b9f76cd15` / 3292 | `c6a505f485c774e20588734798e33d6c37f9296aa555b2d5ba44b9e3fe2debc7` | 31 / 720 | 9 |
| `knowledge/design/concept-cards/posts/typographic-rhythm-modular-scale.md` | `2881057b6bcf91de971875c6c1634e195026aa090cab74e9bf39c70626ed001a` / 10146 | `43ed283f61eae8713016caa6e7b7552a15fa3c25d9562825e203b9f82d2aca0a` / 10086 | `8d0e9b8c575bdebc29587c3543d4ec42c39c8cef721926f8ee42e25694fc6a2f` / 8458 | `e522e1bf0d480469ce5cb024a701ae31fe0ae54feb3d11d17bcc0dcf8828fdfb` / 8398 | `e43365e3712b8ba2720d1361f035eb368d833d7401704f6a3747f6a736ba3185` | 48 / 1688 | 20 |
| `knowledge/design/concept-cards/posts/xyz-colour-space.md` | `68614909628a812ebc4a6bd17fad9df484c08fce520b08b26c20fd1eee6a0b8e` / 6301 | `00c15c4dc875a4934b0ecef5a19d4d6917df0194fe8bc15940862e1209892664` / 6201 | `ff3676ab800e42b7d5f01514228cf5fe80ff1ff58255029740936b5c7827c15a` / 5324 | `14c735d4d33e58edea6c7ce03e3e8890cadc2fd9c91e0225a70e1948664f8c66` / 5224 | `4dc891e454052b69e9fa1fc7b6c262d8a61ea7b161800b1be2582c9d4d5a036e` | 37 / 977 | 33 |

## Checks and actual command outcomes

| Check | Result |
|---|---|
| `make help` | Passed; current Makefile targets inspected. |
| `make check-skills` | Passed: 24 skills,18 existing editorial-length notices, no hard failure. |
| `make check-skill-versions` | First sandboxed attempt could not write ignored `build/` and `target/` outputs and failed; rerun with filesystem access passed: 24 source skills,24 generated packages, 0 errors. |
| `make check-package-paths` | Passed: 24 ZIPs/388 Markdown files, 0 hard failures, 596 warnings across594 locations, 3 explicit exceptions, 681 skipped external URLs; parser-suppressed material omitted by parser. |
| Fresh `make design` | Passed; produced a 10-member ZIP with 8 Markdown entries. ZIP SHA-256 `4086701b0c619f8a95b77dd71c0b6c4343b08b353c2f8bc2e2fc56a584f83fb5`, 46965 bytes. Actual ZIP/source comparison passed 8/8 Markdown members byte-for-byte. |
| Source expected-byte replay | Passed 233/233 current input pins;46 exact corrected body outputs; 187 whole-file unchanged; all 233 metadata prefixes unchanged; UTF-8, line counts and idempotence passed. Total 1,062 replacements / −3,337 bytes. |
| Three discriminating equality controls | Passed: expected corrected Matrix bytes accepted; leaving one active escape, changing one header field or changing an unrelated body number was rejected. |
| Version/history contract | Passed: one sibling history;1.0.6 metadata/history pair; no duplicate dotted skill-version labels outside the owning entrypoint/history; prior entries retained. |
| Git scope and whitespace | Passed: source commit contains exactly48 authorized paths; source `git diff --check`, staged check and committed `git show --check` passed. |

The first read-only projection helper had a bytes/string regex mismatch; a second
had an overescaped temporary regex; the first expected-header boundary assumed
the newline belonged to the prefix, while the frozen offset begins the body at
that newline; and the first header-negative fixture guessed a `title` key where
the card uses `concept`. Each was corrected before writing and rerun. The
corrected projection, byte oracle and all negative specimens then passed. A
package-gate run without filesystem access also failed before bundle staging;
the required rerun with filesystem access passed. These attempts changed no
tracked repository files.

## Corrected Arc06 hosted evidence and remaining visibility boundary

Updated only `hosted` for the 46 affected records in Arc06's existing
`artifacts/batch-results.jsonl`. All other 187 JSONL records are byte-identical;
for affected rows every field outside `hosted` is byte-preserved. Each corrected
record has overall `fail`, metadata `pass`, body `fail`, an observed token
count, a concrete expected-versus-visible snippet, CC correction observer/date
and reason, the exact revised-source candidate, and a preserved
`prior_observations` element containing the complete original hosted object
from `eac665f569d269b6a913e2f9349ef3e73656781e` with an explicit superseded reason. Retained raw response
hashes/URL and original structural checks remain explicitly identified as the
prior direct fetch; this correction did not refetch GitHub. No repaired body is
called hosted-pass.

The published `c4cc742` responses were complete HTTP200 observations. CDC's
independent F01 establishes visible literal escapes in all 46 affected bodies;
per-card counts and examples are attached to those exact records. Metadata stays
pass. The other 187 hosted records and their historical claims are unchanged.
The corrected source candidate `589d7c21bd6c9a415b921b80479822561861fa79` is not published or hosted
checked. The prompt grants no new publication authority; actual corrected
revision checks re-enter Arc06 only after independent source review and the
Operator's publication/access decision.

Historical initial unavailable results, the CC233-pass proposal, and its CDC
supersession remain in their original chronological sections. Slice02 keeps
five rows done and S02-05 open. Its source-preservation result at `c4cc742`
remains historically true for Arc06's metadata-only mutation; this intentional
Arc02 body correction is recorded as a separate later revision.

## Proposed row outcomes and ownership

CC proposes the four Slice09 criteria satisfied at the source/evidence scope
shown here; all four ledger statuses remain `open` for independent CDC review.

| Row | CC-proposed outcome | Evidence / next gate |
|---|---|---|
| S09-01 | Reconciled | Immutable233-row bridge, exact 46/48 write scope and all source hashes; CDC reviews scope and preservation. |
| S09-02 | Reproduced locally by CC | Exact46-byte oracle,1,062/23 token counts, all 233 headers,187 unchanged cards, UTF-8/line and three negative controls; no semantic acceptance. |
| S09-03 | Reproduced locally by CC | Version1.0.6/history contract, fresh package gates and 8/8 actual ZIP member comparison; CDC reviews package applicability. |
| S09-04 | Reconciled as a correction record | 46 hosted failures corrected with historical observations, locators and downstream owners; Arc06 waits for corrected-revision hosted checks. |

Arc02 retains full source-fidelity, technical-correctness, scope, consistency,
relationship and question-coverage review for all cards. CDC owns independent
Slice09 review. Operator owns any later publication/access decision; CDC then
owns actual exact-revision hosted rechecks with Arc06. Arc04 owns final package,
composition and release gates. P10-13 and Arc06 S02-05 remain open. No new
research, semantic acceptance, release or install claim is made.
