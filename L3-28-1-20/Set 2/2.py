import pandas as pd

data =pd.read_csv("Trail.csv")

print(data.head)
print(data.isnull().sum())

data = data.drop_duplicates()
print('Result DataFrame:\n', data.head)
print(data.isnull().sum())

data['AveragePrice']=data['AveragePrice'].fillna(1.25)
print(data.isnull().sum())
print(data.head)
