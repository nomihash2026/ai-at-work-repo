#!/usr/bin/env python3
"""ai-at-work.au static site generator.

    python3 build.py            build every route into ./site
    python3 build.py --serve    build, then serve ./site on :8000

Conventions this file enforces, so no page can drift from them:
  * one stylesheet, content-hashed, cached immutable
  * GTM on every route, head and body
  * trailing slashes everywhere
  * Organization + WebSite + BreadcrumbList schema on every page, page-type
    schema on top
  * one conversion action sitewide: the enquiry form at /contact/
"""

import hashlib
import json
import os
import re
import shutil
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.site import SITE, INDUSTRIES, ENGAGEMENTS          # noqa: E402
from data import nav as NAV                                   # noqa: E402
from data.metas import METAS                                  # noqa: E402
from data.media import MEDIA                                  # noqa: E402
from src import illos                                         # noqa: E402
import content.posts as POSTS                                 # noqa: E402
import content.newpages as NEW                                # noqa: E402
import content.expansions as EXP                              # noqa: E402
import content.audience as AUD                                # noqa: E402
import content.figures as FIG                                 # noqa: E402
import content.llms as LLMS                                   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")
TODAY = date.today().isoformat()
ORIGIN = SITE["origin"]


# ------------------------------------------------------------------ assets ---

def build_css():
    css = (open(f"{ROOT}/src/base.css").read() + "\n" +
           open(f"{ROOT}/src/extra.css").read())
    digest = hashlib.sha256(css.encode()).hexdigest()[:10]
    path = f"assets/site.{digest}.css"
    os.makedirs(f"{OUT}/assets", exist_ok=True)
    open(f"{OUT}/{path}", "w").write(css)
    return "/" + path


def build_tool_assets(name):
    """Per-tool stylesheet and script, content-hashed like the main sheet.
    Neither tool posts anywhere: both hand off to the enquiry form instead."""
    css = open(f"{ROOT}/src/{name}.css").read()
    js = open(f"{ROOT}/src/{name}.js").read()
    d = hashlib.sha256((css + js).encode()).hexdigest()[:10]
    open(f"{OUT}/assets/{name}.{d}.css", "w").write(css)
    open(f"{OUT}/assets/{name}.{d}.js", "w").write(js)
    return f"/assets/{name}.{d}.css", f"/assets/{name}.{d}.js"


# -------------------------------------------------------------------- html ---

def gtm_head():
    return (
        "<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':"
        "new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
        "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src="
        "'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
        f"}})(window,document,'script','dataLayer','{SITE['gtm']}');</script>"
    )


def gtm_body():
    return (
        f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={SITE["gtm"]}"'
        ' height="0" width="0" style="display:none;visibility:hidden"'
        ' title="Google Tag Manager"></iframe></noscript>'
    )


ALL_TITLES = {}   # route -> short label, filled once the registry is built


def parent_of(route):
    """Explicit parent if one is declared, otherwise the route one segment up
    when that route exists. Blog posts and category pages resolve this way."""
    if route in NAV.PARENTS:
        return NAV.PARENTS[route]
    segs = [s for s in route.strip("/").split("/") if s]
    for cut in range(len(segs) - 1, 0, -1):
        cand = "/" + "/".join(segs[:cut]) + "/"
        if cand in ALL_TITLES or cand in LEGACY:
            return cand
    return "/"


def crumbs_for(route):
    """Walk parents up to home. Returns [(route, label), ...] root first."""
    chain, cur, guard = [], route, 0
    while cur and cur != "/" and guard < 8:
        guard += 1
        label = (NAV.CRUMB_LABELS.get(cur) or ALL_TITLES.get(cur)
                 or PAGE_TITLES.get(cur) or cur.strip("/").split("/")[-1].replace("-", " ").capitalize())
        chain.append((cur, label))
        cur = parent_of(cur)
    chain.append(("/", "Home"))
    return list(reversed(chain))


