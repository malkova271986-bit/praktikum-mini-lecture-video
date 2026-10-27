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
