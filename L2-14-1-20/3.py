import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

water=[3.2, 3.5, 3.6, 2.5, 2.8, 5.9, 2.9, 3.9, 4.9, 6.9, 7.9, 8.0, 3.3, 6.6, 4.4]
beverages=[2.2, 2.5, 2.6, 1.5, 3.8, 1.9, 0.9, 3.9, 4.9, 6.9, 0.1, 8.0, 0.3, 2.6, 1.4]

f=plt.figure(1)
sns.distplot(water, hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = 'water')
sns.distplot(beverages,  hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = 'beverages')

[mean,mode,median,stnd]=[np.mean(water),stats.mode(water)[0][0],np.median(water),np.std(water)]
skew=(mean-mode)/stnd

print(mean,median,mode,skew)

[mean,mode,median,stnd]=[np.mean(beverages),stats.mode(beverages)[0][0],np.median(beverages),np.std(beverages)]
skew=(mean-mode)/stnd

print(mean,median,mode,skew)
plt.legend()
plt.xlabel("Avg Consumption(litres)")
plt.ylabel("Density")
#Mean should be the central fulcrum that balances the curve
#Median should be the point which divides the area equally
#Mode is the peak of the curve
#Can be left or right skewed. If Mean is to the right of median then it is right skewed.


f1=plt.figure(2)
sns.rugplot(water, label="water",color="blue")
sns.rugplot(beverages, label="beverages",color="orange")
plt.legend()
plt.xlabel("Avg Consumption(litres)")


plt.show()
