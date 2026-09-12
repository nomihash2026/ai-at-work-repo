# ai-at-work.au

Python static site generator, no dependencies beyond python3. 65 routes, each
written as `<route>/index.html`.

## Commands

```bash
python3 build.py                    # build every route into ./site
python3 build.py --serve            # build, then serve ./site on :8000
python3 scripts/verify.py           # link check, schema, GTM, metadata, form, blog
python3 scripts/audit.py            # layout: overflow, tap targets, console, 5 widths
python3 scripts/shots.py [routes]   # screenshot at 1280px and 390px
python3 scripts/e2e.py              # drive the assessment through to the form
python3 scripts/patch_assessment.py # re-apply our changes to the ported engine
```

`verify.py` exits non-zero on failure. Run it before every deploy — it is the
only thing standing between a broken internal link and production.

`audit.py` drives a real browser over thirteen representative routes at 1440,
1280, 900, 390 and 320 wide, with the menu opened at each, and fails on
horizontal overflow, any element wider than the viewport, text under 14px, tap
targets under 24px and console errors. It catches the class of problem a link
check cannot see. Links inside a sentence are exempt from the tap-target rule,
per WCAG 2.5.8.

## Layout

```
build.py              shell, nav, footer, schema, GTM, sitemap, robots, SITEMAP.md
netlify.toml          MUST stay at repo root; Netlify ignores it anywhere else
data/
  site.py             domain, GTM container, org identity, the one CTA, industries
  media.py            the image registry: one image per route, maximum
  nav.py              mega menu, footer, breadcrumb parents and labels
  metas.py            title/description overrides for salvaged pages
src/
  base.css            the original stylesheet, salvaged
  extra.css           figures, artwork, enquiry form, blog
  illos.py            SVG artwork (svg_*) and HTML diagrams (dg_*)
  assessment.css/js   the ported planning tool; edit via patch_assessment.py
  prompt.css/js       the prompt builder; plain source, no patch script
  assessment.main.html
content/
  meta.json           salvaged per-route metadata and original JSON-LD
  pages/*.html        salvaged <main> content, one file per route
  helpers.py          sect(), faq_section(), faq_schema()
  newpages.py         contact, thank-you, privacy — written here, not salvaged
  expansions.py       the expansion pass; merges the exp_* builders
  exp_training.py     depth for /training/*
  exp_tools.py        depth for /tools/*
  exp_library.py      depth for guides, resources, industries, about, case studies
  exp_more.py         depth for home, services, pricing, why-two-tools, assessment
  audience.py         /who-this-is-for/ and the prompt builder page
  figures.py          the five diagrams that replaced the screenshot slots
  llms.py             the curated llms.txt index, checked against the registry
  posts.py            blog engine: markdown subset, hub, categories, Article schema
  posts/*.md          the articles
static/
  brand/              generated brand assets, copied through as-is
  photo/              supplied photography and screenshots, copied to /photo/
  netlify.toml        drag-and-drop copy (no [build] section)
  _redirects          hand-maintained; build.py never writes it
site/                 build output — the publish directory
```

## How a page is assembled

1. `content/pages/<slug>.html` supplies the salvaged `<main>`, with metadata and
   original JSON-LD from `content/meta.json`.
2. `sanitise()` strips the legacy in-page green CTA band and demotes it to a
   plum prompt pointing at the enquiry form.
3. `content/expansions.py` appends depth sections and FAQ schema inside `<main>`.
4. `data/metas.py` overrides titles and descriptions last, so it always wins.
5. `render()` wraps it in the shell: GTM, schema graph, nav, footer, closing CTA.

Pages written from scratch (`contact`, `thank-you`, `privacy`, the blog) skip
steps 1–3 and go straight into the registry.

## Conventions worth not breaking

- **One image per page, one slot.** `data/media.py` is a dict keyed by route,
  so a second image on a page is not expressible. It renders directly under the
  hero on every route that has one, never anywhere else. A registered file that
  is not yet in `static/photo/` is skipped silently and listed by `build.py`, so
  the site stays shippable ahead of the photography.
