---
name: Chioma
description: Personal brand site for Chioma — fashion/beauty/lifestyle model, content creator, and brand ambassador.
colors:
  bg: "#000000"
  bg-pearl: "#111111"
  bg-blush: "#222222"
  accent: "#FF4F8B"
  accent-soft: "#FF85B0"
  accent-deep: "#000000"
  ink: "#FFD6E8"
  ink-soft: "#C0718C"
  on-accent: "#000000"
  ivory-surface: "#FFD6E8"
typography:
  display:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(4.5rem, 13vw, 9rem)"
    fontWeight: 600
    lineHeight: 0.9
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(2.75rem, 6vw, 4.5rem)"
    fontWeight: 500
    lineHeight: 1.1
  cta-title:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(2.25rem, 5vw, 3.5rem)"
    fontWeight: 500
  title:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(2rem, 4vw, 2.75rem)"
    fontWeight: 500
  contact-title:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(1.75rem, 3.5vw, 2.5rem)"
    fontWeight: 600
  title-sm:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "2rem"
    fontWeight: 500
  brand-link:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "1.6rem"
    fontWeight: 600
  logo:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "1.7rem"
    fontWeight: 600
  section-label:
    fontFamily: "Cormorant Garamond, Georgia, 'Times New Roman', serif"
    fontSize: "1.5rem"
    fontWeight: 600
  icon-glyph:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "1.9rem"
  lead:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 400
    lineHeight: 1.75
  body:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.8
  fact:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 400
  button-label:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 700
    letterSpacing: "0.08em"
  footnote:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 400
  note:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 400
  label:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 700
    letterSpacing: "0.1em"
  kicker:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    letterSpacing: "0.2em"
  caption:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 400
  meta:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.7rem"
    fontWeight: 700
    letterSpacing: "0.14em"
  tag:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.68rem"
    fontWeight: 600
    letterSpacing: "0.16em"
  micro:
    fontFamily: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: "0.65rem"
    fontWeight: 700
    letterSpacing: "0.14em"
rounded:
  flat: "2px"
  pill: "100px"
spacing:
  section: "7rem"
  section-tablet: "5rem"
  section-mobile: "3.5rem"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.flat}"
    padding: "1.05rem 2.1rem"
  button-primary-inverse:
    backgroundColor: "{colors.on-accent}"
    textColor: "{colors.ivory-surface}"
    rounded: "{rounded.flat}"
    padding: "1.05rem 2.1rem"
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.ink-soft}"
    rounded: "{rounded.pill}"
    padding: "0.6rem 1.25rem"
  filter-pill-active:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.pill}"
    padding: "0.6rem 1.25rem"
---

# Design System: Chioma

## Overview

**Creative North Star: "The Lookbook Cover, Shot Under One Light"**

The site reads as a fashion lookbook's opening spread rather than a
templated influencer landing page: an editorial masthead, real
photography presented as tilted, layered "polaroid" cards (a hero
photo stack, and a photo-plus-peeking-accent-shape treatment on every
other page header), and kicker-plus-hairline labeling borrowed from
magazine contributor pages. The site runs on one persistent true-black
ground — every page, every section, with no alternating light/dark
breaks — so the experience reads as one continuous cinematic reel
rather than a sequence of unrelated snapshots stitched together. Every
real photo (color or pre-existing black-and-white) passes through one
shared warm cinematic grade so the whole body of work looks graded by
the same hand. Hot pink carries every piece of interactive color on
that dark ground (links, CTAs, active states) and is the system's only
accent hue; the one deliberate exception to the dark ground is the
closing CTA section, a full-bleed pink moment that closes every page.
As of the Oct 2026 "Editorial Spotlight Pink" repaint, the palette is
sourced from an external black/pink palette reference rather than a
client-pinned brief — see the Palette History note below for the full
lineage and what carried over.

Confirmed rejection: no centered-headshot-plus-CTA-button template
hero, no icon-led card grids (the Oct 2026 `.focus-item` card treatment
is a scoped exception — see Do's and Don'ts), no gray neutrals outside
the palette's own two near-black tones (see the Named Rules below for
what replaced the old warm-black rule), and no alternating light/dark
page sections; the dark ground is the site's constant, broken only by
the one pink CTA moment.

**Key Characteristics:**
- Editorial, not corporate-influencer: kickers, hairline rules, serif italic labels
- Persistent true-black ground across all 8 pages, with hot pink as the single interactive accent and one deliberate full-bleed pink CTA moment per page
- Every real photograph passes through one shared `img` color-grade filter so mixed color/black-and-white source shoots read as one deliberately graded body of work
- A peeking-accent-shape motif at masthead scale: the hero's swipeable/autoplaying polaroid stack (Home only) and a single rotated, thick-dark-framed photo with a hot-pink clipped shape peeking from behind (page-header size, every other page). The homepage's "Selected Work" tiles are a separate, explicitly client-directed exception — see Shapes → Heart-frame variant — not a third scale of this same device.
- Flat surfaces, true-black shadows, near-zero border-radius except pill badges/buttons — **the one deliberate exception is the site header**, a dark glass (`backdrop-filter: blur`) that floats above page content, the system's only non-flat surface
- Motion is deliberately restrained: one authored focal sequence on the homepage, quiet shared support elsewhere

## Colors

Full palette strategy — five named roles, each owning a field-scale region rather than appearing as scattered accents. **Oct 2026: repainted from a soft-noir-black + dusty-rose system to a stark true-black + hot-pink one ("Editorial Spotlight Pink")** — see the Palette History note below for what carried over and what changed.

### Primary
- **Hot Pink** (`#FF4F8B`, `--color-accent`): the site's one interactive color — CTAs, links, active states, headings-as-accent, the closing CTA section's full-bleed background. A vivid, saturated pink rather than the prior system's muted dusty rose — the palette's own namesake color.

### Secondary
- **Pale Rose** (`#FF85B0`, `--color-accent-soft`): decorative/structural only — the nav wordmark and mobile toggle bars, underline/hairline tints, gradient stops. Never carries body copy. A derived midpoint between `--color-accent` and `--color-ink`, not a value sourced directly from the palette.

### Tertiary
- **Truest Black** (`#000000`, `--color-accent-deep`): the system's single darkest value — gradient/shadow depth stop, and the thick 10px frame border on every `.page-header-photo`. Identical to `--color-bg` in this palette (see Named Rules below).

