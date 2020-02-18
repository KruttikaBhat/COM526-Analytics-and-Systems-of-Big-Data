import pandas as pd
import math
import numpy as np

data = pd.read_excel(r"avocado.xlsx")
data = data.sort_values("Total Volume")
binsize=50
size=len(data.index)

for i in range(math.ceil(size / binsize)):
    data.loc[data.index[i * binsize:(i + 1) * binsize],"Mean"] = np.mean(data.iloc[i * binsize:(i + 1) * binsize,3])
    data.loc[data.index[i * binsize:(i + 1) * binsize],"Median"] = np.median(data.iloc[i * binsize:(i + 1) * binsize,3])


print(data.head)
print(data.shape)
Q1=data["Total Volume"].quantile(0.25)
Q3=data["Total Volume"].quantile(0.75)
IQR=Q3-Q1
i=size-1
while(len(data.index)>0.98*size):
    print(len(data.index),0.98*size,i,data.iloc[i,3],Q3 + (1.5 * IQR),Q1 - (1.5 * IQR))
    if(data.iloc[i,3] > (Q3 + (1.5 * IQR)) or data.iloc[i,3] < (Q1 - (1.5 * IQR))):
        data=data.drop(data.index[i])
        print("dropped")
        print(len(data.index))
    i=i-1

#data = data[(data["Total Volume"] > (Q1 - 1.5 * IQR)) &( data["Total Volume"]< (Q3 + 1.5 * IQR))]
print(data.shape)

size= len(data.index)
for i in range(math.ceil(size / binsize)):
    print((i+1)*binsize-1)
    min_value=data.iloc[i*binsize,3]
    max_value= data.iloc[(i+1)*binsize-1,3] if (i+1)*binsize<=size else data.iloc[-1,3]
    data.loc[data.index[i * binsize:(i + 1) * binsize],"Bin Boundary"]=data.iloc[i * binsize:(i + 1) * binsize,3].apply(lambda i: min_value if (i-min_value) < (max_value-i) else max_value)

print(data[["Total Volume", "Mean", "Median", "Bin Boundary"]])

"""
data=pd.read_excel(r"avocado.xlsx")

binsize=10000
#noOfBins=math.ceil((data['Total Volume'].max()-data['Total Volume'].min())/binsize)
bins = np.arange(data['Total Volume'].min()-data['Total Volume'].min()%binsize, data['Total Volume'].max()-data['Total Volume'].max()%binsize+binsize, binsize)
#print(bins)

data["bins"]=pd.cut(data['Total Volume'],bins)
data["TotalVolume_Mean"]=data.groupby("bins")["Total Volume"].apply(lambda x:x.mean())
data["TotalVolume_Median"]=data.groupby("bins")["Total Volume"].transform(np.nanmedian)
print(data["bins"].value_counts())
#trim data, remove outliers
print(data.shape)
Q1=data["Total Volume"].quantile(0.25)
Q3=data["Total Volume"].quantile(0.75)
IQR=Q3-Q1
data = data[(data["Total Volume"] > (Q1 - 1.5 * IQR)) &( data["Total Volume"]< (Q3 + 1.5 * IQR))]
print(data.shape)
"""
