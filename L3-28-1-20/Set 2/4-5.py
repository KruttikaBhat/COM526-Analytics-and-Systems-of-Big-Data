import pandas as pd
import numpy as np

data=pd.read_excel(r"avocado.xlsx")

print(data.dtypes)
data = data.replace([0,' ','NULL','na'],np.nan)
data["AveragePrice"]=data["AveragePrice"].astype(float)
print(data.dtypes)
obj_df = data.select_dtypes(include=['object']).copy()
print(obj_df.head())


for col in obj_df.head():
    obj_df[col]=obj_df[col].astype('category')
    obj_df[col+"_cat"] = obj_df[col].cat.codes
print(obj_df.head())
print(obj_df.dtypes)

data=pd.get_dummies(data, columns=["region"])
print(data.head())
print(data.dtypes)
