"""Post-build checks. Run after build.py; exits non-zero if anything is broken."""
import glob, json, os, re, sys

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")
files = sorted(glob.glob(f"{OUT}/**/index.html", recursive=True))
routes = {("/" + os.path.relpath(f, OUT)[:-len("index.html")]).replace("//", "/")
          for f in files}
routes = {r if r.endswith("/") else r + "/" for r in routes}
static = {os.path.relpath(p, OUT) for p in glob.glob(f"{OUT}/**/*", recursive=True)}
fails, warns = [], []

for f in files:
    h = open(f).read()
    route = ("/" + os.path.relpath(f, OUT)[:-len("index.html")]).replace("//", "/")

    # internal links
    for href in set(re.findall(r'href="(/[^"#?]*)"', h)):
        if href.lstrip("/") in static:
            continue
        if href.endswith("/") and href in routes:
            continue
        fails.append(f"{route}: broken link -> {href}")

    # GTM on every route, head and body
    if "GTM-5BL56Z44" not in h:
        fails.append(f"{route}: no GTM container")
    if "googletagmanager.com/ns.html" not in h:
        fails.append(f"{route}: no GTM noscript fallback")

    # one canonical, one title, one description, one h1
    for tag, pat in (("canonical", r'rel="canonical"'), ("title", r"<title>"),
                     ("description", r'name="description"')):
        if len(re.findall(pat, h)) != 1:
            fails.append(f"{route}: expected exactly one {tag}")
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    if len(h1s) != 1:
        fails.append(f"{route}: {len(h1s)} h1 tags")

    # title / description length sanity for search results
    title = re.search(r"<title>(.*?)</title>", h, re.S).group(1)
    desc = re.search(r'name="description" content="(.*?)"', h, re.S).group(1)
    if len(title) > 65:
        warns.append(f"{route}: title {len(title)} chars")
    if not (110 <= len(desc) <= 300):
        warns.append(f"{route}: description {len(desc)} chars")

    # schema parses and carries the sitewide graph
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    if not blocks:
        fails.append(f"{route}: no JSON-LD")
    for b in blocks:
        try:
            data = json.loads(b)
        except Exception as e:
            fails.append(f"{route}: JSON-LD does not parse ({e})")
            continue
        types = [n.get("@type") for n in data.get("@graph", [])]
        if "Organization" not in types or "WebSite" not in types:
            fails.append(f"{route}: graph missing Organization/WebSite, got {types}")
        if route != "/" and "BreadcrumbList" not in types:
            fails.append(f"{route}: no BreadcrumbList")

    # images carry alt text
    for img in re.findall(r"<img[^>]*>", h):
        if "alt=" not in img:
            fails.append(f"{route}: img without alt: {img[:60]}")
    # inline svg must be labelled or hidden
    for svg in re.findall(r"<svg[^>]*>", h):
        if "aria-hidden" not in svg and "role=" not in svg:
            warns.append(f"{route}: unlabelled svg: {svg[:60]}")

# the one form
contact = open(f"{OUT}/contact/index.html").read()
for needle, why in (('name="enquiry"', "form name"),
                    ('data-netlify="true"', "netlify forms attribute"),
                    ('action="/thank-you/"', "thank-you redirect"),
                    ('netlify-honeypot="bot-field"', "honeypot"),
                    ('name="form-name"', "hidden form-name field")):
    if needle not in contact:
        fails.append(f"/contact/: missing {why}")
forms = [f for f in files if "<form" in open(f).read()]
if len(forms) != 1:
    fails.append(f"expected exactly one form on the site, found {len(forms)}: {forms}")

# blog integrity: every related: slug resolves, and every category has posts
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.posts import load, CATEGORIES          # noqa: E402
posts = load()
slugs = {p["slug"] for p in posts}
for p in posts:
    for rel in p.get("related", []):
        if rel not in slugs:
            fails.append(f"/insights/{p['slug']}/: related slug does not exist -> {rel}")
    if p["category"] not in CATEGORIES:
        fails.append(f"/insights/{p['slug']}/: unknown category {p['category']}")
    for field in ("description", "summary", "meta_title"):
        if not p.get(field):
            warns.append(f"/insights/{p['slug']}/: no {field}")
for slug in CATEGORIES:
    if not [p for p in posts if p["category"] == slug]:
        warns.append(f"/insights/category/{slug}/: no posts, so noindexed")
print(f"{len(posts)} posts, {len(slugs)} slugs, categories "
      + ", ".join(f"{s}:{len([p for p in posts if p['category'] == s])}" for s in CATEGORIES))

# sitemap agrees with what's indexable
sm = open(f"{OUT}/sitemap.xml").read()
locs = {u.replace("https://ai-at-work.au", "") for u in re.findall(r"<loc>(.*?)</loc>", sm)}
for f in files:
    h = open(f).read()
    route = ("/" + os.path.relpath(f, OUT)[:-len("index.html")]).replace("//", "/")
    noindex = 'content="noindex' in h
    if noindex and route in locs:
        fails.append(f"{route}: noindex but in sitemap")
    if not noindex and route not in locs:
        fails.append(f"{route}: indexable but missing from sitemap")

print(f"{len(files)} routes checked, {len(locs)} in sitemap")
for w in warns:
    print("  warn:", w)
# ---------------------------------------------------------------- llms.txt ---
# The curated index is hand-written, so it is exactly the kind of file that
# rots. Every link in it has to resolve to a route that was actually built.
llms_path = os.path.join(OUT, "llms.txt")
if not os.path.isfile(llms_path):
    fails.append("llms.txt was not written")
else:
    llms = open(llms_path).read()
    linked = set(re.findall(r"\]\(https://ai-at-work\.au(/[^)]*)\)", llms))
    built = {"/" + os.path.relpath(os.path.dirname(f), OUT).strip(".").replace("\\", "/") + "/"
             for f in files}
    built = {r.replace("//", "/") for r in built}
    dead = sorted(r for r in linked if r not in built and not r.endswith(".xml"))
    if dead:
        fails.append(f"llms.txt links to routes that do not exist: {dead}")
    if "> Practical AI training" not in llms:
        fails.append("llms.txt is missing its summary block")
    print(f"llms.txt: {len(linked)} links, all resolving" if not dead
          else f"llms.txt: {len(dead)} dead links")

# ----------------------------------------------------------------- robots ----
robots_txt = open(os.path.join(OUT, "robots.txt")).read()
for agent in ("GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended"):
    if f"User-agent: {agent}" not in robots_txt:
        fails.append(f"robots.txt no longer names {agent}")
if "llms.txt" not in robots_txt:
    fails.append("robots.txt no longer points at llms.txt")

if fails:
    print(f"\n{len(fails)} FAILURES")
    for x in fails[:40]:
        print("  fail:", x)
    sys.exit(1)
print("all checks passed")
