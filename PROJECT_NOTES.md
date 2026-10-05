# Project Notes — Chioma Portfolio

Operational handoff doc: build status, remaining placeholders, and
technical implementation details that don't belong in `PRODUCT.md`
(product truth) or `DESIGN.md` (visual system). Read those two first;
this file assumes them.

<!-- impeccable:project-notes 1 -->

## Orientation

- Static site, no build step, no framework, no npm. Open `index.html`
  directly or serve the folder with any static server.
- Deployed via GitHub Pages at `soma.azhyre.co.za` (see `CNAME`) — an
  invented subdomain (echoing her TikTok handle `@itssoma75`), not a
  literal rendering of her name; `azhyre.co.za` itself belongs to the
  Azhyre brand family and wasn't Claude's to invent.
- Site name is **Chioma** (renamed from an earlier "Lettie" placeholder
  during the original build, then from "Eullie" when the site changed
  to a different subject — every file was updated to match each time,
  including `contact.html`'s email, phone numbers, and socials — see
  "Real contact details" below).
- **Palette was rebranded from plum to black** at Chioma's request
  ("she likes black"): the system's old royal-plum/soft-orchid palette
  (which had an explicit, brief-driven "No-Black Rule") was replaced
  with a soft-noir-black/dusty-rose one — same five-role token
  structure (`--color-accent`/`-soft`/`-deep`, `--color-ink`/`-soft`,
  `--color-on-accent`), new hex values, `--color-bg-lavender` renamed
  to `--color-bg-blush`. Full before/after values and the renamed
  "Soft-Noir Rule" live in `DESIGN.md`'s Colors section and its
  "Palette History" note — read that before touching any color value.
  Every hardcoded `rgba(36,21,48,…)`/`rgba(15,8,20,…)` shadow/overlay
  tint in `css/style.css` and `css/responsive.css` was updated to the
  new `rgba(31,26,26,…)`/`rgba(11,8,8,…)` noir equivalents in the same
  pass — if you ever add a new dark tint, derive it from the current
  `--color-ink`/`--color-accent-deep` hex rather than copying an old
  plum rgba triple from memory or an old commit.
