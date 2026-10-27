import numpy as np, json, wave
D=float(__import__('sys').argv[1]); sr=44100
N=int(D*sr); t=np.arange(N)/sr
def midi(n): return 440*2**((n-69)/12)
prog=[[57,60,64,69],[53,57,60,65],[48,55,60,64],[55,59,62,67]]  # Am F C G
bar=8.0
out=np.zeros(N)
rng=np.random.default_rng(7)
# pad
for i in range(int(D/bar)+1):
    ch=prog[i%4]; s0=int(i*bar*sr); s1=min(N,int((i+1)*bar*sr+1.5*sr))
    if s0>=N: break
    tt=np.arange(s1-s0)/sr; L=len(tt)
    env=np.minimum(1,tt/2.0)*np.minimum(1,np.maximum(0,(bar+1.5-tt)/2.0))
    for n in ch:
        f=midi(n-12)
        for det in (-0.12,0.12):
            ph=2*np.pi*f*(1+det/100)*tt
            out[s0:s1]+=0.05*env*(np.sin(ph)+0.25*np.sin(2*ph)+0.1*np.sin(3*ph))
    # bass
    f=midi(ch[0]-24); out[s0:s1]+=0.07*env*np.sin(2*np.pi*f*tt)
# arpeggio plucks (soft triangle) every 0.5s
step=0.5
for k in range(int(D/step)):
    i=int(k*step/bar); ch=prog[i%4]
    pattern=[0,2,1,3,2,1,3,2]
    n=ch[pattern[k%8]]+12
    s0=int(k*step*sr); L=int(1.2*sr); s1=min(N,s0+L); tt=np.arange(s1-s0)/sr
    f=midi(n); tri=2*np.abs(2*((f*tt)%1)-1)-1
    out[s0:s1]+=0.035*np.exp(-tt*4.5)*tri*(0.7+0.3*rng.random())
# simple echo
d=int(0.375*sr); echo=np.zeros(N); echo[d:]=out[:-d]*0.3; out=out+echo
from scipy.signal import butter, lfilter
b,a=butter(2,3500/(sr/2)); out=lfilter(b,a,out)
fade=np.minimum(1,t/3)*np.minimum(1,np.maximum(0,(D-t)/4))
out*=fade
out=out/np.max(np.abs(out))*0.35
st=np.stack([out, np.roll(out,int(0.012*sr))],1)
pcm=(st*32767).astype(np.int16)
w=wave.open(__import__('sys').argv[2],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes()); w.close()
