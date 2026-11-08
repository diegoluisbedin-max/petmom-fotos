"""Desalaranja só o dourado da joia (regra-dourado-claro), com máscara suave.
Uso: ajuste_ouro.py in out [box x0,y0,x1,y1] [forca]"""
import sys, numpy as np
from PIL import Image, ImageFilter
src,dst=sys.argv[1:3]
im=Image.open(src).convert('RGB'); hsv=np.asarray(im.convert('HSV')).astype(float)/255.
h,s,v=hsv[...,0],hsv[...,1],hsv[...,2]
k=float(sys.argv[4]) if len(sys.argv)>4 else 1.0
w=np.clip((s-0.30)/0.15,0,1)*np.clip(1-np.abs(h-0.12)/0.06,0,1)*np.clip((v-0.3)/0.2,0,1)
if len(sys.argv)>3 and sys.argv[3]!='-':
    x0,y0,x1,y1=map(int,sys.argv[3].split(',')); z=np.zeros_like(w); z[y0:y1,x0:x1]=w[y0:y1,x0:x1]; w=z
wm=Image.fromarray((w*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))
w=np.asarray(wm).astype(float)/255.*k
h2=h+0.012*w; s2=s*(1-0.28*w); v2=np.clip(v*(1+0.03*w),0,1)
out=Image.fromarray((np.stack([h2,s2,v2],-1)*255).astype(np.uint8),'HSV').convert('RGB')
out.save(dst); print(dst)
