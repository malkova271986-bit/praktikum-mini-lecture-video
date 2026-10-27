import cv2, numpy as np, sys
src, out, x0,y0,x1,y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
img = cv2.imread(src, cv2.IMREAD_COLOR)[y0:y1, x0:x1]
h,w = img.shape[:2]
# background model: heavy blur of image with foreground suppressed -> fit smooth plane via low-order poly on border
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32)
# fit quadratic surface to border pixels
ys,xs = np.mgrid[0:h,0:w]
border = np.zeros((h,w),bool); b=12
border[:b,:]=border[-b:,:]=border[:,:b]=border[:,-b:]=True
def feats(x,y):
    x=x/w; y=y/h
    return np.stack([np.ones_like(x),x,y,x*x,y*y,x*y],-1)
F=feats(xs[border],ys[border])
bg=np.zeros_like(lab)
for c in range(3):
    coef,*_=np.linalg.lstsq(F,lab[...,c][border],rcond=None)
    bg[...,c]=(feats(xs,ys)@coef)
d=np.linalg.norm(lab-bg,axis=2)
mask=np.full((h,w),cv2.GC_PR_BGD,np.uint8)
mask[d<6]=cv2.GC_BGD
mask[d>22]=cv2.GC_PR_FGD
mask[d>40]=cv2.GC_FGD
bgd=np.zeros((1,65));fgd=np.zeros((1,65))
cv2.grabCut(img,mask,None,bgd,fgd,4,cv2.GC_INIT_WITH_MASK)
m=np.where((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD),255,0).astype(np.uint8)
# keep components of reasonable size
n,lbl,st,_=cv2.connectedComponentsWithStats(m)
keep=np.zeros_like(m)
for i in range(1,n):
    if st[i,cv2.CC_STAT_AREA]>800: keep[lbl==i]=255
keep=cv2.morphologyEx(keep,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
# fill holes
ff=keep.copy(); cv2.floodFill(ff,None,(0,0),128)
keep[ff==0]=255
alpha=cv2.GaussianBlur(keep,(0,0),1.2)
rgba=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA); rgba[...,3]=alpha
cv2.imwrite(out,rgba)
# preview on dark
prev=(rgba[...,:3].astype(float)*(alpha[...,None]/255)+np.array([60,20,25])*(1-alpha[...,None]/255)).astype(np.uint8)
cv2.imwrite(out.replace('.png','_prev.jpg'),prev)
