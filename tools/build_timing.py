import json, re, subprocess, sys, wave
proj=sys.argv[1]
d=json.load(open(f'{proj}/subs.json')); seg=json.load(open(f'{proj}/out/voice_segs.json'))
TL=[]; k=0; T=0.4; offs=[]
for si,(sid,subs) in enumerate(d):
    n=len(subs); a=seg[k:k+n]; k+=n
    lead=0.8 if si==0 else 1.3
    start=T; off=start+lead-a[0][0]
    ss=[]
    for j,(t0,t1) in enumerate(a):
        e=(a[j+1][0]+off-0.05) if j<n-1 else t1+off+0.4
        ss.append([t0+off,e])
    end=ss[-1][1]+0.4
    TL.append({'start':start,'end':end,'subs':ss}); offs.append([max(0,a[0][0]-0.15),a[-1][1]+0.15,off]); T=end
D=round(T+1.6,2)
s=open(f'{proj}/index.html').read()
s=re.sub(r'const FIXED = .*?;\n','const FIXED = '+json.dumps(TL)+';\n',s,count=1,flags=re.S)
open(f'{proj}/index.html','w').write(s)
f=[];lab=[]
for i,(a0,a1,off) in enumerate(offs):
    dl=int(round((a0+off)*1000))
    f.append(f"[0:a]atrim={a0:.3f}:{a1:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st={a1-a0-0.08:.3f}:d=0.08,adelay={dl}|{dl}[v{i}]"); lab.append(f"[v{i}]")
f.append("".join(lab)+f"amix=inputs={len(lab)}:normalize=0,apad,atrim=0:{D}[voice]")
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{proj}/out/voice.mp3','-filter_complex',';'.join(f),'-map','[voice]','-ac','2','-ar','44100',f'{proj}/out/voice_track.wav'],check=True)
json.dump(TL,open(f'{proj}/out/fixed.json','w'))
print(D)
