import  pandas as pd
from sklearn import  cluster
from sklearn import  metrics
import numpy as np
from scipy.spatial.distance import cdist

from matplotlib import pyplot as plt
CLUSTER = 5

#agrupamento
km = cluster.KMeans(n_clusters=CLUSTER)


ds = pd.read_csv('red-rec.csv')
ds = ds.drop(ds.columns[0], axis=1)


km.fit(ds.values)



data_set_header = np.array(['young','adult','elder','pizza','fit','japanese','italian','fast food','hamburger','rock','pop','country','no music','live'])

ds1 = []
for row in ds.values :

    row2 = []
    for i in range(0,14) :


        if row[i] == 1 :
            row2.append(data_set_header[i])
        elif row[i] == 0 :
            row2.append (np.nan)


    ds1.append(row2)



ds_k = dict()

for i in range(0,CLUSTER) :
    list_buffer = []
    ds_k[i] = list_buffer


n_row =0



for i in km.labels_ :

    ds_k[int(i)].append(ds1[n_row])

    n_row+=1
i =0


for dt_st in ds_k :
    dt = pd.DataFrame(ds_k[dt_st])
    dt.to_csv('cluster_'+str(dt_st)+'.csv')


'''
   




na = np.array([1,1,1,1,0,0,0,0,0,0,0,0,0,0])

na = na.reshape((1,-1))


for i in range(0,30) :
   np.random.shuffle(na[0])

   cl = km.predict ( na )
   print(cl)
   i+=1
   
   
   '''


