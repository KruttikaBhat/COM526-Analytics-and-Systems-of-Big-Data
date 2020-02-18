import pandas as pd

data=pd.read_excel(r"avocado.xlsx")
print(data[data['type']=='organic'][["Total Volume",4046,4225,4770]].sort_values("Total Volume"))
