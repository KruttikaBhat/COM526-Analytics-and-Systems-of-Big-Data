import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
"""
x=[]
y=[]
n=100
for i in range(n):
    x.append(random.randint(25,50))
    y.append(random.randint(10,50))

#plt.hexbin(x,y)
#plt.xlabel("Age of drivers")
#plt.ylabel("Number of car accidents")
"""
df = pd.DataFrame({'x': np.random.randint(25,50,size=100),'y': np.random.randint(10,50,size=100)})
ax = df.plot.hexbin(x='x', y='y', gridsize=15)
plt.show()