- **Oct 2026 "doesn't look professional" visual-craft pass**: fixed the
  hero's huge dead space and a broken-looking polaroid crop (see "Two
  bugs found" under "Hero polaroid stack" below), and added a visible
  1px tile edge plus a stronger two-layer overlay gradient to every
  photo tile/page-header photo/lightbox panel site-wide (see
  `DESIGN.md`'s Cards/Tiles section for the exact values).
- **Oct 2026 full dark-world redesign**: the entire palette flipped
  from light grounds/dark text to a persistent dark ground/light text,
  fused from two real reference sites the user pointed at (an
  actor-portfolio and a fashion-photographer template) rather than a
  generated concept roll. Every `:root` token in `css/style.css` was
  redefined (same names, inverted values); dusty rose promoted to the
  primary interactive/CTA color; a site-wide `img` filter grades every
  real photo (color and pre-existing black-and-white alike) through
  one consistent warm cinematic look; `.page-header-photo` gained a
  thick dark frame; the closing CTA section is now a full-bleed rose
  moment (was full-bleed dark) — the one deliberate color event in an
  otherwise dark site. The homepage hero's polaroid stack was
  explicitly kept as-is structurally, not replaced with a single
  photo, per direct user confirmation. Full before/after values,
  component-by-component reasoning for every flipped color (including
  the several ripple/border colors that needed manual contrast
  auditing rather than a blind flip), and the recorded direction
  contract (also in `index.html`'s opening HTML comment) are in
  `DESIGN.md`.
- **Oct 2026 layout-richness follow-up**: right after the dark-world
  flip, the user flagged it as "too flat and plain" — on the dark
  ground, with no light/dark section alternation left to lean on, the
  homepage's text-only About teaser and the `.focus-list`/brand-strip
  sections read as large empty stretches, especially on mobile (which
  the user explicitly prioritized) where everything just stacks into
  plain text with no grid asymmetry to break it up. Fixed with two
  targeted additions, not a new redesign pass: (1) the homepage About
  teaser now reuses the exact `.page-header-photo-frame` markup/CSS
  (no new styles) as a third grid column, capped to `max-width: 280px`
  via `.about-grid .page-header-photo-frame`; (2) `.focus-section`
  (reused on Home/About/Contact) and `.brand-strip` (Home only) each
  gained a `.glass-ripples` instance — the exact same ring-pulse
  decoration already used in the nav, reused for its texture alone,
  **not** its glass/backdrop-blur surface (see `DESIGN.md`'s amended
  Don't rule on this distinction) — which required adding
  `position: relative` to both section rules so the ripples'
  `position: absolute; inset: 0` had a containing block.

  **Follow-up bug, same day:** the user then reported mobile as "not
  balanced at all." The About-teaser photo added above was the cause —
  `.about-grid .page-header-photo-frame`'s `max-width: 280px` had no
  `margin: auto`, so as a block element narrower than its grid column
  it just hugged the column's start (left) edge per normal block
  layout; `.page-header-photo`'s own `rotate(-4deg) translate(-4%,-3%)
  scale(1.06)` transform then shifted it left again on top of that.
  Confirmed via `elementFromPoint` at 390px width: the photo's actual
  visual footprint ran ~x:-18 to x:306 in a 372px content column —
  nowhere near centered, with a large dead gap on the right. Fixed
  with `margin: 0 auto` on the same rule. **If you ever cap another
  photo-frame component to a fixed `max-width` inside a wider column,
  add `margin: 0 auto` (or `justify-self: center` if it's a direct
  grid item) in the same edit — a capped block element does not
  center itself by default, and this component's own rotate/scale
  transform makes an off-center miss more visually obvious than it
  would be for an unrotated element.**
- **Oct 2026 "lacks character" pass**: four separate complaints, fixed
  together where they overlapped.
  1. **Homepage portfolio-teaser crop.** `.work-panel img`/`.work-panel--large img`
     had no `object-position` (default 50% 50%), and the large panel
     especially is a wide landscape box (~761×420 at desktop) cropping
     a tall portrait phone photo — center-crop cut the subject's head
     off entirely on `park-halter-trousers-01.jpg`. Checked all 3
     homepage-teaser photos individually at their real rendered box
     sizes (not guessed): `balloon-portrait-02.jpg` and
     `garden-cardigan-01.jpg` already crop fine at center (their
     subjects sit vertically mid-frame in the source photos), so only
     `park-halter-trousers-01.jpg` needed a fix — `object-position: 82%
     6%` (she's positioned right-of-center and near the top of the
     source photo). **The same photo is also used in
     `portfolio.html`'s `.portfolio-item--wide` tile** (16:9, a
     similarly extreme crop) — same fix applied there too via inline
     `style` on that `<img>`, matching the established "Per-image crop
     overrides" pattern (see below) rather than a shared CSS rule,
     since this object-position is specific to this one photo, not a
     general rule for wide tiles.
  2. **Brand-row + Editorial List numbering device** — see DESIGN.md's
     Brand Credits Row and Editorial List sections for the full
     writeup; one shared numbered-index device fixed "the brand names
     look pale" and "What I Offer lacks character" together.
  3. **Real footer** — see DESIGN.md's Footer section. Hand-duplicated
     across all 8 pages with the correct relative-path prefix per
     page; re-check all 8 via `grep -rn "footer-grid"` if it's ever
     edited again, same caution as the nav.
- Shared across every page: `css/style.css` (base + design system),
  `css/responsive.css` (900px/600px breakpoints), `js/main.js` (glass
  nav toggle/scroll-shrink, portfolio filters, lightbox, ripple,
  looping typewriter, hero polaroid stack, random page-header photo).
- Fonts: Google Fonts CDN (`Cormorant Garamond` + `Manrope`), loaded
  per-page via `<link>` in `<head>` with `display=swap`.

## Build status per page

| Page | Status |
|---|---|
| `index.html` (Home) | Full build: masthead hero w/ looping typewriter + real-photo "polaroid stack" (swipeable/autoplaying, replaces the old duotone silhouette), About teaser, Portfolio teaser (real photography), "What I Offer" services, Brand strip, closing CTA. |
| `about.html` | Full build: page-header (real photo, see "Page-header photo" below), "At a Glance" facts + bio copy, "Where I Create" list, closing CTA. |
| `portfolio.html` | Full build: page-header (real photo), filterable contact-sheet grid (14 tiles: 5 fashion, 6 beauty, 3 lifestyle) with real photography, working lightbox, closing CTA. |
| `brands/index.html` | Full build: page-header (real photo), partner-credit row list, closing CTA. |
| `brands/azhyre-tech.html`, `azhyre-fashion.html`, `serenq.html` | Full build: page-header (real photo + real website links the user added), Partnership glance-list + bio copy, 3-tile campaign-preview gallery (still placeholder swatches), closing CTA. |
| `contact.html` | Full build: page-header (real photo), email + socials (**real values, user-supplied**), "Good to Know" list. No closing CTA section (page IS the destination). |

## Placeholder content still to replace

Everything below is intentionally placeholder/editable — confirmed via
`PRODUCT.md`'s "never fabricate" principle. Search each file for the
HTML comment `<!-- Placeholder ... -->` to find the exact spot.

- **All body/bio copy** on Home, About, and all 3 brand pages — written
  in-voice as an editable draft, not confirmed fact.
- **Brand/campaign imagery** on the 3 brand pages — every gallery tile
  there is still a CSS gradient "swatch" (`.swatch-1`–`.swatch-6`)
  standing in for real photography. No files exist yet in
  `images/brands/`. This is now the **only** remaining placeholder
  imagery on the site — the hero, the Portfolio grid, the homepage
  teaser, and every page-header visual all use real photos now (see
  "Real photography" / "Hero polaroid stack" / "Page-header photo"
  below).
- **Brand relationship specifics** — `PRODUCT.md` flags that the exact
  nature of each brand partnership (equity, exclusivity, employment)
  is unconfirmed; the glance-list "Role: Brand Ambassador" / "Status:
  Ongoing partnership" entries are safe generic placeholders, not
  confirmed facts.
- **`images/icons/favicon.ico`** — referenced by every page's
  `<link rel="icon">`, file does not exist (harmless 404, not visible
  to users, but worth adding a real favicon before launch).

**Already resolved, not placeholder:** contact email(s), phone numbers,
Instagram/TikTok handles, and the three brand website links — the user
filled these in directly.

**Chioma's real contact details (as of the Eullie → Chioma rename):**
business email `chioma@azhyre.co.za`, personal email
`chiomabvuma@icloud.com`, phone `+27 79 247 4794` (primary) and
`+27 69 474 5469` (alternate), Instagram `@itsschibaby`, TikTok
`@itssoma75`. **No Facebook** — the old Facebook entry
("Euleth A. Ngobeni") was removed from `contact.html` rather than kept
or guessed-at, since no Facebook presence was supplied for Chioma.
`contact.html`'s `.contact-grid` grew from two columns (Email, Find Me
On) to three (Email+personal email, Phone, Find Me On) to fit the new
fields; `css/style.css`'s `.contact-grid` is now `1fr 1fr 1fr` / `gap:
3rem` instead of `1fr 1fr` / `gap: 4rem` — still collapses to one
column at the existing 900px breakpoint, no new CSS classes needed
(the extra email/phone lines reuse `.contact-social`/`.contact-socials`
as-is). The personal email's surname ("Bvuma") differs from the site's
public name (Chioma Miyelani Anieze) — same pattern as the old site's
Facebook name differing from its "Eullie" brand name; not a mistake to
"fix."

## Technical implementation notes

### Animation system
- One global easing curve: `--ease-out-expo` = `cubic-bezier(0.16, 1, 0.3, 1)`.
- Homepage hero has the one deliberate "focal moment" (per `animate.md`
  discipline): the polaroid stack (see below) does a 3D `page-open`
  reveal on load, the wordmark loops through 4 names letter-by-letter
  (see below), kicker/tagline/CTAs fade up in a staggered sequence.
- Every other page's `<h1>` uses `ink-reveal` (a clip-path wipe) — a
  quieter echo of the same "masthead" motion vocabulary.
- Cross-document **View Transitions** (`@view-transition { navigation: auto; }`
  in `style.css`) give page-to-page navigation a cross-fade. Native
  CSS, zero JS, silently no-ops in unsupported browsers.
- `prefers-reduced-motion: reduce` is respected everywhere — see the
  media query near the bottom of `style.css`. Ripples and the
  typewriter are skipped at the JS level too (`main.js` checks
  `matchMedia` before attaching), not just hidden via CSS.

### Typewriter effect (hero wordmark)
`initTypewriter()` in `main.js` cycles the hero wordmark through
`WORDS = ['Chioma', 'Miyelani', 'Anieze']` forever — type in,
hold, erase, next word, repeat. **This replaced two earlier approaches**:
first a `steps()`-based CSS width-clip (jerky on the proportional italic
face — fixed-step width clipping doesn't respect glyph boundaries, so
letters got cut mid-character), then a one-shot per-letter
`animation-delay` reveal (typed "Eullie" once and stopped, back when
the site's subject and `WORDS` list were still Eullie/Euleth/Amukelo/
Ngobeni — the mechanism carried over unchanged when the name changed).
Current
version builds each letter as a `<span class="letter">`, adds `.is-in`
one frame after insertion (`requestAnimationFrame` x2, same pattern
`initPortfolioFilters` uses) so its opacity/transform *transition* (not
a keyframe) has something to animate from, and reverses that same
transition on erase instead of just deleting the span outright — this
is what makes backspacing read as a smooth cascade rather than an
abrupt snap. **Gotcha this required:** erase ticks fire faster (45ms)
than each letter's fade-out transition takes to finish (~230ms), so at
any moment several already-"erased" spans are still sitting in the DOM
mid-fade. Counting on `el.childElementCount` to know how many letters
are logically left would get this wrong; `initTypewriter()` instead
keeps its own `liveLetters` array as the source of truth, and lets the
fading-but-not-yet-`.remove()`'d spans clean themselves up on their own
timers. Per-letter typing speed is randomized (70–130ms) for an organic
feel rather than a mechanical fixed interval. The last letter of
whichever word is currently showing gets `.accent` (not just "Chioma"'s
final "a" — kept consistent across all 3 words in the loop). Skipped
entirely under reduced motion; the plain "Chioma" text node the
original markup already had stays fully visible and static.

### Ripple effect
`initRipples()` in `main.js` attaches a `pointerdown` listener (works
for touch and mouse alike) to buttons, filter pills, portfolio tiles,
the lightbox close button, and the mobile nav toggle. Ripple tint is
set per-component via a `--ripple-color` CSS custom property. **Watch
for this gotcha**: `.ripple-surface` deliberately does NOT set
`position` (only `overflow: hidden`) — an earlier version set
`position: relative` there too, which silently broke `.lightbox-close`'s
`position: absolute` due to a CSS specificity/source-order tie. Each
ripple-eligible selector sets its own `position` directly instead.

### Glass nav (header + mobile drawer) and the backdrop-filter containing-block trap
The site header (`.site-nav`) is a sticky, dark-noir glass bar
(`backdrop-filter: blur`), and on mobile the hamburger opens
`.nav-collapse` as a fixed off-canvas drawer (not the old in-flow
accordion) sliding in over a dimming `.nav-scrim`. Both share the same
dark glass + `.glass-ripples` decorative rings.

**Oct 2026 critique fixes (three separate issues found in one pass,
via a dual-agent `/impeccable critique` — see `.impeccable/critique/`
for the full report):**
- **Muddy nav color.** `backdrop-filter: blur(...) saturate(160%)` was
  tuned for the old lavender-tinted background — boosting the
  saturation of a faint lavender bleed-through read as rich glass.
  Against the current blush-pink background it instead boosted the
  pink into a visibly muddy brown/taupe cast on every page load,
  confirmed live via screenshot. Fixed by dropping to `saturate(100%)`
  (no boost) and raising the base background alpha (`.site-nav`:
  `.78` → `.9`; `.nav-collapse`: `.84` → `.93`) to compensate so the
  bar still reads as glass, not flat. **If you ever retint this glass
  background again, test it live against the real page background
  behind it** — `saturate()` in a `backdrop-filter` amplifies whatever
  color is actually behind the element, not just the element's own
  background-color, so the "right" hex value depends on what's behind
  it, not just the token itself.
- **Mobile horizontal overflow.** The closed `.nav-collapse` drawer
  sits at `transform: translateX(...)`, not `display: none`, and
  nothing clipped it — every page had ~305px of horizontal overflow at
  phone width (confirmed via `document.documentElement.scrollWidth` vs
  `clientWidth` in a sized iframe), so a visitor swiping sideways on
  their phone could scroll the whole page and see the drawer bleed
  into view without ever opening it. Fixed with `overflow-x: hidden`
  on both `html` and `body` in `style.css`. Safe with the full-bleed
  `position: fixed` header — fixed elements size against the viewport
  regardless of an ancestor's `overflow-x`.
- **Ripple rings colliding with nav link text.** `.glass-ripples
  span:nth-child(N)` positions were percentages roughly spanning the
  bar's vertical center (`top: 25–70%`), which is also where nav link
  text sits — at some viewport widths a ring's horizontal position
  landed on a specific link ("BRANDS" at one width, "ABOUT" at
  another), reading as a stray UI dot rather than ambient decoration.
  Moving one ring just shifted which link it collided with at a
  different width, so the real fix was systemic: all 6 rings now sit
  near the bar's top/bottom edges (`top: 15%`/`85%`) instead of its
  vertical center, avoiding the text band entirely regardless of
  viewport. **The mobile drawer reuses the exact same `.glass-ripples
  span` rules** (it's a shared class, same spans), but the drawer is a
  tall, narrow, top-aligned link *list* rather than a short wide bar —
  the same edge-hugging percentages don't generalize there (they can
  still land on a link vertically, and it shifts with viewport
  *height* now, not width). Rather than chase a geometric fix across
  every possible drawer height, `.nav-collapse .glass-ripples span`
  gets a `responsive.css` override that fades the ring borders further
  (`rgba(250,249,251,.35)` → `.16`) so even where one does sit near a
  link, it reads as background texture, not a UI element. **If you add
  a 4th context that reuses `.glass-ripples`, don't assume either
  existing fix transfers — check it against that context's own layout.**

**`.site-nav` vs `.nav-inner` split (full-bleed bar, capped content):**
`.site-nav` used to also carry the `.container` class directly, which
capped the entire glass bar — background, blur, border, everything —
to the 1200px content column, leaving visible page background on both
sides on any viewport wider than ~1250px. Per feedback ("on pc it's
not responsive, it's supposed to span the whole horizontal"),
`.site-nav` no longer has a `max-width` (spans the full viewport edge
to edge; only vertical padding lives on it now, horizontal padding
moved off it entirely) and the flex row (logo/links/toggle) moved into
a new child, `.nav-inner container` — `.nav-inner` supplies
`display:flex`/`align-items`/`justify-content`, `.container` supplies
the shared `max-width:1200px; margin:0 auto; padding-left/right`. This
mirrors every other section's use of `.container` for its content
column while letting the header be the one full-bleed surface.
`.glass-ripples` (the first one, the ambient decorative rings) stays a
**direct child of `.site-nav`**, not `.nav-inner`, so the rings scatter
across the full-width bar rather than being confined to the 1200px
column. `.nav-scrim` and `.nav-collapse` moved one level deeper (now
inside `.nav-inner`) — this is safe because the backdrop-filter
containing-block behavior described below applies to *any* descendant
of `.site-nav`, not just direct children, and every `.site-nav`-scoped
CSS selector already used descendant combinators (`.site-nav .logo`,
`.site-nav ul`, etc.), never `>`. **This same nav block is duplicated
across all 8 HTML files** (no templating on this static site) — if you
touch this markup again, check `grep -rn "class=\"site-nav\""` across
the repo, not just `index.html`.

**Real bug hit while building this, worth remembering:** `.nav-scrim`
is `position: fixed`, and was originally sized with `inset: 0`. It
rendered collapsed to only ~44px tall (just the header bar's own
height) instead of covering the page — clicking it to close the drawer
silently did nothing outside that tiny strip. Cause: `.site-nav` (the
scrim's ancestor) has `backdrop-filter`, and **`backdrop-filter` (like
`filter`, `transform`, `perspective`, `will-change` naming one of
those) makes that element the containing block for `position: fixed`
descendants' *percentage* offsets** — `top/right/bottom/left: 0`
(what `inset: 0` expands to) resolved against `.site-nav`'s own small
box, not the true viewport. `.nav-collapse`'s `height: 100vh` was
*not* affected by the same trap, because `vh`/`vw` units are always
viewport-relative regardless of containing block — only percentage-style
offsets are caught by this. **Fix:** gave `.nav-scrim` `top: 0; left: 0;
width: 100vw; height: 100vh;` instead of `inset: 0`. **If you ever add
another `position: fixed` element inside (or descended from) anything
with `backdrop-filter`/`filter`/`transform`, use `vw`/`vh` for its
sizing/offsets, not percentages or `inset` shorthand, or it will
silently size itself against the wrong box.**

**`.container`/`.site-nav` padding cascade trap:** `.site-nav` carries
both `site-nav` and `container` classes (for horizontal alignment with
the rest of the page). Below 900px, `responsive.css`'s `.container`
rule used to be a `padding: 0 1rem;` shorthand — identical specificity
(0,0,1,0) to `.site-nav`'s own padding rule in `style.css`, but loaded
in a later stylesheet (`index.html` links `style.css` then
`responsive.css`), so it won outright and **zeroed out all of
`.site-nav`'s vertical padding** below 900px, in every scroll state
(`.is-compact`/`.is-mid`/fully-grown alike) — not just the horizontal
gutter it was meant to control. This silently undid the header's
thickness (and the whole scroll-shrink size difference) on any tablet/
mobile viewport, confirmed via `getComputedStyle` showing `padding: 0px
16px` instead of the intended `80px 16px`. **Fix:** both `.container`
rules (base, in `style.css`, and the 900px override, in
`responsive.css`) now set `padding-left`/`padding-right` explicitly
instead of a `padding: 0 …` shorthand, so they can never clobber
another selector's vertical padding via source order. **If another
element ever needs `.container` plus its own vertical padding, check
this pattern still holds** — shorthand `padding` on a shared-specificity
utility class is a footgun for exactly this reason.

**Scroll-shrink header:** `initStickyNav()` in `main.js` tracks
`window.scrollY` (rAF-throttled) and toggles state on `.site-nav` via
CSS classes: fully grown (no class, only at `scrollY <= 0`) and
`.is-compact` (shrunk) any time `scrollY > 0` — plus `.is-shadow` (a
lifting drop-shadow) at the same time, so the header only looks
"flush"/flat at the absolute top of the page. **`.is-compact`/
`.is-shadow` are deliberately not direction-aware**: an earlier version
also had `.is-mid` (grown back to a halfway size while scrolling up but
not yet back at the top), so the header grew partway before fully
expanding again. Per feedback, the header should stay shrunk-but-visible
the whole way back up and only return to full size once the page is
actually scrolled to the top — `.is-mid` was removed (from both
`main.js` and `style.css`) rather than kept as dead code.

**Desktop-only fixed overlay + auto-hide (`.is-hidden`), and the
mobile-vs-desktop position split:** Per later feedback ("let it be over
the hero, hero beneath it" + "hides on scroll down, reveals on scroll
up" — confirmed via `AskUserQuestion` since "hides on scroll" is
ambiguous about direction), `header` is `position: fixed` by default
(`style.css`), not `sticky` — this takes it out of flow so the
hero/page-header section starts at the true top of the viewport with
the glass bar floating over it (confirmed live: scrolling to the very
top with a real backdrop behind it shows the hero content visibly
blurred through the glass). `initStickyNav()`'s `update()` regained a
`lastY` comparison (removed in the `.is-mid` cleanup above, reintroduced
here) *specifically* to drive `.is-hidden`
(`transform: translateY(-100%)`, transitioned): added while
`y > lastY` (scrolling down) and `scrollY > 0`, removed the instant
`y <= lastY` (scrolling up) or `scrollY <= 0`. Note `.is-compact`/
`.is-shadow` stay direction-independent (per the note above) — only
`.is-hidden` cares about direction; these are two independent concerns
toggled by the same `update()` call. **This overlay/auto-hide treatment
is desktop-only.** At ≤900px, `responsive.css` reverts `header` back to
`position: sticky` (original in-flow behavior — pushes hero/page-header
down normally) and neutralizes `.is-hidden` with `transform: none`, so
tablet/mobile never overlay or auto-hide, matching the original
pre-overlay UX there. Verified in this environment (whose Chrome tab is
stuck at ~400px width, see the quirks section below) by temporarily
setting `document.styleSheets` → the `responsive.css` sheet →
`.disabled = true` via `javascript_tool`, which strips every breakpoint
override and exposes the raw desktop rules regardless of actual
viewport width — confirmed `header` computes to `position: fixed`,
`.is-hidden` actually translates the bar off-screen, and re-enabling
the sheet restores the ≤900px reverts. **If you need to verify desktop
nav behavior again in this environment, reuse that stylesheet-disable
trick** rather than fighting `resize_window` (confirmed broken here).

**Mobile resting-size reduction:** separately, per feedback that the
mobile header's resting (top-of-page, scrollY = 0) size looked too big
next to its own scrolled/shrunk size, `responsive.css`'s ≤600px block
sets `.site-nav { padding: 1.75rem 0; }` — the same value as
`.is-compact` — so the mobile header no longer visibly grows when
scrolled back to the top. This is independent of the desktop
fixed/overlay/hide work above (different breakpoint, different
property), just implemented in the same pass.

### The `[hidden]` + `display` CSS gotcha (portfolio filters)
`main.js` toggles `item.hidden = true/false` to remove filtered-out
portfolio tiles from layout. **This does nothing by itself** if any
author stylesheet rule sets `display` on that element with normal
(non-`!important`) priority — author-origin CSS always beats the
browser's built-in `[hidden] { display: none }` rule regardless of
selector specificity, because origin/importance is checked before
specificity in the cascade. Fix in place: `.portfolio-item[hidden] { display: none; }`
with higher specificity than the base `.portfolio-item { display: block; }`
rule. **If you ever add another `hidden`-toggled element, check this
pattern applies to it too.**

### Real photography (portfolio grid + home teaser)
`portfolio.html`'s 11 tiles and `index.html`'s 3-tile Portfolio teaser
(`.work-panel`) now use real photos from
`images/portfolio/{fashion,beauty,lifestyle}/` (kebab-case, scene-
descriptive names, no category prefix since the folder already gives
that — e.g. `fashion/park-halter-trousers-01.jpg`). Each tile swapped
its old `<span class="swatch swatch-N">` for an `<img>`. On
`portfolio.html`, `data-swatch="swatch-N"` became `data-image` (the
lightbox's full-size source) plus `data-caption` (the lightbox
caption text — `<p class="lightbox-caption">` is now only rendered
when a caption is present, since brand-page-style placeholder
galleries don't set one). `main.js`'s `open()` reads
`trigger.dataset.image`/`dataset.caption` instead of `dataset.swatch`,
and builds an `<img>` inside `.lightbox-panel` rather than applying a
swatch class to the panel itself. In `style.css`, the old
`.portfolio-item .swatch::before` / `.work-panel .swatch::before`
soft-light overlays moved to `.portfolio-item::after` /
`.work-panel::after` (applied to the tile itself, not a swatch child)
so they still overlay correctly regardless of whether the tile holds
an `<img>` or (brand galleries, still placeholder) a swatch span —
**if you add another photo-backed grid, reuse this `::after` overlay +
`<img>` with `position:absolute; inset:0; object-fit:cover` pattern
rather than re-introducing a swatch wrapper.** The `.swatch-1`–
`.swatch-6` classes and their CSS are untouched and still power the
brand-page campaign galleries (still placeholder, no real photos
supplied for those yet).

**Per-image crop overrides:** most of these source photos are
portrait phone shots with a lot of empty sky/background above the
subject. `object-fit: cover` at default `object-position: 50% 50%`
crops those decently in normal 3:4 tiles, but the wide 16:9 tiles
(`.portfolio-item--wide`, `.work-panel--large`) only keep ~32% of the
image's height — center-crop can land mid-forehead. Where that
happened (`portfolio.html`'s `lifestyle/garden-cardigan-02.jpg` wide
tile), the fix was a per-`<img>` inline `style="object-position: 50%
48%;"` tuned by trial in-browser (screenshot, adjust, repeat) rather
than a CSS rule, since the right value is specific to that one photo's
framing. **If a newly added wide/large tile crops awkwardly, check
this per-image object-position pattern before reaching for a different
crop ratio.**

### Gallery-tile swatch bug (brand campaign previews)
`.gallery-tile .swatch` (the brand-page campaign-preview galleries)
had never had a positioning rule — `.swatch` spans have no intrinsic
size, so with no `position: absolute; inset: 0`, the gradient was
literally invisible (zero-size span) on all 3 brand pages since they
were first built. Fixed by adding `.gallery-tile .swatch { position:
absolute; inset: 0; }` and a matching `.gallery-tile::after` soft-light
overlay (same pattern as `.portfolio-item`/`.work-panel`) in
`style.css`. **This was never caught earlier because the Chrome
verification issues noted below meant these tiles were never actually
looked at in a browser.**

**Second swatch bug, Oct 2026 critique:** `.swatch-1`
(`linear-gradient(135deg, var(--color-accent) 0%, var(--color-accent-deep) 70%)`)
paired two near-black stops (`#171212` → `#0B0808`) with almost no
luminance gap — it rendered as a flat black square with no visible
gradient, indistinguishable from a broken image (confirmed via
computed styles; used on `brands/azhyre-tech.html` and
`brands/serenq.html`, both of which include `.swatch-1`). Fixed by
pairing it with `--color-accent-soft` (dusty rose) instead, matching
the dark+light pattern every other swatch already uses. **If you add
another swatch, keep both gradient stops' colors from the same side of
the Soft-Noir Rule's light/dark split** — two near-black or two
near-white stops will read as a flat, broken-looking block regardless
of which two tokens they are.

### Hero polaroid stack (replaces the old silhouette placeholder)
`index.html`'s hero visual is now a stack of 6 real photos
(`.polaroid-stack` > `.polaroid-card`s with `data-polaroid-stack` /
`data-polaroid-card`), reusing the exact slot and one-time `page-open`
3D entrance the old `.silhouette-frame` had (`.hero-visual
.polaroid-stack` in the "Hero focal moment" CSS section) so swapping it
didn't change the hero's layout or motion signature. `initPolaroidStack()`
in `main.js` drives everything else:
- **Cycling** reassigns cards to a *fixed* set of back-of-pile scatter
  "slots" (`--tx`/`--ty`/`--rot` custom properties) rather than
  re-rolling every card's own offset on every cycle — this is what makes
  the motion read as "one photo slides to the back, the next rises to
  front," not the whole pile jumping. Only **reshuffle** (double-tap/
  -click, or Enter) re-rolls the slot offsets themselves
  (`rollSlots()`).
- **Autoplay**: a 4s `setInterval` cycles the front card forward,
  paused via `IntersectionObserver` when the stack scrolls out of view
  and disabled entirely under `prefers-reduced-motion`.
- **Swipe**: pointerdown/move/up on the stack drags the front card
  live (a `--drag` custom property), and a swipe past 50px triggers
  `cycle()` in that direction *and* sets which way autoplay continues
  from there (`autoDirection`) — so a swipe against the current
  autoplay direction flips it permanently until swiped again.
- **Double-tap/-click** (two pointerups within 350ms, each under 10px
  of movement) triggers `reshuffle()` instead of a cycle.
- **Keyboard**: the stack is `tabindex="0"` with `role="group"`;
  ArrowLeft/ArrowRight cycle, Enter/Space reshuffles — same actions as
  swipe/tap, just keyboard-reachable.
- No-JS fallback: fixed (non-random) `nth-child` scatter values in CSS
  so the hero never shows a dead, unrotated stack of identical photos
  if JS fails to run.

**Two bugs found in the Oct 2026 "doesn't look professional" critique:**
- **Hero dead space.** `.hero-visual` had no `max-width`, so
  `.polaroid-stack`'s `aspect-ratio: 3/4` derived its height purely
  from the full bled grid-column width (~845px at common desktop
  widths) → ~1126px tall, against `.hero-copy`'s ~413px (confirmed via
  `getBoundingClientRect`). `.hero-grid`'s `align-items: center` then
  split that ~713px difference into huge empty blush-pink space above
  *and* below the text block — visually, almost all of it landed below
  the buttons since the kicker/wordmark/paragraph/buttons block itself
  is top-weighted. Fixed with `.hero-visual { max-width: 560px; }`,
  which keeps the signature oversized-bleeding-photo effect (still
  bleeds past the column edge via the existing negative margins) while
  bringing the two columns' heights within ~1.8x of each other instead
  of ~2.7x — close enough that centered alignment reads as centered.
  **If you change the hero copy's content length (shorter/longer
  tagline, more/fewer buttons) or the stack's aspect-ratio, recheck
  this balance** — the right `max-width` depends on both.
