"""Click the assessment through to a plan, follow the handoff, and confirm the
summary arrives in the enquiry form. Exits non-zero if the chain breaks."""
import http.server, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
PORT = 8113


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=OUT, **k)

    def log_message(self, *a):
        pass


socketserver.TCPServer.allow_reuse_address = True
threading.Thread(target=socketserver.TCPServer(("", PORT), H).serve_forever,
                 daemon=True).start()

fails, errs = [], []
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 900})
    pg.on("pageerror", lambda e: errs.append(str(e)))

    pg.goto(f"http://localhost:{PORT}/assessment/", wait_until="load")

    # answer every question by taking the first option until the plan renders
    for i in range(15):
        if pg.locator("#capture").count():
            break
        opts = pg.locator("#card .opt input")
        if not opts.count():
            fails.append(f"stalled at question {i + 1}: no options rendered")
            break
        opts.first.check()
        nxt = pg.locator("#next")
        if not nxt.count():
            fails.append(f"question {i + 1}: no next button")
            break
        if not nxt.is_enabled():
            fails.append(f"question {i + 1}: next disabled after choosing an option")
            break
        label = nxt.inner_text()
        nxt.click()
        if label.startswith("Build"):
            pg.wait_for_selector("#capture", timeout=5000)

    if not pg.locator("#capture").count():
        fails.append("plan never rendered")
    else:
        print("plan rendered")
        for sel, what in (("#handoff", "handoff button"),
                          ("#print", "print button"),
                          (".bound", "boundary block")):
            if not pg.locator(sel).count():
                fails.append(f"plan missing {what}")
        if pg.locator("#f-email, #send").count():
            fails.append("email capture still present on the plan")

        pg.locator("#handoff").click()
        pg.wait_for_url("**/contact/")
        print("landed on", pg.url)
        val = pg.locator("#q-plan").input_value()
        if "Assessment summary" not in val:
            fails.append(f"form not prefilled: {val[:80]!r}")
        else:
            print("form prefilled with:", val.splitlines()[0])
        if pg.locator("#plan-note").get_attribute("data-has") != "true":
            fails.append("prefill note not revealed")

        # the form itself
        for name in ("name", "business", "email", "whats_eating_the_week",
                     "plan_summary", "form-name", "bot-field"):
            if not pg.locator(f'[name="{name}"]').count():
                fails.append(f"form field missing: {name}")
        if pg.get_attribute("form.eform", "action").split("localhost:%d" % PORT)[-1] != "/thank-you/":
            fails.append("form action is not /thank-you/")

        # required fields actually block an empty submit
        pg.locator("form.eform button[type=submit]").click()
        if "/thank-you/" in pg.url:
            fails.append("empty form submitted without validation")
        else:
            print("empty submit blocked by validation")
    b.close()

errs = [e for e in errs if "403" not in e]
if errs:
    fails.append(f"JS errors: {errs}")
print("\nFAILURES:" if fails else "\nassessment handoff works end to end")
for f in fails:
    print("  fail:", f)
sys.exit(1 if fails else 0)
