import pandas as pd

data=pd.read_excel(r"avocado.xlsx")

print(data.head)
threshold=2016
data['year'] = (data['year'] > threshold).astype(int)
print(data.head)
