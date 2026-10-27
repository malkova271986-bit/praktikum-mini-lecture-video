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
