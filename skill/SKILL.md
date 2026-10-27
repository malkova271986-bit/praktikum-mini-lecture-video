---
name: praktikum-mini-lecture-video
description: Делает мини-лекцию (3–5 мин) по презентации .pptx в фирменном стиле практикума Е. В. Бэкман с героем-мальчиком: анализ слайдов, текст для озвучки, анимация, синхронизация с озвучкой ElevenLabs, MP4 и комплект для YouTube.
---

# Мини-лекция практикума по презентации

Серия видео к учебному практикуму Е. В. Бэкман. Ведущий — герой практикума, мальчик в фиолетовой голографической толстовке с LED-экраном (сердце + Wi-Fi + ON), в кепке с USB-кабелем, рядом два маленьких летающих робота-монитора. Лекцию «читает» он, поэтому озвучка — мужской голос (ElevenLabs, раньше использовались Alan и Podcaster; для единства серии лучше один голос).

Уже сделано в серии: 1) «Цифровизация и цифровые технологии в образовании»; 2) «Организация образовательного и воспитательного процессов с использованием ИКТ» (социология интернета, теория поколений, ИКТ); 3) «Дизайн ЭОР: от педагогических принципов до игровых механик» (завершающая).

## Порядок работы (два хода с пользователем)

**Ход 1 — сразу после получения .pptx:**
1. Сказать одной фразой, что делаешь. Извлечь текст слайдов и заметок (python-pptx: текст фигур, таблицы, notes). Заметки докладчика — главный источник содержания.
2. Сжать лекцию в 8–10 смысловых сцен + вступление + финал, итого ≈ 3 400–3 700 знаков (≈ 4–5 мин). Каждая сцена: 2–4 фразы-субтитра по 90–190 знаков. Записать `subs.json`: `[["intro",[...]],["s1",[...]],...,["outro",[...]]]`.
3. Сделать `voice.json` той же структуры — текст для синтеза: латиницу и цифры, которые голос исказит, записать по-русски (Kahoot→Кахут, Canva→Канва, X/Y/Z→икс/игрек/зет, Telegram→Телеграм, «более 90%»→«более девяноста процентов», «1950-е»→«пятидесятые годы двадцатого века», «КНР»→«Китае»). Из него — файл `Текст_для_озвучки_N.txt`: только сплошной текст, абзац на сцену, без таймкодов и заголовков (пользователь вставляет его прямо в ElevenLabs). Отправить файл и коротко перечислить блоки.
4. Пока пользователь озвучивает — собрать композицию, проверить кадры, сделать обложку.

**Ход 2 — когда пришёл mp3:** синхронизация → рендер (≈ 30 мин, в фоне) → сведение → проверка кадров → отправить MP4, обложку, описание, SRT; текст описания дать и в ответе.

## Правила содержания
- Язык научный, но разговорный для студентов; связки «Между тем», «Ведь», «Следовательно», «Обратим внимание». В субтитрах: «КНР» вместо «Китай», «РБ» вместо «Беларусь».
- **На первом слайде видео НЕ ставить имя автора** (пользователь просил убрать).
- Каждая сцена начинается с вопроса героя в облачке (эвристический диалог «Что? – Как? – Почему?»).
- Финал: вопрос для обсуждения на практикуме (взять из слайдов «Обсуждение/Дискуссия» или сформулировать по теме) + «До встречи на практикуме!». В завершающей лекции серии — благодарность за серию.
- Факты и цифры — только из презентации или проверенные; устаревшие прогнозы и цены не брать; названия коммерческих сайтов давать обобщённо, если они не суть темы. Прямые цитаты дословно и с автором.
- На экране не ставить библиографические ссылки в скобках.

## Визуальный стиль (не менять)
1920×1080, 25 fps. Тёмно-индиговый фон с точечной сеткой и плавающими фиолетовым/бирюзовым свечениями; палитра героя: фиолетовый #8b5cf6/#a78bfa/#c4b5fd, бирюза #5eead4/#67e8f9, розовый #f472b6, зелёный #4ade80. Шрифты Inter / Inter Display (заголовки 800–900), DejaVu Sans Mono для LED-плашек («01 · ТЕМА»). Сверху прогресс-полоса с отметками сцен. Контент слева (x 100–1280), субтитры — плашка внизу слева (y 880), герой справа: анфас (`front_0.png`) в объясняющих сценах, профиль (`side_0.png`, смотрит на контент) — в чередующихся; роботы `front_1/front_2` парят рядом. Вступление и финал — окно «голограммы» `holo_win.jpg` с подписью `*.EXE` вместо героя. Карточки — полупрозрачные фиолетовые с иконками-контурами; диаграммы (сети, лестницы, цепочки, таймлайны) рисовать SVG, а не списками. Музыка — тихий эмбиент (Am–F–C–G, мягкие арпеджио), под голосом приглушается.