- **Back-card crop landing on dead space.** `.polaroid-card img` had no
  `object-position` (default 50% 50%, dead center). On
  `mirror-selfie-04.jpg` specifically, a back-of-stack card only
  reveals a thin sliver past the scatter offset, and that sliver landed
  on the photo's near-black jeans — looked exactly like a broken/empty
  image, not a styling choice. Fixed with a blanket `object-position:
  50% 22%` (biased toward the upper third, where the face/subject
  sits in these portrait phone photos) on `.polaroid-card img`.
  **Check any newly added polaroid-stack photo against this default**
  the same way the header-photo pool's additions were checked (see
  "Pool widened" above) — if the default crop still looks bad for a
  specific photo, override `object-position` on that `<img>` inline,
  same pattern as the portfolio grid's per-image overrides below.

### Page-header photo (About/Portfolio/Brands/Contact)
The smaller `.silhouette-frame.small` panel used in every other
page's masthead is now `.page-header-photo-frame` — a real photo.
`initHeaderPhoto()` in `main.js` picks one of `HEADER_PHOTOS` at random on
every page load (`[data-header-photo]`) rather than a fixed per-page
assignment — reads the existing `src`'s `../` prefix (brand pages are
one directory deeper) so the swap works from either root or `brands/`.
Visually it's a two-layer composition echoing the hero's old
silhouette-back/front bleed, now with a photo standing in for the front
shape: `.page-header-photo-back` is the same dusty-rose clipped-polygon
shape as the hero's `.silhouette-back`, offset behind; `.page-header-photo`
is the photo, rotated (`rotate(-4deg)`) and scaled up slightly
(`scale(1.06)`) so it reads as bigger/more dynamic than a flat
rectangle and the dusty-rose shape peeks out from behind on one side.

