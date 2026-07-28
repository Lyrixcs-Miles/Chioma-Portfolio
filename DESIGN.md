---
name: Eullie
description: Personal brand site for Eullie — fashion/beauty/lifestyle model, content creator, and brand ambassador.
colors:
  bg: "#FFFFFF"
  bg-pearl: "#FAF9FB"
  bg-lavender: "#F2ECF7"
  accent: "#5B2A86"
  accent-soft: "#A98BC7"
  accent-deep: "#3D1C60"
  ink: "#241530"
  ink-soft: "#6B5A7D"
  on-accent: "#FAF9FB"
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
    backgroundColor: "{colors.bg-pearl}"
    textColor: "{colors.accent}"
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

# Design System: Eullie

## Overview

**Creative North Star: "The Lookbook Cover"**

The site reads as a fashion lookbook's opening spread rather than a
templated influencer landing page: an editorial masthead, real
photography presented as tilted, layered "polaroid" cards (a hero
photo stack, and a photo-plus-peeking-accent-shape treatment on every
other page header), and kicker-plus-hairline labeling borrowed from
magazine contributor pages. The palette and type
pairing were pinned by the client brief (exact hex values and font
names supplied up front), so the visual world was never an open
concept choice — the craft lives in composition: the masthead's
oversized cover-line bleeding behind the panel, the asymmetric
contact-sheet portfolio grid, and the reused "at a glance" fact-list
pattern that ties About, Contact, and the brand profile pages together.

Confirmed rejection: no centered-headshot-plus-CTA-button template
hero, no icon+heading+text card grids, no gray neutrals (every neutral
in the palette is tinted from the plum hue, never literal black/gray).

**Key Characteristics:**
- Editorial, not corporate-influencer: kickers, hairline rules, serif italic labels
- Palette is a brief-pinned "Full palette" strategy (5 named roles), not a designer's free choice
- One tilted-photo-plus-peeking-accent-shape motif reused at two scales: the hero's swipeable/autoplaying polaroid stack (masthead-size, Home only) and a single rotated photo with a purple clipped shape peeking from behind (page-header size, every other page)
- Flat surfaces, tinted plum shadows, near-zero border-radius except pill badges/buttons — **the one deliberate exception is the site header**, a dark-plum glass (`backdrop-filter: blur`) that floats above page content, the system's only non-flat surface
- Motion is deliberately restrained: one authored focal sequence on the homepage, quiet shared support elsewhere

## Colors

Full palette strategy — five named roles, each owning a field-scale region rather than appearing as scattered accents. No black anywhere by explicit brief requirement.

### Primary
- **Royal Plum** (`#5B2A86`, `--color-accent`): CTAs, headings-as-accent (the colored last letter in the wordmark), links, active states, the closing CTA section's full-bleed background.

### Secondary
- **Soft Orchid** (`#A98BC7`, `--color-accent-soft`): decorative/structural only — gradient stops, hairline-rule tints, hover-state borders. **Never used as standalone text color**: it fails 4.5:1 contrast against both white and the lavender background (~2.5–2.9:1 measured).
- **Deep Plum** (`#3D1C60`, `--color-accent-deep`): gradient/shadow depth stop, never a stand-in for black.

### Neutral
- **White** (`#FFFFFF`, `--color-bg`): primary page background.
- **Pearl** (`#FAF9FB`, `--color-bg-pearl`): secondary background — About-teaser, footer, brand-gallery sections.
- **Whisper Lavender** (`#F2ECF7`, `--color-bg-lavender`): section-background role — hero, page-headers, brand strip.
- **Ink** (`#241530`, `--color-ink`): primary text. A deep plum-black, not literal black — this is the "no black anywhere" rule's load-bearing color.
- **Ink Soft** (`#6B5A7D`, `--color-ink-soft`): secondary/muted text, tinted from the accent hue rather than gray (measured ~6.2:1 on white, passes).
- **On-Accent** (`#FAF9FB`, `--color-on-accent`): text/icon color on solid plum surfaces (buttons, closing CTA).

