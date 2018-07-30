import pandas as pd
import numpy as np

N_SAMPLES = 1000
data_set_header_2 =np.array(['pizza','fit','japanese','italian','fast food','hamburger','rock','pop','country','no music','live'])
data_set_header_1 =  np.array(['young','adult','elder'])

age_data = np.zeros((N_SAMPLES,len(data_set_header_1)),dtype=np.int32)

age_options = np.array([1,0,0],dtype=np.int32)
for i in range(0,len(age_data)) :

    age_data[i] = age_options
    np.random.shuffle ( age_data[i] )



data = np.random.randint ( 2 , size=(N_SAMPLES,len(data_set_header_2)) )

data_set_1 = pd.DataFrame(data=age_data,columns=data_set_header_1)
data_set_2 = pd.DataFrame(data=data,columns=data_set_header_2)


data_set = pd.concat([data_set_1,data_set_2],axis=1)

data_set.to_csv('red-rec.csv')

