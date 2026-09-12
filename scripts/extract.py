"""One-time salvage: pull CSS, per-route <main> content and metadata out of the
built site so the generator can be rebuilt around them."""
import re, glob, os, json, html

SRC = '/home/claude/work/ai-at-work-website'

h = open(f'{SRC}/about/index.html').read()
base = re.findall(r'<style>(.*?)</style>', h, re.S)[0]
open('src/base.css', 'w').write(base)

a = open(f'{SRC}/assessment/index.html').read()
ablocks = re.findall(r'<style>(.*?)</style>', a, re.S)
open('src/assessment.css', 'w').write(ablocks[1])
open('src/assessment.main.html', 'w').write(re.search(r'<main.*?</main>', a, re.S).group(0))

navscript = [s.strip() for s in re.findall(r'<script>(.*?)</script>', h, re.S)]
extra = [s for s in re.findall(r'<script[^>]*>(.*?)</script>', a, re.S) if s.strip() not in navscript]
open('src/assessment.js', 'w').write('\n/* ---- */\n'.join(extra))

meta = {}
for f in sorted(glob.glob('**/index.html', recursive=True, root_dir=SRC)):
    p = open(os.path.join(SRC, f)).read()
    route = '/' + f[:-len('index.html')]

    def g(pat):
        m = re.search(pat, p, re.S)
        return m.group(1) if m else None

    main = re.search(r'<main.*?</main>', p, re.S).group(0)
    ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', p, re.S)
    stripped = re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>', '', main, flags=re.S))
    meta[route] = {
        'title': html.unescape(g(r'<title>(.*?)</title>') or ''),
        'description': g(r'<meta name="description" content="(.*?)">'),
        'canonical': g(r'<link rel="canonical" href="(.*?)">'),
        'robots': g(r'<meta name="robots" content="(.*?)">'),
        'ld': [json.loads(x) for x in ld],
        'words': len(re.findall(r"[A-Za-z0-9'\-]+", stripped)),
    }
    slug = route.strip('/').replace('/', '__') or 'home'
    open(f'content/pages/{slug}.html', 'w').write(main)

json.dump(meta, open('content/meta.json', 'w'), indent=1)
print(f"{len(meta)} routes extracted | base.css {len(base)} chars | "
      f"assessment css {len(ablocks[1])} js {sum(len(s) for s in extra)}")