### Neutral
- **True Black Ground** (`#000000`, `--color-bg`): primary page background. Holds for every page, with no light-background sections anywhere except the pink CTA fill.
- **Secondary Dark** (`#111111`, `--color-bg-pearl`): formerly the about-teaser/focus/brand-gallery/footer fill — no section uses it as a fill since the Seamless-Ground pass (see Named Rules); kept as a token for gradient stops. An interpolated midpoint, not sourced directly from the palette (see Palette History).
- **Charcoal** (`#222222`, `--color-bg-blush`): formerly the hero/page-header/brand-strip fill; now only a gradient stop (page-header accent shape, swatches) since the Seamless-Ground pass.
- **Pale Pink Ink** (`#FFD6E8`, `--color-ink`): primary text — sourced directly from the palette.
- **Muted Rose-Mauve** (`#C0718C`, `--color-ink-soft`): secondary/muted text, blended from the accent hue toward neutral gray rather than sourced directly.
- **True Black On-Accent** (`#000000`, `--color-on-accent`): dark text atop solid pink-accent fills (buttons, the CTA heading). Identical to `--color-bg`/`--color-accent-deep` in this palette — see Named Rules below.
- **Ivory Surface** (`#FFD6E8`, `--color-ivory-surface`): the one deliberately BRIGHT surface in an otherwise all-dark system — the polaroid card's paper mat background, and the "Work With Me" button's ivory text atop its dark fill on the pink CTA section. Same value as Pale Pink Ink, kept as a separate token because the role (a bright card-like object / a guaranteed-bright text color) is distinct from "body text."

### Named Rules
**The Persistent-Ground Rule.** The page background is true black on every page and every in-page section — `--color-bg`, `--color-bg-pearl`, and `--color-bg-blush` are all near-black, never white or light. The site never alternates back to a light section.

**The Seamless-Ground Rule (Oct 2026, supersedes per-section tiers).** Client direction: sections should "flow and fade into each other without it looking all boxes." No section paints its own background anymore — every section sits on the one continuous `body` black, so there is no seam anywhere between sections, and `--color-bg-pearl`/`--color-bg-blush` no longer fill any section (they survive only as gradient stops inside swatches/the page-header shape). Atmosphere comes only from soft radial pink glows that fade to transparent well inside their own section (`.hero`, `.page-header`, `.cta-close`). The ambient `.glass-ripples` rings were removed from `.focus-section`/`.brand-strip` in the same pass (they read as scattered). **A first attempt — feathered grey tier bands, multiple offset glows, glowing cards, a pink band with a gradient ramp, and scroll-driven fade-ins — was rejected as "scattered and messy, not seamless."** Lesson: seamless here means *fewer* surfaces, not softer edges on the same number of surfaces. Don't reintroduce a full-width section fill, a section-level card/box, or per-section decoration.

**The Pink-Glow CTA.** `.cta-close` is the page's one pink moment — no longer a full-bleed solid pink band (it was the biggest box on the page) but a pink radial glow pooled behind centered ink-colored text, with a standard `.btn-primary`. Don't add a second glow of this strength; its force depends on staying singular.

**The True-Black Rule** (supersedes the prior Soft-Noir Rule). Every near-black value in the system — `--color-bg`, `--color-accent-deep`, `--color-on-accent` — is literal `#000000`; `--color-bg-pearl` (`#111111`) and `--color-bg-blush` (`#222222`) are the only lifted dark tiers, both neutral gray rather than warm-tinted. This is a deliberate reversal of the prior system's "never flat #000000 / always warm black" rule: the Editorial Spotlight Pink palette is intentionally starker and more graphic, with no warm undertone in its blacks. Don't reintroduce warm-tinted near-blacks or treat flat `#000000` as a mistake to "fix" — it's the current system's literal ground value.

**The One Accent Rule.** Hot Pink (`--color-accent`) is the only hue carrying interactive meaning (links, CTAs, active states) anywhere in the system. Pale Rose (`--color-accent-soft`) is structural/decorative only and never stands in for it. Don't introduce a second interactive hue.

### Palette History
This system has gone through three full repaints, each pinned by an external source rather than invented in-session: "royal plum + soft orchid" (an explicit No-Black Rule brief) → "soft-noir-black on white/blush" (Chioma's own black preference) → "persistent dark-noir ground + dusty rose" (Oct 2026, fused from two reference portfolio sites) → **"true-black + hot pink, 'Editorial Spotlight Pink'"** (Oct 2026, same day — sourced from a black/pink color-palette reference guide, at the client's direct request to "use one of these color palettes"). Every `:root` custom property kept its name and role across all four; only the values moved. This latest repaint: `--color-accent` flipped from muted dusty rose (`#CBA3A8`) to vivid hot pink (`#FF4F8B`); `--color-ink`/`--color-ivory-surface` flipped from warm ivory (`#F3E9E7`) to pale pink (`#FFD6E8`); and `--color-bg`/`--color-accent-deep`/`--color-on-accent` all collapsed to literal `#000000` since the source palette gives only two near-black anchors (`#000000`, `#222222`) rather than the prior system's five distinct warm-noir tiers — `--color-bg-pearl` (`#111111`) is the one interpolated value needed to keep a 3-tier dark-surface system working with only two sourced blacks. Every hardcoded shadow/overlay/ripple `rgba()` literal tied to the old tokens was remapped to match (see `css/style.css`'s and `css/responsive.css`'s git history for the exact before/after). If you find references to "dusty rose," "warm noir," or a non-`#000000` ground/accent-deep/on-accent anywhere outside this note, they're stale — update them to match this section.

## Typography

**Display/Headline Font:** Cormorant Garamond (italic weight 500/600), with Georgia/Times New Roman fallback
**Body/UI Font:** Manrope (400/500/600/700), with system-sans fallback

**Character:** A high-contrast italic display serif (editorial, cover-line register) paired with a clean geometric grotesque for everything functional (nav, labels, body, buttons) — the magazine-masthead-meets-caption-line pairing. Unchanged by the Oct 2026 dark-world redesign — the direction contract pinned this pairing as a carryover, and only the color tokens around it moved.

### Hierarchy

The full ramp below is the real, complete scale — every literal `font-size` in `css/style.css` maps to one of these named steps. It's wider than a typical 4-role system because this is a rich editorial layout with many small label variants (kicker vs. tag vs. meta vs. caption); each step is a genuine, reused, intentional choice, not one-off drift.

