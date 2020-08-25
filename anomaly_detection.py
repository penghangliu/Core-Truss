import numpy as np
import pandas as pd
from scipy.stats import entropy
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys

file = sys.argv[1]
title = file[6:len(file)-4]

#threshold


core = []
with open(file) as f:
    lines=f.readlines()
    for line in lines:
        myarray = np.fromstring(line, dtype=int, sep='\t')
        core.append(myarray[1])

CORE = np.sort(np.array(core))

a = CORE[int(CORE.shape[0]/4)+1]

#read file

T = []
ID = []
core = []
deg = []
MT = []
with open(file) as f:
    lines=f.readlines()
    for line in lines:
        myarray = np.fromstring(line, dtype=int, sep='\t')
        if myarray[1] >= a:
            ID.append(myarray[0])
            core.append(myarray[1])
            deg.append(myarray[2])
            myarray = np.delete(myarray, [0,1,2])
            T.append(myarray)
            MT.append(max(myarray))

K = []
for i in T:
    for j in i:
        K.append(j)
K = np.unique(K)

D = []
for t in T:
    d = []
    a = t.tolist()
    for k in K:
        n = a.count(k)
        d.append(n)
    D.append(d)

for d in D:
    s = sum(d)
    if s!=0:
        for i in range(len(d)):
            d[i] = d[i]/s

D = np.array(D)

#elbow method

sse = {}
for k in range(1, 35):
    kmeans = KMeans(n_clusters=k).fit(D)
    sse[k] = kmeans.inertia_
fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(10,7))
ax.plot(list(sse.keys()), list(sse.values()))
ax.set_xlabel("Number of cluster", fontsize=30)
ax.tick_params(axis = 'x',labelsize=15)
ax.tick_params(axis = 'y',labelsize=10)
ax.set_ylabel("Sum of squared error", fontsize=30)
fig.savefig('elbow_'+title+'.png',dpi=100)


#k means

kmeans = KMeans(n_clusters=15).fit(D) #please change the parameter based on the elbow plot

out = kmeans.labels_


d = {'node id': ID, 'core': core, 'degree': deg, 'cluster': out, 'max truss': MT}
df = pd.DataFrame(data=d)

#anomaly detection

nc = df['cluster'].unique().shape[0]

cores = np.sort(df['core'].unique())

out = pd.DataFrame()
pp = PdfPages(title + '.pdf')
for i in range(nc):
    df1 = df[df['cluster']==i].reset_index(drop=True)
    
    m = df1['core'].mean()
    std = df1['core'].std()
    Z = []
    outlier = []
    for j in df1['core']:
        score = (j-m)/std
        Z.append(score)
        if score > 2:
            outlier.append(True)
        else:
            outlier.append(False)
    df1['z-score'] = Z
    df1['outlier'] = outlier
    out = pd.concat([out, df1])
    
    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(10,6))
    ax.hist(df1['core'], bins = cores)
    ax.set_xlabel('Core number', fontsize=25)
    ax.tick_params(labelsize=15)
    ax.set_ylabel('Cluster' + ' ' + str(i), fontsize=25)
    pp.savefig(fig)
pp.close()

out.to_csv('out_'+title+'.csv',columns=['cluster','node id','core','degree','max truss','z-score','outlier'],index=False)
