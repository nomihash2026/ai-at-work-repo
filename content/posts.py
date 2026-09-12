"""The blog.

Articles are authored as markdown in content/posts/*.md with a small front
matter block. This module parses them, renders the article pages, the hub at
/insights/ and a page per category, and emits Article schema.

Deliberately a tiny markdown subset rather than a dependency: the site has no
build requirements beyond python3 and that is worth keeping.
"""

import os
import re
from datetime import date

from data.site import SITE

ORIGIN = SITE["origin"]
HERE = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(HERE, "posts")

CATEGORIES = {
    "privacy-and-policy": (
        "Privacy & policy",
        "Where the line sits, how to write it down, and what to do about the "
        "staff member who has been pasting client documents into a free account "
        "for six months.",
    ),
    "getting-started": (
        "Getting started",
        "The first month with a team. What to teach first, what to leave alone "
        "until later, and how to tell three weeks afterwards whether any of it "
        "actually stuck.",
    ),
    "industry-notes": (
        "Industry notes",
        "The same skills, applied to the work that actually fills the week in "
        "accounting practices, clinics, firms, agencies and trade businesses.",
    ),
    "tools": (
        "Tools",
        "Claude and ChatGPT, side by side, with no reseller relationship in "
        "either direction — including the jobs where the answer is neither.",
    ),
}


# Guidance shown under each category listing, so a category page is worth
# indexing on its own rather than being a bare list of cards.
INTROS = {
    "privacy-and-policy": (
        '<div class="prose" style="margin-top:3rem"><h2>Where to start if nothing is '
        'written down</h2><p>Read the never list first and hand it to your team this '
        'week — it is the shortest path from exposed to bounded. Then establish which '
        'accounts are actually in use, because the account type matters more than the '
        'brand. Only then write the rule, since a policy built on a guess is one you '
        "can't enforce.</p><p>The free versions of all three are in the "
        '<a href="/guides/">guides</a>, and the engagement that does it for you is '
        '<a href="/services/policy-and-audit/">policy and audit</a>.</p></div>'),
    "getting-started": (
        '<div class="prose" style="margin-top:3rem"><h2>The short version</h2>'
        '<p>Where information goes, then one real job start to finish, then the tool '
        'decision, then the setups your team keeps. Prompt technique sits in the middle '
        'and is not the opener. Three weeks later, ask which job is being done '
        'differently and by whom — one named job is a successful session, and enthusiasm '
        'with no named job changed nothing.</p><p>The full curriculum is under '
        '<a href="/training/">training</a>.</p></div>'),
    "industry-notes": (
        '<div class="prose" style="margin-top:3rem"><h2>The pattern across industries</h2>'
        '<p>Roughly seventy percent of the work is identical wherever you look: drafting, '
        'summarising long documents, structuring messy information, client communication, '
        'reusable setups, and knowing when not to use it. What differs is which of those '
        'dominates the week, where the compliance line sits, and what the documents are '
        'called.</p><p>Seven industry tracks are published under '
        '<a href="/industries/">industries</a>, and an unpublished industry is not a '
        'barrier to an engagement.</p></div>'),
    "tools": (
        '<div class="prose" style="margin-top:3rem"><h2>The rule in four lines</h2>'
        '<p>Long and voice-sensitive work one way. Fast, high-volume work the other. '
        'Regulated judgement to neither. Check everything before it leaves the '
        'building.</p><p>No reseller agreement, partner status or referral fee with '
        'either vendor, and where a free tier is enough we say so. The detail is under '
        '<a href="/tools/">tools</a>.</p></div>'),
}


# ------------------------------------------------------------------ parsing --

def _unquote(v):
    """A value wrapped in double quotes is a quoted scalar: strip the wrapper
    and unescape the quotes inside it. Without this a title that contains a
    quotation mark renders its own backslashes on the page."""
    if len(v) > 1 and v[0] == '"' and v[-1] == '"':
        return v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return v


def _front_matter(raw):
    meta, body = {}, raw
    if raw.startswith("---"):
        end = raw.index("\n---", 3)
        block, body = raw[3:end], raw[end + 4:]
        for line in block.strip().splitlines():
            if not line.strip():
                continue
            k, _, v = line.partition(":")
            k, v = k.strip(), _unquote(v.strip())
            if k == "faq":
                q, _, a = v.partition("::")
                meta.setdefault("faq", []).append((q.strip(), a.strip()))
            elif k in ("related", "tags"):
                meta[k] = [x.strip() for x in v.split(",") if x.strip()]
            else:
                meta[k] = v
    return meta, body.strip()


