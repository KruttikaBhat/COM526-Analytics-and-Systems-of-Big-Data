import pandas as pd

data=pd.read_excel(r"avocado.xlsx")
print(data.isnull().sum())
data=data.dropna()
print(data.isnull().sum())