def org_schema():
    return {
        "@type": "Organization",
        "@id": f"{ORIGIN}/#organization",
        "name": SITE["name"],
        "url": ORIGIN + "/",
        "email": SITE["email"],
        "logo": {"@type": "ImageObject", "url": ORIGIN + "/brand/logo-lockup.png"},
        "image": ORIGIN + SITE["og_image"],
        "description": SITE["tagline"],
        "areaServed": {"@type": "Country", "name": "Australia"},
        "address": {"@type": "PostalAddress", "addressLocality": SITE["city"],
                    "addressRegion": SITE["region"], "addressCountry": SITE["country"]},
        "knowsAbout": ["AI training", "Claude", "ChatGPT", "AI policy",
                       "privacy and data handling", "workflow automation"],
        "contactPoint": {"@type": "ContactPoint", "contactType": "sales",
                         "email": SITE["email"], "areaServed": "AU",
                         "availableLanguage": "en"},
    }


def website_schema():
    return {
        "@type": "WebSite",
        "@id": f"{ORIGIN}/#website",
        "url": ORIGIN + "/",
        "name": SITE["name"],
        "inLanguage": SITE["locale"],
        "publisher": {"@id": f"{ORIGIN}/#organization"},
    }


def breadcrumb_schema(route):
    chain = crumbs_for(route)
    if len(chain) < 2:
        return None
    return {
        "@type": "BreadcrumbList",
        "@id": f"{ORIGIN}{route}#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": re.sub("&amp;", "&", label),
             "item": ORIGIN + r} for i, (r, label) in enumerate(chain)
        ],
    }


def webpage_schema(route, page):
    """One WebPage node per route, tying the page to the site and the
    organisation. Without it a crawler sees a title, a description and a
    disconnected page-type node; with it every route is an addressable entity
    that the Organization and WebSite nodes reach."""
    node = {
        "@type": "WebPage",
        "@id": f"{ORIGIN}{route}#webpage",
        "url": ORIGIN + route,
        "name": page["title"],
        "description": page["description"],
        "inLanguage": SITE["locale"],
        "isPartOf": {"@id": f"{ORIGIN}/#website"},
        "about": {"@id": f"{ORIGIN}/#organization"},
        "publisher": {"@id": f"{ORIGIN}/#organization"},
    }
    if route != "/":
        node["breadcrumb"] = {"@id": f"{ORIGIN}{route}#breadcrumb"}
    for key in ("published", "updated"):
        if page.get(key):
            node["datePublished" if key == "published" else "dateModified"] = page[key]
    return node


def ld_block(graph):
    graph = [g for g in graph if g]
    payload = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">'
            + json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
            + "</script>")


def head(page, route, css_href, extra_css=None):
    title = page["title"]
    desc = page["description"]
    canonical = ORIGIN + route
    robots = page.get("robots", "index,follow")
    og_image = ORIGIN + page.get("og_image", SITE["og_image"])
    og_type = page.get("og_type", "website")
    graph = [org_schema(), website_schema(), breadcrumb_schema(route),
             webpage_schema(route, page)]
    graph += page.get("schema", [])
    extra = f'<link rel="stylesheet" href="{extra_css}">' if extra_css else ""
    art = ""
    if og_type == "article":
        art = (f'<meta property="article:published_time" content="{page["published"]}">'
               f'<meta property="article:modified_time" content="{page.get("updated", page["published"])}">')
    return (
        '<!doctype html><html lang="en-AU"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"{gtm_head()}"
        f"<title>{title}</title>"
        f'<meta name="description" content="{desc}">'
        f'<link rel="canonical" href="{canonical}">'
        f'<meta name="robots" content="{robots}">'
        f'<meta property="og:type" content="{og_type}">'
        f'<meta property="og:site_name" content="{SITE["name"]}">'
        f'<meta property="og:title" content="{title}">'
        f'<meta property="og:description" content="{desc}">'
        f'<meta property="og:url" content="{canonical}">'
        f'<meta property="og:image" content="{og_image}">'
        f'<meta property="og:locale" content="en_AU">'
        f"{art}"
        '<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{title}">'
        f'<meta name="twitter:description" content="{desc}">'
        '<link rel="icon" href="/brand/favicon-32.png" sizes="32x32">'
        '<link rel="apple-touch-icon" href="/brand/favicon-180.png">'
        '<meta name="theme-color" content="#2A0033">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Newsreader:'
        'ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet">'
        f'<link rel="stylesheet" href="{css_href}">{extra}'
        f"{ld_block(graph)}"
        "</head>"
    )


def wordmark(tag="a", href="/"):
    inner = '<span class="wm"><b>AI</b><i>at work</i></span>'
    if tag == "a":
        return f'<a class="wordmark" href="{href}" aria-label="AI at work — home">{inner}</a>'
    return f'<span class="wordmark">{inner}</span>'