**Display tier (Cormorant Garamond, italic):**
- **Display** (weight 600, `clamp(4.5rem, 13vw, 9rem)`, line-height 0.9): the homepage hero wordmark only. Deliberately exceeds the general 6rem display cap — an earned exception because the masthead's cover-line-bleeding-behind-the-panel concept only reads at this scale.
- **Headline** (weight 500, `clamp(2.75rem, 6vw, 4.5rem)`): every other page's `<h1>` in `.page-header`.
- **CTA Title** (weight 500, `clamp(2.25rem, 5vw, 3.5rem)`): the closing CTA's `<h2>`.
- **Title** (weight 500, `clamp(2rem, 4vw, 2.75rem)`): in-page section headings (`.about-grid h2`, `.work-intro h2`).
- **Contact Title** (weight 600, `clamp(1.75rem, 3.5vw, 2.5rem)`): the Contact page's email link.
- **Title Sm** (weight 500, 2rem): `.brand-index-name`.
- **Brand Link** (weight 600, 1.6rem): the homepage brand-partner row links.
- **Logo** (weight 600, 1.7rem): the nav wordmark.
- **Section Label** (weight 600, 1.5rem): small serif labels like "About", "Bio", "Selected Work" — an italic-serif alternative to the uppercase kicker for variety.

**Body tier (Manrope):**
- **Lead** (400, 1.05rem, line-height 1.75): hero tagline, page-header intro, contact-social lines.
- **Body** (400, 1rem, line-height 1.8, max-width 58–65ch): paragraph copy.
- **Fact** (400, 0.95rem): `.glance-item dd` (the "at a glance" fact values).
- **Icon Glyph** (1.9rem, no letter-spacing): the lightbox × close glyph — sized as an icon, not running text.

**Label/meta tier (Manrope, mostly uppercase + tracked):**
- **Button Label** (700, 0.82rem, letter-spacing 0.08em): `.btn-primary`, `.btn-primary-inverse`, `.btn-secondary`.
- **Footnote** (400, 0.85rem): `.brand-back-link`, `.site-footer`.
- **Note** (400, 0.8rem): `.work-note`, `.lightbox-caption`.
- **Label** (700, 0.78rem, letter-spacing 0.1em): nav links, `.portfolio-filters button`, `.brand-index-arrow`.
- **Kicker** (700, 0.75rem, letter-spacing 0.2em): `.kicker` (the eyebrow-plus-hairline label).
- **Meta** (700, 0.7rem, letter-spacing 0.14em): `.glance-item dt`, `.portfolio-item-view` ("View" hover pill).
- **Micro** (700, 0.65rem, letter-spacing 0.14em): `.work-tag` (the smallest pill badge), `.polaroid-caption`.

### Named Rules
**The Earned-Exception Rule.** The hero wordmark's 9rem cap breaks the general 6rem display-size guideline on purpose — a brief-driven signature moment, not a habit. Don't extend the exception to any other heading.


**Display exceptions, Oct 2026.** Five literal sizes sit deliberately outside the ramp above, each used for a single decorative or interactive moment rather than running text, and each is an earned exception in the same sense as the hero wordmark: the intro mark (`.site-intro-mark`, `clamp(9rem, 32vw, 15rem)`), the ghost words (`.ghost-word`, `clamp(7rem, 21vw, 18rem)`), the marquee (`.marquee-track span`, `clamp(2.5rem, 6vw, 4.75rem)`), the heart zoom caption (`.heart-zoom-caption`, `1.3rem`), and the lightbox arrows (`.lightbox-nav`, `2.6rem` on desktop and `2.2rem` on mobile). Do not extend these to running text or ordinary headings.

## Layout

`.container`: max-width 1200px, centered, 1.5rem side padding (1rem at ≤900px). Section vertical rhythm uses a single `--section-pad` custom property: 7rem desktop → 5rem at ≤900px → 3.5rem at ≤600px. Unchanged by the dark-world redesign.

Breakpoints: 900px (tablet — grids collapse to 1 column, hero-visual reorders above the copy; the fixed/overlay desktop header reverts to in-flow `sticky`) and 600px (mobile — nav becomes an off-canvas glass drawer, portfolio/work grids go single-column).

Recurring grid shapes: two-column asymmetric splits (`1.15fr/1fr` hero, `0.6–0.85fr / 1.15–1.4fr` bio/page-header/contact panels), a 6-column asymmetric span grid for the homepage portfolio teaser (one `span 4 / row 2` tile + two `span 2` tiles), a 3-column grid with occasional `span 2` "wide" tiles for the full Portfolio contact-sheet, and plain 3-equal-column grids for the reusable editorial list component (see Components → Editorial List).

## Elevation & Depth

Flat by default. Depth appears only as tinted, soft-blurred drop shadows on interactive/floating elements (buttons on hover, the polaroid cards/page-header photo, the lightbox panel) — never a neutral-gray shadow lifted straight from a browser default. **Oct 2026 "Editorial Spotlight Pink" repaint:** every shadow literal collapsed to a pure-black (`rgba(0,0,0,X)`) tint, replacing the prior system's two warm-noir shadow families (`rgba(31,26,26,X)`/`rgba(11,8,8,X)`, themselves carried over from an even earlier palette generation). Since this palette's own darkest token (`--color-bg`/`--color-accent-deep`/`--color-on-accent`) is literal `#000000`, there's no longer a distinct "deeper" near-black to draw a second shadow family from — the two depth tiers below are now differentiated by alpha/blur alone, not by a secondary hue. That's consistent with "flat by default" rather than a defect to chase: depth is a secondary, quiet cue here, not a focal device.

### Shadow Vocabulary
- **Button Lift** (`0 14px 28px -14px rgba(0,0,0,.55)` → `0 20px 34px -12px rgba(0,0,0,.6)` on hover): `.btn-primary`.
- **Button Lift (Inverse)** (`0 14px 28px -14px rgba(0,0,0,.35)`): `.btn-primary-inverse` — the deeper tint, since it sits on the full-bleed pink CTA background.
- **Panel Float** (`0 32px 60px -22px rgba(0,0,0,.5)`): each `.polaroid-card` in the hero stack, and `.page-header-photo` on every other page.
- **Lightbox Lift** (`0 50px 90px -30px rgba(0,0,0,.65)`): the enlarged lightbox panel — the deepest shadow in the system, matching its topmost z-index.
- **Tile Edge** (`box-shadow: 0 0 0 1px rgba(255,214,232,.18)`): a light-tinted 1px hairline (not a layout-affecting `border`) on `.portfolio-item`, `.work-panel`, `.gallery-tile` — light-tinted (not dark) so adjacent tiles with light edge content (sky, pale clothing) still separate from each other and from the dark page ground.

