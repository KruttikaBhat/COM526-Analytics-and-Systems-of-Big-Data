import pandas as pd
import numpy as np
data=pd.read_excel(r"avocado.xlsx")

print(data.isnull().sum())
data = data.replace([' ','NULL','na'],np.nan)
print(data.isnull().sum())

data["AveragePrice"]=data["AveragePrice"].astype(float)
data["AveragePrice"] = data.groupby("region")["AveragePrice"].transform(lambda x: x.fillna(x.mean()))
print(data.isnull().sum())
print(data)