def header_html(route):
    items = ""
    for m in NAV.MEGA:
        cols = ""
        for gname, links in m["groups"]:
            lis = ""
            for href, label in links:
                if href:
                    lis += f'<li><a href="{href}">{label}</a></li>'
                else:
                    lis += f'<li><span class="soon">{label} — in development</span></li>'
            cols += f'<div class="mega-group"><h4>{gname}</h4><ul>{lis}</ul></div>'
        items += (
            f'<div class="nav-item"><button class="nav-btn" aria-expanded="false" '
            f'aria-controls="mega-{m["id"]}" data-mega>{m["label"]} '
            f'<i class="chev" aria-hidden="true"></i></button>'
            f'<div class="mega" id="mega-{m["id"]}" data-open="false">'
            f'<div class="shell mega-in"><div class="mega-lead"><h3>{m["lead_h"]}</h3>'
            f'<p>{m["lead_p"]}</p><a href="{m["lead_href"]}">{m["lead_cta"]}</a></div>'
            f'<div class="mega-cols">{cols}</div></div></div></div>'
        )
    # Every item in the bar opens a panel, and there is exactly one action.
    # "Build your plan" used to sit here as a bare link between five category
    # labels and the enquiry CTA, which made it read as a second, competing
    # call to action — the one thing the style budget rules out. It now leads
    # the "Free, no account" group in two panels, and still appears in the
    # home hero and the footer.
    return (
        '<header class="bar" id="bar" data-mobile="false"><div class="shell bar-in">'
        f'{wordmark()}'
        '<button class="burger" id="burger" aria-expanded="false" aria-controls="nav">Menu</button>'
        f'<nav class="nav" id="nav" aria-label="Main">{items}</nav>'
        f'<a class="bar-cta" href="{SITE["cta"]["href"]}">'
        f'<span class="cta-long">{SITE["cta"]["label"]}</span>'
        f'<span class="cta-short">{SITE["cta"]["short"]}</span></a>'
        "</div></header>"
    )


def footer_html():
    cols = ""
    for name, links in NAV.FOOTER:
        lis = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in links)
        cols += f"<div><h4>{name}</h4><ul>{lis}</ul></div>"
    return (
        '<footer class="foot"><div class="shell"><div class="foot-top"><div>'
        f'{wordmark("span")}<p>{SITE["tagline"]}</p></div>'
        f'<div class="foot-grid">{cols}</div></div>'
        f'<div class="foot-base"><span>&copy; 2026 {SITE["name"]}. {SITE["city"]}, Australia.</span>'
        f'<span>Managed and maintained by <a href="{SITE["maintainer"]["url"]}" rel="noopener">'
        f'{SITE["maintainer"]["name"]}</a>.</span></div></div></footer>'
    )


NAV_JS = """
(function(){
  var bar = document.getElementById('bar');
  var btns = [].slice.call(document.querySelectorAll('[data-mega]'));
  function closeAll(except){
    btns.forEach(function(b){
      if (b === except) return;
      b.setAttribute('aria-expanded','false');
      document.getElementById(b.getAttribute('aria-controls')).setAttribute('data-open','false');
    });
  }
  btns.forEach(function(b){
    b.addEventListener('click', function(){
      var open = b.getAttribute('aria-expanded') === 'true';
      closeAll(b);
      b.setAttribute('aria-expanded', open ? 'false' : 'true');
      document.getElementById(b.getAttribute('aria-controls')).setAttribute('data-open', open ? 'false' : 'true');
    });
  });
  document.addEventListener('click', function(e){
    if (!e.target.closest('.nav-item')) closeAll(null);
  });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') closeAll(null);
  });
  var burger = document.getElementById('burger');
  if (burger) burger.addEventListener('click', function(){
    var open = bar.getAttribute('data-mobile') === 'true';
    bar.setAttribute('data-mobile', open ? 'false' : 'true');
    burger.setAttribute('aria-expanded', open ? 'false' : 'true');
    burger.textContent = open ? 'Menu' : 'Close';
  });

  /* One motion rule: a 600ms 24px fade-up, once, on each top-level section. */
  var fadables = [].slice.call(document.querySelectorAll('main > section, .foot'));
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
    fadables.forEach(function(el){ el.setAttribute('data-fade',''); });
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.02 });
    fadables.forEach(function(el){ io.observe(el); });
  }
})();
"""