## Подготовка героя
Попросить у пользователя исходные картинки героя (PNG: разворот «анфас | профиль» и кадр с голограммой), если их нет в сессии. Вырезать фон: `cutout.py` (кроп анфаса `0 0 700 768`, профиля `712 0 1408 700` для разворота 1408×768), затем `split.py` → `front_0` (герой), `front_1/front_2` (роботы), `side_0`. Голограмму не вырезать: кроп `(330,0,1250,768)` → `holo_win.jpg` (без водяного знака в правом нижнем углу). Если внутри петли кабеля у профиля остался серый фон — обнулить альфу серых пикселей в этом прямоугольнике. Проверять превью на тёмном фоне. В шаблоне ширины спрайтов (414 и 351 px) заданы под эти вырезки — при других исходниках поправить.

## Сборка
Рабочая папка `video/` с `assets/`, `out/`, `subs.json`, `voice.json`. `index.html` = шаблон ниже: заменить три примерные сцены на сцены лекции (по одной на запись `subs.json`, в том же порядке) и `__SUBS__` на содержимое `subs.json`.
Сцена: `{ id, chip:'03 · Тема', title:'Текст <em>акцент</em>', bubble:'Вопрос героя?', pose:'front'|'side'|'none', html:\`...\` }`. Элемент появляется синхронно с фразой: `data-sub="k"` (номер фразы в сцене), `data-d="сек"` (задержка от начала фразы — ставить по месту слова в фразе), `data-fx` = up | left | scale | pop | fade | rise | grow | win. Хелперы: `ic(name)`, `pill(text,color)`, `card3([...])`, `bannerBox(top,sub,delay,inner,color)`.
Проверка: `node still.js index.html <dir> t1 t2 ...` → печатает расписание сцен и сохраняет кадры; смотреть кадр в конце каждой сцены (склеить сеткой 2×2), искать наложения, вылезающий текст, пустоты. Типичные правки: длинные заголовки ≤ 1 строки (60 px, до 1170 px), h3 в узких карточках 22–30 px, иконкам `flex-shrink:0`.

## Синхронизация с озвучкой
1. `python3 voice_align.py <proj> <proj>/out/voice.mp3` — ищет паузы (silencedetect) и динамикой подбирает границы фраз, минимизируя разброс темпа (слоги/с, по `voice.json`). Смотреть столбец темпа: норма ≈ 5–7 слог/с; выбросы (< 4 или > 8) = сдвинутая граница → передать исправления JSON-аргументом `'{"10":[76.99,77.35]}'` (индекс границы → пауза из списка `silences`).
2. `python3 build_timing.py <proj>` — вписывает тайминг в `index.html` (паузы 1,3 с между сценами для переходов), собирает `out/voice_track.wav`, печатает длительность D.
3. `python3 music.py D out/music.wav`, затем сведение:
`ffmpeg -i music.wav -i voice_track.wav -filter_complex "[0:a]volume=0.55[m];[1:a]loudnorm=I=-16:TP=-1.5,asplit=2[v][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=50:release=600[md];[md][v]amix=inputs=2:normalize=0[out]" -map "[out]" -ar 48000 mix.wav`
4. Рендер в два потока (фоновой командой, с `wait`): `node render.js index.html out/p1.mp4 0 H` и `... out/p2.mp4 H F` (F = D×25), склейка `ffmpeg -f concat -safe 0 -i list.txt -c copy video_only.mp4`, затем `ffmpeg -i video_only.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -af apad -t D -movflags +faststart "<Тема>_мини-лекция.mp4"`. Не использовать `pkill -f` с шаблоном, совпадающим с собственной командой.
5. Проверить 10 кадров готового MP4 (сетка 2×5). Мелкие правки (например, вступление) — перерендерить только диапазон кадров и склеить.

## Комплект для YouTube (всегда)
- **Обложка** 1280×720 JPG: плашка «МИНИ-ЛЕКЦИЯ», крупный заголовок (Inter Display 900, акцентное слово градиентом), розовая плашка внизу («за 4 минуты» / «финал серии»), справа герой анфас, рядом маленький робот (не перекрывать текст).
- **Название** (≤ 100 знаков), **описание**: 1–2 абзаца о содержании + вопрос для обсуждения + «Содержание:» с главами (первая 0:00; время = начало первой фразы сцены − 0,3 с) + 3 хэштега; **теги** через запятую. Всё в `YouTube_описание_N.txt` и тем же текстом в ответе.
- **Субтитры** `.srt` из тайминга (субтитры уже вшиты в видео; SRT — для поиска и отдельного показа).
- Напомнить настройки: доступ **«Доступ по ссылке»** (не «Ограниченный» — тот закрывает видео для всех, кроме приглашённых), «Не для детей», категория «Образование», язык русский.

## Скрипты (создать в рабочей папке)

