import pandas as pd
import statsmodels.api as sm
import pylab as py
import numpy as np

data=pd.read_excel(r"avocado.xlsx")
data = data.replace([' ','NULL','na'],np.nan)
data["AveragePrice"]=data["AveragePrice"].astype(float)

Old=data[(data['year']==2015) | (data['year']==2016)]
New=data[data['year']==2017]
Recent=data[data['year']==2018]
print(Old)
print(New)
print(Recent)


sm.qqplot(Old['AveragePrice'], line ='45')
py.title("Old")
sm.qqplot(New['AveragePrice'], line ='45')
py.title("New")
sm.qqplot(Recent['AveragePrice'], line ='45')
py.title("Recent")
py.show()