def cta_band(page):
    """The closing band. Green, one loud surface, always the same destination."""
    c = page.get("cta", {})
    h = c.get("h", "Tell us what's eating the week")
    p = c.get("p", "One form, one reply from a person. We'll tell you which engagement "
                   "fits, roughly what it costs, and if we're the wrong fit we'll say so.")
    label = c.get("label", "Start an enquiry")
    return ('<section class="cta"><div class="shell cta-in">'
            f"<h2>{h}</h2><p>{p}</p>"
            f'<a class="btn-primary" href="{SITE["cta"]["href"]}">{label}</a>'
            "</div></section>")


def render(route, page, css_href, extra_css=None, body_js=None):
    body_scripts = f"<script>{NAV_JS}</script>"
    if page.get("inline_js"):
        body_scripts += f'<script>{page["inline_js"]}</script>'
    if body_js:
        body_scripts += f'<script src="{body_js}" defer></script>'
    html = (
        head(page, route, css_href, extra_css)
        + '<body>' + gtm_body()
        + '<a class="skip" href="#main">Skip to content</a>'
        + header_html(route)
        + page["main"]
        + ("" if page.get("no_cta") else cta_band(page))
        + footer_html()
        + body_scripts
        + "</body></html>"
    )
    d = os.path.join(OUT, route.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(html)
    return html


# ----------------------------------------------------------------- content ---

LEGACY = json.load(open(f"{ROOT}/content/meta.json"))
PAGE_TITLES = {r: m["title"].split(" — ")[0] for r, m in LEGACY.items()}


def legacy_main(route):
    slug = route.strip("/").replace("/", "__") or "home"
    return open(f"{ROOT}/content/pages/{slug}.html").read()


LEGACY_CTA = re.compile(
    r'<section class="cta"><div class="shell cta-in"><h2>(.*?)</h2><p>(.*?)</p>'
    r'<a class="btn-primary" href="(.*?)">(.*?)</a></div></section>', re.S)


def sanitise(main):
    """Two retirements.

    The newsletter route is gone, so links to it become plain text.

    Every salvaged page carried its own green CTA band inside <main>, which now
    collides with the sitewide closing band: two loud green surfaces per page,
    and two competing destinations. The copy is worth keeping, so the band is
    demoted to a plum prompt pointing at the enquiry form, with the assessment
    kept as a plain secondary link rather than a second button. Returns the
    cleaned main plus that prompt, which the caller appends last."""
    main = re.sub(r'<a href="/newsletter/">([^<]*)</a>', r"\1", main)
    tail = ""
    m = LEGACY_CTA.search(main)
    if m:
        heading, body, href, label = m.groups()
        text = f"<strong>{heading}.</strong> {body}"
        if href and href != SITE["cta"]["href"]:
            text += f' <a href="{href}">{label}</a>.'
        tail = ('<section class="sect" style="padding-bottom:0"><div class="shell">'
                f'<div class="ask"><p>{text}</p>'
                f'<a href="{SITE["cta"]["href"]}">{SITE["cta"]["label"]}</a>'
                '</div></div></section>')
        main = main.replace(m.group(0), "")
    return main, tail



# -------------------------------------------------------------------- media --

PHOTO_DIR = os.path.join(ROOT, "static", "photo")
MISSING_MEDIA = []


def media_html(route):
    """The one image slot. Returns nothing when the file has not been supplied
    yet, so an unphotographed route builds clean rather than showing a box."""
    spec = MEDIA.get(route)
    if not spec:
        return ""
    src = os.path.join(PHOTO_DIR, spec["file"])
    if not os.path.isfile(src):
        MISSING_MEDIA.append((route, spec["file"]))
        return ""
    cap = spec.get("caption")
    cap = f"<figcaption><span>{cap}</span></figcaption>" if cap else ""
    kind = spec.get("kind", "photo")
    ratio = spec.get("ratio", "wide")
    return (
        f'<section class="media" data-kind="{kind}" data-ratio="{ratio}">'
        f'<figure class="ph"><img src="/photo/{spec["file"]}" alt="{spec["alt"]}"'
        ' loading="lazy" decoding="async">'
        f'{cap}</figure></section>'
    )


def inject_media(main, route):
    """One slot, every page: directly after the hero, before the first body
    section. Held for every route, because alternating placement reads as
    indecision rather than rhythm."""
    block = media_html(route)
    if not block:
        return main
    i = main.find("</section>")
    if i == -1:
        return main.replace("</main>", block + "</main>", 1)
    i += len("</section>")
    return main[:i] + block + main[i:]


def crumb_html(route):
    chain = crumbs_for(route)[:-1]
    if not chain:
        return ""
    parts = " / ".join(f'<a href="{r}">{l}</a>' for r, l in chain)
    return f'<p class="crumb">{parts}</p>'


def inject_crumb(main, route):
    """Legacy pages carry a hand-written crumb on some routes only. Normalise."""
    if 'class="crumb"' in main or route == "/":
        return main
    ch = crumb_html(route)
    if not ch:
        return main
    return main.replace('<section class="phero"><div class="shell">',
                        f'<section class="phero"><div class="shell">{ch}', 1)


def ask(text, label="Start an enquiry"):
    return (f'<div class="ask"><p>{text}</p>'
            f'<a href="{SITE["cta"]["href"]}">{label}</a></div>')


# ------------------------------------------------------------- page registry --

def course_schema(name, desc, route):
    return {
        "@type": "Course",
        "name": name,
        "description": desc,
        "url": ORIGIN + route,
        "provider": {"@id": f"{ORIGIN}/#organization"},
        "inLanguage": SITE["locale"],
        "teaches": name,
        "isAccessibleForFree": False,
        "hasCourseInstance": {
            "@type": "CourseInstance",
            "courseMode": ["Onsite", "Online"],
            "courseWorkload": "PT2H",
            "location": {"@type": "Country", "name": "Australia"},
        },
    }


def service_schema(name, desc, route):
    return {
        "@type": "Service",
        "name": name,
        "description": desc,
        "url": ORIGIN + route,
        "serviceType": name,
        "provider": {"@id": f"{ORIGIN}/#organization"},
        "areaServed": {"@type": "Country", "name": "Australia"},
        "audience": {"@type": "BusinessAudience", "name": "Australian small and mid-sized businesses"},
    }


SERVICE_META = {
    "/services/team-workshop/": "Team workshop",
    "/services/workflow-build/": "Done-with-you workflow build",
    "/services/policy-and-audit/": "AI policy and audit",
    "/services/advisory/": "Ongoing AI advisory",
}
COURSE_META = {
    "/training/useful-output/": "Getting output you can actually use",
    "/training/choosing-your-tool/": "Choosing your tool for the job",
    "/training/long-documents/": "Working with long documents",
    "/training/reusable-setups/": "Building reusable setups",
    "/training/what-never-goes-in/": "What never goes in an AI tool",
    "/training/team-ai-policy/": "Writing your team's AI policy",
}


# Hub routes and what they list. An ItemList tells a crawler that a hub is an
# index of these specific pages rather than a page that happens to contain
# links, which is the difference between the children being understood as a set
# and being crawled as unrelated URLs.
HUBS = {
    "/industries/": [f"/industries/{s}/" for s, _ in INDUSTRIES],
    "/services/": [f"/services/{s}/" for s, _ in ENGAGEMENTS] + ["/services/what-it-costs/"],
    "/training/": list(COURSE_META),
    "/who-this-is-for/": [
        "/who-this-is-for/worried-about-your-job/",
        "/who-this-is-for/never-used-it/",
        "/who-this-is-for/teaching-yourself/",
        "/who-this-is-for/owners-and-managers/",
    ],
    "/guides/": ["/guides/getting-your-team-started/", "/guides/privacy-basics/",
                 "/guides/what-never-goes-in/"],
    "/resources/": ["/resources/ai-policy-templates/", "/resources/prompt-library/",
                    "/resources/vendor-checklist/"],
}


def itemlist_schema(route, children, pages):
    return {
        "@type": "ItemList",
        "@id": f"{ORIGIN}{route}#list",
        "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "numberOfItems": len(children),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "url": ORIGIN + c,
             "name": pages[c]["title"].split(" — ")[0]}
            for i, c in enumerate(children) if c in pages
        ],
    }


