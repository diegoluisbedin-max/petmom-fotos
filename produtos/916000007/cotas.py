"""Cotas da posição 5 (pingentes com as medidas em cm) e textos sobre foto, padrão de 08/11/2026.
Coordenadas no quadro de 1024 (como a base sai da IA); a saída é 1600x1600.
Letra mínima: 40 no quadro de 1024 = 62 px no de 1600 (regra do padrao-cadastro-petmom.md).
Nada importante a menos de 64 (1024) / 100 px (1600) da borda. No máximo poucas cotas, grandes.
Uso: copiar para produtos/<SKU>/cotas.py, trocar as cotas do fim e rodar: python3 cotas.py base.png saida.png"""
import sys
from PIL import Image, ImageDraw, ImageFont
src, dst = sys.argv[1:3]
SS = 3  # supersampling
im = Image.open(src).convert("RGB").resize((1024*SS, 1024*SS), Image.LANCZOS)
d = ImageDraw.Draw(im)
COR = (74, 64, 56)
f = lambda size, w="Medium": ImageFont.truetype(f"/usr/share/fonts/opentype/inter/Inter-{w}.otf", int(size*SS))
def s(*v): return [x*SS for x in v]
LBL = 40  # tamanho mínimo das cotas (quadro de 1024)
def hcota(x0, x1, y, label, below=True):
    d.line(s(x0, y, x1, y), fill=COR, width=3*SS)
    for x in (x0, x1): d.line(s(x, y-10, x, y+10), fill=COR, width=3*SS)
    ft = f(LBL); w = d.textlength(label, font=ft)/SS
    d.text(s((x0+x1)/2 - w/2, y+14 if below else y-56), label, font=ft, fill=COR)
def vcota(x, y0, y1, label, left=False):
    d.line(s(x, y0, x, y1), fill=COR, width=3*SS)
    for y in (y0, y1): d.line(s(x-10, y, x+10, y), fill=COR, width=3*SS)
    ft = f(LBL); w = d.textlength(label, font=ft)/SS
    d.text(s(x-16-w if left else x+16, (y0+y1)/2 - 24), label, font=ft, fill=COR)
def titulo(txt, y, size=54, w="SemiBold"):
    ft = f(size, w); tw = d.textlength(txt, font=ft)/SS
    d.text(s(512 - tw/2, y), txt, font=ft, fill=COR)
def rotulo(txt, cx, y, size=40):
    ft = f(size); tw = d.textlength(txt, font=ft)/SS
    d.text(s(cx - tw/2, y), txt, font=ft, fill=COR)
# ---- 916000007 conjunto medalha patinha (brinco esq x155-352 y445-645; pingente x405-610 y309-655; brinco dir x667-866) ----
titulo("Medidas", 150)
hcota(157, 352, 700, "0,9 cm")
hcota(407, 610, 700, "0,9 cm")
hcota(669, 866, 700, "0,9 cm")
rotulo("brinco", 254, 770, 34)
rotulo("pingente", 508, 770, 34)
rotulo("brinco", 767, 770, 34)
rotulo("corrente veneziana 45 cm", 512, 850)
rotulo("+ 3 cm de extensor", 512, 905)
# ---------------------------------------
im.resize((1600, 1600), Image.LANCZOS).save(dst)
