import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_excel(r"avocado.xlsx")
print("Dimension: "+str(data.ndim))
data = data.replace([' ','NULL','na'],np.nan)
data["AveragePrice"]=data["AveragePrice"].astype(float)
print("Most frequently occuring value in each column:")
for col in data.head():
    print(str(col)+": "+str(data[col].value_counts().idxmax()))

print("Data type:")
print(data.dtypes)

print(data.describe())
print("Correlation matrix")
print(data.corr())

print("Skewness:")
print(data.skew())

pd.Series(data['type']).value_counts().plot('bar')
plt.show()
