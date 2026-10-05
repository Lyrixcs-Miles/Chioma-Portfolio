# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Two audiences share this site:

1. **Brands, agencies, and collaborators** evaluating Chioma for modeling, content, or partnership work — deciding whether to book or reach out to her.
2. **General visitors** browsing her fashion/beauty/lifestyle portfolio and discovering the Azhyre/SerenQ brand ecosystem she's affiliated with.

## Product Purpose

A personal portfolio for Chioma, a fashion/beauty/lifestyle model and content creator, that showcases her work and her role as brand ambassador for Azhyre Tech, Azhyre Fashion, and SerenQ. Success means a visitor can browse/filter her portfolio, learn who she is, find the brands she's connected to, and reach her.

## Positioning

Open decision: the site combines a personal-portfolio identity with a hub pointing to three affiliated brand ventures (Azhyre Tech, Azhyre Fashion, SerenQ). The precise differentiation of Chioma's role relative to those brands (exclusive ambassador vs. one of several, founder involvement, etc.) has not been confirmed and should not be assumed.

## Operating Context

Static site, no backend or build step, deployed via GitHub Pages at the custom domain `soma.azhyre.co.za` (see `CNAME`). Pages: Home (`index.html`), About (`about.html`), Portfolio (`portfolio.html` — filterable by fashion/beauty/lifestyle with a lightbox), Brands (`brands/index.html` plus `azhyre-tech.html`, `azhyre-fashion.html`, `serenq.html`), and Work With Me (`contact.html`). Shared nav/footer across all pages; `js/main.js` drives the mobile nav toggle, portfolio filters, and lightbox; styles split between `css/style.css` (base) and `css/responsive.css` (breakpoints).

## Capabilities and Constraints

- Filterable portfolio grid with lightbox, no CMS — portfolio items are hand-added `<a>`/`<img>` entries per the commented example in `portfolio.html`.
- Mobile nav toggle via `js/main.js`.
- Contact mechanism: `contact.html` has two email addresses (business `chioma@azhyre.co.za`, personal `chiomabvuma@icloud.com`), two phone numbers (`+27 79 247 4794`, `+27 69 474 5469`), and social links for Instagram (`@itsschibaby`) and TikTok (`@itssoma75`). No Facebook link — none was supplied for Chioma, so the old Facebook entry was removed rather than carried over or guessed at.
- Brand pages (`brands/*.html`) are structurally scaffolded but have no real content per brand yet.

## Brand Commitments

- Site identity/name: "Chioma."
- Affiliated brands, current relationship confirmed as model/content creator and ambassador: **Azhyre Tech**, **Azhyre Fashion**, **SerenQ**. Further specifics of each brand relationship (equity, employment, exclusivity) are not established.

## Evidence on Hand

The Portfolio grid now has real photography (11 shots across fashion/beauty/lifestyle, in `images/portfolio/`). Every other page still holds placeholder copy ("content goes here," "A little about me goes here"), and brand campaign galleries still have no real photos. Future work must not invent bio details, photos, testimonials, brand descriptions, pricing, or contact information — this content will be supplied later.

## Product Principles

1. Portfolio and brand hub are equal citizens — nav and home should serve both without either crowding out the other.
2. Build structure and design system ahead of content, but never fabricate copy, photography, or brand facts to fill gaps.
3. The fashion/beauty/lifestyle imagery is the primary evidence of credibility once supplied — the display craft around that imagery (grid, filtering, lightbox) matters more than dense text.
4. Keep the stack lightweight and static — no build step, deployable as-is to GitHub Pages.

## Accessibility & Inclusion

No product-specific requirement established yet.