### template.html (основа index.html)
```html
<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>Мини-лекция практикума</title>
<style>
:root{
  --bg0:#0d0a24; --bg1:#1a1446; --violet:#8b5cf6; --violet2:#a78bfa; --lilac:#c4b5fd;
  --cyan:#5eead4; --cyan2:#67e8f9; --pink:#f472b6; --green:#4ade80; --ink:#f5f3ff; --mute:#b9b3d9;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;overflow:hidden;background:var(--bg0)}
body{font-family:'Inter',sans-serif;color:var(--ink);position:relative}
#stage{position:absolute;inset:0;overflow:hidden;
  background:radial-gradient(1200px 900px at 78% 55%, #2a1f6b 0%, rgba(42,31,107,0) 60%),
             radial-gradient(900px 700px at 15% 20%, #1d1650 0%, rgba(29,22,80,0) 70%),
             linear-gradient(160deg,#120d33 0%,#0b0820 100%);}
.abs{position:absolute}
#dots{position:absolute;inset:-40px;opacity:.35;
  background-image:radial-gradient(circle,rgba(167,139,250,.35) 1.4px,transparent 1.6px);background-size:36px 36px;}
.glow{position:absolute;border-radius:50%;filter:blur(80px);opacity:.45}
/* top progress */
#prog{left:100px;right:100px;top:44px;height:4px;border-radius:2px;background:rgba(196,181,253,.15)}
#progfill{position:absolute;left:0;top:0;bottom:0;border-radius:2px;background:linear-gradient(90deg,var(--violet),var(--cyan));transform-origin:0 0}
.tick{position:absolute;top:-4px;width:12px;height:12px;border-radius:3px;background:#2a2160;border:2px solid #4c3d9e;margin-left:-6px}
.tick.on{background:var(--cyan);border-color:var(--cyan);box-shadow:0 0 12px var(--cyan)}
/* header */
.chip{display:inline-flex;align-items:center;gap:12px;font-family:'DejaVu Sans Mono',monospace;font-size:22px;letter-spacing:3px;
  color:var(--cyan);padding:9px 18px;border:2px solid rgba(94,234,212,.5);border-radius:10px;background:rgba(94,234,212,.07);text-transform:uppercase}
.chip i{width:10px;height:10px;background:var(--green);border-radius:2px;box-shadow:0 0 10px var(--green)}
.h1{font-family:'Inter Display','Inter';font-weight:800;font-size:66px;line-height:1.05;letter-spacing:-1px}
.h1 em{font-style:normal;background:linear-gradient(90deg,var(--lilac),var(--cyan2));-webkit-background-clip:text;color:transparent}
.scene{position:absolute;left:0;top:0;width:1920px;height:1080px}
.head{position:absolute;left:100px;top:96px}
.head .h1{margin-top:22px;font-size:60px;max-width:1170px}
.body{position:absolute;left:100px;top:300px;width:1180px;height:540px}
/* cards */
.card{position:absolute;border-radius:22px;background:linear-gradient(160deg,rgba(139,92,246,.20),rgba(30,22,80,.55));
  border:1.5px solid rgba(167,139,250,.35);box-shadow:0 20px 50px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.08);padding:28px 30px}
.card h3{font-family:'Inter Display';font-weight:700;font-size:30px;line-height:1.12;margin-bottom:12px}
.card p{font-size:25px;line-height:1.38;color:var(--mute)}
.num{font-family:'DejaVu Sans Mono';font-size:22px;color:var(--cyan);letter-spacing:2px;margin-bottom:14px;display:block}
.ico{width:64px;height:64px;margin-bottom:16px;flex-shrink:0}
.ico *{fill:none;stroke:var(--cyan2);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
.lbl{font-size:26px;color:var(--mute);line-height:1.35}
/* subtitles */
#sub{position:absolute;left:100px;top:880px;width:1180px;height:150px;display:flex;align-items:center}
#subbox{position:relative;width:100%;padding:22px 30px 22px 34px;border-radius:18px;background:rgba(10,7,30,.72);border:1px solid rgba(167,139,250,.25)}
#subbox:before{content:"";position:absolute;left:0;top:18px;bottom:18px;width:5px;border-radius:3px;background:linear-gradient(var(--violet2),var(--cyan))}
#subtext{font-size:31px;line-height:1.36;font-weight:500;color:#fff}
/* hero */
#hero{position:absolute;left:1330px;top:0;width:560px;height:1080px}
#hero img{position:absolute}
.bubble{position:absolute;left:1300px;top:92px;width:400px;padding:22px 26px;border-radius:24px 24px 6px 24px;background:#f5f3ff;color:#1b1446;
  font-family:'Inter Display';font-weight:700;font-size:28px;line-height:1.22;box-shadow:0 16px 40px rgba(0,0,0,.4), 0 0 0 3px rgba(167,139,250,.6)}
.bubble:after{content:"";position:absolute;right:-14px;bottom:0;border-left:22px solid #f5f3ff;border-top:22px solid transparent}
.bubble .cur{display:inline-block;width:3px;height:30px;background:var(--violet);margin-left:3px;vertical-align:-4px}
/* holo window */
.win{position:absolute;border-radius:26px;overflow:hidden;border:2px solid rgba(167,139,250,.7);
  box-shadow:0 0 0 8px rgba(139,92,246,.12),0 0 80px rgba(139,92,246,.45),0 30px 60px rgba(0,0,0,.5);background:#777}
.win .bar{position:absolute;left:0;right:0;top:0;height:46px;background:rgba(18,13,51,.85);display:flex;align-items:center;gap:10px;padding-left:20px;z-index:2}
.win .bar b{width:13px;height:13px;border-radius:50%;display:block}
.win .bar span{margin-left:14px;font-family:'DejaVu Sans Mono';font-size:17px;color:var(--lilac);letter-spacing:2px}
.win img{position:absolute;left:0;top:46px;width:100%}
.pill{display:inline-block;padding:10px 20px;border-radius:999px;font-size:24px;font-weight:600;border:1.5px solid rgba(94,234,212,.5);color:var(--cyan);background:rgba(94,234,212,.08);margin:0 10px 12px 0}
svg text{font-family:'Inter'}
</style>
</head>
<body>
<div id="stage">
  <div id="dots"></div>
  <div class="glow" id="g1" style="width:620px;height:620px;background:#7c3aed;left:1250px;top:300px"></div>
  <div class="glow" id="g2" style="width:420px;height:420px;background:#0e7490;left:-80px;top:620px;opacity:.3"></div>
  <div class="abs" id="prog"><div id="progfill"></div></div>
  <div id="scenes"></div>
  <div id="hero">
    <img id="heroFront" src="assets/front_0.png">
    <img id="heroSide" src="assets/side_0.png">
    <img id="robA" src="assets/front_1.png">
    <img id="robB" src="assets/front_2.png">
  </div>
  <div class="bubble" id="bubble"><span id="btext"></span><span class="cur" id="bcur"></span></div>
  <div id="sub"><div id="subbox"><div id="subtext"></div></div></div>
</div>

<script>
// ---------------- content ----------------
const ICON = {
  book:'<path d="M8 12h20a6 6 0 0 1 6 6v36a5 5 0 0 0-5-5H8z"/><path d="M58 12H38a6 6 0 0 0-6 6v36a5 5 0 0 1 5-5h21z"/>',
  gear:'<circle cx="32" cy="32" r="9"/><path d="M32 6v8M32 50v8M6 32h8M50 32h8M13.6 13.6l5.7 5.7M44.7 44.7l5.7 5.7M13.6 50.4l5.7-5.7M44.7 19.3l5.7-5.7"/>',
  bolt:'<path d="M36 6 14 36h16l-4 22 24-32H34z"/>',
  pc:'<rect x="8" y="10" width="48" height="32" rx="4"/><path d="M24 54h16M32 42v12"/>',
  ai:'<rect x="16" y="16" width="32" height="32" rx="6"/><path d="M26 6v10M38 6v10M26 48v10M38 48v10M6 26h10M6 38h10M48 26h10M48 38h10"/><path d="M26 38l6-14 6 14M28 34h8"/>',
  target:'<circle cx="32" cy="32" r="24"/><circle cx="32" cy="32" r="14"/><circle cx="32" cy="32" r="4"/>',
  method:'<path d="M10 50 26 30l10 10 18-24"/><path d="M42 16h12v12"/>',
  org:'<rect x="8" y="12" width="48" height="42" rx="5"/><path d="M8 24h48M20 6v12M44 6v12M18 34h8M30 34h8M42 34h4M18 44h8M30 44h8"/>',
  clock:'<circle cx="32" cy="32" r="24"/><path d="M32 18v14l10 6"/>',
  globe:'<circle cx="32" cy="32" r="24"/><path d="M8 32h48M32 8c8 8 8 40 0 48M32 8c-8 8-8 40 0 48"/>',
  vr:'<path d="M8 22h48v22H40l-4-6h-8l-4 6H8z"/><circle cx="20" cy="32" r="4"/><circle cx="44" cy="32" r="4"/>',
  chart:'<path d="M10 54V10M10 54h44"/><rect x="18" y="34" width="8" height="14"/><rect x="32" y="24" width="8" height="24"/><rect x="46" y="14" width="8" height="34"/>',
  nowifi:'<path d="M8 24a34 34 0 0 1 48 0M16 32a22 22 0 0 1 32 0M24 40a10 10 0 0 1 16 0"/><circle cx="32" cy="50" r="2.5"/><path d="M10 8l44 48"/>',
  user:'<circle cx="26" cy="20" r="10"/><path d="M8 54c0-11 8-18 18-18s18 7 18 18"/><path d="M46 18a7 7 0 1 1 7 7v5M53 38v1"/>'
};
const ic = (k,cls='ico') => `<svg class="${cls}" viewBox="0 0 64 64">${ICON[k]}</svg>`;

// people pictogram for formats
const person = (x,y,c,s=1) => `<g transform="translate(${x},${y}) scale(${s})"><circle cx="0" cy="-26" r="11" fill="${c}"/><path d="M-18 8c0-14 8-22 18-22s18 8 18 22z" fill="${c}"/></g>`;
const laptop = (x,y,s=1) => `<g transform="translate(${x},${y}) scale(${s})" fill="none" stroke="#67e8f9" stroke-width="3"><rect x="-26" y="-34" width="52" height="34" rx="4"/><path d="M-34 6h68"/></g>`;
const board = (x,y) => `<g transform="translate(${x},${y})"><rect x="-60" y="-50" width="120" height="70" rx="6" fill="none" stroke="#c4b5fd" stroke-width="3"/><path d="M-40 -28h50M-40 -12h80" stroke="#c4b5fd" stroke-width="3"/></g>`;

Object.assign(ICON, {
  search:'<circle cx="27" cy="27" r="16"/><path d="M39 39l16 16"/>',
  chat:'<path d="M8 12h36v24H24l-10 9v-9H8z"/><path d="M48 24h8v22h-6v8l-9-8H30v-6"/>',
  check:'<rect x="8" y="8" width="48" height="48" rx="8"/><path d="M18 33l9 9 19-20"/>',
  play:'<rect x="6" y="12" width="52" height="40" rx="6"/><path d="M27 22v20l16-10z"/>',
  text:'<path d="M14 8h26l12 12v36H14z"/><path d="M40 8v12h12M22 30h22M22 38h22M22 46h14"/>',
  img:'<rect x="8" y="12" width="48" height="40" rx="5"/><circle cx="22" cy="26" r="5"/><path d="M8 46l16-14 12 10 8-6 12 10"/>',
  audio:'<path d="M10 26h10l14-12v36L20 38H10z"/><path d="M42 22a12 12 0 0 1 0 20M48 16a20 20 0 0 1 0 32"/>',
  av:'<rect x="6" y="14" width="40" height="36" rx="5"/><path d="M46 26l12-8v28l-12-8z"/><path d="M14 40a8 8 0 0 1 16 0"/>',
  lab:'<path d="M24 8h16M28 8v18L12 52a4 4 0 0 0 4 6h32a4 4 0 0 0 4-6L36 26V8"/><path d="M18 42h28"/>',
  vr:'<path d="M6 22h52v22H40l-4-6h-8l-4 6H6z"/><circle cx="19" cy="33" r="4"/><circle cx="45" cy="33" r="4"/>',
  phone:'<rect x="18" y="6" width="28" height="52" rx="5"/><path d="M28 50h8"/><path d="M26 22l4 4 8-8"/>',
  sheet:'<rect x="10" y="6" width="44" height="52" rx="5"/><path d="M18 18h28M18 28h8M30 28h16M18 38h8M30 38h16M18 48h20"/>',
  team:'<circle cx="20" cy="20" r="7"/><circle cx="44" cy="20" r="7"/><path d="M6 50c0-9 6-16 14-16s14 7 14 16M30 50c0-9 6-16 14-16s14 7 14 16"/>',
  slide:'<rect x="6" y="10" width="52" height="34" rx="4"/><path d="M32 44v10M22 56h20M14 20h20M14 28h28"/>',
  target:'<circle cx="32" cy="32" r="24"/><circle cx="32" cy="32" r="14"/><circle cx="32" cy="32" r="4"/>',
  wheel:'<circle cx="32" cy="32" r="24"/><circle cx="32" cy="32" r="7"/><path d="M32 8v17M32 39v17M8 32h17M39 32h17M15 15l12 12M37 37l12 12M15 49l12-12M37 27l12-12"/>',
  game:'<path d="M14 22h36a10 10 0 0 1 10 10v8a6 6 0 0 1-11 3l-5-6H20l-5 6a6 6 0 0 1-11-3v-8a10 10 0 0 1 10-10z"/><path d="M18 30v8M14 34h8"/><circle cx="44" cy="31" r="2"/><circle cx="48" cy="37" r="2"/>',
  ai:'<rect x="16" y="16" width="32" height="32" rx="6"/><path d="M26 6v10M38 6v10M26 48v10M38 48v10M6 26h10M6 38h10M48 26h10M48 38h10"/><path d="M26 38l6-14 6 14M28 34h8"/>'
});
const pill = (t,c='') => `<span class="pill" ${c?`style="color:${c};border-color:${c}88;background:${c}14"`:''}>${t}</span>`;
const banner = (icon,title,sub,c='#5eead4') => `${ic(icon)}<div><div style="font-family:'Inter Display';font-weight:800;font-size:30px">${title}</div>${sub?`<div style="font-size:23px;color:#ddd6fe;margin-top:2px">${sub}</div>`:''}</div>`;
const bannerBox = (top,sub,d,inner,c='#5eead4') => `<div class="abs" style="left:100px;top:${top}px;width:1180px;padding:20px 30px;border-radius:18px;border:1.5px solid ${c};background:linear-gradient(90deg,${c}2e,rgba(139,92,246,.12));display:flex;align-items:center;gap:22px" data-sub="${sub}" data-d="${d}" data-fx="up">${inner}</div>`;
const card3 = (items) => items.map((c,i)=> !c ? '' : `
  <div class="card" style="left:${100+i*400}px;top:${c[4]||300}px;width:370px;height:${c[5]||250}px;padding:24px 28px" data-sub="${c[3]}" data-d="${c[6]||0.3}" data-fx="up">
    <div style="display:flex;gap:18px;align-items:center">${ic(c[0])}<h3 style="margin:0 0 14px">${c[1]}</h3></div><p>${c[2]}</p></div>`).join('');

const SCENES = [];
SCENES.push(
 { id:'intro', chip:'', title:'', bubble:'', pose:'none', html:`
   <div class="abs" style="left:100px;top:130px;width:1020px">
     <div class="chip" data-sub="0" data-d="0" data-fx="left"><i></i>Завершающая мини-лекция серии</div>
     <div class="h1" style="font-size:72px;margin-top:36px" data-sub="0" data-d="0.15" data-fx="up">Дизайн ЭОР:<br>от <em>педагогических принципов</em><br>до <em>игровых механик</em></div>
     <div style="margin-top:40px">
       ${['педагогический дизайн','геймификация','эмоциональный дизайн'].map((t,i)=>`<span data-sub="1" data-d="${0.8+i*1.4}" data-fx="pop" style="display:inline-block">${pill(t,i==1?'#f472b6':i==2?'#a78bfa':'')}</span>`).join('')}
     </div>
   </div>
   <div class="win" style="left:1160px;top:150px;width:670px;height:604px" data-sub="0" data-d="0.3" data-fx="win">
     <div class="bar"><b style="background:#f472b6"></b><b style="background:#facc15"></b><b style="background:#4ade80"></b><span>EDU_DESIGN.EXE</span></div>
     <img src="assets/holo_win.jpg" style="left:-40px;width:750px;top:46px">
   </div>`},
 { id:'s4', chip:'04 · Педагогический дизайн', title:'Сначала <em>цель</em>, потом сервис', bubble:'Как выбрать нужный сервис?', pose:'side', html:`
   ${['Запоминание','Понимание','Применение','Анализ','Оценка','Создание'].map((t,i)=>{const c=['#c4b5fd','#a78bfa','#8b5cf6','#67e8f9','#5eead4','#4ade80'][i]; return `
     <div class="abs" style="left:${100+i*60}px;top:${560-i*52}px;width:${480}px;height:46px;border-radius:10px;background:${c}2a;border:1.5px solid ${c};display:flex;align-items:center;padding-left:18px;font-weight:700;font-size:23px;color:#f5f3ff" data-sub="0" data-d="${2.6+i*0.6}" data-fx="left"><span style="font-family:'DejaVu Sans Mono';color:${c};margin-right:12px">${i+1}</span>${t}</div>`}).join('')}
   <div class="abs" style="left:100px;top:620px;font-size:23px;color:var(--mute)" data-sub="0" data-d="1.2" data-fx="fade">таксономия Блума ↗</div>
   <div class="card" style="left:780px;top:290px;width:500px;height:230px;padding:26px" data-sub="1" data-d="0.4" data-fx="up">
     <div style="display:flex;gap:18px;align-items:center">${ic('wheel')}<h3 style="margin:0 0 14px">«Падагогическое колесо»</h3></div>
     <p>А. Каррингтон: приложения по уровням целей обучения</p></div>
   ${bannerBox(680,2,0.4,`<div style="font-family:'Inter Display';font-weight:800;font-size:34px">«Суть не в приложениях, суть — в <span style="color:#5eead4">педагогике</span>»</div>`,'#a78bfa')}`},
 { id:'outro', chip:'', title:'', bubble:'', pose:'none', html:`
   <div class="abs" style="left:100px;top:150px;width:1020px">
     <div class="chip" data-sub="0" data-d="0" data-fx="left"><i></i>Вопрос для обсуждения</div>
     <div class="h1" style="font-size:66px;margin-top:40px" data-sub="0" data-d="0.2" data-fx="up">Какой <em>электронный ресурс</em><br>вы создали бы для своих<br>будущих воспитанников?</div>
     <div style="margin-top:44px" data-sub="1" data-d="0.2" data-fx="up"><span class="pill">спасибо за серию!</span><span class="pill" style="color:var(--pink);border-color:rgba(244,114,182,.5);background:rgba(244,114,182,.08)">до встречи на практикуме!</span></div>
   </div>
   <div class="win" style="left:1160px;top:150px;width:670px;height:604px" data-sub="0" data-d="0.3" data-fx="win">
     <div class="bar"><b style="background:#f472b6"></b><b style="background:#facc15"></b><b style="background:#4ade80"></b><span>SEE_YOU.EXE</span></div>
     <img src="assets/holo_win.jpg" style="left:-40px;width:750px;top:46px">
   </div>`}
);
const SUBS = __SUBS__; // [[sceneId,[sub0,sub1,...]],...] from subs.json, same order as SCENES
SCENES.forEach((s,i)=>{ s.subs = SUBS[i][1]; });

// ---------------- timing ----------------
const FPS = 25;
const subDur = s => Math.max(3.6, s.length/15.5 + 1.0);
let T = 0.4; const TL = [];
const FIXED = null;
SCENES.forEach((sc,si)=>{
  if (FIXED){ const F=FIXED[si]; TL.push({sc,start:F.start,end:F.end,subs:F.subs.map((x,j)=>({text:sc.subs[j],t0:x[0],t1:x[1]}))}); T=F.end; return; }
  const start = T; const lead = si===0 ? 0.6 : 1.2; let t = start + lead; const subs = [];
  sc.subs.forEach(s=>{ const d = subDur(s); subs.push({text:s,t0:t,t1:t+d}); t += d; });
  const end = t + 0.5;
  TL.push({sc,start,end,subs}); T = end;
});
const DURATION = T + 1.6;
window.__meta = {DURATION, FPS, TL: TL.map(x=>({id:x.sc.id,start:x.start,end:x.end,subs:x.subs}))};

// ---------------- build DOM ----------------
const scenesEl = document.getElementById('scenes');
TL.forEach((S,i)=>{
  const d = document.createElement('div'); d.className='scene'; d.id='sc_'+S.sc.id;
  let head = '';
  if (S.sc.title) head = `<div class="head"><div class="chip" data-hd="0"><i></i>${S.sc.chip}</div><div class="h1" data-hd="1">${S.sc.title}</div></div>`;
  d.innerHTML = head + S.sc.html; scenesEl.appendChild(d);
  S.el = d;
  S.items = [...d.querySelectorAll('[data-sub],[data-hd]')].map(e=>{
    let a;
    if (e.dataset.hd!==undefined) a = S.start + 0.6 + (+e.dataset.hd)*0.2;
    else a = S.subs[+e.dataset.sub].t0 + (+e.dataset.d||0) - 0.35;
    return {e, a, fx: e.dataset.fx || (e.dataset.hd!==undefined ? (e.dataset.hd==='0'?'left':'up') : 'up'), dur:+(e.dataset.dur||0)};
  });
});
// progress ticks
const prog = document.getElementById('prog');
TL.forEach((S,i)=>{ if(i===0) return; const k=document.createElement('div'); k.className='tick'; k.style.left=(S.start/DURATION*100)+'%'; prog.appendChild(k); S.tick=k; });

// ---------------- easing ----------------
const cl = (x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eo = x=>1-Math.pow(1-x,3);
const eb = x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
const eio = x=> x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;

function applyFx(it,t){
  const {e,a,fx} = it; const D = fx==='grow' ? (it.dur||2) : 0.75;
  const p = cl((t-a)/D);
  let o=1, tr='';
  if (fx==='up'){ const q=eo(p); o=q; tr=`translateY(${(1-q)*40}px)`; }
  else if (fx==='left'){ const q=eo(p); o=q; tr=`translateX(${(1-q)*-50}px)`; }
  else if (fx==='scale'){ const q=eb(p); o=cl(p*2); tr=`scale(${0.6+0.4*q})`; }
  else if (fx==='pop'){ const q=eb(p); o=cl(p*3); tr=`scale(${q})`; }
  else if (fx==='grow'){ const q=eio(p); o=1; tr=`scaleX(${q})`; }
  else if (fx==='rise'){ const q=eb(p); o=cl(p*3); tr=`scaleY(${Math.max(0,q)})`; }
  else if (fx==='fade'){ o=eo(p); tr=''; }
  else if (fx==='win'){ const q=eo(p); o=q; tr=`perspective(1400px) rotateY(${(1-q)*-28}deg) translateX(${(1-q)*120}px) scale(${0.9+0.1*q})`; }
  e.style.opacity = o; e.style.transform = tr;
}

// hero elements
const hF=document.getElementById('heroFront'), hS=document.getElementById('heroSide'), rA=document.getElementById('robA'), rB=document.getElementById('robB');
const HERO = document.getElementById('hero');
const bubble=document.getElementById('bubble'), btext=document.getElementById('btext'), bcur=document.getElementById('bcur');
const subEl=document.getElementById('subtext'), subBox=document.getElementById('sub');
const fill=document.getElementById('progfill');
const g1=document.getElementById('g1'), g2=document.getElementById('g2'), dots=document.getElementById('dots');

function poseAt(t){ // returns opacity of front/side/none blend
  for (const S of TL){ if (t < S.end) return S; } return TL[TL.length-1];
}

window.render = function(t){
  // background drift
  g1.style.transform = `translate(${Math.sin(t*0.21)*60}px,${Math.cos(t*0.17)*40}px)`;
  g2.style.transform = `translate(${Math.cos(t*0.13)*80}px,${Math.sin(t*0.19)*30}px)`;
  dots.style.transform = `translate(${(t*6)%36}px,${(t*3)%36}px)`;
  fill.style.transform = `scaleX(${cl(t/DURATION)})`;

  TL.forEach((S,i)=>{
    if (S.tick) S.tick.classList.toggle('on', t >= S.start);
    const vis = t >= S.start-0.05 && (t < S.end + 0.7 || i===TL.length-1);
    S.el.style.display = vis ? 'block' : 'none';
    if (!vis) return;
    const q = cl((t - S.end)/0.6);  // exit
    const isLast = i===TL.length-1;
    const ex = isLast ? 0 : eio(q);
    S.el.style.opacity = 1-ex; S.el.style.transform = `translateY(${-30*ex}px)`;
    S.items.forEach(it=>applyFx(it,t));
  });

  // current scene
  let cur = TL.findIndex(S=> t < S.end); if (cur<0) cur = TL.length-1;
  const S = TL[cur];
  // subtitles
  let sub = null; for (const s of S.subs){ if (t>=s.t0-0.15 && t< s.t1) sub=s; }
  if (!sub){ // gap
    subBox.style.opacity = 0;
  } else {
    subEl.textContent = sub.text;
    const a = cl((t-sub.t0+0.15)/0.3), b = cl((sub.t1-t)/0.25);
    subBox.style.opacity = Math.min(a,b);
    subBox.style.transform = `translateY(${(1-eo(a))*12}px)`;
  }

  // hero pose weights with crossfade around scene boundaries
  const w = {front:0, side:0, none:0};
  const poseOf = k => TL[k].sc.pose;
  const prev = cur>0 ? TL[cur-1] : null;
  const k = prev ? cl((t - prev.end)/0.7) : 1;
  w[poseOf(cur)] += eio(k); if (prev) w[poseOf(cur-1)] += 1-eio(k);
  const heroVis = w.front + w.side;
  const bob = Math.sin(t*1.6)*7;
  const hop = prev ? Math.sin(Math.PI*cl((t-prev.end)/0.7))*-18 : 0;
  const sc = 1.15;
  hF.style.cssText = `left:60px;bottom:-40px;width:${414*sc}px;opacity:${w.front};transform:translateY(${bob+hop+(1-w.front)*30}px)`;
  hS.style.cssText = `left:110px;bottom:-30px;width:${351*sc}px;opacity:${w.side};transform:translateY(${bob+hop+(1-w.side)*30}px)`;
  const ra = 0.9*heroVis;
  rA.style.cssText = `left:${410+Math.sin(t*0.7)*12}px;top:${600+Math.sin(t*1.1+1)*18}px;width:150px;opacity:${ra};transform:rotate(${Math.sin(t*0.9)*5}deg)`;
  rB.style.cssText = `left:${-5+Math.cos(t*0.6)*10}px;top:${450+Math.sin(t*0.95)*20}px;width:92px;opacity:${ra};transform:rotate(${Math.cos(t*0.8)*6}deg)`;
  HERO.style.opacity = 1;

  // bubble typewriter
  const bq = S.sc.bubble;
  if (bq){
    const t0 = S.start + 0.75; const n = Math.floor(cl((t-t0)/1.4)*bq.length);
    const inA = cl((t-t0+0.05)/0.35), outA = 1-cl((t-S.end+0.1)/0.35);
    const o = Math.min(inA,outA);
    bubble.style.opacity = o; bubble.style.transform = `scale(${0.85+0.15*eb(inA)})`; bubble.style.transformOrigin='100% 100%';
    btext.textContent = bq.slice(0,n);
    bcur.style.opacity = (n<bq.length || Math.floor(t*2)%2===0) ? 1 : 0;
  } else bubble.style.opacity = 0;
};
window.render(0);
</script>
</body>
</html>
```

