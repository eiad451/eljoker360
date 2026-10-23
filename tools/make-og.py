#!/usr/bin/env python3
"""Render the 1200x630 Open Graph card for El Joker Agency."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
PAPER = (247, 245, 240)
INK = (28, 28, 26)
SECOND = (111, 106, 97)
MUTED = (154, 149, 140)
BORDER = (231, 225, 214)

ARABIC = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"
LATIN_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
LATIN_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

f_ar = ImageFont.truetype(ARABIC, 84)
f_sub = ImageFont.truetype(LATIN_SANS, 27)
f_brand = ImageFont.truetype(LATIN_SERIF, 30)
f_mark = ImageFont.truetype(LATIN_SERIF, 40)
f_foot = ImageFont.truetype(LATIN_SANS, 24)

def rtl(draw, xy, text, font, fill):
    draw.text(xy, text, font=font, fill=fill, direction="rtl", language="ar", anchor="ra")

# border frame (hairline)
d.rectangle([24, 24, W - 25, H - 25], outline=BORDER, width=2)

# monogram block, top-right for RTL
d.rounded_rectangle([W - 130, 76, W - 76, 130], radius=12, fill=INK)
d.text((W - 103, 103), "EJ", font=f_mark, fill=PAPER, anchor="mm")

# brand line
d.text((W - 76, 168), "EL JOKER AGENCY", font=f_brand, fill=INK, anchor="ra")

# headline (Arabic, RTL)
rtl(d, (W - 76, 236), "نموّ رقمي مبني على النظام", f_ar, INK)

# rule
d.line([76, 372, W - 76, 372], fill=BORDER, width=2)

# subtitle
rtl(d, (W - 76, 404), "تسويق رقمي · هوية بصرية · حملات مدفوعة", f_sub, SECOND)

# footer
d.text((76, H - 96), "eljoker360.com", font=f_foot, fill=MUTED)
d.text((W - 76, H - 96), "القاهرة، مصر", font=ImageFont.truetype(ARABIC, 26), fill=MUTED,
       direction="rtl", language="ar", anchor="ra")

img.save("og.png", optimize=True)
print("og.png written")
