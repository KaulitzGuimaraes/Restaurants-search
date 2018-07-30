import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import  pandas as pd
import  numpy as np
# Some data
N_CLUSTER = 4
c0 = pd.read_csv('cluster_'+str(N_CLUSTER)+'.csv')
c0 = c0.fillna(0)
c0  = c0.drop(c0.columns[0], axis=1)
labels =pd.read_csv('red-rec.csv').columns.values

fracs = c0.values

dict_1 = dict()
for label in labels :
    dict_1[label] = 0
age = []
for row in fracs :
    for element in row :
        if element != 0:
         dict_1[element] +=1

for label in dict_1 :

     age.append(dict_1[label])

plt.pie(age,labels=labels, autopct='%.0f%%', radius=1.0)
plt.title('CLUSTER ' + str(N_CLUSTER))
plt.show()