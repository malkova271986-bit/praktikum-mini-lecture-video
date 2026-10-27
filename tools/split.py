import cv2, numpy as np, sys
src, prefix = sys.argv[1], sys.argv[2]
rgba=cv2.imread(src,cv2.IMREAD_UNCHANGED)
a=rgba[...,3]
n,l,st,_=cv2.connectedComponentsWithStats((a>40).astype(np.uint8))
order=sorted(range(1,n),key=lambda i:-st[i,cv2.CC_STAT_AREA])
for k,i in enumerate(order[:3]):
    x,y,w,h,ar=st[i]
    print(k,x,y,w,h,ar)
    m=(l==i).astype(np.uint8)*255
    m=cv2.dilate(m,np.ones((5,5),np.uint8))
    out=rgba.copy(); out[...,3]=np.minimum(a,m)
    p=6; y0=max(0,y-p); x0=max(0,x-p)
    cv2.imwrite(f"{prefix}_{k}.png", out[y0:y+h+p, x0:x+w+p])