def _inline(t):
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def _blocks(body, ask, illos):
    """Render the markdown subset. Blank-line separated blocks."""
    out = []
    for chunk in re.split(r"\n\s*\n", body):
        c = chunk.strip()
        if not c:
            continue
        if c.startswith(":::ask"):
            out.append(ask(_inline(c[6:].strip())))
        elif c.startswith(":::checklist"):
            parts = [p.strip() for p in c[12:].split("|")]
            out.append(illos.dg_checklist(_inline(parts[0]),
                                          [_inline(p) for p in parts[1:]]))
        elif c.startswith("<"):
            out.append(c)
        elif c.startswith("### "):
            out.append(f"<h3>{_inline(c[4:].strip())}</h3>")
        elif c.startswith("## "):
            out.append(f"<h2>{_inline(c[3:].strip())}</h2>")
        elif c.startswith("> "):
            text = " ".join(l[2:].strip() for l in c.splitlines())
            out.append(f"<blockquote><p>{_inline(text)}</p></blockquote>")
        elif re.match(r"^- ", c):
            items = "".join(f"<li>{_inline(l[2:].strip())}</li>"
                            for l in c.splitlines() if l.strip().startswith("- "))
            out.append(f"<ul>{items}</ul>")
        elif re.match(r"^\d+\. ", c):
            items = "".join(f"<li>{_inline(re.sub(r'^\d+\. ', '', l.strip()))}</li>"
                            for l in c.splitlines() if re.match(r"^\d+\. ", l.strip()))
            out.append(f"<ol>{items}</ol>")
        else:
            out.append(f"<p>{_inline(' '.join(l.strip() for l in c.splitlines()))}</p>")
    return "".join(out)


def load():
    posts = []
    if not os.path.isdir(POSTS_DIR):
        return posts
    for fn in sorted(os.listdir(POSTS_DIR)):
        if not fn.endswith(".md"):
            continue
        meta, body = _front_matter(open(os.path.join(POSTS_DIR, fn)).read())
        meta["body_md"] = body
        meta.setdefault("slug", fn[:-3])
        meta.setdefault("category", "getting-started")
        meta.setdefault("published", date.today().isoformat())
        meta["route"] = f"/insights/{meta['slug']}/"
        words = len(re.findall(r"[A-Za-z0-9'\-]+", re.sub(r"[#>*`\[\]()]", " ", body)))
        meta["words"] = words
        meta.setdefault("read", str(max(3, round(words / 220))))
        posts.append(meta)
    posts.sort(key=lambda p: p["published"], reverse=True)
    return posts


# ----------------------------------------------------------------- renderers --

def _meta_line(p):
    cat_name = CATEGORIES[p["category"]][0]
    bits = [f'<a href="/insights/category/{p["category"]}/">{cat_name}</a>',
            f'<span>{_human_date(p["published"])}</span>',
            f'<span>{p["read"]} minute read</span>']
    if p.get("updated") and p["updated"] != p["published"]:
        bits.append(f'<span>Updated {_human_date(p["updated"])}</span>')
    return f'<p class="post-meta">{"".join(bits)}</p>'


def _human_date(iso):
    y, m, d = iso.split("-")
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    return f"{int(d)} {months[int(m) - 1]} {y}"


def _card(p, illos):
    return (f'<a class="pcard" href="{p["route"]}">{illos.svg_post_cover(p["slug"])}'
            f'<span class="pcard-b"><span class="pcard-cat">'
            f'{CATEGORIES[p["category"]][0]}</span>'
            f'<h3>{p["title"]}</h3><p>{p.get("summary", p["description"])}</p>'
            f'<span class="pcard-m">{p["read"]} minute read</span></span></a>')


def _cat_chips(current=None):
    li = f'<li><a href="/insights/"{" aria-current=\"page\"" if current is None else ""}>Everything</a></li>'
    for slug, (name, _) in CATEGORIES.items():
        cur = ' aria-current="page"' if slug == current else ""
        li += f'<li><a href="/insights/category/{slug}/"{cur}>{name}</a></li>'
    return f'<ul class="cats">{li}</ul>'


def _faq_html(faq):
    if not faq:
        return ""
    items = "".join(
        f'<div class="qa-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in faq)
    return f'<section class="qa"><h2>Questions people ask about this</h2>{items}</section>'


def _related(p, posts, illos):
    picks = [q for q in posts if q["slug"] in p.get("related", [])]
    if not picks:
        picks = [q for q in posts
                 if q["category"] == p["category"] and q["slug"] != p["slug"]][:2]
    if not picks:
        return ""
    cards = "".join(_card(q, illos) for q in picks[:3])
    return (f'<section class="rel"><h2>Read next</h2>'
            f'<div class="plist">{cards}</div></section>')


def _article_schema(p):
    s = {
        "@type": "BlogPosting",
        "@id": f"{ORIGIN}{p['route']}#article",
        "headline": p["title"],
        "description": p["description"],
        "url": ORIGIN + p["route"],
        "datePublished": p["published"],
        "dateModified": p.get("updated", p["published"]),
        "inLanguage": SITE["locale"],
        "wordCount": p["words"],
        "articleSection": CATEGORIES[p["category"]][0],
        "author": {"@id": f"{ORIGIN}/#organization"},
        "publisher": {"@id": f"{ORIGIN}/#organization"},
        "image": ORIGIN + SITE["og_image"],
        "isPartOf": {"@type": "Blog", "@id": f"{ORIGIN}/insights/#blog"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": ORIGIN + p["route"]},
    }
    if p.get("tags"):
        s["keywords"] = ", ".join(p["tags"])
    return s


def _faq_schema(p):
    if not p.get("faq"):
        return None
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in p["faq"]
        ],
    }


