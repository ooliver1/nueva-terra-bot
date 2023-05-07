from __future__ import annotations

from io import BytesIO

from nextcord import Embed, File
from PIL import Image, ImageDraw, ImageFont

from nueva_terra.time import current_format

IMAGE: Image.Image = Image.open("images/background.png")
BIG_FONT = ImageFont.truetype("fonts/Minecrafter_3.ttf", size=200)
LICENSE = "https://mirrors.creativecommons.org/presskit/icons/cc.png"
LICENSE_TEXT = "Font: CC BY-ND 4.0 - MadPixel"
BRANDING = 0x13602D
TEXT_COLOUR = (185, 174, 172)
TEXT_OUTLINE = (0, 0, 0)


def generate_content() -> tuple[File, Embed]:
    fp = BytesIO()
    image = IMAGE.copy()
    text = current_format()
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(text, BIG_FONT)
    width, height = image.size

    # Center text.
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.multiline_text(
        (x, y),
        text,
        font=BIG_FONT,
        fill=TEXT_COLOUR,
        stroke_width=5,
        stroke_fill=TEXT_OUTLINE,
    )

    # Save to an in-memory file, then seek the pointer to the beginning to be read.
    image.save(fp, format="png")
    fp.seek(0)
    file = File(fp, filename="time.png")

    embed = Embed(colour=BRANDING)
    embed.set_image(url="attachment://time.png")
    embed.set_footer(text=LICENSE_TEXT, icon_url=LICENSE)

    return file, embed