### Named Rules
**The No-Black Rule.** Every dark value in the system is plum-tinted (`#241530`, `#3D1C60`), never a neutral gray or `#000`. This was an explicit, non-negotiable brief requirement — check any new dark color against it before adding.

**The Orchid-Is-Decorative Rule.** Soft Orchid (`#A98BC7`) never carries body or label text on a light ground; it fails contrast. It only appears as fills, gradient stops, and hairline tints.

## Typography

**Display/Headline Font:** Cormorant Garamond (italic weight 500/600), with Georgia/Times New Roman fallback
**Body/UI Font:** Manrope (400/500/600/700), with system-sans fallback

**Character:** A high-contrast italic display serif (editorial, cover-line register) paired with a clean geometric grotesque for everything functional (nav, labels, body, buttons) — the magazine-masthead-meets-caption-line pairing.

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

## Layout

`.container`: max-width 1200px, centered, 1.5rem side padding (1rem at ≤900px). Section vertical rhythm uses a single `--section-pad` custom property: 7rem desktop → 5rem at ≤900px → 3.5rem at ≤600px.

Breakpoints: 900px (tablet — grids collapse to 1 column, hero-visual reorders above the copy) and 600px (mobile — nav becomes a slide-down panel, portfolio/work grids go single-column).

Recurring grid shapes: two-column asymmetric splits (`1.15fr/1fr` hero, `0.6–0.85fr / 1.15–1.4fr` bio/page-header/contact panels), a 6-column asymmetric span grid for the homepage portfolio teaser (one `span 4 / row 2` tile + two `span 2` tiles), a 3-column grid with occasional `span 2` "wide" tiles for the full Portfolio contact-sheet, and plain 3-equal-column grids for the reusable editorial list component (see Components → Editorial List).

## Elevation & Depth

Flat by default. Depth appears only as tinted, soft-blurred drop shadows on interactive/floating elements (buttons on hover, the polaroid cards/page-header photo, the lightbox panel) — never a neutral gray shadow. Two plum-black tints are in use: `rgba(36, 21, 48, X)` (= `--color-ink`, for surface-level lift) and a slightly deeper `rgba(15, 8, 20, X)` (for elements that float furthest off the page — the pearl-background button and the lightbox). Both satisfy the No-Black Rule; the second is documented here rather than unified into one value since it reads as a deliberate "floats-higher-gets-darker" depth cue, not an authoring slip.

### Shadow Vocabulary
- **Button Lift** (`0 14px 28px -14px rgba(36,21,48,.55)` → `0 20px 34px -12px rgba(36,21,48,.6)` on hover): `.btn-primary`.
- **Button Lift (Inverse)** (`0 14px 28px -14px rgba(15,8,20,.35)`): `.btn-primary-inverse` — the pearl-fill button uses the deeper tint since it sits on the plum CTA background.
- **Panel Float** (`0 32px 60px -22px rgba(36,21,48,.5)`): each `.polaroid-card` in the hero stack, and `.page-header-photo` on every other page.
- **Lightbox Lift** (`0 50px 90px -30px rgba(15,8,20,.65)`): the enlarged lightbox panel — the deepest shadow in the system, matching its topmost z-index.

### Named Rules
**The Tinted-Shadow Rule.** Every shadow's color is a plum, never gray/black — consistent with the No-Black Rule above.

## Shapes

Near-flat throughout: `2px` border-radius on cards, tiles, and buttons (an editorial, not-rounded feel). The one exception is pill shapes (`100px` radius) reserved for tag badges, filter buttons, and category labels — a deliberate contrast between "flat editorial surface" and "rounded UI control."

**Signature shape — tilted real photography with a peeking accent shape:** the hero's `.polaroid-stack` is a swipeable/autoplaying pile of real photo cards (`aspect-ratio: 3/4` slot, bleeding off the homepage hero's right edge and overlapping the wordmark) that replaced the original duotone silhouette panel placeholder. Every other page header keeps a smaller echo of that panel's two-layer look — `.page-header-photo-back` is a single `clip-path: polygon(...)` shape in orchid→lavender gradient, offset behind a rotated, slightly scaled-up real photo (`.page-header-photo`, `aspect-ratio: 3/4`) — so the purple shape still peeks out from one edge the way the old silhouette's back layer did, just behind a photo instead of another gradient panel.

