import pandas as pd
import numpy as np

data=pd.read_excel(r"avocado.xlsx")
print(data.isnull().sum())
data = data.replace([' ','NULL','na'],np.nan)
print(data.isnull().sum())
print(data.shape)

#data=data.dropna(thresh=10,how='all',axis=1)
data = data.loc[:, data.isnull().sum() < any(data.isnull().sum())]
print(data.isnull().sum())
print(data.shape)
