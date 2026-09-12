# ai-at-work.au — project handover

**Status as at 11 September 2026, session 4.** Rebuilt as a maintainable
generator, with GTM, full schema coverage, a single enquiry form, an original
illustration system, a twelve-article blog and content on every page. 65 routes,
44,917 words. Verified. Still not live — see §3.

This supersedes the earlier 11 September handover. The positioning, brand,
taxonomy and per-vertical reasoning in that document all still stand and are not
repeated here; **keep it** for §§1–6 of the original (concept, positioning, tool
stance, brand, industry taxonomy, key insight per vertical). What follows is what
changed and what's outstanding.

**Deliverables**

| File | What it's for |
|---|---|
| `ai-at-work-DEPLOY-drop-this.zip` | Root is the site itself. Drag onto Netlify Drop, nothing to configure. |
| `ai-at-work-repo.zip` | Full source. `netlify.toml` at root, publish dir `site`, build `python3 build.py`. |
| `README.md` (in repo) | Commands, architecture, conventions, deploy paths. |
| `SITEMAP.md` (in repo) | Generated route inventory: words, sitemap status, page schema. |

---

## 1. What changed this session

### The source repo was reconstructed
Only the built HTML survived. It has been salvaged into a real generator: each
route's `<main>` lives in `content/pages/`, metadata and original JSON-LD in
`content/meta.json`, the stylesheet in `src/base.css`, the ported assessment
engine in `src/assessment.js`. Global changes are now one edit rather than 65.

**The data packs did not survive and were not recreated.** The seven industry
pages are salvaged HTML, not rendered from `industries/*.json`. That is the one
real regression against the original architecture: adding an eighth vertical is
currently writing a page, not writing a file. If more verticals are coming,
rebuilding the pack layer is the next structural job — the schema is documented
in §7 of the previous handover.

### One conversion action
The enquiry form at `/contact/` is the only form on the site, and `verify.py`
asserts exactly that. Netlify Forms, honeypot, posting to `/thank-you/`, which
pushes an `enquiry_submitted` event to `dataLayer`. Every other CTA on the site
links to it.

Each salvaged page carried its own green CTA band inside `<main>`; with the new
sitewide closing band that was two loud green surfaces and two competing
destinations per page. Those are demoted to plum prompts pointing at the form,
with the assessment kept as a plain secondary link.

`/newsletter/` is retired — it competed with the one CTA and had no mailing setup
behind it. It 301s to the blog.

### The assessment hands off instead of capturing
**This closes the launch blocker about the CRM endpoint — there is nothing left
to choose.** The email fields and `submit()` are gone. The plan now ends with a
handoff that writes a summary to `sessionStorage`; the contact page reads it and
prefills an editable field. No query string, so nothing about a business lands in
a URL or a log. `gating: 'free'` is retained in spirit: the full plan still shows
before anything is asked.

The engine is otherwise untouched — question set, packs, scoring, module
ordering and offer recommendation all behave as before. Our changes are applied
by `scripts/patch_assessment.py` rather than hand-edited, so they can be
re-applied if the engine is ever re-extracted.

### GTM, and the honesty problem it created
Container `GTM-5BL56Z44` is in the head and as a `<noscript>` iframe on all 65
routes. The CSP in both `netlify.toml` files is widened for googletagmanager and
google-analytics **and nothing else** — any other tag added inside the container
will be silently blocked until that list is widened deliberately.

`/privacy/` was rewritten, because the old page stated there were no third-party
scripts and that stopped being true the moment the container went on. It now
documents the analytics, the fonts, the form and the sessionStorage handoff. **If
the container gains anything with wider reach — an ad pixel, remarketing, a
session recorder — that page needs updating in the same deploy.**

This reverses the "no analytics, ad pixels or third-party scripts" convention
from the previous handover. That was a deliberate instruction, not an oversight.

### Schema on every route
Organization and WebSite sitewide, BreadcrumbList on all 64 non-home routes, plus
page-type schema: Service on the four engagements and seven industry pages,
Course on the six training modules, ContactPage, WebApplication on the
assessment, Blog, BlogPosting, ItemList, CollectionPage, and FAQPage on 30-odd
pages. `verify.py` parses every block and fails on a missing graph.

### Images, without a licensing problem
Two kinds, both original, both drawn from the brand tokens so a palette change
propagates:

- **Artwork** (`svg_*` in `src/illos.py`): a node-and-rule spine motif echoing
  the mark, a boundary field stopped by one green rule, a two-tools decision
  diagram, a layer stack, seven industry line marks, and deterministic
  geometric covers for blog cards — same slug, same artwork, always.
