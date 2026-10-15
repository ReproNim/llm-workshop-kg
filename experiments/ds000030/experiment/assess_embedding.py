from pathlib import Path
import json,csv,numpy as np
from sklearn.manifold import trustworthiness
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent;d=json.load((R/'results/embedding_input.json').open());runs=json.load((R/'results/umap_runs.json').open());X=np.array(d['X']);Y=np.array(runs[0]['embedding']);pca=PCA(n_components=2,random_state=42).fit_transform(X)
def nbr(y):return NearestNeighbors(n_neighbors=16).fit(y).kneighbors(y,return_distance=False)[:,1:]
base=nbr(Y);metrics=[]
for r in runs:
 z=np.array(r['embedding']);n=nbr(z);metrics.append({**{k:v for k,v in r.items() if k!='embedding'},'trustworthiness_k15':round(trustworthiness(X,z,n_neighbors=15),4),'mean_neighbor_overlap_with_seed42':round(np.mean([len(set(a)&set(b))/15 for a,b in zip(base,n)]),4)})
res={'n_participants':len(X),'n_features':X.shape[1],'imputed_cells':int(sum(d['missing_fraction'])*X.shape[1]+.5),'umap':metrics,'pca_trustworthiness_k15':round(trustworthiness(X,pca,n_neighbors=15),4),'caveat':'Exploratory unsupervised geometry, no subtype or causal inference; missingness, instrument weighting, demographics and scanner effects remain relevant.'}
json.dump(res,(R/'results/embedding_assessment.json').open('w'),indent=2)
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False});fig,axs=plt.subplots(1,3,figsize=(15,4.5));groups=np.array([r['diagnosis'] for r in d['participants']]);colors={'CONTROL':'#167d8d','SCHZ':'#bd4f2f','BIPOLAR':'#875c9c','ADHD':'#b99121'}
for name,c in colors.items():
 k=groups==name;axs[0].scatter(Y[k,0],Y[k,1],s=19,c=c,label=name,alpha=.8)
axs[0].legend(fontsize=8);axs[0].set_title('UMAP colored by recorded diagnosis')
sc=axs[1].scatter(Y[:,0],Y[:,1],s=19,c=[int(p['age']) for p in d['participants']],cmap='viridis');fig.colorbar(sc,ax=axs[1],label='Age (years)');axs[1].set_title('Same embedding colored by age')
for name,c in colors.items():
 k=groups==name;axs[2].scatter(pca[k,0],pca[k,1],s=19,c=c,alpha=.8)
axs[2].set_title('PCA comparison, same input matrix')
for i,ax in enumerate(axs):ax.set_xlabel('UMAP 1' if i<2 else 'PC 1');ax.set_ylabel('UMAP 2' if i<2 else 'PC 2')
fig.suptitle('272 participants, 10 behavioral/cognitive scores; diagnosis excluded from inputs',fontsize=14);fig.tight_layout();fig.savefig(R/'results/phenotype_embedding.png',dpi=180);fig.savefig(R/'results/phenotype_embedding.pdf')
with (R/'results/participant_embedding.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['participant_id','diagnosis','age','gender','scanner','umap1','umap2','pca1','pca2','missing_fraction'])
 for i,p in enumerate(d['participants']):w.writerow([p['participant_id'],p['diagnosis'],p['age'],p['gender'],p['ScannerSerialNumber'],*Y[i],*pca[i],d['missing_fraction'][i]])
print(json.dumps(res,indent=2))
