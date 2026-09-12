"""Screenshot key routes at desktop and mobile widths, and report JS errors."""
import http.server, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
SHOTS = os.path.join(ROOT, "shots")
PORT = 8111

ROUTES = sys.argv[1:] or ["/", "/contact/", "/thank-you/", "/insights/",
                          "/insights/first-ninety-minutes/",
                          "/industries/accounting-bookkeeping/", "/assessment/"]


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=OUT, **kw)

    def log_message(self, *a):
        pass


def serve():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as s:
        s.serve_forever()


threading.Thread(target=serve, daemon=True).start()
os.makedirs(SHOTS, exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    for label, vw, full in (("desk", 1280, True), ("mob", 390, True)):
        page = b.new_page(viewport={"width": vw, "height": 900})
        errs = []
        page.on("pageerror", lambda e: errs.append(str(e)))
        page.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        for r in ROUTES:
            page.goto(f"http://localhost:{PORT}{r}", wait_until="networkidle")
            name = (r.strip("/").replace("/", "-") or "home")
            page.screenshot(path=f"{SHOTS}/{name}.{label}.png", full_page=full)
        print(f"{label}: {len(ROUTES)} shots", "| JS errors:", errs or "none")
        page.close()
    b.close()
print("shots in", SHOTS)
