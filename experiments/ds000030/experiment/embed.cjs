const fs=require('fs');global.window={};const {UMAP}=require('./vendor/umap-js.cjs');
const d=JSON.parse(fs.readFileSync(__dirname+'/results/embedding_input.json'));
function rng(seed){return function(){let t=seed+=0x6D2B79F5;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return ((t^t>>>14)>>>0)/4294967296}}
let runs=[];for(const [seed,neighbors] of [[42,15],[43,15],[44,15],[42,30]]){const u=new UMAP({nNeighbors:neighbors,minDist:.1,nComponents:2,nEpochs:500,random:rng(seed)});runs.push({seed,nNeighbors:neighbors,minDist:.1,nEpochs:500,metric:'euclidean',embedding:u.fit(d.X)});}
fs.writeFileSync(__dirname+'/results/umap_runs.json',JSON.stringify(runs));console.log(runs.map(r=>({seed:r.seed,n:r.embedding.length,neighbors:r.nNeighbors})));