- **Diagrams** (`dg_*`): session clocks, before/after tables, the goes-in /
  never-goes-in split, step arcs, checklists. Built from real HTML rather than
  SVG, so text reflows, screen readers get structure, and nothing goes
  illegible at 390px the way SVG label text does.

No stock photography, no third-party assets, nothing to license, no extra HTTP
requests. **Slots for real photography of actual sessions remain the obvious
upgrade** — see §4.

### Content
18,101 → 44,917 words. Median page 628 words, up from roughly 300.

Depth was added as an expansion pass (`content/exp_*.py`) that appends inside
`<main>`, so the original copy keeps its place at the top and its voice. Every
service page now carries what happens in the room hour by hour, what changes
afterwards, who should and shouldn't be there, and where the engagement stops.
Training modules answer the same four questions each. Tools pages carry the
durable reasoning and deliberately no vendor terms.

### Blog
Twelve articles, 830–1,100 words each, across four categories with a hub,
category pages, related posts, FAQ schema and heavy internal linking into the
industry, training and service pages. `/insights/` is de-noindexed and in the
sitemap. Articles are markdown in `content/posts/` with a small front matter
block; `verify.py` checks every `related:` slug resolves.

Category split: privacy and policy 3, getting started 3, industry notes 4,
tools 2.

### Stylesheet moved out of the HTML
13.8KB of identical CSS was inlined into all 48 pages. It is now one
content-hashed file cached immutable, with a matching `/assets/*` cache header.
This breaks the previous "self-contained HTML per route" property, which was
worth trading at 65 routes.

---

## 2. Verification

```
python3 scripts/verify.py     # 65 routes: links, schema, GTM, metadata, form, blog
python3 scripts/e2e.py        # assessment → plan → handoff → prefilled form
python3 scripts/shots.py      # renders at 1280px and 390px
```

`verify.py` currently passes with one warning (the noindexed thank-you page's
description is short, which does not matter). It checks: zero broken internal
links; GTM in head and body; exactly one canonical, title, description and `h1`
per route; title and description lengths; every JSON-LD block parses and carries
the sitewide graph; alt text on every image; exactly one form sitewide with all
its Netlify attributes; no green CTA band inside `<main>`; sitemap membership
matching each page's robots directive; and blog integrity.

`e2e.py` drives headless Chromium through all nine questions and confirms the
plan renders, no email capture remains, the handoff lands on `/contact/`, the
summary arrives prefilled, every form field exists, and an empty submit is
blocked by validation.

**Run both before every deploy.** They are the only thing between a broken link
and production.

---

## 3. Blocking live launch

1. **Set the Netlify Forms notification address**, or submissions are stored and
   nobody is told. This replaces the old CRM-endpoint blocker.
2. **Set up `hello@ai-at-work.au`** — published on the contact page and in
   Organization schema.
3. **Register `aiatwork.au`** and point it here. Redirects already written.
4. **Set the primary domain in Netlify** to the apex, or the www redirect has no
   target.
5. **Confirm GTM is configured** at the container end, and that the
   `enquiry_submitted` event is wired to whatever counts as a conversion.
6. **Check the VERIFY items** in §10 of the previous handover for the verticals
   pushed first. Nothing in this session's writing asserts a CPD hour count, a
   price, a client name, a testimonial or a statistic — that constraint held
   throughout and should keep holding.
7. **Have the allied health privacy content reviewed** by someone qualified. The
   site now says out loud, in several places, that this review is necessary.
   Saying it and not doing it is worse than not saying it.

---

## 4. Still open

1. **The industry data pack layer**, per §1. The one architectural regression.
2. **Price band**, and whether to publish it. `/services/what-it-costs/` now
   argues our own position and then argues the counter-case honestly: a
   published range would filter better. Still unresolved.
3. **Which two verticals have real first-hand client evidence.** Asked four times
   across three sessions, never answered. `top_tasks` written from something
   actually witnessed beats anything inferred, and it should override the
   current priority ordering.
4. **Photography.** The illustration system is doing the work an original
   photograph would do better: a real room, real laptops, real documents on a
   table. Nothing needs to change structurally to drop it in.
5. **No named case studies.** `/case-studies/` now describes the honest shape of
   each engagement and lists the four questions to ask us instead. Anything
   named needs written consent.
6. **Delivery capacity** — how many engagements a month are actually
   deliverable. Never pinned, and the site now promises "a date, or an honest
   no", which needs a real answer behind it.
7. **The two-hour session plans**, unstarted. The question from the previous
   handover still stands: is the two-hour block a standalone offer, or the first
   module of the half day? The site currently describes it as the former, which
   is a decision made by writing rather than deliberately — worth confirming.
8. **Four categories, twelve articles.** Tools has two; the industry notes could
   carry one per published vertical. The engine makes each new article a
   markdown file.