- **One conversion action.** The enquiry form at `/contact/` is the only form on
  the site, and `verify.py` asserts that. Everything else links to it. Both
  tools — the assessment and the prompt builder — are tools rather than
  conversions: each hands its result to the form via `sessionStorage` under the
  `aiw_plan` key, same tab only and never a query string, and asks for nothing.
  A tool that captured an address itself would be a second form and a second
  destination, which is the thing this rule exists to prevent.
- **Tool assets are per-route.** `build_tool_assets(name)` hashes
  `src/<name>.css` and `src/<name>.js`; `TOOL_ASSETS` in `main()` maps a route
  to the pair. Shared option, field and action styling lives in `extra.css`, not
  in either tool sheet, so the two tools cannot drift apart visually.
- **One loud green surface per page.** The closing CTA band. Green elsewhere is
  the mark and small labels only. `verify.py` checks no `.cta` appears inside
  `<main>`.
- **Trailing slashes throughout.** `_redirects` forces one canonical form.
- **Every item in the top bar opens a panel, and there is exactly one action.**
  A bare destination link sitting among the category labels reads as a second,
  competing call to action. "Build your plan" lives in two panels, the home
  hero and the footer instead.
- **Menu and footer carry the same structure.** The menu is the interactive
  path, the footer is the crawlable one. Anything that matters appears in both.
- **Nothing deeper than three levels**; every page two clicks from home.
- **Edit sources, not output.** `src/assessment.js` via the patch script,
  `content/pages/*.html` and the `exp_*` modules for page content, never
  `site/`.
- **`_redirects` and both `netlify.toml` files are hand-maintained.** Rebuilding
  never clobbers them.
- **No invented facts.** No prices, CPD hour counts, client names, testimonials
  or statistics anywhere. Where a number would be invented, the page says what
  moves it instead.
- **Motion only where it answers an action.** Reduced motion respected.

## Discoverability

`robots.txt` names fifteen crawlers explicitly rather than leaving them to the
wildcard, because several read a named block and ignore `*`, and being quotable
inside an answer engine is the point of publishing the guides and the blog.

`llms.txt` is a curated index in the `llms.txt` convention: what the site is,
the positions it takes, and the pages worth reading, in that order. It is
hand-ordered in `content/llms.py` rather than generated from the route list,
because a model answering a question needs the useful forty rather than all
seventy-one. `verify.py` fails the build if any link in it is dead.

The schema graph carries `Organization`, `WebSite`, `BreadcrumbList` and a
`WebPage` node on every route, page-type schema on top, and an `ItemList` on
each hub declaring what it indexes.

`sitemap.xml` emits `lastmod` only where a real publication date exists.
Stamping every URL with the build date says the whole site changed on every
deploy, which is untrue and quickly discounted.

## Analytics

Google Tag Manager container `GTM-5BL56Z44`, in the head and as a `<noscript>`
iframe, on every route. `/thank-you/` pushes an `enquiry_submitted` event to
`dataLayer` for conversion tracking.

The CSP in both `netlify.toml` files allows googletagmanager and
google-analytics and nothing else. **Any other tag added inside the container
will be silently blocked until that list is widened.** If a tag does nothing in
production, check the browser console for a CSP violation before assuming the
tag is misconfigured.

`/privacy/` documents this accurately. If the container gains anything with a
wider reach — an ad pixel, a remarketing tag, a session recorder — that page
needs updating in the same deploy.

## The enquiry form

Netlify Forms: `name="enquiry"`, hidden `form-name` field, `bot-field`
honeypot, posting to `/thank-you/`. Netlify detects the form in the deployed
HTML, stores submissions, and emails them — set the notification address in
Netlify under Forms, and set up `hello@ai-at-work.au`, which is published on
the contact page.

## Deploying

**Git-based.** `netlify.toml` at the repository root, publish directory `site`,
build command `python3 build.py`.

**Drag-and-drop.** Drop the **contents** of `site/`, not the repo folder and not
a zip with a wrapper directory. Netlify looks for `index.html` at the root of
what you give it; one level of nesting produces "Page not found" on a deploy it
reports as successful.

Either way: **set the apex as the primary domain in Netlify**, or the www
redirect has no target.
