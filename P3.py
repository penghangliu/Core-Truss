
# coding: utf-8

# In[18]:


import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
#plt.switch_backend('agg')
import math

#file = 'DBLP_dbs.txt'
file = sys.argv[1]
title = file[0:len(file)-4]


# In[19]:


df = pd.read_csv(file, sep="\t", header=None)
df.columns = ['id','core', 'deg', 'mean_truss', 'std_truss', 'min_truss','max_truss', 'mean_tri', 'std_tri', 'min_tri', 'max_tri']


# In[26]:

df1 = df.groupby(['core']).mean()
df2 = df.groupby(['core']).quantile(0.75)
df3 = df.groupby(['core']).quantile(0.25)

fig,ax = plt.subplots(figsize=(7,5))
ax.fill_between(df1.index,df2.max_truss,df3.max_truss,color='salmon', alpha=0.6)
ax.fill_between(df1.index,df2.min_truss,df3.min_truss,color='lightskyblue', alpha=0.6)
ax.plot(df1.max_truss,color='red')
ax.plot(df1.min_truss,color='blue')
plt.legend(loc='upper left', fontsize=25)
ax.set_ylabel('Truss Number', fontsize=40)
ax.set_xlabel('Core Number', fontsize=40)
ax.tick_params(labelsize=30)
plt.savefig('CoreTruss_' + title + '.png')

df1 = df.groupby(['core']).mean()
df2 = df.groupby(['core']).quantile(0.75)
df3 = df.groupby(['core']).quantile(0.25)

fig,ax = plt.subplots(figsize=(7,5))
ax.fill_between(df1.index,df2.max_tri,df3.max_tri,color='salmon', alpha=0.6)
ax.fill_between(df1.index,df2.min_tri,df3.min_tri,color='lightskyblue', alpha=0.6)
ax.plot(df1.max_tri,color='red')
ax.plot(df1.min_tri,color='blue')
plt.legend(loc='upper left', fontsize=25)
ax.set_ylabel('Truss Number', fontsize=40)
ax.set_xlabel('Core Number', fontsize=40)
ax.tick_params(labelsize=30)
plt.savefig('CoreTri_' + title + '.png')

df1 = df.groupby(['deg']).mean()
df2 = df.groupby(['deg']).quantile(0.75)
df3 = df.groupby(['deg']).quantile(0.25)

fig,ax = plt.subplots(figsize=(7,5))
ax.fill_between(df1.index,df2.max_truss,df3.max_truss,color='salmon', alpha=0.6)
ax.fill_between(df1.index,df2.min_truss,df3.min_truss,color='lightskyblue', alpha=0.6)
ax.plot(df1.max_truss,color='red')
ax.plot(df1.min_truss,color='blue')
plt.legend(loc='upper left', fontsize=25)
ax.set_ylabel('Truss Number', fontsize=40)
ax.set_xlabel('Core Number', fontsize=40)
ax.tick_params(labelsize=30)
plt.savefig('DegTruss_' + title + '.png')

df1 = df.groupby(['deg']).mean()
df2 = df.groupby(['deg']).quantile(0.75)
df3 = df.groupby(['deg']).quantile(0.25)

fig,ax = plt.subplots(figsize=(7,5))
ax.fill_between(df1.index,df2.max_tri,df3.max_tri,color='salmon', alpha=0.6)
ax.fill_between(df1.index,df2.min_tri,df3.min_tri,color='lightskyblue', alpha=0.6)
ax.plot(df1.max_tri,color='red')
ax.plot(df1.min_tri,color='blue')
plt.legend(loc='upper left', fontsize=25)
ax.set_ylabel('Truss Number', fontsize=40)
ax.set_xlabel('Core Number', fontsize=40)
ax.tick_params(labelsize=30)
plt.savefig('DegTri_' + title + '.png')