**Pool widened, Oct 2026 critique:** originally **only** the 4
`images/portfolio/beauty/mirror-selfie-0{1..4}.jpg` photos, per an
earlier request to keep this treatment to that specific set. All 4 are
near-identical black-and-white shots in the same pose family, so even
genuinely random picks (`Math.random()`, confirmed not a caching bug)
read as repetitive across consecutive page loads. Widened to 7 photos
spanning all 3 portfolio categories — each addition was checked at the
actual `aspect-ratio: 3/4, object-fit: cover, object-position: 50% 50%`
crop before being added; all three new ones crop cleanly at the
default center position, so none needed a per-image `object-position`
override. **If this pool is narrowed back down or re-themed, re-check
each candidate's crop the same way first** — see "Per-image crop
overrides" below for what happens when a photo doesn't crop cleanly at
the default center position.
Neither layer sets `overflow: hidden` on the outer `-frame` (matching
the hero's `.silhouette-frame`, which never clipped its own children
either) — that's what lets the back shape's offset actually show.
**Aspect ratio is 3:4 (portrait), not 4:3** — these are portrait phone
selfies, and a landscape frame cropped away too much of each photo;
3:4 also happens to match the hero's original (pre-polaroid-stack)
silhouette proportions, which is why it reads as "the same shape,
now a photo."