### cutout.py — вырезка героя из серого фона
```python
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
```

### split.py — разделение на героя и роботов
```python
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
```

### voice_align.py
```python
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
```

### build_timing.py
```python
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
```

### music.py — фоновый эмбиент (аргументы: длительность, путь)
```python
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
```

### render.js — покадровый рендер (Playwright → ffmpeg)
```js
const { chromium } = require('playwright'); const { spawn } = require('child_process');
(async()=>{
  const [,,html,out,f0,f1]=process.argv;
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+html); await p.waitForTimeout(800);
  const {FPS}=await p.evaluate(()=>window.__meta);
  const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out],{stdio:['pipe','inherit','inherit']});
  for(let f=+f0;f<+f1;f++){
    await p.evaluate(t=>window.render(t),f/FPS);
    const buf=await p.screenshot({type:'jpeg',quality:93});
    if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
    if(f%250===0) console.log(out,f);
  }
  ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close();
})();
```

### still.js — стоп-кадры для проверки
```js
const { chromium } = require('playwright');
(async()=>{
  const [,,html,out,...ts]=process.argv;
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+html); await p.waitForTimeout(500);
  const meta=await p.evaluate(()=>window.__meta); console.log('DURATION',meta.DURATION.toFixed(1));
  meta.TL.forEach(x=>console.log(x.id,x.start.toFixed(1),x.end.toFixed(1)));
  for(const t of ts){ await p.evaluate(t=>window.render(+t),t); await p.screenshot({path:`${out}/still_${t}.png`}); }
  await b.close();
})();
```
