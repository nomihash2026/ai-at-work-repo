"""The image registry.

One image per route, maximum. That is the whole rule, and build.py enforces it
by construction: this is a dict, so a route cannot hold two.

An entry renders only if the file actually exists in static/photo/. Until then
the route builds clean with no gap and no placeholder box, so the site can go
live before the photography does. `build.py` prints what is still missing.

  file     filename inside static/photo/
  alt      what the image shows, for someone who cannot see it. Not a caption.
  caption  what it tells the reader that the text does not. Optional, but if
           you cannot write one, the image is decoration and should be cut.
  ratio    "wide" (16:9, full bleed) or "portrait" (4:5, one column)
  kind     "photo" or "screen" — screenshots sit in the column, not full bleed

Slot: directly beneath the page hero, before the first body section. One slot,
every page, no exceptions — alternating placement reads as indecision.
"""

MEDIA = {
    # ---------------------------------------------------------------- proof --
    # Photographs of the real thing. These carry what prose cannot: that there
    # is a room, and people in it, and that it is not a webinar.
    "/": {
        "file": "workshop-room.jpg",
        "ratio": "wide",
        "kind": "photo",
        "alt": "A team around a table with laptops open during an AI at work "
               "session, one person standing at a screen.",
        "caption": "A session in progress. Two thirds of the time is the team "
                   "doing their own work while someone watches over their shoulder.",
    },
    "/about/": {
        "file": "who-is-teaching.jpg",
        "ratio": "portrait",
        "kind": "photo",
        "alt": "The person who runs the training sessions.",
        "caption": "Who turns up on the day.",
    },
    "/services/team-workshop/": {
        "file": "workshop-delivery.jpg",
        "ratio": "wide",
        "kind": "photo",
        "alt": "A close view of a laptop screen and a notepad during a workshop.",
        "caption": "The work people bring is their own. Nothing is demonstrated "
                   "on an invented example.",
    },

    # ------------------------------------------------------------- evidence --
    # Deliberately empty. The five slots that used to live here — project
    # setup, custom setups, tier settings, a long-document upload and a prompt
    # before-and-after — are now typographic figures built in content/, not
    # images. Three reasons, in order of weight: inventing a vendor's interface
    # is not ours to do; this site's own rule is that nothing on it is made up;
    # and a screenshot of a UI is stale the quarter after it is taken, while a
    # diagram of what goes where is not. Replace with real captures once there
    # are real sessions to capture — add the entry back and drop the file in.
}
