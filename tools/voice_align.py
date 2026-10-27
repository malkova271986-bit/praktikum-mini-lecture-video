"""Usage: python3 voice_align.py <project_dir> <voice.mp3> [fix_json]
Aligns subtitle boundaries in <project>/subs.json to pauses in the voice track,
prints per-segment speaking rate (chars/s) to spot misalignment."""
import json, subprocess, sys, re, numpy as np
proj, voice = sys.argv[1], sys.argv[2]
fix = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
d = json.load(open(f'{proj}/subs.json'))
subs = [x for _, s in d for x in s]
import os
vsubs = [x for _, s in json.load(open(f'{proj}/voice.json')) for x in s] if os.path.exists(f'{proj}/voice.json') else subs
out = subprocess.run(['ffmpeg', '-i', voice, '-af', 'silencedetect=noise=-38dB:d=0.22', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr.replace('\r', '\n')
st = [float(x) for x in re.findall(r'silence_start: ([0-9.]+)', out)]
en = [float(x) for x in re.findall(r'silence_end: ([0-9.]+)', out)]
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', voice],
                           capture_output=True, text=True).stdout)
sil = list(zip(st, en))
S0 = sil[0][1] if sil and sil[0][0] < 0.05 else 0.0
E = sil[-1][0] if sil and sil[-1][1] > dur - 0.3 else dur
inner = [s for s in sil if s[0] > S0 + 1 and s[1] < E - 0.5]
V='аеёиоуыэюяАЕЁИОУЫЭЮЯ'
REP=[('1991','тысяча девятьсот девяносто первом'),('1943','тысяча девятьсот сорок третьего'),('1963','тысяча девятьсот шестьдесят третий'),('1983','тысяча девятьсот восемьдесят третий'),('2003','две тысячи третьего'),('2012','две тысячи двенадцатом'),('1950-е','пятидесятые двадцатого века'),('2018','две тысячи восемнадцатого'),('1980-х','тысяча девятьсот восьмидесятых'),('1990-х','тысяча девятьсот девяностых'),('2000-х','двухтысячных'),(' X',' икс'),(' Y',' игрек'),(' Z',' зет'),('Telegram','телеграм'),('XV','пятнадцатом'),('XXI','двадцать первом')]
def vc(t):
    for a,b in REP: t=t.replace(a,b)
    return sum(c in V for c in t)
w = np.array([vc(s) + 2 for s in vsubs], float)
# DP minimising deviation of each segment's syllable rate from the global rate
pts = [(S0, S0)] + [tuple(x) for x in inner] + [(E, E)]
P = len(pts); n = len(subs)
r = w.sum() / (E - S0 - sum(b - a for a, b in inner) * 0.0)
INF = 1e18
cost = np.full((n + 1, P), INF); back = np.zeros((n + 1, P), int); cost[0, 0] = 0
for i in range(1, n + 1):
    for k in range(1, P):
        if i == n and k != P - 1: continue
        if i < n and k == P - 1: continue
        best = INF; bj = 0
        for j in range(0, k):
            if cost[i - 1, j] >= INF: continue
            t0 = pts[j][1]; t1 = pts[k][0]
            if t1 - t0 < 0.8: continue
            c = np.log((w[i - 1] / (t1 - t0)) / r) ** 2 - (0.15 * (pts[k][1] - pts[k][0]) if i < n else 0)
            if cost[i - 1, j] + c < best: best = cost[i - 1, j] + c; bj = j
        cost[i, k] = best; back[i, k] = bj
k = P - 1; idx = []
for i in range(n, 0, -1):
    j = back[i, k]; idx.append(j); k = j
idx = idx[::-1][1:]
sel = [list(pts[j]) for j in idx]
for kk, v in fix.items(): sel[int(kk)] = v
b = [[0, S0]] + sel + [[E, dur]]
seg = [(b[i][1], b[i + 1][0]) for i in range(len(subs))]
for i, (s, (t0, t1)) in enumerate(zip(subs, seg)):
    print(i, round(t0, 2), round(t1, 2), round(w[i] / max(0.1, t1 - t0), 2), s[:45])
print('silences:', ' '.join(f'{a:.2f}-{b:.2f}' for a, b in inner))
json.dump(seg, open(f'{proj}/out/voice_segs.json', 'w'))
