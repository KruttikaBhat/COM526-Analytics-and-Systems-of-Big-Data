import pandas as pd
import math
import numpy as np
import pyfpgrowth

data = pd.read_excel(r"avocado.xlsx")
data = data.sort_values("Total Volume")
binsize=50
size=len(data.index)

for i in range(math.ceil(size / binsize)):
    data.loc[data.index[i * binsize:(i + 1) * binsize],"Mean"] = np.mean(data.iloc[i * binsize:(i + 1) * binsize,3])



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
data = data.replace([0,' ','NULL','na'],np.nan)
data=data.dropna()
data = data.drop_duplicates()
print(data.isnull().sum())

print(data.dtypes)
df1=data[['AveragePrice','Mean', 'type','region']]
df1['AveragePrice']=df1['AveragePrice'].astype(int).astype(str)
df1['Mean']=df1['Mean'].astype(int).astype(str)

print(df1.dtypes)
df=df1.values.tolist()
print(df)

patterns = pyfpgrowth.find_frequent_patterns(df, 10)
rules=pyfpgrowth.generate_association_rules(patterns, 0.7)
for i in rules:
    print(i)
