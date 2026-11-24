#!/usr/bin/env python3
"""Draw the Bump Crew home-screen icon and write every size iOS and Android ask for.

    python3 scripts/make-icon.py      (needs Pillow: pip install pillow)

The mark is a baby bottle, matching the 🍼 in the app header, drawn from the
geometry in SPEC (fractions of the canvas), so it is retuned by changing
numbers rather than in an image editor.

The canvas is square and full-bleed on purpose: iOS applies its own rounded
mask, so rounded corners drawn here would leave slivers outside it.
"""
import os
from PIL import Image, ImageDraw, PngImagePlugin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "icons")

PINK = "#E0607E"   # background: the app's accent colour
CREAM = "#FFF6EE"  # bottle body
GOLD = "#F4B860"   # collar and nipple (the trimester-2 colour in the app)

# Each shape: (x0, y0, x1, y1, corner radius), in fractions of the canvas.
SPEC = {
    "nipple": (0.445, 0.115, 0.555, 0.280, 0.055),
    "flange": (0.400, 0.240, 0.600, 0.290, 0.020),
    "collar": (0.330, 0.280, 0.670, 0.375, 0.028),
    "body":   (0.310, 0.365, 0.690, 0.885, 0.085),
    # Measuring marks on the body: (x0, x1, y), drawn with rounded ends.
    "ticks": [(0.385, 0.505, 0.505), (0.385, 0.465, 0.605), (0.385, 0.505, 0.705)],
    "tick_width": 0.030,
}

SS = 4  # draw 4x larger, then downscale, for smooth curves


def render(size):
    n = size * SS
    img = Image.new("RGB", (n, n), PINK)
    d = ImageDraw.Draw(img)

    def box(key, fill):
        x0, y0, x1, y1, r = SPEC[key]
        d.rounded_rectangle((x0 * n, y0 * n, x1 * n, y1 * n), radius=r * n, fill=fill)

    box("nipple", GOLD)
    box("flange", GOLD)
    box("body", CREAM)
    box("collar", GOLD)
    w = SPEC["tick_width"] * n
    for x0, x1, y in SPEC["ticks"]:
        d.rounded_rectangle((x0 * n, y * n - w / 2, x1 * n, y * n + w / 2), radius=w / 2, fill=PINK)
    return img.resize((size, size), Image.LANCZOS)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    # Tag as sRGB so iOS doesn't have to guess a colour space when it bakes
    # the home-screen asset.
    meta = PngImagePlugin.PngInfo()
    meta.add(b"sRGB", b"\x00")
    meta.add(b"gAMA", (45455).to_bytes(4, "big"))
    # The exact sizes iOS asks for (152 iPad, 167 iPad Pro, 180 iPhone), so it
    # never rescales one itself, plus 192/512 for Android and the manifest.
    names = {180: "apple-touch-icon.png", 152: "icon-152.png", 167: "icon-167.png",
             192: "icon-192.png", 512: "icon-512.png", 32: "favicon-32.png"}
    for size, name in names.items():
        render(size).save(os.path.join(OUT_DIR, name), pnginfo=meta)
    print("wrote", ", ".join(sorted(names.values())), "to icons/")


if __name__ == "__main__":
    main()
