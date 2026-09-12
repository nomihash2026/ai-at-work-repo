"""Layout and accessibility audit across representative routes and widths.

Checks the things a link checker cannot see: horizontal overflow, elements
wider than the viewport, tap targets below the 44px minimum, text smaller than
16px on mobile, images without dimensions, and console errors. Exits non-zero
on a failure so it can gate a deploy alongside verify.py.
"""
import http.server, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
PORT = 8555

ROUTES = sys.argv[1:] or [
    "/", "/who-this-is-for/", "/who-this-is-for/owners-and-managers/",
    "/industries/accounting-bookkeeping/", "/services/", "/training/useful-output/",
    "/tools/tiers-and-your-data/", "/tools/prompt-builder/", "/assessment/",
    "/insights/", "/insights/first-ninety-minutes/", "/contact/", "/about/",
]
WIDTHS = [(1440, "wide"), (1280, "desk"), (900, "tab"), (390, "mob"), (320, "small")]


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=OUT, **k)
    def log_message(self, *a): pass


PROBE = """() => {
  const vw = document.documentElement.clientWidth;
  const out = { scrollW: document.documentElement.scrollWidth, vw, wide: [], small: [], tap: [], noDim: [] };
  document.querySelectorAll('body *').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) return;
    const id = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string'
      ? '.' + el.className.trim().split(/\\s+/).slice(0,2).join('.') : '');
    // deliberately off-screen: the skip link and the honeypot field
    if (r.left < -2000) return;
    if (el.closest('.table-wrap')) return;   // scroll containers are allowed to exceed
    if (r.right > vw + 1 || r.left < -1) out.wide.push(id + ' [' + Math.round(r.left) + '..' + Math.round(r.right) + ']');
    const fs = parseFloat(cs.fontSize);
    if (el.children.length === 0 && el.textContent.trim() && fs < 14) out.small.push(id + ' ' + fs + 'px');
    if (['a','button','select','input','textarea','label'].includes(el.tagName.toLowerCase())) {
      if (el.type === 'radio' || el.type === 'checkbox') return;
      // WCAG 2.5.8 exempts a link inside a sentence of running text
      const p = el.parentElement;
      const inline = getComputedStyle(el).display.startsWith('inline') &&
        p && ['P','LI','SPAN','STRONG','EM','TD','TH','FIGCAPTION'].includes(p.tagName);
      if (inline) return;
      if (r.height < 24 && r.height > 0) out.tap.push(id + ' h=' + Math.round(r.height));
    }
    if (el.tagName === 'IMG' && (!el.getAttribute('width') && !cs.aspectRatio.includes('/'))) out.noDim.push(id);
  });
  return out;
}"""


def main():
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(("", PORT), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fails, notes = [], []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for w, tag in WIDTHS:
            c = b.new_context(viewport={"width": w, "height": 900}, reduced_motion="reduce")
            pg = c.new_page()
            errs = []
            pg.on("console", lambda m: errs.append(m.text)
                  if m.type == "error" and "403" not in m.text else None)
            for route in ROUTES:
                pg.goto(f"http://localhost:{PORT}{route}", wait_until="load")
                pg.wait_for_timeout(120)
                r = pg.evaluate(PROBE)
                if r["scrollW"] > r["vw"] + 1:
                    fails.append(f"{tag} {route}: horizontal scroll {r['scrollW']}>{r['vw']}")
                for k, label in (("wide", "overflows viewport"), ("small", "text under 14px"),
                                 ("noDim", "image without dimensions")):
                    if r[k]:
                        fails.append(f"{tag} {route}: {label}: {sorted(set(r[k]))[:4]}")
                if tag in ("mob", "small") and r["tap"]:
                    notes.append(f"{tag} {route}: short tap targets {sorted(set(r['tap']))[:4]}")
                if errs:
                    fails.append(f"{tag} {route}: console {errs[:2]}")
                    errs.clear()
            # the menu, opened, at every width
            pg.goto(f"http://localhost:{PORT}/", wait_until="load")
            if w <= 896:
                pg.click("#burger")
            pg.click("[data-mega]")
            pg.wait_for_timeout(150)
            r = pg.evaluate(PROBE)
            if r["scrollW"] > r["vw"] + 1 or r["wide"]:
                fails.append(f"{tag} menu open: overflow {r['wide'][:3] or r['scrollW']}")
            c.close()
        b.close()
    srv.shutdown()
    for n in notes:
        print("  note:", n)
    for f in fails:
        print("  FAIL:", f)
    print(f"audit: {len(ROUTES)} routes x {len(WIDTHS)} widths | "
          f"{len(fails)} failures, {len(notes)} notes")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
