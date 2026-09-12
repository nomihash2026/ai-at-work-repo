# static/photo

Drop supplied images here using the exact filename listed in `data/media.py`.

Anything present is copied to `/photo/<name>` at build time and rendered at the
one image slot on its route. Anything missing is skipped silently — the page
builds clean — and `build.py` prints it as outstanding.

Do not add a file that is not in the registry; it will be copied and never used.