### Named Rules
**The Tinted-Shadow Rule.** Every shadow's color is a true-black tint, never a flat gray lifted from a browser default — consistent with the True-Black Rule above. Edge/hairline treatments on tiles are the one shadow-family exception that goes light-tinted instead, because their job is separation against a dark ground, not depth.

## Shapes

Near-flat throughout: `2px` border-radius on cards, tiles, and buttons (an editorial, not-rounded feel). Pill shapes (`100px` radius) are reserved for tag badges, filter buttons, and category labels. The homepage's "Selected Work" tiles are a second, explicitly client-directed exception — a heart `clip-path`, not a radius — see the Heart-frame variant below; treat it as a one-off, not a precedent for organic shapes elsewhere.

**Signature shape — tilted real photography with a peeking accent shape:** the hero's `.polaroid-stack` is a swipeable/autoplaying pile of real photo cards (`aspect-ratio: 3/4` slot, bleeding off the homepage hero's right edge and overlapping the wordmark), kept structurally unchanged through the Oct 2026 redesign — only its surrounding tokens (the now-dark `--color-bg-blush` ground beneath it) moved. Every other page header keeps a smaller echo of that same layered look: `.page-header-photo-back` is a single `clip-path: polygon(...)` shape in a hot-pink→dark gradient, offset behind a rotated, slightly scaled-up real photo (`.page-header-photo`, `aspect-ratio: 3/4`) — so the pink shape still peeks out from one edge. New in this redesign: `.page-header-photo` now sits inside a thick `10px solid var(--color-accent-deep)` frame (was a hairline/shadow-only edge before) — a deliberately heavier device, scoped to page-header photos only, never the hero polaroid stack.

**Heart-frame variant, Oct 2026 — explicit client direction, a real departure from "near-flat/2px-radius everywhere":** the homepage's `.work-panel` tiles ("Selected Work") went through two passes before this one. First, flat rectangles with no tilt, no peeking shape, no hover feedback — the one place on the site presenting real photography with none of the signature device above. Then a corner-notch variant (an asymmetric `clip-path` chamfering one corner of each tile, revealing a solid accent layer behind it — kept the device's "accent peeks out" idea inside a tight grid where individual-tile rotation risked tiles colliding). The client then asked directly for "floating heart shaped frames," which this section now documents; the corner-notch CSS no longer exists. **This is a deliberate, acknowledged exception to the system's otherwise-flat, non-decorative shape language** — raised once to the client as a real departure from the editorial direction before building it, then built as asked once they confirmed.

Each `.work-panel` is no longer a grid cell: `.work-grid` is a centered, wrapping flex row, and each tile independently floats (`translateY` bob, `work-panel-float`, 6s, staggered per tile, `prefers-reduced-motion` disables it) with its own static rotation. The heart shape itself is one `<clipPath id="heart-clip" clipPathUnits="objectBoundingBox">` defined once in `index.html` and referenced via `clip-path: url(#heart-clip)` on two stacked layers — `.work-panel-accent` (a solid `--color-accent` heart, sized a few pixels larger via a negative `inset`) behind `.work-panel-photo` (the actual photo, clipped to the same path at `inset: 0`) — so the accent shows through as an even pink rim all the way around, a locket frame rather than a bare clipped photo. Depth comes from `filter: drop-shadow(...)` on the accent layer (not `box-shadow`, which would shadow the rectangular bounding box instead of the heart silhouette) and deepens on hover alongside a slight scale on the photo layer. `.work-tag` moved from an absolutely-positioned corner badge to a normal centered pill below each frame — hearts have no clean rectangular corner for a badge to sit in the way rectangles do.