## Components

### Buttons
- **Shape:** 2px radius, solid fill, uppercase Manrope 700 label.
- **Primary** (`.btn-primary`): plum fill, pearl text, lift + deepen shadow on hover (`translateY(-3px)`), ripple on click.
- **Primary Inverse** (`.btn-primary-inverse`): pearl fill, plum text — used on the plum-background closing CTA.
- **Secondary/Text** (`.btn-secondary`, `.text-link`): no fill; an orchid-tint underline that solidifies to plum on hover.
- **Filter pills** (`.portfolio-filters button`): transparent/outlined at rest, solid plum when `.active`; ripple on click.

### Editorial List (signature component)
The site's recurring "contributor page" list pattern, reused with different content on four different pages: `.focus-list`/`.focus-item` (3-column, hairline-divided, heading+paragraph — Home's "What I Offer", About's "Where I Create", Contact's "Good to Know") and `.glance-list`/`.glance-item` (a `<dt>/<dd>` fact-list variant — About's "At a Glance", each brand page's "Partnership" block). Both are plain hairline-divided text, never bordered icon cards.

### Cards / Tiles
- **Corner:** 2px radius, `overflow: hidden`.
- **Background:** the full Portfolio grid and the homepage portfolio teaser now hold real photography (`<img>`, `object-fit: cover`); brand campaign-preview galleries still use duotone gradient "swatches" (`.swatch-1` through `.swatch-6`, defined in the palette family) standing in for real photography until their own photos arrive.
- **Overlay:** every tile — photo or swatch — gets the same radial soft-light highlight, via a `::after` on the tile itself (`.portfolio-item::after`, `.work-panel::after`, `.gallery-tile::after`) so it works whether the tile holds an `<img>` or a swatch span.
- **States:** `.portfolio-item` scales its image/swatch slightly and reveals a "View" pill on hover/focus; filtered-out tiles fade+scale out via `.is-hidden` before being set `hidden` (see PROJECT_NOTES.md for the CSS-specificity gotcha this required).

### Navigation (signature component, glass)
Manrope uppercase links (pearl, not the system's usual ink — see below) with an animated underline (`transform: scaleX()`, not `width`, to avoid layout thrash). The header itself is a dark-plum glass bar (`rgba(36,21,48,.78)` + `backdrop-filter: blur(18px) saturate(160%)`) with faint pulsing "water droplet" ring outlines (`.glass-ripples`, 6 staggered rings, `@keyframes ripple-pulse`) — the system's one intentionally non-flat, non-editorial surface. Content (logo/links/toggle) is capped to the same 1200px column as the rest of the page via a `.nav-inner.container` child, but the glass bar itself spans the full viewport width edge-to-edge, not just that column. It resizes on scroll: fully grown at the very top, shrunk any time `scrollY > 0` (whether scrolling up or down), and gains a lifting drop-shadow (`.is-shadow`) any time it isn't at that resting top position, so it reads as hovering above content rather than flush with it.

**Desktop-only: fixed overlay + auto-hide.** Above 900px, the header is `position: fixed` rather than in-flow — it floats over the hero/page-header instead of pushing that content down, so the hero starts at the true top of the viewport with the glass bar (and its backdrop blur) overlaid on top of it. It also hides (`.is-hidden`, `transform: translateY(-100%)`) while actively scrolling down, and reappears the instant the user scrolls up, so it doesn't permanently occupy screen space over page content but is always one upward scroll away. At ≤900px this all reverts to the original in-flow `position: sticky` header that simply pushes content down and never hides — the overlay/auto-hide treatment is desktop-only.

Mobile: a two-bar hamburger that morphs into an X (`.nav-toggle[aria-expanded="true"]`), opening `.nav-collapse` as a fixed off-canvas drawer (not an in-flow accordion) that slides in from the right over a dimming `.nav-scrim` backdrop — same dark glass and ripple treatment as the header bar, top-aligned links (not vertically centered). Closes via the same toggle button (now an X), a tap on the scrim, or Escape. At ≤600px the header's resting (top-of-page) size matches its already-shrunk scrolled size, rather than growing larger at rest — per feedback that the larger resting size read as too big on mobile.

**Because the header is glass, its text/logo/toggle/ripple colors are inverted from the rest of the system**: `.site-nav ul li a` and the mobile drawer's links use `--color-bg-pearl` (not the system-wide `--color-ink` default), the logo uses `--color-accent-soft` (not `--color-accent`), and ripple rings use a light pearl outline — the system's usual light-background/dark-text pairing would be nearly invisible on this one dark surface.

### Lightbox (signature component)
A fixed, centered overlay (`.lightbox-overlay`) that fades and scales in a single enlarged panel — a real `<img>` for the Portfolio grid's photos, a swatch-tinted panel for anything still on placeholder imagery. Width is capped against *both* viewport width and viewport height (converted through the panel's 4:5 ratio) so the close button and caption can never overflow off-screen on a short viewport.