def pages(ask, illos):
    posts = load()
    out = {}

    for p in posts:
        body = _blocks(p["body_md"], ask, illos)
        main = (
            '<main id="main"><section class="phero"><div class="shell">'
            '<p class="crumb"><a href="/">Home</a> / <a href="/insights/">Blog</a></p>'
            f'<h1>{p["title"]}</h1>'
            f'<p class="lede">{p.get("summary", p["description"])}</p>'
            f'{_meta_line(p)}</div></section>'
            '<section class="sect" style="padding-top:0"><div class="shell">'
            f'<div class="prose post-body">{body}</div>'
            f'{_faq_html(p.get("faq"))}'
            f'{_related(p, posts, illos)}'
            '</div></section></main>'
        )
        out[p["route"]] = {
            # meta_title keeps the search-result title short where the headline
            # on the page is long; falls back to the headline when absent.
            "title": f'{p.get("meta_title", p["title"])} — AI at work',
            "description": p["description"],
            "main": main,
            "og_type": "article",
            "published": p["published"],
            "updated": p.get("updated", p["published"]),
            "schema": [s for s in (_article_schema(p), _faq_schema(p)) if s],
            "cta": {
                "h": p.get("cta_h", "Tell us what's eating the week"),
                "p": p.get("cta_p", "Reading is free and always will be. When you want "
                                    "this applied to your own work, there's one form, "
                                    "and a person answers it."),
            },
        }

    # hub
    hub_cards = "".join(_card(p, illos) for p in posts)
    hub_main = (
        '<main id="main"><section class="phero"><div class="shell">'
        '<p class="crumb"><a href="/">Home</a></p>'
        '<h1>Blog</h1>'
        '<p class="lede">Written for the person who owns the P&amp;L and carries the '
        'risk, not for the curious employee. Everything here is the reasoning we would '
        'give you on a call, published rather than saved for one.</p>'
        f'{_cat_chips(None)}</div></section>'
        '<section class="sect" style="padding-top:0"><div class="shell">'
        f'<div class="plist">{hub_cards}</div></div></section></main>'
    )
    out["/insights/"] = {
        "title": "Blog — practical AI at work in Australian businesses — AI at work",
        "description": "Articles on using Claude and ChatGPT in real business work: "
                       "where the privacy line sits, what to teach a team first, which "
                       "tool suits which job, and what stays with a qualified person.",
        "main": hub_main,
        "schema": [
            {
                "@type": "Blog",
                "@id": f"{ORIGIN}/insights/#blog",
                "name": "AI at work — blog",
                "url": f"{ORIGIN}/insights/",
                "inLanguage": SITE["locale"],
                "publisher": {"@id": f"{ORIGIN}/#organization"},
                "blogPost": [{"@id": f"{ORIGIN}{p['route']}#article"} for p in posts],
            },
            {
                "@type": "ItemList",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "url": ORIGIN + p["route"],
                     "name": p["title"]} for i, p in enumerate(posts)
                ],
            },
        ],
    }

    # one page per category
    for slug, (name, blurb) in CATEGORIES.items():
        sel = [p for p in posts if p["category"] == slug]
        cards = "".join(_card(p, illos) for p in sel)
        intro = INTROS.get(slug, "")
        body = (f'<div class="plist">{cards}</div>{intro}' if sel else
                '<div class="prose"><p>Nothing published in this category yet. '
                '<a href="/insights/">Everything else is here.</a></p></div>')
        out[f"/insights/category/{slug}/"] = {
            "title": f"{name} — blog — AI at work",
            "description": blurb,
            "main": (
                '<main id="main"><section class="phero"><div class="shell">'
                '<p class="crumb"><a href="/">Home</a> / <a href="/insights/">Blog</a></p>'
                f'<h1>{name}</h1><p class="lede">{blurb}</p>{_cat_chips(slug)}'
                '</div></section>'
                '<section class="sect" style="padding-top:0"><div class="shell">'
                f'{body}</div></section></main>'
            ),
            "robots": "index,follow" if sel else "noindex,follow",
            "schema": [{
                "@type": "CollectionPage",
                "name": name,
                "url": f"{ORIGIN}/insights/category/{slug}/",
                "description": blurb,
                "isPartOf": {"@id": f"{ORIGIN}/insights/#blog"},
                "mainEntity": {
                    "@type": "ItemList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": i + 1,
                         "url": ORIGIN + p["route"], "name": p["title"]}
                        for i, p in enumerate(sel)
                    ],
                },
            }],
        }
    return out