**Desktop-only second row, same day.** Per feedback ("on desktop put more heart frames with images in 'em"), three more hearts (`.work-panel--c/--d/--e`, each category's second photo) sit alongside the original three, all six wrapping into a loose two-row cluster on wide viewports. Shared `.work-panel--extra` marker hides those three at the ≤900px tablet breakpoint (see `responsive.css`), so mobile keeps the original 3-heart scroll length rather than doubling it — "desktop" was explicit in the request, and the earlier mobile-first priority this project has been held to elsewhere argued against growing the mobile experience too.


**Tap to zoom.** A heart can be opened to a full-size view: tap, click, or press Enter/Space on a heart and it animates out from its own position, rotation, and scale via the Web Animations API, over a dimmed backdrop, with a caption below (`.heart-zoom-caption`, a documented display exception). Escape or a second tap closes it. The heart that is open is excluded from the periodic swap (`initHeartCycle`), and the zoom is skipped under reduced motion.
### Magazine devices (Oct 2026 "add character" pass)
Client asked for more character so the site doesn't read as generic or template-made; references were black-magazine cover/spread boards on Pinterest (giant cropped mastheads behind the model, vertical cover-lines, drop caps, print texture). Each device is type or texture placed directly on the seamless ground — none adds a surface, per the Seamless-Ground Rule.
- **Ghost word** (`.has-ghost` section + `<span class="ghost-word" aria-hidden="true">`): a giant italic Cormorant word (`clamp(7rem, 21vw, 18rem)`), outline-only (`-webkit-text-stroke: 1px rgba(255,133,176,.22)`, transparent fill), cropped off the viewport edge behind the section's content. `--right` anchors it right; `--low` drops it to the section's bottom so it sits behind a photo cluster instead of a heading. Placements: Home — "About" (right, behind the bio copy) and "Work" (low-left, beside the second row of hearts); About — "Story" (low-right, `.bio-section`); Contact — "Hello" (low-right, `.contact-section`); each brand page — "Fashion"/"Tech"/"SerenQ" (low-right, `.bio-section`). Portfolio and the Brands index have none (photo grid / full-width name rows leave no clear space). **Never let a ghost word cross a heading** — the first placement of "Work" did and read as clutter. Two per page max.
  **≤900px:** a ghost word stops being absolutely positioned (in a stacked one-column layout it just hid behind photos, leaving stray letter fragments) and becomes an in-flow section opener — `30vw`, its own line above the content, slightly stronger stroke (`.3` alpha), `--right` kept via `text-align: right` so pages still alternate sides.
- **Edition line** (`.edition-line`, hero only): a vertical uppercase cover-line ("Portfolio Edition — 2026 — …") up the hero's left edge, `0.65rem`/`0.32em` tracking, `--color-ink-soft`. Hidden below 1320px, where there's no margin outside the 1200px column for it.
- **Drop cap** (`.drop-cap::first-letter`): 4.6em italic Cormorant in `--color-accent`, floated — opens the homepage About passage, the About page bio, and each brand page's profile copy.
- **Type band** (`.marquee` > `.marquee-track`, homepage only, between Selected Work and What I Offer): a slow (45s) horizontal ticker of the cover-line words, `clamp(2.5rem, 6vw, 4.75rem)` italic Cormorant alternating solid `--color-ink` and pink-outline, separated by a small CSS-drawn pink diamond (a rotated square — the ✦ glyph fell back to a mismatched font inside Cormorant italic). Track holds two identical halves and translates `-50%` for a seamless loop; static under reduced motion; `aria-hidden`.
- **Contact-sheet frame numbers** (`.portfolio-item::before`, Portfolio grid): film-negative edge marks "01A, 02A…" from a CSS counter (`counter-reset: frame` on `.portfolio-grid`), `0.72rem` ink with a tight dark text-shadow for legibility over light skies. Filtered-out tiles drop out of the count.
- **Print grain** (`body::after`): a fixed, static SVG fractal-noise layer at 0.07 opacity over the whole viewport, `pointer-events: none`. No animation.

**Random rotation + tap-to-zoom, Oct 2026 (client request).** The hearts no longer hold fixed per-category picks: on every load each heart gets a random, non-repeating photo from the whole manifest (all categories pooled), and every 3.2s one visible heart crossfades (0.9s opacity, new `<img>` stacked over the old) to a photo not currently on any heart — only while the section is on screen and the tab visible, never the zoomed heart, never the same heart twice in a row, off under reduced motion. The `.work-tag` follows the photo's category. Tapping/clicking a heart (or Enter/Space — panels get `role="button"`, `tabindex="0"`, focus shows a light rim) lifts an enlarged copy out of the page to the viewport center (up to 560px wide, ≤86vw, ≤62vh tall) over an `rgba(0,0,0,.86)` backdrop, then — because the heart shape crops a lot of each photo — opens out into the **whole uncropped photo** at its own aspect ratio (as large as fits: ≤90vw/760px wide, ≤70vh tall) in a 6px hot-pink frame, the heart swelling and fading as the full photo scales up (0.88→1) into its place, with the manifest caption in italic Cormorant fading in below it. After 4.5s (or a tap/Escape) it folds back into the heart, which shrinks back into its slot. The copy is rendered at full size and animated from the small heart's position/rotation/scale to `none` (so the final state is sharp, not an upscaled raster), and its pink rim is scaled to keep the same proportion. `cursor: zoom-in` on hearts, `zoom-out` on the overlay. Overlay `z-index: 700` (above nav 500 and lightbox 600; the print grain still overlays it).

## Components

### Buttons
- **Shape:** 2px radius, solid fill, uppercase Manrope 700 label.
- **Primary** (`.btn-primary`): rose fill, dark (`--color-on-accent`) text, lift + deepen shadow on hover (`translateY(-3px)`), dark ripple on click.
- **Primary Inverse** (removed Oct 2026 with the Seamless-Ground pass — `.cta-close` now uses `.btn-primary`; history kept below) (`.btn-primary-inverse`): dark (`--color-on-accent`) fill, ivory (`--color-ivory-surface`) text — used only inside `.cta-close`, where the section background is itself the full rose accent, so this is the one button that needs to read dark-on-rose instead of the system default.
- **Secondary/Text** (`.btn-secondary`, `.text-link`): no fill; a rose-tint underline that solidifies to ivory ink on hover.
- **Filter pills** (`.portfolio-filters button`): transparent/outlined at rest, solid rose when `.active`; light ripple on click.

### Editorial List (signature component)
The site's recurring "contributor page" list pattern, reused with different content on four different pages: `.focus-list`/`.focus-item` (3-column, heading+paragraph — Home's "What I Offer", About's "Where I Create", Contact's "Good to Know") and `.glance-list`/`.glance-item` (a `<dt>/<dd>` fact-list variant — About's "At a Glance", each brand page's "Partnership" block, still plain hairline-divided text, unchanged by the card pass below).

**Seamless-Ground update, Oct 2026 (supersedes the card pass described next):** `.focus-item` no longer has a card surface or ring — open columns separated by the grid gap, keeping the numeral/italic-heading device. `.footer-form-card` likewise lost its tinted surface and ring (just a `max-width: 34rem` column). The paragraph below is history.

**Oct 2026 "lacks character" card pass (`.focus-item` only):** this is a deliberate reversal of the system's earlier "no bordered card grids" stance, made at the client's explicit direction ("make 'what I offer' in cards or something visually appealing"). Each `.focus-item` is now a standalone surface — `background: rgba(255,214,232,.04)`, a 1px light-tinted `box-shadow` ring (same hairline-via-shadow technique as the Cards/Tiles edge treatment, not a layout-affecting `border`), 2px radius — that lifts and brightens on hover (`translateY(-6px)`, deeper shadow, brighter background), all on `transform`/`box-shadow`/`background`, never layout properties. The old cell-divider borders (`border-right`/`border-bottom: var(--rule-soft)` between items) are gone; the grid gap alone now separates cards. `.glance-list` keeps the original plain hairline-divided text — the card treatment is scoped to `.focus-item` only, not the whole Editorial List pattern.