### Polaroid Stack (signature component, hero)
A pile of real photo cards (`.polaroid-stack` > `.polaroid-card`) in the homepage hero, replacing the old duotone silhouette panel in the same slot and reusing its one-time `page-open` 3D entrance. Front card centered/unrotated; back cards sit in fixed scatter "slots" (randomized only on reshuffle, not on every cycle) so cycling reads as one photo sliding back and the next rising to front. Autoplays on a timer (paused off-screen, disabled under reduced motion), swipeable (drag flips which direction autoplay continues in), double-tap/-click or Enter reshuffles the scatter, arrow keys cycle. No-JS fallback is a fixed (non-random) fanned arrangement via CSS `nth-child` rules.

### Page-Header Photo (signature component, every other page)
A quieter, page-header-scale echo of the same idea: a single real photo (`.page-header-photo`), rotated and scaled up slightly, with a purple `clip-path` shape (`.page-header-photo-back`) peeking out from behind on one side — same visual logic as the polaroid stack's front-card-over-back-layer look, at a single-photo scale. `aspect-ratio: 3/4` (portrait, matching the source photos and the hero's original proportions — a 4:3 landscape frame cropped these portrait phone photos too aggressively). Which photo shows is picked at random client-side on each page load from a fixed set, so the page/photo pairing isn't static.

## Do's and Don'ts

### Do:
- **Do** keep every dark/neutral value plum-tinted — check new colors against the No-Black Rule.
- **Do** reuse the editorial-list pattern (`.focus-list`/`.glance-list`) for any new "several short facts" content rather than inventing icon cards.
- **Do** use `--ease-out-expo` (`cubic-bezier(0.16, 1, 0.3, 1)`) for all deliberate motion; it's the system's one easing curve.
- **Do** treat the tilted-photo-plus-peeking-accent-shape pattern (`.polaroid-stack` on Home, `.page-header-photo-frame` everywhere else) as the site's default way of presenting real photography in the hero/masthead position — it replaced the old duotone-silhouette placeholder now that real photos exist for every one of those slots.

### Don't:
- **Don't** use Soft Orchid (`#A98BC7`) as text color on a light background — it fails contrast.
- **Don't** animate `width`/`height`/`padding`/`margin` for hover or state feedback; use `transform`/`opacity` (the nav underline and brand-index-row hover were both fixed for exactly this). **Confirmed exception:** the header's scroll-shrink `transition: padding` — a `transform: scale()` would visually distort the logo/link text instead of the box genuinely resizing, and it's one small element transitioning at most once per scroll-direction change, not a per-frame animation. Don't extend this exception to anything else without the same reasoning holding.
- **Don't** add icon+heading+text card grids; the system's list pattern is hairline-divided text, not bordered cards.
- **Don't** extend the hero wordmark's 9rem display-size exception to any other heading.
- **Don't** extend the glass/backdrop-blur treatment beyond the site header/nav — it's a deliberate, one-surface exception to the "flat by default" rule, not a new standing pattern for cards, panels, or other components.