def build_pages():
    """Assemble the page registry: salvaged routes, overridden metadata,
    rewritten pages, and everything new."""
    pages = {}
    for route, m in LEGACY.items():
        if route == "/newsletter/":
            continue                      # retired: competed with the one CTA
        main, ask_tail = sanitise(legacy_main(route))
        main = inject_crumb(main, route)
        pages[route] = {
            "ask_tail": ask_tail,
            "title": m["title"],
            "description": m["description"],
            "robots": m["robots"] or "index,follow",
            "schema": list(m["ld"]),
            "main": main,
        }

    # page-type schema on top of the salvaged graph
    for route, name in SERVICE_META.items():
        pages[route]["schema"].append(
            service_schema(name, pages[route]["description"], route))
    for route, name in COURSE_META.items():
        pages[route]["schema"].append(
            course_schema(name, pages[route]["description"], route))
    for slug, name in INDUSTRIES:
        r = f"/industries/{slug}/"
        pages[r]["schema"].append(service_schema(
            f"AI training for {name}", pages[r]["description"], r))

    # depth added to salvaged pages: engagement modules, figures and FAQs,
    # appended inside <main> so the original copy keeps its place at the top
    EXP.expand(pages, ask, illos)

    # rewritten and new pages
    pages.update(NEW.pages(ask, illos))

    # the audience section: organised by who is in the room rather than by
    # what the business does
    pages.update(AUD.pages(ask, illos))

    # blog
    pages.update(POSTS.pages(ask, illos))

    # metadata overrides, applied last so they win over anything — salvaged,
    # rewritten or generated. The blog used to be registered after this and so
    # could not be overridden at all.
    for route, over in METAS.items():
        if route in pages:
            pages[route].update(over)

    # hub pages declare what they index
    for route, children in HUBS.items():
        if route in pages:
            pages[route].setdefault("schema", []).append(
                itemlist_schema(route, children, pages))

    # the five diagrams that replaced the retired screenshot slots
    FIG.apply(pages, illos)

    # the one image slot, applied to every route that has an entry
    for route, page in pages.items():
        page["main"] = inject_media(page["main"], route)

    # the demoted legacy prompt goes last, after any expansion sections
    for page in pages.values():
        tail = page.pop("ask_tail", "")
        if tail:
            page["main"] = page["main"].replace("</main>", tail + "</main>", 1)
    return pages


