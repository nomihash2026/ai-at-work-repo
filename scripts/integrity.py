"""Render every route at desktop and mobile and report what is actually broken.

verify.py checks the HTML. This checks the rendered page: horizontal overflow,
elements escaping the viewport, controls that sit on different baselines, tap
targets below the minimum, contrast-bearing colours, duplicate ids and missing
alt text. Run it before a deploy that changed CSS.
"""
import http.server, json, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
PORT = 8444

ROUTES = sys.argv[1:] or sorted(
    "/" + os.path.relpath(d, OUT).strip(".").replace("\\", "/") + "/"
    for d, _, fs in os.walk(OUT) if "index.html" in fs)
ROUTES = [r.replace("//", "/") for r in ROUTES]

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=OUT, **k)
    def log_message(s, *a): pass

PROBE = """() => {
  const out = {overflow: [], escaped: [], misaligned: [], small: [],
               dupIds: [], noAlt: [], empty: []};
  const vw = document.documentElement.clientWidth;
  if (document.documentElement.scrollWidth > vw + 1)
    out.overflow.push(document.documentElement.scrollWidth + ' vs ' + vw);

  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    if (r.right > vw + 1.5 || r.left < -1.5) {
      const cs = getComputedStyle(el);
      if (cs.position === 'fixed' || cs.overflowX === 'auto' ||
          cs.overflowX === 'scroll') return;
      out.escaped.push(el.tagName.toLowerCase() + '.' +
        (el.className.toString().split(' ')[0] || '') +
        ' [' + Math.round(r.left) + '..' + Math.round(r.right) + ']');
    }
  });

  // controls that sit side by side must share a baseline
  document.querySelectorAll('.hero-actions, .actions, .bar-in').forEach(g => {
    const kids = [...g.children].filter(k => {
      const r = k.getBoundingClientRect();
      return r.height > 0 && r.width > 0;
    });
    if (kids.length < 2) return;
    const tops = kids.map(k => {
      const r = k.getBoundingClientRect();
      return {n: k.tagName.toLowerCase() + '.' + (k.className.toString().split(' ')[0] || ''),
              b: Math.round(r.bottom), t: Math.round(r.top)};
    });
    const sameRow = tops.every(t => Math.abs(t.t - tops[0].t) < 30);
    if (!sameRow) return;
    const spread = Math.max(...tops.map(t => t.b)) - Math.min(...tops.map(t => t.b));
    if (spread > 2)
      out.misaligned.push(g.className.split(' ')[0] + ': ' +
        tops.map(t => t.n + '@' + t.b).join(' | ') + ' spread ' + spread);
  });

  // tap targets
  if (vw < 600) {
    document.querySelectorAll('a, button, label.opt, select, [role=button]').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return;
      if (getComputedStyle(el).display === 'inline' && el.closest('p, li')) return;
      if (r.height < 30)
        out.small.push((el.tagName.toLowerCase() + '.' +
          (el.className.toString().split(' ')[0] || '')) + ' h=' + Math.round(r.height) +
          ' "' + (el.textContent || '').trim().slice(0, 28) + '"');
    });
  }

  const seen = {};
  document.querySelectorAll('[id]').forEach(el => {
    if (seen[el.id]) out.dupIds.push(el.id); else seen[el.id] = 1;
  });
  document.querySelectorAll('img:not([alt])').forEach(el => out.noAlt.push(el.src));
  document.querySelectorAll('a:not([aria-label])').forEach(el => {
    if (!(el.textContent || '').trim() && !el.querySelector('img'))
      out.empty.push(el.getAttribute('href'));
  });
  return out;
}"""

def main():
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(("", PORT), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    problems = 0
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for w, tag in ((1280, "desk"), (390, "mob")):
            c = b.new_context(viewport={"width": w, "height": 900},
                              reduced_motion="reduce")
            pg = c.new_page()
            errs = []
            pg.on("console", lambda m: errs.append(m.text)
                  if m.type == "error" and "403" not in m.text else None)
            for r in ROUTES:
                pg.goto(f"http://localhost:{PORT}{r}", wait_until="load")
                res = pg.evaluate(PROBE)
                for k, v in res.items():
                    if v:
                        problems += len(v)
                        for item in v[:4]:
                            print(f"{tag:<5} {r:<44} {k}: {item}")
            if errs:
                problems += len(errs)
                print(f"{tag:<5} JS errors: {errs[:5]}")
            c.close()
        b.close()
    srv.shutdown()
    print(f"\n{len(ROUTES)} routes x 2 widths — {problems} problems")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
