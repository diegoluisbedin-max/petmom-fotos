"""Posição 4 (onde fica) do berloque 221301318: foto da posição 2 + 2 informações numa faixa creme embaixo."""
import sys
from PIL import Image, ImageDraw, ImageFont
src, dst = sys.argv[1:3]
im = Image.open(src).convert("RGB").resize((1600, 1600), Image.LANCZOS)
d = ImageDraw.Draw(im)
COR = (74, 64, 56); CREME = (246, 240, 230)
d.rectangle([0, 1330, 1600, 1600], fill=CREME)
f = lambda s, w: ImageFont.truetype(f"/usr/share/fonts/opentype/inter/Inter-{w}.otf", s)
for txt, y, size, w in [("Passante: a pulseira atravessa o coração", 1370, 66, "SemiBold"), ("1,02 cm de altura × 0,9 cm de largura", 1470, 62, "Medium")]:
    ft = f(size, w); tw = d.textlength(txt, font=ft); d.text(((1600 - tw) / 2, y), txt, font=ft, fill=COR)
im.save(dst, quality=95)