# ----------------------------------------------------------------- sitemap ---

PRIORITY = {"/": "1.0", "/contact/": "0.9", "/industries/": "0.9", "/services/": "0.8",
            "/training/": "0.8", "/tools/": "0.8", "/insights/": "0.8", "/assessment/": "0.9",
            "/who-this-is-for/": "0.9"}


def sitemap(pages):
    urls = []
    for route in sorted(pages):
        p = pages[route]
        if "noindex" in (p.get("robots") or ""):
            continue
        pr = PRIORITY.get(route)
        if pr is None:
            pr = "0.7" if route.startswith(("/industries/", "/services/", "/insights/")) else "0.6"
        # lastmod only where a real date exists. Stamping every URL with the
        # build date tells a crawler the whole site changed on every deploy,
        # which is both untrue and quickly ignored.
        lastmod = p.get("updated") or p.get("published")
        lm = f"<lastmod>{lastmod}</lastmod>" if lastmod else ""
        urls.append(f"<url><loc>{ORIGIN}{route}</loc>{lm}"
                    f"<priority>{pr}</priority></url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           + "".join(urls) + "</urlset>")
    open(f"{OUT}/sitemap.xml", "w").write(xml)
    return len(urls)


def routes_md(pages):
    """A human-readable route inventory. Generated, so it cannot drift."""
    rows = []
    for route in sorted(pages):
        p = pages[route]
        text = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", "", p["main"], flags=re.S))
        words = len(re.findall(r"[A-Za-z0-9'\-]+", text))
        types = [n.get("@type") for n in p.get("schema", [])]
        idx = "no" if "noindex" in (p.get("robots") or "") else "yes"
        rows.append(f"| `{route}` | {words} | {idx} | {', '.join(types) or '—'} |")
    body = "\n".join(rows)
    open(f"{ROOT}/SITEMAP.md", "w").write(
        f"# Routes\n\nGenerated by `build.py` on {TODAY}. "
        f"{len(pages)} routes.\n\nPage-type schema is listed; every route also "
        f"carries Organization, WebSite and (except home) BreadcrumbList.\n\n"
        f"| Route | Words | In sitemap | Page schema |\n|---|---|---|---|\n{body}\n")


# Crawlers named explicitly rather than left to the wildcard. Being findable
# inside an answer engine is the point of publishing the guides and the blog, so
# the permission is stated rather than inferred — several of these read a named
# block and ignore the wildcard, and a few operators check for one before
# treating a site as opted in.
AI_AGENTS = [
    ("GPTBot", "OpenAI, model training and ChatGPT browsing"),
    ("OAI-SearchBot", "OpenAI, search index"),
    ("ChatGPT-User", "OpenAI, fetching a page a user asked about"),
    ("ClaudeBot", "Anthropic"),
    ("Claude-User", "Anthropic, fetching a page a user asked about"),
    ("Claude-SearchBot", "Anthropic, search index"),
    ("PerplexityBot", "Perplexity"),
    ("Perplexity-User", "Perplexity, fetching a page a user asked about"),
    ("Google-Extended", "Google, Gemini and AI Overviews grounding"),
    ("Applebot-Extended", "Apple Intelligence"),
    ("Bingbot", "Microsoft, which also feeds Copilot"),
    ("CCBot", "Common Crawl, which many models are trained from"),
    ("Meta-ExternalAgent", "Meta"),
    ("Amazonbot", "Amazon"),
    ("cohere-ai", "Cohere"),
]


def robots():
    lines = ["User-agent: *", "Allow: /", ""]
    lines.append("# Answer engines are welcome; the guides and the blog are the")
    lines.append("# point. Nothing here is gated, so there is nothing to protect")
    lines.append("# by keeping a crawler out.")
    lines.append("")
    for agent, who in AI_AGENTS:
        lines.append(f"# {who}")
        lines.append(f"User-agent: {agent}")
        lines.append("Allow: /")
        lines.append("")
    lines.append("# A curated index written for language models, in the llms.txt")
    lines.append("# convention. Shorter than the sitemap and ordered by what is")
    lines.append("# worth reading rather than by path.")
    lines.append(f"# {ORIGIN}/llms.txt")
    lines.append("")
    lines.append(f"Sitemap: {ORIGIN}/sitemap.xml")
    open(f"{OUT}/robots.txt", "w").write("\n".join(lines) + "\n")


# -------------------------------------------------------------------- main ---

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    shutil.copytree(f"{ROOT}/static/brand", f"{OUT}/brand")
    if os.path.isdir(f"{ROOT}/static/photo"):
        os.makedirs(f"{OUT}/photo", exist_ok=True)
        for f in os.listdir(f"{ROOT}/static/photo"):
            if not f.startswith(".") and f != "README.md":
                shutil.copy(f"{ROOT}/static/photo/{f}", f"{OUT}/photo/{f}")
    for f in ("_redirects", "netlify.toml"):
        shutil.copy(f"{ROOT}/static/{f}", f"{OUT}/{f}")

    css_href = build_css()
    TOOL_ASSETS = {
        "/assessment/": build_tool_assets("assessment"),
        "/tools/prompt-builder/": build_tool_assets("prompt"),
    }

    pages = build_pages()
    ALL_TITLES.update({r: (NAV.CRUMB_LABELS.get(r) or p["title"].split(" — ")[0])
                       for r, p in pages.items()})
    words = 0
    for route, page in sorted(pages.items()):
        t_css, t_js = TOOL_ASSETS.get(route, (None, None))
        render(route, page, css_href, extra_css=t_css, body_js=t_js)
        text = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", "", page["main"], flags=re.S))
        words += len(re.findall(r"[A-Za-z0-9'\-]+", text))

    n = sitemap(pages)
    robots()
    listed = LLMS.build(pages, OUT)
    routes_md(pages)
    print(f"built {len(pages)} routes | {n} in sitemap | {listed} in llms.txt "
          f"| {words:,} words of main content")
    print(f"stylesheet {css_href}")
    if MISSING_MEDIA:
        print(f"images outstanding ({len(MISSING_MEDIA)}) — these routes build "
              f"without an image until the file lands in static/photo/:")
        for route, f in sorted(set(MISSING_MEDIA)):
            print(f"  {route:<42} {f}")

    if "--serve" in sys.argv:
        os.chdir(OUT)
        import http.server, socketserver
        with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as s:
            print("serving ./site on http://localhost:8000")
            s.serve_forever()


if __name__ == "__main__":
    main()
