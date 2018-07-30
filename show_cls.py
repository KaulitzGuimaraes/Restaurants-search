import pandas as pd

cluster = []

for i in range(0,5) :
    ds = pd.read_csv('cluster_'+str(i)+'.csv')
    cluster.append(ds)


for ds in cluster :
    print(ds.tail())
    print('--------------------------------------------')