**Ambient ring texture, Oct 2026 layout pass:** `.focus-section` (the wrapper around every `.focus-list` instance) and the homepage's `.brand-strip` now each carry a `.glass-ripples` instance (same 6-span markup/CSS as the nav's) purely as background texture — these are long, photography-free text passages that read as flat empty stretches on the persistent dark ground, especially on mobile where there's no asymmetric grid to lean on. **This reuses only the ring-pulse decoration, not the glass/backdrop-blur surface** — see the Navigation entry below and the amended Don't rule for that distinction. Both sections needed `position: relative` added (the ripples' `position: absolute; inset: 0` had nothing to anchor to before).

**Numbered-index device, Oct 2026 "lacks character" pass:** each `.focus-item` now carries a large muted italic numeral (`counter-reset`/`counter-increment`, `decimal-leading-zero`) above its heading — `--font-heading` italic at 2.5rem, `--color-ink-soft` at 0.55 opacity, so it reads as a quiet "01/02/03" editorial index rather than a bare heading+paragraph repeated three times. Text-generated via CSS counters, not hand-typed per item, so reordering or adding a fourth `.focus-item` renumbers automatically. **The exact same device (same font/size/color/opacity, same counter mechanism) is reused on `.brand-row`** (see Brand Credits Row below) — one signature number treatment answers both "What I Offer lacks character" and "the brand names look pale," rather than two unrelated fixes.

### Cards / Tiles
- **Corner:** 2px radius, `overflow: hidden`. `.work-panel` is the one exception — see the Shapes section's Heart-frame variant above; its photo/accent layers are clipped to a heart `clip-path`, not a radius.
- **Edge:** `.portfolio-item` and `.gallery-tile` get a 1px `box-shadow: 0 0 0 1px rgba(255,214,232,.18)` — not a real `border`, so it doesn't add to the box's layout size against the grid's `aspect-ratio`/gap math. Light-tinted (not dark) against the current dark ground. `.work-panel` uses `filter: drop-shadow(...)` instead (see Shapes) since its accent/photo layers aren't rectangular.
- **Background:** the full Portfolio grid and the homepage portfolio teaser now hold real photography (`<img>`, `object-fit: cover`, passed through the site-wide cinematic grade filter); brand campaign-preview galleries still use duotone gradient "swatches" (`.swatch-1` through `.swatch-6`, each pairing `--color-accent`/`--color-accent-soft` against `--color-accent-deep` or `--color-bg-blush` for a clear luminance gap — the current hot-pink accent against true-black accent-deep gives a strong gradient with no risk of the prior palette's "both too light to pair" bug) standing in for real photography until their own photos arrive.
- **Overlay:** every tile — photo or swatch — gets the same two-layer gradient via a `::after` on the tile's photo layer (`.portfolio-item::after`, `.work-panel-photo::after`, `.gallery-tile::after`): a soft-light radial highlight (`circle at 75% 15%, rgba(255,214,232,.3)`, derived from `--color-ink`/`--color-ivory-surface` rather than a literal white) plus a subtle bottom-edge vignette (`linear-gradient(195deg, transparent 55%, rgba(0,0,0,.28) 100%)`).
- **States:** `.portfolio-item` scales its image/swatch slightly and reveals a "View" pill on hover/focus; `.work-panel` scales its photo layer and deepens its drop-shadow on hover (no "View" pill — these tiles aren't clickable, the teaser's actual CTA is the "View the full portfolio" link below the grid); filtered-out `.portfolio-item` tiles fade+scale out via `.is-hidden` before being set `hidden` (see PROJECT_NOTES.md for the CSS-specificity gotcha this required).

### Navigation (signature component, glass)
Manrope uppercase links (ivory `--color-ink`, not a borrowed token — see below) with an animated underline (`transform: scaleX()`, not `width`, to avoid layout thrash). The header itself is a dark-noir glass bar (`rgba(23,18,18,.9)` + `backdrop-filter: blur(18px) saturate(100%)`) with faint pulsing "water droplet" ring outlines (`.glass-ripples`, 6 staggered rings, `@keyframes ripple-pulse`) — the system's one intentionally non-flat, non-editorial surface. No saturation boost on the blur (a higher base opacity does the "glass" work instead); this was already tuned against the pre-redesign blush background and carried forward unchanged, since the header glass was already its own dark surface independent of the page-ground flip. Content (logo/links/toggle) is capped to the same 1200px column as the rest of the page via a `.nav-inner.container` child, but the glass bar itself spans the full viewport width edge-to-edge, not just that column. It resizes on scroll: fully grown at the very top, shrunk any time `scrollY > 0` (whether scrolling up or down), and gains a lifting drop-shadow (`.is-shadow`) any time it isn't at that resting top position, so it reads as hovering above content rather than flush with it.

**Desktop-only: fixed overlay + auto-hide.** Above 900px, the header is `position: fixed` rather than in-flow — it floats over the hero/page-header instead of pushing that content down, so the hero starts at the true top of the viewport with the glass bar (and its backdrop blur) overlaid on top of it. It also hides (`.is-hidden`, `transform: translateY(-100%)`) while actively scrolling down, and reappears the instant the user scrolls up. At ≤900px this all reverts to the original in-flow `position: sticky` header that simply pushes content down and never hides.

Mobile: a two-bar hamburger that morphs into an X (`.nav-toggle[aria-expanded="true"]`), opening `.nav-collapse` as a fixed off-canvas drawer (not an in-flow accordion) that slides in from the right over a dimming `.nav-scrim` backdrop — same dark glass and ripple treatment as the header bar, top-aligned links. Closes via the same toggle button (now an X), a tap on the scrim, or Escape.

**Because the header is glass over a now-also-dark page, its link color is still `--color-ink` directly** (not a separately borrowed token) — now that ink itself is the light ivory tone, no special-casing is needed the way the pre-redesign system needed to borrow a light neutral for this one dark surface. The logo and toggle bars use `--color-accent-soft` (not `--color-accent`), and ripple rings use a light ivory outline.

### Lightbox (signature component)
A fixed, centered overlay (`.lightbox-overlay`) that fades and scales in an enlarged panel showing the **whole photo** (`object-fit: contain`, letterboxed on the dark backdrop — the grid crops, the viewer never does). Oct 2026: a contact-sheet viewer — large Cormorant ‹ › arrows outside the panel on desktop (on dark discs over its edges ≤900px), arrow keys, and swipe step through the currently visible (filtered) tiles, wrapping; the new photo slides in ~6% from the direction of travel as the old slides out the other way (0.45s). A film-negative counter ("03 / 15", Manrope 700, 0.24em tracking, hot pink) sits above the caption; the category pill is pinned top-left over the photo. Width is capped against *both* viewport width and viewport height (converted through the panel's 4:5 ratio) so the close button and caption can never overflow off-screen on a short viewport.


**Prev/next arrows, Oct 2026:** the lightbox can step through the visible photos with arrow buttons (`.lightbox-nav`), large display-scale glyphs (`2.6rem` on desktop, `2.2rem` on mobile) that are a documented display exception (see Typography).
### First-visit intro (homepage only)
The issue's "cover": on a visitor's first ever load, a black screen with a giant pink italic Cormorant "C" (`clamp(9rem, 32vw, 15rem)`) inking in left-to-right (`ink-reveal`), and "PORTFOLIO EDITION — 2026" (Manrope 0.7rem, 0.32em tracking, `--color-ink-soft`) fading up beneath; after ~2.3s (or a tap/key) the cover fades away (0.8s) and the hero's own entrance plays. Never shown again (localStorage), never under reduced motion.

### Page-turn transitions
Cross-page navigation turns like a magazine page instead of crossfading: the old page swings away on its left spine (`perspective(1800px) rotateY(10deg) translateX(-5%)`, fading, 0.5s ease-in) while the new one slides in from 6% right (0.65s ease-out-expo, 0.12s later). The header holds still (`view-transition-name: site-header`). Native View Transitions — unsupported browsers just navigate normally.

### Site icon & link preview
Icon: a hot-pink italic Cormorant "C" on true black (`images/icons/`). Link-preview card (`images/og/og-cover.jpg`, 1200×630): kicker + hairline, the "Chioma" wordmark with its pink final "a" (matching the hero), the tagline in `--color-ink-soft`, the domain, and a graded hero photo feathered into the black on the right — the cover in miniature.

### Polaroid Stack (signature component, hero)
A pile of real photo cards (`.polaroid-stack` > `.polaroid-card`) in the homepage hero. Kept deliberately unchanged in structure and behavior through the Oct 2026 redesign per direction confirmation — only the dark ground beneath it changed. Front card centered/unrotated; back cards sit in fixed scatter "slots" (randomized only on reshuffle, not on every cycle) so cycling reads as one photo sliding back and the next rising to front. The card's own paper mat stays `--color-ivory-surface` (deliberately bright) regardless of the dark ground around it. Autoplays on a timer (paused off-screen, disabled under reduced motion), swipeable (drag flips which direction autoplay continues in), double-tap/-click or Enter reshuffles the scatter, arrow keys cycle. No-JS fallback is a fixed (non-random) fanned arrangement via CSS `nth-child` rules.

### Page-Header Photo (signature component, every other page)
A quieter, page-header-scale echo of the same idea: a single real photo (`.page-header-photo`), rotated and scaled up slightly, with a hot-pink `clip-path` shape (`.page-header-photo-back`) peeking out from behind on one side. New in this redesign: a thick `10px solid var(--color-accent-deep)` frame around the photo itself (was a hairline/shadow-only edge before) — the device is scoped to this component only, never the hero polaroid stack. `aspect-ratio: 3/4` (portrait, matching the source photos). Which photo shows is picked at random client-side on each page load from a fixed set, so the page/photo pairing isn't static.

**Reused, not duplicated, in the homepage About teaser:** `.about-grid` (Oct 2026 layout pass) now carries the exact same `.page-header-photo-frame` markup/CSS as its first column, capped to `max-width: 280px` **and `margin: 0 auto`** via `.about-grid .page-header-photo-frame`. Added because the teaser was a plain two-column text/text split with no photography at all — on the persistent dark ground this read as a large flat empty stretch, confirmed by the user ("too flat and plain"). No new photo-frame CSS was written; this is the identical component, just dropped into a third grid column. **The `margin: 0 auto` was a same-day follow-up fix**: without it, a block element capped to a fixed `max-width` inside a wider column just hugs the column's start edge per normal block layout, and this component's own `rotate()`/`scale()`/`translate()` transform shifts it further off-center on top of that — confirmed via `elementFromPoint` at 390px width, the photo's visual footprint ran ~x:-18 to x:306 in a 372px column before the fix. If this component is ever capped to a fixed width anywhere else, center it in the same edit, not as an afterthought.

### Brand Credits Row (`.brand-row`, homepage only)
Oct 2026 "lacks character" pass — was plain centered italic links with generous gaps, nothing distinguishing them from any other rose text-link on the page. Now a bounded "masthead credits line": `.brand-row` gets `border-top`/`border-bottom: var(--rule-soft)` and padding, turning the whole row into one deliberate editorial object rather than floating text. Each brand name sits inside `<a><span>Name</span></a>` — the `<a>` carries the same large muted-numeral `::before` as `.focus-item` (see Editorial List), `align-items: flex-start` stacks number above name, and the `<span>` carries the original italic-rose link styling plus its hover state (moved from the `<a>` itself so the number doesn't inherit the hover-underline treatment). **If you add a fourth brand, no HTML numbering is needed** — the CSS counter renumbers automatically, same as `.focus-item`.

**Mobile centering fix, same pass:** `align-items: flex-start` is correct for the desktop row (it aligns number above name across the cross axis of a `flex-direction: row` layout), but at the ≤600px breakpoint where `.brand-row` switches to `flex-direction: column`, `align-items` governs the now-horizontal cross axis instead — without an override every item (and its number) was shoving flush-left rather than centering. Fixed with a mobile-only `align-items: center` + `text-align: center` on `.brand-row`/`.brand-row a` in `responsive.css`. Any other component that flips `flex-direction` at a breakpoint should get the same cross-axis check.

### Offers, campaign embeds, and link-in-bio (Oct 2026)
Three new surfaces for promotions, built from existing components so they read as part of the same site.

- **Offers page (`offers.html`, in the main navigation and footer).** The page header matches the other inner pages. Offers are `.focus-item` cards in the same `.focus-list` grid as the Editorial List, with three additions: a brand label in `--color-accent` uppercase, the offer title, the details in `--color-ink-soft`, and an `.offer-code` row. The code is a dashed `--color-accent` box (`code`, `2px` radius, tinted fill) beside a `.btn-secondary` "Copy code" button, which copies the code and briefly reads "Copied". The `.btn-secondary` is reset to a plain button in the same way as the footer form button.
- **Campaign embeds (on the offers page).** Videos and images sit in `.embed-frame` boxes: 16:9 by default, `.embed-frame--portrait` (4:5) for vertical images, a `--color-bg-blush` ground, a 1px light ring, and a `2px` radius. Any `iframe` or `img` placed inside fills the frame absolutely. An empty slot shows a small uppercase `.embed-frame-empty` label.
- **Link-in-bio page (`link.html`, not in the navigation).** One centered column for the single link in a bio: a circular photo with an accent ring, the name in the display face, a one-line bio, and a stack of full-width `.link-button`s. Outlined buttons fill with `--color-accent` on hover and focus. The first button is the filled primary `.link-button--primary`. Social and email sit as small uppercase text links underneath.

These are intentionally plain: no tracking, no sign-up forms, no per-visitor codes.

### Footer (`.site-footer`, every page)
Oct 2026 "basically nonexistent" pass — was a single centered copyright line. Rebuilt from pieces the rest of the system already has, not a new visual language: a brand block (`.footer-wordmark`, a bare italic Cormorant Garamond mark at 1.9rem, deliberately *not* reusing the `.logo` class since that's scoped to `.site-nav` only and carries no standalone styling of its own) with a one-line tagline, and real contact/nav details — nothing fabricated. A hairline (`border-bottom`) on `.footer-top` separates it from `.footer-bottom`, a flex row holding the copyright line and a "Back to top" link (`href="#"`, relies on the browser default scroll-to-top rather than a hand-placed `id="top"` anchor). **Every page's footer is hand-duplicated with correct relative paths** (plain paths on root-level pages, `../`-prefixed on `brands/*.html`, except the "Brands" link itself which stays bare from within `brands/`) — same no-templating constraint as the nav; if you edit the footer again, check all 8 pages via `grep -rn "footer-top"`, not just one.

**Two-zone restructure, same-day follow-up.** The original layout was a flat 3-column `.footer-grid` (brand | Navigate | Connect) with the quick-message form in its own full-width row underneath — reading as four stacks of plain text in a row, with nothing to separate the form from the nav links next to it. Feedback: "the footer have some character, it looks flat... navigate and connect in the same row messes things up." Rebuilt as two deliberate zones in `.footer-top` (`display: grid; grid-template-columns: 1.3fr 1fr;`, collapsing to 1 column at ≤900px, same breakpoint list as `.hero-grid`/`.about-grid`/etc.):
- **`.footer-contact`** (left): the brand block, with `.footer-form-card` — the "Send a Quick Message" form promoted into its own tinted, ringed surface — stacked directly beneath it.
- **`.footer-link-columns`** (right): Navigate and Connect as two side-by-side sub-columns (`display: grid; grid-template-columns: repeat(2, 1fr);`), directly per the client's own suggested fix ("have navigate and connect side by side").

**Reorder, same day.** The form initially sat in its own zone to the *right* of a combined brand+nav+connect column. Feedback: "move the form above the connect and navigate." Regrouped instead around *what* each zone is for — `.footer-contact` (brand statement + the CTA form, both "about/reach us") versus `.footer-link-columns` (pure navigation, "where to go") — rather than the form floating as a disconnected third element. This also fixes the stacking order at the ≤900px collapse: brand, then form, then Navigate/Connect, matching the "form in a container above or below" fallback the client floated in the original request.

The form card itself reuses the exact card-edge language `.focus-item` established (see Editorial List → Oct 2026 card pass: `background: rgba(255,79,139,.06)`, a 1px light-tinted `box-shadow` ring, 2px radius) rather than inventing a second card style. This is the footer's one deliberate CTA object, the direct answer to "give it character." The "Send a Quick Message" label is tinted `--color-accent` (not the default `--color-ink-soft`) inside this card only, so it reads as the footer's accent moment. Fields stack full-width in a column (not the old wrapping flex row, since the card is narrower than the old full-bleed row was), and the submit button is `.btn-primary` (solid pink fill, full-width) rather than the original `.btn-secondary` text-link — a stronger visual anchor befitting a card's one clear action.

**No backend exists on this static site**, so the form is wired client-side in `js/main.js` (`initFooterForm`) to build a `mailto:` link from the three field values and hand off to the user's own email client on submit — the only genuinely functional option that doesn't add a third-party form-service dependency requiring separate approval/account setup. An `aria-live="polite"` note below the form confirms this handoff (and gives a manual-email fallback) since the mail client opening is invisible to the page itself. Identical markup on all 8 pages, same hand-duplication constraint as the rest of the footer — the form itself has no page-relative links, so it's lower-risk to propagate than the nav/footer-links columns.

## Do's and Don'ts

### Do:
- **Do** keep every dark/neutral value one of the system's two literal blacks (`#000000` or `#222222`) or the interpolated `#111111` midpoint — check new colors against the True-Black Rule.
- **Do** keep the dark ground persistent and continuous across every page/section — no section gets its own background fill (see the Seamless-Ground Rule); the pink CTA glow is the system's one strong color moment.
- **Do** run every new real photo through the site-wide `img` filter (`saturate(0.78) sepia(0.16) contrast(1.08) brightness(0.96)`) rather than hand-grading individual images — it's what keeps mixed color/black-and-white shoots reading as one body of work.
- **Do** reuse the editorial-list pattern (`.focus-list`/`.glance-list`) for any new "several short facts" content. `.focus-item` is now a bordered-surface card (see Editorial List → Oct 2026 card pass); `.glance-list` stays plain hairline-divided text — match whichever of the two the new content is closer to, rather than inventing a third treatment.
- **Do** let below-the-masthead content enter via the shared scroll reveal (`initScrollReveal()` in `main.js`, Oct 2026): elements ease up 32px and fade in over 1s as they cross 12% above the viewport bottom, siblings staggered 110ms (capped at 4), kicker hairlines draw across (`scaleX`) after their label, ghost words drift in from their own side over ~2s. Opt in by matching `REVEAL_SELECTOR` there or adding `.reveal`; hero/page-header are excluded (they have their own authored entrance). States only apply once JS adds `.reveal-armed`, so no-JS and reduced-motion visitors always see content.
- **Do** use `--ease-out-expo` (`cubic-bezier(0.16, 1, 0.3, 1)`) for all deliberate motion; it's the system's one easing curve.
- **Do** treat the rotated-photo-over-clipped-polygon peeking-accent-shape pattern as the site's default way of presenting real photography in hero/masthead positions. The homepage's heart-frame tiles (see Shapes) are a one-off, explicitly client-directed exception, not a template for other components — check with the client before extending organic/decorative shapes elsewhere.

### Don't:
- **Don't** animate `width`/`height`/`padding`/`margin` for hover or state feedback; use `transform`/`opacity`. **Confirmed exception:** the header's scroll-shrink `transition: padding` — a `transform: scale()` would visually distort the logo/link text instead of the box genuinely resizing, and it's one small element transitioning at most once per scroll-direction change, not a per-frame animation. Don't extend this exception to anything else without the same reasoning holding.
- **Don't** add icon+heading+text card grids with illustrative icons — `.focus-item`'s Oct 2026 card treatment (subtle tinted surface + shadow-ring edge, numeral instead of icon) is the one confirmed exception; it doesn't license icon-led cards generally.
- **Don't** extend the hero wordmark's 9rem display-size exception to any other heading.
- **Don't** extend the glass/backdrop-blur *surface* (`backdrop-filter`, the translucent dark fill) beyond the site header/nav — it's a deliberate, one-surface exception to the "flat by default" rule. **Do**, however, reuse the `.glass-ripples` *ring-pulse decoration on its own* as ambient texture in long photography-free text sections (see Editorial List → "Ambient ring texture") — that's a lighter-weight reuse of one decorative device, not an extension of the glass material itself.
- **Don't** extend the thick `10px` photo-frame device to the hero polaroid stack; it's scoped to `.page-header-photo` only, a deliberate contrast between the two photo-presentation scales.
- **Don't** introduce a second interactive accent hue alongside Hot Pink, and don't reintroduce accent-on-light-background reasoning — there is no light background left in the system to fail contrast against; hot pink is the primary interactive color on the dark ground itself.
