import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) *(1-sigmoid (x))

#load data
iris = pd.read_csv('iris.csv')

#remove 1 class and change the labels to integer values
iris = iris[iris['species']!='setosa']
iris['species'] = iris['species'].astype('category')
iris['species_cat'] = iris['species'].cat.codes

#take first 2 features
X = iris[['petal_length', 'petal_width']].values.T
Y = iris[['species_cat']].values.T
Y = Y.astype('uint8')

np.random.seed(0)
feature_set=X.reshape(X.shape[1],X.shape[0])

labels=Y
labels=labels.reshape(100)

#check the scatter plot
plt.figure(figsize=(10,7))
plt.scatter(feature_set[:,0], feature_set[:,1], c=labels, cmap=plt.cm.winter)
plt.title("IRIS DATA ",fontsize=20)
plt.xlabel('Petal Length',fontsize=20)
plt.ylabel('Petal Width',fontsize=20)
plt.show()
labels = labels.reshape(100, 1)

#intialise weight matrix
wh = np.random.rand(len(feature_set[0]),4)
wo = np.random.rand(4, 1)
lr = 0.5

for epoch in range(1000):
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
