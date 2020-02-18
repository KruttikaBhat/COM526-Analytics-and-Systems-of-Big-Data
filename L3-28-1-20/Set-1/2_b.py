import pandas as pd
import numpy as np
import copy

data=pd.read_excel(r"avocado.xlsx")
data = data.replace([' ','NULL','na'],np.nan)
data["AveragePrice"]=data["AveragePrice"].astype(float)
months=copy.deepcopy(data)
years=copy.deepcopy(data)

months["month"]=pd.DatetimeIndex(months['Date']).month
months=months.groupby(["type","year","month","region"]).sum()
print(months.head)

years=years.groupby(["type","year","region"]).sum()
print(years.head)