**Background-removal attempt, reverted:** before landing on plain
rectangular photos, a same-session experiment installed `rembg` +
`onnxruntime` (`pip3 install rembg onnxruntime`, ~180MB `u2net_human_seg`
model download) to cut transparent-background PNGs of the 4
mirror-selfie photos for a die-cut floating-figure look. Output quality
was poor — the pale phone in one shot nearly vanished (segmented as
background), and another had a disconnected stray artifact — so the
user asked to stop and use full rectangular photos instead. `rembg`/
`onnxruntime` are still installed in this environment's Python if
someone wants to retry with a different model or manual matte cleanup,
but nothing in the repo depends on them.

### Visible "placeholder" language scrub
Several pages had copy that literally told visitors the content was a
placeholder — e.g. brand-page bio copy ("This profile is a
placeholder... will replace this copy before launch"), gallery
captions ("Placeholder compositions shown above."), and
`brands/index.html`'s intro ("Each profile below is a working
placeholder..."). That reads as broken/unfinished to an actual site
visitor, even though it's accurate for internal tracking. Removed or
reworded all of it (moved the "still pending real copy" caveat into
HTML comments only) without fabricating any new facts — see
`PRODUCT.md`'s "never fabricate" principle, still in force. The
existing bio/bio-copy paragraphs on Home/About/brand pages were
already reasonable in-voice drafts (not "content goes here" filler)
and didn't need rewriting, just the self-referential sentences cut.

### Lightbox
Fixed overlay, single reusable `.lightbox-overlay > .lightbox-content`
DOM built fresh per-open in `main.js`. Width is capped against *both*
`90vw`/`720px` AND a viewport-height-derived limit
(`calc((100vh - 6rem) * 4 / 5)`) so the close button and caption can
never overflow off-screen on a short viewport — an earlier version
only bounded width, and the panel could grow taller than the viewport.
Closes on Escape, click-outside, or the close button; returns focus to
the trigger tile on close.

**z-index vs. the fixed header:** `.lightbox-overlay` was `z-index: 100`
— lower than `header`'s `z-index: 500` — so whenever the header was
visually on top of the viewport's top strip, it painted over the top of
the lightbox (photo, tag pill, and close button all cut off behind the
glass bar). This was always technically true (header's z-index has
always been 500), but went unnoticed while `header` was `position:
sticky` and only overlapped page content while actively scrolled past
the top. Once `header` became `position: fixed` on desktop (see the
overlay/auto-hide note above), it overlaps the viewport top *at every
scroll position*, making the bug immediately visible any time the
lightbox opens. **Fixed by raising `.lightbox-overlay` to `z-index:
600`** — a full-screen modal should always be the topmost thing on the
page, above chrome as well as content. If you add another fixed/modal
overlay (a second lightbox variant, a toast, a dialog), check its
z-index against `header`'s 500 rather than assuming "z-index: 100" (a
common default-ish value) is automatically high enough.

