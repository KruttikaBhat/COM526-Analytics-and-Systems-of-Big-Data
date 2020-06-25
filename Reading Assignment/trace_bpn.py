import pandas as pd
import numpy as np
from sklearn import preprocessing

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) *(1-sigmoid (x))


#load data
data=pd.read_csv('golf.csv')

#encode the data
encoded_data=data.copy()
encoded_data.head()
for col in encoded_data.head():
    encoded_data[col]=encoded_data[col].astype('category')
    encoded_data[col] = encoded_data[col].cat.codes

#normalize the encoded values
x = encoded_data.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
data = pd.DataFrame(x_scaled)

#extract feature set and labels
feature_set=data.iloc[:,0:2].to_numpy()
labels=data.iloc[:,2].to_numpy()
labels = labels.reshape(13, 1)

#Everything below this point is the same as BPN.py, but only 1 epoch is done. If you run this then the values will be different
#from what is shown in the Report as the weights are initialised randomly. That is why a pdf of the jupyter notebook is included.

wh = np.random.rand(len(feature_set[0]),4)
wo = np.random.rand(4, 1)
lr = 0.5

# feedforward
zh = np.dot(feature_set, wh)
ah = sigmoid(zh)

zo = np.dot(ah, wo)
ao = sigmoid(zo)

# Phase1 =======================

error_out = ((1 / 2) * (np.power((ao - labels), 2)))
print(error_out.sum())


dcost_dao = ao - labels
dao_dzo = sigmoid_der(zo)
dzo_dwo = ah
dcost_wo = np.dot(dzo_dwo.T, dcost_dao * dao_dzo)

# Phase 2 =======================
dcost_dzo = dcost_dao * dao_dzo
dzo_dah = wo
dcost_dah = np.dot(dcost_dzo , dzo_dah.T)


dah_dzh = sigmoid_der(zh)
dzh_dwh = feature_set
dcost_wh = np.dot(dzh_dwh.T, dah_dzh * dcost_dah)

# Update Weights ================

wh -= lr * dcost_wh
wo -= lr * dcost_wo
