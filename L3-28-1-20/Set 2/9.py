import numpy as np
import pandas as pd
import math

def gini(array):
    #0 indicates all values are equal, 1 indicates that there's one value that dominates all others
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq:
    # http://www.statsdirect.com/help/generatedimages/equations/equation154.svg
    # from:
    # http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    # All values are treated equally, arrays must be 1d:
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    # Gini coefficient:
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))

def entropy(class0, class1):
	return -(class0 * math.log2(class0) + class1 * math.log2(class1))


data=pd.read_excel(r"avocado.xlsx")
print("Gini Index of Total Volume: "+str(gini(data["Total Volume"].to_numpy())))
print("Gini Index of Total Bags: "+str(gini(data["Total Bags"].to_numpy())))

type=pd.Series(data['type']).value_counts()
one=type["conventional"]/sum(type)
two=type["organic"]/sum(type)
#print(one,two)
s_entropy=entropy(one,two)
print('Dataset Entropy: %.3f bits' % s_entropy)

split=data[data["Total Volume"]<=data["Total Volume"].mean()]
#print(split.shape)
type1=pd.Series(split['type']).value_counts()
one1=type1["conventional"]/sum(type1)
two1=type1["organic"]/sum(type1)
#print(one1,two1)
s1_entropy=entropy(one1,two1)
print('Group1 Entropy: %.3f bits' % s1_entropy)

split2=data[data["Total Volume"]>data["Total Volume"].mean()]
#print(split2.shape)
type2=pd.Series(split2['type']).value_counts()
one2=type2["conventional"]/sum(type2)
two2=type2["organic"]/sum(type2)
#print(one2,two2)
s2_entropy=entropy(one2,two2)
print('Group2 Entropy: %.3f bits' % s2_entropy)

gain = s_entropy - (sum(type1)/sum(type) * s1_entropy + sum(type2)/sum(type) * s2_entropy)
print('Information Gain: %.3f bits' % gain)