### Portfolio filter transitions
`setItemVisible()` in `main.js` adds `.is-hidden` (opacity/scale
transition) before setting `hidden = true` after a 350ms timeout on
hide, and reverses the order on show (`hidden = false` → double
`requestAnimationFrame` → remove `.is-hidden`) so the fade actually has
something to animate from.

## Known environment quirks (this dev machine / session)

- **Reassigning an existing `<iframe>`'s `src` to the same URL can serve
  a stale cached CSS file**, even after the source file changed on
  disk and even with a cache-busting query string on the iframe's own
  `src` — Chrome's HTTP cache still served the old `css/style.css` to
  the iframe's `<link>` tag in this environment (python's
  `http.server` sends no cache-control headers, so default heuristic
  caching applies). Confirmed via `getComputedStyle` showing a stale
  value, then confirmed the live server WAS serving the updated file
  (`fetch()`'d it directly), isolating the cache as the cause. A
  top-level `navigate()` call on the real tab did *not* show this
  problem (probably a different cache-validation path for real
  navigations vs. programmatic iframe `src` changes) — only reused
  iframes during mobile-viewport checks were affected. **Fix:** after
  setting an iframe's `src`, also cache-bust the stylesheet `<link>`
  itself from inside the iframe's own document (`link.href =
  link.href.split('?')[0] + '?v=' + Date.now()`), not just the
  iframe's `src`. If a future mobile-viewport check via iframe looks
  unexpectedly unchanged after an edit, suspect this before suspecting
  the CSS.
- **Background/unfocused tabs throttle `setTimeout`-driven loops** (the
  typewriter loop, the polaroid stack's autoplay timer) — Chrome slows
  or effectively pauses timers in a hidden/unfocused tab, so verifying
  these by opening several tabs and checking one later can make a
  perfectly-working loop look frozen. It "catches up" in a burst once
  the tab regains focus. Always bring the specific tab to the front
  (e.g. a `computer` screenshot call) before judging whether a
  timer-based effect is actually running.
  could not resize its window below its native ~1536px width in this
  environment — `resize_window` calls silently no-op'd. Mobile-viewport
  screenshots were never obtained live; mobile/tablet CSS was verified
  by code review only. Worth a real device/DevTools check before launch.
- The same extension occasionally drops connection mid-session
  (`CDP sendCommand timed out`, "extension disconnected"). Opening a
  fresh tab via `tabs_create_mcp` reliably recovers; retrying the same
  tab usually doesn't.
- Local verification server: `python -m http.server 8123` from the
  project root. Always stopped via `taskkill` (Windows) after each
  verification pass — check `netstat -ano | grep :8123` if port 8123
  seems stuck in a future session.

## DESIGN.md + sidecar

`DESIGN.md` documents a **full, ~19-step type scale** (not the usual
4-role display/headline/body/label set) — every literal `font-size` in
`css/style.css` maps to a named step. That's deliberate: this is a
rich editorial layout with many genuinely distinct, intentional label
variants (kicker vs. tag vs. meta vs. caption vs. footnote, etc.), not
accidental drift. If it ever looks like too many steps, don't collapse
it without checking each one still maps to a real, distinct component
first. The two shadow-tint families (`rgba(36,21,48,X)` vs the deeper
`rgba(15,8,20,X)` on `.btn-primary-inverse` and `.lightbox-panel`) are
similarly intentional, not an inconsistency to unify.

`.impeccable/design.json` is the sidecar the impeccable skill's
`document.md` spec calls for — it carries what `DESIGN.md`'s
frontmatter schema can't hold (shadows, motion tokens, full
component HTML/CSS snippets, narrative/rules). If you regenerate
`DESIGN.md`, regenerate this alongside it.

## Drift flag

`PRODUCT.md`'s "Capabilities and Constraints" and "Evidence on Hand"
sections still describe the pre-build state ("brand pages are
structurally scaffolded but have no real content", "every page
currently holds placeholder copy") — that's now out of date given the
build described above, though the underlying "don't fabricate facts"
principle still holds. Not fixed here since this file's job is to
record state, not repair `PRODUCT.md` drift unasked — run
`/impeccable doctor` or do a quick manual pass when convenient.
