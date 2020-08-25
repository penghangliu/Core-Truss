import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import math

#file = 'data/Orkut.txt'
file = sys.argv[1]
title = file[5:len(file)-4]
# title = 'BerkStan'

f = open(file, 'r') 
lines = f.readlines()
truss = []
tri = []
L_deg = []
S_deg = []
L_core = []
S_core = []
for line in lines:
    p = line.split()
    truss.append(int(p[2]))
    tri.append(int(p[3]))
    S_deg.append(min(int(p[4]),int(p[5])))
    L_deg.append(max(int(p[4]),int(p[5])))
    S_core.append(min(int(p[6]),int(p[7])))
    L_core.append(max(int(p[6]),int(p[7])))
f.close()
truss = np.array(truss)
tri = np.array(tri)
S_deg = np.array(S_deg)
L_deg = np.array(L_deg)
S_core = np.array(S_core)
L_core = np.array(L_core)

d = {'tri': tri, 'truss': truss, 'deg1': S_deg, 'deg2': L_deg, 'core1': S_core, 'core2': L_core}
df = pd.DataFrame(data=d)

df1 = df.groupby(['deg1', 'deg2']).size().reset_index(name='counts')
df2 = df.groupby(['core1', 'core2']).size().reset_index(name='counts')
deg1 = df1['deg1'].values
deg2 = df1['deg2'].values
deg_count = df1['counts'].values
core1 = df2['core1'].values
core2 = df2['core2'].values
core_count = df2['counts'].values

deg_tri_avg = np.array(df.groupby(['deg1', 'deg2']).mean()['tri'])
deg_tri_std = np.array(df.groupby(['deg1', 'deg2']).std()['tri'])
deg_truss_avg = np.array(df.groupby(['deg1', 'deg2']).mean()['truss'])
deg_truss_std = np.array(df.groupby(['deg1', 'deg2']).std()['truss'])
deg_tri_std = np.nan_to_num(deg_tri_std)
deg_truss_std = np.nan_to_num(deg_truss_std)

core_tri_avg = np.array(df.groupby(['core1', 'core2']).mean()['tri'])
core_tri_std = np.array(df.groupby(['core1', 'core2']).std()['tri'])
core_truss_avg = np.array(df.groupby(['core1', 'core2']).mean()['truss'])
core_truss_std = np.array(df.groupby(['core1', 'core2']).std()['truss'])
core_tri_std = np.nan_to_num(core_tri_std)
core_truss_std = np.nan_to_num(core_truss_std)

x1 = core1
y1 = core2
x2 = deg1
y2 = deg2
z1 = core_truss_avg
z2 = deg_truss_avg
z3 = core_tri_avg
z4 = deg_tri_avg

idx1 = z1.argsort()
idx2 = z2.argsort()
idx3 = z3.argsort()
idx4 = z4.argsort()

lsize = 20
tsize = 15

fig, ((ax0,ax1),(ax2,ax3)) = plt.subplots(nrows=2,ncols=2,figsize=(15,10))
c0 = ax0.scatter(x1[idx1], y1[idx1], c=z1[idx1], cmap='YlOrRd', vmin=z1.min(), vmax=z1.max())
c1 = ax1.scatter(x2[idx2], y2[idx2], c=z2[idx2], cmap='YlOrRd', vmin=z2.min(), vmax=z2.max())
c2 = ax2.scatter(x1[idx3], y1[idx3], c=z3[idx3], cmap='YlGnBu', vmin=z3.min(), vmax=z3.max())
c3 = ax3.scatter(x2[idx4], y2[idx4], c=z4[idx4], cmap='YlGnBu', vmin=z4.min(), vmax=z4.max())

cb3 = fig.colorbar(c0, ax=ax0)
cb1 = fig.colorbar(c1, ax=ax1)
cb4 = fig.colorbar(c2, ax=ax2)
cb2 = fig.colorbar(c3, ax=ax3)
cb1.set_label(label='Truss Number', size=lsize)
cb2.set_label(label='Triangle Count', size=lsize)
cb3.set_label(label='Truss Number', size=lsize)
cb4.set_label(label='Triangle Count', size=lsize)
cb3.ax.tick_params(labelsize=tsize)
cb4.ax.tick_params(labelsize=tsize)
cb1.ax.tick_params(labelsize=tsize)
cb2.ax.tick_params(labelsize=tsize)

ax0.set(xlabel='Core Number', ylabel='Core Number', xscale='log', yscale='log')
ax0.yaxis.label.set_size(lsize)
ax0.xaxis.label.set_size(lsize)
maxx = round(math.log(ax0.get_ylim()[1],10),1)
ax0.plot([0,10**maxx], [0,10**maxx], '-', lw = 0.6, color = 'black')
ax0.set_xlim(0.8, 10**maxx)
ax0.set_ylim(0.8, 10**maxx)
ax0.tick_params(axis="x", labelsize=tsize)
ax0.tick_params(axis="y", labelsize=tsize)

ax1.set(xlabel='Degree', ylabel='Degree', xscale='log', yscale='log')
ax1.yaxis.label.set_size(lsize)
ax1.xaxis.label.set_size(lsize)
maxx = round(math.log(ax1.get_ylim()[1],10),1)
ax1.plot([0,10**maxx], [0,10**maxx], '-', lw = 0.6, color = 'black')
ax1.set_xlim(0.8, 10**maxx)
ax1.set_ylim(0.8, 10**maxx)
ax1.tick_params(axis="x", labelsize=tsize)
ax1.tick_params(axis="y", labelsize=tsize)

ax2.set(xlabel='Core Number', ylabel='Core Number', xscale='log', yscale='log')
ax2.yaxis.label.set_size(lsize)
ax2.xaxis.label.set_size(lsize)
maxx = round(math.log(ax2.get_ylim()[1],10),1)
ax2.plot([0,10**maxx], [0,10**maxx], '-', lw = 0.6, color = 'black')
ax2.set_xlim(0.8, 10**maxx)
ax2.set_ylim(0.8, 10**maxx)
ax2.tick_params(axis="x", labelsize=tsize)
ax2.tick_params(axis="y", labelsize=tsize)

ax3.set(xlabel='Degree', ylabel='Degree', xscale='log', yscale='log')
ax3.yaxis.label.set_size(lsize)
ax3.xaxis.label.set_size(lsize)
maxx = round(math.log(ax3.get_ylim()[1],10),1)
ax3.plot([0,10**maxx], [0,10**maxx], '-', lw = 0.6, color = 'black')
ax3.set_xlim(0.8, 10**maxx)
ax3.set_ylim(0.8, 10**maxx)
ax3.tick_params(axis="x", labelsize=tsize)
ax3.tick_params(axis="y", labelsize=tsize)

#fig.suptitle(title + ' (mean)', fontsize=20)
#plt.show()
fig.savefig(title + '.png',dpi=144)
print(title + ' ' + 'complete!')


